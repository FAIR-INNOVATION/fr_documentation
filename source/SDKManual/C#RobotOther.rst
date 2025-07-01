其他接口
================

.. toctree:: 
    :maxdepth: 5

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

代码示例
+++++++++
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

获取SSH公钥
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取SSH公钥 
    * @param [out] keygen 公钥
    * @return 错误码 
    */
    int GetSSHKeygen(ref string keygen);

计算指定路径下文件的MD5值
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 计算指定路径下文件的MD5值 
    * @param [in] file_path 文件路径包含文件名，默认Traj文件夹路径为:"/fruser/traj/",如"/fruser/traj/trajHelix_aima_1.txt"
    * @param [out] md5 文件MD5值
    * @return 错误码 
    */
    int ComputeFileMD5(string file_path, ref string md5);

获取机器人急停状态
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取机器人急停状态 
    * @param [out] state 急停状态，0-非急停，1-急停
    * @return 错误码 
    */
    int GetRobotEmergencyStopState(ref byte state);

获取SDK与机器人的通讯状态
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取SDK与机器人的通讯状态 
    * @param [out] state 通讯状态，0-通讯正常，1-通讯异常
    * @return 错误码 
    */
    int GetSDKComState(ref int state)

获取安全停止信号
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取安全停止信号 
    * @param [out] si0_state 安全停止信号SI0，0-无效，1-有效
    * @param [out] si1_state 安全停止信号SI1，0-无效，1-有效
    * @return 错误码 
    */
    int GetSafetyStopState(ref byte si0_state, ref byte si1_state)

获取机器人DH参数补偿值
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取安全停止信号 
    * @param [out] dhCompensation 机器人DH参数补偿值(mm) [cmpstD1,cmpstA2,cmpstA3,cmpstD4,cmpstD5,cmpstD6]
    * @return 错误码 
    */
    int GetDHCompensation(ref double[] dhCompensation)

代码示例
+++++++++
.. code-block:: c#
    :linenos:

    private void btnTestOthers_Click(object sender, EventArgs e)
        {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");
        int rtn = -1;
        double[] dhCompensation = new double[6]{0,0,0,0,0,0};
        rtn = robot.GetDHCompensation(ref dhCompensation);
        Console.WriteLine($"GetDHCompensation:  rtn :{rtn}    {dhCompensation[0]}  {dhCompensation[1]}  {dhCompensation[2]}  {dhCompensation[3]}  {dhCompensation[4]}  {dhCompensation[5]}");
        string ssh = "";
        rtn = robot.GetSSHKeygen(ref ssh);
        Console.WriteLine($"GetSSHKeygen:  ssh {ssh}  rtn  {rtn}");
        string file_path = "/fruser/test.txt";
        string md5 = "";
        robot.ComputeFileMD5(file_path, ref md5);

        byte state = 255;
        rtn = robot.GetRobotEmergencyStopState(ref state);
        Console.WriteLine($"GetRobotEmergencyStopState:  rtn  {rtn}   state {state}");

        int comState = -1;
        rtn = robot.GetSDKComState(ref comState);
        Console.WriteLine($"GetSDKComState:  rtn  {rtn}   state  {comState}");

        byte si0_state = 255;
        byte si1_state = 255;

        rtn = robot.GetSafetyStopState(ref si0_state, ref si1_state);
        Console.WriteLine($"GetSafetyStopState:  rtn  {rtn}   si0_state  {si0_state}   si1_state  {si1_state}");
    }

上传点位表
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 点位表从本地计算机上传至机器人控制器 
    * @param [in] pointTableFilePath 点位表在本地计算机的绝对路径C://test/pointTabl e1.db
    * @return 错误码 
    */
    int PointTableUpLoad(string pointTableFilePath);

下载点位表
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 点位表从机器人控制器下载到本地计算机 
    * @param [in] pointTableName 控制器中的点位表名称：pointTable1.db
    * @param [in] saveFilePath 点位表下载到计算机的路径 C://test/
    * @return 错误码 
    */
    int PointTableDownLoad(string pointTableName, string saveFilePath);

点位表更新Lua程序
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 使用给定的点位表更新lua程序中的点
    * @param [in] pointTableName 控制器中的点位表名称："pointTable1.db", 当点位表为空，即""时，表示将lua程序更新为未应用点位表的初始程序
    * @param [in] luaFileName 要更新的lua文件名称   "test.lua"
    * @param [out] errorStr 点位表更新lua错误信息  
    * @return 错误码 
    */
    int PointTableUpdateLua(string pointTableName, string luaFileName, ref string errorStr);

