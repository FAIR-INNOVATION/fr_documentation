数据结构说明
================

.. toctree:: 
    :maxdepth: 5

关节位置数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 关节位置数据类型 
    */  
    struct JointPos
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jPos;   /* 六个关节位置，单位deg */
    }

笛卡尔空间位置数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 笛卡尔空间位置数据类型
    */
    struct DescTran
    {
        public double x;    /* x轴坐标，单位mm  */
        public double y;    /* y轴坐标，单位mm  */
        public double z;    /* z轴坐标，单位mm  */
    }

欧拉角姿态数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 欧拉角姿态数据类型
    */
    struct Rpy
    {
    public double rx;   /* 绕固定轴X旋转角度，单位：deg  */
    public double ry;   /* 绕固定轴Y旋转角度，单位：deg  */
    public double rz;   /* 绕固定轴Z旋转角度，单位：deg  */
    }

笛卡尔空间位姿数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    *@brief 笛卡尔空间位姿类型
    */
    struct DescPose
    {
        public DescTran tran;     /* 笛卡尔空间位置  */
        public Rpy rpy;			/* 笛卡尔空间姿态  */
    }

扩展轴位置数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 扩展轴位置数据类型
    */
    struct ExaxisPos
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public double[] ePos;   /* 四个扩展轴位置，单位mm */
    }

力矩传感器数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 力传感器的受力分量和力矩分量
    */
    struct ForceTorque
    {
        public double fx;  /* 沿x轴受力分量，单位N  */
        public double fy;  /* 沿y轴受力分量，单位N  */
        public double fz;  /* 沿z轴受力分量，单位N  */
        public double tx;  /* 绕x轴力矩分量，单位Nm */
        public double ty;  /* 绕y轴力矩分量，单位Nm */
        public double tz;  /* 绕z轴力矩分量，单位Nm */
    }

螺旋参数数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public struct SpiralParam
    {
        public int circle_num;           /* 螺旋圈数  */
        public float circle_angle;         /* 螺旋倾角  */
        public float rad_init;             /* 螺旋初始半径，单位mm  */
        public float rad_add;              /* 半径增量  */
        public float rotaxis_add;          /* 转轴方向增量  */
        public uint rot_direction;  /* 旋转方向，0-顺时针，1-逆时针  */
        public int velAccMode;      // 速度加速度参数模式：0-角速度恒定；1-线速度恒定
        public SpiralParam(int num, float angle, float initRad, float addRad, float axisAdd, uint direction, int mode)
        {
            circle_num = num;
            circle_angle = angle;
            rad_init = initRad;
            rad_add = addRad;
            rotaxis_add = axisAdd;
            rot_direction = direction;
            velAccMode = mode;
        }
    }

扩展轴状态类型
+++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /**
    * @brief  扩展轴状态类型
    */
    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct ROBOT_AUX_STATE
    {
        public byte servoId;           //伺服驱动器ID号
        public int servoErrCode;       //伺服驱动器故障码
        public int servoState;         //伺服驱动器状态
        public double servoPos;        //伺服当前位置
        public float servoVel;         //伺服当前速度
        public float servoTorque;      //伺服当前转矩
    }

焊接中断状态
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct WELDING_BREAKOFF_STATE
    {
        public byte breakOffState;  // 焊接中断状态
        public byte weldArcState;   // 焊接电弧中断状态
    }

