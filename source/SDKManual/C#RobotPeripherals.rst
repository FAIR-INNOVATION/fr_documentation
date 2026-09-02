机器人外设
============

.. toctree:: 
    :maxdepth: 5

配置夹爪
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  配置夹爪
    * @param  [in] company  夹爪厂商，待定
    * @param  [in] device  设备号，暂不使用，默认为0
    * @param  [in] softvesion  软件版本号，暂不使用，默认为0
    * @param  [in] bus 设备挂在末端总线位置，暂不使用，默认为0
    * @return  错误码
    */
    int SetGripperConfig(int company, int device, int softvesion, int bus);

获取夹爪配置
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取夹爪配置
    * @param  [in] company  夹爪厂商，待定
    * @param  [in] device  设备号，暂不使用，默认为0
    * @param  [in] softvesion  软件版本号，暂不使用，默认为0
    * @param  [in] bus 设备挂在末端总线位置，暂不使用，默认为0
    * @return  错误码
    */
    int GetGripperConfig(int *company, int *device, int *softvesion, int *bus);

激活夹爪
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  激活夹爪
    * @param  [in] index  夹爪编号
    * @param  [in] act  0-复位，1-激活
    * @return  错误码
    */
    int ActGripper(int index, byte act); 

控制夹爪
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  控制夹爪
    * @param  [in] index  夹爪编号
    * @param  [in] pos  位置百分比，范围[0~100]
    * @param  [in] vel  速度百分比，范围[0~100]
    * @param  [in] force  力矩百分比，范围[0~100]
    * @param  [in] max_time  最大等待时间，范围[0~30000]，单位ms
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [in] type 夹爪类型，0-平行夹爪；1-旋转夹爪
    * @param  [in] rotNum 旋转圈数
    * @param  [in] rotVel 旋转速度百分比[0-100]
    * @param  [in] rotTorque 旋转力矩百分比[0-100]
    * @return  错误码
    */
    int MoveGripper(int index, int pos, int vel, int force, int max_time, byte block, int type, double rotNum, int rotVel, int rotTorque);

获取夹爪运动状态
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取夹爪运动状态(仅末端开放协议定义，已适配设备获取的运动状态为透传值)
    * @param  [out] fault  0-无错误，其他-有错误
    * @param  [out] staus  0-运动未完成，1-运动完成未检测到物体 2-运动完成检测到物体
    * @return  错误码
    */
    int GetGripperMotionDone(ref int fault, ref int status); 

获取夹爪激活状态
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取夹爪激活状态
    * @param  [out] fault  0-无错误，1-有错误
    * @param  [out] status  bit0~bit15对应夹爪编号0~15，bit=0为未激活，bit=1为激活
    * @return  错误码
    */
    int GetGripperActivateStatus(ref int fault, ref int status);

等待夹爪运动状态
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  等待夹爪运动状态（仅末端开放协议定义，已适配设备status定义透传各夹爪厂商）
    * @param  [in]  staus  0-运动未完成，1-运动完成未检测到物体 2-运动完成检测到物体
    * @param  [in] timeout 超时时间（ms） -1永久等待
    * @param  [in] strategy  0-停止报错，1-继续运行
    * @param  [in] type  0-平行夹爪，1-旋转夹爪
    * @return  错误码
    */
    public int GripperWaitMotionDone(int staus, int timeout, int strategy, int type) 
    
等待夹爪运动状态代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public void TestGripperWaitMotionDone()
    {
        int rtn;
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();


        // 夹爪张开
        rtn = robot.MoveGripper(1, 50, 50, 100, 30000, 0, 0, 0, 0, 0);
        Console.WriteLine("MoveGripper(张开) ret={0}", rtn);
        Thread.Sleep(2000);
        robot.GetRobotRealTimeState(ref pkg);
        Console.WriteLine(" gripper_motiondone {0})", pkg.gripper_motiondone);
        // 夹爪闭合
        rtn = robot.MoveGripper(1, 90, 100, 100, 30000, 0, 0, 0, 0, 0);
        Console.WriteLine("MoveGripper(闭合) ret={0}", rtn);
        Thread.Sleep(2000);
        robot.GetRobotRealTimeState(ref pkg);
        Console.WriteLine(" gripper_motiondone {0}", pkg.gripper_motiondone);
        // 等待运动完成未检测到物体，超时30s，停止报错
        rtn = robot.GripperWaitMotionDone(2, -1, 0, 0);
        Console.WriteLine("GripperWaitMotionDone(等待完成未检测到物体) ret={0}", rtn);

        // 夹爪张开
        rtn = robot.MoveGripper(1, 0, 100, 100, 30000, 0, 0, 0, 0, 0);
        Console.WriteLine("MoveGripper(张开) ret={0}", rtn);
    }

获取夹爪位置
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取夹爪位置
    * @param  [out] fault  0-无错误，1-有错误
    * @param  [out] position  位置百分比，范围0~100%
    * @return  错误码
    */
    int GetGripperCurPosition(ref int fault, ref int position);

获取夹爪速度
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取夹爪速度
    * @param  [out] fault  0-无错误，1-有错误
    * @param  [out] speed  速度百分比，范围0~100%
    * @return  错误码
    */
    int GetGripperCurSpeed(ref int fault, ref int speed);
     
获取夹爪电流
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取夹爪电流
    * @param  [out] fault  0-无错误，1-有错误
    * @param  [out] current  电流百分比，范围0~100%
    * @return  错误码
    */
    int GetGripperCurCurrent(ref int fault, ref int current);

获取夹爪电压
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取夹爪电压
    * @param  [out] fault  0-无错误，1-有错误
    * @param  [out] voltage  电压,单位0.1V
    * @return  错误码
    */
    int GetGripperVoltage(ref int fault, ref int voltage);

获取夹爪温度
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取夹爪温度
    * @param  [out] fault  0-无错误，1-有错误
    * @param  [out] temp  温度，单位℃
    * @return  错误码
    */
    int GetGripperTemp(ref int fault, ref int temp);

计算预抓取点-视觉
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 计算预抓取点-视觉 
    * @param [in] desc_pos 抓取点笛卡尔位姿 
    * @param [in] zlength z轴偏移量 
    * @param [in] zangle 绕z轴旋转偏移量
    * @param [out] pre_pos 预抓取点
    * @return 错误码 
    */ 
    int ComputePrePick(DescPose desc_pos, double zlength, double zangle, ref DescPose pre_pos);

计算撤退点-视觉
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 计算撤退点-视觉 
    * @param [in] desc_pos 撤退点笛卡尔位姿 
    * @param [in] zlength z轴偏移量 
    * @param [in] zangle 绕z轴旋转偏移量
    * @param [out] post_pos 撤退点
    * @return 错误码 
    */ 
    int ComputePostPick(DescPose desc_pos, double zlength, double zangle, ref DescPose post_pos);

机器人夹爪操作代码示例
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button36_Click(object sender, EventArgs e)
    {
        int company = 4;
        int device = 0;
        int softversion = 0;
        int bus = 2;
        int index = 2;
        byte act = 0;
        int max_time = 30000;
        byte block = 0;
        int status=0;
        int fault=0;
        int active_status = 0;
        int current_pos = 0;
        int current = 0;
        int voltage = 0;
        int temp = 0;
        int speed = 0;

        robot.SetGripperConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.GetGripperConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine("gripper config:{0},{1},{2},{3}\n", company, device, softversion, bus);

        robot.ActGripper(index, act);
        Thread.Sleep(1000);
        act = 1;
        robot.ActGripper(index, act);
        Thread.Sleep(1000);

        robot.MoveGripper(index, 90, 50, 50, max_time, block, 0, 0, 0, 0);
        Thread.Sleep(1000);
        robot.MoveGripper(index, 30, 50, 0, max_time, block, 0, 0, 0, 0);

        robot.GetGripperMotionDone(ref fault, ref status);
        Console.WriteLine("motion status:{0},{1}\n", fault, status);

        robot.GetGripperActivateStatus(ref fault, ref active_status);
        Console.WriteLine("gripper active fault is: {0}, status is: {1}\n", fault, active_status);

        robot.GetGripperCurPosition(ref fault, ref current_pos);
        Console.WriteLine("fault is:{0}, current position is: {1}\n", fault, current_pos);

        robot.GetGripperCurCurrent(ref fault, ref current);
        Console.WriteLine("fault is:{0}, current current is: {1}\n", fault, current);

        robot.GetGripperVoltage(ref fault, ref voltage);
        Console.WriteLine("fault is:{0}, current voltage is: {1} \n", fault, voltage);

        robot.GetGripperTemp(ref fault, ref temp);
        Console.WriteLine("fault is:{0}, current temperature is: {1}\n", fault, temp);

        robot.GetGripperCurSpeed(ref fault, ref speed);
        Console.WriteLine("fault is:{0}, current speed is: {1}\n", fault, speed);

        int retval = 0;
        DescPose prepick_pose = new DescPose();
        DescPose postpick_pose = new DescPose();

        DescPose p1Desc = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose p2Desc = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);

        retval = robot.ComputePrePick(p1Desc, 10, 0, ref prepick_pose);
        Console.WriteLine("ComputePrePick retval is: {0}\n", retval);
        Console.WriteLine("xyz is: {0}, {1}, {2}; rpy is: {3}, {4}, {5}\n",
            prepick_pose.tran.x, prepick_pose.tran.y, prepick_pose.tran.z,
            prepick_pose.rpy.rx, prepick_pose.rpy.ry, prepick_pose.rpy.rz);

        retval = robot.ComputePostPick( p2Desc, -10, 0, ref postpick_pose);
        Console.WriteLine("ComputePostPick retval is: {0}\n", retval);
        Console.WriteLine("xyz is: {0}, {1}, {2}; rpy is: {3}, {4}, {5}\n",
            postpick_pose.tran.x, postpick_pose.tran.y, postpick_pose.tran.z,
            postpick_pose.rpy.rx, postpick_pose.rpy.ry, postpick_pose.rpy.rz);

    }