切换点位表并应用
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 切换点位表并应用
    * @param [in] pointTableName 要切换的点位表名称   "pointTable1.db"
    * @param [out] errorStr 切换点位表错误信息   
    * @return 错误码 
    */
    int PointTableSwitch(string pointTableName, ref string errorStr);

代码示例
+++++++++
.. code-block:: c#
    :linenos:

    private void btnUpload_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");
        int rtn = -1;
        rtn = robot.PointTableUpLoad("C://point_table_test.db");
        Thread.Sleep(2000);
        rtn = robot.PointTableDownLoad("point_table_test.db", "D://zDOWN/");
        string errorStr = "";
        rtn = robot.PointTableUpdateLua("point_table_test.db", "test.lua", ref errorStr);
        Console.WriteLine($"PointTableSwitch rtn  is {rtn}" + errorStr);
        rtn = robot.ProgramLoad("/fruser/test.lua");
        rtn = robot.ProgramRun();
    }

初始化日志参数
+++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /**
    * @brief 初始化日志参数
    * @param [in] logType：输出模式，DIRECT-直接输出；BUFFER-缓冲输出；ASYNC-异步输出
    * @param [in] logLevel：日志过滤等级，ERROR-错误；WARNING-警告;INFO-信息；DEBUG-调试
    * @param [in] filePath: 文件保存路径，如“D://Log/”
    * @param [in] saveFileNum：保存文件个数，同时超出保存文件个数和保存文件天数的文件将被删除
    * @param [in] saveDays: 保存文件天数，同时超出保存文件个数和保存文件天数的文件将被删除
    * @return 错误码
    */
    public int LoggerInit(FrLogType logType = FrLogType.DIRECT, FrLogLevel logLevel = FrLogLevel.ERROR, string filePath = "", int saveFileNum = 10, int saveDays = 10);

设置日志过滤等级
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /**
    * @brief 设置日志过滤等级;
    * @param [in] logLevel: 日志过滤等级，ERROR-错误；WARNING-警告;INFO-信息；DEBUG-调试
    * @return 错误码
    */
    public int SetLoggerLevel(FrLogLevel logLevel);


代码示例
+++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    private void btnTestLog_Click(object sender, EventArgs e)
    {
        robot = new Robot();//实例化机器人对象
        robot.RPC("192.168.58.2"); //与控制箱建立连接
        string path = "D://log/";
        robot.LoggerInit(FrLogType.ASYNC, FrLogLevel.DEBUG, path, 5, 5);
        robot.SetLoggerLevel(FrLogLevel.INFO);
    }

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

代码示例
++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: console
    :linenos:

    private void btnSetProto_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        int protocol = 4098;//ModbusMaster 
        robot.SetExDevProtocol(protocol);

        robot.GetExDevProtocol(ref protocol);
        Console.Writeline("protocol is" + protocol);
    }

末端传感器配置
+++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

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
.. versionadded:: C# SDK-v1.1.0-3.7.8

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
.. versionadded:: C# SDK-v1.1.0-3.7.8

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
.. versionadded:: C# SDK-v1.1.0-3.7.8

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

代码示例
+++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8
    
.. code-block:: c#
    :linenos:

    private void button2_Click_1(object sender, EventArgs e)
    {
        robot.AxleSensorConfig(18, 0, 0, 1);
        int company = -1;
        int type = -1;
        robot.AxleSensorConfigGet(ref company, ref type);
        Console.WriteLine($"company is {company}, type is {type}");
        robot.AxleSensorActivate(1);
        robot.AxleSensorRegWrite(1, 4, 6, 1, 0, 0, 0);       
    }

控制器日志下载
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  控制器日志下载
    * @param [in] savePath 保存文件路径"D://zDown/"
    * @return  错误码
    */
    int RbLogDownload(string savePath);

