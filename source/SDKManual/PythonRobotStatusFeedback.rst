数据结构说明
==========================

.. toctree:: 
    :maxdepth: 5

机器人状态反馈结构体类型
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:

    class ROBOT_AUX_STATE(Structure):
        _pack_ = 1
        _fields_ = [
            ("servoId", c_uint8),         # 伺服驱动器ID号
            ("servoErrCode", c_int),     # 伺服驱动器故障码
            ("servoState", c_int),       # 伺服驱动器状态
            ("servoPos", c_double),      # 伺服当前位置
            ("servoVel", c_float),       # 伺服当前速度
            ("servoTorque", c_float),    # 伺服当前转矩
        ]

    class EXT_AXIS_STATUS(Structure):
        _pack_ = 1
        _fields_ = [
            ("pos", c_double),        # 扩展轴位置
            ("vel", c_double),        # 扩展轴速度
            ("errorCode", c_int),     # 扩展轴故障码
            ("ready", c_uint8),        # 伺服准备好
            ("inPos", c_uint8),        # 伺服到位
            ("alarm", c_uint8),        # 伺服报警
            ("flerr", c_uint8),        # 跟随误差
            ("nlimit", c_uint8),       # 到负限位
            ("pLimit", c_uint8),       # 到正限位
            ("mdbsOffLine", c_uint8),  # 驱动器485总线掉线
            ("mdbsTimeout", c_uint8),  # 控制卡与控制箱485通信超时
            ("homingStatus", c_uint8), # 扩展轴回零状态
        ]

    class WELDING_BREAKOFF_STATE(Structure):
        _pack_ = 1
        _fields_ = [
            ("breakOffState", c_uint8),        # 焊接中断状态
            ("weldArcState", c_uint8),        # 焊接电弧中断状态
        ]

    # ==================== 完整机器人状态结构体 ====================
    class RobotStatePkg(Structure):
        """
        机器人状态反馈数据包
        """
        _pack_ = 1
        _fields_ = [
            # 帧头信息
            ("frame_head", c_uint16),           # 帧头，约定为0x5A5A
            ("frame_cnt", c_uint8),             # 帧计数，循环计数0-255
            ("data_len", c_uint16),             # 数据内容的长度
            ("program_state", c_uint8),         # 程序运行状态，1-停止；2-运行；3-暂停
            ("robot_state", c_uint8),             # 机器人运动状态，1-停止；2-运行；3-暂停；4-拖动
            ("main_code", c_int),               # 主故障码
            ("sub_code", c_int),                # 子故障码
            ("robot_mode", c_uint8),            # 机器人模式，1-手动模式；0-自动模式

            # 关节位置和速度
            ("jt_cur_pos", c_double * 6),       # 6个轴当前关节位置，单位deg
            ("tl_cur_pos", c_double * 6),       # 工具当前位置 [x,y,z,rx,ry,rz]
            ("flange_cur_pos", c_double * 6),   # 末端法兰当前位置 [x,y,z,rx,ry,rz]
            ("actual_qd", c_double * 6),        # 当前6个关节速度，单位deg/s
            ("actual_qdd", c_double * 6),       # 当前6个关节加速度，单位deg/s^2
            ("target_TCP_CmpSpeed", c_double * 2),  # TCP合成指令速度[位置mm/s,姿态deg/s]
            ("target_TCP_Speed", c_double * 6), # TCP指令速度[x,y,z,rx,ry,rz]
            ("actual_TCP_CmpSpeed", c_double * 2),  # TCP合成实际速度[位置mm/s,姿态deg/s]
            ("actual_TCP_Speed", c_double * 6), # TCP实际速度[x,y,z,rx,ry,rz]
            ("jt_cur_tor", c_double * 6),       # 6个轴当前扭矩，单位N·m

            # 工具和用户坐标系
            ("tool", c_int),                    # 应用的工具坐标系编号
            ("user", c_int),                    # 应用的工件坐标系编号

            # 数字IO
            ("cl_dgt_output_h", c_uint8),       # 控制箱数字量IO输出15-8
            ("cl_dgt_output_l", c_uint8),       # 控制箱数字量IO输出7-0
            ("tl_dgt_output_l", c_uint8),       # 工具数字量IO输出7-0，仅bit0-bit1有效
            ("cl_dgt_input_h", c_uint8),        # 控制箱数字量IO输入15-8
            ("cl_dgt_input_l", c_uint8),        # 控制箱数字量IO输入7-0
            ("tl_dgt_input_l", c_uint8),        # 工具数字量IO输入7-0，仅bit0-bit1有效

            # 模拟量IO 
            ("cl_analog_input", c_uint16 * 2),  # 控制箱模拟量输入[0],[1]
            ("tl_anglog_input", c_uint16),      # 工具模拟量输入

            # 力矩传感器
            ("ft_sensor_raw_data", c_double * 6),   # 力矩传感器原始数据
            ("ft_sensor_data", c_double * 6),      # 力矩传感器数据
            ("ft_sensor_active", c_uint8),          # 力矩传感器激活状态

            # 状态信号
            ("EmergencyStop", c_uint8),         # 急停标志，0-急停未按下，1-急停按下
            ("motion_done", c_int),             # 运动到位信号，1-到位，0-未到位
            ("gripper_motiondone", c_uint8),    # 夹爪运动完成信号，0-未完成，1-完成(未检测到物体)，2-运动完成（检测到物体）
            ("mc_queue_len", c_int),            # 运动指令队列长度
            ("collisionState", c_uint8),        # 碰撞检测，1-碰撞，0-无碰撞
            ("trajectory_pnum", c_int),         # 轨迹点编号
            ("safety_stop0_state", c_uint8),    # 安全停止信号SI0
            ("safety_stop1_state", c_uint8),    # 安全停止信号SI1

            # 夹爪信息
            ("gripper_fault_id", c_uint8),      # 错误夹爪号
            ("gripper_fault", c_uint16),        # 夹爪故障0-无故障 1-485超时 2-指令错误 3-工件掉落 其他-夹爪故障码
            ("gripper_active", c_uint16),      # 夹爪激活状态
            ("gripper_position", c_uint8),      # 夹爪位置
            ("gripper_speed", c_int8),          # 夹爪速度
            ("gripper_current", c_int8),        # 夹爪电流
            ("gripper_temp", c_int),            # 夹爪温度
            ("gripper_voltage", c_int),         # 夹爪电压

            # 扩展轴状态
            ("aux_axis_state", ROBOT_AUX_STATE * 25),    # 485扩展轴状态 (25个)
            ("extAxisStatus", EXT_AXIS_STATUS * 4), # UDP扩展轴状态 (4个)

            # 扩展IO状态
            ("extDIState", c_uint16 * 8),       # 扩展DI输入
            ("extDOState", c_uint16 * 8),       # 扩展DO输出
            ("extAIState", c_uint16 * 4),        # 扩展AI输入
            ("extAOState", c_uint16 * 4),        # 扩展AO输出

            # 机器人和关节状态
            ("rbtEnableState", c_int),                  # 机器人使能状态
            ("jointDriverTorque", c_double * 6),        # 机器人关节驱动器扭矩
            ("jointDriverTemperature", c_double * 6),   # 机器人关节驱动器温度

            # 机器人时间
            #("robotTime", c_int * 7),             # 机器人系统时间 [year,month,day,hour,min,sec,ms]
            ("year", ctypes.c_uint16),  # 年
            ("mouth", ctypes.c_uint8),  # 月
            ("day", ctypes.c_uint8),  # 日
            ("hour", ctypes.c_uint8),  # 小时
            ("minute", ctypes.c_uint8),  # 分
            ("second", ctypes.c_uint8),  # 秒
            ("millisecond", ctypes.c_uint16),  # 毫秒

            ("softwareUpgradeState", c_int),      # 机器人软件升级状态
            ("endLuaErrCode", c_uint16),          # 末端LUA运行状态

            # 模拟量输出
            ("cl_analog_output", c_uint16 * 2), # 控制箱模拟量输出[0],[1]
            ("tl_analog_output", c_uint16),       # 工具模拟量输出

            # 旋转夹爪
            ("gripperRotNum", c_float),         # 旋转夹爪当前旋转圈数
            ("gripperRotSpeed", c_uint8),       # 旋转夹爪当前旋转速度百分比
            ("gripperRotTorque", c_uint8),      # 旋转夹爪当前旋转力矩百分比

            # 焊接中断状态 - 使用结构体
            ("weldingBreakOffState", WELDING_BREAKOFF_STATE),  # 焊接中断状态

            # 目标关节扭矩
            ("jt_tgt_tor", c_double * 6),       # 关节指令力矩

            ("smartToolState", c_int),          # SmartTool手柄按钮状态
            ("wideVoltageCtrlBoxTemp", c_float),        # 宽电压控制箱温度
            ("wideVoltageCtrlBoxFanCurrent", c_uint16), # 宽电压控制箱风扇电流(mA)

            # 坐标系数值
            ("toolCoord", c_double * 6),        # 当前工具坐标系数值；x,y,z,rx,ry,rz
            ("wobjCoord", c_double * 6),        # 当前工件坐标系数值；x,y,z,rx,ry,rz
            ("extoolCoord", c_double * 6),      # 当前外部工具坐标系数值；x,y,z,rx,ry,rz
            ("exAxisCoord", c_double * 6),      # 当前扩展轴坐标系数值；x,y,z,rx,ry,rz

            # 负载
            ("load", c_double),                 # 负载质量
            ("loadCog", c_double * 3),            # 负载质心

            # 伺服指令
            ("lastServoTarget", c_double * 6),  # 队列中最后一个ServoJ目标位置
            ("servoJCmdNum", c_int),            # servoJ指令计数

            # 目标关节数据
            ("targetJointPos", c_double * 6),   # 6个关节指令位置，单位°
            ("targetJointVel", c_double * 6),   # 6个关节指令速度，单位°/s
            ("targetJointAcc", c_double * 6),   # 6个关节指令加速度，单位°/s2
            ("targetJointCurrent", c_double * 6), # 6个关节指令电流，单位A
            ("actualJointCurrent", c_double * 6), # 6个关节当前电流，单位A
            ("actualTCPForce", c_double * 6),   # 机器人末端力矩Nm；x,y,z,rx,ry,rz
            ("targetTCPPos", c_double * 6),     # 机器人TCP指令位置mm；x,y,z,rx,ry,rz

            ("collisionLevel", c_uint8 * 6),    # 机器人碰撞等级
            ("speedScaleManual", c_double),     # 手动模式全局速度百分比
            ("speedScaleAuto", c_double),       # 自动模式全局速度百分比
            ("luaLineNum", c_int),              # 当前lua程序运行行号
            ("abnomalStop", c_uint8),           # 0-无异常；1-有异常
            ("currentLuaFileName", c_uint8 * 256),  # 当前运行lua程序名称
            ("programTotalLine", c_uint8),      # lua程序总行数
            ("safetyBoxSingal", c_uint8 * 6),   # 机器人按钮盒按钮状态

            # 焊接数据
            ("weldVoltage", c_double),          # 焊接电压 V
            ("weldCurrent", c_double),          # 焊接电流
            ("weldTrackVel", c_double),         # 焊缝跟踪速度 mm/s

            ("tpdException", c_uint8),            # TPD轨迹加载数量超限，0-未超限，1-超限
            ("alarmRebootRobot", c_uint8),      # 警告，1-松开急停按钮请断电重启控制箱，2-关节通讯异常请断电重启控制箱
            ("modbusMasterConnect", c_uint8),   # bit0-bit7位对应ModbusTCP的0-7主站连接状态
            ("modbusSlaveConnect", c_uint8),    # ModbusTCP从站连接状态
            ("btnBoxStopSignal", c_uint8),      # 按钮盒急停信号
            ("dragAlarm", c_uint8),             # 拖动警告
            ("safetyDoorAlarm", c_uint8),       # 安全门警告
            ("safetyPlaneAlarm", c_uint8),      # 进入安全墙警告
            ("motonAlarm", c_uint8),            # 运动警告
            ("interfaceAlarm", c_uint8),        # 进入干涉区警告
            ("udpCmdState", c_int),             # 20007端口UDP通讯连接状态
            ("weldReadyState", c_uint8),        # 焊机准备完成状态
            ("alarmCheckEmergStopBtn", c_uint8),    # 0-正常；1-通信异常，检查急停按钮是否松开
            ("tsTmCmdComError", c_uint8),       # 0-正常；1-扭矩指令通讯失败
            ("tsTmStateComError", c_uint8),     # 0-正常；1-扭矩状态通讯失败
            ("ctrlBoxError", c_int),            # 控制箱错误
            ("safetyDataState", c_uint8),       # 安全数据状态标志
            ("forceSensorErrState", c_uint8),   # 力传感器连接超时故障
            ("ctrlOpenLuaErrCode", c_uint8 * 4),  # 4个控制器外设协议错误码
            ("strangePosFlag", c_uint8),        # 当前处于奇异位姿标志
            ("alarm", c_uint8),                 # 警告
            ("driverAlarm", c_uint8),           # 驱动器报警轴号
            ("aliveSlaveNumError", c_uint8),    # 活动从站数量错误
            ("slaveComError", c_uint8 * 8),     # 从站错误状态
            ("cmdPointError", c_uint8),         # 指令点错误
            ("IOError", c_uint8),               # IO错误
            ("gripperError", c_uint8),          # 夹爪错误
            ("fileError", c_uint8),             # 文件错误
            ("paraError", c_uint8),             # 参数错误
            ("exaxisOutLimitError", c_uint8),   # 外部轴超出软限位错误
            ("driverComError", c_uint8 * 6),    # 与驱动器通信故障
            ("driverError", c_uint8),           # 驱动器通信故障轴号
            ("outSoftLimitError", c_uint8),     # 超出软限位故障
            ("axleGenComData", c_uint8 * 130),   # 轴通用通讯非周期数据
            ("socketConnTimeout", c_uint8),     # socket连接超时
            ("socketReadTimeout", c_uint8),     # socket读取超时
            ("tsWebStateComErr", c_uint8),      # TS_WEB状态通讯错误
            ("exaxisCoordID", c_uint8),         # 外部扩展轴ID
            ("ProgramRunState", c_uint8),       # LUA程序运行状态 0-程序未运行；1-程序运行中(包含程序暂停)
            ("check_sum", c_uint16)          # 和校验
        ]

