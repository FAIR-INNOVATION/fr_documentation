焊接
======================

.. toctree:: 
    :maxdepth: 5

焊接开始
++++++++++++++++++++++++++++++++++
.. versionadded:: python sdk-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "ARCStart(ioType, arcNum, timeout)"
    "描述", "焊接开始"
    "必选参数", "- ``ioType``：io类型 0-控制器IO； 1-扩展IO
    - ``arcNum``： 焊机配置文件编号
    - ``timeout``： 起弧超时时间"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')

    weldIOType =0
    arcNum =0
    weldTimeout=5000
    #起弧
    ret = robot.ARCStart(weldIOType,arcNum,weldTimeout)
    print("ARCStart错误码", ret)
    time.sleep(3)

焊接结束
++++++++++++++++++++++++++++++++++
.. versionadded:: python sdk-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "ARCEnd(ioType, arcNum, timeout)"
    "描述", "焊接结束"
    "必选参数", "- ``ioType``： 类型 0-控制器IO； 1-扩展IO
    - ``arcNum``： 焊机配置文件编号
    - ``timeout``： 起弧超时时间"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')

    weldIOType =0
    arcNum =0
    weldTimeout=5000
    #收弧
    ret = robot.ARCEnd(weldIOType,arcNum,weldTimeout)
    print("ARCEnd错误码", ret)
    time.sleep(3)

设置焊接电流与输出模拟量对应关系
++++++++++++++++++++++++++++++++++
.. versionadded:: python sdk-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "WeldingSetCurrentRelation(currentMin, currentMax, outputVoltageMin, outputVoltageMax)"
    "描述", "设置焊接电流与输出模拟量对应关系"
    "必选参数", "- ``currentMin``： 焊接电流-模拟量输出线性关系左侧点电流值(A)
    - ``currentMax``：  焊接电流-模拟量输出线性关系右侧点电流值(A)
    - ``outputVoltageMin``： 焊接电流-模拟量输出线性关系左侧点模拟量输出电压值(V)
    - ``outputVoltageMax``：焊接电流-模拟量输出线性关系右侧点模拟量输出电压值(V)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    weldIOType =0

    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    #设置焊接电流与模拟量线性关系
    ret = robot.WeldingSetCurrentRelation(0,400,0,10)
    print("WeldingSetCurrentRelation错误码", ret)
    time.sleep(1)
    #获取焊接电流与模拟量线性关系
    ret = robot.WeldingGetCurrentRelation()
    print("WeldingGetCurrentRelation错误码", ret)
    time.sleep(1)

    #设置焊接电压与模拟量线性关系
    ret = robot.WeldingSetVoltageRelation(0,400,0,10)
    print("WeldingSetVoltageRelation错误码", ret)
    time.sleep(1)
    #获取焊接电压与模拟量线性关系
    ret = robot.WeldingGetVoltageRelation()
    print("WeldingGetVoltageRelation错误码", ret)
    time.sleep(1)

    #设置焊接电流
    ret = robot.WeldingSetCurrent(weldIOType,100,0)
    print("WeldingSetCurrent错误码", ret)
    time.sleep(1)

    #设置焊接电压
    ret = robot.WeldingSetVoltage(weldIOType,19,1)
    print("WeldingSetVoltage错误码", ret)
    time.sleep(1)

设置焊接电压与输出模拟量对应关系
++++++++++++++++++++++++++++++++++
.. versionadded:: python sdk-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "WeldingSetVoltageRelation(weldVoltageMin, weldVoltageMax, outputVoltageMin, outputVoltageMax)"
    "描述", "设置焊接电压与输出模拟量对应关系"
    "必选参数", "- ``weldVoltageMin``： 焊接电压-模拟量输出线性关系左侧点焊接电压值(A)
    - ``weldVoltageMax``：  焊接电压-模拟量输出线性关系右侧点焊接电压值(A)
    - ``outputVoltageMin``： 焊接电压-模拟量输出线性关系左侧点模拟量输出电压值(V)
    - ``outputVoltageMax``：焊接电压-模拟量输出线性关系右侧点模拟量输出电压值(V)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取焊接电流与输出模拟量对应关系
