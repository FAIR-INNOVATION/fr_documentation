机器人状态查询
===============

.. toctree:: 
    :maxdepth: 5

获取当前关节位置(角度)
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前关节位置(角度)
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] jPos 六个关节位置，单位deg
    * @return  错误码
    */
    int GetActualJointPosDegree(byte flag, ref JointPos jPos); 

获取当前关节位置(弧度)
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前关节位置(弧度)
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] jPos 六个关节位置，单位rad
    * @return  错误码
    */   
    int GetActualJointPosRadian(byte flag, ref JointPos jPos);

获取关节反馈速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取关节反馈速度-deg/s 
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] speed 六个关节速度 
    * @return 错误码 
    */
    int GetActualJointSpeedsDegree(byte flag, ref double[] speed);

获取关节反馈加速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取关节反馈加速度-deg/s^2 
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] acc 六个关节加速度 
    * @return 错误码 
    */
    int GetActualJointAccDegree(byte flag, ref double[] acc); 

获取TCP指令速度-合速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取TCP指令速度-合速度 
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] tcp_speed 线性速度 
    * @param [out] ori_speed 姿态速度 
    * @return 错误码 
    */
    int GetTargetTCPCompositeSpeed(byte flag, ref double tcp_speed, ref double ori_speed); 

获取TCP反馈速度-合速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:
    
    /** 
    * @brief 获取TCP反馈速度-合速度
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] tcp_speed 线性速度 
    * @param [out] ori_speed 姿态速度 
    * @return 错误码 
    */
    int GetActualTCPCompositeSpeed(byte flag, ref double tcp_speed, ref double ori_speed);

获取TCP指令速度-分速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取TCP指令速度-分速度
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] speed [x,y,z,rx,ry,rz]速度 
    * @return 错误码 
    */
    int GetTargetTCPSpeed(byte flag, ref double[] speed);

获取TCP反馈速度-分速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取TCP反馈速度-分速度
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] speed [x,y,z,rx,ry,rz]速度 
    * @return 错误码 
    */
    int GetActualTCPSpeed(byte flag, ref double[] speed);

获取当前工具位姿
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前工具位姿
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] desc_pos  工具位姿
    * @return  错误码
    */
    int GetActualTCPPose(byte flag, ref DescPose desc_pos); 

获取当前工具坐标系编号
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前工具坐标系编号
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] id  工具坐标系编号
    * @return  错误码
    */
    int GetActualTCPNum(byte flag, ref int id);  

获取当前工件坐标系编号
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前工件坐标系编号
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] id  工件坐标系编号
    * @return  错误码
    */
    int GetActualWObjNum(byte flag, ref int id);

获取当前末端法兰位姿
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前末端法兰位姿
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] desc_pos  法兰位姿
    * @return  错误码
    */
    int GetActualToolFlangePose(byte flag, ref DescPose desc_pos);   

获取当前关节转矩
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取当前关节转矩
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] torques 关节转矩
    * @return  错误码
    */
    int GetJointTorques(byte flag, float[] torques); 

获取系统时间
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取系统时间
    * @param  [out] t_ms 单位ms
    * @return  错误码
    */
    int GetSystemClock(ref double t_ms);

查询机器人运动是否完成
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  查询机器人运动是否完成
    * @param  [out]  state  0-未完成，1-完成
    * @return  错误码
    */   
    int GetRobotMotionDone(ref byte state);

查询机器人运动队列缓存长度
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 查询机器人运动队列缓存长度 
    * @param [out] len   缓存长度
    * @return 错误码 
    */
    int GetMotionQueueLength(ref int len);

获取机器人急停状态
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取机器人急停状态
    * @param [out] state 急停状态，0-非急停，1-急停
    * @return 错误码  
    */
    int GetRobotEmergencyStopState(ref byte state);

获取SDK与机器人的通讯状态
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取SDK与机器人的通讯状态
    * @param [out]  state 通讯状态，0-通讯正常，1-通讯异常
    */
    int GetSDKComState(ref int state);

