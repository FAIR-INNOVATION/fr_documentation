机器人力控
============

.. toctree:: 
    :maxdepth: 5

力传感器配置
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  配置力传感器
    * @param  [in] company  力传感器厂商，17-坤维科技
    * @param  [in] device  设备号，暂不使用，默认为0
    * @param  [in] softvesion  软件版本号，暂不使用，默认为0
    * @param  [in] bus 设备挂在末端总线位置，暂不使用，默认为0
    * @return  错误码
    */
    int FT_SetConfig(int company, int device, int softvesion, int bus); 

获取力传感器配置 
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取力传感器配置 
    * @param [out] deviceID 力传感器编号 
    * @param [out] company 力传感器厂商，，力传感器厂商，17-坤维科技，19-航天十一院，20-ATI传感器，21-中科米点，22-伟航敏芯
    * @param [out] device  设备号，坤维(0-KWR75B)，航天十一院(0-MCS6A-200-4)，ATI (0-AXIA80 -M8)，中科米点(0-MST2010)，伟航敏芯(0-WHC6L-YB-10A) 
    * @param [out] softvesion 软件版本号，暂不使用，默认为 0 
    * @return 错误码 
    */ 
    int FT_GetConfig(ref int deviceID, ref int company, ref int device, ref int softvesion); 

力传感器激活
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  力传感器激活
    * @param  [in] act  0-复位，1-激活
    * @return  错误码
    */
    int FT_Activate(byte act); 

力传感器校零
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  力传感器校零
    * @param  [in] act  0-去除零点，1-零点矫正
    * @return  错误码
    */
    int FT_SetZero(byte act); 

代码示例
+++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnFT_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        int company = 17;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int index = 1;
        byte act = 0;

        robot.FT_SetConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        company = 0;
        robot.FT_GetConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine($"FT config : {company}, {device}, {softversion}, {bus}");
        Thread.Sleep(1000);

        robot.FT_Activate(act);
        Thread.Sleep(1000);
        act = 1;
        robot.FT_Activate(act);
        Thread.Sleep(1000);

        robot.SetLoadWeight(0.0f);
        Thread.Sleep(1000);
        DescTran coord = new DescTran(0, 0, 0);
                
        robot.SetLoadCoord(coord);
        Thread.Sleep(1000);
        robot.FT_SetZero(0);//0去除零点  1零点矫正
        Thread.Sleep(1000);

        ForceTorque ft = new ForceTorque(0, 0, 0, 0, 0, 0);
        int rtn = robot.FT_GetForceTorqueOrigin(1, ref ft);
        Console.WriteLine($"ft origin : {ft.fx}, {ft.fy}, { ft.fz}, { ft.tx}, { ft.ty}, { ft.tz}    rtn   {rtn}");
        rtn = robot.FT_SetZero(1);//零点矫正
        //Console.WriteLine($"set zero rtn {rtn}");

        Thread.Sleep(2000);
        rtn = robot.FT_GetForceTorqueOrigin(1, ref ft);
        Console.WriteLine($"ft rcs : {ft.fx}, {ft.fy}, {ft.fz}, {ft.tx}, {ft.ty}, {ft.tz}  rtn  {rtn}");

        robot.FT_GetForceTorqueRCS(1, ref ft);
        Console.WriteLine($"FT_GetForceTorqueRCS rcs : {ft.fx}, {ft.fy}, {ft.fz}, {ft.tx}, {ft.ty}, {ft.tz}");
    }

设置力传感器参考坐标系
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置力传感器参考坐标系
    * @param  [in] ref  0-工具坐标系，1-基坐标系
    * @return  错误码
    */
    int FT_SetRCS(byte type); 

负载重量辨识记录
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  负载重量辨识记录
    * @param  [in] id  传感器坐标系编号，范围[1~14]
    * @return  错误码
    */
    int FT_PdIdenRecord(int id);

负载重量辨识计算
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  负载重量辨识计算
    * @param  [out] weight  负载重量，单位kg
    * @return  错误码
    */   
    int FT_PdIdenCompute(ref double weight);

负载质心辨识记录
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  负载质心辨识记录
    * @param  [in] id  传感器坐标系编号，范围[1~14]
    * @param  [in] index 点编号，范围[1~3]
    * @return  错误码
    */
    int FT_PdCogIdenRecord(int id, int index); 