控制器状态反馈数据包
~~~~~~~~~~~~~~~~~~~~~~~~
.. versionadded:: python SDK-v2.1.7
    
.. csv-table:: 
    :header-rows: 1
    :name: 控制器状态反馈数据包
    :widths: 20 30

    "变量","含义"
    "program_state","程序运行状态，1-停止；2-运行；3-暂停"
    "robot_state","机器人运动状态，1-停止；2-运行；3-暂停；4-拖动"
    "main_code","主故障码"
    "sub_code",	子故障码"
    "robot_mode","机器人模式，0-自动模式；1-手动模式"
    "jt_cur_pos[i]","关节当前位置,单位deg,i:0~5"
    "tl_cur_pos[i]","工具当前位姿,单位deg&mm,i:0~5"
    "flange_cur_pos[i]","末端法兰当前位姿,单位deg&mm,i:0~5"
    "actual_qd[i]","机器人当前关节速度,单位deg/s,i:0~5"
    "actual_qdd[i]","机器人当前关节加速度,单位deg/s^2,i:0~5"
    "target_TCP_CmpSpeed[i]","机器人TCP合成指令速度,单位mm/s&deg/s,i:0~1"
    "target_TCP_Speed[i]","机器人TCP指令速度,单位mm/s&deg/s,i:0~5"
    "actual_TCP_CmpSpeed[i]","机器人TCP合成实际速度,单位mm/s&deg/s,i:0~1"
    "actual_TCP_Speed[i]","机器人TCP实际速度,单位mm/s&deg/s,i:0~5"
    "jt_cur_tor[i]","当前扭矩,单位N·m ,i:0~5"
    "tool","应用的工具坐标系编号"
    "user","应用的工件坐标系编号"
    "cl_dgt_output_h","控制箱数字量IO输出15-8"
    "cl_dgt_output_l","控制箱数字量IO输出7-0"
    "tl_dgt_output_l","工具数字量IO输出7-0，仅bit0-bit1有效"
    "dgt_input_h","控制箱数字量IO输入15-8"
    "cl_dgt_input_l","控制箱数字量IO输入7-0"
    "tl_dgt_input_l","工具数字量IO输入7-0，仅bit0-bit1有效"
    "cl_analog_input[i]","控制箱模拟量输入,i:0~2"
    "tl_anglog_input","工具模拟量输入"
    "ft_sensor_raw_data","力矩传感器原始数据,单位N&Nm,i:0~5"
    "ft_sensor_data","力矩传感器数据,单位N&Nm,i:0~5"
    "ft_sensor_active","力矩传感器激活状态，0-复位，1-激活"
    "EmergencyStop","急停标志,0-急停未按下,1-急停按下"
    "motion_done","运动到位信号,1-到位，0-未到位"
    "gripper_motiondone","夹爪运动完成信号，0-未完成，1-完成(未检测到物体)，2-运动完成（检测到物体）"
    "mc_queue_len","运动指令队列长度"
    "collisionState","碰撞检测,1-碰撞，0-无碰撞 "
    "trajectory_pnum","轨迹点编号"
    "safety_stop0_state","安全停止信号SI0"
    "safety_stop1_state","安全停止信号SI1"
    "gripper_fault_id","错误夹爪号"
    "gripper_fault","夹爪故障0-无故障 1-485超时 2-指令错误 3-工件掉落 其他-夹爪故障码"
    "gripper_active","夹爪激活状态，0-未激活，1-激活"
    "gripper_position","夹爪位置(百分比)"
    "gripper_speed","夹爪速度(百分比)"
    "gripper_current","夹爪电流(百分比)"
    "gripper_tmp","夹爪温度,单位℃"
    "gripper_voltage","夹爪电压,单位V"
    "auxState.servoId","485扩展轴,伺服驱动器ID号,i:0~3"
    "auxState.servoErrCode","485扩展轴,伺服驱动器故障码,i:0~3"
    "auxState.servoState","485扩展轴,伺服驱动器状态,i:0~3"
    "auxState.servoPos","485扩展轴,伺服当前位置,i:0~3"
    "auxState.servoVel","485扩展轴,伺服当前速度,i:0~3"
    "auxState.servoTorque","485扩展轴,伺服当前转矩,i:0~3"
    "extAxisStatus[i].pos","UDP扩展轴,位置,i:0~3"
    "extAxisStatus[i].vel","UDP扩展轴,速度,i:0~3"
    "extAxisStatus[i].errorCode","UDP扩展轴,故障码,i:0~3"
    "extAxisStatus[i].ready","UDP扩展轴,伺服准备好,i:0~3"
    "extAxisStatus[i].inPos","UDP扩展轴,伺服到位,i:0~3"
    "extAxisStatus[i].alarm","UDP扩展轴,伺服报警,i:0~3"
    "extAxisStatus[i].flerr","UDP扩展轴,跟随误差,i:0~3"
    "extAxisStatus[i].nlimit","UDP扩展轴,到负限位,i:0~3"
    "extAxisStatus[i].pLimit","UDP扩展轴,到正限位,i:0~3"
    "extAxisStatus[i].mdbsOffLine","UDP扩展轴,驱动器485总线掉线"
    "extAxisStatus[i].mdbsTimeout","UDP扩展轴,控制卡与控制箱485通信超时"
    "extAxisStatus[i].homingStatus","UDP扩展轴,回零状态"
    "extDIState","扩展数字输入状态"
    "extDOState","扩展数字输出状态"
    "extAIState","扩展模拟输入状态"
    "extAOState","扩展模拟输出状态"
    "rbtEnableState","机器人使能状态"
    "jointDriverTorque","关节驱动器当前扭矩"
    "jointDriverTemperature","关节驱动器当前温度"
    "year","年"
    "mouth","月"
    "day","日"
    "hour","小时"
    "minute","分"
    "second","秒"
    "millisecond","毫秒"
    "softwareUpgradeState","机器人软件升级状态"
    "endLuaErrCode","末端LUA运行状态"
    "cl_analog_output[i]","控制箱模拟量输出,i:0~1"
    "tl_analog_output","工具模拟量输出"
    "gripperRotNum","旋转夹爪当前旋转圈数"
    "gripperRotSpeed","旋转夹爪当前旋转速度百分比"
    "gripperRotTorque","旋转夹爪当前旋转力矩百分比"
    "weldingBreakOffState","焊接中断状态"
    "jt_tgt_tor","关节指令力矩"
    "smartToolState","SmartTool手柄按钮状态"
    "wideVoltageCtrlBoxTemp","宽电压控制箱温度"
    "wideVoltageCtrlBoxFanCurrent","宽电压控制箱风扇电流(ma)"
    "toolCoord[i]","工具坐标系,i:0~5"
    "wobjCoord[i]","工件坐标系,i:0~5"
    "extoolCoord[i]","外部工具坐标系,i:0~5"
    "exAxisCoord[i]","扩展轴坐标系,i:0~5"
    "load","负载质量"
    "loadCog[i]","负载质心,i:0~2"
    "lastServoTarget[i]","队列中最后一个ServoJ目标位置,i:0~5"
    "servoJCmdNum","ServoJ指令计数"

