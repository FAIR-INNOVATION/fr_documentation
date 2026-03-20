机器人力控
============

.. toctree:: 
    :maxdepth: 5

力传感器配置
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_SetConfig(company,device,softversion=0,bus=0)``"
    "描述", "力传感器配置"
    "必选参数", "- ``company``：传感器厂商，17-坤维科技，19-航天十一院，20-ATI传感器，21-中科米点，22-伟航敏芯，23-NBIT，24-鑫精诚(XJC)，26-NSR；
    - ``device``：设备号，坤维(0-KWR75B)，航天十一院(0-MCS6A-200-4)，ATI(0-AXIA80-M8)，中科米点(0-MST2010)，伟航敏芯(0-WHC6L-YB-10A)，NBIT(0-XLH93003ACS)，鑫精诚XJC(0-XJC-6F-D82)，NSR(0-NSR-FTSensorA)；"
    "默认参数", "- ``softversion``：软件版本号，暂不使用，默认为0；
    - ``bus``：设备挂载末端总线位置，暂不使用，默认为 0；"
    "返回值", "错误码 成功-0  失败- errcode"

获取力传感器配置
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_GetConfig()``"
    "描述", "获取力传感器配置"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``[number,company,device,softversion,bus]``：number 传感器编号;company  力传感器厂商，17-坤维科技，19-航天十一院，20-ATI 传感器，21-中科米点，22-伟航敏芯;device  设备号，坤维 (0-KWR75B)，航天十一院 (0-MCS6A-200-4)，ATI(0-AXIA80-M8)，中科米点 (0-MST2010)，伟航敏芯 (0-WHC6L-YB10A);softvesion  软件版本号，暂不使用，默认为0" 

力传感器激活
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_Activate(state)``"
    "描述", "力传感器激活"
    "必选参数", "- ``state``：0-复位，1-激活"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

力传感器校零
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_SetZero(state)``"
    "描述", "力传感器校零"
    "必选参数", "- ``state``：0-去除零点，1-零点矫正"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置力传感器参考坐标系
+++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_SetRCS(ref,coord=[0,0,0,0,0,0])``"
    "描述", "设置力传感器参考坐标系"
    "必选参数", "- ``ref``：0-工具坐标系，1-基坐标系"
    "默认参数", "- ``coord``：[x,y,z,rx,ry,rz]自定义坐标系值,默认[0,0,0,0,0,0]"
    "返回值", "错误码 成功-0  失败- errcode "

        
设置力传感器下负载重量
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetForceSensorPayload(weight)``"
    "描述", "设置力传感器下负载重量"
    "必选参数", " - ``weight``：负载重量 kg"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
  
设置力传感器下负载质心
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetForceSensorPayloadCog(x,y,z)``"
    "描述", "设置力传感器下负载质心"
    "必选参数", "
    - ``x``：负载质心x mm
    - ``y``：负载质心y mm
    - ``z``：负载质心z mm
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
            
获取力传感器下负载重量
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetForceSensorPayload()``"
    "描述", "获取力传感器下负载重量"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``weight``：负载重量 kg"
            
获取力传感器下负载质心
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetForceSensorPayloadCog()``"
    "描述", "获取力传感器下负载质心"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``x``：负载质心x mm 
    - ``y``：负载质心y mm 
    - ``z``：负载质心z mm"

力传感器自动校零
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ForceSensorAutoComputeLoad()``"
    "描述", "力传感器自动校零"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``weight``：传感器质量 kg
    - ``pos=[x,y,z]``：传感器质心 mm"

获取参考坐标系下力/扭矩数据
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_GetForceTorqueRCS()``"
    "描述", "获取参考坐标系下力/扭矩数据"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``data=[fx,fy,fz,tx,ty,tz]``：参考坐标系下力/扭矩数据"

