机器人状态查询
===============

.. toctree:: 
    :maxdepth: 5

获取当前关节位置(角度)
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualJointPosDegree(flag=1)``"
    "描述", "获取关节当前位置(角度)"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞，默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``joint_pos=[j1,j2,j3,j4,j5,j6]``：当前关节位置(角度)"

获取当前关节位置(弧度)
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualJointPosRadian(flag=1)``"
    "描述", "获取关节当前位置(弧度)"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞 默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``joint_pos=[j1,j2,j3,j4,j5,j6]``：当前关节位置(弧度)"

获取关节反馈速度-deg/s
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualJointSpeedsDegree(flag=1)``"
    "描述", "获取关节反馈速度-deg/s"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞 默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``speed=[j1,j2,j3,j4,j5,j6]``：关节反馈速度-deg/s"

获取关节反馈加速度-deg/s^2
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualJointAccDegree(flag=1)``"
    "描述", "获取关节反馈加速度-deg/s^2"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞 默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``acc=[j1,j2,j3,j4,j5,j6]``：关节反馈加速度-deg/s^2"

获取TCP指令合速度
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTargetTCPCompositeSpeed(flag=1)``"
    "描述", "获取TCP指令合速度"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞 默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``[tcp_speed,ori_speed]``：tcp_speed-线性合速度 ori_speed-姿态合速度"

获取TCP反馈合速度
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualTCPCompositeSpeed(flag=1)``"
    "描述", "获取TCP反馈合速度"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞 默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``[tcp_speed,ori_speed]``：tcp_speed-线性合速度 ori_speed-姿态合速度"

获取TCP指令速度
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTargetTCPSpeed(flag=1)``"
    "描述", "获取TCP指令速度"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞 默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``speed=[x,y,z,rx,ry,rz]``：TCP指令速度，mm/s"

获取TCP反馈速度
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualTCPSpeed(flag=1)``"
    "描述", "获取TCP反馈速度"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞 默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``speed=[x,y,z,rx,ry,rz]``：TCP反馈速度"

获取当前工具位姿
++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualTCPPose(flag=1)``"
    "描述", "获取当前工具位姿"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞 默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``tcp_pose=[x,y,z,rx,ry,rz]``：当前工具位姿"

获取当前工具坐标系编号
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualTCPNum(flag=1)``"
    "描述", "获取当前工具坐标系编号"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞 默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``tool_id``:工具坐标系编号"

获取当前工件坐标系编号
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualWObjNum(flag=1)``"
    "描述", "获取当前工件坐标系编号"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞  默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``wobj_id``:工件坐标系编号"

获取当前末端法兰位姿
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualToolFlangePose(flag=1)``"
    "描述", "获取当前末端法兰位姿"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞  默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``flange_pose=[x,y,z,rx,ry,rz]``：当前末端法兰位姿"

获取当前关节转矩
+++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetJointTorques(flag=1)``"
    "描述", "获取当前关节转矩"
    "必选参数", "无"
    "默认参数", "``flag``：0-阻塞，1-非阻塞  默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``torques=[j1,j2,j3,j4,j5,j6]``：关节扭矩"

获取系统时间
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSystemClock()``"
    "描述", "获取系统时间"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``t_ms``: 系统时间，单位 [ms]"

查询机器人运动是否完成
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotMotionDone()``"
    "描述", "查询机器人运动是否完成"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``state``: 机器人运动状态，0-未完成，1-完成"

查询机器人运动队列缓存长度
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetMotionQueueLength()``"
    "描述", "查询机器人运动队列缓存长度"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``len``：缓存长度"

获取机器人急停状态
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotEmergencyStopState()``"
    "描述", "获取机器人急停状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``state``：急停状态，0-非急停，1-急停"

获取SDK与机器人的通讯状态
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSDKComState()``"
    "描述", "获取SDK与机器人的通讯状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``state``：通讯状态，0-通讯正常，1-通讯异常"

获取安全停止信号
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSafetyStopState()``"
    "描述", "获取安全停止信号"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``[si0_state,si1_state]``：si0_state 安全停止信号SI0，0-无效，1-有效 si1_state 安全停止信号SI1，0-无效，1-有效"

获取关节驱动器当前温度(℃)
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetJointDriverTemperature()``"
    "描述", "获取关节驱动器当前温度(℃)"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``data=[t1,t2,t3,t4,t5,t6]``：各关节当前温度"

获取关节驱动器当前扭矩(Nm)
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetJointDriverTorque()``"
    "描述", "获取关节驱动器当前扭矩(Nm)"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``data=[j1,j2,j3,j4,j5,j6]``：关节扭矩 [fx,fy,fz,tx,ty,tz]"

