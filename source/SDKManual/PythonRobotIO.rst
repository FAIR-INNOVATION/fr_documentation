机器人IO
============

.. toctree:: 
    :maxdepth: 5

设置控制箱数字量输出
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetDO(id, status, smooth=0, block=0)``"
    "描述", "设置控制箱数字量输出"
    "必选参数", "-  ``id``:io编号，范围[0~15]；
    - ``status``:0-关，1-开；"
    "默认参数", "- ``smooth``:0-不平滑，1-平滑 默认0;
    - ``block``:0-阻塞，1-非阻塞 默认0"
    "返回值", "错误码 成功-0  失败- errcode"

设置工具数字量输出
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolDO (id, status, smooth=0, block=0)``"
    "描述", "设置工具数字量输出"
    "必选参数", "-  ``id``:io编号，范围[0~1]；
    - ``status``:0-关，1-开；"
    "默认参数", "- ``smooth``:0-不平滑，1-平滑；
    - ``block``:0-阻塞，1-非阻塞。"
    "返回值", "错误码 成功-0  失败- errcode"

设置控制箱模拟量输出
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAO(id,value,block=0)``"
    "描述", "设置控制箱模拟量输出"
    "必选参数", "- ``id``:io编号，范围[0~1]；
    - ``value``:电流或电压值百分比，范围[0~100%]对应电流值[0~20mA]或电压[0~10V]；"
    "默认参数", "- ``block``:[0]-阻塞，[1]-非阻塞 默认0"
    "返回值", "错误码 成功-0  失败- errcode"

设置工具模拟量输出
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolAO(id,value,block=0)``"
    "描述", "设置工具模拟量输出"
    "必选参数", "- ``id``:io编号，范围[0]；
    - ``value``:电流或电压值百分比，范围[0~100%]对应电流值[0~20mA]或电压[0~10V]；"
    "默认参数", "- ``block``:[0]-阻塞，[1]-非阻塞 默认0"
    "返回值", "错误码 成功-0  失败- errcode"

设置数字量、模拟量输出代码示例
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    status = 1
    smooth = 0  
    block = 0 
    for i in range(16):
        robot.SetDO(i, status, smooth, block)
        time.sleep(0.3) 
    status = 0 
    for i in range(16):
        robot.SetDO(i, status, smooth, block)
        time.sleep(0.3)
    status = 1
    for i in range(2):
        robot.SetToolDO(i, status, smooth, block)
        time.sleep(1) 
    status = 0 
    for i in range(2):
        robot.SetToolDO(i, status, smooth, block)
        time.sleep(1)
    for i in range(100):
        robot.SetAO(0, i, block)
        time.sleep(0.03)
    for i in range(100):
        robot.SetToolAO(0, i, block)
        time.sleep(0.03)
    robot.CloseRPC()

获取控制箱数字量输入
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDI(id, block=0)``"
    "描述", "获取控制箱数字量输入"
    "必选参数", "- ``id``:io编号，范围[0~15]；"
    "默认参数", "- ``block``:0-阻塞，1-非阻塞 默认0"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``di``: 0-低电平，1-高电平"

获取工具数字量输入
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetToolDI(id, block=0)``"
    "描述", "获取工具数字量输入"
    "必选参数", "- ``id``:io编号，范围[0~1]；"
    "默认参数", "- ``block``:0-阻塞，1-非阻塞 默认0"
    "返回值", "错误码 成功-0  失败- errcode
    - ``di``: 0-低电平，1-高电平"

获取控制箱模拟量输入
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAI(id, block = 0)``"
    "描述", "获取控制箱模拟量输入"
    "必选参数", "- ``id``:io编号，范围[0~1]；"
    "默认参数", "- ``block``:0-阻塞，1-非阻塞 默认0 "
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``value``: 输入电流或电压值百分比，范围 [0~100] 对应电流值 [0~20mA] 或电压 [0~10V]"

获取工具模拟量输入
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetToolAI(id, block = 0)``"
    "描述", "获取末端模拟量输入"
    "必选参数", "- ``id``:io编号，范围[0]；"
    "默认参数", "- ``block``:0-阻塞，1-非阻塞 默认0"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``value``: 输入电流或电压值百分比，范围 [0~100] 对应电流值 [0~20mA] 或电压 [0~10V]"

获取机器人末端点记录按钮状态
++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxlePointRecordBtnState()``"
    "描述", "获取机器人末端点记录按钮状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``buttonstatus``: 按钮状态，0-按下，1-松开"