机器人状态反馈结构体类型
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    /**
    * @brief  机器人状态反馈结构体类型
    */
    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public class ROBOT_STATE_PKG
    {
        public UInt16 frame_head;           //帧头 0x5A5A
        public byte frame_cnt;              // 帧计数
        public UInt16 data_len;             //数据长度  5
        public byte program_state;          // 程序运行状态，1-停止；2-运行；3-暂停；
        public byte robot_state;            // 机器人运动状态，1-停止；2-运行；3-暂停；4-拖动
        public int main_code;               // 主故障码
        public int sub_code;                // 子故障码
        public byte robot_mode;             // 机器人模式，1-手动模式；0-自动模式；

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jt_cur_pos;         // 6个轴当前关节位置，单位deg
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] tl_cur_pos;         // 工具当前位置
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] flange_cur_pos;     // 末端法兰当前位置
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] actual_qd;          // 当前6个关节速度，单位deg/s
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] actual_qdd;         // 当前6个关节加速度，单位deg/s^2
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
        public double[] target_TCP_CmpSpeed;// TCP合成指令速度(位置,姿态)
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] target_TCP_Speed;   // TCP指令速度
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
        public double[] actual_TCP_CmpSpeed;// TCP合成实际速度
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] actual_TCP_Speed;   // TCP实际速度
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jt_cur_tor;         // 6个轴当前扭矩，单位N·m

        public int tool;                    // 应用的工具坐标系编号
        public int user;                    // 应用的工件坐标系编号
        public byte cl_dgt_output_h;        // 控制箱数字量IO输出15-8
        public byte cl_dgt_output_l;        // 控制箱数字量IO输出7-0
        public byte tl_dgt_output_l;        // 工具数字量IO输出7-0，仅bit0-bit1有效
        public byte cl_dgt_input_h;         // 控制箱数字量IO输入15-8
        public byte cl_dgt_input_l;         // 控制箱数字量IO输入7-0
        public byte tl_dgt_input_l;         // 工具数字量IO输入7-0，仅bit0-bit1有效

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
        public UInt16[] cl_analog_input;        //控制箱模拟量输入
        public UInt16 tl_anglog_input;          //工具模拟量输入                            

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] ft_sensor_raw_data; // 力矩传感器原始数据
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] ft_sensor_data;     // 力矩传感器数据
        public byte ft_sensor_active;       // 力矩传感器激活状态，0-复位，1-激活

        public byte EmergencyStop;          // 急停标志，0-未按下，1-按下
        public int motion_done;             // 运动到位信号，1-到位，0-未到位
        public byte gripper_motiondone;     // 夹爪运动完成信号，1-完成，0-未完成
        public int mc_queue_len;            // 运动指令队列长度
        public byte collisionState;         // 碰撞检测，1-碰撞，0-无碰撞
        public int trajectory_pnum;         // 轨迹点编号
        public byte safety_stop0_state;     // 安全停止信号SI0
        public byte safety_stop1_state;     // 安全停止信号SI1
        public byte gripper_fault_id;       // 错误夹爪号
        public UInt16 gripper_fault;     /* 夹爪故障 */
        public UInt16 gripper_active;    /* 夹爪激活状态 */
        public byte gripper_position;       // 夹爪位置
        public byte gripper_speed;       /* 夹爪速度 */
        public byte gripper_current;     /* 夹爪电流 */
        public int gripper_temp;            // 夹爪温度
        public int gripper_voltage;         // 夹爪电压

        public ROBOT_AUX_STATE auxState;   // 485扩展轴状态

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public EXT_AXIS_STATUS[] extAxisStatus; // UDP扩展轴状态

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
        public UInt16[] extDIState;        //扩展DI输入
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
        public UInt16[] extDOState;        //扩展DO输出
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public UInt16[] extAIState;        //扩展AI输入
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public UInt16[] extAOState;        //扩展AO输出

        public int rbtEnableState;          // 机器人使能状态

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jointDriverTorque;      // 机器人关节驱动器扭矩
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jointDriverTemperature; // 机器人关节驱动器温度

        public ROBOT_TIME robotTime;        // 机器人系统时间
        public int softwareUpgradeState;    // 机器人软件升级状态
        public UInt16 endLuaErrCode;    //末端LUA运行状态 

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
        public  UInt16[] cl_analog_output;  //控制箱模拟量输出				  Control box analog output
        public UInt16 tl_analog_output;     //工具模拟量输出				  Tool analog output

        public float gripperRotNum;         // 旋转夹爪当前旋转圈数
        public byte gripperRotSpeed;        // 旋转夹爪当前旋转速度百分比
        public byte gripperRotTorque;       // 旋转夹爪当前旋转力矩百分比

        public WELDING_BREAKOFF_STATE weldingBreakOffState; // 焊接中断状态

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jt_tgt_tor;         // 关节指令力矩
        public int smartToolState;          // SmartTool手柄按钮状态
        public float wideVoltageCtrlBoxTemp; // 宽电压控制箱温度
        public UInt16 wideVoltageCtrlBoxFanVel;   //宽电压控制箱风扇电流（mA）

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] toolCoord;          // 当前工具坐标系数值；x,y,z,rx,ry,rz
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] wobjCoord;          // 当前工件坐标系数值；x,y,z,rx,ry,rz
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] extoolCoord;        // 当前外部工具坐标系数值；x,y,z,rx,ry,rz
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] exAxisCoord;        // 当前扩展轴坐标系数值；x,y,z,rx,ry,rz

        public double load;                 // 负载质量
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 3)]
        public double[] loadCog;            // 负载质心
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] lastServoTarget;    // 队列中最后一个ServoJ目标位置
        public int servoJCmdNum;            // servoJ指令计数

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] targetJointPos;     // 6个关节指令位置，单位°
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] targetJointVel;     // 6个关节指令速度，单位°/s
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] targetJointAcc;     // 6个关节指令加速度，单位°/s²
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] targetJointCurrent; // 6个关节指令电流，单位A
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] actualJointCurrent; // 6个关节当前电流，单位A
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] actualTCPForce;     // 机器人末端力矩Nm；x,y,z,rx,ry,rz
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] targetTCPPos;       // 机器人TCP指令位置mm；x,y,z,rx,ry,rz
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public byte[] collisionLevel;       // 机器人碰撞等级

        public double speedScaleManual;     // 手动模式全局速度百分比
        public double speedScaleAuto;       // 自动模式全局速度百分比
        public int luaLineNum;              // 当前lua程序运行行号
        public byte abnomalStop;            // 0-无异常；1-有异常

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 256)]
        public byte[] currentLuaFileName;   // 当前运行lua程序名称
        public byte programTotalLine;       // lua程序总行数
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public byte[] safetyBoxSingal;      // 机器人按钮盒按钮状态

        public double weldVoltage;          // 焊接电压 V
        public double weldCurrent;          // 焊接电流
        public double weldTrackVel;         // 焊缝跟踪速度 mm/s

        public byte tpdException;           // TPD轨迹加载数量超限，0-未超限，1-超限
        public byte alarmRebootRobot;       // 警告，1-松开急停按钮请断电重启控制箱，2-关节通讯异常请断电重启控制箱
        public byte modbusMasterConnect;    // bit0-bit7位对应ModbusTCP的0-7主站连接状态  0-未连接   1-连接
        public byte modbusSlaveConnect;     // ModbusTCP从站连接状态 0-未连接；1-已连接
        public byte btnBoxStopSignal;       // 按钮盒急停信号，0-松开急停；1-按下急停
        public byte dragAlarm;              // 拖动警告，当前处于自动模式,0-不报警，1-报警 ，2-位置反馈异常不切换
        public byte safetyDoorAlarm;        // 安全门警告；0-安全门关闭；1-安全门打开
        public byte safetyPlaneAlarm;       // 进入安全墙警告；0-未进入安全墙；1-已进入安全墙
        public byte motonAlarm;             // 运动警告
        public byte interfaceAlarm;         // 进入干涉区警告
        public int udpCmdState;             // 20007端口UDP通讯连接状态
        public byte weldReadyState;         // 焊机准备完成状态
        public byte alarmCheckEmergStopBtn; // 0-正常；1-通信异常，检查急停按钮是否松开
        public byte tsTmCmdComError;        // 0-正常；1-扭矩指令通讯失败
        public byte tsTmStateComError;      // 0-正常；1-扭矩状态通讯失败
        public int ctrlBoxError;            // 控制箱错误
        public byte safetyDataState;        // 安全数据状态标志，0-正常，1-异常
        public byte forceSensorErrState;    // 力传感器连接超时故障；bit0-bit1对应力传感器ID1-ID2

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public byte[] ctrlOpenLuaErrCode;   // 4个控制器外设协议错误码(500错误码)

        public byte strangePosFlag;         // 当前处于奇异位姿标志；0-正常；1-奇异位姿
        public byte alarm;                  // 警告
        public byte driverAlarm;            // 驱动器报警轴号
        public byte aliveSlaveNumError;     // 活动从站数量错误，0：正常；1：数量错误

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
        public byte[] slaveComError;        // 从站错误，0：正常；1：从站掉线；2：从站状态与设置值不一致；3：从站未配置；4：从站配置错误；5：从站初始化错误；6：从站邮箱通信初始化错误

        public byte cmdPointError;          // 指令点错误
        public byte IOError;                // IO错误
        public byte gripperError;           // 夹爪错误
        public byte fileError;              // 文件错误
        public byte paraError;              // 参数错误
        public byte exaxisOutLimitError;    // 外部轴超出软限位错误

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public byte[] driverComError;       // 与驱动器通信故障
        public byte driverError;            // 驱动器通信故障轴号
        public byte outSoftLimitError;      // 超出软限位故障

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 130)]
        public byte[] axleGenComData;       // 机器人末端透传反馈数据

        public byte socketConnTimeout;     // socket连接超时标志
        public byte socketReadTimeout;     // socket读取超时标志
        public byte tsWebStateComErr;      // ts_web_state_com_err

        public UInt16 check_sum;         /* 和校验 */                 

        // 构造函数：初始化所有数组字段
        public ROBOT_STATE_PKG()
        {
            jt_cur_pos = new double[6];
            tl_cur_pos = new double[6];
            flange_cur_pos = new double[6];
            actual_qd = new double[6];
            actual_qdd = new double[6];
            target_TCP_CmpSpeed = new double[2];
            target_TCP_Speed = new double[6];
            actual_TCP_CmpSpeed = new double[2];
            actual_TCP_Speed = new double[6];
            jt_cur_tor = new double[6];
            cl_analog_input = new ushort[2];
            ft_sensor_raw_data = new double[6];
            ft_sensor_data = new double[6];
            extAxisStatus = new EXT_AXIS_STATUS[4];
            extDIState = new ushort[8];
            extDOState = new ushort[8];
            extAIState = new ushort[4];
            extAOState = new ushort[4];
            jointDriverTorque = new double[6];
            jointDriverTemperature = new double[6];
            cl_analog_output = new ushort[2];
            jt_tgt_tor = new double[6];
            toolCoord = new double[6];
            wobjCoord = new double[6];
            extoolCoord = new double[6];
            exAxisCoord = new double[6];
            loadCog = new double[3];
            lastServoTarget = new double[6];
            targetJointPos = new double[6];
            targetJointVel = new double[6];
            targetJointAcc = new double[6];
            targetJointCurrent = new double[6];
            actualJointCurrent = new double[6];
            actualTCPForce = new double[6];
            targetTCPPos = new double[6];
            collisionLevel = new byte[6];
            currentLuaFileName = new byte[256];
            safetyBoxSingal = new byte[6];
            ctrlOpenLuaErrCode = new byte[4];
            slaveComError = new byte[8];
            driverComError = new byte[6];
            axleGenComData = new byte[130];
        }
    }