获取安全停止信号
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取安全停止信号
    * @param [out]  si0_state 安全停止信号SI0，0-无效，1-有效
    * @param [out]  si1_state 安全停止信号SI1，0-无效，1-有效
    */
    int GetSafetyStopState(ref byte si0_state, ref byte si1_state);

获取机器人关节驱动器温度(℃)
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取机器人关节驱动器温度(℃)
    * @return 错误码
    */
    int GetJointDriverTemperature(double[] temperature);

获取机器人关节驱动器扭矩(Nm)
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取机器人关节驱动器扭矩(Nm)
    * @return 错误码
    */
    int GetJointDriverTorque(double torque[]);

获取机器人实时状态结构体
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取机器人实时状态结构体
    * @param [out] pkg 机器人实时状态结构体 
    * @return 错误码 
    */
    int GetRobotRealTimeState(ref ROBOT_STATE_PKG pkg);

机器人状态查询代码示例
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button29_Click(object sender, EventArgs e)
    {
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
        double yangle = 0, zangle = 0;
        robot.GetRobotInstallAngle(ref yangle, ref zangle);
        Console.WriteLine($"yangle:{yangle},zangle:{zangle}");

        JointPos j_deg = new JointPos(0,0,0,0,0,0);
        robot.GetActualJointPosDegree(0, ref j_deg);
        Console.WriteLine($"joint pos deg:{j_deg.jPos[0]},{j_deg.jPos[1]},{j_deg.jPos[2]},{j_deg.jPos[3]},{j_deg.jPos[4]},{j_deg.jPos[5]}");

        double[] jointSpeed = new double[6];
        robot.GetActualJointSpeedsDegree(0, ref jointSpeed);
        Console.WriteLine($"joint speeds deg:{jointSpeed[0]},{jointSpeed[1]},{jointSpeed[2]},{jointSpeed[3]},{jointSpeed[4]},{jointSpeed[5]}");

        double[] jointAcc = new double[6];
        robot.GetActualJointAccDegree(0, ref jointAcc);
        Console.WriteLine($"joint acc deg:{jointAcc[0]},{jointAcc[1]},{jointAcc[2]},{jointAcc[3]},{jointAcc[4]},{jointAcc[5]}");

        double tcp_speed = 0, ori_speed = 0;
        robot.GetTargetTCPCompositeSpeed(0, ref tcp_speed, ref ori_speed);
        Console.WriteLine($"GetTargetTCPCompositeSpeed tcp {tcp_speed}; ori {ori_speed}");

        robot.GetActualTCPCompositeSpeed(0, ref tcp_speed, ref ori_speed);
        Console.WriteLine($"GetActualTCPCompositeSpeed tcp {tcp_speed}; ori {ori_speed}");

        double[] targetSpeed = new double[6];
        robot.GetTargetTCPSpeed(0,ref targetSpeed);
        Console.WriteLine($"GetTargetTCPSpeed {targetSpeed[0]},{targetSpeed[1]},{targetSpeed[2]},{targetSpeed[3]},{targetSpeed[4]},{targetSpeed[5]}");

        double[] actualSpeed = new double[6];
        robot.GetActualTCPSpeed(0, ref actualSpeed);
        Console.WriteLine($"GetTargetTCPSpeed {actualSpeed[0]},{actualSpeed[1]},{actualSpeed[2]},{actualSpeed[3]},{actualSpeed[4]},{actualSpeed[5]}");

        DescPose tcp = new DescPose(0, 0, 0, 0, 0, 0);
        robot.GetActualTCPPose(0, ref tcp);
        Console.WriteLine($"tcp pose:{tcp.tran.x},{tcp.tran.y},{tcp.tran.z},{tcp.rpy.rx},{tcp.rpy.ry},{tcp.rpy.rz}");

        DescPose flange = new DescPose(0, 0, 0, 0, 0, 0);
        robot.GetActualToolFlangePose(0, ref flange);
        Console.WriteLine($"flange pose:{flange.tran.x},{flange.tran.y},{flange.tran.z},{flange.rpy.rx},{flange.rpy.ry},{flange.rpy.rz}");

        int id = 0;
        robot.GetActualTCPNum(0, ref id);
        Console.WriteLine($"tcp num:{id}");

        robot.GetActualWObjNum(0, ref id);
        Console.WriteLine($"wobj num:{id}");

        double[] jtorque = new double[6];
        robot.GetJointTorques(0, jtorque);
        Console.WriteLine($"torques:{jtorque[0]},{jtorque[1]},{jtorque[2]},{jtorque[3]},{jtorque[4]},{jtorque[5]}");

        double t_ms = 0;
        robot.GetSystemClock(ref t_ms);
        Console.WriteLine($"system clock:{t_ms}");

        int config = 0;
        robot.GetRobotCurJointsConfig(ref config);
        Console.WriteLine($"joint config:{config}");

        byte motionDone = 0;
        robot.GetRobotMotionDone(ref motionDone);
        Console.WriteLine($"GetRobotMotionDone :{motionDone}");

        int len = 0;
        robot.GetMotionQueueLength(ref len);
        Console.WriteLine($"GetMotionQueueLength :{len}");

        byte emergState = 0;
        robot.GetRobotEmergencyStopState(ref emergState);
        Console.WriteLine($"GetRobotEmergencyStopState :{emergState}");

        int comstate = 0;
        robot.GetSDKComState(ref comstate);
        Console.WriteLine($"GetSDKComState :{comstate}");

        byte si0_state = 0, si1_state = 0;
        robot.GetSafetyStopState(ref si0_state, ref si1_state);
        Console.WriteLine($"GetSafetyStopState :{si0_state} {si1_state}");

        double[] temp = new double[6];
        robot.GetJointDriverTemperature(temp);
        Console.WriteLine($"Temperature:{temp[0]},{temp[1]},{temp[2]},{temp[3]},{temp[4]},{temp[5]}");

        double[] torque = new double[6];
        robot.GetJointDriverTorque(torque);
        Console.WriteLine($"torque:{torque[0]},{torque[1]},{torque[2]},{torque[3]},{torque[4]},{torque[5]}");

        robot.GetRobotRealTimeState(ref pkg);
    }

