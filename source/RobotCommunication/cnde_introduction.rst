CNDE简介
==================

协作机器人可配置网络数据交换协议（以下简称CNDE）是一种客户端通过UDP通讯进行机器人控制和获取机器人反馈状态的方式。

表1-1为CNDE可以获取到的机器人所有状态集合，客户端可以从表中任意挑选若干个需要的状态，并使机器人按照设定的反馈周期进行状态反馈。

同样，客户端也可以从表1-2中挑选需要的机器人控制功能组合进行机器人控制操作。客户端和机器人CNDE通信数据需按照指定的帧格式，机器人CNDE通讯端口为20005和20006，20005端口用于TCP通信，20006端口用于UDP通信。

使用机器人CNDE功能主要有以下四个步骤：

①输入、输出数据内容配置：客户端向机器人发送一条输入、输出配置指令，其中指令内容形如“std_DI_box,cfg_DI_box,motion_queue_len”等一系列控制或状态功能名称，机器人端记录并识别这些名称后向客户端反馈对应功能数据类型如“UINT8,UINT8,INT32”，即表示配置成功。

②启动机器人CNDE数据输出：客户端向机器人发送一条启动CNDE数据输出指令，机器人即开始按照配置的周期以字节数组(小端模式)的形式将机器人状态数据通过UDP发送至客户端。

③解析机器人状态数据：客户端循环接收机器人反馈的状态数据，并根据输出配置时机器人反馈的数据类型和表1-3中每个数据类型对应的字节长度进行数据解析，得到每个状态的实际数值。机器人CNDE输出数据最多支持4096个字节，可配置CNDE输出周期为1 ~ 200ms。

④发送机器人控制数据：客户端根据输入配置时机器人反馈的数据类型和表1-3中每个数据类型对应的字节长度进行控制数据组包，并通过UDP通讯发送到机器人，机器人端收到控制数据后进行数据解析和机器人控制操作。机器人CNDE输入支持256个配方，客户端可以根据需要先配置多个输入配方，在向机器人发送输入数据时需要指定当前数据对应的配方编号。

.. centered:: 表1-1 机器人输出配置功能