伺服控制器状态
~~~~~~~~~~~~~~~~~~~~~~~~
.. versionadded:: python SDK-v2.1.3
    
.. csv-table:: 
    :header-rows: 1
    :name: 伺服控制器状态
    :widths: 20 30

    "变量","含义"
    "servoId","伺服驱动器ID号"
    "servoErrCode","伺服驱动器故障码"
    "servoState","伺服驱动器状态"
    "servoPos","伺服当前位置"
    "servoVel","伺服当前速度"
    "servoTorque","伺服当前转矩"

扩展轴状态
~~~~~~~~~~~~~~~~~~~~~~~~
.. versionadded:: python SDK-v2.1.3
    
.. csv-table:: 
    :header-rows: 1
    :name: 扩展轴状态
    :widths: 20 30

    "变量","含义"
    "pos","扩展轴位置"
    "vel","扩展轴速度"
    "errorCode","扩展轴故障码"
    "ready","伺服准备好"
    "inPos","伺服到位"
    "alarm","伺服报警"
    "flerr","跟随误差"
    "nlimit","到负限位"
    "pLimit","到正限位"
    "mdbsOffLine","驱动器485总线掉线"
    "mdbsTimeout","控制卡与控制箱485通信超时"
    "homingStatus","扩展轴回零状态"

