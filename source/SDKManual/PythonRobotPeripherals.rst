机器人外设
============

.. toctree:: 
    :maxdepth: 5

配置夹爪
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetGripperConfig(company,device,softversion=0,bus=0)``"
    "描述", "配置夹爪"
    "必选参数", "- ``company``：夹爪厂商，1-Robotiq，2-慧灵，3-天机，4-大寰，5-知行；
    - ``device``：设备号，Robotiq(0-2F-85系列)，慧灵(0-NK系列,1-Z-EFG-100)，天机(0-TEG-110)，大寰(0-PGI-140)，知行(0-CTPM2F20)"
    "默认参数", "- ``softversion``：软件版本号，暂不使用，默认为0；
    - ``bus``：设备挂载末端总线位置，暂不使用，默认为0；"
    "返回值", "错误码 成功-0  失败- errcode "

获取夹爪配置
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperConfig()``"
    "描述", "获取夹爪配置"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``[number,company,device,softversion]``： number，夹爪编号;company，夹爪厂商，1-Robotiq，2-慧灵，3-天机，4-大寰，5-知行 ;device，设备号，Robotiq(0-2F-85系列)，慧灵(0-NK系列,1-Z-EFG-100)，天机(0-TEG-110)，大寰(0-PGI-140)，知行(0-CTPM2F20);softvesion，软件版本号，暂不使用，默认为0。"

激活夹爪
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ActGripper(index,action)``"
    "描述", "激活夹爪"
    "必选参数", "- ``index``:夹爪编号；
    - ``action``:0-复位，1-激活"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

控制夹爪
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveGripper(index,pos,vel,force,maxtime,block,type,rotNum,rotVel,rotTorque)``"
    "描述", "控制夹爪"
    "必选参数", "- ``index``:夹爪编号；
    - ``pos``:位置百分比，范围[0~100]；
    - ``vel``:速度百分比，范围[0~100];
    - ``force``:力矩百分比，范围[0~100]；
    - ``maxtime``:最大等待时间，范围[0~30000]，单位[ms]；
    - ``block``:0-阻塞，1-非阻塞；
    - ``type``:夹爪类型，0-平行夹爪；1-旋转夹爪；
    - ``rotNum``:rotNum 旋转圈数；
    - ``rotVel``:旋转速度百分比[0-100]；
    - ``rotTorque``:旋转力矩百分比[0-100]。"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

获取夹爪运动状态
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperMotionDone()``"
    "描述", "获取夹爪运动状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``[fault,status]``：夹爪运动状态，fault:0-无错误，1-有错误；status:0-运动未完成，1-运动完成"

获取夹爪激活状态
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperActivateStatus()``"
    "描述", "获取夹爪激活状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``fault``：0-无错误，1-有错误
    - ``gripper_active``：bit0~bit15对应夹爪编号0~15，bit=0为未激活，bit=1为激活"

获取夹爪位置
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperCurPosition()``"
    "描述", "获取夹爪位置"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``fault``：0-无错误，1-有错误
    - ``position``：位置百分比，范围0~100%"

获取夹爪速度
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperCurSpeed()``"
    "描述", "获取夹爪速度"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``fault``：0-无错误，1-有错误
    - ``speed``：速度百分比，范围0~100%"

获取夹爪电流
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperCurCurrent()``"
    "描述", "获取夹爪电流"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``fault``：0-无错误，1-有错误
    - ``current``：电流百分比，范围0~100%"

获取夹爪电压
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperVoltage()``"
    "描述", "获取夹爪电压"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``fault``：0-无错误，1-有错误
    - ``voltage``：电压,单位0.1V"

获取夹爪温度
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperTemp()``"
    "描述", "获取夹爪温度"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``fault``：0-无错误，1-有错误
    - ``temp``：温度，单位℃"

计算预抓取点-视觉
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputePrePick(desc_pos, zlength, zangle)``"
    "描述", "计算预抓取点-视觉"
    "必选参数", "- ``desc_pos``：夹抓取点笛卡尔位姿;
    - ``zlength``：z轴偏移量;
    - ``zangle``：绕z轴旋转偏移量"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``pre_pos``：预抓取点笛卡尔位姿"