获取旋转夹爪的旋转圈数
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取旋转夹爪的旋转圈数
    * @param  [out] fault  0-无错误，1-有错误
    * @param  [out] num  旋转圈数
    * @return  错误码
    */
    int GetGripperRotNum(ref UInt16 fault, ref double num);

获取旋转夹爪的旋转速度百分比
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取旋转夹爪的旋转速度百分比
    * @param  [out] fault  0-无错误，1-有错误
    * @param  [out] speed  旋转速度百分比
    * @return  错误码
    */
    int GetGripperRotSpeed(ref UInt16 fault, ref int speed);

获取旋转夹爪的旋转力矩百分比
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取旋转夹爪的旋转力矩百分比
    * @param  [out] fault  0-无错误，1-有错误
    * @param  [out] torque  旋转力矩百分比
    * @return  错误码
    */
    int GetGripperRotTorque(ref UInt16 fault, ref int torque);

获取旋转夹爪状态代码示例
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    int MoveRotGripper(int pos, double rotPos)
    {
        robot.ResetAllError();
        robot.ActGripper(1, 1);
        Thread.Sleep(1000);
        int rtn = robot.MoveGripper(1, pos, 50, 50, 5000, 1, 1, rotPos, 50, 100);
        Console.WriteLine($"move gripper rtn is {rtn}" );
        UInt16 fault = 0;
        double rotNum = 0.0;
        int rotSpeed = 0;
        int rotTorque = 0;
        robot.GetGripperRotNum(ref fault, ref rotNum);
        robot.GetGripperRotSpeed(ref fault, ref rotSpeed);
        robot.GetGripperRotTorque(ref fault, ref rotTorque);
        Console.WriteLine($"gripper rot num :{ rotNum}, gripper rotSpeed :{rotSpeed}, gripper rotTorque : { rotTorque}");
        return 0;
    }

传动带启动、停止
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 传动带启动、停止 
    * @param [in] status 状态，1-启动，0-停止
    * @return 错误码 
    */ 
    int ConveyorStartEnd(byte status); 

记录IO检测点
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 记录IO检测点 
    * @return 错误码 
    */ 
    int ConveyorPointIORecord(); 

记录A点
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 记录A点 
    * @return 错误码 
    */ 
    int ConveyorPointARecord();

记录参考点
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 记录参考点 
    * @return 错误码 
    */ 
    int ConveyorRefPointRecord(); 

记录B点
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 记录B点 
    * @return 错误码 
    */ 
    int ConveyorPointBRecord();

传送带工件IO检测
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 传送带工件IO检测 
    * @param [in] max_t 最大检测时间，单位ms
    * @return 错误码 
    */ 
    int ConveyorIODetect(int max_t);

获取物体当前位置
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取物体当前位置 
    * @param [in] mode 1-跟踪抓取，2-跟踪运动，3-TPD跟踪
    * @return 错误码 
    */ 
    int ConveyorGetTrackData(int mode);

传动带跟踪开始
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 传动带跟踪开始 
    * @param [in] status 状态，1-启动，0-停止
    * @return 错误码 
    */
    int ConveyorTrackStart(byte status);

传动带跟踪停止
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 传动带跟踪停止 
    * @return 错误码 
    */
    int ConveyorTrackEnd();

传送带原地跟踪参数配置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  传送带原地跟踪参数配置
    * @param  [in] trackMode 0-时间；1-距离；2-时间和距离任意满足一个
    * @param  [in] trackTime 跟踪时间，单位s
    * @param  [in] trackDis 跟踪距离
    * @return  错误码
    */
    public int SetStationaryTrackPara(int trackMode, double trackTime, int trackDis)
    
等待原地空运动完成
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 等待原地空运动完成
    * @return 错误码
    */
    public int WaitStationaryMotionDone()
        
传送带原地跟踪运动代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public int TestStationaryTrack()
    {
        Console.WriteLine("\n========== Stationary Track Test ==========");

        int rtn;

        JointPos j1 = new JointPos(-35.146, -102.684, 120.805, -100.401, -90.295, 150.105);
        DescPose d1 = new DescPose(-121.814, -348.341, 209.978, -173.152, -3.585, -5.446);

        ExaxisPos ex = new ExaxisPos(0, 0, 0, 0);
        DescPose zeroOff = new DescPose(0, 0, 0, 0, 0, 0);

        int tool = 1;
        int workpiece = 1;

        rtn = robot.ConveyorSetParam(0, 10000, 200, 0, 0, 10);

        robot.MoveJ(j1, d1, tool, workpiece, 100, 100, 100, ex, -1, 0, zeroOff);

        // Step 1: SetDO control signal ON
        Console.WriteLine("--- Step 1: SetDO(6,1) ---");
        rtn = robot.SetDO(6, 1, 0, 0);
        Console.WriteLine("  SetDO(6,1) rtn={0}", rtn);

        // Step 2: Conveyor tracking start
        Console.WriteLine("--- Step 2: ConveyorTrackStart(2) ---");
        rtn = robot.ConveyorTrackStart(2);
        Console.WriteLine("  ConveyorTrackStart(2) rtn={0}", rtn);

        // Step 3: Workpiece IO detect
        Console.WriteLine("--- Step 3: ConveyorIODetect(10000) ---");
        rtn = robot.ConveyorIODetect(10000);
        Console.WriteLine("  ConveyorIODetect(10000) rtn={0}", rtn);

        // Step 4: Get track data
        Console.WriteLine("--- Step 4: ConveyorGetTrackData(2) ---");
        rtn = robot.ConveyorGetTrackData(2);
        Console.WriteLine("  ConveyorGetTrackData(2) rtn={0}", rtn);

        // Step 5: Set stationary track parameters (time mode, 200s, distance 5)
        Console.WriteLine("--- Step 5: SetStationaryTrackPara(0,200,5) ---");
        rtn = robot.SetStationaryTrackPara(0, 5, 5);
        Console.WriteLine("  SetStationaryTrackPara(0,200,5) rtn={0}", rtn);

        // Step 6: Execute stationary motion
        Console.WriteLine("--- Step 6: MoveStationary() ---");
        rtn = robot.MoveStationary();
        Console.WriteLine("  MoveStationary() rtn={0}", rtn);

        // Step 7: Wait for stationary motion done
        Console.WriteLine("--- Step 7: WaitStationaryMotionDone() ---");
        rtn = robot.WaitStationaryMotionDone();
        Console.WriteLine("  WaitStationaryMotionDone() rtn={0}", rtn);

        // Step 8: Conveyor tracking end
        Console.WriteLine("--- Step 8: ConveyorTrackEnd() ---");
        rtn = robot.ConveyorTrackEnd();
        Console.WriteLine("  ConveyorTrackEnd() rtn={0}", rtn);

        // Step 9: SetDO control signal OFF
        Console.WriteLine("--- Step 9: SetDO(6,0) ---");
        rtn = robot.SetDO(6, 0, 0, 0);
        Console.WriteLine("  SetDO(6,0) rtn={0}", rtn);

        Console.WriteLine("\n========== Stationary Track Test Complete ==========");
        return 0;
    }

传动带参数配置
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 传动带参数配置
    * @param [in] para[0] 编码器通道 1~2
    * @param [in] para[1] 编码器转一圈的脉冲数
    * @param [in] para[2] 编码器转一圈传送带行走距离
    * @param [in] para[3] 工件坐标系编号 针对跟踪运动功能选择工件坐标系编号，跟踪抓取、TPD跟踪设为0
    * @param [in] para[4] 是否配视觉  0 不配  1 配
    * @param [in] para[5] 速度比  针对传送带跟踪抓取选项（1-100）  其他选项默认为1 
    * @return 错误码
    */
    int ConveyorSetParam(int encChannel, int resolution, double lead, int wpAxis, int vision, double speedRadio, int followType, int startDis=0, int endDis=100);

设置传动带抓取点补偿
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置传动带抓取点补偿 
    * @param [in] cmp 补偿位置 double[3]{x, y, z}
    * @return 错误码 
    */
    int ConveyorCatchPointComp(double[] cmp);

传送带跟踪直线运动
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 传送带跟踪直线运动 
    * @param [in] name 运动点名称
    * @param [in] tool 工具坐标号，范围[0~14] 
    * @param [in] wobj 工件坐标号，范围[0~14] 
    * @param [in] vel 速度百分比，范围[0~100] 
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放 
    * @param [in] ovl 速度缩放因子，范围[0~100] 
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm  
    * @return 错误码 
    */
    int ConveyorTrackMoveL(string name, int tool, int wobj, float vel, float acc, float ovl, float blendR);

传送带通讯输入检测
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 传送带通讯输入检测
    * @param [in] timeout 等待超时时间ms
    * @return 错误码
    */
    public int ConveyorComDetect(int timeout)

传送带通讯输入检测触发
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 传送带通讯输入检测触发
    * @return 错误码
    */
    int ConveyorComDetectTrigger();

