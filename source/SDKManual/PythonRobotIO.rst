机器人IO
============

.. toctree:: 
    :maxdepth: 5

设置控制箱数字量输出
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetDO(id, status, smooth = 0, block = 0)``"
    "描述", "设置控制箱数字量输出"
    "参数", "-  ``必选参数 id``:io编号，范围[0~15]；
    - ``必选参数 status``:0-关，1-开；
    - ``默认参数 smooth``:0-不平滑，1-平滑 默认0;
    - ``默认参数 block``:0-阻塞，1-非阻塞 默认0"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    # 测试控制箱DO
    for i in range(0,16):
        error = robot.SetDO(i,1)      #打开控制箱DO
    time.sleep(1)
    for i in range(0,16):
        robot.SetDO(i,0)      #关闭控制箱DO

设置工具数字量输出
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolDO (id, status, smooth = 0, block = 0)``"
    "描述", "设置工具数字量输出"
    "参数", "-  ``必选参数 id``:io编号，范围[0~1]；
    - ``必选参数 status``:0-关，1-开；
    - ``默认参数 smooth``:0-不平滑，1-平滑；
    - ``默认参数 block``:0-阻塞，1-非阻塞。"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    # 测试工具DO
    error_tooldo = 0
    for i in range(0,2):
        error = robot.SetToolDO(i,1)    #打开工具DO
    robot.WaitMs(1000)
    for i in range(0,2):
        error = robot.SetToolDO(i,0)    #关闭工具DO


设置控制箱模拟量输出
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAO(id,value,block = 0)``"
    "描述", "设置控制箱模拟量输出"
    "参数", "- ``必选参数 id``:io编号，范围[0~1]；
    - ``必选参数 value``:电流或电压值百分比，范围[0~100%]对应电流值[0~20mA]或电压[0~10V]；
    - ``默认参数 block``:[0]-阻塞，[1]-非阻塞 默认0"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    # 测试控制箱AO
    error = robot.SetAO(0,100.0)
    print("设置AO0错误码:", error)
    error = robot.SetAO(1,100.0)
    print("设置AO1错误码:", error)

设置工具模拟量输出
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolAO(id,value,block = 0)``"
    "描述", "设置工具模拟量输出"
    "参数", "- ``必选参数 id``:io编号，范围[0]；
    - ``必选参数 value``:电流或电压值百分比，范围[0~100%]对应电流值[0~20mA]或电压[0~10V]；
    - ``默认参数 block``:[0]-阻塞，[1]-非阻塞 默认0"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    # 测试末端AO
    error = robot.SetToolAO(0,100.0)
    print("设置ToolAO0错误码:", error)
    Robot.WaitMs(1000)
    error = robot.SetToolAO(0,0.0)
    print("设置ToolAO0错误码:", error)

获取控制箱数字量输入
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDI(id, block = 0)``"
    "描述", "获取控制箱数字量输入"
    "参数", "- ``必选参数 id``:io编号，范围[0~15]；
    - ``默认参数 block``:0-阻塞，1-非阻塞 默认0"
    "返回值", "错误码 成功-0  失败- errcode
    - 返回值（调用成功返回）di: 0-低电平，1-高电平"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    error = robot.GetDI(0,0)
    print("获取DI0",error)

获取工具数字量输入
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetToolDI(id, block = 0)``"
    "描述", "获取工具数字量输入"
    "参数", "- ``必选参数 id``:io编号，范围[0~1]；
    - ``默认参数 block``:0-阻塞，1-非阻塞 默认0"
    "返回值", "错误码 成功-0  失败- errcode
    - 返回值（调用成功返回）di: 0-低电平，1-高电平"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    tool_di = robot.GetToolDI(1,0)
    print("获取ToolDI",tool_di)

等待控制箱数字量输入
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitDI(id,status,maxtime,opt)``"
    "描述", "等待控制箱数字量输入"
    "参数", "- ``必选参数 id``:io编号，范围[0~15]；
    - ``必选参数 status``:0-关，1-开；
    - ``必选参数 maxtime``:最大等待时间，单位[ms]；
    - ``必选参数 opt``:超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    max_waittime = 2000
    #等待控制箱DI
    error = robot.WaitDI(0,1,max_waittime,0)
    print("WaitDI错误码",error)