.. list-table::
   :widths: 20 40 80
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **名称**
     - **数据类型**
     - **描述**

   * - std_DI_box
     - UINT8
     - 控制箱标准DI输入(bit0 ~ bit7表示DI0 ~ DI7)

   * - cfg_DI_box
     - UINT8
     - 控制箱可配置CI输入(bit0 ~ bit7表示CI0 ~ CI7)

   * - cfg_DI_tool
     - UINT8
     - 控制箱可配置工具DI输入(bit0 ~ bit2表示toolDI0 ~ toolDI1)

   * - std_AI0_box
     - DOUBLE
     - 控制箱模拟量输入AI0(0 ~ 4095)

   * - std_AI1_box
     - DOUBLE
     - 控制箱模拟量输入AI1(0 ~ 4095)

   * - std_AI_tool
     - DOUBLE
     - 末端工具模拟量输入tool_AI0(0 ~ 4095)

   * - run_up_time
     - DOUBLE
     - 机器人开机时间统计(s)

   * - target_joint_pos
     - DOUBLE_6
     - 关节1-6目标位置(°)

   * - target_joint_vel
     - DOUBLE_6
     - 关节1-6目标速度(°/s)

   * - target_joint_acc
     - DOUBLE_6
     - 关节1-6目标加速度(°/s2)

   * - target_joint_current
     - DOUBLE_6
     - 关节1-6目标电流(A)

   * - target_joint_torque
     - DOUBLE_6
     - 关节1-6目标扭矩(Nm)

   * - actual_joint_pos
     - DOUBLE_6
     - 关节1-6当前位置(°)

   * - actual_joint_vel
     - DOUBLE_6
     - 关节1-6当前速度(°/s)

   * - actual_joint_current
     - DOUBLE_6
     - 关节1-6当前电流(A)

   * - actual_joint_torque
     - DOUBLE_6
     - 关节1-6目标扭矩(Nm)

   * - actual_TCP_pos
     - DOUBLE_6
     - 工具当前位置DKR(mm)

   * - actual_TCP_vel
     - DOUBLE_6
     - 工具当前速度DKR(mm/s)

   * - actual_TCP_force
     - DOUBLE_6
     - 工具合力DKR(N)

   * - target_TCP_pos
     - DOUBLE_6
     - 工具目标位置DKR(mm)

   * - target_TCP_vel
     - DOUBLE_6
     - 工具目标速度DKR(mm/s)

   * - std_DO_box
     - UINT8
     - 控制箱标准DO输出(bit0 ~ bit7表示DO0 ~ DO7)

   * - cfg_DO_box
     - UINT8
     - 控制箱可配置CO输出(bit0 ~ bit7表示CO0 ~ CO7)

   * - cfg_DO_tool
     - UINT8
     - 控制箱标准工具DO输出(bit0 ~ bit1表示toolDO0 ~ toolDO1)

   * - std_AO0_box
     - DOUBLE
     - 控制箱模拟量AO0 (0.0 ~ 4095.0)

   * - std_AO1_box
     - DOUBLE
     - 控制箱模拟量AO1 (0.0 ~ 4095.0)

   * - std_AO_tool
     - DOUBLE
     - 工具模拟量AO1 (0.0 ~ 4095.0)

   * - robot_mode
     - UINT8
     - 机器人模式(0-自动；1-手动)

   * - collision_level
     - UINT8_6
     - 关节1-6碰撞等级(1 ~ 10)

   * - speed_scaling_man
     - DOUBLE
     - 手动模式速度百分比(0 ~ 100)

   * - speed_scaling_auto
     - DOUBLE
     - 自动模式速度百分比(0 ~ 100)

   * - program_state
     - UINT8
     - 机器人程序运行状态(1-停止；2-运动中；3-暂停；4-拖动)

   * - line_number
     - INT32
     - 当前程序运行行号

   * - payload
     - DOUBLE
     - 负载质量(kg)

   * - pay_cog
     - DOUBLE_3
     - 负载质心(x,y,z)(mm)

   * - motion_queue_len
     - INT32
     - 当前运动队列长度
   
   * - ft_sensor_data
     - DOUBLE_6
     - 力传感器原始数据

   * - main_code
     - INT32
     - 主故障码

   * - sub_code
     - INT32
     - 子故障码

   * - emergency_stop
     - UINT8
     - 急停状态

   * - motion_done
     - INT32
     - 运动完成状态

   * - timestamp_us
     - UINT64
     - 机器人系统时间(us)

   * - output_BIT_reg_8xX
     - UINT8_X
     - BIT型机器人输出寄存器(8xX表示寄存器个数，若您需要16个BIT型输出寄存器，则实际名称为：“output_BIT_reg_8x2”，机器人最多支持128个BIT型输出寄存器)

   * - output_INT_reg_X
     - INT32_X
     - INT型机器人输出寄存器(X表示寄存器个数，若您需要16个INT型输出寄存器，则实际名称为：“output_INT_reg_16”，机器人最多支持64个INT型输出寄存器)

   * - output_DOUBLE_reg_X
     - DOUBLE_X
     - DOUBLE型机器人输出寄存器(X表示寄存器个数，若您需要16个DOUBLE型输出寄存器，则实际名称为：“output_DOUBLE_reg_16”，机器人最多支持64个DOUBLE型输出寄存器)

   * - servoj_time
     - UINT64_5
     - servoj时间戳数据,单位纳秒

   * - actual_joint_temp
     - DOUBLE_6
     - 关节j1-j6驱动器温度，单位°

   * - axle_gen_com_data
     - UINT8_130
     - 末端通用周期性数据

   * - abnormal_stop
     - UINT8
     - 异常状态，0：无异常，1：有异常

   * - cur_lua_file_name
     - UINT8_256
     - 当前运行lua文件名称

   * - prog_total_line
     - UINT8
     - 当前文件总行数

   * - safety_box_signal
     - UINT8_6
     - 按钮盒按键信号 0：按下  1：松开

   * - welding_voltage
     - DOUBLE
     - 实际焊接电压，单位V

   * - welding_current
     - DOUBLE
     - 实际焊接电流，单位A

   * - welding_track_speed
     - DOUBLE
     - 焊缝跟踪速度mm/s

   * - tpd_exception
     - UINT8
     - TPD异常

   * - alarm_reboot_robot
     - UINT8
     - 机器人重启警告

   * - modbus_master_connect
     - UINT8
     - | Modbus8个主站的连接状态  
       | bit0-bit7代表0-7个主站0-未连接，1-已连接

   * - modbus_slave_connect
     - UINT8
     - Modbus从站连接状态 0-未连接 1-已连接

   * - btn_box_stop_signal
     - UINT8
     - 急停按钮信号

   * - drag_alarm
     - UINT8
     - 拖动警告

   * - safety_door_alarm
     - UINT8
     - 安全门警告，0无警告，1安全门触发

   * - safety_plane_alarm
     - UINT8
     - 安全墙警告，0无警告，1进入安全墙

   * - motion_alarm
     - UINT8
     - | 运动警告，0-无警告，
       | 1-LIN指令姿态变化过大，  
       | 2-TCP超速，
       | 3-发生碰撞，  
       | 4-1轴超过最大速度，
       | 5-2轴超过最大速度，  
       | 6-3轴超过最大速度，
       | 7-4轴超过最大速度，  
       | 8-5轴超过最大速度，
       | 9-6轴超过最大速度，  
       | 10-1轴关节指令与反馈偏差过大，
       | 11-2轴关节指令与反馈偏差过大，  
       | 12-3轴关节指令与反馈偏差过大，
       | 13-4轴关节指令与反馈偏差过大，  
       | 14-5轴关节指令与反馈偏差过大，
       | 15-6轴关节指令与反馈偏差过大，  
       | 16-奇异位姿，
       | 17-LIN指令运动速度自适应，  
       | 18-目标速度调整超时或调速未完成，
       | 19-旋转插入运动失败，  
       | 20-螺旋插入运动失败，
       | 21-直线插入运动失败，  
       | 22-表面定位运动失败

   * - interfere_alarm
     - UINT8
     - 干涉区警告，0无警告，1进入干涉区

   * - udp_cmd_state
     - INT32
     - UDP连接状态

   * - weld_ready_state
     - UINT8
     - 焊机准备好状态，1：准备好，0：焊机错误

   * - alarm_check_emerg_stop_btn
     - UINT8
     - 关节通讯异常警告

   * - ts_tm_cmd_com_error
     - UINT8
     - 扭矩系统指令错误

   * - ts_tm_state_com_error
     - UINT8
     - 扭矩系统状态错误

   * - ctrl_box_error
     - INT32
     - 控制箱错误

   * - safety_data_state
     - UINT8
     - 安全数据状态标志，0无异常，1-异常

   * - force_sensor_err_state
     - UINT8
     - 力传感器连接超时故障；bit0-bit1对应力传感器ID1-ID2

   * - ctrl_open_lua_errcode
     - UINT8_4
     - 控制器开放协议错误码

   * - servo_id
     - UINT8
     - 伺服驱动器ID号

   * - servo_errcode
     - INT32
     - 伺服驱动器故障码

   * - servo_state
     - INT32
     - 伺服器驱动器状态

   * - servo_actual_pos
     - DOUBLE
     - 伺服当前位置

   * - servo_actual_speed
     - DOUBLE
     - 伺服当前速度
   
   * - servo_actual_torque
     - DOUBLE
     - 伺服当前转矩
   
   * - gripper_active
     - INT32
     - 夹爪激活状态
   
   * - gripper_position
     - UINT8
     - 夹爪位置反馈（百分比）
   
   * - gripper_speed
     - INT32
     - 夹爪速度反馈（百分比）
   
   * - gripper_current
     - INT32
     - 夹爪电流反馈（百分比）
   
   * - gripper_temp
     - INT32
     - 夹爪当前温度，单位°
   
   * - gripper_voltage
     - INT32
     - 夹爪当前电压，单位V
   
   * - rotating_gripper_num
     - DOUBLE
     - 旋转夹爪旋转圈数反馈
   
   * - rotating_gripper_speed
     - UINT8
     - 旋转夹爪旋转速度反馈（百分比）
   
   * - rotating_gripper_tor
     - UINT8
     - 旋转夹爪旋转力矩反馈（百分比）
   
   * - weld_break_off_state
     - UINT8
     - 焊接中断状态：0-焊接未中断   1-焊接中断
   
   * - weld_arc_state
     - UINT8
     - 焊接电弧状态 0-电弧未中断 1-电弧已中断
   
   * - smarttool_state
     - UINT32
     - 末端扩展IO数据(Smart-Tool)
   
   * - tool_coord
     - DOUBLE_6
     - 当前工具相对于末端位姿
   
   * - wobj_coord
     - DOUBLE_6
     - 当前工件相对于基座位姿
   
   * - exTool_coord
     - DOUBLE_6
     - 当前外部工具相对于工具位姿
   
   * - exAxis_coord
     - DOUBLE_6
     - 当前外部轴相对于基坐标系位姿
   
   * - robot_state
     - UINT8
     - | 机器人运行状态， 
       | 1.已经停止;2.正在运动;3.已经暂停;4.拖动
   
   * - actual_flange_pos
     - DOUBLE_6
     - 末端实际位姿
   
   * - target_TCP_cmpvel
     - DOUBLE_2
     - TCP指令线性、姿态速度，单位mm/s、°/s
   
   * - actual_TCP_cmpvel
     - DOUBLE_2
     - TCP实际线性、姿态速度，单位mm/s、°/s
   
   * - tool_id
     - INT32
     - 工具号
   
   * - wobj_id
     - INT32
     - 工件号
   
   * - ft_sensor_raw_data
     - DOUBLE_6
     - 末端力/力矩-传感器坐标系下原始数据
   
   * - ft_sensor_active
     - UINT8
     - 力/扭矩传感器激活状态
   
   * - gripper_motion_done
     - UINT8
     - 夹爪运动完成
   
   * - collision_state
     - UINT8
     - 碰撞检测状态
   
   * - trajectory_pnum
     - INT32
     - 离散点运动当前序号
   
   * - safety_stop0_state
     - UINT8
     - 安全停止SI0信号状态
   
   * - safety_stop1_state
     - UINT8
     - 安全停止SI1信号状态
   
   * - gripper_fault_id
     - UINT8
     - 错误夹爪号
   
   * - gripper_fault
     - INT32
     - 夹爪错误编号
   
   * - ext_DI_state
     - UINT8_16
     - 扩展DI
   
   * - ext_DO_state
     - UINT8_16
     - 扩展DO
   
   * - ext_AI_state
     - INT32_4
     - 扩展AI
   
   * - ext_AO_state
     - INT32_4
     - 扩展AO
   
   * - rbt_enable_state
     - INT32
     - 驱动器使能完成状态
   
   * - joint_driver_torque
     - DOUBLE_6
     - 关节j1-j6实际扭矩值，单位Nm
   
   * - robot_time
     - INT32_7
     - 机器人系统时间，年，月，日，时，分，秒，毫秒
   
   * - software_upgrade_state
     - INT32
     - 机器人软件升级状态
   
   * - end_lua_err_code
     - INT32
     - 末端按钮信号状态
   
   * - wide_voltage_ctrl_box_temp
     - DOUBLE
     - 宽电压控制箱温度，单位°
   
   * - wide_voltage_ctrl_box_fan_current
     - INT32
     - 宽电压控制箱风扇电流
   
   * - last_servoJ_target
     - DOUBLE_6
     - 最后一个servoJ目标指令位姿
   
   * - servoJ_cmd_num
     - INT32
     - servoJ指令计数
   
   * - strange_pos_flag
     - UINT8
     - 奇异位姿标志
   
   * - alarm
     - UINT8
     - | 警告，0-无警告，  
       | 1-肩关节配置变化，
       | 2-肘关节配置变化，  
       | 3-腕关节配置变化，
       | 4-RPY初始化失败，  
       | 5-WaitDI等待超时，
       | 6-WaitAI等待超时，  
       | 7-WaitToolDI等待超时，
       | 8-WaitToolAI等待超时，  
       | 9-起弧成功DI未配置，
       | 10-WaitAuxDI等待超时，  
       | 11-WaitAuxAI等待超时，
       | 12-摆动轨迹中存在不可到达点位，  
       | 13-传送带跟踪抓取点计算失败，
       | 14-关节扭矩传感器数据异常
   
   * - dr_alarm
     - UINT8
     - | 驱动器警告，0-无警告，
       | 1-1轴驱动器警告，可复位，  
       | 2-2轴驱动器警告，可复位，
       | 3-3轴驱动器警告，可复位，  
       | 4-4轴驱动器警告，可复位，
       | 5-5轴驱动器警告，可复位，  
       | 6-6轴驱动器警告，可复位
   
   * - alive_slave_num_error
     - UINT8
     - 活动从站数量故障，0-无故障，1-错误，不可复位
   
   * - slave_com_error
     - UINT8_8
     - | 从站通信故障，0-无故障，
       | 1-从站掉线，  
       | 2-从站状态与设置值不一致，
       | 3-从站未配置，  
       | 4-从站配置错误，
       | 5-从站初始化错误，  
       | 6-从站邮箱通信初始化错误
   
   * - cmd_point_error
     - UINT8
     - | 指令点故障，0-无故障，
       | 1-关节指令点错误，  
       | 2-直线目标点错误，
       | 3-圆弧中间点错误，  
       | 4-圆弧目标点错误，
       | 5-圆弧指令点间距过小，  
       | 6-整圆/螺旋线中间点1错误，
       | 7-整圆/螺旋线中间点2错误，  
       | 8-整圆/螺旋线中间点3错误，
       | 9-整圆/螺旋线指令点间距过小，  
       | 10-TPD指令点错误，
       | 11-TPD指令工具与当前工具不符，  
       | 12-TPD当前指令与下一指令起始点偏差过大，
       | 13-内外部工具切换错误，  
       | 14-新螺旋线起点错误，
       | 15-新样条曲线指令点错误，  
       | 17-PTP关节指令超限，
       | 18-TPD关节指令超限，  
       | 19-LIN\ARC下发关节指令超限，
       | 20-笛卡尔空间内指令超速，  
       | 21-关节空间内扭矩指令超限，
       | 22-JOG关节指令超限，  
       | 23-轴1关节空间内指令速度超限，
       | 24-轴2关节空间内指令速度超限，  
       | 25-轴3关节空间内指令速度超限，
       | 26-轴4关节空间内指令速度超限，  
       | 27-轴5关节空间内指令速度超限，
       | 28-轴6关节空间内指令速度超限，  
       | 29-关节反馈速度超限，
       | 30-关节指令与反馈偏差过大，  
       | 31-DMP目标点错误（包括工具不符），
       | 32-TCP速度超限，  
       | 33-下一指令关节配置发生变化，
       | 34-当前指令关节配置发生变化，  
       | 35-LIN指令中关节速度超限，
       | 36-LIN指令自适应速度超出阈值，  
       | 37-轨迹中存在不可到达点位，
       | 38-轨迹中存在不可到达点位-奇异位姿，  
       | 49-ARCSTART和ARCEND之间不允许PTP和SPTP指令，
       | 50-WEAVESTART和WEAVEEND之间不允许PTP和SPTP指令，  
       | 51-摆焊参数错误，
       | 52-摆焊指令点间距过小，  
       | 53-摆动轨迹中存在不可到达点位-奇异位姿，
       | 54-摆动轨迹中存在不可到达点位-关节指令超限，
       | 55-摆动轨迹中存在不可到达点位-规划异常（工具Z与前进方向X夹角重合），
       | 56-摆动轨迹中存在不可到达点位-规划异常（圆弧路点错误），
       | 65-激光传感器指令偏差过大，  
       | 66-激光传感器指令中断，焊缝跟踪提前结束，
       | 81-外部轴指令速度超限，  
       | 82-外部轴指令与反馈偏差过大，
       | 83-扩展外设(外部轴/IO)通信中断，  
       | 84-扩展外设(外部轴/IO)通信丢包异常，
       | 85-外部轴1关节空间内指令速度超限，  
       | 86-外部轴2关节空间内指令速度超限，
       | 87-外部轴3关节空间内指令速度超限，  
       | 88-外部轴4关节空间内指令速度超限，
       | 89-扩展外设(外部轴/IO)Ethercat通信错误，  
       | 90-扩展外设(外部轴/IO)Canopen通信错误，
       | 97-传送带跟踪-起始点与参考点姿态变化过大，  
       | 113-恒力控制-X方向超过最大调整距离，
       | 114-恒力控制-Y方向超过最大调整距离，  
       | 115-恒力控制-Z方向超过最大调整距离，
       | 116-恒力控制-RX方向超过最大调整角度，  
       | 117-恒力控制-RY方向超过最大调整角度，
       | 118-恒力控制-RZ方向超过最大调整角度，  
       | 119-外部传感器数据错误，
       | 120-螺旋线探索运动失败，  
       | 121-旋转插入运动失败，
       | 122-直线插入运动失败，  
       | 123-表面定位运动失败，
       | 124-拖动力异常，进入拖动失败，  
       | 129-超过最大扭矩记录点数，
       | 130-速度切换错误，  
       | 131-工具方向超限，  
       | 132-动量超限，
       | 133-功率超限，  
       | 134-STL-Flash诊断异常，  
       | 135-STL-RAM诊断异常，
       | 136-STL-CPU诊断异常，  
       | 137-安全板II-ECAT安全数据异常，
       | 138-1轴ECAT安全数据异常，  
       | 139-2轴ECAT安全数据异常，
       | 140-3轴ECAT安全数据异常，  
       | 141-4轴ECAT安全数据异常，
       | 142-5轴ECAT安全数据异常，  
       | 143-6轴ECAT安全数据异常，
       | 145-安全板与控制器通讯异常，  
       | 147-焦点跟随错误，
       | 148-姿态速度超限，  
       | 149-关节状态字反馈异常
   
   * - IO_error
     - UINT8
     - | IO故障，0-无故障，
       | 1-通道错误，可复位，  
       | 2-数值错误，可复位，
       | 3-WaitDI等待超时，可复位，  
       | 4-WaitAI等待超时，可复位，
       | 5-WaitAxleDI等待超时，可复位，  
       | 6-WaitAxleAI等待超时，可复位，
       | 7-通道已配置功能错误，可复位，  
       | 8-起弧超时，可复位，
       | 9-收弧超时，可复位，  
       | 10-寻位超时，可复位，
       | 11-传送带IO检测超时，可复位，  
       | 12-WaitAuxDI等待超时，可复位，
       | 13-WaitAuxAI等待超时，可复位，  
       | 14-焊丝寻位超时，可复位
   
   * - gripper_error
     - UINT8
     - 夹爪故障，0-无故障，1-夹爪运动超时错误，可复位
   
   * - file_error
     - UINT8
     - | 配置文件故障，0-无故障，
       | 1-zbt配置文件版本错误，初始化错误-不可复位，
       | 2-zbt配置文件加载失败，初始化错误-不可复位，
       | 3-user配置文件版本错误，初始化错误-不可复位，
       | 4-user配置文件加载失败，初始化错误-不可复位，
       | 5-exaxis配置文件版本错误，初始化错误-不可复位，
       | 6-exaxis配置文件加载失败，初始化错误-不可复位，
       | 7-机器人型号不一致，需要重新设置-不可复位，
       | 8-dhpara配置文件版本错误，初始化错误-不可复位，
       | 9-dhpara配置文件加载失败，初始化错误-不可复位，
       | 10-机器人型号未设置-不可复位，
       | 11-load配置文件版本错误，初始化错误-不可复位，
       | 12-load配置文件加载失败，初始化错误-不可复位，
       | 13-speed配置文件版本错误，初始化错误-不可复位，
       | 14-speed配置文件加载失败，初始化错误-不可复位，
       | 15-weavepara配置文件版本错误，初始化错误-不可复位，
       | 16-weavepara配置文件加载失败，初始化错误-不可复位
   
   * - para_error
     - UINT8
     - | 配置参数故障，0-无故障，
       | 1-工具号超限错误-可复位，  
       | 2-定位完成阈值错误-可复位，
       | 3-碰撞等级错误-可复位，  
       | 4-负载重量错误-可复位，
       | 5-负载质心X错误-可复位，  
       | 6-负载质心Y错误-可复位，
       | 7-负载质心Z错误-可复位，  
       | 8-DI滤波时间错误-可复位，
       | 9-AxleDI滤波时间错误-可复位，  
       | 10-AI滤波时间错误-可复位，
       | 11-AxleAI滤波时间错误-可复位，  
       | 12-DI高低电平范围错误-可复位，
       | 13-DO高低电平范围错误-可复位，  
       | 14-工件号超限错误-可复位，
       | 15-外部轴号超限错误-可复位，  
       | 16-传送带跟踪-编码器通道错误-可复位，
       | 17-传送带跟踪-工件轴号错误-可复位，  
       | 18-FR30L安装方式-非正装错误-可复位
   
   * - exaxis_out_slimit_error
     - UINT8
     - | 外部轴软限位故障，0-无故障，
       | 1-外部轴1轴超出软限位故障，可复位，  
       | 2-外部轴2轴超出软限位故障，可复位，
       | 3-外部轴3轴超出软限位故障，可复位，  
       | 4-外部轴4轴超出软限位故障，可复位，
       | 5-外部轴5轴超出软限位故障，可复位，  
       | 6-外部轴6轴超出软限位故障，可复位
   
   * - dr_com_err
     - UINT8_6
     - 驱动器通信故障，0-无故障，1-故障
   
   * - dr_err
     - UINT8
     - | 驱动器故障，0-无故障，
       | 1-1轴驱动器故障，不可复位，  
       | 2-2轴驱动器故障，不可复位，
       | 3-3轴驱动器故障，不可复位，  
       | 4-4轴驱动器故障，不可复位，
       | 5-5轴驱动器故障，不可复位，  
       | 6-6轴驱动器故障，不可复位
   
   * - out_sflimit_err
     - UINT8
     - | 软限位故障，0-无故障，
       | 1-1轴超出软限位故障，可复位，  
       | 2-2轴超出软限位故障，可复位，
       | 3-3轴超出软限位故障，可复位，  
       | 4-4轴超出软限位故障，可复位，
       | 5-5轴超出软限位故障，可复位，  
       | 6-6轴超出软限位故障，可复位

