机器人外设
============

.. toctree:: 
    :maxdepth: 5

配置夹爪
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  配置夹爪
    * @param  [in] config .company  夹爪厂商，1-Robotiq，2-慧灵，3-天机，4-大寰，5-知行
    * @param  [in] config .device  设备号，Robotiq(0-2F-85系列)，慧灵(0-NK系列,1-Z-EFG-100)，天机(0-TEG-110)，大寰(0-PGI-140)，知行(0-CTPM2F20)
    * @param  [in] config .softvesion  软件版本号，暂不使用，默认为0
    * @param  [in] config .bus 设备挂在末端总线位置，暂不使用，默认为0
    * @return  错误码
    */
    int SetGripperConfig(DeviceConfig config);

获取夹爪配置
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取夹爪配置
    * @param  [out] config .company  夹爪厂商，1-Robotiq，2-慧灵，3-天机，4-大寰，5-知行
    * @param  [out] config .device  设备号，Robotiq(0-2F-85系列)，慧灵(0-NK系列,1-Z-EFG-100)，天机(0-TEG-110)，大寰(0-PGI-140)，知行(0-CTPM2F20)
    * @param  [out] config .softvesion  软件版本号，暂不使用，默认为0
    * @param  [out] config .bus 设备挂在末端总线位置，暂不使用，默认为0
    * @return  错误码
    */
    int GetGripperConfig(DeviceConfig config);

激活夹爪
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  激活夹爪
    * @param  [in] index  夹爪编号
    * @param  [in] act  0-复位，1-激活
    * @return  错误码
    */
    int ActGripper(int index, int act); 

控制夹爪
++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    * @return 错误码
    */
    int MoveGripper(int index, int pos, int vel, int force, int max_time, int block, int type, double rotNum, int rotVel, int rotTorque); 

获取夹爪运动状态
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取夹爪运动状态
    * @return List[0]:错误码; List[1] : fault  0-无错误，1-有错误; List[2]: staus  0-运动未完成，1-运动完成
    */
    List<Integer> GetGripperMotionDone(); 

获取夹爪激活状态
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取夹爪激活状态
    * @return  List[0]:错误码; List[1] : fault  0-无错误，1-有错误; List[2]: status  bit0~bit15对应夹爪编号0~15，bit=0为未激活，bit=1为激活
    */
    List<Number> GetGripperActivateStatus()

获取夹爪位置
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取夹爪位置
    * @return  List[0]:错误码; List[1] : fault  0-无错误，1-有错误; List[2]: position  位置百分比，范围0~100%
    */
    List<Number> GetGripperCurPosition()

获取夹爪速度
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取夹爪速度
    * @return  List[0]:错误码; List[1] : fault  0-无错误，1-有错误; List[2]: speed  速度百分比，范围0~100%
    */
    List<Number> GetGripperCurSpeed()

获取夹爪电流
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取夹爪电流
    * @return  List[0]:错误码; List[1] : fault  0-无错误，1-有错误; List[2]: current  电流百分比，范围0~100%
    */
    List<Number> GetGripperCurCurrent()

获取夹爪电压
++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取夹爪电压
    * @return List[0]:错误码; List[1] : fault  0-无错误，1-有错误; List[2]:voltage  电压,单位0.1V
    */
    List<Number> GetGripperVoltage()

获取夹爪温度
++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取夹爪温度
    * @return List[0]:错误码; List[1] : fault  0-无错误，1-有错误; List[2]:temp  温度，单位℃
    */
    List<Number> GetGripperTemp()

计算预抓取点-视觉
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 计算预抓取点-视觉 
    * @param [in] desc_pos  抓取点笛卡尔位姿
    * @param [in] zlength   z轴偏移量
    * @param [in] zangle    绕z轴旋转偏移量
    * @param [out] pre_pos  获取点
    * @return 错误码 
    */ 
    int ComputePrePick(DescPose desc_pos, double zlength, double zangle, DescPose pre_pos);

计算撤退点-视觉
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 计算撤退点-视觉 
    * @param [in] desc_pos  抓取点笛卡尔位姿
    * @param [in] zlength   z轴偏移量 
    * @param [in] zangle    绕z轴旋转偏移量
    * @param [out] post_poss 撤退点
    * @return 错误码 
    */ 
    int ComputePostPick(DescPose desc_pos, double zlength, double zangle, DescPose post_pos);