++++++++++++++++++++++++++++++++++
.. versionadded:: python sdk-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "WeldingGetCurrentRelation()"
    "描述", "获取焊接电流与输出模拟量对应关系"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - Return:（if success）currentMin，currentMax，outputVoltageMin，outputVoltageMax
    - currentMin 焊接电流-模拟量输出线性关系左侧点电流值(A)
    - currentMax 焊接电流-模拟量输出线性关系右侧点电流值(A)
    - outputVoltageMin 焊接电流-模拟量输出线性关系左侧点模拟量输出电压值(V)
    - outputVoltageMax 焊接电流-模拟量输出线性关系右侧点模拟量输出电压值(V)"

获取焊接电压与输出模拟量对应关系
++++++++++++++++++++++++++++++++++
.. versionadded:: python sdk-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "WeldingGetVoltageRelation()"
    "描述", "获取焊接电压与输出模拟量对应关系"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - Return:（if success）weldVoltageMin,weldVoltageMax,outputVoltageMin, outputVoltageMax, weldVoltageMin 
    - weldVoltageMin 焊接电压-模拟输出线性关系左点焊电压值(V)
    - weldVoltageMax  焊接电压-模拟量输出线性关系右侧点焊接电压值(V)
    - outputVoltageMin  焊接电压-模拟量输出线性关系左侧点模拟量输出电压值(V)
    - outputVoltageMax  焊接电流-模拟量输出线性关系右侧点模拟量输出电压值(V)"

设置焊接电流
++++++++++++++++++++++++++++++++++
.. versionadded:: python sdk-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "WeldingSetCurrent(ioType,current, AOIndex)"
    "描述", "设置焊接电流"
    "必选参数", "- ``ioType``： 类型 0-控制器IO； 1-扩展IO
    - ``current``： 焊接电流值(A)
    - ``AOIndex``： 焊接电流控制箱模拟量输出端口(0-1)"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

设置焊接电压
++++++++++++++++++++++++++++++++++
.. versionadded:: python sdk-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "WeldingSetVoltage(ioType,voltage, AOIndex)"
    "描述", "设置焊接电压"
    "必选参数", "- ``ioType``： 类型 0-控制器IO； 1-扩展IO
    - ``voltage``： 焊接电压值(V)
    - ``AOIndex``： 焊接电流控制箱模拟量输出端口(0-1)"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

设置摆动参数
++++++++++++++++++++++++++++++++++
.. versionadded:: python sdk-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "WeaveSetPara(weaveNum, weaveType, weaveFrequency, weaveIncStayTime, weaveRange, weaveLeftStayTime, weaveRightStayTime, weaveCircleRadio, weaveStationary)"
    "描述", "设置摆动参数"
    "必选参数", "- ``weaveNum``： 摆焊参数配置编号
    - ``weaveType``： 摆动类型 0-平面三角波摆动；1-垂直L型三角波摆动；2-顺时针圆形摆动；3-逆时针圆形摆动；4-平面正弦波摆动；5-垂直L型正弦波摆动；6-垂直三角波摆动；7-垂直正弦波摆动
    - ``weaveFrequency``： 摆动频率(Hz)
    - ``weaveIncStayTime``： 等待模式 0-周期不包含等待时间；1-周期包含等待时间必选参数
    - ``weaveRange``： 摆动幅度(mm)
    - ``weaveLeftStayTime``： 摆动左停留时间(ms)
    - ``weaveRightStayTime``：  摆动右停留时间(ms)
    - ``weaveCircleRadio``： 圆形摆动-回调比率(0-100%)
    - ``weaveStationary``： 摆动位置等待，0-等待时间内位置继续移动；1-等待时间内位置静止"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    weaveNum =0
    weaveType = 0
    weaveFraquency = 1
    weavelncStayTime = 0
    weaveRange = 10
    weaveLeftStayTime = 10
    weaveRightStayTime = 10
    weaveCircleRadio =0
    weaveStationary =1
    #设置摆动参数
    ret = robot.WeaveSetPara(weaveNum,weaveType,weaveFraquency,weavelncStayTime,weaveRange,weaveLeftStayTime,weaveRightStayTime,weaveCircleRadio,weaveStationary)
    print("WeaveSetPara ", ret)
    time.sleep(1)

    #摆动开始
    ret = robot.WeaveStart(0)
    print("WeaveStart ", ret)
    time.sleep(1)
    ret,pose =robot.GetActualTCPPose(1);
    print(ret,pose)
    pose[2]=pose[2]+50
    ret = robot.MoveL(pose,tool,user)
    print("MoveL ", ret)
    time.sleep(1)
    #即时设置摆动参数
    ret = robot.WeaveOnlineSetPara (weaveNum,weaveType,weaveFraquency,weavelncStayTime,weaveRange,weaveLeftStayTime,weaveRightStayTime,weaveCircleRadio,weaveStationary)
    print("WeaveOnlineSetPara ", ret)
    time.sleep(1)
    #摆动结束
    ret = robot.WeaveEnd(0)
    print("WeaveEnd ", ret)
    time.sleep(1)