等待控制箱多路数字量输入
++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitMultiDI(mode,id,status,maxtime,opt)``"
    "描述", "等待控制箱多路数字量输入"
    "参数", "- ``必选参数 mode``:[0]-多路与，[1]-多路或；
    - ``必选参数 id``:io编号，bit0~bit7对应DI0~DI7，bit8~bit15对应CI0~CI7；
    - ``必选参数 status``:bit0~bit7对应DI0~DI7状态，bit8~bit15对应CI0~CI7状态位的状态[0]-关，[1]-开；
    - ``必选参数 maxtime``:最大等待时间，单位[ms]；
    - ``必选参数 opt``:超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待。"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    max_waittime = 2000
    #等待控制箱多路DI
    error = robot.WaitMultiDI(1,3,1,max_waittime,0)
    print("WaitMultiDI错误码",error)

等待工具数字量输入
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitToolDI(id,status,maxtime,opt)``"
    "描述", "等待末端数字量输入"
    "参数", "- ``必选参数 id``:io编号，范围[0~1]；
    - ``必选参数 status``:0-关，1-开；
    - ``必选参数 maxtime``:最大等待时间，单位[ms]；
    - ``必选参数 opt``:超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    max_waittime = 2000
    #等待工具DI
    error = robot.WaitToolDI(1,1,max_waittime,0)
    print("WaitToolDI错误码",error)

获取控制箱模拟量输入
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAI(id, block = 0)``"
    "描述", "获取控制箱模拟量输入"
    "参数", "- ``必选参数 id``:io编号，范围[0~1]；
    - ``默认参数 block``:0-阻塞，1-非阻塞 默认0 "
    "返回值", "错误码 成功-0  失败- errcode
    - 返回值（调用成功返回）value: 输入电流或电压值百分比，范围 [0~100] 对应电流值 [0~20mA] 或电压 [0~10V]"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    error = robot.GetAI(0)
    print("获取AI0",error)

获取工具模拟量输入
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetToolAI (id, block = 0)``"
    "描述", "获取末端模拟量输入"
    "参数", "- ``必选参数 id``:io编号，范围[0]；
    - ``默认参数 block``:0-阻塞，1-非阻塞 默认0"
    "返回值", "错误码 成功-0  失败- errcode
    - 返回值（调用成功返回）value: 输入电流或电压值百分比，范围 [0~100] 对应电流值 [0~20mA] 或电压 [0~10V]"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    error = robot.GetToolAI(0)
    print("获取ToolAI0",error)

等待控制箱模拟量输入
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitAI(id,sign,value,maxtime,opt)``"
    "描述", "等待控制箱模拟量输入"
    "参数", "- ``必选参数 id``:io编号，范围[0~1]；
    - ``必选参数 sign``:0-大于，1-小于
    - ``必选参数 value``:输入电流或电压值百分比，范围[0~100]对应电流值[0~20mA]或电压[0~10V]；
    - ``必选参数 maxtime``:最大等待时间，单位[ms]；
    - ``必选参数 opt``:超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    max_waittime = 2000
    #等待控制箱AI
    error = robot.WaitAI(0,0,50,max_waittime,1)         #忽略超时提示程序继续执行
    print("WaitAI错误码",error)

等待工具模拟量输入
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitToolAI(id,sign,value,maxtime,opt)``"
    "描述", "等待末端模拟量输入"
    "参数", "- ``必选参数 id``:io编号，范围[0]；
    - ``必选参数 sign``:0-大于，1-小于
    - ``必选参数 value``:输入电流或电压值百分比，范围[0~100]对应电流值[0~20mA]或电压[0~10V]；
    - ``必选参数 maxtime``:最大等待时间，单位[ms]；
    - `必选参数 `opt``:超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    max_waittime = 2000
    #等待工具AI
    error = robot.WaitToolAI(0,0,50,max_waittime,0)
    print("WaitToolAI错误码",error)