.. centered:: 表1-2 机器人输入控制配置功能

.. list-table::
   :widths: 20 40 80
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **名称**
     - **数据类型**
     - **描述**

   * - speed_mask
     - UINT8
     - 全局速度设置掩码：0-不生效；1-生效

   * - speed
     - UINT8
     - 设置全局速度（0-100）

   * - std_DO_mask
     - UINT8
     - 控制箱标准DO输出控制掩码(bit0 ~ bit7表示DO0 ~ DO7)

   * - std_DO_box
     - UINT8
     - 控制箱标准DO输出(bit0 ~ bit7表示DO0 ~ DO7)

   * - cfg_DO_mask
     - UINT8
     - 控制箱可配置CO输出控制掩码(bit0 ~ bit7表示CO0 ~ CO7)

   * - cfg_DO_box
     - UINT8
     - 控制箱可配置CO输出(bit0 ~ bit7表示CO0 ~ CO7)

   * - cfg_DO_tool_mask
     - UINT8
     - 控制箱标准工具DO输出控制掩码(bit0 ~ bit1表示toolDO0 ~ toolDO1)

   * - cfg_DO_tool
     - UINT8
     - 控制箱标准工具DO输出(bit0 ~ bit1表示toolDO0 ~ toolDO1)

   * - std_AO_mask
     - UINT8
     - 机器人模拟量输出控制掩码(bit0 ~ bit1表示控制箱AO0 ~ AO1；bit2表示工具AO0)

   * - std_AO0_box
     - DOUBLE
     - 控制箱模拟量AO0 (0.0 ~ 4095.0)

   * - std_AO1_box
     - DOUBLE
     - 控制箱模拟量AO1 (0.0 ~ 4095.0)

   * - std_AO0_tool
     - DOUBLE
     - 工具模拟量AO1 (0.0 ~ 4095.0)

   * - input_BIT_reg_8xX
     - UINT8_X
     - BIT型机器人输入寄存器(8xX表示寄存器个数，若您需要16个BIT型输入寄存器，则实际名称为：“input_BIT_reg_8x2”，机器人最多支持128个BIT型寄存器)

   * - input_INT_reg_X
     - INT32_X
     - INT型机器人输入寄存器(X表示寄存器个数，若您需要16个INT型输入寄存器，则实际名称为：“input_INT_reg_16”，机器人最多支持64个INT型寄存器)
  
   * - input_DOUBLE_reg_X
     - DOUBLE_X
     - DOUBLE型机器人输入寄存器(X表示寄存器个数，若您需要16个DOUBLE型输入寄存器，则实际名称为：“input_DOUBLE_reg_16”，机器人最多支持64个DOUBLE型寄存器)

.. centered:: 表1-3 数据类型及字节长度对应关系

.. list-table::
   :widths: 60 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **数据类型**
     - **字节长度**

   * - UINT8
     - 1

   * - INT32
     - 4

   * - DOUBLE
     - 8

   * - UINT8_X
     - 1*X

   * - INT32_X
     - 4*X

   * - DOUBLE_X
     - 8*X