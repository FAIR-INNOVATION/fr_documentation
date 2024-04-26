扩展轴
=============

.. toctree:: 
    :maxdepth: 5

设置485扩展轴参数
+++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetParam(servoId,servoCompany,servoModel,servoSoftVersion, servoResolution,axisMechTransRatio)``"
    "描述", "设置485扩展轴参数"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``servoCompany``：伺服驱动器厂商，1-戴纳泰克；
    - ``servoModel``：伺服驱动器型号，1-FD100-750C；
    - ``servoSoftVersion``：伺服驱动器软件版本，1-V1.0；
    - ``servoResolution``：编码器分辨率；
    - ``axisMechTransRatio``：机械传动比；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
-------------

.. code-block:: python
    :linenos:

    from time import sleep
    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    ret = robot = Robot.RPC('192.168.58.2')

    ret =robot.AuxServoSetParam(1,1,1,1,131072,15.45)#设置485扩展轴参数
    print("AuxServoSetParam",ret)
    sleep(1)

    ret =robot.AuxServoGetParam(1)#获取485扩展轴配置参数
    print("AuxServoGetParam",ret)
    sleep(1)

    ret =robot.AuxServoGetStatus(1)#查询状态
    print("AuxServoGetStatus",ret)
    sleep(1)

    ret =robot.AuxServoClearError(1)#清除错误
    print("AuxServoClearError",ret)
    sleep(1)

获取485扩展轴配置参数
+++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoGetParam(servoId)``"
    "描述", "获取485扩展轴配置参数"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode;
    - ``servoCompany``：伺服驱动器厂商，1-戴纳泰克；
    - ``servoModel``：伺服驱动器型号，1-FD100-750C；
    - ``servoSoftVersion``：伺服驱动器软件版本，1-V1.0；
    - ``servoResolution``：编码器分辨率；
    - ``axisMechTransRatio``：机械传动比；"

代码示例
-----------
参考设置485扩展轴参数的代码示例

设置485扩展轴使能/去使能
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoEnable(servoId,status)``"
    "描述", "设置485扩展轴使能/去使能"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``status``：使能状态，0-去使能， 1-使能;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
-------------

.. code-block:: python
    :linenos:

    from time import sleep
    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    ret = robot = Robot.RPC('192.168.58.2')
    ret =robot.AuxServoEnable(1,0)#修改控制模式前需去使能
    print("AuxServoEnable(0)",ret)
    sleep(3)

    ret =robot.AuxServoSetControlMode(1,0)#设置为位置模式
    print("AuxServoSetControlMode",ret)
    sleep(3)

    ret =robot.AuxServoEnable(1,1)#修改控制模式后需使能
    print("AuxServoEnable(1)",ret)
    sleep(3)

    ret =robot.AuxServoHoming(1,1,10,10)#回零
    print("AuxServoHoming",ret)
    sleep(5)

    ret =robot.AuxServoGetStatus(1)#查询状态
    print("AuxServoGetStatus",ret)
    sleep(1)
    i=1
    while(i<5):
        ret =robot.AuxServoSetTargetPos(1,300*i,30)#位置模式运动，速度30
        print("AuxServoSetTargetPos",ret)
        sleep(11)
        ret =robot.AuxServoGetStatus(1)#查询状态
        print("AuxServoGetStatus",ret)
        sleep(1)
        i=i+1

设置485扩展轴控制模式
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetControlMode(servoId,mode)``"
    "描述", "设置485扩展轴控制模式"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``mode``：控制模式，0-位置模式，1-速度模式;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
---------------------------------
参考设置485扩展轴使能/去使能的代码示例

设置485扩展轴目标位置(位置模式)
++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetTargetPos(servoId,pos,speed)``"
    "描述", "设置485扩展轴目标位置(位置模式)"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``pos``：目标位置，mm或°；
    - ``speed``：目标速度，mm/s或°/s;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
---------------------------------
参考设置485扩展轴使能/去使能的代码示例

