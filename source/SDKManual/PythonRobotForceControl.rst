机器人力控
============

.. toctree:: 
    :maxdepth: 5

获取力传感器配置
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_GetConfig()"
    "描述", "获取力传感器配置"
    "参数", "无"
    "返回值", "错误码 成功-0  失败- errcode
    - 返回值（调用成功返回）[number,company,device,softversion,bus]
    - number 传感器编号;
    - company  力传感器厂商，17-坤维科技，19-航天十一院，20-ATI 传感器，21-中科米点，22-伟航敏芯;
    - device  设备号，坤维 (0-KWR75B)，航天十一院 (0-MCS6A-200-4)，ATI(0-AXIA80-M8)，中科米点 (0-MST2010)，伟航敏芯 (0-WHC6L-YB10A);
    - softvesion  软件版本号，暂不使用，默认为0" 

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    company = 17    #传感器厂商，17-坤维科技
    device = 0      #传感器设备号
    error = robot.FT_SetConfig(company, device)   #配置力传感器
    print("配置力传感器错误码",error)
    config = robot.FT_GetConfig() #获取力传感器配置信息
    print('获取力传感器配置信息',config)
    time.sleep(1)
    error = robot.FT_Activate(0)  #传感器复位
    print("传感器复位错误码",error)
    time.sleep(1)
    error = robot.FT_Activate(1)  #传感器激活
    print("传感器激活错误码",error)
    time.sleep(1)
    error = robot.SetLoadWeight(0.0)    #末端负载设置为零
    print("末端负载设置为零错误码",error)
    time.sleep(1)
    error = robot.SetLoadCoord(0.0,0.0,0.0)  #末端负载质心设置为零
    print("末端质心设置为零错误码",error)
    time.sleep(1)
    error = robot.FT_SetZero(0)   #传感器去除零点
    print("传感器去除零点错误码",error)
    time.sleep(1)
    error = robot.FT_GetForceTorqueOrigin()   #查询传感器原始数据
    print("查询传感器原始数据",error)
    error = robot.FT_SetZero(1)   #传感器零点矫正,注意此时末端不能安装工具，只有力传感器
    print("传感器零点矫正",error)
    time.sleep(1)
    error = robot.FT_GetForceTorqueRCS()  #查询传感器坐标系下数据
    print("查询传感器坐标系下数据",error)

力传感器配置
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_SetConfig(company,device,softversion=0,bus=0)"
    "描述", "力传感器配置"
    "参数", "- ``必选参数 company``：传感器厂商，17-坤维科技，19-航天十一院，20-ATI传感器，21-中科米点，22-伟航敏芯；
    - ``必选参数 device``：设备号，坤维(0-KWR75B)，航天十一院(0-MCS6A-200-4)，ATI(0-AXIA80-M8)，中科米点(0-MST2010)，伟航敏芯(0-WHC6L-YB-10A)；
    - ``默认参数 softversion``：软件版本号，暂不使用，默认为0；
    - ``默认参数 bus``：设备挂载末端总线位置，暂不使用，默认为 0；"
    "返回值", "- 成功：[0]
    - 失败：[errcode]"

力传感器激活
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_Activate(state)"
    "描述", "力传感器激活"
    "参数", "- ``必选参数 state``：0-复位，1-激活"
    "返回值", "错误码 成功-0  失败- errcode "

力传感器校零
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_SetZero(state)"
    "描述", "力传感器校零"
    "参数", "- ``必选参数 state``：0-去除零点，1-零点矫正"
    "返回值", "错误码 成功-0  失败- errcode"

设置力传感器参考坐标系
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_SetRCS(ref)"
    "描述", "设置力传感器参考坐标系"
    "参数", "- ``必选参数 ref``：0-工具坐标系，1-基坐标系"
    "返回值", "错误码 成功-0  失败- errcode "