传送带通讯输入检测触发示例程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button3_Click(object sender, EventArgs e)
    {

        // 禁用按钮防止重复点击
        button3.Enabled = false;

        // 在后台线程中执行耗时操作
        Thread conveyorThread = new Thread(ConveyorTest);
        conveyorThread.IsBackground = true;
        conveyorThread.Start();
    }

    private void button4_Click(object sender, EventArgs e)
    {
        // 获取用户输入
        string input = texBox.Text;
        Console.WriteLine($"please input a number to trigger:{input}");
    
        int rtn = robot.ConveyorComDetectTrigger();
        Console.WriteLine($"ConveyorComDetectTrigger 返回值: {rtn}");
        
    }

    private void ConveyorTest()
    {
        // 使用Invoke来更新UI线程上的控件
        this.Invoke((MethodInvoker)delegate {
            Console.WriteLine("开始传送带测试...");
        });

        int retval = 0;
        int index = 1;
        int max_time = 30000;
        bool block = false;
        retval = 0;

        /* 传送带抓取流程 */
        DescPose startdescPose = new DescPose(139.176f, 4.717f, 9.088f, -179.999f, -0.004f, -179.990f);
        JointPos startjointPos = new JointPos(-34.129f, -88.062f, 97.839f, -99.780f, -90.003f, -34.140f);

        DescPose homePose = new DescPose(139.177f, 4.717f, 69.084f, -180.000f, -0.004f, -179.989f);
        JointPos homejointPos = new JointPos(-34.129f, -88.618f, 84.039f, -85.423f, -90.003f, -34.140f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        // 移动到安全位置
        retval = robot.MoveL(homejointPos, homePose, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 1, 1);
        Console.WriteLine($"MoveL 到安全位置返回值: {retval}");

        // 传送带检测
        retval = robot.ConveryComDetect(1000 * 10);
        Console.WriteLine($"ConveyorComDetect 返回值: {retval}");

        // 获取跟踪数据
        retval = robot.ConveyorGetTrackData(2);
        Console.WriteLine($"ConveyorGetTrackData 返回值: {retval}");

        // 开始跟踪
        retval = robot.ConveyorTrackStart(2);
        Console.WriteLine($"ConveyorTrackStart 返回值: {retval}");

        // 移动到起始位置
        robot.MoveL(startjointPos, startdescPose, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 1, 1);
        robot.MoveL(startjointPos, startdescPose, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 1, 1);

        // 结束跟踪
        retval = robot.ConveyorTrackEnd();
        Console.WriteLine($"ConveyorTrackEnd 返回值: {retval}");

        // 返回安全位置
        robot.MoveL(homejointPos, homePose, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 1, 1);

        this.Invoke((MethodInvoker)delegate {
            Console.WriteLine("传送带测试完成!");
            button3.Enabled = true;
        });
    }

机器人传送带操作示例程序
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnConvert_Click(object sender, EventArgs e)
    {
        // Conveyor belt tracking
        DescPose pos1 = new DescPose(-354.549, 63.914, 270.176, -179.679, -0.134, 2.468);
        DescPose pos2 = new DescPose(-351.203, -213.393, 351.054, -179.932, -0.508, 2.472);

        double[] cmp = { 0.0, 0.0, 0.0 };
        int rtn = robot.ConveyorCatchPointComp(cmp); // Set conveyor pick-up point compensation
        if (rtn != 0)
        {
            return;
        }
        Console.WriteLine("ConveyorCatchPointComp: rtn  " + rtn);

        rtn = robot.MoveCart(pos1, 1, 0, (float)30.0, (float)180.0, (float)100.0, (float)-1.0, -1);
        Console.WriteLine("MoveCart: rtn  " + rtn);

        rtn = robot.ConveyorIODetect(10000); // Conveyor workpiece I/O detection
        Console.WriteLine("ConveyorIODetect: rtn   " + rtn);

        robot.ConveyorGetTrackData(1); // Configure conveyor tracking for picking
        rtn = robot.ConveyorTrackStart(1); // Start tracking
        Console.WriteLine("ConveyorTrackStart: rtn  " + rtn);

        rtn = robot.ConveyorTrackMoveL("cvrCatchPoint", 1, 0, (float)100.0, (float)0.0, (float)100.0, (float)-1.0, 0, 0);
        Console.WriteLine("ConveyorTrackMoveL: rtn  " + rtn);

        rtn = robot.MoveGripper(2, 30, 60, 30, 30000, 0, 0, 0, 50, 50);
        Console.WriteLine("ConveyorTrackMoveL: rtn  " + rtn);
            

        rtn = robot.ConveyorTrackMoveL("cvrRaisePoint", 1, 0, (float)100.0, (float)0.0, (float)100.0, (float)-1.0, 0, 0);
        Console.WriteLine("ConveyorTrackMoveL: rtn   " + rtn);

        rtn = robot.ConveyorTrackEnd(); // Stop conveyor tracking
        Console.WriteLine("ConveyorTrackEnd: rtn  " + rtn);

        rtn = robot.MoveCart(pos2, 1, 0, (float)30.0, (float)180.0, (float)100.0, (float)-1.0, -1);
        Console.WriteLine("MoveCart: rtn  " + rtn);

        rtn = robot.MoveGripper(2, 100, 60, 30, 30000, 0,0,0,50,50);
        Console.WriteLine("MoveGripper: rtn  " + rtn);

    }

末端传感器配置
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  末端传感器配置
    * @param  [in] idCompany 厂商，18-JUNKONG；25-HUIDE
    * @param  [in] idDevice 类型，0-JUNKONG/RYR6T.V1.0
    * @param  [in] idSoftware 软件版本，0-J1.0/HuiDe1.0(暂未开放)
    * @param  [in] idBus 挂载位置，1-末端1号口；2-末端2号口...8-末端8号口(暂未开放)
    * @return  错误码
    */
    int AxleSensorConfig(int idCompany, int idDevice, int idSoftware, int idBus);

获取末端传感器配置
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取末端传感器配置
    * @param  [out] idCompany 厂商，18-JUNKONG；25-HUIDE
    * @param  [out] idDevice 类型，0-JUNKONG/RYR6T.V1.0
    * @return  错误码
    */
    int AxleSensorConfigGet(ref int idCompany, ref int idDevice);

末端传感器激活
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  末端传感器激活
    * @param  [in] actFlag 0-复位；1-激活
    * @return  错误码
    */
    int AxleSensorActivate(int actFlag);

末端传感器寄存器写入
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  末端传感器寄存器写入
    * @param  [in] devAddr  设备地址编号 0-255
    * @param  [in] regHAddr 寄存器地址高8位
    * @param  [in] regLAddr 寄存器地址低8位
    * @param  [in] regNum  寄存器个数 0-255
    * @param  [in] data1 写入寄存器数值1
    * @param  [in] data2 写入寄存器数值2
    * @param  [in] isNoBlock 0-阻塞；1-非阻塞
    * @return  错误码
    */
     int AxleSensorRegWrite(int devAddr, int regHAddr, int regLAddr, int regNum, int data1, int data2, int isNoBlock);

末端传感器代码示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button2_Click_1(object sender, EventArgs e)
    {
        robot.AxleSensorConfig(18, 0, 0, 1);
        int company = -1;
        int type = -1;
        robot.AxleSensorConfigGet(ref company, ref type);
        Console.WriteLine("company is " + company + ", type is " + type);

        int rtn = robot.AxleSensorActivate(1);
        Console.WriteLine("AxleSensorActivate rtn is " + rtn);

        Thread.Sleep(1000);

        rtn = robot.AxleSensorRegWrite(1, 4, 6, 1, 0, 0, 0);
        Console.WriteLine("AxleSensorRegWrite rtn is " + rtn);   
    }

获取机器人外设协议
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取机器人外设协议
    * @param [out] protocol 机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 错误码 
    */
    int GetExDevProtocol(ref int protocol);

设置机器人外设协议
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置机器人外设协议
    * @param [in] protocol 机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 错误码 
    */
    int SetExDevProtocol(int protocol);

设置机器人外设协议示例程序
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnSetProto_Click(object sender, EventArgs e)
    {
      int protocol = 4096;
      int rtn = robot.SetExDevProtocol(protocol);
      Console.WriteLine("SetExDevProtocol rtn " + rtn);
      rtn = robot.GetExDevProtocol(ref protocol);
      Console.WriteLine("GetExDevProtocol rtn " + rtn + " protocol is: " + protocol);
    }

获取末端通讯参数
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取末端通讯参数
    * @param param 末端通讯参数
    * @return  错误码
    */
    int GetAxleCommunicationParam(ref AxleComParam getParam);

设置末端通讯参数
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置末端通讯参数
    * @param param  末端通讯参数
    * @return  错误码
    */
    int SetAxleCommunicationParam(AxleComParam param);

设置末端文件传输类型
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置末端文件传输类型
    * @param type 1-MCU升级文件；2-LUA文件
    * @return  错误码
    */
    int SetAxleFileType(int type);

设置启用末端LUA执行
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置启用末端LUA执行
    * @param enable 0-不启用；1-启用
    * @return  错误码
    */
    int SetAxleLuaEnable(int enable);

末端LUA文件异常错误恢复
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 末端LUA文件异常错误恢复
    * @param status 0-不恢复；1-恢复
    * @return  错误码
    */
    int SetRecoverAxleLuaErr(int status);

获取末端LUA执行使能状态
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取末端LUA执行使能状态
    * @param [out] status 0-未使能；1-已使能
    * @return  错误码
    */
    int GetAxleLuaEnableStatus(ref int status);

设置末端LUA末端设备启用类型
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置末端LUA末端设备启用类型
    * @param [in] forceSensorEnable 力传感器启用状态，0-不启用；1-启用
    * @param [in] gripperEnable 夹爪启用状态，0-不启用；1-启用
    * @param [in] IOEnable IO设备启用状态，0-不启用；1-启用
    * @param [in] dexhandEnable 灵巧手设备启用状态，0-不启用；1-启用
    * @return  错误码
    */
    public int SetAxleLuaEnableDeviceType(int forceSensorEnable, int gripperEnable, int IOEnable, int dexhandEnable)

获取末端LUA末端设备启用类型
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取末端LUA末端设备启用类型
    * @param [out] forceSensorEnable 力传感器启用状态，0-不启用；1-启用
    * @param [out] gripperEnable 夹爪启用状态，0-不启用；1-启用
    * @param [out] IOEnable IO设备启用状态，0-不启用；1-启用
    * @param [out] dexhandEnable 灵巧手设备启用状态，0-不启用；1-启用
    * @return  错误码
    */
    public int GetAxleLuaEnableDeviceType(ref int forceSensorEnable, ref int gripperEnable, ref int IOEnable, ref int dexhandEnable)

获取当前配置的末端设备
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取当前配置的末端设备
    * @param [out] forceSensorEnable 力传感器启用设备编号 0-未启用；1-启用
    * @param [out] gripperEnable 夹爪启用设备编号，0-不启用；1-启用
    * @param [out] IODeviceEnable IO设备启用设备编号，0-不启用；1-启用
    * @param [out] decHandEnable 灵巧手启用设备编号，0-不启用；1-启用
    * @return  错误码
    */
    public int GetAxleLuaEnableDevice(ref int[] forceSensorEnable, ref int[] gripperEnable, ref int[] IODeviceEnable, ref int[] decHandEnable)

设置启用夹爪动作控制功能
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置启用夹爪动作控制功能
    * @param [in] id 夹爪设备编号
    * @param [in] func func[0]-夹爪使能；func[1]-夹爪初始化；func[2]-位置设置；func[3]-速度设置；func[4]-力矩设置；func[6]-读夹爪状态；
        func[7]-读初始化状态；func[8]-读故障码；func[9]-读位置；func[10]-读速度；func[11]-读力矩; func[12]-旋转夹爪旋转圈数设置； 
        func[13]-旋转夹爪旋转速度设置； func[14]-旋转夹爪旋转力矩设置； func[15]-读旋转夹爪状态；func[16]-读旋转夹爪初始化状态；
        func[17]-读旋转夹爪圈数；func[18]-读旋转夹爪速度；func[19]-读旋转夹爪力矩；func[20]-多轴同步运动设置；func[21]-故障清除指令；
        func[22]-单轴运行状态；func[23]-所有轴运行状态；
    * @return  错误码
    */
    public int SetAxleLuaGripperFunc(int id, int[] func)

获取启用夹爪动作控制功能
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取启用夹爪动作控制功能
    * @param [in] id 夹爪设备编号
    * @param [out] func func[0]-夹爪使能；func[1]-夹爪初始化；func[2]-位置设置；func[3]-速度设置；func[4]-力矩设置；func[6]-读夹爪状态；
        func[7]-读初始化状态；func[8]-读故障码；func[9]-读位置；func[10]-读速度；func[11]-读力矩; func[12]-旋转夹爪旋转圈数设置； 
        func[13]-旋转夹爪旋转速度设置； func[14]-旋转夹爪旋转力矩设置； func[15]-读旋转夹爪状态；func[16]-读旋转夹爪初始化状态；
        func[17]-读旋转夹爪圈数；func[18]-读旋转夹爪速度；func[19]-读旋转夹爪力矩；func[20]-多轴同步运动设置；func[21]-故障清除指令；
        func[22]-单轴运行状态；func[23]-所有轴运行状态；
    * @return  错误码
    */
    public int GetAxleLuaGripperFunc(int id, ref int[] func) 

机器人Ethercat从站文件写入
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 机器人Ethercat从站文件写入
    * @param [in] type 从站文件类型，1-升级从站文件；2-升级从站配置文件
    * @param [in] slaveID 从站号
    * @param [in] fileName 上传文件名
    * @return  错误码
    */
    int SlaveFileWrite(int type, int slaveID, string fileName);

上传末端Lua开放协议文件
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 上传末端Lua开放协议文件
    * @param filePath 本地lua文件路径名 ".../AXLE_LUA_End_DaHuan.lua"
    * @return 错误码 
    */
    int AxleLuaUpload(string filePath);

机器人Ethercat从站进入boot模式
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 机器人Ethercat从站进入boot模式
    * @return  错误码
    */
    int SetSysServoBootMode();

机器人末端LUA文件操作代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button41_Click(object sender, EventArgs e)
    {
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
        robot.AxleLuaUpload("D://zUP/AXLE_LUA_End_JunDuo_V0.4_20260602.lua");

        AxleComParam param = new AxleComParam(7, 8, 1, 0, 5, 3, 1);
        robot.SetAxleCommunicationParam(param);

        AxleComParam getParam = new AxleComParam();
        robot.GetAxleCommunicationParam(ref getParam);
        Console.WriteLine("GetAxleCommunicationParam param is {0} {1} {2} {3} {4} {5} {6}",
            getParam.baudRate, getParam.dataBit, getParam.stopBit, getParam.verify,
            getParam.timeout, getParam.timeoutTimes, getParam.period);

        robot.SetAxleLuaEnable(1);
        int luaEnableStatus = 0;
        robot.GetAxleLuaEnableStatus(ref luaEnableStatus);
        robot.SetAxleLuaEnableDeviceType(0, 1, 0, 0);

        int forceEnable = 0;
        int gripperEnable = 0;
        int ioEnable = 0;
        int dexhandEnable = 0;
        robot.GetAxleLuaEnableDeviceType(ref forceEnable, ref gripperEnable, ref ioEnable, ref dexhandEnable);
        Console.WriteLine("GetAxleLuaEnableDeviceType param is {0} {1} {2}", forceEnable, gripperEnable, ioEnable);

        int[] func = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
        robot.SetAxleLuaGripperFunc(1, func);

        int[] getFunc = new int[32];
        robot.GetAxleLuaGripperFunc(1, ref getFunc);
        int[] getforceEnable = new int[16];
        int[] getgripperEnable = new int[16];
        int[] getioEnable = new int[16];
        int[] dexhandEnable1 = new int[16];
        robot.GetAxleLuaEnableDevice(ref getforceEnable, ref getgripperEnable, ref getioEnable,ref dexhandEnable1);
        Console.WriteLine("\ngetforceEnable status : ");
        foreach (int i in getforceEnable)
        {
            Console.Write(i + ",");
        }
        Console.WriteLine("\ngetgripperEnable status : ");
        foreach (int i in getgripperEnable)
        {
            Console.Write(i + ",");
        }
        Console.WriteLine("\ngetioEnable status : ");
        foreach (int i in getioEnable)
        {
            Console.Write(i + ",");
        }
        Console.WriteLine();
        robot.ActGripper(1, 0);
        Thread.Sleep(3000);
        robot.ActGripper(1, 1);
        Thread.Sleep(4000);
        robot.MoveGripper(1, 50, 10, 100, 50000, 0, 0, 0, 0, 0);
        int pos = 0;
        while (true)
        {
            robot.GetRobotRealTimeState(ref pkg);
            Console.WriteLine("gripper pos is " + pkg.gripper_position);
            Thread.Sleep(100);
        }
    } 

获取SmartTool按钮状态
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取SmartTool按钮状态
    * @param [out] state SmartTool手柄按钮状态;(bit0:0-通信正常；1-通信掉线；bit1-撤销操作；bit2-清空程序；
        bit3-A键；bit4-B键；bit5-C键；bit6-D键；bit7-E键；bit8-IO键；bit9-手自动；bit10开始)
    * @return 错误码
    */
    int GetSmarttoolBtnState(ref int state);

代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    private void button11_Click(object sender, EventArgs e)
    {

        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
        int state = 0;
        while (true)
        {
            int rtn = robot.GetSmarttoolBtnState(ref state);
            string binaryString = Convert.ToString(state, 2).PadLeft(32, '0');
            Console.WriteLine($"GetSmarttoolBtnState rtn (binary): {binaryString}");
            Thread.Sleep(100);
        }

    }

上传开放协议的Lua文件
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief 上传开放协议的Lua文件
    * @param  filePath 本地开放协议lua文件路径名
    * @return 错误码
    */
    public int OpenLuaUpload(string filePath)


获取从站板卡参数
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  获取从站板卡参数
    * @param  type  0-Ethercat，1-CClink, 3-Ethercat, 4-EIP
    * @param  version  协议版本
    * @param  connState  0-未连接 1-已连接
    * @return  错误码
    */
    public int GetFieldBusConfig(int[] type, int[] version, int[] connState)

写入从站DO
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  写入从站DO
    * @param   DOIndex  DO编号
    * @param   wirteNum  写入的数量
    * @param   status 写入的数值，最多写8个
    * @return  错误码
    */
    public int FieldBusSlaveWriteDO(int DOIndex, int wirteNum, int[] status)

写入从站AO
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  写入从站AO
    * @param [in] AOIndex AO编号
    * @param [in] wirteNum 写入数量
    * @param [in] status 写入数值数组（最多8个）,AO0~AO15为整型，AO16~AO31为浮点
    * @return 错误码
    */
    public int FieldBusSlaveWriteAO(int AOIndex, int wirteNum, double[] status)

读取从站DI
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  读取从站DI
    * @param  DOIndex  DI编号
    * @param  readNum  读取的数量
    * @param  status 读取到的数值，最多读8个
    * @return  错误码
    */
    public int FieldBusSlaveReadDI(int DOIndex, int readNum, int[] status)

读取从站AI
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  读取从站AI
    * @param  AIIndex  AI编号
    * @param  readNum  读取的数量
    * @param  status 读取到的数值，最多读8个
    * @return  错误码
    */
    public int FieldBusSlaveReadAI(int AIIndex, int readNum, double[] status)

等待扩展DI输入
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief 等待扩展DI输入
    * @param  DIIndex DI编号
    * @param  status 0-低电平；1-高电平
    * @param  waitMs 最大等待时间(ms)
    * @return 错误码
    */
    public int FieldBusSlaveWaitDI(int DIIndex, int status, int waitMs)

等待扩展AI输入
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief 等待扩展AI输入
    * @param  AIIndex AI编号
    * @param  waitType 0-大于；1-小于
    * @param  value AI值
    * @param  waitMs 最大等待时间(ms)
    * @return 错误码
    */
    public int FieldBusSlaveWaitAI(int AIIndex, int waitType, double value, int waitMs)

从站模式相关接口指令代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button101_Click(object sender, EventArgs e)
    {
        int rtn = 0;
    
        int type = 0, version = 0, connState = 0;
        int[] ctrl = new int[8];
        double[] ctrlAO = new double[8];
        int[] DI = new int[8];
        double[] AI = new double[8];
        if (rtn != 0)
        {
            return;
        }
        // Upload and load open protocol file
        robot.OpenLuaUpload("E://temp /CtrlDev_field.lua");
        Thread.Sleep(2000);
        robot.SetCtrlOpenLUAName(3, "CtrlDev_field.lua");
        robot.UnloadCtrlOpenLUA(3);
        robot.LoadCtrlOpenLUA(3);
        Thread.Sleep(8000);
    
        // Get protocol type, software version, and connection status with PLC
        robot.GetFieldBusConfig(ref type, ref version, ref connState);
        Console.WriteLine($"type is {type}, version is {version}, connState is {connState}");
    
        // Write DO0 = 1, DO1 = 0, DO2 = 1
        ctrl[0] = 1;
        ctrl[1] = 0;
        ctrl[2] = 1;
        robot.FieldBusSlaveWriteDO(0, 3, ctrl);
    
        // Write AO2 = 0x1000
        ctrlAO[0] = 0x1000;
        robot.FieldBusSlaveWriteAO(2, 1, ctrlAO);

        for (int i = 0; i < 100; i++)
        {
            robot.FieldBusSlaveReadDI(0, 4, ref DI);
            Console.WriteLine($"DI0 is {DI[0]}, DI1 is {DI[1]}, DI2 is {DI[2]}, DI3 is {DI[3]}");
            robot.FieldBusSlaveReadAI(0, 3, ref AI);
            Console.WriteLine($"AI0 is {AI[0]}, AI1 is {AI[1]}, AI2 is {AI[2]}");
            Thread.Sleep(10);
        }
        int ret = robot.FieldBusSlaveWaitDI(0, 1, 100);
        Console.WriteLine($"FieldBusSlaveWaitDI result is {ret}");

        ret = robot.FieldBusSlaveWaitAI(0, 0, 400.00f, 100);
        Console.WriteLine($"FieldBusSlaveWaitAI result is {ret}"); 
    }

控制阵列式吸盘
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief 控制阵列式吸盘
    * @param  slaveID 从站号
    * @param  len 长度
    * @param  ctrlValue 控制值 1-按最大真空度吸取 2-按设定真空度吸取 3-停止吸取
    * @return 错误码
    */
    public int SetSuckerCtrl(int slaveID, int len, int[] ctrlValue)

获取阵列式吸盘状态
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief 获取阵列式吸盘状态
    * @param  slaveID 从站号
    * @param  state 吸附状态 0-释放物体 1-检测到工件吸附成功 2-没有吸附到物体 3-物体脱离
    * @param  pressValue 当前真空度 单位kpa
    * @param  error 吸盘当前的错误码
    * @return 错误码
    */
    public int GetSuckerState(int slaveID, int[] state, int[] pressValue, int[] error)

等待吸盘状态
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief 等待吸盘状态
    * @param  slaveID 从站号
    * @param  state 吸附状态 0-释放物体 1-检测到工件吸附成功 2-没有吸附到物体 3-物体脱离
    * @param  ms 等待最大时间
    * @return 错误码
    */
    public int WaitSuckerState(int slaveID, int state, int ms)

阵列式吸盘控制指令代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void TestSucker(Robot robot)
    {
    
        int[] ctrl = new int[20];
        int state=0;
        int pressValue=0;
        int error=0;
        int rtn;
    
    
        // Upload and load open protocol file
        robot.OpenLuaUpload(@"C:\SDK\CtrlDev_sucker.lua");
        Thread.Sleep(2000);
        robot.UnloadCtrlOpenLUA(1);
        robot.LoadCtrlOpenLUA(1);
        Thread.Sleep(1000);
    
        // Control sucker in broadcast mode with maximum adsorption capacity
        ctrl[0] = 1;
        robot.SetSuckerCtrl(0, 1, ctrl);
    
        // Monitor states of sucker 1 and sucker 12 in a loop
        for (int i = 0; i < 100; i++)
        {
            robot.GetSuckerState(1, ref state, ref pressValue, ref error);
            Console.WriteLine($"sucker1 state is {state}, pressValue is {pressValue}, error num is {error}");
            robot.GetSuckerState(12, ref state, ref pressValue, ref error);
            Console.WriteLine($"sucker12 state is {state}, pressValue is {pressValue}, error num is {error}");
            Thread.Sleep(100);
        }
        // Wait for sucker 1 to reach adsorbed state, timeout 100ms
        int ret = robot.WaitSuckerState(1, 1, 100);
        Console.WriteLine($"WaitSuckerState result is {ret}");
    
        // Unicast mode to turn off sucker 1 and 12
        ctrl[0] = 3;
        robot.SetSuckerCtrl(1, 1, ctrl);
        robot.SetSuckerCtrl(12, 1, ctrl);
    
        robot.CloseRPC();
    }

激光外设打开关闭函数
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 激光外设打开关闭函数
     * @param [in] OnOff 0-关闭 1-打开
     * @param [in] weldId 焊缝ID 默认为0
     * @return 错误码
     */
    public int LaserTrackingLaserOnOff(int OnOff, int weldId)
    
激光跟踪开始结束函数
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    
    /**
     * @brief 激光跟踪开始结束函数
     * @param [in] OnOff 0-结束 1-开始
     * @param [in] coordId 激光外设工具坐标系编号
     * @return 错误码
     */
    public int LaserTrackingTrackOnOff(int OnOff, int coordId)

激光寻位-固定反向
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 激光寻位-固定反向
     * @param [in] direction 0-x+ 1-x- 2-y+ 3-y- 4-z+ 5-z-
     * @param [in] vel 速度 单位%
     * @param [in] distance 最大寻位距离 单位mm
     * @param [in] timeout 寻位超时时间 单位ms
     * @param [in] posSensorNum 激光标定的工具坐标编号
     * @return 错误码
     */
    public int LaserTrackingSearchStart_xyz(int direction, int vel, int distance, int timeout, int posSensorNum)
    
激光寻位-任意方向
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 激光寻位-任意方向
     * @param [in] directionPoint 寻位输入的点的xyz左边
     * @param [in] vel 速度 单位%
     * @param [in] distance 最大寻位距离 单位mm
     * @param [in] timeout 寻位超时时间 单位ms
     * @param [in] posSensorNum 激光标定的工具坐标编号
     * @return 错误码
     */
    public int LaserTrackingSearchStart_point(DescTran directionPoint, int vel, int distance, int timeout, int posSensorNum)
   
激光寻位结束
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
    * @brief  激光寻位结束
    * @return 错误码
    */
    public int LaserTrackingSearchStop()

激光IP配置
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 激光IP配置
     * @param [in] ip 激光外设的ip地址
     * @param [in] port 激光外设的端口号
     * @return 错误码
     */
    public int LaserTrackingSensorConfig(string ip, int port)

激光外设采样周期配置
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 激光外设采样周期配置
     * @param [in] period 激光外设采样周期 单位ms
     * @return 错误码
     */
    public int LaserTrackingSensorSamplePeriod(int period)

激光外设驱动加载
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 激光外设驱动加载
     * @param [in] type 激光外设驱动的协议类型 101-睿牛 102-创想 103-全视 104-同舟 105-奥太
     * @return 错误码
     */
    public int LoadPosSensorDriver(int type)

激光外设驱动卸载
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 激光外设驱动卸载
     * @return 错误码
     */
    public int UnLoadPosSensorDriver()

激光焊缝轨迹记录
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 激光焊缝轨迹记录
     * @param [in] status 0-停止记录 1-实时跟踪  2-开始记录
     * @param [in] delayTime 延时时间 单位ms
     * @return 错误码
     */
    public int LaserSensorRecord1(int status, int delayTime)

激光焊缝轨迹复现
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 激光焊缝轨迹复现
     * @param [in] delayTime 延时时间 单位ms
     * @param [in] speed 速度 单位%
     * @return 错误码
     */
    public int LaserSensorReplay(int delayTime, double speed)

激光跟踪复现
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 激光跟踪复现
     * @return 错误码
     */
    public int MoveLTR()

激光焊缝轨迹记录及复现
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 激光焊缝轨迹记录及复现
    * @param [in] delayMode 模式 0-延时时间 1-延时距离
    * @param [in] delayTime 延时时间 单位ms
    * @param [in] delayDisExAxisNum 扩展轴编号
    * @param [in] delayDis 延时距离 单位mm
    * @param [in] sensitivePara 补偿灵敏系数
    * @param [in] trackMode 定点跟踪类型。0-扩展轴异步运动；1-机器人
    * @param [in] triggerMode 定点跟踪触发方式。0-跟踪时长；1-IO
    * @param [in] runTime 机器人定点跟踪时长(s)
    * @param [in] speed 速度 单位%
    * @return 错误码
    */
    public int LaserSensorRecordandReplay(int delayMode, int delayTime, int delayDisExAxisNum,double delayDis, double sensitivePara, int trackMode, int triggerMode,double runTime, double speed)
    
运动到焊缝记录的起点
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 运动到焊缝记录的起点
     * @param [in] moveType 0-PTP 1-LIN
     * @param [in] ovl 速度 单位%
     * @return 错误码
     */
    public int MoveToLaserRecordStart(int moveType, double ovl)

运动到焊缝记录的终点
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 运动到焊缝记录的终点
     * @param [in] moveType 0-PTP 1-LIN
     * @param [in] ovl 速度 单位%
     * @return 错误码
     */
    public int MoveToLaserRecordEnd(int moveType, double ovl)

运动到激光传感器寻位点
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 运动到激光传感器寻位点
     * @param [in] moveFlag 运动类型：0-PTP；1-LIN
     * @param [in] ovl 速度缩放因子，0-100
     * @param [in] dataFlag 焊缝缓存数据选择：0-执行规划数据；1-执行记录数据
     * @param [in] plateType 板材类型：0-波纹板；1-瓦楞板；2-围栏板；3-油桶；4-波纹甲壳钢
     * @param [in] trackOffectType 激光传感器偏移类型：0-不偏移；1-基坐标系偏移；2-工具坐标系偏移；3-激光传感器原始数据偏移
     * @param [in] offset 偏移量
     * @return 错误码
     */
    public int MoveToLaserSeamPos(int moveFlag, double ovl, int dataFlag, int plateType, int trackOffectType, DescPose offset)
    
获取激光传感器寻位点坐标信息
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 获取激光传感器寻位点坐标信息
     * @param [in] trackOffectType 激光传感器偏移类型：0-不偏移；1-基坐标系偏移；2-工具坐标系偏移；3-激光传感器原始数据偏移
     * @param [in] offset 偏移量
     * @param [out] jPos 关节位置[°]
     * @param [out] descPos 笛卡尔位置[mm]
     * @param [out] tool 工具坐标系
     * @param [out] user 工件坐标系
     * @param [out] exaxis 扩展轴位置[mm]
     * @return 错误码
     */
    public int GetLaserSeamPos(int trackOffectType, DescPose offset, ref JointPos jPos, ref DescPose descPos, ref int tool, ref int user, ref ExaxisPos exaxis)

激光外设传感器参数配置及调试代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    void testLaserConfig()
    {
        int[] ctrl = new int[20];
        int state;
        int pressValue;
        int error;
        robot.LaserTrackingSensorConfig("192.168.58.20", 5020);
        robot.LaserTrackingSensorSamplePeriod(20);
        robot.LoadPosSensorDriver(101);
        robot.LaserTrackingLaserOnOff(0, 0);
        System.Threading.Thread.Sleep(3000);
        robot.LaserTrackingLaserOnOff(1, 0);
    }

激光轨迹扫描及轨迹复现的代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    void testLaserRecordAndReplay()
    { 
        int[] ctrl = new int[20];
        int state;
        int pressValue;
        int error;
        robot.OpenLuaUpload("D://zUP/CtrlDev_laser_ruiniu-0117.lua");
        System.Threading.Thread.Sleep(2000);
        robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua");
        robot.UnloadCtrlOpenLUA(0);
        robot.LoadCtrlOpenLUA(0);
        System.Threading.Thread.Sleep(8000);
        for (int i=0;i<10;++i)
        {
            JointPos startjointPos = new JointPos(56.205, -117.951, 141.872, -118.149, -94.217, -122.176);
            DescPose startdescPose = new DescPose(-97.552, -282.855, 26.675, 174.182, -1.338, -91.707);
            ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
            DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

            robot.MoveL(startjointPos, startdescPose, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0);
            robot.LaserSensorRecord1(2, 10);

            JointPos endjointPos = new JointPos(68.809, -87.100, 121.120, -127.233, -95.038, -109.555);
            DescPose enddescPose = new DescPose(-103.555, -464.234, 13.076, 174.179, -1.344, -91.709);
            robot.MoveL(endjointPos, enddescPose, 1, 0, 50, 100, 100, -1, exaxisPos, 0, 0, offdese, 0);

            robot.LaserSensorRecord1(0, 10);
            robot.MoveToLaserRecordStart(1, 30);
            robot.LaserSensorReplay(10, 100);
            robot.MoveLTR();
            robot.LaserSensorRecord1(0, 10);
            Console.WriteLine($"Number of completions : {i+1} ");
        }
                
    }

激光寻位及实时跟踪的代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    public static void testLasertrack()
    {
        int[] ctrl = new int[20];
        int state;
        int pressValue;
        int error;
        robot.OpenLuaUpload("D://zUP/CtrlDev_laser_ruiniu-0117.lua");
        System.Threading.Thread.Sleep(2000);
        robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua");
        robot.UnloadCtrlOpenLUA(0);
        robot.LoadCtrlOpenLUA(0);
        System.Threading.Thread.Sleep(8000);
        for (int i = 0; i < 10; ++i)
        {
            JointPos startjointPos = new JointPos(56.205, -117.951, 141.872, -118.149, -94.217, -122.176);
            DescPose startdescPose = new DescPose(-97.552, -282.855, 26.675, 174.182, -1.338, -91.707);
            ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
            DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
            DescTran directionPoint = new DescTran();

            robot.MoveL(startjointPos, startdescPose, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0);
            robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 3);
            robot.LaserTrackingSearchStop();
            robot.MoveToLaserSeamPos(1, 30, 0, 0, 0, offdese);

            robot.LaserTrackingTrackOnOff(1, 3);

            JointPos endjointPos = new JointPos(68.809, -87.100, 121.120, -127.233, -95.038, -109.555);
            DescPose enddescPose = new DescPose(-103.555, -464.234, 13.076, 174.179, -1.344, -91.709);
            robot.MoveL(endjointPos, enddescPose, 1, 0, 20, 100, 100, -1, exaxisPos, 0, 0, offdese, 0);
            robot.LaserTrackingTrackOnOff(0, 3);
            Console.WriteLine($"Number of completions : {i + 1} ");
        }
    }