负载质心辨识计算
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  负载质心辨识计算
    * @param  [out] cog  负载质心，单位mm
    * @return  错误码
    */   
    int FT_PdCogIdenCompute(ref DescTran cog);

代码示例
+++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnFTPdCog_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        double weight = 0.1;
        int rtn = -1;
        DescPose tcoord, desc_p1, desc_p2, desc_p3;
        tcoord = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p3 = new DescPose(0, 0, 0, 0, 0, 0);

        robot.FT_SetRCS(0);
        Thread.Sleep(1000);

        tcoord.tran.z = 35.0;
        robot.SetToolCoord(10, tcoord, 1, 0);
        Thread.Sleep(1000);
        robot.FT_PdIdenRecord(10);
        Thread.Sleep(1000);
        robot.FT_PdIdenCompute(ref weight);
        Console.WriteLine($"payload weight : {weight}");

        desc_p1.tran.x = -47.805;
        desc_p1.tran.y = -362.266;
        desc_p1.tran.z = 317.754;
        desc_p1.rpy.rx = -179.496;
        desc_p1.rpy.ry = -0.255;
        desc_p1.rpy.rz = 34.948;

        desc_p2.tran.x = -77.805;
        desc_p2.tran.y = -312.266;
        desc_p2.tran.z = 317.754;
        desc_p2.rpy.rx = -179.496;
        desc_p2.rpy.ry = -0.255;
        desc_p2.rpy.rz = 34.948;

        desc_p3.tran.x = -167.805;
        desc_p3.tran.y = -312.266;
        desc_p3.tran.z = 387.754;
        desc_p3.rpy.rx = -179.496;
        desc_p3.rpy.ry = -0.255;
        desc_p3.rpy.rz = 34.948;

        rtn = robot.MoveCart(desc_p1, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        Console.WriteLine($"MoveCart rtn  {rtn}");
        Thread.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 1);
        robot.MoveCart(desc_p2, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        Thread.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 2);
        robot.MoveCart(desc_p3, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        Thread.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 3);
        Thread.Sleep(1000);
        DescTran cog = new DescTran(0, 0, 0);

        robot.FT_PdCogIdenCompute(ref cog);
        Console.WriteLine($"cog : {cog.x}, {cog.y}, {cog.z}");
    }

获取参考坐标系下力/扭矩数据
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取参考坐标系下力/扭矩数据
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  错误码
    */   
    int FT_GetForceTorqueRCS(byte flag, ref ForceTorque ft); 

获取力传感器原始力/扭矩数据
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取力传感器原始力/扭矩数据
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  错误码
    */   
    int FT_GetForceTorqueOrigin(byte flag, ref ForceTorque ft); 

碰撞守护
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  碰撞守护
    * @param  [in] flag 0-关闭碰撞守护，1-开启碰撞守护
    * @param  [in] sensor_id 力传感器编号
    * @param  [in] select  选择六个自由度是否检测碰撞，0-不检测，1-检测
    * @param  [in] ft  碰撞力/扭矩，fx,fy,fz,tx,ty,tz
    * @param  [in] max_threshold 最大阈值
    * @param  [in] min_threshold 最小阈值
    * @note   力/扭矩检测范围：(ft-min_threshold, ft+max_threshold)
    * @return  错误码
    */   
    int FT_Guard(int flag, int sensor_id, int[] select, ForceTorque ft, double[] max_threshold, double[] min_threshold); 