代码示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button6_Click(object sender, EventArgse)
    {  
        Console.WriteLine("RbLogDownload start");
        int rtn = robot.RbLogDownload(@"D:\zDOWN1\");
        Console.WriteLine($"RbLogDownload rtn is {rtn}");
    }

所有数据源下载
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 所有数据源下载
    * @param [in] savePath 保存文件路径"D://zDown/"
    * @return  错误码
    */
    int AllDataSourceDownload(string savePath);

代码示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button6_Click(object sender, EventArgse)
    {   
        Console.WriteLine("AllDataSourceDownload start");
        int rtn = robot.AllDataSourceDownload(@"D:\zDOWN\");
        Console.WriteLine($"AllDataSourceDownload rtn is {rtn}");
    }

数据备份包下载
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 数据备份包下载
    * @param [in] savePath 保存文件路径"D://zDown/"
    * @return  错误码
    */
    int DataPackageDownload(string savePath);

代码示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button6_Click(object sender, EventArgse)
    {   
        Console.WriteLine("DataPackageDownload start");
        int rtn = robot.DataPackageDownload(@"D:\zDOWN\");
        Console.WriteLine($"DataPackageDownload rtn is {rtn}");
    }

获取控制箱SN码
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取控制箱SN码
    * @param [out] SNCode 控制箱SN码
    * @return 错误码
    */
    int GetRobotSN(string SNCode);

代码示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button6_Click(object sender, EventArgse)
    {   
        string SN = "";
        int rtn = robot.GetRobotSN(ref SN); 
        Console.WriteLine($"robot SN is {SN}");
    }

关闭机器人操作系统
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 关闭机器人操作系统
    * @return 错误码
    */
    int ShutDownRobotOS();

代码示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button6_Click(object sender, EventArgse)
    {   
        int rtn = robot.ShutDownRobotOS();
        Console.WriteLine($"ShutDownRobotOS rtn is {rtn}");
    }

下发SCP指令
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 下发SCP指令
    * @param [in] mode 0-上传（上位机->控制器），1-下载（控制器->上位机）
    * @param [in] sshname 上位机用户名
    * @param [in] sship 上位机ip地址
    * @param [in] usr_file_url 上位机文件路径
    * @param [in] robot_file_url 机器人控制器文件路径
    * @return 错误码
    */
    int SetSSHScpCmd(int mode, string sshname, string sship, string usr_file_url, string robot_file_url);

代码示例
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    private void button46_Click(object sender, EventArgs e)
    {
        string file_path = "/fruser/airlab.lua";
        string md5 = "";
        byte emerg_state = 0;
        byte si0_state = 0;
        byte si1_state = 0;
        int sdk_com_state = 0;

        string ssh_keygen = "";
        int retval = robot.GetSSHKeygen(ref ssh_keygen);
        Console.WriteLine("GetSSHKeygen retval is: {0}", retval);
        Console.WriteLine("ssh key is: {0}", ssh_keygen);

        string ssh_name = "fr";
        string ssh_ip = "192.168.58.45";
        string ssh_route = "/home/fr";
        string ssh_robot_url = "/root/robot/dhpara.config";
        retval = robot.SetSSHScpCmd(1, ssh_name, ssh_ip, ssh_route, ssh_robot_url);
        Console.WriteLine("SetSSHScpCmd retval is: {0}", retval);
        Console.WriteLine("robot url is: {0}", ssh_robot_url);

        robot.ComputeFileMD5(file_path, ref md5);
        Console.WriteLine("md5 is: {0}", md5);
    }

设置宽电压控制箱温度及风扇转速监控参数
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置宽电压控制箱温度及风扇转速监控参数
    * @param [in] enable 0-不使能监测；1-使能监测
    * @param [in] period 监测周期(s),范围1-100
    * @return 错误码
    */
    int SetWideBoxTempFanMonitorParam(int enable, int period);

获取宽电压控制箱温度及风扇转速监控参数
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取宽电压控制箱温度及风扇转速监控参数
    * @param [out] enable 0-不使能监测；1-使能监测
    * @param [out] period 监测周期(s),范围1-100
    * @return 错误码
    */
    int GetWideBoxTempFanMonitorParam(ref int enable, ref int period);

代码示例
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    private void button46_Click(object sender, EventArgs e)
    {
        var pkg = new ROBOT_STATE_PKG(); 
        robot.SetWideBoxTempFanMonitorParam(1, 2);    
        int enable = 0;
        int period = 0;
        robot.GetWideBoxTempFanMonitorParam(ref enable, ref period);
        Console.WriteLine($"GetWideBoxTempFanMonitorParam enable is {enable}   period is {period}");  
        for (int i = 0; i < 100; i++)
        {
            robot.GetRobotRealTimeState(ref pkg);
            Console.WriteLine($"robot ctrl box temp is {pkg.wideVoltageCtrlBoxTemp}, fan current is {pkg.wideVoltageCtrlBoxFanVel}");
            Thread.Sleep(100);
        }       
        int rtn = robot.SetWideBoxTempFanMonitorParam(0, 2);
        Console.WriteLine($"SetWideBoxTempFanMonitorParam rtn is {rtn}");       
        enable = 0;
        period = 0;
        robot.GetWideBoxTempFanMonitorParam(ref enable, ref period);
        Console.WriteLine($"GetWideBoxTempFanMonitorParam enable is {enable}   period is {period}");  
        for (int i = 0; i < 100; i++)
        {
            robot.GetRobotRealTimeState(ref pkg);
            Console.WriteLine($" robot ctrl box temp is {pkg.wideVoltageCtrlBoxTemp}, fan current is {pkg.wideVoltageCtrlBoxFanVel}");
            Thread.Sleep(100);
        }
    }