扩展轴与机器人同步进行激光跟踪的代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    public void TestLaserTrackAndExitAxis()
    {   
        ExaxisPos startexaxisPos = new ExaxisPos(0, 0, 0, 0);
        ExaxisPos seamexaxisPos = new ExaxisPos(-10, 0, 0, 0);
        ExaxisPos endexaxisPos = new ExaxisPos(-30, 0, 0, 0);      
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);     
        JointPos startjointPos = new JointPos(58.337, -119.628, 146.037, -116.358, -92.224, -117.654);
        DescPose startdescPose = new DescPose(-53.375, -255.363, 0.919, 178.054, 1.077, -94.026);
        for (int i=0;i<10;++i)
        {
            robot.ExtAxisSyncMoveJ(startjointPos, startdescPose, 1, 0, 100, 100, 100, startexaxisPos, -1, 0, offdese);
            Console.WriteLine("11111");
            int ret = robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 2);
            robot.LaserTrackingSearchStop();
            Console.WriteLine("2222");
            int tool = 0;
            int user = 0;
            JointPos seamjointPos = new JointPos();
            DescPose seamdescPose = new DescPose();
            robot.GetLaserSeamPos(0, offdese, ref seamjointPos, ref seamdescPose, ref tool, ref user, ref startexaxisPos);
            Console.WriteLine($"{seamjointPos.jPos[0]}, {seamjointPos.jPos[1]}, {seamjointPos.jPos[2]}, " +
                            $"{seamjointPos.jPos[3]}, {seamjointPos.jPos[4]}, {seamjointPos.jPos[5]}, " +
                            $"{seamdescPose.tran.x}, {seamdescPose.tran.y}, {seamdescPose.tran.z}, " +
                            $"{seamdescPose.rpy.rx}, {seamdescPose.rpy.ry}, {seamdescPose.rpy.rz}");
            if (ret == 0)
            {
                robot.ExtAxisSyncMoveJ(seamjointPos, seamdescPose, 1, 0, 100, 100, 100, seamexaxisPos, -1, 0, offdese);
                Console.WriteLine("3333");
                robot.LaserTrackingTrackOnOff(1, 2);
                JointPos endjointPos = new JointPos(70.580, -90.918, 126.593, -125.154, -92.162, -105.403);
                DescPose enddescPose = new DescPose(-53.375, -419.020, 0.920, 178.054, 1.076, -94.026);
                robot.ExtAxisSyncMoveL(endjointPos, enddescPose, 1, 0, 20, 100, 100, -1, endexaxisPos, 0, offdese);
                robot.LaserTrackingTrackOnOff(0, 2);
            }
            Console.WriteLine($"Number of completions : {i + 1} ");
        }     
    }