获取机器人末端DO输出状态
++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetToolDO()``"
    "描述", "获取机器人末端DO输出状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``do_state``: DO输出状态，do0~do1对应bit1~bit2,从bit0开始"

获取机器人控制器DO输出状态
++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDO()``"
    "描述", "获取机器人控制器DO输出状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``do_state_h``: DO输出状态，co0~co7对应bit0~bit7 do_state_l DO输出状态，do0~do7对应bit0~bit7"

获取机器人DI、DO状态代码示例
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    block = 0 
    error,di = robot.GetDI(0, block)
    print(f"di0: {di}")
    error,tool_di = robot.GetToolDI(1, block)
    print(f"tool_di1: {tool_di}")
    error,ai = robot.GetAI(0, block)
    print(f"ai0: {ai:.2f}") 
    error,tool_ai = robot.GetToolAI(0, block)
    print(f"tool_ai0: {tool_ai:.2f}")
    error,button_state = robot.GetAxlePointRecordBtnState()
    print(f"_button_state is: {button_state}")
    error,tool_do_state = robot.GetToolDO()
    print(f"tool DO state: {tool_do_state}")
    error,[do_state_h, do_state_l] = robot.GetDO()
    print(f"DO state hight  : {do_state_h}")
    print(f"DO state low : {do_state_l}")
    robot.CloseRPC()

等待控制箱数字量输入
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitDI(id,status,maxtime,opt)``"
    "描述", "等待控制箱数字量输入"
    "必选参数", "- ``id``:io编号，范围[0~15]；
    - ``status``:0-关，1-开；
    - ``maxtime``:最大等待时间，单位[ms]；
    - ``opt``:超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

等待控制箱多路数字量输入
++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitMultiDI(mode,id,status,maxtime,opt)``"
    "描述", "等待控制箱多路数字量输入"
    "必选参数", "- ``mode``:[0]-多路与，[1]-多路或；
    - ``id``:io编号，bit0~bit7对应DI0~DI7，bit8~bit15对应CI0~CI7；
    - ``status``:bit0~bit7对应DI0~DI7状态，bit8~bit15对应CI0~CI7状态位的状态[0]-关，[1]-开；
    - ``maxtime``:最大等待时间，单位[ms]；
    - ``opt``:超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待。"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

等待工具数字量输入
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitToolDI(id,status,maxtime,opt)``"
    "描述", "等待末端数字量输入"
    "必选参数", "- ``id``:io编号，范围[0~1]；
    - ``status``:0-关，1-开；
    - ``maxtime``:最大等待时间，单位[ms]；
    - ``opt``:超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

等待控制箱模拟量输入
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitAI(id,sign,value,maxtime,opt)``"
    "描述", "等待控制箱模拟量输入"
    "必选参数", "- ``id``:io编号，范围[0~1]；
    - ``sign``:0-大于，1-小于
    - ``value``:输入电流或电压值百分比，范围[0~100]对应电流值[0~20mA]或电压[0~10V]；
    - ``maxtime``:最大等待时间，单位[ms]；
    - ``opt``:超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

等待工具模拟量输入
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitToolAI(id,sign,value,maxtime,opt)``"
    "描述", "等待末端模拟量输入"
    "必选参数", "- ``id``:io编号，范围[0]；
    - ``sign``:0-大于，1-小于
    - ``value``:输入电流或电压值百分比，范围[0~100]对应电流值[0~20mA]或电压[0~10V]；
    - ``maxtime``:最大等待时间，单位[ms]；
    - ``opt``:超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