获取机器人状态
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotRealTimeState()``"
    "描述", "获取机器人状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``robot_state_pkg``：机器人状态结构体"

机器人状态查询代码示例
++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    error,[yangle, zangle] = robot.GetRobotInstallAngle()
    print(f"yangle:{yangle},zangle:{zangle}")
    error,j_deg = robot.GetActualJointPosDegree(0)
    print(f"joint pos deg:{j_deg[0]},{j_deg[1]},{j_deg[2]},{j_deg[3]},{j_deg[4]},{j_deg[5]}")
    error,jointSpeed = robot.GetActualJointSpeedsDegree(0)
    print(f"joint speeds deg:{jointSpeed[0]},{jointSpeed[1]},{jointSpeed[2]},{jointSpeed[3]},{jointSpeed[4]},{jointSpeed[5]}")
    error,jointAcc = robot.GetActualJointAccDegree(0)
    print(f"joint acc deg:{jointAcc[0]},{jointAcc[1]},{jointAcc[2]},{jointAcc[3]},{jointAcc[4]},{jointAcc[5]}")
    error,[tcp_speed, ori_speed] = robot.GetTargetTCPCompositeSpeed(0)
    print(f"GetTargetTCPCompositeSpeed tcp {tcp_speed}; ori {ori_speed}")
    error,[tcp_speed, ori_speed] = robot.GetActualTCPCompositeSpeed(0)
    print(f"GetActualTCPCompositeSpeed tcp {tcp_speed}; ori {ori_speed}")
    error,targetSpeed = robot.GetTargetTCPSpeed(0)
    print(f"GetTargetTCPSpeed {targetSpeed[0]},{targetSpeed[1]},{targetSpeed[2]},{targetSpeed[3]},{targetSpeed[4]},{targetSpeed[5]}")
    error,actualSpeed = robot.GetActualTCPSpeed(0)
    print(f"GetActualTCPSpeed {actualSpeed[0]},{actualSpeed[1]},{actualSpeed[2]},{actualSpeed[3]},{actualSpeed[4]},{actualSpeed[5]}")
    error,tcp = robot.GetActualTCPPose(0)
    print(f"tcp pose:{tcp[0]},{tcp[1]},{tcp[2]},{tcp[3]},{tcp[4]},{tcp[5]}")
    error,flange = robot.GetActualToolFlangePose(0)
    print(f"flange pose:{flange[0]},{flange[1]},{flange[2]},{flange[3]},{flange[4]},{flange[5]}")
    error,id = robot.GetActualTCPNum(0)
    print(f"tcp num:{id}")
    error,id = robot.GetActualWObjNum(0)
    print(f"wobj num:{id}")
    error,jtorque = robot.GetJointTorques(0)
    print(f"torques:{jtorque[0]},{jtorque[1]},{jtorque[2]},{jtorque[3]},{jtorque[4]},{jtorque[5]}")
    error,t_ms = robot.GetSystemClock()
    print(f"system clock:{t_ms}")
    error,config = robot.GetRobotCurJointsConfig()
    print(f"joint config:{config}")
    error,motionDone = robot.GetRobotMotionDone()
    print(f"GetRobotMotionDone:{motionDone}")
    error,len = robot.GetMotionQueueLength()
    print(f"GetMotionQueueLength:{len}")
    error,emergState = robot.GetRobotEmergencyStopState()
    print(f"GetRobotEmergencyStopState:{emergState}")
    error,comstate = robot.GetSDKComState()
    print(f"GetSDKComState:{comstate}")
    error,[si0_state, si1_state] = robot.GetSafetyStopState()
    print(f"GetSafetyStopState:{si0_state} {si1_state}")
    error,temp = robot.GetJointDriverTemperature()
    print(f"Temperature:{temp[0]},{temp[1]},{temp[2]},{temp[3]},{temp[4]},{temp[5]}")
    error,torque = robot.GetJointDriverTorque()
    print(f"torque:{torque[0]},{torque[1]},{torque[2]},{torque[3]},{torque[4]},{torque[5]}")
    error,pkg = robot.GetRobotRealTimeState()
    robot.CloseRPC()

逆运动学求解
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetInverseKin(type,desc_pos,config=-1)``"
    "描述", "逆运动学，笛卡尔位姿求解关节位置 "
    "必选参数", "- ``type``:0-绝对位姿(基坐标系)，1-相对位姿（基坐标系），2-相对位姿（工具坐标系）
    - ``desc_pose``:[x,y,z,rx,ry,rz],工具位姿，单位[mm][°]"
    "默认参数", "- ``config``:关节配置，[-1]-参考当前关节位置求解，[0~7]-依据关节配置求解 默认-1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``joint_pos=[j1,j2,j3,j4,j5,j6]``：逆运动学解，笛卡尔位姿求解关节位置"