激光记录复现+常规摆动代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    void TestLaserReproduceNormalWeave()
    {
        JointPos startjointPos = new JointPos(69.655, -71.524, -119.568, -76.454, 91.188, 138.014);
        DescPose startdescPose = new DescPose(214.765, 311.139, 41.255, 7.693, -0.287, 37.080);
        JointPos endjointPos = new JointPos(58.803, -79.528, -113.688, -74.599, 91.637, 127.167);
        DescPose enddescPose = new DescPose(294.942, 311.153, 41.302, 7.701, -0.283, 37.081);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        int rtn = 0;

        // WaitMs(1000)
        Thread.Sleep(1000);

        // MoveL to start position (extended axis 0,174.957,0,0)
        rtn = robot.MoveL(startjointPos, startdescPose, 5, 0, 100, 100, 100, -1, 0, new ExaxisPos(0, 174.957, 0, 0), 0, 0, offdese, 100, 0, 0, 10);

        Console.WriteLine($"MoveL start: {rtn}");

        // Start laser recording
        rtn = robot.LaserSensorRecord1(2, 10);
        Console.WriteLine($"LaserSensorRecord start: {rtn}");

        // MoveL to end position
        rtn = robot.MoveL(endjointPos, enddescPose, 5, 0, 100, 100, 100, -1, 0, new ExaxisPos(0, 174.957, 0, 0), 0, 0, offdese, 100, 0, 0, 10);
        Console.WriteLine($"MoveL end: {rtn}");

        // Stop laser recording
        rtn = robot.LaserSensorRecord1(0, 10);
        Console.WriteLine($"LaserSensorRecord stop: {rtn}");

        // MoveL back to start position
        rtn = robot.MoveL(startjointPos, startdescPose, 5, 0, 100, 100, 100, -1, 0, new ExaxisPos(0, 174.957, 0, 0), 0, 0, offdese, 100, 0, 0, 10);
        Console.WriteLine($"MoveL back: {rtn}");

        // LIN motion to the start of the laser record path
        rtn = robot.MoveToLaserRecordStart(1, 30);
        Console.WriteLine($"MoveToLaserRecordStart: {rtn}");

        // Start normal weaving
        rtn = robot.WeaveStart(0);
        Console.WriteLine($"WeaveStart: {rtn}");

        // Start replay recording
        rtn = robot.LaserSensorRecord1(3, 10);
        Console.WriteLine($"LaserSensorRecord replay: {rtn}");

        // Laser tracking replay motion
        rtn = robot.MoveLTR();
        Console.WriteLine($"MoveLTR: {rtn}");
        Thread.Sleep(3000);

        // Stop replay recording
        rtn = robot.LaserSensorRecord1(0, 10);
        Console.WriteLine($"LaserSensorRecord stop: {rtn}");

        // End normal weaving
        rtn = robot.WeaveEnd(0);
        Console.WriteLine($"WeaveEnd: {rtn}");
    }

