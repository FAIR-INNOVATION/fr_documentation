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
    * @brief  获取夹爪运动状态
    * @param  [out] fault  0-无错误，1-有错误
    * @param  [out] staus  0-运动未完成，1-运动完成
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
    * @param [in] followType 跟踪运动类型，0-跟踪运动；1-追检运动
    * @param [in] startDis 追检抓取需要设置， 跟踪起始距离， -1：自动计算(工件到达机器人下方后自动追检)，单位mm， 默认值0
    * @param [in] endDis 追检抓取需要设置，跟踪终止距离， 单位mm， 默认值100
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
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");
        DescPose pos1 = new DescPose(0, 0, 0, 0 ,0 ,0);
        DescPose pos2 = new DescPose(0, 0, 0, 0, 0, 0);

        pos1.tran.x = -351.175;
        pos1.tran.y = 3.389;
        pos1.tran.z = 431.172;
        pos1.rpy.rx = -179.111;
        pos1.rpy.ry = -0.241;
        pos1.rpy.rz = 90.388;

        pos2.tran.x = -333.654;
        pos2.tran.y = -229.003;
        pos2.tran.z = 404.335;
        pos2.rpy.rx = -179.139;
        pos2.rpy.ry = -0.779;
        pos2.rpy.rz = 91.269;
        int rtn = -1;

        double[] cmp = new double[3] { 0, 9.99, 0};
        rtn = robot.ConveyorCatchPointComp(cmp);
        if(rtn != 0)
        {
            return;
        }
        Console.WriteLine($"ConveyorCatchPointComp: rtn  {rtn}");

        rtn = robot.MoveCart(pos1, 0, 0, 100.0f, 180.0f, 100.0f, -1.0f, -1);
        Console.WriteLine($"MoveCart: rtn  {rtn}");

        rtn = robot.ConveyorIODetect(10000);
        Console.WriteLine($"ConveyorIODetect: rtn  {rtn}");

        robot.ConveyorGetTrackData(1);
        rtn = robot.ConveyorTrackStart(1);
        Console.WriteLine($"ConveyorTrackStart: rtn  {rtn}");

        rtn = robot.ConveyorTrackMoveL("cvrCatchPoint", 0, 0, 100.0f, 0.0f, 100.0f, -1.0f, 0, 0);
        Console.WriteLine($"ConveyorTrackMoveL: rtn  {rtn}");

        rtn = robot.MoveGripper(1, 59, 43, 21, 30000, 0);
        Console.WriteLine($"MoveGripper: rtn  {rtn}");

        rtn = robot.ConveyorTrackMoveL("cvrRaisePoint", 0, 0, 100.0f, 0.0f, 100.0f, -1.0f, 0, 0);
        Console.WriteLine($"ConveyorTrackMoveL: rtn  {rtn}");

        rtn = robot.ConveyorTrackEnd();
        Console.WriteLine($"ConveyorTrackEnd: rtn  {rtn}");

        rtn = robot.MoveCart(pos2, 0, 0, 100.0f, 180.0f, 100.0f, -1.0f, -1);
        Console.WriteLine($"MoveCart: rtn  {rtn}");

        rtn = robot.MoveGripper(1, 100, 43, 21, 30000, 0);
        Console.WriteLine($"MoveGripper: rtn  {rtn}");
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
    * @return  错误码
    */
    int SetAxleLuaEnableDeviceType(int forceSensorEnable, int gripperEnable, int IOEnable);

获取末端LUA末端设备启用类型
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取末端LUA末端设备启用类型
    * @param [out] forceSensorEnable 力传感器启用状态，0-不启用；1-启用
    * @param [out] gripperEnable 夹爪启用状态，0-不启用；1-启用
    * @param [out] IOEnable IO设备启用状态，0-不启用；1-启用
    * @return  错误码
    */
    int GetAxleLuaEnableDeviceType(ref int forceSensorEnable, ref int gripperEnable, ref int IOEnable);

获取当前配置的末端设备
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取当前配置的末端设备
    * @param [out] forceSensorEnable 力传感器启用设备编号 0-未启用；1-启用
    * @param [out] gripperEnable 夹爪启用设备编号，0-不启用；1-启用
    * @param [out] IODeviceEnable IO设备启用设备编号，0-不启用；1-启用
    * @return  错误码
    */
    int GetAxleLuaEnableDevice(ref int[] forceSensorEnable, ref int[] gripperEnable, ref int[] IODeviceEnable);

设置启用夹爪动作控制功能
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置启用夹爪动作控制功能
    * @param [in] id 夹爪设备编号
    * @param [in] func func[0]-夹爪使能；func[1]-夹爪初始化；2-位置设置；3-速度设置；4-力矩设置；6-读夹爪状态；7-读初始化状态；8-读故障码；9-读位置；10-读速度；11-读力矩
    * @return  错误码
    */
    int SetAxleLuaGripperFunc(int id, int[] func);

获取启用夹爪动作控制功能
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取启用夹爪动作控制功能
    * @param [in] id 夹爪设备编号
    * @param [out] func func[0]-夹爪使能；func[1]-夹爪初始化；2-位置设置；3-速度设置；4-力矩设置；6-读夹爪状态；7-读初始化状态；8-读故障码；9-读位置；10-读速度；11-读力矩
    * @return  错误码
    */
    int GetAxleLuaGripperFunc(int id, ref int[] func);

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
        robot.AxleLuaUpload("D://zUP/AXLE_LUA_End_JunDuo_Xinjingcheng.lua");

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
        robot.SetAxleLuaEnableDeviceType(0, 1, 0);

        int forceEnable = 0;
        int gripperEnable = 0;
        int ioEnable = 0;
        robot.GetAxleLuaEnableDeviceType(ref forceEnable, ref gripperEnable, ref ioEnable);
        Console.WriteLine("GetAxleLuaEnableDeviceType param is {0} {1} {2}", forceEnable, gripperEnable, ioEnable);

        int[] func = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
        robot.SetAxleLuaGripperFunc(1, func);
        int[] getFunc = new int[16];
        robot.GetAxleLuaGripperFunc(1, ref getFunc);
        int[] getforceEnable = new int[16];
        int[] getgripperEnable = new int[16];
        int[] getioEnable = new int[16];
        robot.GetAxleLuaEnableDevice(ref getforceEnable, ref getgripperEnable, ref getioEnable);
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
        Thread.Sleep(2000);
        robot.ActGripper(1, 1);
        Thread.Sleep(2000);
        robot.MoveGripper(1, 90, 10, 100, 50000, 0, 0, 0, 0, 0);
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