焊接中断状态
~~~~~~~~~~~~~~~~~~~~~~~~
.. versionadded:: python SDK-v2.1.3
    
.. csv-table:: 
    :header-rows: 1
    :name: 焊接中断状态
    :widths: 20 30

    "变量","含义"
    "breakOffState","焊接中断状态"
    "weldArcState","焊接电弧中断状态"

代码示例
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    print("program_state:", robot.robot_state_pkg.program_state)
    print("robot_state:", robot.robot_state_pkg.robot_state)
    print("main_code:", robot.robot_state_pkg.main_code)
    print("sub_code:", robot.robot_state_pkg.sub_code)
    print("robot_mode:", robot.robot_state_pkg.robot_mode)
    print("jt_cur_pos0:", robot.robot_state_pkg.jt_cur_pos[0])
    print("jt_cur_pos1:", robot.robot_state_pkg.jt_cur_pos[1])
    print("jt_cur_pos2:", robot.robot_state_pkg.jt_cur_pos[2])
    print("jt_cur_pos3:", robot.robot_state_pkg.jt_cur_pos[3])
    print("jt_cur_pos4:", robot.robot_state_pkg.jt_cur_pos[4])
    print("jt_cur_pos5:", robot.robot_state_pkg.jt_cur_pos[5])
    print("tl_cur_pos0:", robot.robot_state_pkg.tl_cur_pos[0])
    print("tl_cur_pos1:", robot.robot_state_pkg.tl_cur_pos[1])
    print("tl_cur_pos2:", robot.robot_state_pkg.tl_cur_pos[2])
    print("tl_cur_pos3:", robot.robot_state_pkg.tl_cur_pos[3])
    print("tl_cur_pos4:", robot.robot_state_pkg.tl_cur_pos[4])
    print("tl_cur_pos5:", robot.robot_state_pkg.tl_cur_pos[5])
    print("flange_cur_pos0:", robot.robot_state_pkg.flange_cur_pos[0])
    print("flange_cur_pos1:", robot.robot_state_pkg.flange_cur_pos[1])
    print("flange_cur_pos2:", robot.robot_state_pkg.flange_cur_pos[2])
    print("flange_cur_pos3:", robot.robot_state_pkg.flange_cur_pos[3])
    print("flange_cur_pos4:", robot.robot_state_pkg.flange_cur_pos[4])
    print("flange_cur_pos5:", robot.robot_state_pkg.flange_cur_pos[5])
    print("actual_qd0:", robot.robot_state_pkg.actual_qd[0])
    print("actual_qd1:", robot.robot_state_pkg.actual_qd[1])
    print("actual_qd2:", robot.robot_state_pkg.actual_qd[2])
    print("actual_qd3:", robot.robot_state_pkg.actual_qd[3])
    print("actual_qd4:", robot.robot_state_pkg.actual_qd[4])
    print("actual_qd5:", robot.robot_state_pkg.actual_qd[5])
    print("actual_qdd0:", robot.robot_state_pkg.actual_qdd[0])
    print("actual_qdd1:", robot.robot_state_pkg.actual_qdd[1])
    print("actual_qdd2:", robot.robot_state_pkg.actual_qdd[2])
    print("actual_qdd3:", robot.robot_state_pkg.actual_qdd[3])
    print("actual_qdd4:", robot.robot_state_pkg.actual_qdd[4])
    print("actual_qdd5:", robot.robot_state_pkg.actual_qdd[5])
    print("target_TCP_CmpSpeed0:", robot.robot_state_pkg.target_TCP_CmpSpeed[0])
    print("target_TCP_CmpSpeed1:", robot.robot_state_pkg.target_TCP_CmpSpeed[1])
    print("target_TCP_Speed0:", robot.robot_state_pkg.target_TCP_Speed[0])
    print("target_TCP_Speed1:", robot.robot_state_pkg.target_TCP_Speed[1])
    print("target_TCP_Speed2:", robot.robot_state_pkg.target_TCP_Speed[2])
    print("target_TCP_Speed3:", robot.robot_state_pkg.target_TCP_Speed[3])
    print("target_TCP_Speed4:", robot.robot_state_pkg.target_TCP_Speed[4])
    print("target_TCP_Speed5:", robot.robot_state_pkg.target_TCP_Speed[5])
    print("actual_TCP_CmpSpeed0:", robot.robot_state_pkg.actual_TCP_CmpSpeed[0])
    print("actual_TCP_CmpSpeed1:", robot.robot_state_pkg.actual_TCP_CmpSpeed[1])
    print("actual_TCP_Speed0:", robot.robot_state_pkg.actual_TCP_Speed[0])
    print("actual_TCP_Speed1:", robot.robot_state_pkg.actual_TCP_Speed[1])
    print("actual_TCP_Speed2:", robot.robot_state_pkg.actual_TCP_Speed[2])
    print("actual_TCP_Speed3:", robot.robot_state_pkg.actual_TCP_Speed[3])
    print("actual_TCP_Speed4:", robot.robot_state_pkg.actual_TCP_Speed[4])
    print("actual_TCP_Speed5:", robot.robot_state_pkg.actual_TCP_Speed[5])
    print("jt_cur_tor0:", robot.robot_state_pkg.jt_cur_tor[0])
    print("jt_cur_tor1:", robot.robot_state_pkg.jt_cur_tor[1])
    print("jt_cur_tor2:", robot.robot_state_pkg.jt_cur_tor[2])
    print("jt_cur_tor3:", robot.robot_state_pkg.jt_cur_tor[3])
    print("jt_cur_tor4:", robot.robot_state_pkg.jt_cur_tor[4])
    print("jt_cur_tor5:", robot.robot_state_pkg.jt_cur_tor[5])
    print("tool:", robot.robot_state_pkg.tool)
    print("user:", robot.robot_state_pkg.user)
    print("cl_dgt_output_h:", robot.robot_state_pkg.cl_dgt_output_h)
    print("cl_dgt_output_l:", robot.robot_state_pkg.cl_dgt_output_l)
    print("tl_dgt_output_l:", robot.robot_state_pkg.tl_dgt_output_l)
    print("cl_dgt_input_h:", robot.robot_state_pkg.cl_dgt_input_h)
    print("cl_dgt_input_l:", robot.robot_state_pkg.cl_dgt_input_l)
    print("tl_dgt_input_l:", robot.robot_state_pkg.tl_dgt_input_l)
    print("cl_analog_input0:", robot.robot_state_pkg.cl_analog_input[0])
    print("cl_analog_input1:", robot.robot_state_pkg.cl_analog_input[1])
    print("tl_anglog_input:", robot.robot_state_pkg.tl_anglog_input)
    print("ft_sensor_raw_data0:", robot.robot_state_pkg.ft_sensor_raw_data[0])
    print("ft_sensor_raw_data1:", robot.robot_state_pkg.ft_sensor_raw_data[1])
    print("ft_sensor_raw_data2:", robot.robot_state_pkg.ft_sensor_raw_data[2])
    print("ft_sensor_raw_data3:", robot.robot_state_pkg.ft_sensor_raw_data[3])
    print("ft_sensor_raw_data4:", robot.robot_state_pkg.ft_sensor_raw_data[4])
    print("ft_sensor_raw_data5:", robot.robot_state_pkg.ft_sensor_raw_data[5])
    print("ft_sensor_data0:", robot.robot_state_pkg.ft_sensor_data[0])
    print("ft_sensor_data1:", robot.robot_state_pkg.ft_sensor_data[1])
    print("ft_sensor_data2:", robot.robot_state_pkg.ft_sensor_data[2])
    print("ft_sensor_data3:", robot.robot_state_pkg.ft_sensor_data[3])
    print("ft_sensor_data4:", robot.robot_state_pkg.ft_sensor_data[4])
    print("ft_sensor_data5:", robot.robot_state_pkg.ft_sensor_data[5])
    print("ft_sensor_active:", robot.robot_state_pkg.ft_sensor_active)
    print("EmergencyStop:", robot.robot_state_pkg.EmergencyStop)
    print("motion_done:", robot.robot_state_pkg.motion_done)
    print("gripper_motiondone:", robot.robot_state_pkg.gripper_motiondone)
    print("mc_queue_len:", robot.robot_state_pkg.mc_queue_len)
    print("collisionState:", robot.robot_state_pkg.collisionState)
    print("trajectory_pnum:", robot.robot_state_pkg.trajectory_pnum)
    print("safety_stop0_state:", robot.robot_state_pkg.safety_stop0_state)
    print("safety_stop1_state:", robot.robot_state_pkg.safety_stop1_state)
    print("gripper_fault_id:", robot.robot_state_pkg.gripper_fault_id)
    print("gripper_fault:", robot.robot_state_pkg.gripper_fault)
    print("gripper_active:", robot.robot_state_pkg.gripper_active)
    print("gripper_position:", robot.robot_state_pkg.gripper_position)
    print("gripper_speed:", robot.robot_state_pkg.gripper_speed)
    print("gripper_current:", robot.robot_state_pkg.gripper_current)
    print("gripper_tmp:", robot.robot_state_pkg.gripper_tmp)
    print("gripper_voltage:", robot.robot_state_pkg.gripper_voltage)
    print("auxState.servoId:", robot.robot_state_pkg.auxState.servoId)
    print("auxState.servoErrCode:", robot.robot_state_pkg.auxState.servoErrCode)
    print("auxState.servoState:", robot.robot_state_pkg.auxState.servoState)
    print("auxState.servoPos:", robot.robot_state_pkg.auxState.servoPos)
    print("auxState.servoVel:", robot.robot_state_pkg.auxState.servoVel)
    print("auxState.servoTorque:", robot.robot_state_pkg.auxState.servoTorque)
    for i in range(4):
        print("extAxisStatus.pos:", i,robot.robot_state_pkg.extAxisStatus[i].pos)
        print("extAxisStatus.vel:", i,robot.robot_state_pkg.extAxisStatus[i].vel)
        print("extAxisStatus.errorCode:", i,robot.robot_state_pkg.extAxisStatus[i].errorCode)
        print("extAxisStatus.ready:", i,robot.robot_state_pkg.extAxisStatus[i].ready)
        print("extAxisStatus.inPos:", i,robot.robot_state_pkg.extAxisStatus[i].inPos)
        print("extAxisStatus.alarm:", i,robot.robot_state_pkg.extAxisStatus[i].alarm)
        print("extAxisStatus.flerr:", i,robot.robot_state_pkg.extAxisStatus[i].flerr)
        print("extAxisStatus.nlimit:", i,robot.robot_state_pkg.extAxisStatus[i].nlimit)
        print("extAxisStatus.pLimit:", i,robot.robot_state_pkg.extAxisStatus[i].pLimit)
        print("extAxisStatus.mdbsOffLine:", i,robot.robot_state_pkg.extAxisStatus[i].mdbsOffLine)
        print("extAxisStatus.mdbsTimeout:", i,robot.robot_state_pkg.extAxisStatus[i].mdbsTimeout)
        print("extAxisStatus.homingStatus:", i,robot.robot_state_pkg.extAxisStatus[i].homingStatus)
    for i in range(8):
        print("extDIState:",i, robot.robot_state_pkg.extDIState[i])
        print("extDOState:", i,robot.robot_state_pkg.extDOState[i])
    for i in range(4):
        print("extAIState:", i,robot.robot_state_pkg.extAIState[i])
        print("extAOState:", robot.robot_state_pkg.extAOState[i])
    print("rbtEnableState:", robot.robot_state_pkg.rbtEnableState)
    print("jointDriverTorque0:", robot.robot_state_pkg.jointDriverTorque[0])
    print("jointDriverTorque1:", robot.robot_state_pkg.jointDriverTorque[1])
    print("jointDriverTorque2:", robot.robot_state_pkg.jointDriverTorque[2])
    print("jointDriverTorque3:", robot.robot_state_pkg.jointDriverTorque[3])
    print("jointDriverTorque4:", robot.robot_state_pkg.jointDriverTorque[4])
    print("jointDriverTorque5:", robot.robot_state_pkg.jointDriverTorque[5])
    print("jointDriverTemperature:", robot.robot_state_pkg.jointDriverTemperature[0])
    print("jointDriverTemperature:", robot.robot_state_pkg.jointDriverTemperature[1])
    print("jointDriverTemperature:", robot.robot_state_pkg.jointDriverTemperature[2])
    print("jointDriverTemperature:", robot.robot_state_pkg.jointDriverTemperature[3])
    print("jointDriverTemperature:", robot.robot_state_pkg.jointDriverTemperature[4])
    print("jointDriverTemperature:", robot.robot_state_pkg.jointDriverTemperature[5])
    print("year:", robot.robot_state_pkg.year)
    print("mouth:", robot.robot_state_pkg.mouth)
    print("day:", robot.robot_state_pkg.day)
    print("hour:", robot.robot_state_pkg.hour)
    print("minute:", robot.robot_state_pkg.minute)
    print("second:", robot.robot_state_pkg.second)
    print("millisecond:", robot.robot_state_pkg.millisecond)
    print("softwareUpgradeState:", robot.robot_state_pkg.softwareUpgradeState)
    print("endLuaErrCode:", robot.robot_state_pkg.endLuaErrCode)
    print("cl_analog_output[0]:", robot.robot_state_pkg.cl_analog_output[0])
    print("cl_analog_output[1]:", robot.robot_state_pkg.cl_analog_output[1])
    print("tl_analog_output:", robot.robot_state_pkg.tl_analog_output)
    print("gripperRotNum:", robot.robot_state_pkg.gripperRotNum)
    print("gripperRotSpeed:", robot.robot_state_pkg.gripperRotSpeed)
    print("gripperRotTorque:", robot.robot_state_pkg.gripperRotTorque)
    print("jt_tgt_tor:", robot.robot_state_pkg.jt_tgt_tor)
    print("smartToolState:", robot.robot_state_pkg.smartToolState)
    print("wideVoltageCtrlBoxTemp:", robot.robot_state_pkg.wideVoltageCtrlBoxTemp)
    print("wideVoltageCtrlBoxFanCurrent:", robot.robot_state_pkg.wideVoltageCtrlBoxFanCurrent)
    print("toolCoord0:", robot.robot_state_pkg.toolCoord[0])
    print("toolCoord1:", robot.robot_state_pkg.toolCoord[1])
    print("toolCoord2:", robot.robot_state_pkg.toolCoord[2])
    print("toolCoord3:", robot.robot_state_pkg.toolCoord[3])
    print("toolCoord4:", robot.robot_state_pkg.toolCoord[4])
    print("toolCoord5:", robot.robot_state_pkg.toolCoord[5])
    print("wobjCoord0:", robot.robot_state_pkg.wobjCoord[0])
    print("wobjCoord1:", robot.robot_state_pkg.wobjCoord[1])
    print("wobjCoord2:", robot.robot_state_pkg.wobjCoord[2])
    print("wobjCoord3:", robot.robot_state_pkg.wobjCoord[3])
    print("wobjCoord4:", robot.robot_state_pkg.wobjCoord[4])
    print("wobjCoord5:", robot.robot_state_pkg.wobjCoord[5])
    print("extoolCoord0:", robot.robot_state_pkg.extoolCoord[0])
    print("extoolCoord1:", robot.robot_state_pkg.extoolCoord[1])
    print("extoolCoord2:", robot.robot_state_pkg.extoolCoord[2])
    print("extoolCoord3:", robot.robot_state_pkg.extoolCoord[3])
    print("extoolCoord4:", robot.robot_state_pkg.extoolCoord[4])
    print("extoolCoord5:", robot.robot_state_pkg.extoolCoord[5])
    print("exAxisCoord0:", robot.robot_state_pkg.exAxisCoord[0])
    print("exAxisCoord1:", robot.robot_state_pkg.exAxisCoord[1])
    print("exAxisCoord2:", robot.robot_state_pkg.exAxisCoord[2])
    print("exAxisCoord3:", robot.robot_state_pkg.exAxisCoord[3])
    print("exAxisCoord4:", robot.robot_state_pkg.exAxisCoord[4])
    print("exAxisCoord5:", robot.robot_state_pkg.exAxisCoord[5])
    print("load:", robot.robot_state_pkg.load)
    print("loadCog0:", robot.robot_state_pkg.loadCog[0])
    print("loadCog1:", robot.robot_state_pkg.loadCog[1])
    print("loadCog2:", robot.robot_state_pkg.loadCog[2])
    print("lastServoTarget0:", robot.robot_state_pkg.lastServoTarget[0])
    print("lastServoTarget1:", robot.robot_state_pkg.lastServoTarget[1])
    print("lastServoTarget2:", robot.robot_state_pkg.lastServoTarget[2])
    print("lastServoTarget3:", robot.robot_state_pkg.lastServoTarget[3])
    print("lastServoTarget4:", robot.robot_state_pkg.lastServoTarget[4])
    print("lastServoTarget5:", robot.robot_state_pkg.lastServoTarget[5])
    print("servoJCmdNum:", robot.robot_state_pkg.servoJCmdNum)