获取力传感器原始力/扭矩数据
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_GetForceTorqueOrigin()``"
    "描述", "获取力传感器原始力/扭矩数据"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode  
    - ``data=[fx,fy,fz,tx,ty,tz]``：力传感器原始力/扭矩数据 "

力传感器配置及自动校零代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    company = 24
    device = 0
    softversion = 0
    bus = 1
    index = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    error,[company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    error,ft = robot.FT_GetForceTorqueOrigin()
    print(f"ft origin:{ft[0]},{ft[1]},{ft[2]},{ft[3]},{ft[4]},{ft[5]}")
    robot.FT_SetZero(1)
    time.sleep(1)
    ftCoord = [0, 0, 0, 0, 0, 0]
    robot.FT_SetRCS(0, ftCoord)
    robot.SetForceSensorPayload(0.824)
    robot.SetForceSensorPayloadCog(0.778, 2.554, 48.765)
    error,weight = robot.GetForceSensorPayload()
    error,x, y, z = robot.GetForceSensorPayloadCog()
    print(f"the FT load is  {weight}, {x} {y} {z}")
    robot.SetForceSensorPayload(0)
    robot.SetForceSensorPayloadCog(0, 0, 0)
    error,computeWeight, tran = robot.ForceSensorAutoComputeLoad()
    print(f"the result is weight {computeWeight} pos is {tran[0]} {tran[1]} {tran[2]}")
    robot.CloseRPC()

负载重量辨识记录
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_PdIdenRecord(tool_id)``"
    "描述", "负载重量辨识记录"
    "必选参数", "- ``tool_id``：传感器坐标系编号，范围[0~14]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode  "

负载重量辨识计算
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_PdIdenCompute()``"
    "描述", "负载重量辨识计算"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode   
    - ``weight``：负载重量，单位 kg  "

负载质心辨识记录
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_PdCogIdenRecord(tool_id,index)``"
    "描述", "负载质心辨识记录"
    "必选参数", "- ``tool_id``：传感器坐标系编号，范围[0~14];
    - ``index``：点编号[1~3]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

负载质心辨识计算
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_PdCogIdenCompute()``"
    "描述", "负载质心辨识计算"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode  
    - ``cog=[cogx,cogy,cogz]``：负载质心，单位 mm  "

力传感器负载辨识代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    company = 24
    device = 0
    softversion = 0
    bus = 1
    index = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    error,[company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    error,ft = robot.FT_GetForceTorqueOrigin()
    print(f"ft origin:{ft[0]},{ft[1]},{ft[2]},{ft[3]},{ft[4]},{ft[5]}")
    robot.FT_SetZero(1)
    time.sleep(1)
    tcoord = [0, 0, 35.0, 0, 0, 0]
    robot.SetToolCoord(10, tcoord, 1, 0, 0, 0)
    robot.FT_PdIdenRecord(10)
    time.sleep(1)
    error,weight = robot.FT_PdIdenCompute()
    print(f"payload weight:{weight}")
    desc_p1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_p2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    desc_p3 = [-327.622, 402.230, 320.402, -178.067, 2.127, -46.207]
    robot.MoveCart(desc_p1, 0, 0, 100.0)
    time.sleep(1)
    robot.FT_PdCogIdenRecord(10, 1)
    robot.MoveCart(desc_p2, 0, 0, 100.0)
    time.sleep(1)
    robot.FT_PdCogIdenRecord(10, 2)
    robot.MoveCart(desc_p3, 0, 0, 100.0)
    time.sleep(1)
    robot.FT_PdCogIdenRecord(10, 3)
    time.sleep(1)
    error,cog = robot.FT_PdCogIdenCompute()
    print(f"FT_PdCogIdenCompute return {error}")
    print(f"cog:{cog[0]},{cog[1]},{cog[2]}")
    robot.CloseRPC()

碰撞守护
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_Guard(flag,sensor_num,select,force_torque,max_threshold,min_threshold)``"
    "描述", "碰撞守护"
    "必选参数", "- ``flag``：0-关闭碰撞守护，1-开启碰撞守护；
    - ``sensor_num``：力传感器编号；
    - ``select``：六个自由度是否检测碰撞[fx,fy,fz,mx,my,mz]，0-不生效，1-生效；
    - ``force_torque``：碰撞检测力/力矩，单位N或Nm；
    - ``max_threshold``：最大阈值；
    - ``min_threshold``：最小阈值；
    - 力/力矩检测范围:(force_torque-min_threshold,force_torque+max_threshold)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

碰撞守护代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    company = 24
    device = 0
    softversion = 0
    bus = 1
    index = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    error,[company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    sensor_id = 1
    select = [1, 1, 1, 1, 1, 1]
    max_threshold = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0]
    min_threshold = [5.0, 5.0, 5.0, 5.0, 5.0, 5.0]
    ft = None 
    desc_p1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_p2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    desc_p3 = [-327.622, 402.230, 320.402, -178.067, 2.127, -46.207]
    error = robot.FT_Guard(1, sensor_id, select,[0.0,0.0,0.0,0.0,0.0,0.0], max_threshold, min_threshold)
    robot.MoveCart(desc_p1, 0, 0, 100.0)
    robot.MoveCart(desc_p2, 0, 0, 100.0)
    robot.MoveCart(desc_p3, 0, 0, 100.0)
    robot.FT_Guard(0, sensor_id, select,[0.0,0.0,0.0,0.0,0.0,0.0], max_threshold, min_threshold)
    robot.CloseRPC()

恒力控制
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_Control(flag,sensor_num,select,force_torque,gain,adj_sign,ILC_sign,max_dis,max_ang)``"
    "描述", "恒力控制"
    "必选参数", "- ``flag``：恒力控制开启标志，0-关，1-开；
    - ``sensor_num``：力传感器编号；
    - ``select``：六个自由度是否检测 [fx,fy,fz,mx,my,mz]，0-不生效，1-生效；
    - ``force_torque``：检测力/力矩，单位N或Nm；
    - ``gain``：[f_p,f_i,f_d,m_p,m_i,m_d],力PID参数，力矩PID参数；
    - ``adj_sign``：自适应启停状态，0-关闭，1-开启；
    - ``ILC_sign``: ILC控制启停状态，0-停止，1-训练，2-实操；
    - ``max_dis``：最大调整距离；
    - ``max_ang``：最大调整角度；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

恒力控制代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    company = 24
    device = 0
    softversion = 0
    bus = 1
    index = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    error,[company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    sensor_id = 1
    select = [0, 0, 1, 0, 0, 0]
    ft_pid = [0.0005, 0.0, 0.0, 0.0, 0.0, 0.0]
    adj_sign = 0
    ILC_sign = 0
    max_dis = 100.0
    max_ang = 0.0
    ft = [0.0,0.0,-10.0,0.0,0.0,0.0]
    j1 = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    j2 = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    desc_p1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_p2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    epos = [0, 0, 0, 0]
    offset_pos = [0, 0, 0, 0, 0, 0]
    rtn = robot.MoveJ(joint_pos=j1,tool= 0,user= 0,vel= 100.0)
    robot.FT_Control(1, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang)
    rtn = robot.MoveJ(joint_pos=j2,tool= 0,user= 0,vel= 100.0)
    robot.FT_Control(0, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang)
    robot.CloseRPC()

螺旋线探索
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_SpiralSearch(rcs, ft, dr=0.7, max_t_ms=60000, max_vel=5)``"
    "描述", "螺旋线探索"
    "必选参数", "- ``rcs``：参考坐标系，0-工具坐标系，1-基坐标系
    - ``ft``：力或力矩阈值 (0~100)，单位 N 或 Nm;"
    "默认参数", "- ``dr``：每圈半径进给量，单位 mm 默认0.7;
    - ``max_t_ms``：最大探索时间，单位 ms 默认 60000;
    - ``max_vel``：线速度最大值，单位 mm/s 默认 5"
    "返回值", "错误码 成功-0  失败- errcode "

旋转插入
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_RotInsertion(rcs, ft, orn, angVelRot=3, angleMax=45, angAccmax=0, rotorn=1)``"
    "描述", "旋转插入"
    "必选参数", "- ``rcs``：参考坐标系，0-工具坐标系，1-基坐标系；
    - ``ft``：力或力矩阈值 (0~100)，单位 N 或 Nm;
    - ``orn``：力/扭矩方向，1-沿z轴方向，2-绕z轴方向;"
    "默认参数", "- ``angVelRot``：旋转角速度，单位°/s,默认 3;
    - ``angleMax``：最大旋转角度，单位 ° 默认 45;
    - ``angAccmax``：最大旋转加速度，单位 °/s^2，暂不使用 默认0;
    - ``rotorn``：旋转方向，1-顺时针，2-逆时针 默认1"
    "返回值", "错误码 成功-0  失败- errcode "

直线插入
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_LinInsertion(rcs, ft, disMax, linorn, lin_v=1.0, lin_a=1.0)``"
    "描述", "直线插入"
    "必选参数", "- ``rcs``：参考坐标系，0-工具坐标系，1-基坐标系；
    - ``ft``：力或力矩阈值 (0~100)，单位 N 或 Nm;
    - ``disMax``：最大插入距离，单位 mm;
    - ``linorn``：插入方向:0-负方向，1-正方向"
    "默认参数", "- ``lin_v``：直线速度，单位 mm/s 默认1;
    - ``lin_a``：直线加速度，单位 mm/s^2，暂不使用 默认1"
    "返回值", "错误码 成功-0  失败- errcode "

螺旋探索、直线插入等指令代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:
    
    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    company = 24
    device = 0
    softversion = 0
    bus = 1
    index = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    error,[company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    status = 1
    sensor_num = 1
    gain = [0.0001, 0.0, 0.0, 0.0, 0.0, 0.0]
    adj_sign = 0
    ILC_sign = 0
    max_dis = 100.0
    max_ang = 5.0
    ft = [0.0,0.0,-10.0,0.0,0.0,0.0]
    rcs = 0
    dr = 0.7
    fFinish = 1.0
    t = 60000.0
    vmax = 3.0
    force_goal = 20.0
    lin_v = 0.0
    lin_a = 0.0
    disMax = 100.0
    linorn = 1
    angVelRot = 2.0
    forceInsertion = 1.0
    angleMax = 45
    orn = 1
    angAccmax = 0.0
    rotorn = 1
    select1 = [0, 0, 1, 1, 1, 0]
    robot.FT_Control(status, sensor_num, select1, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    rtn = robot.FT_SpiralSearch(rcs, dr, fFinish, t, vmax)
    print(f"FT_SpiralSearch rtn is {rtn}")
    robot.FT_Control(0, sensor_num, select1, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    select2 = [1, 1, 1, 0, 0, 0]
    gain[0] = 0.00005
    ft[2] = -30.0
    robot.FT_Control(1, sensor_num, select2, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    rtn = robot.FT_LinInsertion(rcs, force_goal, lin_v, lin_a, disMax, linorn)
    print(f"FT_LinInsertion rtn is {rtn}")
    robot.FT_Control(0, sensor_num, select2, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    select3 = [0, 0, 1, 1, 1, 0]
    ft[2] = -10.0
    gain[0] = 0.0001
    robot.FT_Control(1, sensor_num, select3, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    rtn = robot.FT_RotInsertion(rcs, angVelRot, forceInsertion, angleMax, orn, angAccmax, rotorn)
    print(f"FT_RotInsertion rtn is {rtn}")
    robot.FT_Control(0, sensor_num, select3, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    select4 = [1, 1, 1, 0, 0, 0]
    ft[2] = -30.0
    robot.FT_Control(1, sensor_num, select4, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    rtn = robot.FT_LinInsertion(rcs, force_goal, lin_v, lin_a, disMax, linorn)
    print(f"FT_LinInsertion rtn is {rtn}")
    robot.FT_Control(0, sensor_num, select4, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    robot.CloseRPC()

表面定位
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_FindSurface (rcs, dir, axis, disMax, ft, lin_v=3.0, lin_a=0.0)``"
    "描述", "表面定位"
    "必选参数", "- ``rcs``： 参考坐标系，0-工具坐标系，1-基坐标系；
    - ``dir``：移动方向，1-正方向，2-负方向；
    - ``axis``：移动轴，1-x，2-y，3-z；
    - ``disMax``：大探索距离，单位 mm;
    - ``ft``：动作终止力阈值，单位N；"
    "默认参数", "- ``lin_v``：探索直线速度，单位mm/s 默认3;
    - ``lin_a``：探索直线加速度，单位mm/s^2 默认0;"
    "返回值", "错误码 成功-0  失败- errcode"

计算中间平面位置开始
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_CalCenterStart()``"
    "描述", "计算中间平面位置开始"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

计算中间平面位置结束
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_CalCenterEnd()``"
    "描述", "计算中间平面位置结束"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode
    - ``pos=[x,y,z,rx,ry,rz]``：中间平面位置"

表面定位代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    company = 24
    device = 0
    softversion = 0
    bus = 1
    index = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    error,[company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    rcs = 0
    dir = 1
    axis = 1
    lin_v = 3.0
    lin_a = 0.0
    maxdis = 50.0
    ft_goal = 2.0
    desc_pos = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    xcenter = [0, 0, 0, 0, 0, 0]
    ycenter = [0, 0, 0, 0, 0, 0]
    ft = [-2.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    robot.MoveCart(desc_pos, 9, 0, 100.0)
    robot.FT_CalCenterStart()
    robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal)
    robot.MoveCart(desc_pos, 9, 0)
    robot.WaitMs(1000)
    dir = 2
    robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal)
    error,xcenter = robot.FT_CalCenterEnd()
    print(f"xcenter:{xcenter[0]},{xcenter[1]},{xcenter[2]},{xcenter[3]},{xcenter[4]},{xcenter[5]}")
    robot.MoveCart(xcenter, 9, 0, 60.0)
    robot.FT_CalCenterStart()
    dir = 1
    axis = 2
    lin_v = 6.0
    maxdis = 150.0
    robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal)
    robot.MoveCart(desc_pos, 9, 0, 100.0)
    robot.WaitMs(1000)
    dir = 2
    robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal)
    error,ycenter = robot.FT_CalCenterEnd()
    print(f"ycenter:{ycenter[0]},{ycenter[1]},{ycenter[2]},{ycenter[3]},{ycenter[4]},{ycenter[5]}")
    robot.MoveCart(ycenter, 9, 0, 60.0)
    robot.CloseRPC()

柔顺控制开启
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_ComplianceStart(p, force)``"
    "描述", "柔顺控制开启"
    "必选参数", "- ``p``: 位置调节系数或柔顺系数
    - ``force``：柔顺开启力阈值，单位N"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode  "

柔顺控制关闭
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_ComplianceStop()``"
    "描述", "柔顺控制关闭"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

柔顺控制代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    company = 24
    device = 0
    softversion = 0
    bus = 1
    index = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    error,[company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    flag = 1
    sensor_id = 1
    select = [1, 1, 1, 0, 0, 0]
    ft_pid = [0.0005, 0.0, 0.0, 0.0, 0.0, 0.0]
    adj_sign = 0
    ILC_sign = 0
    max_dis = 100.0
    max_ang = 0.0
    ft = [-10.0, -10.0, -10.0, 0.0, 0.0, 0.0]
    offset_pos = [0.0,0.0,0.0,0.0,0.0,0.0]  # 替代 DescPose(0, 0, 0, 0, 0, 0)
    epos = [0.0,0.0,0.0,0.0]  # 替代 ExaxisPos(0, 0, 0, 0)
    j1 = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]  # JointPos
    j2 = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    desc_p1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]  # DescPose
    desc_p2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    p = 0.00005
    force = 30.0
    rtn = robot.FT_ComplianceStart(p, force)
    print(f"FT_ComplianceStart rtn is {rtn}")
    count = 3
    while count > 0:
        robot.MoveL(desc_pos=desc_p1,tool= 0,user= 0,vel= 100.0)
        robot.MoveL(desc_pos=desc_p2,tool= 0,user= 0,vel= 100.0)
        count -= 1
    robot.FT_ComplianceStop()
    print(f"FT_ComplianceStop rtn is {rtn}")
    flag = 0
    robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    robot.CloseRPC()

负载辨识滤波初始化
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadIdentifyDynFilterInit()``"
    "描述", "负载辨识滤波初始化"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode  "

负载辨识变量初始化
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadIdentifyDynVarInit()``"
    "描述", "负载辨识变量初始化"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode  "

负载辨识主程序
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadIdentifyMain(joint_torque, joint_pos, t)``"
    "描述", "负载辨识主程序"
    "必选参数", "- ``joint_torque``： 关节扭矩 j1-j6；
    - ``joint_pos``：关节位置 j1-j6
    - ``t``：采样周期"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取负载辨识结果
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadIdentifyGetResult(gain)``"
    "描述", "获取负载辨识结果"
    "必选参数", "- ``gain``：重力项系数double[6]，离心项系数double[6]"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``weight``：负载重量
    - ``cog=[x,y,z]``：负载质心坐标"

机器人负载辨识代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    retval = robot.LoadIdentifyDynFilterInit()
    print(f"LoadIdentifyDynFilterInit retval is: {retval}")
    retval = robot.LoadIdentifyDynVarInit()
    print(f"LoadIdentifyDynVarInit retval is: {retval}")
    error, posJ = robot.GetActualJointPosDegree(0)
    posJ[1] += 10  # Modify joint 2
    error, joint_toq = robot.GetJointTorques(0)
    joint_toq[1] += 2  # Modify torque on joint 2
    tmpTorque = joint_toq.copy()
    retval = robot.LoadIdentifyMain(tmpTorque, posJ, 1)
    print(f"LoadIdentifyMain retval is: {retval}")
    gain = [0, 0.05, 0, 0, 0, 0, 0, 0.02, 0, 0, 0, 0]
    weight = [0.0]
    load_pos = [0.0, 0.0, 0.0]
    retval, weight, load_pos = robot.LoadIdentifyGetResult(gain)
    print(f"LoadIdentifyGetResult retval is: {retval} ; weight is {weight}  cog is {load_pos[0]} {load_pos[1]} {load_pos[2]}")
    robot.CloseRPC()

力传感器辅助拖动
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``EndForceDragControl(status, asaptiveFlag, interfereDragFlag, ingularityConstraintsFlag, M, B, K, F, Fmax, Vmax, forceCollisionFlag=0)``"
    "描述", "力传感器辅助拖动"
    "必选参数", "- ``status``：控制状态，0-关闭；1-开启
    - ``asaptiveFlag``：自适应开启标志，0-关闭；1-开启
    - ``interfereDragFlag``：干涉区拖动标志，0-关闭；1-开启
    - ``ingularityConstraintsFlag``：奇异点策略，0-规避；1-穿越
    - ``forceCollisionFlag``：辅助拖动时机器人碰撞检测标志；0-关闭；1-开启
    - ``M=[m1,m2,m3,m4,m5,m6]``：惯性系数
    - ``B=[b1,b2,b3,b4,b5,b6]``：阻尼系数
    - ``K=[k1,k2,k3,k4,k5,k6]``：刚度系数
    - ``F=[f1,f2,f3,f4,f5,f6]``：拖动六维力阈值
    - ``Fmax``：最大拖动力限制
    - ``Vmax``：最大关节速度限制"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
        
获取力传感器拖动开关状态
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetForceAndTorqueDragState()``"
    "描述", "获取力传感器拖动开关状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``dragState``：力传感器辅助拖动控制状态，0-关闭；1-开启
    - ``sixDimensionalDragState``：六维力辅助拖动控制状态，0-关闭；1-开启"
    
报错清除后力传感器自动开启
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetForceSensorDragAutoFlag(status)``"
    "描述", "报错清除后力传感器自动开启"
    "必选参数", "- ``status``：控制状态，0-关闭；1-开启"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
力传感器辅助拖动代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.SetForceSensorDragAutoFlag(1)
    M = [15.0, 15.0, 15.0, 0.5, 0.5, 0.1]
    B = [150.0, 150.0, 150.0, 5.0, 5.0, 1.0]
    K = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    F = [10.0, 10.0, 10.0, 1.0, 1.0, 1.0]
    robot.EndForceDragControl(1, 0, 0, 0, M, B, K, F, 50, 100)
    time.sleep(5)
    drag_state = 0
    six_dimensional_drag_state = 0
    error,drag_state, six_dimensional_drag_state = robot.GetForceAndTorqueDragState()
    print(f"the drag state is {drag_state} {six_dimensional_drag_state}")
    robot.EndForceDragControl(0, 0, 0, 0, M, B, K, F, 50, 100)
    robot.CloseRPC()
    
设置六维力和关节阻抗混合拖动开关及参数
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ForceAndJointImpedanceStartStop(status, impedanceFlag, lamdeDain, KGain, BGain, dragMaxTcpVel, dragMaxTcpOriVel)``"
    "描述", "设置六维力和关节阻抗混合拖动开关及参数"
    "必选参数", "- ``status``：控制状态，0-关闭；1-开启
    - ``impedanceFlag``：阻抗开启标志，0-关闭；1-开启
    - ``lamdeDain``：[D1,D2,D3,D4,D5, D6] 拖动增益
    - ``KGain``：[K1,K2,K3,K4,K5,K6]刚度增益
    - ``BGain``：[B1,B2,B3,B4,B5,B]阻尼增益
    - ``dragMaxTcpVel``：拖动末端最大线速度限制
    - ``dragMaxTcpOriVel``：拖动末端最大角速度限制"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

六维力和关节阻抗混合拖动代码示例
++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.DragTeachSwitch(1)
    lamde_dain = [3.0, 2.0, 2.0, 2.0, 2.0, 3.0]
    k_gain = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    b_gain = [150.0, 150.0, 150.0, 5.0, 5.0, 1.0]
    rtn = robot.ForceAndJointImpedanceStartStop(1, 0, lamde_dain, k_gain, b_gain, 1000, 180)
    print(f"ForceAndJointImpedanceStartStop rtn is {rtn}")
    time.sleep(5)
    robot.DragTeachSwitch(0)
    rtn = robot.ForceAndJointImpedanceStartStop(0, 0, lamde_dain, k_gain, b_gain, 1000, 180)
    print(f"ForceAndJointImpedanceStartStop rtn is {rtn}")
    robot.CloseRPC()

设置焊丝寻位扩展IO端口
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWireSearchExtDIONum(searchDoneDINum, searchStartDONum)``"
    "描述", "设置焊丝寻位扩展IO端口"
    "必选参数", "- ``searchDoneDINum``：焊丝寻位成功DO端口(0-127)
    - ``searchStartDONum``：焊丝寻位启停控制DO端口(0-127)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

代码示例
++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    toolCoord = [0, 0, 200, 0, 0, 0]
    robot.SetToolCoord(1, toolCoord, 0, 0, 1, 0)
    wobjCoord = [0, 0, 0, 0, 0, 0]
    robot.SetWObjCoord(1, wobjCoord, 0)
    robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 50, 5, 50, 1, 50, 10)
    robot.ExtDevLoadUDPDriver()
    robot.SetWireSearchExtDIONum(0, 0)
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    descStart = [216.543, 445.175, 93.465, 179.683, 1.757, -112.641]
    jointStart = [-128.345, -86.660, 114.679, -119.625, -89.219, 74.303]
    descEnd = [111.143, 523.384, 87.659, 179.703, 1.835, -97.750]
    jointEnd = [-113.454, -81.060, 109.328, -119.954, -89.218, 74.302]
    error = robot.MoveL(desc_pos=descStart,tool= 1,user= 1,vel= 100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos=descEnd,tool= 1,user= 1,vel= 100)
    print(f"MoveL return: {error}")
    descREF0A = [142.135, 367.604, 86.523, 179.728, 1.922, -111.089]
    jointREF0A = [-126.794, -100.834, 128.922, -119.864, -89.218, 74.302]
    descREF0B = [254.633, 463.125, 72.604, 179.845, 2.341, -114.704]
    jointREF0B = [-130.413, -81.093, 112.044, -123.163, -89.217, 74.303]
    descREF1A = [92.556, 485.259, 47.476, -179.932, 3.130, -97.512]
    jointREF1A = [-113.231, -83.815, 119.877, -129.092, -89.217, 74.303]
    descREF1B = [203.103, 583.836, 63.909, 179.991, 2.854, -103.372]
    jointREF1B = [-119.088, -69.676, 98.692, -121.761, -89.219, 74.303]
    error = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchStart return: {error}")
    error = robot.MoveL(desc_pos=descREF0A,tool= 1,user= 1,vel= 100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos=descREF0B,tool= 1,user= 1,vel= 100,search=1)
    print(f"MoveL return: {error}")
    error = robot.WireSearchWait("REF0")
    print(f"WireSearchWait return: {error}")
    error = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchEnd return: {error}")
    error = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchStart return: {error}")
    error = robot.MoveL(desc_pos= descREF1A,tool= 1,user= 1,vel= 100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos= descREF1B,tool= 1,user= 1,vel= 100,search=1)
    print(f"MoveL return: {error}")
    error = robot.WireSearchWait("REF1")
    print(f"WireSearchWait return: {error}")
    error = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0)
    error = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchStart return: {error}")
    error = robot.MoveL(desc_pos= descREF0A,tool= 1,user= 1,vel= 100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos= descREF0B,tool= 1,user= 1,vel= 100,search=1)
    print(f"MoveL return: {error}")
    error = robot.WireSearchWait("RES0")
    print(f"WireSearchWait return: {error}")
    error = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchEnd return: {error}")
    error = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchStart return: {error}")
    error = robot.MoveL(desc_pos= descREF1A,tool= 1,user= 1,vel= 100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos= descREF1B,tool= 1,user= 1,vel= 100,search=1)
    print(f"MoveL return: {error}")
    error = robot.WireSearchWait("RES1")
    print(f"WireSearchWait return: {error}")
    error = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchEnd return: {error}")
    varNameRef = ["REF0", "REF1", "#", "#", "#", "#"]
    varNameRes = ["RES0", "RES1", "#", "#", "#", "#"]
    offectFlag = 0
    offectPos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    error, offectFlag, offectPos = robot.GetWireSearchOffset(0, 0, varNameRef, varNameRes)
    print(f"GetWireSearchOffset return: {error}")
    error = robot.PointsOffsetEnable(0, offectPos)
    print(f"PointsOffsetEnable return: {error}")
    error = robot.MoveL(desc_pos= descStart,tool= 1,user= 1,vel= 100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos= descEnd,tool= 1,user= 1,vel= 100,search=1)
    print(f"MoveL return: {error}")
    error = robot.PointsOffsetDisable()
    robot.CloseRPC()