即时设置摆动参数
++++++++++++++++++++++++++++++++++
.. versionadded:: python sdk-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "WeaveOnlineSetPara (weaveNum, weaveType, weaveFrequency, weaveIncStayTime, weaveRange, weaveLeftStayTime, weaveRightStayTime, weaveCircleRadio, weaveStationary)"
    "描述", "即时设置摆动参数"
    "必选参数", "- ``weaveNum``： 摆焊参数配置编号
    - ``weaveType``： 摆动类型 0-平面三角波摆动；1-垂直L型三角波摆动；2-顺时针圆形摆动；3-逆时针圆形摆动；4-平面正弦波摆动；5-垂直L型正弦波摆动；6-垂直三角波摆动；7-垂直正弦波摆动
    - ``weaveFrequency``： 摆动频率(Hz)
    - ``weaveIncStayTime``： 等待模式 0-周期不包含等待时间；1-周期包含等待时间必选参数
    - ``weaveRange``： 摆动幅度(mm)
    - ``weaveLeftStayTime``： 摆动左停留时间(ms)
    - ``weaveRightStayTime``：  摆动右停留时间(ms)
    - ``weaveCircleRadio``： 圆形摆动-回调比率(0-100%)
    - ``weaveStationary``： 摆动位置等待，0-等待时间内位置继续移动；1-等待时间内位置静止"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

摆动开始
++++++++++++++++++++++++++++++++++
.. versionadded:: python sdk-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "WeaveStart(weaveNum)"
    "描述", "摆动开始"
    "必选参数", "- ``weaveNum``： 类型 0-控制器IO； 1-扩展IO"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

摆动结束
++++++++++++++++++++++++++++++++++
.. versionadded:: python sdk-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "WeaveEnd(weaveNum)"
    "描述", "摆动结束"
    "必选参数", "- ``weaveNum``： 摆焊参数配置编号"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

正向送丝
++++++++++++++++++++++++++++++++++
.. versionadded:: python sdk-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "SetForwardWireFeed(ioType, wireFeed)"
    "描述", "正向送丝"
    "必选参数", "- ``ioType``： 0-控制器IO；1-扩展IO
    - ``wireFeed``： 送丝控制  0-停止送丝；1-送丝"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')

    weldIOType =0
    #正向送丝
    ret = robot.SetForwardWireFeed(weldIOType,1)
    print("SetForwardWireFeed错误码", ret)
    time.sleep(1)
    ret = robot.SetForwardWireFeed(weldIOType,0)
    print("SetForwardWireFeed错误码", ret)
    time.sleep(1)

    #反向送丝
    ret = robot.SetReverseWireFeed(weldIOType,1)
    print("SetReverseWireFeed错误码", ret)
    time.sleep(1)
    #停止反向送丝
    ret = robot.SetReverseWireFeed(weldIOType,0)
    print("SetReverseWireFeed错误码", ret)
    time.sleep(1)

    #送气
    ret = robot.SetAspirated(weldIOType,1)
    print("SetAspirated错误码", ret)
    time.sleep(1)
    #停止送气
    ret = robot.SetAspirated(weldIOType,0)
    print("SetAspirated错误码", ret)
    time.sleep(1)