代码示例
+++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnFTGuard_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        byte flag = 1;
        byte sensor_id = 1;
        int[] select = new int[6]{ 1, 0, 0, 0, 0, 0 };//只启用x轴碰撞守护
        double[] max_threshold = new double[6]{ 5.0f, 0.01f, 0.01f, 0.01f, 0.01f, 0.01f };
        double[] min_threshold = new double[6]{ 3.0f, 0.01f, 0.01f, 0.01f, 0.01f, 0.01f };

        ForceTorque ft = new ForceTorque(0, 0, 0, 0, 0, 0);
        DescPose desc_p1, desc_p2, desc_p3;
        desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p3 = new DescPose(0, 0, 0, 0, 0, 0);

        desc_p1.tran.x = 1.299;
        desc_p1.tran.y = -719.159;
        desc_p1.tran.z = 141.314;
        desc_p1.rpy.rx = 177.999;
        desc_p1.rpy.ry = -0.715;
        desc_p1.rpy.rz = -161.937;

        desc_p2.tran.x = 245.047;
        desc_p2.tran.y = -675.509;
        desc_p2.tran.z = 139.538;
        desc_p2.rpy.rx = 177.987;
        desc_p2.rpy.ry = -0.129;
        desc_p2.rpy.rz = -142.238;

        desc_p3.tran.x = 157.233;
        desc_p3.tran.y = -550.088;
        desc_p3.tran.z = 112.485;
        desc_p3.rpy.rx = -176.579;
        desc_p3.rpy.ry = -2.819;
        desc_p3.rpy.rz = -148.415;
        robot.SetSpeed(5);

        int rtn =  robot.FT_Guard(flag, sensor_id, select, ft, max_threshold, min_threshold);
        Console.WriteLine($"FT_Guard start rtn {rtn}");
        robot.MoveCart(desc_p1, 1, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        robot.MoveCart(desc_p2, 1, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        robot.MoveCart(desc_p3, 1, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        flag = 0;
        rtn = robot.FT_Guard(flag, sensor_id, select, ft, max_threshold, min_threshold);
        Console.WriteLine($"FT_Guard end rtn {rtn}");
    }

恒力控制
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  恒力控制
    * @param  [in] flag 0-关闭恒力控制，1-开启恒力控制
    * @param  [in] sensor_id 力传感器编号
    * @param  [in] select  选择六个自由度是否检测碰撞，0-不检测，1-检测
    * @param  [in] ft  碰撞力/扭矩，fx,fy,fz,tx,ty,tz
    * @param  [in] ft_pid 力pid参数，力矩pid参数
    * @param  [in] adj_sign 自适应启停控制，0-关闭，1-开启
    * @param  [in] ILC_sign ILC启停控制， 0-停止，1-训练，2-实操
    * @param  [in] 最大调整距离，单位mm
    * @param  [in] 最大调整角度，单位deg
    * @return  错误码
    */   
    int FT_Control(int flag, int sensor_id, int[] select, ForceTorque ft, double[] ft_pid, int adj_sign, int ILC_sign, double max_dis, double max_ang);   

代码示例
+++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnFTConttol_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        byte flag = 1;
        byte sensor_id = 1;
        int[] select = new int[6]{ 0, 0, 1, 0, 0, 0 };
        double[] ft_pid = new double[6]{ 0.0005f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f };
        byte adj_sign = 0;
        byte ILC_sign = 0;
        float max_dis = 100.0f;
        float max_ang = 0.0f;

        ForceTorque ft = new ForceTorque(0, 0, 0, 0 ,0 ,0);
        DescPose desc_p1, desc_p2, offset_pos;
        JointPos j1, j2;
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);
        offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        j2 = new JointPos(0, 0, 0, 0, 0, 0);
        j1 = new JointPos(0, 0, 0, 0, 0, 0);

        desc_p1.tran.x = 1.299;
        desc_p1.tran.y = -719.159;
        desc_p1.tran.z = 141.314;
        desc_p1.rpy.rx = 177.999;
        desc_p1.rpy.ry = -0.715;
        desc_p1.rpy.rz = -161.937;

        desc_p2.tran.x = 245.047;
        desc_p2.tran.y = -675.509;
        desc_p2.tran.z = 139.538;
        desc_p2.rpy.rx = 177.987;
        desc_p2.rpy.ry = -0.129;
        desc_p2.rpy.rz = -142.238;
        ft.fz = -10.0;

        robot.GetInverseKin(0, desc_p1, -1, ref j1);
        robot.GetInverseKin(0, desc_p2, -1, ref j2);

        robot.MoveJ(j1, desc_p1, 1, 0, 100.0f, 180.0f, 100.0f, epos, -1.0f, 0, offset_pos);
        int rtn = robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang);
        Console.WriteLine($"FT_Control start rtn {rtn}");

        robot.MoveL(j2, desc_p2, 1, 0, 100.0f, 180.0f, 20.0f, -1.0f, epos, 0, 0, offset_pos);
        flag = 0;
        rtn = robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang);
        Console.WriteLine($"FT_Control end rtn {rtn}");
    }

柔顺控制开启
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  柔顺控制开启
    * @param  [in] p 位置调节系数或柔顺系数
    * @param  [in] force 柔顺开启力阈值，单位N
    * @return  错误码
    */   
    int FT_ComplianceStart(float p, float force);