机器人夹爪操作代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestGripper(Robot robot)
    {
        int company = 4;
        int device = 0;
        int softversion = 0;
        int bus = 2;
        int index = 2;
        int act = 0;
        int max_time = 30000;
        int block = 0;

        int current_pos = 0;
        int current = 0;
        int voltage = 0;
        int temp = 0;
        int speed = 0;

        DeviceConfig cnn=new DeviceConfig(company,device,softversion,bus);
        robot.SetGripperConfig(cnn);
        robot.GetGripperConfig(cnn);

        robot.ActGripper(index, act);
        robot.Sleep(1000);
        act = 1;
        robot.ActGripper(index, act);
        robot.Sleep(1000);

        robot.MoveGripper(index, 100, 50, 50, max_time, block, 0, 0, 0, 0);
        robot.Sleep(1000);
        robot.MoveGripper(index, 0, 50, 0, max_time, block, 0, 0, 0, 0);

        List<Integer> stat=new ArrayList<>();
        stat=robot.GetGripperMotionDone();

        List<Number> list=new ArrayList<>();
        list=robot.GetGripperActivateStatus();

        list=robot.GetGripperCurPosition();

        list=robot.GetGripperCurCurrent();

        list=robot.GetGripperVoltage();

        list=robot.GetGripperTemp();

        list=robot.GetGripperCurSpeed();

        int retval = 0;
        DescPose prepick_pose = new DescPose(){};
        DescPose postpick_pose = new DescPose(){};

        DescPose p1Desc=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose p2Desc=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        retval = robot.ComputePrePick(p1Desc, 10, 0, prepick_pose);

        retval = robot.ComputePostPick(p2Desc, -10, 0, postpick_pose);
        return 0;
    }

获取旋转夹爪的旋转圈数
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取旋转夹爪的旋转圈数
    * @return List[0]:错误码 List[1]: 0-无错误，1-有错误 List[2]:旋转圈数
    */
    List<Number> GetGripperRotNum(); 

获取旋转夹爪的旋转速度百分比
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取旋转夹爪的旋转速度百分比
    * @return List[0]:错误码 List[1]: 0-无错误，1-有错误 List[2]:旋转速度百分比
    */
    List<Number> GetGripperRotSpeed(); 

获取旋转夹爪的旋转力矩百分比
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取旋转夹爪的旋转力矩百分比
    * @return List[0]:错误码 List[1]: 0-无错误，1-有错误 List[2]:旋转力矩百分比
    */
    List<Number> GetGripperRotTorque(); 

代码示获取旋转夹爪状态代码示例
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestRotGripperState(Robot robot)
    {
        int fault = 0;
        List<Number> rotNum=new ArrayList<>();
        List<Number> rotSpeed=new ArrayList<>();
        List<Number> rotTorque=new ArrayList<>();

        rotNum=robot.GetGripperRotNum();
        rotSpeed=robot.GetGripperRotSpeed();
        rotTorque=robot.GetGripperRotTorque();
        System.out.println("gripper rot num :"+rotNum.get(2)+ ", gripper rotSpeed :"+rotSpeed.get(2)+",gripper rotTorque : "+rotTorque.get(2));

        return 0;
    }

传动带启动、停止
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  传动带启动、停止
    * @param  [in] status 状态，1-启动，0-停止
    * @return  错误码
    */
    int ConveyorStartEnd(int status);

记录IO检测点
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  记录IO检测点
    * @return  错误码
    */
    int ConveyorPointIORecord();

记录A点
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  记录A点
    * @return  错误码
    */
    int ConveyorPointARecord(); 

记录参考点
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  记录参考点
    * @return  错误码
    */
    int ConveyorRefPointRecord();

记录B点
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  记录B点
    * @return 错误码
    */
    int ConveyorPointBRecord(); 

传送带工件IO检测
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 传送带工件IO检测
    * @param [in] max_t 最大检测时间，单位ms
    * @return 错误码 
    */ 
    int ConveyorIODetect(int max_t);

获取物体当前位置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取物体当前位置
    * @param [in] mode 1-跟踪抓取，2-跟踪运动，3-TPD跟踪
    * @return 错误码 
    */ 
    int ConveyorGetTrackData(int mode);

传动带跟踪开始
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 传动带跟踪开始
    * @param [in] status 状态，1-启动，0-停止
    * @return 错误码 
    */ 
    int ConveyorTrackStart(int status);

传动带跟踪停止
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 传动带跟踪停止
    * @return 错误码 
    */ 
    int ConveyorTrackEnd();