逆运动学求解
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  逆运动学求解
    * @param  [in] type 0-绝对位姿(基坐标系)，1-增量位姿(基坐标系)，2-增量位姿(工具坐标系)
    * @param  [in] desc_pos 笛卡尔位姿
    * @param  [in] config 关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解
    * @param  [out] joint_pos 关节位置
    * @return  错误码
    */ 
    int GetInverseKin(int type, DescPose desc_pos, int config, ref JointPos joint_pos);

逆运动学求解(参考位置)
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  逆运动学求解，参考指定关节位置判断是否有解
    * @param  [in] type 0-绝对位姿(基坐标系)，1-增量位姿(基坐标系)，2-增量位姿(工具坐标系)
    * @param  [in] desc_pos 笛卡尔位姿
    * @param  [in] joint_pos_ref 参考关节位置
    * @param  [out] result 0-无解，1-有解
    * @return  错误码
    */   
    int GetInverseKinRef(int posMode, DescPose desc_pos, JointPos joint_pos_ref, ref JointPos joint_pos); 

获取逆运动学是否有解
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 逆运动学求解，判断指定参考关节位置是否有解
    * @param [in] posMode 0绝对位姿，1相对位姿-基坐标系，2相对位姿-工具坐标系 
    * @param [in] desc_pos 笛卡尔位姿 
    * @param [in] joint_pos_ref 参考关节位置 
    * @param [out] hasResult 0-无解，1-有解 
    * @return 错误码 
    */ 
    int GetInverseKinHasSolution(int posMode, DescPose desc_pos, JointPos joint_pos_ref, ref bool hasResult);  

