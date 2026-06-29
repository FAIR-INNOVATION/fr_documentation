数据结构说明
================

.. toctree:: 
    :maxdepth: 5

关节位置数据类型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 关节位置数据类型 
    */  
    public class JointPos
    {
      double J1;
      double J2;
      double J3;
      double J4;
      double J5;
      double J6;

      public JointPos(double j1, double j2, double j3, double j4, double j5, double j6)
      {
        J1 = j1;
        J2 = j2;
        J3 = j3;
        J4 = j4;
        J5 = j5;
        J6 = j6;
      }

      public JointPos()
      {

      }
    }

笛卡尔空间位置数据类型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 笛卡尔空间位置数据类型
    */
    public class DescTran
    {
      public double x = 0.0;    /* x轴坐标，单位mm  */
      public double y = 0.0;    /* y轴坐标，单位mm  */
      public double z = 0.0;    /* z轴坐标，单位mm  */
      public DescTran(double posX, double posY, double posZ)
      {
        x = posX;
        y = posY;
        z = posZ;
      }

      public DescTran()
      {

      }

    }

欧拉角姿态数据类型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 欧拉角姿态数据类型
    */
    public class Rpy
    {
      public double rx = 0.0;   /* 绕固定轴X旋转角度，单位：deg  */
      public double ry = 0.0;   /* 绕固定轴Y旋转角度，单位：deg  */
      public double rz = 0.0;   /* 绕固定轴Z旋转角度，单位：deg  */
      public Rpy(double rotateX, double rotateY, double rotateZ)
      {
        rx = rotateX;
        ry = rotateY;
        rz = rotateZ;
      }
    }

笛卡尔空间位姿数据类型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    *@brief 笛卡尔空间位姿类型
    */
    public class DescPose
    {
      public DescTran tran = new DescTran(0.0, 0.0, 0.0);      /* 笛卡尔空间位置  */
      public Rpy rpy = new Rpy(0.0, 0.0, 0.0);			       /* 笛卡尔空间姿态  */

      public DescPose()
      {

      }

      public DescPose(DescTran descTran, Rpy rotateRpy)
      {
        tran = descTran;
        rpy = rotateRpy;
      }

      public DescPose(double tranX, double tranY, double tranZ, double rX, double ry, double rz)
      {
        tran.x = tranX;
        tran.y = tranY;
        tran.z = tranZ;
        rpy.rx = rX;
        rpy.ry = ry;
        rpy.rz = rz;
      }

      public String toString()
      {
        return String.valueOf(tran.x) + "," +  String.valueOf(tran.y) + "," +String.valueOf(tran.z) + "," +String.valueOf(rpy.rx) + "," +String.valueOf(rpy.ry) + "," +String.valueOf(rpy.rz);
      }
    }

扩展轴位置数据类型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 扩展轴位置数据类型
    */
    public class ExaxisPos
    {
      public double axis1 = 0.0;
      public double axis2 = 0.0;
      public double axis3 = 0.0;
      public double axis4 = 0.0;

      public ExaxisPos()
      {

      }
      public ExaxisPos(double[] exaxisPos)
      {
        axis1 = exaxisPos[0];
        axis2 = exaxisPos[1];
        axis3 = exaxisPos[2];
        axis4 = exaxisPos[3];
      }

      public ExaxisPos(double pos1, double pos2, double pos3, double pos4)
      {
        axis1 = pos1;
        axis2 = pos2;
        axis3 = pos3;
        axis4 = pos4;
      }
    }

力矩传感器数据类型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 力传感器的受力分量和力矩分量
    */
    public class ForceTorque
    {
      public double fx;  /* 沿x轴受力分量，单位N  */
      public double fy;  /* 沿y轴受力分量，单位N  */
      public double fz;  /* 沿z轴受力分量，单位N  */
      public double tx;  /* 绕x轴力矩分量，单位Nm */
      public double ty;  /* 绕y轴力矩分量，单位Nm */
      public double tz;  /* 绕z轴力矩分量，单位Nm */
      public ForceTorque(double fX, double fY, double fZ, double tX, double tY, double tZ)
      {
        fx = fX;
        fy = fY;
        fz = fZ;
        tx = tX;
        ty = tY;
        tz = tZ;
      }
    }