逆运动学求解-指定参考位置
++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetInverseKinRef(type,desc_pos,joint_pos_ref)``"
    "描述", "逆运动学，工具位姿求解关节位置，参考指定关节位置求解"
    "必选参数", "- ``type``:0-绝对位姿(基坐标系)，1-相对位姿（基坐标系），2-相对位姿（工具坐标系）
    - ``desc_pos``：[x,y,z,rx,ry,rz]工具位姿，单位[mm][°]
    - ``joint_pos_ref``：[j1,j2,j3,j4,j5,j6]，关节参考位置，单位[°]"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``joint_pos=[j1,j2,j3,j4,j5,j6]``：逆运动学解，工具位姿求解关节位置"

逆运动学求解-是否有解
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetInverseKinHasSolution(type,desc_pos,joint_pos_ref)``"
    "描述", "逆运动学，工具位姿求解关节位置 是否有解"
    "必选参数", "- ``type``:0-绝对位姿(基坐标系)，1-相对位姿（基坐标系），2-相对位姿（工具坐标系）
    - ``desc_pos``：[x,y,z,rx,ry,rz]工具位姿，单位[mm][°]
    - ``joint_pos_ref``：[j1,j2,j3,j4,j5,j6]，关节参考位置，单位[°]"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``result``:“True”-有解，“False”-无解"

正运动学求解
+++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetForwardKin(joint_pos)``"
    "描述", "正运动学，关节位置求解工具位姿"
    "必选参数", "- ``joint_pos``:[j1,j2,j3,j4,j5,j6]:关节位置，单位[°]"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``desc_pos=[x,y,z,rx,ry,rz]``：正运动学解，关节位置求解工具位姿"

机器人正逆运动学计算代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    j1 = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    desc_pos1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    error, inverseRtn = robot.GetInverseKin(0, desc_pos=desc_pos1, config=-1)
    print(f"dcs1 GetInverseKin rtn is {inverseRtn[0]}, {inverseRtn[1]}, {inverseRtn[2]}, "
          f"{inverseRtn[3]}, {inverseRtn[4]}, {inverseRtn[5]}")
    error, inverseRtn = robot.GetInverseKinRef(0, desc_pos=desc_pos1, joint_pos_ref=j1)
    print(f"dcs1 GetInverseKinRef rtn is {inverseRtn[0]}, {inverseRtn[1]}, {inverseRtn[2]}, "
          f"{inverseRtn[3]}, {inverseRtn[4]}, {inverseRtn[5]}")
    error, hasResult = robot.GetInverseKinHasSolution(0, desc_pos=desc_pos1, joint_pos_ref=j1)
    print(f"dcs1 GetInverseKinRef result {hasResult}")
    error, forwordResult = robot.GetForwardKin(j1)
    print(f"jpos1 forwordResult rtn is {forwordResult[0]}, {forwordResult[1]}, {forwordResult[2]}, "
          f"{forwordResult[3]}, {forwordResult[4]}, {forwordResult[5]}")
    robot.CloseRPC()

查询机器人示教管理点位数据
++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotTeachingPoint(name)``"
    "描述", "查询机器人示教管理点位数据"
    "必选参数", "``name``：点位名"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``[x,y,z,rx,ry,rz,j1,j2,j3,j4,j5,j6,tool,wobj,speed,acc,e1,e2,e3,e4]``：点位数据"

获取DH补偿参数
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDHCompensation()``"
    "描述", "获取DH补偿参数"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``dhCompensation=[cmpstD1,cmpstA2,cmpstA3,cmpstD4,cmpstD5,cmpstD6]``：机器人DH参数补偿值(mm)"

获取控制箱SN码
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotSN()``"
    "描述", "获取控制箱SN码"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``SNCode``：控制箱SN码"

查询机器人示教管理点位数据代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    name = "P1"
    rtn, data = robot.GetRobotTeachingPoint(name)
    print(f"{rtn} name is: {name}")
    for i in range(20):
        print(f"data is: {data[i]}")
    rtn,que_len = robot.GetMotionQueueLength()
    print(f"GetMotionQueueLength rtn is: {rtn}, queue length is: {que_len}")
    retval,dh = robot.GetDHCompensation()
    print(f"retval is: {retval}")
    print(f"dh is: {dh[0]} {dh[1]} {dh[2]} {dh[3]} {dh[4]} {dh[5]}")
    error,sn = robot.GetRobotSN()
    print(f"robot SN is {sn[0]}")
    robot.CloseRPC()