传动带参数配置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /**
    * @brief  传动带参数配置
    * @param [in] encChannel 编码器通道 1~2
    * @param [in] resolution 编码器转一圈的脉冲数
    * @param [in] lead 编码器转一圈传送带行走距离
    * @param [in] wpAxis 工件坐标系编号 针对跟踪运动功能选择工件坐标系编号，跟踪抓取、TPD跟踪设为0
    * @param [in] vision 是否配视觉  0 不配  1 配
    * @param [in] speedRadio 速度比  针对传送带跟踪抓取选项（1-100）  其他选项默认为1
    * @param [in] followType 跟踪运动类型，0-跟踪运动；1-追检运动
    * @param [in] startDis 追检抓取需要设置， 跟踪起始距离， -1：自动计算(工件到达机器人下方后自动追检)，单位mm， 默认值0
    * @param [in] endDis 追检抓取需要设置，跟踪终止距离， 单位mm， 默认值100
    * @return 错误码
    */
    int ConveyorSetParam(int encChannel, int resolution, double lead, int wpAxis, int vision, double speedRadio, int followType, int startDis, int endDis); 

设置传动带抓取点补偿
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置传动带抓取点补偿
    * @param [in] cmp 补偿位置 double[3]{x, y, z}
    * @return 错误码 
    */ 
    int ConveyorCatchPointComp(Object[] cmp);

传动带直线运动
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 直线运动
    * @param [in] name 运动点描述
    * @param [in] tool 工具坐标号，范围[0~14]
    * @param [in] wobj 工件坐标号，范围[0~14]
    * @param [in] vel 速度百分比，范围[0~100]
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl 速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @return 错误码 
    */ 
    int ConveyorTrackMoveL(String name, int tool, int wobj, double vel, double acc, double ovl, double blendR);   

传送带通讯输入检测
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /** 
    * @brief 传送带通讯输入检测
    * @param [in] timeout 等待超时时间ms
    * @return 错误码
    */
    int ConveyorComDetect(int timeout);

传送带通讯输入检测触发
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /** 
    * @brief 传送带通讯输入检测触发
    * @param [in] timeout 等待超时时间ms
    * @return 错误码
    */
    int ConveyorComDetectTrigger();

机器人传送带操作示例程序
++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestConveyor(Robot robot)
    {
        int retval = 0;

        retval = robot.ConveyorStartEnd(1);

        retval = robot.ConveyorPointIORecord();

        retval = robot.ConveyorPointARecord();

        retval = robot.ConveyorRefPointRecord();

        retval = robot.ConveyorPointBRecord();

        retval = robot.ConveyorStartEnd(0);

        retval = 0;

        retval = robot.ConveyorSetParam(1,10000,200,0,0,20,0,0,100);

        Object[] cmp = new Object[]{ 0.0, 0.0, 0.0 };
        retval = robot.ConveyorCatchPointComp(cmp);

        int index = 1;
        int max_time = 30000;
        int block = 0;
        retval = 0;

        DescPose p1Desc=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose p2Desc=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);


        retval = robot.MoveCart(p1Desc, 1, 0, 100.0, 100.0, 100.0, -1.0, -1);

        retval = robot.WaitMs(1);

        retval = robot.ConveyorTrackStart(1);

        retval = robot.ConveyorTrackMoveL("cvrCatchPoint", 1, 0, 100, 100, 100, -1.0);

        retval = robot.MoveGripper(index, 51, 40, 30, max_time, block, 0, 0, 0, 0);

        retval = robot.ConveyorTrackMoveL("cvrRaisePoint", 1, 0, 100, 100, 100, -1.0);

        retval = robot.ConveyorTrackEnd();

        robot.MoveCart(p2Desc, 1, 0, 100.0, 100.0, 100.0, -1.0, -1);

        retval = robot.MoveGripper(index, 100, 40, 10, max_time, block, 0, 0, 0, 0);

        return 0;
    }

末端传感器配置
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 末端传感器配置
    * @param [in] config idCompany 厂商，18-JUNKONG；25-HUIDE
    * @param [in] config idDevice 类型，0-JUNKONG/RYR6T.V1.0
    * @param [in] config idSoftware 软件版本，0-J1.0/HuiDe1.0(暂未开放)
    * @param [in] config idBus 挂载位置，1-末端1号口；2-末端2号口...8-末端8号口(暂未开放)
    * @return 错误码
    */
    int AxleSensorConfig(DeviceConfig config);

获取末端传感器配置
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取末端传感器配置
    * @param [out] config idCompany 厂商，18-JUNKONG；25-HUIDE
    * @param [out] config idDevice 类型，0-JUNKONG/RYR6T.V1.0
    * @return 错误码
    */
    int AxleSensorConfigGet(DeviceConfig config);

末端传感器激活
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 末端传感器激活
    * @param [in] actFlag 0-复位；1-激活
    * @return 错误码
    */
    int AxleSensorActivate(int actFlag);