代码示例
------------
.. code-block:: python
    :linenos:
    :emphasize-lines: 4

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    #负载辨识，此时末端安装要辨识的工具，工具安装在力传感器下方,末端竖直向下
    error = robot.FT_SetRCS(0)    #设置参考坐标系为工具坐标系，0-工具坐标系，1-基坐标系
    print('设置参考坐标系错误码',error)
    time.sleep(1)
    tool_id = 10  #传感器坐标系编号
    tool_coord = [0.0,0.0,35.0,0.0,0.0,0.0]   # 传感器相对末端法兰位姿
    tool_type = 1  # 0-工具，1-传感器
    tool_install = 0 # 0-安装末端，1-机器人外部
    error = robot.SetToolCoord(tool_id,tool_coord,tool_type,tool_install)     #设置传感器坐标系，传感器相对末端法兰位姿
    print('设置传感器坐标系错误码',error)
    time.sleep(1)
    error = robot.FT_PdIdenRecord(tool_id)   #记录辨识数据
    print('记录负载重量错误码',error)
    time.sleep(1)
    error = robot.FT_PdIdenRecord()  #计算负载重量，单位kg
    print('计算负载重量错误码',error)
    #负载质心辨识，机器人需要示教三个不同的姿态，然后记录辨识数据，最后计算负载质心
    robot.Mode(1)
    ret = robot.DragTeachSwitch(1)  #机器人切入拖动示教模式，必须在手动模式下才能切入拖动示教模式
    time.sleep(5)
    ret = robot.DragTeachSwitch(0)
    time.sleep(1)
    error = robot.FT_PdCogIdenRecord(tool_id,1)
    print('负载质心1错误码',error)#记录辨识数据
    ret = robot.DragTeachSwitch(1)  #机器人切入拖动示教模式，必须在手动模式下才能切入拖动示教模式
    time.sleep(5)
    ret = robot.DragTeachSwitch(0)
    time.sleep(1)
    error = robot.FT_PdCogIdenRecord(tool_id,2)
    print('负载质心2错误码',error)
    ret = robot.DragTeachSwitch(1)  #机器人切入拖动示教模式，必须在手动模式下才能切入拖动示教模式
    time.sleep(5)
    ret = robot.DragTeachSwitch(0)
    time.sleep(1)
    error = robot.FT_PdCogIdenRecord(tool_id,3)
    print('负载质心3错误码',error)
    time.sleep(1)
    error = robot.FT_PdCogIdenCompute()
    print('负载质心计算错误码',error)

负载重量辨识计算
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_PdIdenCompute()"
    "描述", "负载重量辨识计算"
    "参数", "无"
    "返回值", "错误码 成功-0  失败- errcode   
    - 返回值（调用成功返回）weight-负载重量，单位 kg  "

负载重量辨识记录
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_PdIdenRecord(tool_id)"
    "描述", "负载重量辨识记录"
    "参数", "- ``必选参数 tool_id``：传感器坐标系编号，范围[0~14]"
    "返回值", "错误码 成功-0  失败- errcode  "

负载质心辨识计算
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_PdCogIdenCompute ()"
    "描述", "负载质心辨识计算"
    "参数", "无"
    "返回值", "错误码 成功-0  失败- errcode  
    - 返回值（调用成功返回）cog=[cogx,cogy,cogz] ，负载质心，单位 mm  "

负载质心辨识记录
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_PdCogIdenRecord(tool_id,index)"
    "描述", "负载质心辨识记录"
    "参数", "- ``必选参数 tool_id``：传感器坐标系编号，范围[0~14];
    - ``必选参数 index``：点编号[1~3]"
    "返回值", "错误码 成功-0  失败- errcode"

获取参考坐标系下力/扭矩数据
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_GetForceTorqueRCS()"
    "描述", "获取参考坐标系下力/扭矩数据"
    "参数", "无"
    "返回值", "错误码 成功-0  失败- errcode 
    - 返回值（调用成功返回）data=[fx,fy,fz,tx,ty,tz]"

代码示例
------------
.. code-block:: python
    :linenos:
    :emphasize-lines: 4

    import frrpc
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = frrpc.RPC('192.168.58.2')
    rcs = robot.FT_GetForceTorqueRCS()  #查询传感器坐标系下数据
    print(rcs)