柔顺控制关闭
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  柔顺控制关闭
    * @return  错误码
    */   
    int FT_ComplianceStop(); 

代码示例
+++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnComplience_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        byte flag = 1;
        int sensor_id = 1;
        int[] select = new int[6]{ 1, 1, 1, 0, 0, 0 };
        double[] ft_pid = new double[6] { 0.0005f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f };
        byte adj_sign = 0;
        byte ILC_sign = 0;
        float max_dis = 100.0f;
        float max_ang = 0.0f;

        ForceTorque ft = new ForceTorque(0, 0, 0, 0, 0, 0);
        DescPose desc_p1, desc_p2, offset_pos;
        JointPos j1, j2;

        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);
        offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        j2 = new JointPos(0, 0, 0, 0, 0, 0);
        j1 = new JointPos(0, 0, 0, 0, 0, 0);

        desc_p1.tran.x = 1.299;
        desc_p1.tran.y = -719.159;
        desc_p1.tran.z = 141.314;
        desc_p1.rpy.rx = 177.999;
        desc_p1.rpy.ry = -0.715;
        desc_p1.rpy.rz = -161.937;

        desc_p2.tran.x = 245.047;
        desc_p2.tran.y = -675.509;
        desc_p2.tran.z = 139.538;
        desc_p2.rpy.rx = 177.987;
        desc_p2.rpy.ry = -0.129;
        desc_p2.rpy.rz = -142.238;
        ft.fz = -10.0;

        robot.GetInverseKin(0, desc_p1, -1, ref j1);
        robot.GetInverseKin(0, desc_p2, -1, ref j2);

        ft.fx = -10.0;
        ft.fy = -10.0;
        ft.fz = -10.0;
        robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang);
        float p = 0.00005f;
        float force = 30.0f;
        int rtn = robot.FT_ComplianceStart(p, force);
        Console.WriteLine($"FT_ComplianceStart rtn {rtn}");
        int count = 15;
        while (count > 0)
        {
            robot.MoveL(j1, desc_p1, 1, 0, 100.0f, 180.0f, 100.0f, -1.0f, epos, 0, 1, offset_pos);
            robot.MoveL(j2, desc_p2, 1, 0, 100.0f, 180.0f, 100.0f, -1.0f, epos, 0, 0, offset_pos);
            count -= 1;
        }
        rtn = robot.FT_ComplianceStop();
        Console.WriteLine($"FT_ComplianceStop rtn {rtn}");
        flag = 0;
        robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang);
    }



负载辨识初始化
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 负载辨识初始化
    * @return 错误码
    */
    int LoadIdentifyDynFilterInit();

负载辨识变量初始化
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 负载辨识变量初始化
    * @return 错误码
    */
    int LoadIdentifyDynVarInit();

负载辨识主程序
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 负载辨识主程序
    * @param [in] joint_torque 关节扭矩
    * @param [in] joint_pos 关节位置
    * @param [in] t 采样周期
    * @return 错误码
    */
    int LoadIdentifyMain(double[] joint_torque, double[] joint_pos, double t);

获取负载辨识结果
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 获取负载辨识结果
    * @param [in] gain  重力项系数double[6]，离心项系数double[6]
    * @param [out] weight 负载重量
    * @param [out] cog 负载质心
    * @return 错误码
    */
    int LoadIdentifyGetResult(double[] gain, ref double weight, ref DescTran cog);

力传感器辅助拖动
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief  力传感器辅助拖动
    * @param  [in] status 控制状态，0-关闭；1-开启
    * @param  [in] asaptiveFlag 自适应开启标志，0-关闭；1-开启
    * @param  [in] interfereDragFlag 干涉区拖动标志，0-关闭；1-开启
    * @param  [in] ingularityConstraintsFlag 奇异点策略，0-规避；1-穿越
    * @param  [in] forceCollisionFlag 辅助拖动时机器人碰撞检测标志；0-关闭；1-开启
    * @param  [in] M 惯性系数
    * @param  [in] B 阻尼系数
    * @param  [in] K 刚度系数
    * @param  [in] F 拖动六维力阈值
    * @param  [in] Fmax 最大拖动力限制 Nm
    * @param  [in] Vmax 最大关节速度限制 °/s
    * @return  错误码
    */
    int EndForceDragControl(int status, int asaptiveFlag, int interfereDragFlag,int ingularityConstraintsFlag,int forceCollisionFlag, double[] M, double[] B, double[] K, double[] F, double Fmax, double Vmax);