机器人可配置状态枚举
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief  机器人可配置状态枚举 范围 3~131
    */
    public enum RobotState
    {
        ProgramState = 3,
        RobotState = 4,
        MainCode = 5,
        SubCode = 6,
        RobotMode = 7,
        JointCurPos = 8,
        ToolCurPos = 9,
        FlangeCurPos = 10,
        ActualJointVel = 11,
        ActualJointAcc = 12,
        TargetTCPCmpSpeed = 13,
        TargetTCPSpeed = 14,
        ActualTCPCmpSpeed = 15,
        ActualTCPSpeed = 16,
        ActualJointTorque = 17,
        Tool = 18,
        User = 19,
        ClDgtOutputH = 20,
        ClDgtOutputL = 21,
        TlDgtOutputL = 22,
        ClDgtInputH = 23,
        ClDgtInputL = 24,
        TlDgtInputL = 25,
        ClAnalogInput = 26,
        TlAnglogInput = 27,
        FtSensorRawData = 28,
        FtSensorData = 29,
        FtSensorActive = 30,
        EmergencyStop = 31,
        MotionDone = 32,
        GripperMotiondone = 33,
        McQueueLen = 34,
        CollisionState = 35,
        TrajectoryPnum = 36,
        SafetyStop0State = 37,
        SafetyStop1State = 38,
        GripperFaultId = 39,
        GripperFault = 40,
        GripperActive = 41,
        GripperPosition = 42,
        GripperSpeed = 43,
        GripperCurrent = 44,
        GripperTemp = 45,
        GripperVoltage = 46,
        AuxState = 47,
        ExtAxisStatus = 48,
        ExtDIState = 49,
        ExtDOState = 50,
        ExtAIState = 51,
        ExtAOState = 52,
        RbtEnableState = 53,
        JointDriverTorque = 54,
        JointDriverTemperature = 55,
        RobotTime = 56,
        SoftwareUpgradeState = 57,
        EndLuaErrCode = 58,
        ClAnalogOutput = 59,
        TlAnalogOutput = 60,
        GripperRotNum = 61,
        GripperRotSpeed = 62,
        GripperRotTorque = 63,
        WeldingBreakOffState = 64,
        TargetJointTorque = 65,
        SmartToolState = 66,
        WideVoltageCtrlBoxTemp = 67,
        WideVoltageCtrlBoxFanCurrent = 68,
        ToolCoord = 69,
        WobjCoord = 70,
        ExtoolCoord = 71,
        ExAxisCoord = 72,
        Load = 73,
        LoadCog = 74,
        LastServoTarget = 75,
        ServoJCmdNum = 76,
        TargetJointPos = 77,
        TargetJointVel = 78,
        TargetJointAcc = 79,
        TargetJointCurrent = 80,
        ActualJointCurrent = 81,
        ActualTCPForce = 82,
        TargetTCPPos = 83,
        CollisionLevel = 84,
        SpeedScaleManual = 85,
        SpeedScaleAuto = 86,
        LuaLineNum = 87,
        AbnomalStop = 88,
        CurrentLuaFileName = 89,
        ProgramTotalLine = 90,
        SafetyBoxSingal = 91,
        WeldVoltage = 92,
        WeldCurrent = 93,
        WeldTrackVel = 94,
        TpdException = 95,
        AlarmRebootRobot = 96,
        ModbusMasterConnect = 97,
        ModbusSlaveConnect = 98,
        BtnBoxStopSignal = 99,
        DragAlarm = 100,
        SafetyDoorAlarm = 101,
        SafetyPlaneAlarm = 102,
        MotonAlarm = 103,
        InterfaceAlarm = 104,
        UdpCmdState = 105,
        WeldReadyState = 106,
        AlarmCheckEmergStopBtn = 107,
        TsTmCmdComError = 108,
        TsTmStateComError = 109,
        CtrlBoxError = 110,
        SafetyDataState = 111,
        ForceSensorErrState = 112,
        CtrlOpenLuaErrCode = 113,
        StrangePosFlag = 114,
        Alarm = 115,
        DriverAlarm = 116,
        AliveSlaveNumError = 117,
        SlaveComError = 118,
        CmdPointError = 119,
        IOError = 120,
        GripperError = 121,
        FileError = 122,
        ParaError = 123,
        ExaxisOutLimitError = 124,
        DriverComError = 125,
        DriverError = 126,
        OutSoftLimitError = 127,
        AxleGenComData = 128,
        SocketConnTimeout = 129,     //socket连接超时，bit0-bit4:socketID 1-4
        SocketReadTimeout = 130,     //socket读取超时，bit0-bit4:socketID 1-4
        TsWebStateComErr = 131     //web-扭矩通讯失败；0-正常；1-失败
    }