获取力传感器原始力/扭矩数据
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_GetForceTorqueOrigin()"
    "描述", "获取力传感器原始力/扭矩数据"
    "参数", "无"
    "返回值", "错误码 成功-0  失败- errcode  
    - 返回值（调用成功返回）data=[fx,fy,fz,tx,ty,tz] "

代码示例
------------
.. code-block:: python
    :linenos:
    :emphasize-lines: 4

    import frrpc
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = frrpc.RPC('192.168.58.2')
    origin = robot.FT_GetForceTorqueOrigin()   #查询传感器原始数据
    print(origin)

碰撞守护
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_Guard(flag,sensor_num,select,force_torque,max_threshold,min_threshold)"
    "描述", "碰撞守护"
    "参数", "- ``必选参数 flag``：0-关闭碰撞守护，1-开启碰撞守护；
    - ``必选参数 sensor_num``：力传感器编号；
    - ``s必选参数 elect``：六个自由度是否检测碰撞[fx,fy,fz,mx,my,mz]，0-不生效，1-生效；
    - ``必选参数 force_torque``：碰撞检测力/力矩，单位N或Nm；
    - ``必选参数 max_threshold``：最大阈值；
    - ``必选参数 min_threshold``：最小阈值；
    - 力/力矩检测范围:(force_torque-min_threshold,force_torque+max_threshold)"
    "返回值", "错误码 成功-0  失败- errcode "

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    #碰撞守护
    actFlag = 1   #开启标志，0-关闭碰撞守护，1-开启碰撞守护
    sensor_num = 1  #力传感器编号
    is_select = [1,1,1,1,1,1]  #六个自由度选择[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
    force_torque = [0.0,0.0,0.0,0.0,0.0,0.0]  #碰撞检测力和力矩，检测范围（force_torque-min_threshold,force_torque+max_threshold）
    max_threshold = [10.0,10.0,10.0,10.0,10.0,10.0]  #最大阈值
    min_threshold = [5.0,5.0,5.0,5.0,5.0,5.0]   #最小阈值
    P1=[-160.619,-586.138,384.988,-170.166,-44.782,169.295]
    P2=[-87.615,-606.209,556.119,-102.495,10.118,178.985]
    P3=[41.479,-557.243,484.407,-125.174,46.995,-132.165]
    error = robot.FT_Guard(actFlag, sensor_num, is_select, force_torque, max_threshold, min_threshold)    #开启碰撞守护
    print("开启碰撞守护错误码",error)
    error = robot.MoveL(P1,1,0)         #笛卡尔空间直线运动
    print("笛卡尔空间直线运动错误码",error)
    error = robot.MoveL(P2,1,0)
    print("笛卡尔空间直线运动错误码",error)
    error = robot.MoveL(P3,1,0)
    print("笛卡尔空间直线运动错误码",error)
    actFlag = 0  
    error = robot.FT_Guard(actFlag, sensor_num, is_select, force_torque, max_threshold, min_threshold)    #关闭碰撞守护
    print("关闭碰撞守护错误码",error)