计算撤退点-视觉
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputePostPick(desc_pos, zlength, zangle)``"
    "描述", "计算撤退点-视觉"
    "必选参数", "- ``desc_pos``：抓取点笛卡尔位姿;
    - ``zlength``：z轴偏移量;
    - ``zangle``：绕z轴旋转偏移量"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``post_pos``：撤退点笛卡尔位姿"

机器人夹爪操作代码示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    company = 4
    device = 0
    softversion = 0
    bus = 2
    index = 2
    act = 0
    max_time = 30000
    block = 0
    status = 0
    fault = 0
    active_status = 0
    current_pos = 0
    current = 0
    voltage = 0
    temp = 0
    speed = 0
    robot.SetGripperConfig(company, device, softversion, bus)
    time.sleep(1)
    error,[company, device, softversion, bus] = robot.GetGripperConfig()
    print(f"gripper config:{company},{device},{softversion},{bus}")
    robot.ActGripper(index, act)
    time.sleep(1)
    act = 1
    robot.ActGripper(index, act)
    time.sleep(1)
    error = robot.MoveGripper(index, 90, 50, 50, max_time, block, 0, 0, 0, 0)
    print(f"MoveGripper retval is:{error}")
    time.sleep(1)
    error = robot.MoveGripper(index, 30, 50, 0, max_time, block, 0, 0, 0, 0)
    print(f"MoveGripper retval is:{error}")
    error, [fault, status] = robot.GetGripperMotionDone()
    print(f"motion status:{fault},{status}")
    error, [fault, active_status] = robot.GetGripperActivateStatus()
    print(f"gripper active fault is:{fault},status is:{active_status}")
    error, [fault, current_pos] = robot.GetGripperCurPosition()
    print(f"fault is:{fault},current position is:{current_pos}")
    error, [fault, current] = robot.GetGripperCurCurrent()
    print(f"fault is:{fault},current current is:{current}")
    error, [fault, voltage] = robot.GetGripperVoltage()
    print(f"fault is:{fault},current voltage is:{voltage}")
    error, [fault, temp] = robot.GetGripperTemp()
    print(f"fault is:{fault},current temperature is:{temp}")
    error, [fault, speed] = robot.GetGripperCurSpeed()
    print(f"fault is:{fault},current speed is:{speed}")
    retval = 0
    prepick_pose = [0.0]*6
    postpick_pose = [0.0]*6
    p1Desc = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    p2Desc = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    retval, prepick_pose = robot.ComputePrePick(p1Desc, 10, 0)
    print(f"ComputePrePick retval is:{retval}")
    print(f"xyz is:{prepick_pose[0]},{prepick_pose[1]},{prepick_pose[2]};rpy is:{prepick_pose[3]},{prepick_pose[4]},{prepick_pose[5]}")
    retval, postpick_pose = robot.ComputePostPick(p2Desc, -10, 0)
    print(f"ComputePostPick retval is:{retval}")
    print(f"xyz is:{postpick_pose[0]},{postpick_pose[1]},{postpick_pose[2]};rpy is:{postpick_pose[3]},{postpick_pose[4]},{postpick_pose[5]}")
    robot.CloseRPC()

获取旋转夹爪的旋转圈数
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperRotNum()``"
    "描述", "获取旋转夹爪的旋转圈数"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``fault``：0-无错误，1-有错误
    - ``num``：旋转圈数"

获取旋转夹爪的旋转速度百分比
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperRotSpeed()``"
    "描述", "获取旋转夹爪的旋转速度百分比"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``fault``：0-无错误，1-有错误
    - ``speed``：旋转速度百分比"

获取旋转夹爪的旋转力矩百分比
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperRotTorque()``"
    "描述", "获取旋转夹爪的旋转力矩百分比"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``fault``：0-无错误，1-有错误
    - ``torque``：旋转力矩百分比"

获取旋转夹爪状态代码示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    fault = 0
    rotNum = 0.0
    rotSpeed = 0
    rotTorque = 0
    error,fault, rotNum = robot.GetGripperRotNum()
    error,fault, rotSpeed = robot.GetGripperRotSpeed()
    error,fault, rotTorque = robot.GetGripperRotTorque()
    print(f"gripper rot num:{rotNum},gripper rotSpeed:{rotSpeed},gripper rotTorque:{rotTorque}")
    robot.CloseRPC()