机器人状态反馈配置列表枚举类型
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:

    class RobotState(enum.Enum):
        """CNDE状态类型枚举"""
        FrameHead = 0
        FrameCnt = 1
        DataLen = 2
        ProgramState = 3
        RobotState = 4
        MainCode = 5
        SubCode = 6
        RobotMode = 7
        JointCurPos = 8
        ToolCurPos = 9
        FlangeCurPos = 10
        ActualJointVel = 11
        ActualJointAcc = 12
        TargetTCPCmpSpeed = 13
        TargetTCPSpeed = 14
        ActualTCPCmpSpeed = 15
        ActualTCPSpeed = 16
        ActualJointTorque = 17
        Tool = 18
        User = 19
        ClDgtOutputH = 20
        ClDgtOutputL = 21
        TlDgtOutputL = 22
        ClDgtInputH = 23
        ClDgtInputL = 24
        TlDgtInputL = 25
        ClAnalogInput = 26
        TlAnglogInput = 27
        FtSensorRawData = 28
        FtSensorData = 29
        FtSensorActive = 30
        EmergencyStop = 31
        MotionDone = 32
        GripperMotiondone = 33
        McQueueLen = 34
        CollisionState = 35
        TrajectoryPnum = 36
        SafetyStop0State = 37
        SafetyStop1State = 38
        GripperFaultId = 39
        GripperFault = 40
        GripperActive = 41
        GripperPosition = 42
        GripperSpeed = 43
        GripperCurrent = 44
        GripperTemp = 45
        GripperVoltage = 46
        AuxState = 47
        ExtAxisStatus = 48
        ExtDIState = 49
        ExtDOState = 50
        ExtAIState = 51
        ExtAOState = 52
        RbtEnableState = 53
        JointDriverTorque = 54
        JointDriverTemperature = 55
        RobotTime = 56
        SoftwareUpgradeState = 57
        EndLuaErrCode = 58
        ClAnalogOutput = 59
        TlAnalogOutput = 60
        GripperRotNum = 61
        GripperRotSpeed = 62
        GripperRotTorque = 63
        WeldingBreakOffState = 64
        TargetJointTorque = 65
        SmartToolState = 66
        WideVoltageCtrlBoxTemp = 67
        WideVoltageCtrlBoxFanCurrent = 68
        ToolCoord = 69
        WobjCoord = 70
        ExtoolCoord = 71
        ExAxisCoord = 72
        Load = 73
        LoadCog = 74
        LastServoTarget = 75
        ServoJCmdNum = 76
        TargetJointPos = 77
        TargetJointVel = 78
        TargetJointAcc = 79
        TargetJointCurrent = 80
        ActualJointCurrent = 81
        ActualTCPForce = 82
        TargetTCPPos = 83
        CollisionLevel = 84
        SpeedScaleManual = 85
        SpeedScaleAuto = 86
        LuaLineNum = 87
        AbnomalStop = 88
        CurrentLuaFileName = 89
        ProgramTotalLine = 90
        SafetyBoxSingal = 91
        WeldVoltage = 92
        WeldCurrent = 93
        WeldTrackVel = 94
        TpdException = 95
        AlarmRebootRobot = 96
        ModbusMasterConnect = 97
        ModbusSlaveConnect = 98
        BtnBoxStopSignal = 99
        DragAlarm = 100
        SafetyDoorAlarm = 101
        SafetyPlaneAlarm = 102
        MotonAlarm = 103
        InterfaceAlarm = 104
        UdpCmdState = 105
        WeldReadyState = 106
        AlarmCheckEmergStopBtn = 107
        TsTmCmdComError = 108
        TsTmStateComError = 109
        CtrlBoxError = 110
        SafetyDataState = 111
        ForceSensorErrState = 112
        CtrlOpenLuaErrCode = 113
        StrangePosFlag = 114
        Alarm = 115
        DriverAlarm = 116
        AliveSlaveNumError = 117
        SlaveComError = 118
        CmdPointError = 119
        IOError = 120
        GripperError = 121
        FileError = 122
        ParaError = 123
        ExaxisOutLimitError = 124
        DriverComError = 125
        DriverError = 126
        OutSoftLimitError = 127
        AxleGenComData = 128
        SocketConnTimeout = 129
        SocketReadTimeout = 130
        TsWebStateComErr = 131
        ExaxisCoordID = 132
        ProgramRunState = 133