恒力控制
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_Control(flag,sensor_num,select,force_torque,gain,adj_sign,ILC_sign,max_dis,max_ang)"
    "描述", "恒力控制"
    "参数", "- ``必选参数 flag``：恒力控制开启标志，0-关，1-开；
    - ``必选参数 sensor_num``：力传感器编号；
    - ``必选参数 select``：六个自由度是否检测 [fx,fy,fz,mx,my,mz]，0-不生效，1-生效；
    - ``必选参数 force_torque``：检测力/力矩，单位N或Nm；
    - ``必选参数 gain``：[f_p,f_i,f_d,m_p,m_i,m_d],力PID参数，力矩PID参数；
    - ``必选参数 adj_sign``：自适应启停状态，0-关闭，1-开启；
    - ``必选参数 ILC_sign``: ILC控制启停状态，0-停止，1-训练，2-实操；
    - ``必选参数 max_dis``：最大调整距离；
    - ``必选参数 max_ang``：最大调整角度；"
    "返回值", "- 成功：[0]
    - 失败：[errcode]"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    #恒力控制
    status = 1  #恒力控制开启标志，0-关，1-开
    sensor_num = 1 #力传感器编号
    is_select = [0,0,1,0,0,0]  #六个自由度选择[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
    force_torque = [0.0,0.0,-10.0,0.0,0.0,0.0]  
    gain = [0.0005,0.0,0.0,0.0,0.0,0.0]  #力PID参数，力矩PID参数
    adj_sign = 0  #自适应启停状态，0-关闭，1-开启
    ILC_sign = 0  #ILC控制启停状态，0-停止，1-训练，2-实操
    max_dis = 100.0  #最大调整距离
    max_ang = 0.0  #最大调整角度
    J1=[70.395, -46.976, 90.712, -133.442, -87.076, -27.138]
    P2=[-123.978, -674.129, 44.308, -178.921, 2.734, -172.449]
    P3=[123.978, -674.129, 42.308, -178.921, 2.734, -172.449]
    error = robot.MoveJ(J1,1,0)    
    print("关节空间运动指令错误码",error)
    error = robot.MoveL(P2,1,0)
    print("笛卡尔空间直线运动指令错误码",error)
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恒力控制开启错误码",error)
    error = robot.MoveL(P3,1,0)   #笛卡尔空间直线运动
    print("笛卡尔空间直线运动指令错误码",error)
    status = 0
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恒力控制结束错误码",error)

螺旋线探索
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_SpiralSearch(rcs,ft, dr = 0.7,max_t_ms = 60000, max_vel = 5)"
    "描述", "螺旋线探索"
    "参数", "- ``必选参数 rcs``：参考坐标系，0-工具坐标系，1-基坐标系
    - ``必选参数 ft``：力或力矩阈值 (0~100)，单位 N 或 Nm;
    - ``默认参数 dr``：每圈半径进给量，单位 mm 默认0.7;
    - ``默认参数 max_t_ms``：最大探索时间，单位 ms 默认 60000;
    - ``默认参数 max_vel``：线速度最大值，单位 mm/s 默认 5"
    "返回值", "- 成功：[0]
    - 失败：[errcode]"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    P = [36.794,-675.119, 65.379, -176.938, 2.535, -179.829]
    #恒力参数
    status = 1  #恒力控制开启标志，0-关，1-开
    sensor_num = 1 #力传感器编号
    is_select = [0,0,1,0,0,0]  #六个自由度选择[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
    force_torque = [0.0,0.0,-10.0,0.0,0.0,0.0]  
    gain = [0.0001,0.0,0.0,0.0,0.0,0.0]  #力PID参数，力矩PID参数
    adj_sign = 0  #自适应启停状态，0-关闭，1-开启
    ILC_sign = 0  #ILC控制启停状态，0-停止，1-训练，2-实操
    max_dis = 100.0  #最大调整距离
    max_ang = 5.0  #最大调整角度
    #螺旋线探索参数
    rcs = 0  #参考坐标系，0-工具坐标系，1-基坐标系
    fFinish = 10 #力或力矩阈值（0~100），单位N或Nm
    error = robot.MoveL(P,1,0) #笛卡尔空间直线运动至初始点
    print("笛卡尔空间直线运动至初始点",error)
    is_select = [0,0,1,1,1,0]  #六个自由度选择[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign, max_dis,max_ang)
    print("恒力控制开启错误码",error)
    error = robot.FT_SpiralSearch(rcs,fFinish,max_vel=3)
    print("螺旋线探索错误码",error)
    status = 0
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign, max_dis,max_ang)
    print("恒力控制关闭错误码",error)