设置485扩展轴目标速度(速度模式)
+++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetTargetSpeed(servoId,speed)``"
    "描述", "设置485扩展轴目标速度(速度模式)"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``speed``：目标速度，mm/s或°/s;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
-------------

.. code-block:: python
    :linenos:

    from time import sleep
    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    ret = robot = Robot.RPC('192.168.58.2')
    ret =robot.AuxServoEnable(1,0)#修改控制模式前需去使能
    print("AuxServoEnable(0)",ret)
    sleep(3)

    ret = robot.AuxServoSetControlMode(1, 1)  # 设置为速度模式
    print("AuxServoSetControlMode",ret)
    sleep(3)

    ret =robot.AuxServoEnable(1,1)#修改控制模式后需使能
    print("AuxServoEnable(1)",ret)
    sleep(3)

    ret =robot.AuxServoHoming(1,1,10,10)#回零
    print("AuxServoHoming",ret)
    sleep(5)

    ret =robot.AuxServoGetStatus(1)#查询状态
    print("AuxServoGetStatus",ret)
    sleep(1)

    ret = robot.AuxServoSetTargetSpeed(1, 30)  # 速度模式运动，速度30
    print("AuxServoSetTargetSpeed", ret)
    sleep(10)

    ret = robot.AuxServoGetStatus(1)  # 查询状态
    print("AuxServoGetStatus", ret)
    sleep(1)

    ret = robot.AuxServoSetTargetSpeed(1, 60)  # 速度模式运动，速度60
    print("AuxServoSetTargetSpeed", ret)
    sleep(10)
    ret = robot.AuxServoGetStatus(1)  # 查询状态
    print("AuxServoGetStatus", ret)
    sleep(1)

    ret = robot.AuxServoSetTargetSpeed(1, 0)  # 结束速度模式运动前应当把速度设为0
    print("AuxServoSetTargetSpeed", ret)
    sleep(3)
    ret = robot.AuxServoGetStatus(1)  # 查询状态
    print("AuxServoGetStatus", ret)
    sleep(1)

设置485扩展轴目标转矩(力矩模式)-暂未开放
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetTargetTorque(servoId,torque)``"
    "描述", "设置485扩展轴目标转矩(力矩模式)"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``torque``：目标力矩，Nm;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置485扩展轴回零
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoHoming(servoId,mode,searchVel,latchVel)``"
    "描述", "设置485扩展轴回零"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``mode``：回零模式，1-当前位置回零；2-负限位回零；3-正限位回零;
    - ``searchVel``： 回零速度，mm/s或°/s;
    - ``latchVel``：箍位速度，mm/s或°/s;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
代码示例
---------------------------------
参考设置485扩展轴使能/去使能的代码示例

清除485扩展轴错误信息
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoClearError(servoId)``"
    "描述", "清除485扩展轴错误信息"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
代码示例
---------------------------------
参考设置485扩展轴参数的代码示例

获取485扩展轴伺服状态
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoGetStatus(servoId)``"
    "描述", "获取485扩展轴伺服状态"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode;
    - ``servoErrCode``：（调用成功返回）伺服驱动器故障码
    - ``servoState``：（调用成功返回）伺服驱动器状态 bit0:0-未使能；1-使能;  bit1:0-未运动；1-正在运动;  bit2 0-正限位未触发；1-正限位触发；bit3 0-负限位未触发；1-负限位触发；bit4 0-未定位完成；1-定位完成；  bit5：0-未回零；1-回零完成；
    - ``servoPos``：（调用成功返回）伺服当前位置 mm或°；
    - ``servoSpeed``：（调用成功返回）伺服当前速度 mm/s或°/s；
    - ``servoTorque``：（调用成功返回）伺服当前转矩Nm；"

代码示例
---------------------------------
参考设置485扩展轴使能/去使能的代码示例

设置状态反馈中485扩展轴数据轴号-暂未开放
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServosetStatusID(servoId)``"
    "描述", "设置状态反馈中485扩展轴数据轴号"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"