激光记录复现 + 扩展轴异步运动 + 定点摆动代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    void TestLaserRecordReplayExaxisWithWave()
    {
        JointPos startjointPos = new JointPos(106.245, -63.397, -93.331, -80.809, 80.389, 134.561);
        DescPose startdescPose = new DescPose(33.534, 516.527, 371.029, 14.712, -31.379, 71.734);
        JointPos endjointPos = new JointPos(105.534, -64.685, -93.681, -79.071, 80.772, 133.952);
        DescPose enddescPose = new DescPose(33.536, 528.536, 364.924, 14.712, -31.379, 71.734);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        int rtn = 0;

        // MoveJ to safe point (extended axis 0,174.957,0,0)
        rtn = robot.MoveJ(startjointPos, startdescPose, 5, 0, 100, 100, 50, new ExaxisPos(0, 174.957, 0, 0), -1, 0, offdese);
        Console.WriteLine($"MoveJ start: {rtn}");

        // Extended axis asynchronous motion to starting point 105.003
        rtn = robot.ExtAxisMove(new ExaxisPos(0, 105.003, 0, 0), 50, -1);
        Console.WriteLine($"ExtAxisMove 105.003: {rtn}");
        Thread.Sleep(3000);

        // MoveL to starting point
        rtn = robot.MoveL(endjointPos, enddescPose, 5, 0, 100, 100, 50, -1, 0, new ExaxisPos(0, 105.003, 0, 0), 0, 0, offdese, 100, 0, 0, 10);
        Console.WriteLine($"MoveL end: {rtn}");

        // Start laser recording
        rtn = robot.LaserSensorRecord1(2, 10);
        Console.WriteLine($"LaserSensorRecord start: {rtn}");

        // Extended axis moves to 174.957 during recording
        rtn = robot.ExtAxisMove(new ExaxisPos(0, 174.957, 0, 0), 50, -1);
        Console.WriteLine($"ExtAxisMove 174.957: {rtn}");
        Thread.Sleep(3000);

        // Stop laser recording
        rtn = robot.LaserSensorRecord1(0, 10);
        Console.WriteLine($"LaserSensorRecord stop: {rtn}");


        // Extended axis returns to 105.003, MoveL back to starting point
        rtn = robot.ExtAxisMove(new ExaxisPos(0, 105.003, 0, 0), 50, -1);
        Console.WriteLine($"ExtAxisMove back: {rtn}");

        // MoveL to starting point
        rtn = robot.MoveL(endjointPos, enddescPose, 5, 0, 100, 100, 50, -1, 0, new ExaxisPos(0, 105.003, 0, 0), 0, 0, offdese, 100, 0, 0, 10);
        Console.WriteLine($"MoveL back: {rtn}");

        // PTP motion to the start of the laser record path
        rtn = robot.MoveToLaserRecordStart(0, 30);
        Console.WriteLine($"MoveToLaserRecordStart: {rtn}");

        // Start replay
        rtn = robot.LaserSensorRecord1(3, 10);
        Console.WriteLine($"LaserSensorRecord replay: {rtn}");

        // Start fixed-point weaving
        DescPose refPoint = new DescPose(61.087, 512.431, 370.523, 14.335, -31.333, 69.014);
        rtn = robot.OriginPointWeaveStart(0, 1, refPoint, 5);
        Console.WriteLine($"OriginPointWeaveStart: {rtn}");

        // Extended axis moves to 174.957 during weaving
        rtn = robot.ExtAxisMove(new ExaxisPos(0, 174.957, 0, 0), 50, -1);
        Console.WriteLine($"ExtAxisMove replay: {rtn}");

        // End weaving
        rtn = robot.OriginPointWeaveEnd();
        Console.WriteLine($"OriginPointWeaveEnd: {rtn}");

        // Stop replay
        rtn = robot.LaserSensorRecord1(0, 10);
        Console.WriteLine($"LaserSensorRecord stop: {rtn}");
    }