传动带启动、停止
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorStartEnd(status)``"
    "描述", "传动带启动、停止"
    "必选参数", "- ``status``： 传动带状态，1-启动，0-停止"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

记录IO检测点
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorPointIORecord()``"
    "描述", "记录IO检测点"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

记录A点
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorPointARecord()``"
    "描述", "记录A点"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

记录参考点
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorRefPointRecord()``"
    "描述", "记录参考点"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

记录B点
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorPointBRecord()``"
    "描述", "记录B点"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

传送带工件IO检测
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorIODetect(max_t)``"
    "描述", "传送带工件IO检测"
    "必选参数", "- ``max_t``： 最大检测时间，单位ms"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取物体当前位置
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorGetTrackData(mode)``"
    "描述", "获取物体当前位置"
    "必选参数", "- ``mode``： 1-跟踪抓取 2-跟踪运动 3-TPD跟踪"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

传动带跟踪开始
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorTrackStart(status)``"
    "描述", "传动带跟踪开始"
    "必选参数", "- ``status``： 状态，1-启动，0-停止"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

传动带跟踪停止
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorTrackEnd()``"
    "描述", "传动带跟踪停止"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

传动带参数配置
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorSetParam(param, followType, startDis, endDis)``"
    "描述", "传动带参数配置"
    "必选参数", "- ``param``： = [encChannel,resolution,lead,wpAxis,vision,speedRadio] 
                    - ``encChannel``: 编码器通道 1-2
                    - ``resolution``: 编码器分辨率 编码器旋转一圈脉冲个数
                    - ``lead``: 机械传动比 编码器旋转一圈传送带移动距离
                    - ``wpAxis``: 工件坐标系编号 针对跟踪运动功能选择工件坐标系编号，跟踪抓取、TPD跟踪设为0
                    - ``vision``: 是否配视觉  0-不配 1-配,
                    - ``speedRadio``: 速度比  针对传送带跟踪抓取速度范围为（1-100）  跟踪运动、TPD跟踪设置为1
    - ``followType``：跟踪运动类型，0-跟踪运动；1-追检运动"
    "默认参数", "- ``startDis``：追检抓取需要设置， 跟踪起始距离， -1：自动计算(工件到达机器人下方后自动追检)，单位mm， 默认值0
    - ``endDis``：追检抓取需要设置，跟踪终止距离， 单位mm， 默认值100"
    "返回值", "错误码 成功-0  失败- errcode"

传动带抓取点补偿
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorCatchPointComp(cmp)``"
    "描述", "传动带抓取点补偿"
    "必选参数", "- ``cmp``： 补偿位置 [x,y,z]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

直线运动
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorTrackMoveL(name,tool,wobj,vel=20,acc=100,ovl=100,blendR=-1.0)``"
    "描述", "直线运动"
    "必选参数", "- ``name``：cvrCatchPoint 或cvrRaisePoint
    - ``tool``: 工具号
    - ``wobj``:  工件号"
    "默认参数", "- ``vel``: 速度 默认20
    - ``acc``: 加速度 默认100
    - ``ovl``: 速度缩放因子 默认100
    - ``blendR``: [-1.0]-运动到位 (阻塞)，[0~1000]-平滑半径 (非阻塞)，单位 [mm] 默认-1.0"
    "返回值", "错误码 成功-0  失败- errcode"

传送带通讯输入检测
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorComDetect(timeout)``"
    "描述", "传送带通讯输入检测"
    "必选参数", "- ``timeout``：等待超时时间ms"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

传送带通讯输入检测触发
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorComDetectTrigger()``"
    "描述", "传送带通讯输入检测触发"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

