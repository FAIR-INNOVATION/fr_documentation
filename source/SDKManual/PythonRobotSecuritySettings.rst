机器人安全设置
=================

.. toctree:: 
    :maxdepth: 5


设置碰撞等级
+++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAnticollision (mode,level,config)``"
    "描述", "设置碰撞等级"
    "参数", "- ``必选参数 mode``:0-等级，1-百分比；
    - ``必选参数 level=[j1,j2,j3,j4,j5,j6]``:碰撞阈值；
    - ``必选参数 config``:0-不更新配置文件，1-更新配置文件"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    level = [1.0,2.0,3.0,4.0,5.0,6.0]
    error = robot.SetAnticollision(0,level,1)
    print("设置碰撞等级错误码:",error)
    level = [50.0,20.0,30.0,40.0,50.0,60.0]
    error = robot.SetAnticollision(1,level,1)
    print("设置碰撞等级错误码:",error)

设置碰撞后策略
++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetCollisionStrategy (strategy)``"
    "描述", "设置碰撞后策略"
    "参数", "- ``必选参数 strategy``：0-报错暂停，1-继续运行"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    error = robot.SetCollisionStrategy(1)
    print("设置碰撞后策略错误码:",error)

设置正限位
+++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLimitPositive(p_limit)``"
    "描述", "设置正限位"
    "参数", "- ``必选参数 p_limit=[j1,j2,j3,j4,j5,j6]``：六个关节位置"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    p_limit = [170.0,80.0,150.0,80.0,170.0,160.0]
    error = robot.SetLimitPositive(p_limit)
    print("设置正限位错误码:",error)

设置负限位
+++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLimitNegative(n_limit)``"
    "描述", "设置负限位"
    "参数", "- ``必选参数 n_limit=[j1,j2,j3,j4,j5,j6]``：六个关节位置"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    n_limit = [-170.0,-260.0,-150.0,-260.0,-170.0,-160.0]
    error = robot.SetLimitNegative(n_limit)
    print("设置负限位错误码:",error)

错误状态清除
++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ResetAllError()``"
    "描述", "错误状态清除，只能清除可复位的错误"
    "参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    error = robot.ResetAllError()
    print("错误状态清除错误码:",error)

关节摩擦力补偿开关
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FrictionCompensationOnOff(state)``"
    "描述", "关节摩擦力补偿开关"
    "参数", "- ``必选参数 state``：0-关，1-开"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    error = robot.FrictionCompensationOnOff(1)
    print("关节摩擦力补偿开关错误码:",error)

设置关节摩擦力补偿系数-正装
++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetFrictionValue_level(coeff)``"
    "描述", "设置关节摩擦力补偿系数-固定安装-正装"
    "参数", "- ``必选参数 coeff=[j1,j2,j3,j4,j5,j6]``：六个关节补偿系数"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    lcoeff = [0.9,0.9,0.9,0.9,0.9,0.9]
    error = robot.SetFrictionValue_level(lcoeff)
    print("设置关节摩擦力补偿系数-正装错误码:",error)

设置关节摩擦力补偿系数-侧装
++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetFrictionValue_wall(coeff)``"
    "描述", "设置关节摩擦力补偿系数-固定安装-侧装"
    "参数", "- ``必选参数 coeff=[j1,j2,j3,j4,j5,j6]``：六个关节补偿系数"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    wcoeff = [0.4,0.4,0.4,0.4,0.4,0.4]
    error = robot.SetFrictionValue_wall(wcoeff)
    print("设置关节摩擦力补偿系数-侧装错误码:",error)

设置关节摩擦力补偿系数-倒装
++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetFrictionValue_ceiling(coeff)``"
    "描述", "设置关节摩擦力补偿系数-固定安装-倒装"
    "参数", "- ``必选参数 coeff=[j1,j2,j3,j4,j5,j6]``：六个关节补偿系数"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ccoeff = [0.6,0.6,0.6,0.6,0.6,0.6]
    error =robot.SetFrictionValue_ceiling(ccoeff)
    print("设置关节摩擦力补偿系数-倒装错误码:",error)

设置关节摩擦力补偿系数-自由安装
+++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetFrictionValue_freedom(coeff)``"
    "描述", "设置关节摩擦力补偿系数-自由安装"
    "参数", "- ``必选参数 coeff=[j1,j2,j3,j4,j5,j6]``：六个关节补偿系数"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    fcoeff = [0.5,0.5,0.5,0.5,0.5,0.5]
    error =robot.SetFrictionValue_freedom(fcoeff)
    print("设置关节摩擦力补偿系数-自由装错误码:",error)