末端传感器寄存器写入
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 末端传感器寄存器写入
    * @param [in] devAddr  设备地址编号 0-255
    * @param [in] regHAddr 寄存器地址高8位
    * @param [in] regLAddr 寄存器地址低8位
    * @param [in] regNum  寄存器个数 0-255
    * @param [in] data1 写入寄存器数值1
    * @param [in] data2 写入寄存器数值2
    * @param [in] isNoBlock 0-阻塞；1-非阻塞
    * @return 错误码
    */
    int AxleSensorRegWrite(int devAddr, int regHAddr, int regLAddr, int regNum, int data1, int data2, int isNoBlock);

末端传感器代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAxleSensor(Robot robot)
    {
        DeviceConfig con=new DeviceConfig(18,0,0,1);
        robot.AxleSensorConfig(con);
        int company = -1;
        int type = -1;
        robot.AxleSensorConfigGet(con);

        int rtn = robot.AxleSensorActivate(1);

        robot.Sleep(1000);

        rtn = robot.AxleSensorRegWrite(1, 4, 6, 1, 0, 0, 0);
        return 0;
    }

获取机器人外设协议
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取机器人外设协议
    * @return List[0]:错误码; List[1] : int protocol 机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster 
    */
    List<Integer> GetExDevProtocol();

设置机器人外设协议
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置机器人外设协议
    * @param [in] protocol 机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 错误码 
    */
    int SetExDevProtocol(int protocol);

设置机器人外设协议示例程序
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestExDevProtocol(Robot robot)
    {
        int protocol = 4096;
        int rtn = robot.SetExDevProtocol(protocol);
        List<Integer> integer=new ArrayList<>();
        integer = robot.GetExDevProtocol();

        return 0;
    }

获取末端通讯参数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取末端通讯参数
    * @param [out] param 末端通讯参数
    * @return 错误码 
    */
    int GetAxleCommunicationParam(AxleComParam param)

设置末端通讯参数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置末端通讯参数
    * @param [in] param 末端通讯参数
    * @return 错误码 
    */
    int SetAxleCommunicationParam(AxleComParam param)

设置末端文件传输类型
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置末端文件传输类型
    * @param [in] type 1-MCU升级文件；2-LUA文件
    * @return  错误码
    */
    public int SetAxleFileType(int type)

设置启用末端LUA执行
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置启用末端LUA执行
    * @param [in] enable 0-不启用；1-启用
    * @return  错误码
    */
    public int SetAxleLuaEnable(int enable)

末端LUA文件异常错误恢复
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 末端LUA文件异常错误恢复
    * @param [in] status 0-不恢复；1-恢复
    * @return  错误码
    */
    public int SetRecoverAxleLuaErr(int status)

获取末端LUA执行使能状态
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取末端LUA执行使能状态
    * @param [out] status[0]: 0-未使能；1-已使能
    * @return  错误码
    */
    int GetAxleLuaEnableStatus(int[] status)

设置末端LUA末端设备启用类型
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置末端LUA末端设备启用类型
    * @param forceSensorEnable 力传感器启用状态，0-不启用；1-启用
    * @param gripperEnable 夹爪启用状态，0-不启用；1-启用
    * @param IOEnable IO设备启用状态，0-不启用；1-启用
    * @return  错误码
    */
    public int SetAxleLuaEnableDeviceType(int forceSensorEnable, int gripperEnable, int IOEnable)

获取末端LUA末端设备启用类型
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 获取末端LUA末端设备启用类型
     * @param enable enable[0]:forceSensorEnable 力传感器启用状态，0-不启用；1-启用
     * @param enable enable[1]:gripperEnable 夹爪启用状态，0-不启用；1-启用
     * @param enable enable[2]:IOEnable IO设备启用状态，0-不启用；1-启用
     * @return  错误码
     */
    public int GetAxleLuaEnableDeviceType(int[] enable)

获取当前配置的末端设备
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 获取当前配置的末端设备
     * @param forceSensorEnable 力传感器启用设备编号 0-未启用；1-启用
     * @param gripperEnable 夹爪启用设备编号，0-不启用；1-启用
     * @param IODeviceEnable IO设备启用设备编号，0-不启用；1-启用
     * @return  错误码
     */
    public int GetAxleLuaEnableDevice(int[] forceSensorEnable, int[] gripperEnable, int[] IODeviceEnable)

设置启用夹爪动作控制功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 设置启用夹爪动作控制功能
     * @param id 夹爪设备编号
     * @param func func[0]-夹爪使能；func[1]-夹爪初始化；2-位置设置；3-速度设置；4-力矩设置；6-读夹爪状态；7-读初始化状态；8-读故障码；9-读位置；10-读速度；11-读力矩
     * @return  错误码
     */
    public int SetAxleLuaGripperFunc(int id, int[] func)