螺旋参数数据类型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  螺旋参数数据类型
    */
    public class SpiralParam
    {
        public int circle_num;           /* 螺旋圈数  */
        public double circle_angle;         /* 螺旋倾角  */
        public double rad_init;             /* 螺旋初始半径，单位mm  */
        public double rad_add;              /* 半径增量  */
        public double rotaxis_add;          /* 转轴方向增量  */
        public int rot_direction;  /* 旋转方向，0-顺时针，1-逆时针  */
        public int velAccMode;     /* 速度加速度参数模式：0-角速度恒定；1-线速度恒定 */
        public SpiralParam(int circleNum, double circleAngle, double radInit, double radAdd, double rotaxisAdd, int rotDirection,int vel_AccMode)
        {
            circle_num = circleNum;
            circle_angle = circleAngle;
            rad_init = radInit;
            rad_add = radAdd;
            rotaxis_add = rotaxisAdd;
            rot_direction = rotDirection;
            velAccMode=vel_AccMode;
        }
    }

扩展轴状态类型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  扩展轴状态类型
    */
    public class EXT_AXIS_STATUS
    {
     public double pos = 0;        //扩展轴位置
     public double vel = 0;        //扩展轴速度
     public int errorCode = 0;     //扩展轴故障码
     public int ready = 0;        //伺服准备好
     public int inPos = 0;        //伺服到位
     public int alarm = 0;        //伺服报警
     public int flerr = 0;        //跟随误差
     public int nlimit = 0;       //到负限位
     public int pLimit = 0;       //到正限位
     public int mdbsOffLine = 0;  //驱动器485总线掉线
     public int mdbsTimeout = 0;  //控制卡与控制箱485通信超时
     public int homingStatus = 0; //扩展轴回零状态
    }

传感器类型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  传感器类型
    */
    public class DeviceConfig
    {
      int company = 0;          // 厂商
      int device = 0;           // 类型/设备号
      int softwareVersion = 0;  // 软件版本
      int bus = 0;              // 挂载位置

      public DeviceConfig()
      {

      }

      public DeviceConfig(int company, int device, int softwareVersion, int bus)
      {
        this.company = company;
        this.device = device;
        this.softwareVersion = softwareVersion;
        this.bus = bus;
      }
    }

485扩展轴配置
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  485扩展轴配置
    */
    public class Axis485Param
    {
      int servoCompany;           // 伺服驱动器厂商，1-戴纳泰克
      int servoModel;             // 伺服驱动器型号，1-FD100-750C
      int servoSoftVersion;       // 伺服驱动器软件版本，1-V1.0
      int servoResolution;        // 编码器分辨率
      double axisMechTransRatio;  // 机械传动比

      public Axis485Param(int company, int model, int softVersion, int resolution, double mechTransRatio)
      {
        servoCompany = company;
        servoModel = model;
        servoSoftVersion = softVersion;
        servoResolution = resolution;
        axisMechTransRatio = mechTransRatio;
      }

      public Axis485Param()
      {

      }
    }

伺服控制器状态
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  伺服控制器状态
    */
    public class ROBOT_AUX_STATE
    {
      public int servoId = 0;           //伺服驱动器ID号
      public int servoErrCode = 0;       //伺服驱动器故障码
      public int servoState = 0;         //伺服驱动器状态
      public double servoPos = 0;        //伺服当前位置
      public float servoVel = 0;         //伺服当前速度
      public float servoTorque = 0;      //伺服当前转矩    25
    }

焊接中断状态
++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  焊接中断状态
    */
    public class WELDING_BREAKOFF_STATE
    {
      public int breakOffState = 0;  //焊接中断状态
      public int weldArcState = 0;   //焊接电弧中断状态
    }