机器人传送带操作代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    retval = robot.ConveyorStartEnd(1)
    print(f"ConveyorStartEnd retval is:{retval}")
    retval = robot.ConveyorPointIORecord()
    print(f"ConveyorPointIORecord retval is:{retval}")
    retval = robot.ConveyorPointARecord()
    print(f"ConveyorPointARecord retval is:{retval}")
    retval = robot.ConveyorRefPointRecord()
    print(f"ConveyorRefPointRecord retval is:{retval}")
    retval = robot.ConveyorPointBRecord()
    print(f"ConveyorPointBRecord retval is:{retval}")
    retval = robot.ConveyorStartEnd(0)
    print(f"ConveyorStartEnd retval is:{retval}")
    param = [1.0, 10000.0, 200.0, 0.0, 0.0, 20.0]
    retval = robot.ConveyorSetParam(param,0)
    print(f"ConveyorSetParam retval is:{retval}")
    cmp = [0.0, 0.0, 0.0]
    retval = robot.ConveyorCatchPointComp(cmp)
    print(f"ConveyorCatchPointComp retval is:{retval}")
    index = 1
    max_time = 30000
    block = 0
    retval = 0
    p1Desc = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    p2Desc = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    retval = robot.MoveCart(p1Desc, 1, 0, 100.0)
    print(f"MoveCart retval is:{retval}")
    retval = robot.WaitMs(1)
    print(f"WaitMs retval is:{retval}")
    retval = robot.ConveyorIODetect(10000)
    print(f"ConveyorIODetect retval is:{retval}")
    retval = robot.ConveyorGetTrackData(1)
    print(f"ConveyorGetTrackData retval is:{retval}")
    retval = robot.ConveyorTrackStart(1)
    print(f"ConveyorTrackStart retval is:{retval}")
    retval = robot.ConveyorTrackMoveL("cvrCatchPoint", 1, 0, 100)
    print(f"TrackMoveL retval is:{retval}")
    retval = robot.MoveGripper(index, 51, 40, 30, max_time, block, 0, 0, 0, 0)
    print(f"MoveGripper retval is:{retval}")
    retval = robot.ConveyorTrackMoveL("cvrRaisePoint", 1, 0, 100)
    print(f"TrackMoveL retval is:{retval}")
    retval = robot.ConveyorTrackEnd()
    print(f"ConveyorTrackEnd retval is:{retval}")
    robot.MoveCart(p2Desc, 1, 0, 100.0, 100.0)
    retval = robot.MoveGripper(index, 100, 40, 10, max_time, block, 0, 0, 0, 0)
    print(f"MoveGripper retval is:{retval}")
    robot.CloseRPC()

末端传感器配置
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleSensorConfig(idCompany, idDevice, idSoftware, idBus)``"
    "描述", "末端传感器配置"
    "必选参数", "
    - ``idCompany``: 厂商，18-JUNKONG；25-HUIDE
    - ``idDevice``: 类型，0-JUNKONG/RYR6T.V1.0
    - ``idSoftware``: 软件版本，0-J1.0/HuiDe1.0(暂未开放)
    - ``idBus``: 挂载位置，1-末端1号口；2-末端2号口...8-末端8号口(暂未开放)
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取末端传感器配置
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleSensorConfigGet()``"
    "描述", "获取末端传感器配置"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``idCompany``: 厂商，18-JUNKONG；25-HUIDE
    - ``idDevice``: 类型，0-JUNKONG/RYR6T.V1.0"
        
末端传感器激活
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleSensorActivate(actFlag)``"
    "描述", "末端传感器激活"
    "必选参数", "``actFlag``： 0-复位；1-激活"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``coord``: 坐标系值[x,y,z,rx,ry,rz]"

末端传感器寄存器写入
+++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleSensorRegWrite(devAddr, regHAddr, regLAddr, regNum, data1, data2, isNoBlock)``"
    "描述", "末端传感器寄存器写入"
    "必选参数", "- ``devAddr``：设备地址编号 0-255
    - ``regHAddr``：寄存器地址高8位
    - ``regLAddr``：寄存器地址低8位
    - ``regNum``：寄存器个数 0-255
    - ``data1``：写入寄存器数值1
    - ``data2``：写入寄存器数值2
    - ``isNoBlock``：是否阻塞 0-阻塞；1-非阻塞"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

末端传感器代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.AxleSensorConfig(18, 0, 0, 1)
    error, company, type = robot.AxleSensorConfigGet()
    print(f"company is:{company},type is:{type}")
    rtn = robot.AxleSensorActivate(1)
    print(f"AxleSensorActivate rtn is:{rtn}")
    time.sleep(1)
    rtn = robot.AxleSensorRegWrite(1, 4, 6, 1, 0, 0, 0)
    print(f"AxleSensorRegWrite rtn is:{rtn}")
    robot.CloseRPC()

获取机器人外设协议
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetExDevProtocol()``"
    "描述", "获取机器人外设协议"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode; 
    - ``protocol``: 机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster"