旋转插入
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_RotInsertion(rcs,ft, orn, angVelRot = 3, angleMax = 45, angAccmax = 0, rotorn =1)"
    "描述", "旋转插入"
    "参数", "- ``必选参数 rcs``：参考坐标系，0-工具坐标系，1-基坐标系；
    - ``必选参数 ft``：力或力矩阈值 (0~100)，单位 N 或 Nm;
    - ``必选参数 orn``：力/扭矩方向，1-沿z轴方向，2-绕z轴方向;
    - ``默认参数 angVelRot``：旋转角速度，单位°/s,默认 3;
    - ``默认参数 angleMax``：最大旋转角度，单位 ° 默认 5;
    - ``默认参数 angAccmax``：最大旋转加速度，单位 °/s^2，暂不使用 默认0;
    - ``默认参数 rotorn``：旋转方向，1-顺时针，2-逆时针 默认1"
    "返回值", "- 成功：[0]
    - 失败：[errcode]"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    P = [36.794,-675.119, 65.379, -176.938, 2.535, -179.829]
    #恒力参数
    status = 1  #恒力控制开启标志，0-关，1-开
    sensor_num = 1 #力传感器编号
    is_select = [0,0,1,0,0,0]  #六个自由度选择[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
    force_torque = [0.0,0.0,-10.0,0.0,0.0,0.0] 
    gain = [0.0001,0.0,0.0,0.0,0.0,0.0]  #力PID参数，力矩PID参数   
    adj_sign = 0  #自适应启停状态，0-关闭，1-开启
    ILC_sign = 0  #ILC控制启停状态，0-停止，1-训练，2-实操
    max_dis = 100.0  #最大调整距离
    max_ang = 5.0  #最大调整角度
    #旋转插入参数
    rcs = 0  #参考坐标系，0-工具坐标系，1-基坐标系
    forceInsertion = 2.0 #力或力矩阈值（0~100），单位N或Nm
    orn = 1 #力的方向，1-fz,2-mz
    #默认参数 angVelRot：旋转角速度，单位 °/s  默认 3
    #默认参数 angleMax：最大旋转角度，单位 ° 默认 5
    #默认参数 angAccmax：最大旋转加速度，单位 °/s^2，暂不使用 默认0
    #默认参数 rotorn：旋转方向，1-顺时针，2-逆时针 默认1
    error = robot.MoveL(P,1,0) #笛卡尔空间直线运动至初始点
    print("笛卡尔空间直线运动至初始点",error)
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恒力控制开启错误码",error)
    error = robot.FT_RotInsertion(rcs,1,orn)
    print("旋转插入错误码",error)
    status = 0
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恒力控制关闭错误码",error)

直线插入
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_LinInsertion(rcs, ft, disMax, linorn, lin_v = 1.0, lin_a = 1.0)"
    "描述", "直线插入"
    "参数", "- ``必选参数 rcs``：参考坐标系，0-工具坐标系，1-基坐标系；
    - ``必选参数 ft``：力或力矩阈值 (0~100)，单位 N 或 Nm;
    - ``必选参数 disMax``：最大插入距离，单位 mm;
    - ``必选参数 linorn``：插入方向:0-负方向，1-正方向
    - ``默认参数 lin_v``：直线速度，单位 mm/s 默认1;
    - ``默认参数 lin_a``：直线加速度，单位 mm/s^2，暂不使用 默认0"
    "返回值", "- 成功：[0]
    - 失败：[errcode]"

代码示例
------------
.. code-block:: python
    :linenos:
    
    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    P = [36.794,-675.119, 65.379, -176.938, 2.535, -179.829]
    #恒力参数
    status = 1  #恒力控制开启标志，0-关，1-开
    sensor_num = 1 #力传感器编号
    is_select = [0,0,1,0,0,0]  #六个自由度选择[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
    force_torque = [0.0,0.0,-10.0,0.0,0.0,0.0]  
    gain = [0.0001,0.0,0.0,0.0,0.0,0.0]  #力PID参数，力矩PID参数
    adj_sign = 0  #自适应启停状态，0-关闭，1-开启
    ILC_sign = 0  #ILC控制启停状态，0-停止，1-训练，2-实操
    max_dis = 100.0  #最大调整距离
    max_ang = 5.0  #最大调整角度
    #直线插入参数
    rcs = 0  #参考坐标系，0-工具坐标系，1-基坐标系
    force_goal = 10.0  #力或力矩阈值（0~100），单位N或Nm
    disMax = 100.0 #最大插入距离，单位mm
    linorn = 1 #插入方向，1-正方向，2-负方向
    #默认参数 lin_v：直线速度，单位 mm/s 默认1
    #默认参数 lin_a：直线加速度，单位 mm/s^2，暂不使用 默认0
    error = robot.MoveL(P,1,0) #笛卡尔空间直线运动至初始点
    print("笛卡尔空间直线运动至初始点",error)
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恒力控制开启错误码",error)
    error = robot.FT_LinInsertion(rcs,force_goal,disMax,linorn)
    print("直线插入错误码",error)
    status = 0
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恒力控制关闭错误码",error)