末端透传功能打开关闭
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 开启末端通用透传功能
    * @param [in] 使能，0-关闭，1-开启
    * @return 错误码
    */
    public int SetAxleGenComEnable(int mode)

末端透传功能非周期数据收发
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 末端发送非周期数据并等待应答
    * @param [in]  len_snd，发送的长度
    * @param [in]  sndBuff[]，发送数据
    * @param [in]  len_rcv，选择接受的长度
    * @param [out]  rcvBuff[]，应答的数据
    * @return 错误码
    */
    public int SndRcvAxleGenComCmdData(int len_snd, int[] sndBuff, int len_rcv, ref int[] rcvdata)

基于末端透传功能倍益康艾灸头非周期数据通信代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    void testAxleGenCom()
    {
        int[] led_on = new int[6] { 0xAB, 0xBA, 0x12, 0x01, 0x01, 0x79 };
        int[] led_off = new int[6] { 0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78 };
        int[] version = new int[5]{ 0xAB, 0xBA, 0x11, 0x00, 0x76 };
        int[] state = new int[6] { 0xAB, 0xBA, 0x1B,0x01, 0xAA, 0x2B };
        int[] cycleState = new int[6] { 0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78 };

        int[] rcvdata = new int[16];
        int ret = 0;
        int cnt = 1;

        JointPos p1Joint = new JointPos(88.708, -86.178, 140.989, -141.825, -89.162, -49.879);
        DescPose p1Desc = new DescPose(188.007, -377.850, 260.207, 178.715, 2.823, -131.466);

        JointPos p2Joint = new JointPos(112.131, -75.554, 126.989, -139.027, -88.044, -26.477);
        DescPose p2Desc = new DescPose(368.003, -377.848, 260.211, 178.715, 2.823, -131.465);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        //开启末端透传功能
        robot.SetAxleGenComEnable(1);
        robot.SetAxleLuaEnable(1);

        while(cnt<=10)
        { 
            //读取版本号
            ret = robot.SndRcvAxleGenComCmdData(5, version, 10, ref rcvdata);
            Console.WriteLine($" hard version : {rcvdata[4]},hard code:{rcvdata[5]}, soft version:{rcvdata[6]} {rcvdata[7]}, soft code:{rcvdata[8]}");
            if (ret != 0)
            {
                break;
            }
            Thread.Sleep(1000);
            //读取艾灸头在位状态
            ret = robot.SndRcvAxleGenComCmdData(6, state, 6, ref rcvdata);
            Console.WriteLine($" state : {rcvdata[4]}");
            Thread.Sleep(1000);
            //开启艾灸头激光
            ret = robot.SndRcvAxleGenComCmdData(6, led_on, 6, ref rcvdata);
            Console.WriteLine($"led on rcv data is: {rcvdata[0]},{rcvdata[1]}, {rcvdata[2]}, {rcvdata[3]}, {rcvdata[4]}, {rcvdata[5]}");
            robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
            Thread.Sleep(4000);
            //关闭艾灸头激光
            ret = robot.SndRcvAxleGenComCmdData(6, led_off, 6, ref rcvdata);
            Console.WriteLine($"led off rcv data is: {rcvdata[0]},{rcvdata[1]}, {rcvdata[2]}, {rcvdata[3]}, {rcvdata[4]}, {rcvdata[5]}");
            robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
            Thread.Sleep(1000);
            Console.WriteLine($"***********************complate No. {cnt}  SDK test*****************************");
            cnt++;
        }

    }

