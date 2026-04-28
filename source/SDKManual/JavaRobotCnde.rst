CNDE
=============

.. toctree:: 
    :maxdepth: 5

配置机器人状态反馈
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 配置机器人状态反馈
    * @param state 机器人状态枚举列表
    * @param period 状态反馈周期，范围8-1000
    * @return 错误码，正常-0，参数异常-4，状态字段不存在-18，字节总数超过4K-20
    */
    public int SetRobotRealtimeStateConfig(List<RobotState> state, int period)
    
CNDE状态配置添加一个机器人状态
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 添加一个机器人状态到配置列表
    * @param state 机器人状态枚举
    * @return 错误码，正常-0，状态已存在-17，状态字段不存在-18，超过4K-20
    */
    public int AddRobotRealtimeState(RobotState state)
    
CNDE状态配置删除一个机器人状态
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 从配置列表删除一个机器人状态
    * @param state 机器人状态枚举
    * @return 错误码，正常-0，状态不存在-18，至少保留一个状态-19
    */
    public int DeleteRobotRealtimeState(RobotState state)
        
设置CNDE状态反馈周期
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置CNDE状态反馈周期
    * @param period 状态反馈周期，范围8-1000
    * @return 错误码，正常-0，参数异常-4
    */
    public int SetRobotRealtimeStatePeriod(int period)
            
获取当前CNDE状态反馈所有状态集合和周期
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 获取当前所有状态集合和周期
     * @return 包含状态列表和周期的配置结果结构体
    */
    public StateConfigResult GetRobotRealtimeStateConfig()
                
CNDE状态反馈使用代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief CNDE实时状态配置接口使用示例
    */
    public static void TestRealtimeStateConfig(Robot robot)
    {
        
        // 1. 创建初始状态列表
        List<RobotState> stateList1 = new ArrayList<>();
        stateList1.add(RobotState.ProgramState);
        stateList1.add(RobotState.RobotState);
        stateList1.add(RobotState.JointCurPos);
        stateList1.add(RobotState.ToolCurPos);
        
        // 2. 第一次调用 SetRobotRealtimeStateConfig 配置状态和周期
        int period1 = 100;  // 100ms周期
        int rtn = robot.SetRobotRealtimeStateConfig(stateList1, period1);
        System.out.printf("1. SetRobotRealtimeStateConfig (initial list, period=%d) rtn: %d%n", period1, rtn);
        
        if (rtn == 0) {
            // 3. 添加额外状态
            rtn = robot.AddRobotRealtimeState(RobotState.RobotTime);
            System.out.printf("2. AddRobotRealtimeState (RobotTime) rtn: %d%n", rtn);
            
            // 4. 再次调用 SetRobotRealtimeStateConfig 重新配置（不同状态列表）
            List<RobotState> stateList2 = new ArrayList<>();
            stateList2.add(RobotState.ProgramState);
            stateList2.add(RobotState.RobotState);
            stateList2.add(RobotState.MainCode);
            stateList2.add(RobotState.SubCode);
            stateList2.add(RobotState.JointCurPos);
            stateList2.add(RobotState.ToolCurPos);
            stateList2.add(RobotState.ActualJointTorque);
            
            int period2 = 50;  // 50ms周期
            rtn = robot.SetRobotRealtimeStateConfig(stateList2, period2);
            System.out.printf("3. SetRobotRealtimeStateConfig (updated list, period=%d) rtn: %d%n", period2, rtn);
            
            // 5. 修改周期
            int newPeriod = 80;  // 80ms周期
            rtn = robot.SetRobotRealtimeStatePeriod(newPeriod);
            System.out.printf("4. SetRobotRealtimeStatePeriod (period=%d) rtn: %d%n", newPeriod, rtn);
            
            // 6. 获取当前配置并打印
            Robot.StateConfigResult configResult = robot.GetRobotRealtimeStateConfig();
            System.out.println("5. GetRobotRealtimeStateConfig result:");
            System.out.printf("   - Period: %d ms%n", configResult.period);
            System.out.println("   - Configured States:");
            for (int i = 0; i < configResult.stateList.size(); i++) {
                System.out.printf("     [%d] %s%n", i, configResult.stateList.get(i));
            }
            
            rtn = robot.RPC("192.168.58.2");
            if (rtn == 0) {
                System.out.println("rpc连接 success");
            } else {
                System.out.println("rpc连接 fail");
                return;
            }
            // 等待CNDE连接建立
            System.out.println("等待CNDE连接建立...");
            while (robot.CNDEGetStateData() == null) {
                robot.Sleep(100);
            }
            System.out.println("CNDE连接已建立，开始接收数据...");

            // 7. 循环读取实时状态验证配置是否生效
            System.out.println("6. Reading real-time states...");
            while(true) {
                robot.Sleep(1000);
                // 通过 CNDE 获取状态数据
                ROBOT_STATE_PKG pkg = robot.CNDEGetStateData();
                if (pkg == null) {
                    System.out.println("状态数据为空，CNDE连接断开，等待重连");
                    continue;  // 连接断开时继续循环，等待重连
                }
                System.out.println("\n--- 机器人时间 ---");
                if (pkg.robotTime != null) {
                    System.out.println("robotTime: " + pkg.robotTime.year + "-" + pkg.robotTime.month + "-" + pkg.robotTime.day +
                            " " + pkg.robotTime.hour + ":" + pkg.robotTime.minute + ":" + pkg.robotTime.second +
                            "." + pkg.robotTime.millisecond);
                }

                System.out.println("   --- 状态信息 ---");
                System.out.printf("   program_state: %d%n", pkg.program_state);
                System.out.printf("   robot_state: %d%n", pkg.robot_state);
                System.out.printf("   main_code: %d%n", pkg.main_code);
                System.out.printf("   sub_code: %d%n", pkg.sub_code);
                System.out.println("   --- 关节位置 (actual_joint_pos) ---");
                System.out.printf("   jt_cur_pos[0-2]: %.2f, %.2f, %.2f%n",
                    pkg.jt_cur_pos[0], pkg.jt_cur_pos[1], pkg.jt_cur_pos[2]);
                System.out.printf("   jt_cur_pos[3-5]: %.2f, %.2f, %.2f%n",
                    pkg.jt_cur_pos[3], pkg.jt_cur_pos[4], pkg.jt_cur_pos[5]);
                System.out.println("   --- TCP位置 (actual_TCP_pos) ---");
                System.out.printf("   tl_cur_pos[0-2]: %.2f, %.2f, %.2f%n",
                    pkg.tl_cur_pos[0], pkg.tl_cur_pos[1], pkg.tl_cur_pos[2]);
                System.out.printf("   tl_cur_pos[3-5]: %.2f, %.2f, %.2f%n",
                    pkg.tl_cur_pos[3], pkg.tl_cur_pos[4], pkg.tl_cur_pos[5]);
                System.out.println("   --- 关节力矩 (actual_joint_torque) ---");
                System.out.printf("   jt_cur_tor[0-2]: %.2f, %.2f, %.2f%n",
                    pkg.jt_cur_tor[0], pkg.jt_cur_tor[1], pkg.jt_cur_tor[2]);
                System.out.printf("   jt_cur_tor[3-5]: %.2f, %.2f, %.2f%n",
                    pkg.jt_cur_tor[3], pkg.jt_cur_tor[4], pkg.jt_cur_tor[5]);
                robot.Sleep(500);
            }
        } else {
            System.out.printf("SetRobotRealtimeStateConfig failed with error: %d%n", rtn);
        }
    }
