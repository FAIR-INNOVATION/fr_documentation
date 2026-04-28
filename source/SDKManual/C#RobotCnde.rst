CNDE
=================

.. toctree:: 
    :maxdepth: 5

配置机器人CNDE的数据列表和更新周期
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 配置机器人实时状态反馈的数据列表和更新周期（覆盖之前的配置）
    * @param [in] states 要订阅的状态枚举列表，顺序决定数据包中的排列顺序。
    * @param [in] period 数据更新周期，单位毫秒，取值范围 [8, 1000]
    * @return 成功返回 0；失败返回负错误码（如 ERR_STATE_INVALID、ERR_PARAM_VALUE 等）
    */
    public int SetRobotRealtimeStateConfig(List<RobotState> states, int period)

在现有状态反馈列表中添加一个状态项
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 在现有状态反馈列表中添加一个状态项
    * @param [in] state 要添加的状态枚举值。
    * @return 成功返回 0；失败返回负错误码（如 ERR_STATE_ALREADY_EXISTS、ERR_STATE_INVALID 等）
    */
    public int AddRobotRealtimeState(RobotState state)
    
从现有状态反馈列表中删除一个状态项
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 从现有状态反馈列表中删除一个状态项（至少保留一个状态）
    * @param [in] state 要删除的状态枚举值
    * @return 成功返回 0；失败返回负错误码（如 ERR_STATE_INVALID、ERR_NEED_AT_LEAST_ONE_STATE）
    */
    public int DeleteRobotRealtimeState(RobotState state)
        
仅修改状态反馈的更新周期
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

     /**
    * @brief 仅修改状态反馈的更新周期，不改变状态列表
    * @param [in] period 新的更新周期，单位毫秒，取值范围 [8, 1000]
    * @return 成功返回 0；失败返回负错误码（如 ERR_PARAM_VALUE）
    */
    public int SetRobotRealtimeStatePeriod(int period)
        
获取当前配置的状态反馈列表和更新周期
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取当前配置的状态反馈列表和更新周期
    * @param [out] states 输出当前订阅的状态枚举列表
    * @param [out] period 输出当前数据更新周期，单位毫秒
    * @return 成功返回 0；失败返回负错误码。
    */
    public int GetRobotRealtimeStateConfig(out List<RobotState> states, out int period)

CNDE配置相关的SDK代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private async void TestRobotRealtimeStates()
    {
        // 1. 定义需要订阅的状态字段
        List<RobotState> requiredStates = new List<RobotState>
        {
            RobotState.JointCurPos,
            RobotState.ToolCurPos, 
            RobotState.JointDriverTemperature,
            RobotState.RobotTime,
        };

        // 2. 配置状态反馈（周期 8ms）
        int periodMs = 8;
        int ret = robot.SetRobotRealtimeStateConfig(requiredStates, periodMs);
        if (ret != 0)
        {
            Console.WriteLine($"配置状态失败，错误码: {ret}");
            return;
        }
        Console.WriteLine($"状态配置成功，共 {requiredStates.Count} 个字段，周期 {periodMs} ms");

        // 验证配置是否生效
        List<RobotState> actualStates;
        int actualPeriod;
        robot.GetRobotRealtimeStateConfig(out actualStates, out actualPeriod);
        Console.WriteLine($"实际生效的状态数: {actualStates.Count}, 周期: {actualPeriod} ms");
        Thread.Sleep(3000);
        // 3. 建立 RPC 连接（内部自动完成 CNDE 握手）
        robot.SetReconnectParam(true, 10, 1000);
        ret = robot.RPC("192.168.58.2");  // 请根据实际机器人 IP 修改
        if (ret != 0)
        {
            Console.WriteLine($"RPC 连接失败，错误码: {ret}");
            return;
        }
        // 4. 循环读取并打印状态数据
        DateTime startTime = DateTime.Now;
        const int durationSeconds = 500;

        while ((DateTime.Now - startTime).TotalSeconds < durationSeconds)
        {
            ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
            ret = robot.GetRobotRealTimeState(ref pkg);
            Console.WriteLine($"GetRobotRealTimeState: {ret}");

            //关节位置（度）
            if (pkg.jt_cur_pos != null && pkg.jt_cur_pos.Length >= 6)
                Console.WriteLine($"关节位置(°): J1={pkg.jt_cur_pos[0]:F2}, J2={pkg.jt_cur_pos[1]:F2}, J3={pkg.jt_cur_pos[2]:F2}, J4={pkg.jt_cur_pos[3]:F2}, J5={pkg.jt_cur_pos[4]:F2}, J6={pkg.jt_cur_pos[5]:F2}");

            //TCP 位姿（mm /°）
            if (pkg.tl_cur_pos != null && pkg.tl_cur_pos.Length >= 6)
                Console.WriteLine($"TCP位姿(mm/°): X={pkg.tl_cur_pos[0]:F2}, Y={pkg.tl_cur_pos[1]:F2}, Z={pkg.tl_cur_pos[2]:F2}, RX={pkg.tl_cur_pos[3]:F2}, RY={pkg.tl_cur_pos[4]:F2}, RZ={pkg.tl_cur_pos[5]:F2}");
    
            // 关节温度
            if (pkg.jointDriverTemperature != null && pkg.jointDriverTemperature.Length >= 6)
                Console.WriteLine($"关节温度(°C): J1={pkg.jointDriverTemperature[0]:F2}, J2={pkg.jointDriverTemperature[1]:F2}, J3={pkg.jointDriverTemperature[2]:F2}, J4={pkg.jointDriverTemperature[3]:F2}, J5={pkg.jointDriverTemperature[4]:F2}, J6={pkg.jointDriverTemperature[5]:F2}");

            // 机器人时间
            Console.WriteLine($"机器人时间: {pkg.robotTime.year}-{pkg.robotTime.mouth:D2}-{pkg.robotTime.day:D2} {pkg.robotTime.hour:D2}:{pkg.robotTime.minute:D2}:{pkg.robotTime.second:D2}.{pkg.robotTime.millisecond:D3}");

            await Task.Delay(100);
        }

        // 5. 断开连接
        robot.CloseRPC();
    }