正运动学求解
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  正运动学求解
    * @param  [in] joint_pos 关节位置
    * @param  [out] desc_pos 笛卡尔位姿
    * @return  错误码
    */
    int GetForwardKin(JointPos joint_pos, ref DescPose desc_pos); 

机器人正逆运动学计算代码示例
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button30_Click(object sender, EventArgs e)
    {
        JointPos j1 = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        DescPose desc_pos1 = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);

        JointPos inverseRtn = new JointPos(0, 0, 0, 0, 0, 0);

        robot.GetInverseKin(0, desc_pos1, -1, ref inverseRtn);
        Console.WriteLine($"dcs1 GetInverseKin rtn is {inverseRtn.jPos[0]} {inverseRtn.jPos[1]} {inverseRtn.jPos[2]} {inverseRtn.jPos[3]} {inverseRtn.jPos[4]} {inverseRtn.jPos[5]}");
        robot.GetInverseKinRef(0,  desc_pos1, j1, ref inverseRtn);
        Console.WriteLine($"dcs1 GetInverseKinRef rtn is {inverseRtn.jPos[0]} {inverseRtn.jPos[1]} {inverseRtn.jPos[2]} {inverseRtn.jPos[3]} {inverseRtn.jPos[4]} {inverseRtn.jPos[5]}");

        bool hasResut = false;
        robot.GetInverseKinHasSolution(0,  desc_pos1,  j1, ref hasResut);
        Console.WriteLine($"dcs1 GetInverseKinRef result {hasResut}");

        DescPose forwordResult = new DescPose(0, 0, 0, 0, 0, 0);
        robot.GetForwardKin(j1, ref forwordResult);
        Console.WriteLine($"jpos1 forwordResult rtn is {forwordResult.tran.x} {forwordResult.tran.y} {forwordResult.tran.z} {forwordResult.rpy.rx} {forwordResult.rpy.ry} {forwordResult.rpy.rz}");
    }

查询机器人示教管理点数据
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 查询机器人示教管理点位数据 
    * @param [in] name    点位名
    * @param [out] data   点位数据double[20]{x,y,z,rx,ry,rz,j1,j2,j3,j4,j5,j6,tool, wobj,speed,acc,e1,e2,e3,e4}
    * @return 错误码 
    */ 
    int GetRobotTeachingPoint(string name, ref double[] data); 

获取机器人DH参数补偿值 
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取机器人DH参数补偿值 
    * @param [out] dhCompensation 机器人DH参数补偿值(mm) [cmpstD1,cmpstA2,cmpstA3,cmpstD4,cmpstD5,cmpstD6]
    * @return 错误码 
    */
    int GetDHCompensation(ref double[] dhCompensation);


获取控制箱SN码
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取控制箱SN码
    * @param [out] SNCode 控制箱SN码
    * @return 错误码
    */
    int GetRobotSN(ref string SNCode);

查询机器人示教管理点位数据代码示例
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button31_Click(object sender, EventArgs e)
    {
        string name = "A0";
        double[] data = new double[20];
        int rtn = robot.GetRobotTeachingPoint(name, ref data);
        Console.WriteLine(" {0} name is: {1} \n", rtn, name);
        for (int i = 0; i < 20; i++)
        {
            Console.WriteLine("data is: {0} \n", data[i]);
        }

        int que_len = 0;
        rtn = robot.GetMotionQueueLength(ref que_len);
        Console.WriteLine("GetMotionQueueLength rtn is: {0}, queue length is: {1} \n", rtn, que_len);

        double[] dh = { 0, 0, 0, 0, 0, 0 };
        int retval = 0;
        retval = robot.GetDHCompensation(ref dh);
        Console.WriteLine($"retval is  {retval}");
        Console.WriteLine($"dh is {dh[0]}, {dh[1]}, {dh[2]}, {dh[3]}, {dh[4]}, {dh[5]}");
        string SN = "";
        robot.GetRobotSN(ref SN);
        Console.WriteLine($"robot SN is  {SN}");
    }