计算中间平面位置开始
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_CalCenterStart()"
    "描述", "计算中间平面位置开始"
    "参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

计算中间平面位置结束
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_CalCenterEnd()"
    "描述", "计算中间平面位置结束"
    "参数", "无"
    "返回值", "错误码 成功-0  失败- errcode
    - 返回值（调用成功返回）pos=[x,y,z,rx,ry,rz]"

表面定位
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_FindSurface (rcs, dir, axis, disMax, ft, lin_v = 3.0, lin_a = 0.0)"
    "描述", "表面定位"
    "参数", "- ``必选参数 rcs``： 参考坐标系，0-工具坐标系，1-基坐标系；
    - ``必选参数 dir``：移动方向，1-正方向，2-负方向；
    - ``必选参数 axis``：移动轴，1-x，2-y，3-z；
    - ``必选参数 disMax``：大探索距离，单位 mm;
    - ``必选参数 ft``：动作终止力阈值，单位N；
    - ``默认参数 lin_v``：探索直线速度，单位mm/s 默认3;
    - ``默认参数 lin_a``：探索直线加速度，单位mm/s^2 默认0;"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    #恒力控制
    status = 1  #恒力控制开启标志，0-关，1-开
    sensor_num = 1 #力传感器编号
    is_select = [1,0,0,0,0,0]  #六个自由度选择[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
    force_torque = [-2.0,0.0,0.0,0.0,0.0,0.0]  
    gain = [0.0002,0.0,0.0,0.0,0.0,0.0]  #力PID参数，力矩PID参数
    adj_sign = 0  #自适应启停状态，0-关闭，1-开启
    ILC_sign = 0  #ILC控制启停状态，0-停止，1-训练，2-实操
    max_dis = 15.0  #最大调整距离
    max_ang = 0.0  #最大调整角度
    #表面定位参数
    rcs = 0 #参考坐标系，0-工具坐标系，1-基坐标系
    direction = 1 #移动方向，1-正方向，2-负方向
    axis = 1 #移动轴，1-X,2-Y,3-Z
    lin_v = 3.0  #探索直线速度，单位mm/s
    lin_a = 0.0  #探索直线加速度，单位mm/s^2
    disMax = 50.0 #最大探索距离，单位mm
    force_goal = 2.0 #动作终止力阈值，单位N
    P1=[-77.24,-679.599,58.328,179.373,-0.028,-167.849]
    Robot.MoveCart(P1,1,0)       #关节空间点到点运动
    #x方向寻找中心
    #第1个表面
    error = robot.FT_CalCenterStart()
    print("计算中间平面开始错误码",error)
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恒力控制开始错误码",error)
    error = robot.FT_FindSurface(rcs,direction,axis,disMax,force_goal)
    print("寻找X+表面错误码",error)
    status = 0
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恒力控制结束错误码",error)
    time.sleep(2)
    error = robot.MoveCart(P1,1,0)       #关节空间点到点运动
    print("关节空间点到点运动错误码",error)
    time.sleep(5)
    #第2个表面
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恒力控制开始错误码",error)
    direction = 2 #移动方向，1-正方向，2-负方向
    error = robot.FT_FindSurface(rcs,direction,axis,disMax,force_goal)
    print("寻找X—表面错误码",error)
    status = 0
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恒力控制结束错误码",error)
    #计算x方向中心位置
    error,xcenter = robot.FT_CalCenterEnd()
    print("计算X方向中间平面结束错误码",xcenter) 
    error = robot.MoveCart(xcenter,1,0)
    print("关节空间点到点运动错误码",error)
    time.sleep(1)
    #y方向寻找中心
    #第1个表面
    error =robot.FT_CalCenterStart()
    print("计算中间平面开始错误码",error)
    error =robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恒力控制开始错误码",error)
    direction = 1 #移动方向，1-正方向，2-负方向
    axis = 2 #移动轴，1-X,2-Y,3-Z
    disMax = 150.0 #最大探索距离，单位mm
    lin_v = 6.0  #探索直线速度，单位mm/s
    error =robot.FT_FindSurface(rcs,direction,axis,disMax,force_goal)
    print("寻找表面Y+错误码",error)
    status = 0
    error =robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恒力控制结束错误码",error)
    error =robot.MoveCart(P1,1,0)       #关节空间点到点运动
    print("关节空间点到点运动错误码",error)
    Robot.WaitMs(1000)
    #第2个表面
    error =robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恒力控制开始错误码",error)
    direction = 2 #移动方向，1-正方向，2-负方向
    error =robot.FT_FindSurface(rcs,direction,axis,disMax,force_goal)
    print("寻找表面Y-错误码",error)
    status = 0
    error =robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恒力控制结束错误码",error)
    #计算y方向中心位置
    error,ycenter=robot.FT_CalCenterEnd()
    print("计算中间平面Y方向结束错误码",ycenter)
    error =robot.MoveCart(ycenter,1,0)
    print("关节空间点到点运动错误码",error)