获取启用夹爪动作控制功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 获取启用夹爪动作控制功能
     * @param id 夹爪设备编号
     * @param func func[0]-夹爪使能；func[1]-夹爪初始化；2-位置设置；3-速度设置；4-力矩设置；6-读夹爪状态；7-读初始化状态；8-读故障码；9-读位置；10-读速度；11-读力矩
     * @return  错误码
     */
    public int GetAxleLuaGripperFunc(int id, int[] func)

机器人Ethercat从站文件写入
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 机器人Ethercat从站文件写入
     * @param type 从站文件类型，1-升级从站文件；2-升级从站配置文件
     * @param slaveID 从站号
     * @param fileName 上传文件名
     * @return  错误码
     */
    public int SlaveFileWrite(int type, int slaveID, String fileName)

上传末端Lua开放协议文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 上传末端Lua开放协议文件
     * @param filePath 本地lua文件路径名 ".../AXLE_LUA_End_DaHuan.lua"
     * @return 错误码
     */
    public int AxleLuaUpload(String filePath)

机器人Ethercat从站进入boot模式
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 机器人Ethercat从站进入boot模式
     * @return  错误码
     */
    public int SetSysServoBootMode()

机器人末端LUA文件操作代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAxleLua(Robot robot)
    {
        robot.AxleLuaUpload("D://zUP/AXLE_LUA_End_DaHuan.lua");

        AxleComParam param=new AxleComParam(7, 8, 1, 0, 5, 3, 1);
        robot.SetAxleCommunicationParam(param);

        robot.GetAxleCommunicationParam(param);

        robot.SetAxleLuaEnable(1);
        int[] luaEnableStatus = new int[]{0};
        robot.GetAxleLuaEnableStatus(luaEnableStatus);
        robot.SetAxleLuaEnableDeviceType(0, 1, 0);

        int forceEnable = 0;
        int gripperEnable = 0;
        int ioEnable = 0;
        int [] enable=new int[]{0,0,0};
        robot.GetAxleLuaEnableDeviceType(enable);

        int[] func = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
        robot.SetAxleLuaGripperFunc(1, func);
        int[] getFunc = { 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
        robot.GetAxleLuaGripperFunc(1, getFunc);
        int[] getforceEnable = { 0,0,0,0,0,0,0,0};
        int[] getgripperEnable = { 0,0,0,0,0,0,0,0};
        int[] getioEnable = { 0,0,0,0,0,0,0,0};
        robot.GetAxleLuaEnableDevice(getforceEnable, getgripperEnable, getioEnable);
        for (int i = 0; i < 8; i++)
        {
            System.out.println(getforceEnable[i]);
        }
        System.out.println("getgripperEnable status : ");
        for (int i = 0; i < 8; i++)
        {
            System.out.println(getgripperEnable[i]);
        }
        System.out.println("getioEnable status : ");
        for (int i = 0; i < 8; i++)
        {
            System.out.println(getioEnable[i]);
        }
        robot.ActGripper(1, 0);
        robot.Sleep(2000);
        robot.ActGripper(1, 1);
        robot.Sleep(2000);
        robot.MoveGripper(1, 90, 10, 100, 50000, 0, 0, 0, 0, 0);
        int pos = 0;
        while (true)
        {
            ROBOT_STATE_PKG pkg=new ROBOT_STATE_PKG();
            pkg=robot.GetRobotRealTimeState();
            System.out.println("gripper pos is:"+pkg.gripper_position);
            robot.Sleep(100);
        }

    }

获取SmartTool按钮状态
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /**
    * @brief 获取SmartTool按钮状态
    * @param [out] state SmartTool手柄按钮状态;(bit0:0-通信正常；1-通信掉线；bit1-撤销操作；bit2-清空程序；bit3-A键；bit4-B键；bit5-C键；bit6-D键；bit7-E键；bit8-IO键；bit9-手自动；bit10开始)
    * @return 错误码
    */
    int GetSmarttoolBtnState(int[] state)

SmartTool按钮代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args) 
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true, 100, 500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn == 0) {
            System.out.println("rpc连接 success");
        } else {
            System.out.println("rpc连接 fail");
            return;
        }

        int[] state = {0};
        while (true)
        {
            robot.GetSmarttoolBtnState(state);

            String binaryString = String.format("%32s", Integer.toBinaryString(state[0])).replace(' ', '0');
            System.out.println("GetSmarttoolBtnState:"+binaryString);
            robot.Sleep(100);
        }
    }