UDP扩展轴通讯参数
++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  焊接中断状态
    */
    public class WELDING_BREAKOFF_STATE
    {
      public String ip = "192.168.58.88";//IP地址
      public int port = 2021;            //端口号
      public int period = 2;             //通讯周期(ms，默认为2，请勿修改此参数)
      public int lossPkgTime = 50;       //丢包检测时间(ms)
      public int lossPkgNum = 2;         //丢包次数
      public int disconnectTime = 100;   //通讯断开确认时长
      public int reconnectEnable = 0;    //通讯断开自动重连使能 0-不使能 1-使能
      public int reconnectPeriod = 100;  //重连周期间隔(ms)
      public int reconnectNum = 3;       //重连次数
      public int selfConnect =0;         //断电重启是否自动建立连接；0-不建立连接；1-建立连接
    }

机器人状态反馈结构体类型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  机器人状态反馈结构体类型
    * /
    public class ROBOT_STATE_PKG {
        public int frame_head;                      // 帧头
        public int frame_cnt;                       // 帧计数
        public int data_len;                        // 数据长度
        public int program_state;                   // 程序状态 - 1-停止；2-运行；3-暂停
        public int robot_state;                     // 机器人运动状态 - 1-停止；2-运行；3-暂停；4-拖动
        public int main_code;                       // 主故障码
        public int sub_code;                        // 子故障码
        public int robot_mode;                      // 机器人模式 - 1-手动模式；0-自动模式
        public double[] jt_cur_pos = new double[6]; // 6个轴当前关节位置，单位deg
        public double[] tl_cur_pos = new double[6]; // 工具当前位置 - [x,y,z,rx,ry,rz]
        public double[] flange_cur_pos = new double[6]; // 末端法兰当前位置 - [x,y,z,rx,ry,rz]
        public double[] actual_qd = new double[6];  // 当前6个关节速度，单位deg/s
        public double[] actual_qdd = new double[6]; // 当前6个关节加速度，单位deg/s^2
        public double[] target_TCP_CmpSpeed = new double[2]; // TCP合成指令速度 - [位置mm/s, 姿态deg/s]
        public double[] target_TCP_Speed = new double[6]; // TCP指令速度 - [vx,vy,vz,wx,wy,wz]
        public double[] actual_TCP_CmpSpeed = new double[2]; // TCP合成实际速度 - [位置mm/s, 姿态deg/s]
        public double[] actual_TCP_Speed = new double[6]; // TCP实际速度 - [vx,vy,vz,wx,wy,wz]
        public double[] jt_cur_tor = new double[6]; // 当前关节力矩
        public int tool;                            // 工具ID
        public int user;                            // 工件ID
        public int cl_dgt_output_h;                 // 控制柜数字输出高字节
        public int cl_dgt_output_l;                 // 控制柜数字输出低字节
        public int tl_dgt_output_l;                 // 工具数字输出低字节
        public int cl_dgt_input_h;                  // 控制柜数字输入高字节
        public int cl_dgt_input_l;                  // 控制柜数字输入低字节
        public int tl_dgt_input_l;                  // 工具数字输入低字节
        public int[] cl_analog_input = new int[2];  // 控制柜模拟输入
        public int tl_anglog_input;                 // 工具模拟输入
        public double[] ft_sensor_raw_data = new double[6]; // 力传感器原始数据
        public double[] ft_sensor_data = new double[6]; // 力传感器数据
        public int ft_sensor_active;                // 力传感器激活状态
        public int EmergencyStop;                   // 急停状态
        public int motion_done;                     // 运动完成
        public int gripper_motiondone;              // 夹爪运动完成信号，0-未完成，1-完成(未检测到物体)，2-运动完成（检测到物体）
        public int mc_queue_len;                    // 运动队列长度
        public int collisionState;                  // 碰撞状态
        public int trajectory_pnum;                 // 轨迹点序号
        public int safety_stop0_state;              // 安全停止0状态
        public int safety_stop1_state;              // 安全停止1状态
        public int gripper_fault_id;                // 夹爪故障ID
        public int gripper_fault;                   // 夹爪故障0-无故障 1-485超时 2-指令错误 3-工件掉落 其他-夹爪故障码
        public int gripper_active;                  // 夹爪激活
        public int gripper_position;                // 夹爪位置
        public int gripper_speed;                   // 夹爪速度
        public int gripper_current;                 // 夹爪电流
        public int gripper_temp;                    // 夹爪温度
        public int gripper_voltage;                 // 夹爪电压
        public AuxState aux_state = new AuxState(); // 内部辅助轴状态
        public EXT_AXIS_STATUS[] extAxisStatus = new EXT_AXIS_STATUS[4]; // 扩展轴状态数组
        public short[] extDIState = new short[8];   // 扩展IO
        public short[] extDOState = new short[8];   // 扩展IO
        public short[] extAIState = new short[4];   // 扩展IO
        public short[] extAOState = new short[4];   // 扩展IO
        public int rbtEnableState;                  // 机器人使能状态
        public double[] jointDriverTorque = new double[6]; // 关节驱动器力矩
        public double[] jointDriverTemperature = new double[6]; // 关节驱动器温度
        public ROBOT_TIME robotTime = new ROBOT_TIME(); // 机器人时间对象
        public int softwareUpgradeState;            // 软件升级状态
        public int endLuaErrCode;                   // 末端Lua错误码
        public int[] cl_analog_output = new int[2]; // 控制柜模拟输出
        public int tl_analog_output;                // 工具模拟输出
        public float gripperRotNum;                 // 旋转夹爪圈数
        public int gripperRotSpeed;                 // 旋转夹爪速度
        public int gripperRotTorque;                // 旋转夹爪力矩
        public WELDING_BREAKOFF_STATE weldingBreakOffState = new WELDING_BREAKOFF_STATE(); // 焊接中断状态
        public double[] jt_tgt_tor = new double[6]; // 目标关节力矩
        public int smartToolState;                  // 智能工具状态
        public float wideVoltageCtrlBoxTemp;        // 宽电压控制箱温度
        public int wideVoltageCtrlBoxFanCurrent;    // 宽电压控制箱风扇电流
        public double[] toolCoord = new double[6];  // 工具坐标系
        public double[] wobjCoord = new double[6];  // 工件坐标系
        public double[] extoolCoord = new double[6]; // 外部工具坐标系
        public double[] exAxisCoord = new double[6]; // 扩展轴坐标系
        public double load;                         // 负载
        public double[] loadCog = new double[3];    // 负载重心
        public double[] lastServoTarget = new double[6]; // 上一次伺服J目标位置
        public int servoJCmdNum;                    // 伺服J命令数量
        public double[] targetJointPos = new double[6]; // 目标关节位置
        public double[] targetJointVel = new double[6]; // 目标关节速度
        public double[] targetJointAcc = new double[6]; // 目标关节加速度
        public double[] targetJointCurrent = new double[6]; // 目标关节电流
        public double[] actualJointCurrent = new double[6]; // 实际关节电流
        public double[] actualTCPForce = new double[6]; // 实际TCP力
        public double[] targetTCPPos = new double[6]; // 目标TCP位置
        public int[] collisionLevel = new int[6];   // 碰撞等级
        public double speedScaleManual;              // 手动速度比例
        public double speedScaleAuto;                // 自动速度比例
        public int luaLineNum;                       // Lua行号
        public int abnomalStop;                      // 异常停止
        public String currentLuaFileName;            // 当前Lua文件名
        public int programTotalLine;                 // 程序总行数
        public int[] safetyBoxSingal = new int[6];   // 安全箱信号
        public double weldVoltage;                   // 焊接电压
        public double weldCurrent;                   // 焊接电流
        public double weldTrackVel;                  // 焊接跟踪速度
        public int tpdException;                     // TPD异常
        public int alarmRebootRobot;                 // 报警重启机器人
        public int modbusMasterConnect;              // Modbus主站连接
        public int modbusSlaveConnect;               // Modbus从站连接
        public int btnBoxStopSignal;                 // 按钮盒停止信号
        public int dragAlarm;                        // 拖动报警
        public int safetyDoorAlarm;                  // 安全门报警
        public int safetyPlaneAlarm;                 // 安全平面报警
        public int motonAlarm;                       // 运动报警
        public int interfaceAlarm;                   // 干涉报警
        public int udpCmdState;                      // UDP命令状态
        public int weldReadyState;                   // 焊接准备状态
        public int alarmCheckEmergStopBtn;           // 报警检查急停按钮
        public int tsTmCmdComError;                  // 命令通信错误
        public int tsTmStateComError;                // 状态通信错误
        public int ctrlBoxError;                     // 控制箱错误
        public int safetyDataState;                  // 安全数据状态
        public int forceSensorErrState;              // 力传感器错误状态
        public int[] ctrlOpenLuaErrCode = new int[4]; // 控制打开Lua错误码
        public int strangePosFlag;                   // 奇异位置标志
        public int alarm;                            // 报警
        public int driverAlarm;                      // 驱动器报警
        public int aliveSlaveNumError;               // 存活从站数量错误
        public int[] slaveComError = new int[8];     // 从站通信错误
        public int cmdPointError;                    // 命令点错误
        public int IOError;                          // IO错误
        public int gripperError;                     // 夹爪错误
        public int fileError;                        // 文件错误
        public int paraError;                        // 参数错误
        public int exaxisOutLimitError;              // 扩展轴超出软限位错误
        public int[] driverComError = new int[6];    // 驱动器通信错误
        public int driverError;                      // 驱动器错误
        public int outSoftLimitError;                // 超出软限位错误
        public byte[] axleGenComData = new byte[130]; // 通用轴通信数据
        public int check_sum;                        // 校验和
        public int socketConnTimeout;                // Socket连接超时
        public int socketReadTimeout;                // Socket读取超时
        public int tsWebStateComErr;                 // TS Web状态通信错误
        public int exaxisCoordID;                  //扩展轴坐标系编号
    }