CNDE增删配置状态及设置通信周期的SDK代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private async void TestAddDeleteCNDE()
    {
        List<RobotState> finalStates;
        int finalPeriod;
        // 初始配置：不请求任何状态（默认配置）
        List<RobotState> emptyStates = new List<RobotState>();
        int ret = robot.SetRobotRealtimeStateConfig(emptyStates, 20);

        robot.SetRobotRealtimeStatePeriod(10);
        // 删除两个状态
        ret = robot.DeleteRobotRealtimeState(RobotState.JointCurPos);
        Console.WriteLine($"删除 JointCurPos 结果: {ret}");
        ret = robot.DeleteRobotRealtimeState(RobotState.ToolCurPos);
        Console.WriteLine($"删除 ToolCurPos 结果: {ret}");
        // 新增一个状态
        ret = robot.AddRobotRealtimeState(RobotState.CollisionLevel);
        Console.WriteLine($"新增 CollisionLevel 结果: {ret}");

        // 获取当前配置列表并重新发送
        List<RobotState> currentStates;
        int currentPeriod;
        robot.GetRobotRealtimeStateConfig(out currentStates, out currentPeriod);
        Console.WriteLine($"当前配置状态数: {currentStates.Count}");
        ret = robot.SetRobotRealtimeStateConfig(currentStates, currentPeriod);
        Console.WriteLine($"应用新配置结果: {ret}"); Console.WriteLine($"初始配置结果: {ret}");
        robot.GetRobotRealtimeStateConfig(out finalStates, out finalPeriod);
        Console.WriteLine($"配置状态数量: {finalStates.Count}");
        foreach (var s in finalStates) Console.WriteLine($"  {s}");
        Console.WriteLine($"周期: {finalPeriod} ms");

        Thread.Sleep(1000);
        //  建立 RPC 连接（内部自动连接 CNDE）
        robot.SetReconnectParam(true, 100, 1000);
        ret = robot.RPC("192.168.58.2");
        if (ret != 0)
        {
            Console.WriteLine($"RPC 连接失败: {ret}");
            return;
        }

        // 循环打印删除和新增的状态，删除的状态打印为0，新增的状态可正常获取实时值
        DateTime lastTime = DateTime.Now;
        int frameCount = 0;
        DateTime startTime = DateTime.Now;
        while ((DateTime.Now - startTime).TotalSeconds < 10)
        {
            ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
            robot.GetRobotRealTimeState(ref pkg);
            DateTime now = DateTime.Now;
            double interval = (now - lastTime).TotalMilliseconds;
            lastTime = now;
            frameCount++;

            if (pkg.jt_cur_pos != null && pkg.jt_cur_pos.Length >= 6)
            {
                Console.WriteLine($"  关节位置(°): J1={pkg.jt_cur_pos[0]:F2}, J2={pkg.jt_cur_pos[1]:F2}, J3={pkg.jt_cur_pos[2]:F2}, J4={pkg.jt_cur_pos[3]:F2}, J5={pkg.jt_cur_pos[4]:F2}, J6={pkg.jt_cur_pos[5]:F2}");
            }
            if (pkg.tl_cur_pos != null && pkg.tl_cur_pos.Length >= 6)
            {
                Console.WriteLine($"  TCP位姿(mm/°): X={pkg.tl_cur_pos[0]:F2}, Y={pkg.tl_cur_pos[1]:F2}, Z={pkg.tl_cur_pos[2]:F2}, RX={pkg.tl_cur_pos[3]:F2}, RY={pkg.tl_cur_pos[4]:F2}, RZ={pkg.tl_cur_pos[5]:F2}");
            }
            // 碰撞等级
            if (pkg.collisionLevel != null && pkg.collisionLevel.Length >= 6)
                Console.WriteLine($"碰撞等级: J1={pkg.collisionLevel[0]}, J2={pkg.collisionLevel[1]}, J3={pkg.collisionLevel[2]}, J4={pkg.collisionLevel[3]}, J5={pkg.collisionLevel[4]}, J6={pkg.collisionLevel[5]}");

            await Task.Delay(50);
        }
        //断开连接
        robot.CloseRPC();
        Console.WriteLine("测试完成。");
    }