代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:


    private void button3_Click(object sender, EventArgs e)
    {

        double[] M = { 15.0, 15.0, 15.0, 0.5, 0.5, 0.1 };
        double[] B = { 150.0, 150.0, 150.0, 5.0, 5.0, 1.0 };
        double[] K = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        double[] F = { 10.0, 10.0, 10.0, 1.0, 1.0, 1.0 };
        int rtn = robot.EndForceDragControl(1, 0, 0, 0, 1, M, B, K, F, 50, 100);
        Console.WriteLine("force drag control start rtn is{rtn}");
        Thread.Sleep(5000);

        rtn = robot.EndForceDragControl(0, 0, 0, 0, 1, M, B, K, F, 50, 100);
        Console.WriteLine($"force drag control end rtn is{rtn}");

        rtn = robot.ResetAllError();
        Console.WriteLine($"ResetAllError rtn is{rtn}");

        robot.EndForceDragControl(1, 0, 0, 0, 1, M, B, K, F, 50, 100);
        Console.WriteLine($"force drag control start again rtn is{rtn}");
        Thread.Sleep(5000);

        rtn = robot.EndForceDragControl(0, 0, 0, 0, 1, M, B, K, F, 50, 100);
        Console.WriteLine($"force drag control end again rtn is {rtn}");
    }
    
获取力传感器拖动开关状态
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief  获取力传感器拖动开关状态
    * @param  [out] dragState 力传感器辅助拖动控制状态，0-关闭；1-开启
    * @param  [out] sixDimensionalDragState 六维力辅助拖动控制状态，0-关闭；1-开启
    * @return  错误码
    */
    int GetForceAndTorqueDragState(ref int dragState, ref int sixDimensionalDragState);

力传感器自动校零
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief  力传感器自动校零
    * @param  [out] weight 传感器质量 kg 
    * @param  [out] pos 传感器质心 mm
    * @return  错误码
    */
    int ForceSensorAutoComputeLoad(ref double weight, ref DescTran pos);

设置六维力和关节阻抗混合拖动开关及参数
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief  设置六维力和关节阻抗混合拖动开关及参数
    * @param  [in] status 控制状态，0-关闭；1-开启
    * @param  [in] impedanceFlag 阻抗开启标志，0-关闭；1-开启
    * @param  [in] lamdeDain 拖动增益
    * @param  [in] KGain 刚度增益
    * @param  [in] BGain 阻尼增益
    * @param  [in] dragMaxTcpVel 拖动末端最大线速度限制
    * @param  [in] dragMaxTcpOriVel 拖动末端最大角速度限制
    * @return  错误码
    */
    int ForceAndJointImpedanceStartStop(int status, int impedanceFlag, double[] lamdeDain, double[] KGain, double[] BGain, double dragMaxTcpVel, double dragMaxTcpOriVel);


设置力传感器下负载重量
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief  设置力传感器下负载重量
    * @param  [in] weight 负载重量 kg
    * @return  错误码
    */
    int SetForceSensorPayLoad(double weight);

设置力传感器下负载质心
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief  设置力传感器下负载质心
    * @param  [in] x 负载质心x mm 
    * @param  [in] y 负载质心y mm
    * @param  [in] z 负载质心z mm
    * @return  错误码
    */
    int SetForceSensorPayLoadCog(double x, double y, double z);

获取力传感器下负载重量
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief  获取力传感器下负载重量
    * @param  [in] weight 负载重量 kg
    * @return  错误码
    */
    int GetForceSensorPayLoad(ref double weight);

获取力传感器下负载质心
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief  获取力传感器下负载质心
    * @param  [out] x 负载质心x mm 
    * @param  [out] y 负载质心y mm
    * @param  [out] z 负载质心z mm
    * @return  错误码
    */
    int GetForceSensorPayLoadCog(ref double x, ref double y, ref double z);

传送带通讯输入检测
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 传送带通讯输入检测
    * @param [in] timeout 等待超时时间ms
    * @return 错误码
    */
    int ConveyorComDetect(int timeout);

传送带通讯输入检测触发
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 传送带通讯输入检测触发
    * @return 错误码
    */
    int ConveyorComDetectTrigger();

代码示例
+++++++++++++++++++++++++++++
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
  