设置机器人外设协议
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExDevProtocol(protocol)``"
    "描述", "设置机器人外设协议"
    "必选参数", "- ``protocol``：机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置机器人外设协议代码示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    protocol = 4096
    rtn = robot.SetExDevProtocol(protocol)
    print(f"SetExDevProtocol rtn:{rtn}")
    rtn, protocol = robot.GetExDevProtocol()
    print(f"GetExDevProtocol rtn:{rtn},protocol is:{protocol}")
    robot.CloseRPC()


获取末端通讯参数
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleCommunicationParam()``"
    "描述", "获取末端通讯参数"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``baudRate``：波特率:支持1-9600，2-14400，3-19200，4-38400，5-56000，6-67600，7-115200，8-128000
    - ``dataBit``：数据位:数据位支持（8,9），目前常用为 8
    - ``stopBit``：停止位:1-1，2-0.5，3-2，4-1.5，目前常用为 1
    - ``verify``：校验位:0-None，1-Odd，2-Even,目前常用为 0
    - ``timeout``：超时时间:1~1000ms，此值需要结合外设搭配设置合理的时间参数
    - ``timeoutTimes``：超时次数:1~10，主要进行超时重发，减少偶发异常提高用户体验
    - ``period``：周期性指令时间间隔:1~1000ms，主要用于周期性指令每次下发的时间间隔"

设置末端通讯参数
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleCommunicationParam(baudRate, dataBit, stopBit, verify, timeout, timeoutTimes, period)``"
    "描述", "设置末端通讯参数"
    "必选参数", "- ``baudRate``：波特率:支持1-9600，2-14400，3-19200，4-38400，5-56000，6-67600，7-115200，8-128000
    - ``dataBit``：数据位:数据位支持（8,9），目前常用为 8
    - ``stopBit``：停止位:1-1，2-0.5，3-2，4-1.5，目前常用为 1
    - ``verify``：校验位:0-None，1-Odd，2-Even,目前常用为 0
    - ``timeout``：超时时间:1~1000ms，此值需要结合外设搭配设置合理的时间参数
    - ``timeoutTimes``：超时次数:1~10，主要进行超时重发，减少偶发异常提高用户体验
    - ``period``：周期性指令时间间隔:1~1000ms，主要用于周期性指令每次下发的时间间隔"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

设置末端文件传输类型
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleFileType(type)``"
    "描述", "设置末端文件传输类型"
    "必选参数", "- ``type``：1-MCU升级文件,2-LUA文件"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

设置启用末端LUA执行
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleLuaEnable(enable)``"
    "描述", "设置启用末端LUA执行"
    "必选参数", "- ``enable``：0-不启用；1-启用"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

末端LUA文件异常错误恢复
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRecoverAxleLuaErr(enable)``"
    "描述", "末端LUA文件异常错误恢复"
    "必选参数", "- ``status``：0-不恢复；1-恢复"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

获取末端LUA执行使能状态
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleLuaEnableStatus()``"
    "描述", "获取末端LUA执行使能状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``enable``：0-不启用；1-启用"

设置末端LUA末端设备启用类型
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleLuaEnableDeviceType(forceSensorEnable, gripperEnable, IOEnable)``"
    "描述", "设置末端LUA末端设备启用类型"
    "必选参数", "- ``forceSensorEnable``：力传感器启用状态，0-不启用；1-启用
    - ``gripperEnable``：夹爪启用状态，0-不启用；1-启用
    - ``IOEnable``：IO设备启用状态，0-不启用；1-启用"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

获取末端LUA末端设备启用类型
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleLuaEnableDeviceType()``"
    "描述", "获取末端LUA末端设备启用类型"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``forceSensorEnable``：力传感器启用状态，0-不启用；1-启用
    - ``gripperEnable``：夹爪启用状态，0-不启用；1-启用
    - ``IOEnable``：IO设备启用状态，0-不启用；1-启用"

获取当前配置的末端设备
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleLuaEnableDevice()``"
    "描述", "获取当前配置的末端设备"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``forceSensorEnable[8]``：力传感器启用状态，0-不启用；1-启用
    - ``gripperEnable[8]``：夹爪启用状态，0-不启用；1-启用
    - ``IOEnable[8]``：IO设备启用状态，0-不启用；1-启用"