反向送丝
++++++++++++++++++++++++++++++++++
.. versionadded:: python sdk-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "SetReverseWireFeed(ioType, wireFeed)"
    "描述", "反向送丝"
    "必选参数", "- ``ioType``： 0-控制器IO；1-扩展IO
    - ``wireFeed``： 送丝控制  0-停止送丝；1-送丝"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

送气
++++++++++++++++++++++++++++++++++
.. versionadded:: python sdk-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "SetAspirated(ioType, airControl)"
    "描述", "送气"
    "必选参数", "- ``ioType``： 0-控制器IO；1-扩展IO
    - ``airControl``： 送气控制  0-停止送气；1-送气"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode"

分段焊接启动
++++++++++++++++++++++++++++++++++
.. versionadded:: python sdk-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "SegmentWeldStart(startDesePos,  endDesePos, startJPos, endJPos, weldLength, noWeldLength, weldIOType, arcNum, weldTimeout, isWeave,weaveNum,tool,user,vel=20.0, acc=0.0, ovl=100.0, blendR=-1.0,exaxis_pos=[0.0, 0.0, 0.0, 0.0],  search=0, offset_flag=0, offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0])"
    "描述", "分段焊接启动"
    "必选参数", "- ``startDesePos``： 初始笛卡尔位姿，单位 [mm][°]
    - ``endDesePos``： 目标笛卡尔位姿，单位 [mm][°]
    - ``startJPos``：初始关节位置，单位 [°] 
    - ``endJPos``：目标关节位置，单位 [°]  
    - ``weldLength``：焊接长度，单位 [mm] 
    - ``noWeldLength``：非焊接长度，单位 [mm] 
    - ``weldIOType``：焊接IO类型(0-控制箱IO；1-扩展IO) arcNum 焊机配置文件编号 
    - ``timeout``：熄弧超时时间 
    - ``isWeave``：焊接 False-不焊接 
    - ``weaveNum``：摆焊参数配置编号 
    - ``tool``：工具号，[0~14]
    - ``user``：工件号，[0~14]"
    "默认参数", "- ``vel``：速度百分比，[0~100] 默认20.0
    - ``acc``：加速度[0~100] 暂不开放 默认0.0
    - ``ovl``：速度缩放因子，[0~100] 默认100.0
    - ``blendR``：[-1.0]-运动到位 (阻塞)，[0~1000]-平滑半径 (非阻塞)，单位 [mm] 默认-1.0
    - ``exaxis_pos``：外部轴 1 位置 ~ 外部轴 4 位置 默认[0.0,0.0,0.0,0.0]
    - ``search``：[0]-不焊丝寻位，[1]-焊丝寻位
    - ``offset_flag``：[0]-不偏移，[1]-工件/基坐标系下偏移，[2]-工具坐标系下偏移 默认 0
    - ``offset_pos``：位姿偏移量，单位 [mm][°] 默认[0.0,0.0,0.0,0.0,0.0,0.0]"
    "返回值", "- 错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')

    weldIOType =0
    arcNum =0
    weldTimeout=5000
    weaveNum =0
    tool =1
    user =0
    weaveType = 0
    weaveFraquency = 1
    weavelncStayTime = 0
    weaveRange = 10
    weaveLeftStayTime = 10
    weaveRightStayTime = 10
    weaveCircleRadio =0
    weaveStationary =1
    start_desc=[0,0,0,0,0,0]
    end_desc=[0,0,0,0,0,0]
    start_joint=[0,0,0,0,0,0]
    end_joint=[0,0,0,0,0,0]
    ret,start_desc =robot.GetActualTCPPose(1);
    print("start_desc",start_desc)
    ret,end_desc =robot.GetActualTCPPose(1);
    end_desc[1]=end_desc[1]+200
    print("start_desc",start_desc)
    print("end_desc",end_desc)
    ret,start_joint=robot.GetInverseKin(0,start_desc)
    ret,end_joint=robot.GetInverseKin(0,end_desc)
    print("start_joint",start_joint)
    print("end_joint",end_joint)
    weldLength =40
    noweldLength =40
    #段焊

    ret = robot.SegmentWeldStart(start_desc,end_desc,start_joint,end_joint,weldLength,noweldLength,weldIOType,arcNum,weldTimeout,True,weaveNum,tool,user)
    print("SegmentWeldStart", ret)