等待控制箱数字、模拟输入信号代码示例
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    status = 1
    smooth = 0
    block = 0
    for i in range(16):
        robot.SetDO(i, status, smooth, block)
        time.sleep(0.3)
    status = 0
    for i in range(16):
        robot.SetDO(i, status, smooth, block)
        time.sleep(0.3)
    status = 1
    for i in range(2):
        robot.SetToolDO(i, status, smooth, block)
        time.sleep(1)
    status = 0
    for i in range(2):
        robot.SetToolDO(i, status, smooth, block)
        time.sleep(1)
    for i in range(100):
        robot.SetAO(0, i, block)
        time.sleep(0.03)
    for i in range(100):
        robot.SetToolAO(0, i, block)
        time.sleep(0.03)
    block = 0
    error,di = robot.GetDI(0, block)
    print(f"di0: {di}")
    error,tool_di = robot.GetToolDI(1, block)
    print(f"tool_di1: {tool_di}")
    error,ai = robot.GetAI(0, block)
    print(f"ai0: {ai:.2f}")
    error,tool_ai = robot.GetToolAI(0, block)
    print(f"tool_ai0: {tool_ai:.2f}")
    error,button_state = robot.GetAxlePointRecordBtnState()
    print(f"_button_state is: {button_state}")
    error,tool_do_state = robot.GetToolDO()
    print(f"tool DO state: {tool_do_state}")
    error,[do_state_h, do_state_l] = robot.GetDO()
    print(f"DO state hight  : {do_state_h}")
    print(f"DO state low : {do_state_l}")
    rtn = robot.WaitDI(0, 1, 1000, 1)
    print(f"WaitDI over; rtn is: {rtn}")
    rtn = robot.WaitMultiDI(1, 3, 3, 1000, 1)
    print(f"WaitDI over; rtn is: {rtn}")
    rtn = robot.WaitToolDI(1, 1, 1000, 1)
    print(f"WaitDI over; rtn is: {rtn}")
    rtn = robot.WaitAI(0, 0, 50, 1000, 1)
    print(f"WaitDI over; rtn is: {rtn}")
    rtn = robot.WaitToolAI(0, 0, 50, 1000, 1)
    print(f"WaitDI over; rtn is: {rtn}")
    robot.CloseRPC()

设置控制箱DO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetCtlBoxDO(resetFlag,reloadFlag)``"
    "描述", "设置控制箱DO停止/暂停后输出是否复位"
    "必选参数", "
    - ``resetFlag``：0-不复位；1-复位
    - ``reloadFlag``：暂停恢复后是否重加载，0-不加载；1-加载"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置控制箱AO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetCtlBoxDO(resetFlag,reloadFlag)``"
    "描述", "设置控制箱AO停止/暂停后输出是否复位"
    "必选参数", "
    - ``resetFlag``：0-不复位；1-复位
    - ``reloadFlag``：暂停恢复后是否重加载，0-不加载；1-加载"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置末端工具DO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetAxleDO(resetFlag,reloadFlag)``"
    "描述", "设置末端工具DO停止/暂停后输出是否复位"
    "必选参数", "
    - ``resetFlag``：0-不复位；1-复位
    - ``reloadFlag``：暂停恢复后是否重加载，0-不加载；1-加载"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置末端工具AO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetAxleAO(resetFlag,reloadFlag)``"
    "描述", "设置末端工具AO停止/暂停后输出是否复位"
    "必选参数", "
    - ``resetFlag``：0-不复位；1-复位
    - ``reloadFlag``：暂停恢复后是否重加载，0-不加载；1-加载"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置扩展DO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetExtDO (resetFlag,reloadFlag)``"
    "描述", "设置扩展DO停止/暂停后输出是否复位"
    "必选参数", "
    - ``resetFlag``：0-不复位；1-复位
    - ``reloadFlag``：暂停恢复后是否重加载，0-不加载；1-加载"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置扩展AO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetExtAO (resetFlag,reloadFlag)``"
    "描述", "设置扩展AO停止/暂停后输出是否复位"
    "必选参数", "
    - ``resetFlag``：0-不复位；1-复位
    - ``reloadFlag``：暂停恢复后是否重加载，0-不加载；1-加载"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置SmartTool停止/暂停后输出是否复位
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetSmartToolDO(resetFlag,reloadFlag)``"
    "描述", "设置SmartTool停止/暂停后输出是否复位"
    "必选参数", "
    - ``resetFlag``：0-不复位；1-复位
    - ``reloadFlag``：暂停恢复后是否重加载，0-不加载；1-加载"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

设置LUA程序停止/暂停后输出复位代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    for i in range(16):
        robot.SetDO(i, 1, 0, 0)
        time.sleep(0.2)
    resetFlag = 0
    resumeReloadFlag = 0
    rtn = robot.SetOutputResetCtlBoxDO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetCtlBoxAO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetAxleDO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetAxleAO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetExtDO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetExtAO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetSmartToolDO(resetFlag, resumeReloadFlag)
    robot.ProgramLoad("/fruser/test.lua")
    robot.ProgramRun()
    time.sleep(2)
    robot.PauseMotion()
    time.sleep(2)
    robot.ResumeMotion()
    time.sleep(2)
    robot.CloseRPC()
    return 0