机器人状态反馈配置结果类
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * 机器人状态反馈配置结果类，包含状态列表和周期
    */
    public static class StateConfigResult {
      public final List<RobotState> stateList;
      public final int period;
    }

机器人状态反馈配置枚举类型
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:
    
    /**
    * 机器人状态枚举类型
    * 用于实时状态反馈配置
    */
    enum class RobotState
    {
        ProgramState,           // 程序运行状态，1-停止；2-运行；3-暂停
        RobotState,             // 机器人运动状态，1-停止；2-运行；3-暂停；4-拖动
        MainCode,               // 主故障码
        SubCode,                // 子故障码
        RobotMode,              // 机器人模式，1-手动模式；0-自动模式
        JointCurPos,            // 6个轴当前关节位置，单位deg
        ToolCurPos,             // 工具当前位置：[0]沿x轴位置(mm)，[1]沿y轴(mm)，[2]沿z轴(mm)，[3]绕固定轴X旋转(deg)，[4]绕固定轴Y(deg)，[5]绕固定轴Z(deg)
        FlangeCurPos,          // 末端法兰当前位置：[0]沿x轴(mm)，[1]沿y轴(mm)，[2]沿z轴(mm)，[3]绕固定轴X(deg)，[4]绕固定轴Y(deg)，[5]绕固定轴Z(deg)
        ActualJointVel,        // 当前6个关节速度，单位deg/s
        ActualJointAcc,        // 当前6个关节加速度，单位deg/s^2
        TargetTCPCmpSpeed,     // TCP合成指令速度：[0]位置(mm/s)，[1]姿态(deg/s)
        TargetTCPSpeed,        // TCP指令速度：[0]沿x轴(mm/s)，[1]沿y轴(mm/s)，[2]沿z轴(mm/s)，[3]绕X角速度(deg/s)，[4]绕Y(deg/s)，[5]绕Z(deg/s)
        ActualTCPCmpSpeed,     // TCP合成实际速度：[0]位置(mm/s)，[1]姿态(deg/s)
        ActualTCPSpeed,        // TCP实际速度：[0]沿x轴(mm/s)，[1]沿y轴(mm/s)，[2]沿z轴(mm/s)，[3]绕X角速度(deg/s)，[4]绕Y(deg/s)，[5]绕Z(deg/s)
        ActualJointTorque,     // 6个轴当前扭矩，单位N·m
        Tool,                  // 应用的工具坐标系编号
        User,                  // 应用的工件坐标系编号
        ClDgtOutputH,          // 控制箱数字量IO输出15-8
        ClDgtOutputL,          // 控制箱数字量IO输出7-0
        TlDgtOutputL,          // 工具数字量IO输出7-0，仅bit0-bit1有效
        ClDgtInputH,           // 控制箱数字量IO输入15-8
        ClDgtInputL,           // 控制箱数字量IO输入7-0
        TlDgtInputL,           // 工具数字量IO输入7-0，仅bit0-bit1有效
        ClAnalogInput,         // 控制箱模拟量输入：[0]通道0，[1]通道1
        TlAnalogInput,         // 工具模拟量输入
        FtSensorRawData,       // 力矩传感器原始数据：[0]沿x轴力(N)，[1]沿y轴力(N)，[2]沿z轴力(N)，[3]沿x轴力矩(Nm)，[4]沿y轴(Nm)，[5]沿z轴(Nm)
        FtSensorData,          // 力矩传感器数据（经处理）：[0]沿x轴力(N)，[1]沿y轴力(N)，[2]沿z轴力(N)，[3]沿x轴力矩(Nm)，[4]沿y轴(Nm)，[5]沿z轴(Nm)
        FtSensorActive,        // 力矩传感器激活状态，0-复位，1-激活
        EmergencyStop,         // 急停标志，0-急停未按下，1-急停按下
        MotionDone,            // 运动到位信号，1-到位，0-未到位
        GripperMotiondone,     // 夹爪运动完成信号，0-未完成，1-完成(未检测到物体)，2-运动完成（检测到物体）
        McQueueLen,            // 运动指令队列长度
        CollisionState,        // 碰撞检测，1-碰撞，0-无碰撞
        TrajectoryPnum,        // 轨迹点编号
        SafetyStop0State,      // 安全停止信号SI0
        SafetyStop1State,      // 安全停止信号SI1
        GripperFaultId,        // 错误夹爪号
        GripperFault,          // 夹爪故障0-无故障 1-485超时 2-指令错误 3-工件掉落 其他-夹爪故障码
        GripperActive,         // 夹爪激活状态
        GripperPosition,       // 夹爪位置
        GripperSpeed,          // 夹爪速度
        GripperCurrent,        // 夹爪电流
        GripperTemp,           // 夹爪温度
        GripperVoltage,        // 夹爪电压
        AuxState,              // 485扩展轴状态
        ExtAxisStatus,         // UDP扩展轴状态（4个轴）
        ExtDIState,            // 扩展DI输入（8个）
        ExtDOState,            // 扩展DO输出（8个）
        ExtAIState,            // 扩展AI输入（4个）
        ExtAOState,            // 扩展AO输出（4个）
        RbtEnableState,        // 机器人使能状态
        JointDriverTorque,     // 机器人关节驱动器扭矩（6个关节）
        JointDriverTemperature,// 机器人关节驱动器温度（6个关节）
        RobotTime,             // 机器人系统时间
        SoftwareUpgradeState,  // 机器人软件升级状态
        EndLuaErrCode,         // 末端LUA运行状态
        ClAnalogOutput,        // 控制箱模拟量输出（2个）
        TlAnalogOutput,        // 工具模拟量输出
        GripperRotNum,         // 旋转夹爪当前旋转圈数
        GripperRotSpeed,       // 旋转夹爪当前旋转速度百分比
        GripperRotTorque,      // 旋转夹爪当前旋转力矩百分比
        WeldingBreakOffState,  // 焊接中断状态
        TargetJointTorque,     // 关节指令力矩（6个关节）
        SmartToolState,        // SmartTool手柄按钮状态
        WideVoltageCtrlBoxTemp,// 宽电压控制箱温度
        WideVoltageCtrlBoxFanCurrent, // 宽电压控制箱风扇电流(mA)
        ToolCoord,             // 当前工具坐标系数值：x,y,z,rx,ry,rz
        WobjCoord,             // 当前工件坐标系数值：x,y,z,rx,ry,rz
        ExtoolCoord,           // 当前外部工具坐标系数值：x,y,z,rx,ry,rz
        ExAxisCoord,           // 当前扩展轴坐标系数值：x,y,z,rx,ry,rz
        Load,                  // 负载质量
        LoadCog,               // 负载质心：x,y,z
        LastServoTarget,       // 队列中最后一个ServoJ目标位置（6个关节）
        ServoJCmdNum,          // servoJ指令计数
        TargetJointPos,        // 6个关节指令位置，单位°
        TargetJointVel,        // 6个关节指令速度，单位°/s
        TargetJointAcc,        // 6个关节指令加速度，单位°/s²
        TargetJointCurrent,    // 6个关节指令电流，单位A
        ActualJointCurrent,    // 6个关节当前电流，单位A
        ActualTCPForce,        // 机器人末端力矩：x,y,z,rx,ry,rz，单位Nm
        TargetTCPPos,          // 机器人TCP指令位置：x,y,z,rx,ry,rz，单位mm
        CollisionLevel,        // 机器人碰撞等级（6个）
        SpeedScaleManual,      // 手动模式全局速度百分比
        SpeedScaleAuto,        // 自动模式全局速度百分比
        LuaLineNum,            // 当前lua程序运行行号
        AbnomalStop,           // 0-无异常；1-有异常
        CurrentLuaFileName,    // 当前运行lua程序名称
        ProgramTotalLine,      // lua程序总行数
        SafetyBoxSingal,       // 机器人按钮盒按钮状态（6个）
        WeldVoltage,           // 焊接电压 V
        WeldCurrent,           // 焊接电流
        WeldTrackVel,          // 焊缝跟踪速度 mm/s
        TpdException,          // TPD轨迹加载数量超限，0-未超限，1-超限
        AlarmRebootRobot,      // 警告：1-松开急停后需断电重启，2-关节通讯异常需断电重启
        ModbusMasterConnect,   // bit0-7对应ModbusTCP主站0-7连接状态，0-未连接，1-连接
        ModbusSlaveConnect,    // ModbusTCP从站连接状态，0-未连接，1-已连接
        BtnBoxStopSignal,      // 按钮盒急停信号，0-松开急停，1-按下急停
        DragAlarm,            // 拖动警告：0-不报警，1-报警，2-位置反馈异常不切换
        SafetyDoorAlarm,      // 安全门警告：0-关闭，1-打开
        SafetyPlaneAlarm,     // 安全墙警告：0-未进入，1-已进入
        MotonAlarm,           // 运动警告
        InterfaceAlarm,       // 进入干涉区警告
        UdpCmdState,          // 20007端口UDP通讯连接状态
        WeldReadyState,       // 焊机准备完成状态
        AlarmCheckEmergStopBtn, // 0-正常；1-通信异常，检查急停按钮
        TsTmCmdComError,      // 0-正常；1-扭矩指令通讯失败
        TsTmStateComError,    // 0-正常；1-扭矩状态通讯失败
        CtrlBoxError,         // 控制箱错误
        SafetyDataState,      // 安全数据状态，0-正常，1-异常
        ForceSensorErrState,  // 力传感器连接超时，bit0-bit1对应ID1-ID2
        CtrlOpenLuaErrCode,   // 4个控制器外设协议错误码(500错误码)
        StrangePosFlag,       // 奇异位姿标志：0-正常，1-奇异位姿
        Alarm,                // 警告
        DriverAlarm,          // 驱动器报警轴号
        AliveSlaveNumError,   // 活动从站数量错误：0-正常，1-数量错误
        SlaveComError,        // 从站错误：0-正常，1-掉线，2-状态不一致，3-未配置，4-配置错误，5-初始化错误，6-邮箱通信初始化错误
        CmdPointError,        // 指令点错误
        IOError,              // IO错误
        GripperError,         // 夹爪错误
        FileError,            // 文件错误
        ParaError,            // 参数错误
        ExaxisOutLimitError,  // 外部轴超出软限位错误
        DriverComError,       // 与驱动器通信故障（6个轴）
        DriverError,          // 驱动器通信故障轴号
        OutSoftLimitError,    // 超出软限位故障
        AxleGenComData,       // 机器人末端透传反馈数据
        SocketConnTimeout,    // socket连接超时，bit0-bit4对应socketID 1-4
        SocketReadTimeout,    // socket读取超时，bit0-bit4对应socketID 1-4
        TsWebStateComErr,     // web-扭矩通讯失败：0-正常，1-失败
        ExaxisCoordID          //扩展轴坐标系编号
    };