柔顺控制关闭
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_ComplianceStop()"
    "描述", "柔顺控制关闭"
    "参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

柔顺控制开启
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "FT_ComplianceStart(p,force)"
    "描述", "柔顺控制开启"
    "参数", "- ``必选参数 p``: 位置调节系数或柔顺系数
    - ``必选参数 force``：柔顺开启力阈值，单位N"
    "返回值", "错误码 成功-0  失败- errcode  "

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    J1=[75.005,-46.434,90.687,-133.708,-90.315,-27.139]
    P2=[-77.24,-679.599,38.328,179.373,-0.028,-167.849]
    P3=[77.24,-679.599,38.328,179.373,-0.028,-167.849]
    #恒力控制参数
    status = 1  #恒力控制开启标志，0-关，1-开
    sensor_num = 1 #力传感器编号
    is_select = [1,1,1,0,0,0]  #六个自由度选择[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
    force_torque = [-10.0,-10.0,-10.0,0.0,0.0,0.0] 
    gain = [0.0005,0.0,0.0,0.0,0.0,0.0]  #力PID参数，力矩PID参数
    adj_sign = 0  #自适应启停状态，0-关闭，1-开启
    ILC_sign = 0  #ILC控制启停状态，0-停止，1-训练，2-实操
    max_dis = 1000.0  #最大调整距离
    max_ang = 0.0  #最大调整角度
    error = robot.MoveJ(J1,1,0)
    print("关节空间运动到点1错误码",error)
    #柔顺控制
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恒力控制开始错误码",error)
    p = 0.00005  #位置调节系数或柔顺系数
    force = 30.0 #柔顺开启力阈值，单位N
    error = robot.FT_ComplianceStart(p,force)
    print("柔顺控制开始错误码",error)
    error = robot.MoveL(P2,1,0,vel =10)   #笛卡尔空间直线运动
    print("笛卡尔空间直线运动到点2错误码", error)
    error = robot.MoveL(P3,1,0,vel =10)
    print("笛卡尔空间直线运动到点3错误码", error)
    time.sleep(1)
    error = robot.FT_ComplianceStop()
    print("柔顺控制结束错误码",error)
    status = 0
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恒力控制关闭错误码",error)