设置启用夹爪动作控制功能
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleLuaGripperFunc(id, func)``"
    "描述", "设置启用夹爪动作控制功能"
    "必选参数", "- ``id``：夹爪设备编号
    - ``func``：0-夹爪使能；1-夹爪初始化；2-位置设置；3-速度设置；4-力矩设置；6-读夹爪状态；7-读初始化状态；8-读故障码；9-读位置；10-读速度；11-读力矩,12-15预留"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

获取启用夹爪动作控制功能
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleLuaGripperFunc(id)``"
    "描述", "获取启用夹爪动作控制功能"
    "必选参数", "- ``id``：夹爪设备编号"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``func``：0-夹爪使能；1-夹爪初始化；2-位置设置；3-速度设置；4-力矩设置；6-读夹爪状态；7-读初始化状态；8-读故障码；9-读位置；10-读速度；11-读力矩,12-15预留"

机器人Ethercat从站文件写入
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SlaveFileWrite(type,slaveID,fileName)``"
    "描述", "机器人Ethercat从站文件写入"
    "必选参数", "- ``type``：从站文件类型，1-升级从站文件；2-升级从站配置文件
    - ``slaveID``：从站号
    - ``fileName``：上传文件名"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

上传末端Lua开放协议文件
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleLuaUpload(filePath)``"
    "描述", "上传末端Lua开放协议文件"
    "必选参数", "- ``filePath``：本地lua文件路径名 .../AXLE_LUA_End_DaHuan.lua"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

机器人Ethercat从站进入boot模式
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetSysServoBootMode(filePath)``"
    "描述", "机器人Ethercat从站进入boot模式"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

机器人末端LUA文件操作代码示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.AxleLuaUpload("D://zUP/AXLE_LUA_End_DaHuan.lua")
    param = [7, 8, 1, 0, 5, 3, 1]  # 对应AxleComParam参数
    robot.SetAxleCommunicationParam(7, 8, 1, 0, 5, 3, 1)
    error,getParam0,getParam1,getParam2,getParam3,getParam4,getParam5,getParam6 = robot.GetAxleCommunicationParam()
    print(f"GetAxleCommunicationParam param is:{getParam0} {getParam1} {getParam2} {getParam3} {getParam4} {getParam5} {getParam6}")
    robot.SetAxleLuaEnable(1)
    error,luaEnableStatus = robot.GetAxleLuaEnableStatus()
    robot.SetAxleLuaEnableDeviceType(0, 1, 0)
    error,forceEnable, gripperEnable, ioEnable = robot.GetAxleLuaEnableDeviceType()
    print(f"GetAxleLuaEnableDeviceType param is:{forceEnable} {gripperEnable} {ioEnable}")
    func = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    robot.SetAxleLuaGripperFunc(1, func)
    error,getFunc = robot.GetAxleLuaGripperFunc(1)
    error,getforceEnable, getgripperEnable, getioEnable = robot.GetAxleLuaEnableDevice()
    print("\ngetforceEnable status:", end=" ")
    for i in range(8):
        print(f"{getforceEnable[i]},", end="")
    print("\ngetgripperEnable status:", end=" ")
    for i in range(8):
        print(f"{getgripperEnable[i]},", end="")
    print("\ngetioEnable status:", end=" ")
    for i in range(8):
        print(f"{getioEnable[i]},", end="")
    print()
    robot.ActGripper(1, 0)
    time.sleep(2)
    robot.ActGripper(1, 1)
    time.sleep(2)
    robot.MoveGripper(1, 90, 10, 100, 50000, 0, 0, 0, 0, 0)
    while True:
        error,pkg = robot.GetRobotRealTimeState()
        print(f"gripper pos is:{pkg.gripper_position}")
        time.sleep(0.1)
    robot.CloseRPC()

    
获取SmartTool按钮状态
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSmarttoolBtnState()``"
    "描述", "获取SmartTool按钮状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``state``：SmartTool手柄按钮状态;(bit0:0-通信正常；1-通信掉线；bit1-撤销操作；bit2-清空程序；bit3-A键；bit4-B键；bit5-C键；bit6-D键；bit7-E键；bit8-IO键；bit9-手自动；bit10开始)"

SmartTool按钮代码示例
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    while True:
        error,state = robot.GetSmarttoolBtnState()
        print(f"{state:016b}")
        time.sleep(0.1)