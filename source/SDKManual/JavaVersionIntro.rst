版本更新说明
====================

.. toctree:: 
    :maxdepth: 5

.. list-table::
   :widths: 10 10 30
   :header-rows: 0
   :align: center

   * - **版本号**
     - **日期**
     - **更新描述**

   * - V3.9.9
     - 2026-09-01
     - | 1.更新获取夹爪运动状态接口GetGripperMotionDone()，更新夹爪状态输出参数定义及使用范围；
       | 2.修改GetInverseKinExaxis()包含扩展轴位置的逆运动学求解接口，增加关节配置参数，默认值为-1参考当前关节配置；
       | 3.修改FT_SpiralSearch()、FT_LinInsertion()、FT_FindSurface()力控接口增加未检测到力/力矩的处理策略参数；
       | 4.修改SetDIConfig()、GetDIConfig()、SetDOConfig()、GetDOConfig()机器人控制箱CIO
       | 5.功能配置接口参数描述，更新新增的功能名称及功能码；新增获取安全配置参数校验和接口GetSafetyParamsCheckSum()；
       | 6.修改机器人基础控制代码示例，增加手动高速模式切换代码示例；
       | 7.新增安全操作密码校验接口SafetyOPPasswordCheck()；
       | 8.新增等待夹爪运动状态接口GripperWaitMotionDone()，支持超时和策略设置（仅适用于末端开放协议）；
       | 9.新增同步系统时间至机器人接口SetRobottime()；
       | 10.新增关节空间伺服模式运动接口ServoJ()，支持多点位一次输入；
       | 11.新增激光记录复现+常规摆动代码示例；
       | 12.新增激光记录复现+扩展轴异步运动+定点摆动代码示例；
       | 13.新增螺旋线探索接口FT_SpiralSearch()；
       | 14.新增切换手动高速模式接口HiSpeedManualSwitch()；
       | 15.新增安全双通道CI功能配置接口SetSafetyDIConfig()；
       | 16.新增安全双通道CO功能配置接口SetSafetyDOConfig()；
       | 17.新增安全双通道CI/CO功能配置设置-读取-清零验证示例。
       
   * - V3.9.8
     - 2026-07-27
     - | 1.更新机器人状态反馈结构体，增加当前机器人lua程序运行状态，0-程序未运行；1-程序运行中(包含程序暂停)；
       | 2.SetExToolCoord()、SetExToolList()设置外部工具坐标系和工具坐标系列表接口更新参数描述，其中外部工具坐标系编号更新为20-39。并更新外部工具坐标系操作代码示例。
       | 3.GetToolCoordWithID()获取工具坐标系参数接口增加工具类型、安装位置、工具ID、负载编号参数获取。
       | 4.GetWObjCoordWithID()获取工件坐标系参数接口增加参考坐标系参数获取；
       | 5.GetExToolCoordWithID()获取外部工具坐标系参数接口增加机器人末端安装工件坐标系位姿参数获取。
       | 6.GetExAxisCoordWithID()获取扩展轴坐标系参数接口增加扩展轴号和标定标志参数获取。
       | 7.SetVelReducePara()设置机器人安全速度接口增加机器人关节安全速度参数设置。
       | 8.设置焊接参数代码示例中增加焊机控制模式获取示例。
       | 9.设置扩展IO焊接信号代码示例增加获取扩展DI、扩展DO功能配置代码示例。
       | 10.新增设置机器人关节安全速度代码示例；
       | 11.新增WaitStationaryMotionDone()等待原地空运动完成接口；
       | 12.新增SetStationaryTrackPara()传送带原地跟踪参数配置接口，及传送带原地跟踪代码示例；
       | 13.新增WorkPieceTrsfStart()、WorkPieceTrsfEnd()工件坐标系转换开始、结束接口，及工件坐标系转换代码示例。
       | 14.增加GetWeldMachineCtrlMode()获取焊机控制模式接口。
       | 15.增加GetExtDIConfig()、GetExtDOConfig()获取扩展DI功能、扩展DI功能接口。
       
   * - V3.9.7
     - 2026-06-25
     - | 1.PhotoelectricSensorTCPCalibration()参数可自适应无路径的文件名；
       | 2.LoadTrajectoryJ()参数可自适应无路径的文件名；
       | 3.LoadTrajectoryLA()参数可自适应无路径的文件名；
       | 4.LoadDefaultProgConfig()参数可自适应无路径的文件名；
       | 5.ProgramLoad()参数可自适应无路径的文件名；
       | 6.SetAxleLuaEnableDeviceType()接口增加灵巧手启用状态参数；
       | 7.GetAxleLuaEnableDeviceType()接口增加灵巧手启用状态参数；
       | 8.修改获取当前配置的末端设备启用类型接、夹爪动作控制接口；
       | 9.新增灵巧手使能及功能码；
       | 10.新增SetDexterousHandsMove ()控制灵巧手运动接口；
       | 11.新增SetDexterousHandsAct ()控制灵巧手复位激活接口；
       | 12.新增ClearDexterousHandsError ()清除灵巧手错误接口；
       | 13.新增SetDexterousHandsFunc()设置启用灵巧手动作控制功能接口；
       | 14.新增GetDexterousHandsFunc()获取启用灵巧手动作控制功能接口；
       | 15.新增设置、获取摆动结束回周期零点接口；
       | 16.新增SetWeaveOffsetRT()设置摆动实时偏移、SetSpeedInstant()实时设置速度接口。

   * - V3.9.6
     - 2026-05-26
     - | 1.更新机器人状态反馈结构体，增加扩展轴坐标系编号状态；
       | 2.更新机器人状态反馈配置枚举类型，增加扩展轴坐标系编号配置枚举；
       | 3.新增ExtAxisGetParamConfig()获取UDP扩展轴参数配置接口。
       | 4.新增ServoJV()机器人关节空间速度伺服模式运动接口。
       | 5.新增ServoMITStart()机器人关节MIT控制开始接口。
       | 6.新增ServoMITEnd()机器人关节MIT控制结束接口。
       | 7.新增ServoMIT()机器人关节MIT控制接口。
       | 8.新增SetLaserWeldingParam()机器人激光焊接参数配置接口。
       | 9.新增SetLaserWeldingStartEnd()设置机器人激光焊接开启停止接口。
       | 10.新增SetLaserWeldingEnable()设置激光焊机使能去使能接口。
       | 11.新增ResetLaserWeldingErr()设置激光焊机故障复位接口。
       | 12.新增GetLaserWeldingRunningState()获取激光焊机运行状态接口。
       | 13.新增GetLaserWeldingErrState()获取激光焊机故障状态接口。
       | 14.新增GetLaserWeldingParamTarget()获取激光焊接配置参数接口。
       | 15.新增GetLaserWeldingParamActual()获取当前激光焊机生效的配置参数接口。
       | 16.新增SetLaserWeldingEnableExtDoNum()配置激光焊机扩展IO使能DO端口接口。
       | 17.新增SetLaserWeldingStartExtDoNum()配置激光焊机扩展IO启动DO端口接口。
       | 18.新增SetLaserWeldingErrResetExtDoNum()配置激光焊机扩展IO故障复位DO端口接口。
       | 19.新增SetLaserWeldingRunningStateExtDiNum()配置激光焊机扩展IO运行状态（出光状态）DI端口接口。
       | 20.新增SetLaserWeldingErrStateExtDiNum()配置激光焊机扩展IO故障状态DI端口接口。

   * - V3.9.5
     - 2026-04-24
     - | 1.SetTrajectoryJSpeed()接口新增模式降速模式、直接切换；
       | 2.更新机器人状态反馈结构体类型；
       | 3.新增机器人状态反馈配置枚举类型；
       | 4.新增机器人状态反馈配置结果类；
       | 5.新增SetRobotRealtimeStateConfig()配置机器人CNDE状态反馈接口；
       | 6.新增AddRobotRealtimeState()CNDE状态配置添加一个机器人状态接口；
       | 7.新增DeleteRobotRealtimeState()CNDE状态配置删除一个机器人状态接口；
       | 8.新增SetRobotRealtimeStatePeriod()设置CNDE状态反馈周期接口；
       | 9.新增GetRobotRealtimeStateConfig()获取当前CNDE状态反馈所有状态集合和周期接口。

   * - V3.9.4
     - 2026-03-25
     - | 1.ServoJTStart()接口新增通信类型选择参数，支持XMLPRC/UDP通信；
       | 2.ServoJTEnd()接口新增通信类型选择参数，支持XMLPRC/UDP通信；
       | 3.ServoJT()接口新增通信类型选择参数，支持XMLPRC/UDP通信；
       | 4.ServoMoveStart()接口新增通信类型选择参数，支持XMLPRC/UDP通信；
       | 5.ServoMoveEnd()接口新增通信类型选择参数，支持XMLPRC/UDP通信；
       | 6.ServoJ()接口新增通信类型选择参数，支持XMLPRC/UDP通信；
       | 7.SetWeldMachineCtrlMode()接口新增控制模式选择参数；
       | 8.ExtDevGetUDPComParam()接口新增获取UDP通信参数：重启控制箱后是否自动重连；
       | 9.新增SetAxleGenComEnable()开启末端通用透传功能接口；
       | 10.新增SndRcvAxleGenComCmdData()末端发送非周期数据并等待应答接口；
       | 11.新增SetRobotStopOnComDisc()设置端口通讯断开时停止机器人运行接口；
       | 12.新增GetRobotStopOnComDisc()获取端口通讯断开时停止机器人运行参数接口；
       | 13.新增SetDIConfig()设置控制箱可配置 CI 端口功能接口；
       | 14.新增GetDIConfig()获取控制箱可配置 CI 端口功能接口；
       | 15.新增SetDOConfig()设置控制箱可配置 CO 端口功能接口；
       | 16.新增GetDOConfig()获取控制箱可配置 CO 端口功能接口；
       | 17.新增SetToolDIConfig()设置末端可配置 End-CI 端口功能接口；
       | 18.新增GetToolDIConfig()获取末端可配置 End-CI 端口功能接口；
       | 19.新增SetDIConfigLevel()设置控制箱可配置 CI 有效状态接口；
       | 20.新增GetDIConfigLevel()获取控制箱可配置 CI 有效状态接口；
       | 21.新增SetDOConfigLevel()设置控制箱可配置 CO 有效状态接口；
       | 22.新增GetDOConfigLevel()获取控制箱可配置 CO 有效状态接口；
       | 23.新增SetToolDIConfigLevel()设置末端可配置 CI 有效状态接口；
       | 24.新增GetToolDIConfigLevel()获取末端可配置 CI 有效状态接口；
       | 25.新增SetStandardDILevel()设置控制箱标准 DI 有效状态接口；
       | 26.新增GetStandardDILevel()获取控制箱标准 DI 有效状态接口；
       | 27.新增SetStandardDOLevel()设置控制箱标准 DO 有效状态接口；
       | 28.新增GetStandardDOLevel()获取控制箱标准 DO 有效状态接口；
       | 29.新增SetExAxisCmdDoneTimeUDP() 扩展轴定位完成时间设置接口；
       | 30.新增OpenLuaDownload()下载开放协议 Lua 文件接口；
       | 31.新增OpenLuaDelete()删除开放协议 Lua 文件接口；
       | 32.新增AllOpenLuaDelete()删除开放协议 Lua 文件接口；
       | 33.新增SendUDPFrameUDP ()发送指令帧接口；
       | 34.新增SetCmdRpyCallback()设置 SDK 通过 UDP 发送指令的执行结果回调函数接口；
       | 35.新增SetVelReducePara()设置安全速度参数接口；
       | 36.新增OriginPointWeaveStart()定点摆动开始接口；
       | 37.新增OriginPointWeaveEnd()定点摆动结束接口；
       | 38.新增SetUserLEDColor()设置用户自定义机器人末端灯色接口；
       | 39.新增MoveToTPDStart()运动到 TPD 轨迹记录起点接口；
   
   * - V3.9.3
     - 2026-02-11
     - | 1.ServoCart()接口增加扩展轴参数
       | 2.SetOutputResetCtlBoxDO()接口增加暂停恢复后是否重加载复位前DO状态参数
       | 3.SetOutputResetCtlBoxAO()接口增加暂停恢复后是否重加载复位前DO状态参数
       | 4.SetOutputResetAxleDO()接口增加暂停恢复后是否重加载复位前DO状态参数
       | 5.SetOutputResetAxleAO()接口增加暂停恢复后是否重加载复位前DO状态参数
       | 6.SetOutputResetExtDO()接口增加暂停恢复后是否重加载复位前DO状态参数
       | 7.SetOutputResetExtAO()接口增加暂停恢复后是否重加载复位前DO状态参数
       | 8.SetOutputResetSmartToolDO()接口增加暂停恢复后是否重加载复位前DO状态参数
       | 9.增加GetInverseKinExaxis()包含扩展轴位置的逆运动学求解接口
       
   * - V3.9.2
     - 2026-01-26
     - | 1.FT_RotInsertion()接口增加未检测到力/力矩的处理策略参数
       | 2.LaserSensorRecordandReplay()接口增加机器人定点跟踪相关参数
       | 3.增加MoveStationary()接口
       | 4.增加TCPComputeRPY()接口
       | 5.增加TCPComputeXYZ()接口
       | 6.增加TCPRecordFlangePosStart()接口
       | 7.增加TCPRecordFlangePosEnd()接口
       | 8.增加TCPGetRecordFlangePos()接口
       | 9.增加PhotoelectricSensorTCPCalibration()接口

   * - V3.9.1
     - 2025-12-25
     - | 1.MoveL()接口增加oacc速度缩放因子参数/物理加速度参数；
       | 2.MoveC()接口增加oacc速度缩放因子参数/物理加速度参数；
       | 3.Circle()接口优化关于物理速度和物理加速度的参数描述；
       | 4.增加FT_Control()重载函数，具有rx、ry启动阈值、力矩调节系数参数；
       | 5.增加SerCoderCompenParams()接口；
       
   * - V3.9.0
     - 2025-11-26
     - | 1.JointSensitivityCalibration()接口增加j1~j6关节线性度返回
       | 2.增加JointHysteresisError()接口
       | 3.增加JointRepeatability()接口
       | 4.增加SetAdmittanceParams()接口
       | 5.增加MoveToIntersectLineStart()接口
       | 6.增加MoveIntersectLine()接口
       
   * - V3.8.7
     - 2025-10-21
     - | 1.FT_Control()增加质量参数和阻尼参数接口
       | 2.增加JointSensitivityCalibration()接口
       | 3.增加JointSensitivityCollect()接口
       | 4.增加MotionQueueClear()接口
       | 5.增加GetSlavePortErrCounter()接口
       | 6.增加SlavePortErrCounterClear()接口
       | 7.增加SetVelFeedForwardRatio()接口
       | 8.增加GetVelFeedForwardRatio()接口
       | 9.增加RobotMCULogCollect()接口
       | 10.状态结构体增加ServoJ指令计数及最后一个指令目标位置数据
       | 11.新螺旋线参数结构体SpiralParam增加速度加速度参数模式；

   * - V3.8.6
     - 2025-09-19
     - | 1.SetLoadCoord()接口增加负载编号参数
       | 2.增加LaserTrackingLaserOnOff()接口
       | 3.增加LaserTrackingTrackOnOff()接口
       | 4.增加LaserTrackingSearchStart_xyz()接口
       | 5.增加LaserTrackingSearchStart_point()接口
       | 6.增加LaserTrackingSearchStop()接口
       | 7.增加LaserTrackingSensorConfig()接口
       | 8.增加LaserTrackingSensorSamplePeriod()接口
       | 9.增加LoadPosSensorDriver()接口
       | 10.增加UnLoadPosSensorDriver()接口
       | 11.增加LaserSensorRecord1()接口
       | 12.增加LaserSensorReplay()接口
       | 13.增加MoveLTR()接口
       | 14.增加LaserSensorRecordandReplay()接口
       | 15.增加MoveToLaserRecordStart()接口
       | 16.增加MoveToLaserRecordEnd()接口
       | 17.增加MoveToLaserSeamPos()接口
       | 18.增加GetLaserSeamPos()接口
       | 19.增加ImpedanceControlStartStop()接口
       | 20.增加GetToolCoordWithID()接口
       | 21.增加GetWObjCoordWithID()接口
       | 22.增加GetExToolCoordWithID()接口
       | 23.增加GetExAxisCoordWithID()接口
       | 24.增加GetTargetPayloadWithID()接口
       | 25.增加GetExAxisCoordWithID()接口
       | 26.增加GetCurWObjCoord()接口
       | 27.增加GetCurExToolCoord()接口
       | 28.增加GetCurExToolCoord()接口
       | 29.增加KernelUpgrade()接口
       | 30.增加GetKernelUpgradeResult()接口
       | 31.增加CustomWeaveSetPara()接口
       | 32.增加CustomWeaveGetPara()接口
       | 33.状态结构体增加工具、工件、外部工具、扩展轴坐标系和负载质量、质心数据

   * - V3.8.5
     - 2025-08-20
     - | 1.增加OpenLuaUpload()接口
       | 2.增加GetFieldBusConfig()接口
       | 3.增加FieldBusSlaveWriteDO()接口
       | 4.增加FieldBusSlaveWriteAO()接口
       | 5.增加FieldBusSlaveReadDI()接口
       | 6.增加FieldBusSlaveReadAI()接口
       | 7.增加FieldBusSlaveWaitDI()接口
       | 8.增加FieldBusSlaveWaitAI()接口
       | 9.增加SetSuckerCtrl()接口
       | 10.增加GetSuckerState()接口
       | 11.增加WaitSuckerState()接口
       | 12.增加MoveL()速度加速度参数模式velAccParamMode接口
       | 13.增加MoveL()重载函数1接口
       | 14.增加MoveL()重载函数2接口
       | 15.增加MoveC()速度加速度参数模式velAccParamMode接口
       | 16.增加MoveC()重载函数1接口
       | 17.增加Circle()速度加速度参数模式velAccParamMode接口
       | 18.增加Circle()重载函数1接口
       | 19.增加SetExAxisRobotPlan()接口

   * - V3.8.4
     - 2025-07-17
     - | 1.ExtAxisMove()接口增加blend平滑参数；
       | 2.增加SetFocusCalibPoint()接口
       | 3.增加ComputeFocusCalib()接口；
       | 4.增加FocusStart()接口；
       | 5.增加FocusEnd()接口
       | 6.增加SetFocusPosition()接口；
       | 7.增加SetEncoderUpgrade()接口；
       | 8.增加SetJointFirmwareUpgrade()接口
       | 9.增加SetCtrlFirmwareUpgrade()接口；
       | 10.增加SetEndFirmwareUpgrade()接口；
       | 11.增加JointAllParamUpgrade()接口；
       
   * - V3.8.3
     - 2025-06-24
     - | 1.Circle()接口增加加速度百分比及平滑半径参数；
       | 2.EndForceDragControl()接口增加辅助拖动时机器人碰撞检测标志参数；
       | 3.ServoJ()接口增加指令ID参数；
       | 4.增加SetSSHScpCmd()接口
       | 5.增加SetWideBoxTempFanMonitorParam()接口；
       | 6.增加GetWideBoxTempFanMonitorParam()接口；
       | 7.状态结构体增加控制箱温度和风扇电流状态数据；
              
   * - V3.8.2
     - 2025-06-13
     - | 1.WeaveSetPara()接口增加摆动方向侧倾角(绕摆动X轴偏转)参数
       | 2.WeaveChangeStart()接口增加摆动编号、焊接开始速度、焊接结束速度参数
       | 3.ExtDevSetUDPComParam()接口增加断电重启后是否自动建立连接参数
       | 4.SetCollisionDetectionMethod()接口增加碰撞等级阈值方式选择
       | 5.PtpFIRPlanningStart()接口增加统一关节急动度极值
       | 6.增加WeldingSetVoltageGradualChangeStart()接口
       | 7.增加WeldingSetVoltageGradualChangeEnd()接口
       | 8.增加WeldingSetCurrentGradualChangeStart()接口
       | 9.增加WeldingSetCurrentGradualChangeEnd()接口
       | 10.增加ArcWeldTraceAIChannelCurrent()接口
       | 11.增加ArcWeldTraceAIChannelVoltage()接口
       | 12.增加ArcWeldTraceCurrentPara()接口
       | 13.增加ArcWeldTraceVoltagePara()接口
       | 14.增加GetSmarttoolBtnState()接口
       | 15.增加ExtAxisGetCoord()接口
                     
   * - V3.8.1
     - 2025-04-24
     - | 1.ConveyorSetParam()接口增加跟踪运动类型、跟踪起始距离、跟踪终止距离参数
       | 2.增加AccSmoothStart()接口
       | 3.增加AccSmoothEnd()接口
       | 4.增加RbLogDownload()接口
       | 5.增加AllDataSourceDownload()接口
       | 6.增加DataPackageDownload()接口
       | 7.增加GetRobotSN()接口
       | 8.增加ShutDownRobotOS()接口
       | 9.增加ConveyorComDetect()接口
       | 10.增加ConveyorComDetectTrigger()接口