下载开放协议Lua文件
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 下载开放协议Lua文件
    * @param [in] fileName 开放协议文件名称“CtrlDev_XXX.lua”
    * @param [in] savePath 开放协议保存文件路径
    * @return 错误码
    */
    public int OpenLuaDownload(string fileName, string savePath)
    
删除开放协议Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 删除开放协议Lua文件
    * @param [in] fileName 要删除的开放协议lua文件名“CtrlDev_XXX.lua”
    * @return 错误码
    */
    public int OpenLuaDelete(string fileName)
        
删除所有开放协议Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 删除所有开放协议Lua文件
    * @return 错误码
    */
    public int AllOpenLuaDelete()

开放协议Lua文件操作的SDK代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    public int TestCtrlOpenLuaOperate()
    {
        int rtn;

        // 上传 Lua 文件到机器人
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_WELDING_A.lua");
        Console.WriteLine($"OpenLuaUpload rtn is {rtn}");
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_SWDPOLISH.lua");
        Console.WriteLine($"OpenLuaUpload rtn is {rtn}");

        // 从机器人下载 Lua 文件
        rtn = robot.OpenLuaDownload("CtrlDev_WELDING_A.lua", "D://zDOWN/");
        Console.WriteLine($"OpenLuaDownload rtn is {rtn}");
        rtn = robot.OpenLuaDownload("CtrlDev_SWDPOLISH.lua", "D://zDOWN/");
        Console.WriteLine($"OpenLuaDownload rtn is {rtn}");

        // 设置控制开放协议 Lua 名称
        rtn = robot.SetCtrlOpenLUAName(0, "CtrlDev_WELDING_A.lua");
        Console.WriteLine($"SetCtrlOpenLUAName rtn is {rtn}");
        rtn = robot.SetCtrlOpenLUAName(1, "CtrlDev_SWDPOLISH.lua");
        Console.WriteLine($"SetCtrlOpenLUAName rtn is {rtn}");

        // 获取控制开放协议 Lua 名称
        string[] name = new string[4];
        rtn = robot.GetCtrlOpenLUAName(ref name);
        Console.WriteLine($"ctrl open lua names : {name[0]}, {name[1]}, {name[2]}, {name[3]}");

        // 加载和卸载开放协议 Lua
        rtn = robot.LoadCtrlOpenLUA(1);
        Console.WriteLine($"LoadCtrlOpenLUA rtn is {rtn}");
        robot.Sleep(2000);
        rtn = robot.UnloadCtrlOpenLUA(1);
        Console.WriteLine($"UnloadCtrlOpenLUA rtn is {rtn}");

        // 删除指定 Lua 文件和所有 Lua 文件
        rtn = robot.OpenLuaDelete("CtrlDev_WELDING_A.lua");
        Console.WriteLine($"OpenLuaDelete rtn is {rtn}");
        rtn = robot.AllOpenLuaDelete();
        Console.WriteLine($"AllOpenLuaDelete rtn is {rtn}");

        return 0;
    }

控制灵巧手运动
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:    

    /**
    * @brief  控制灵巧手运动
    * @param  [in] idstart  起始从站号
    * @param  [in] slaveNum  数量
    * @param  [in] pos[16]  位置(-360~360) 
    * @param  [in] speed[16]  速度百分比，范围[0~100]
    * @param  [in] force[16]  力矩百分比，范围[0~100]
    * @param  [in] max_time  最大等待时间，范围[0~30000]，单位ms
    * @return  错误码
    */
    public int SetDexterousHandsMove(int idstart, int slaveNum, double[] pos, int[] speed, int[] force, int max_time)
    
控制灵巧手复位激活
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:   

    /**
    * @brief  控制灵巧手复位激活
    * @param  [in] id  从站号
    * @param  [in] act  0-复位 1-激活
    * @return  错误码
    */
    public int SetDexterousHandsAct(int id, int act)
    
清除灵巧手错误
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:   

    /**
    * @brief  清除灵巧手错误
    * @return  错误码
    */
    public int ClearDexterousHandsError()
    
设置启用灵巧手动作控制功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:   

    /**
    * @brief 设置启用灵巧手动作控制功能
    * @param [in] id 灵巧手从站编号
    * @param [in] 0-夹持触发、1-夹爪初始化、2-位置设置、3-速度设置、4-力矩设置、6-读夹爪状态、7-读初始化状态、8-读故障码、9-读位置、10-读速度、11-读力矩、12-旋转圈数设置、13-旋转速度设置、14-旋转力矩设置、15-读旋转夹爪状态、16-读旋转初始化状态、17-读旋转圈数、18-读旋转速度、19-读旋转力矩、20-多轴同步运动设置、21-故障清除指令、22-单轴运行状态、23-所有轴运行状态
    * @return  错误码
    */
    public int SetDexterousHandsFunc(int id, int[] func)
    
获取启用灵巧手动作控制功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:   

    /**
    * @brief 获取启用灵巧手动作控制功能
    * @param [in] id 灵巧手设备编号
    * @param [out]0-夹持触发、1-夹爪初始化、2-位置设置、3-速度设置、4-力矩设置、6-读夹爪状态、7-读初始化状态、8-读故障码、9-读位置、10-读速度、11-读力矩、12-旋转圈数设置、13-旋转速度设置、14-旋转力矩设置、15-读旋转夹爪状态、16-读旋转初始化状态、17-读旋转圈数、18-读旋转速度、19-读旋转力矩、20-多轴同步运动设置、21-故障清除指令、22-单轴运行状态、23-所有轴运行状态
    */
    public int GetDexterousHandsFunc(int id, ref int[] func)

末端灵巧手配置及运动代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    private void button105_Click(object sender, EventArgs e)
    {
        int id = 1;               // Slave station number
        int slaveNum = 4;         // Control 4 fingers
        int max_time = 8000;      // Maximum wait time 8 seconds
        int[] speed = new int[16]; // Speed array, all 0 means use default speed
        int[] force = new int[16]; // Torque array

        // Initialize torque array: first 4 fingers set to 50%, the rest 0 (values sent via Move command)
        for (int i = 0; i < 16; i++)
            force[i] = (i < 4) ? 50 : 0;

        // Helper function: set position array (only first 4 fingers are effective)
        double[] pos = new double[16];
        void SetPositions(double v1, double v2, double v3, double v4)
        {
            for (int i = 0; i < 16; i++)
                pos[i] = 0;
            pos[0] = v1;
            pos[1] = v2;
            pos[2] = v3;
            pos[3] = v4;
        }

        JointPos j1 = new JointPos(-91.876, -85.920, 109.279, -86.239, -96.664, -28.563);
        JointPos j2 = new JointPos(-40.954, -85.920, 109.279, -86.239, -96.664, -28.563);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        Console.WriteLine("===== Dexterous Hand Full Function Test Started =====");

        // 1. Clear error
        int ret = robot.ClearDexterousHandsError();
        Console.WriteLine($"ClearDexterousHandsError -> {ret}");

        // ========== 2. Set function switches ==========
        int[] setFunc = new int[32];
        setFunc[2] = 1;   // Enable position setting function
        setFunc[4] = 1;   // Enable torque setting function
        setFunc[9] = 1;   // Read position
        setFunc[10] = 1;  // Read torque
        setFunc[11] = 1;  // Read status
        setFunc[22] = 1;  // Single-axis motion status

        ret = robot.SetDexterousHandsFunc(id, setFunc);
        Console.WriteLine($"SetDexterousHandsFunc(enable + init + position/torque functions enabled) -> {ret}");

        // ========== 3. Read function status (verify settings took effect) ==========
        int[] getFunc = new int[32];  // GetDexterousHandsFunc returns 32 integers
        ret = robot.GetDexterousHandsFunc(id, ref getFunc);
        Console.WriteLine($"GetDexterousHandsFunc -> {ret}");
        if (ret == 0)
        {
            // Print all 32 values
            Console.WriteLine("All 32 values returned by GetDexterousHandsFunc:");
            for (int i = 0; i < getFunc.Length; i++)
            {
                Console.Write($"  [{i}]={getFunc[i]}");
                if ((i + 1) % 8 == 0)
                    Console.WriteLine();          // New line every 8 items
                else if (i < getFunc.Length - 1)
                    Console.Write(", ");
            }
            if (getFunc.Length % 8 != 0)
                Console.WriteLine();              // Add newline if last line has fewer than 8 items
        }

        // ========== 4. Activate dexterous hand ==========
        ret = robot.SetDexterousHandsAct(id, 1);
        Console.WriteLine($"SetDexterousHandsAct(activate) -> {ret}");
        if (ret != 0)
        {
            Console.WriteLine("Activation failed, test aborted");
            return;
        }

        // ========== 5. Initial move to 20° (send position and torque values via Move command) ==========
        SetPositions(20, 20, 20, 20);
        ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time);
        Console.WriteLine($"Initial move to 20° -> {ret}");
        robot.Sleep(5000);

        // ========== 6. Reciprocating motion 10 times (10° ↔ 50°) ==========
        Console.WriteLine("Starting 10 reciprocating motions...");
        for (int iteration = 1; iteration <= 10; iteration++)
        {
            robot.MoveJ(j1, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);

            SetPositions(10, 10, 10, 10);
            ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time);
            Console.WriteLine($"[{iteration}] Move to 10° -> {ret}");
            robot.Sleep(1000);

            robot.MoveJ(j2, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);

            SetPositions(50, 50, 50, 50);
            ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time);
            Console.WriteLine($"[{iteration}] Move to 50° -> {ret}");
            robot.Sleep(1000);
        }

        Console.WriteLine("Test completed (function switch set/read + activation + 10 reciprocating motions).");
    }