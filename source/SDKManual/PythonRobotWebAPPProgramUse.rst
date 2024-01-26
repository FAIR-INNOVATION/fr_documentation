机器人WebAPP程序使用
======================

.. toctree:: 
    :maxdepth: 5

设置开机自动加载默认的作业程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadDefaultProgConfig(flag,program_name)``"
    "描述", "设置开机自动加载默认的作业程序"
    "必选参数", "- ``flag``：1-开机自动加载默认程序，0-不自动加载默认程序
    - ``program_name``：作业程序名及路径，如“/fruser/movej.lua”，其中“/fruser/”为固定路径"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

加载指定的作业程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramLoad(program_name)``"
    "描述", "加载指定的作业程序"
    "必选参数", "- ``program_name``：作业程序名及路径，如“/fruser/movej.lua”，其中“/fruser/”为固定路径"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取当前机器人作业程序的执行行号
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetCurrentLine()``"
    "描述", "获取当前机器人作业程序的执行行号"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode
    - 返回值（调用成功返回）line_num"

运行当前加载的作业程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramRun()``"
    "描述", "运行当前加载的作业程序"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

暂停当前运行的作业程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramPause()``"
    "描述", "暂停当前运行的作业程序"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

恢复当前暂停的作业程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramResume()``"
    "描述", "恢复当前暂停的作业程序"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

终止当前运行的作业程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramStop()``"
    "描述", "终止当前运行的作业程序"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取机器人作业程序执行状态
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetProgramState()``"
    "描述", "获取机器人作业程序执行状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode
    - 返回值（调用成功返回）state:1-程序停止或无程序运行，2-程序运行中，3-程序暂停"

获取已加载的作业程序名
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetLoadedProgram()``"
    "描述", "获取已加载的作业程序名"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode
    - 返回值（调用成功返回）program_name"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    def print_program_state():
        pstate = robot.GetProgramState()    #查询程序运行状态,1-程序停止或无程序运行，2-程序运行中，3-程序暂停
        linenum = robot.GetCurrentLine()    #查询当前作业程序执行的行号
        name = robot.GetLoadedProgram()     #查询已加载的作业程序名
        print("the robot program state is:",pstate[1])
        print("the robot program line number is:",linenum[1])
        print("the robot program name is:",name[1])
        time.sleep(1)
    #机器人webapp程序使用接口
    robot.Mode(0)   #机器人切入自动运行模式
    print_program_state()
    ret = robot.ProgramLoad('/fruser/test0923.lua')   #加载要执行的机器人程序，testPTP.lua程序需要先在webapp上编写好
    print("加载要执行的机器人程序错误码", ret)
    ret = robot.ProgramRun()     #执行机器人程序
    print("执行机器人程序错误码", ret)
    time.sleep(2)
    print_program_state()
    ret = robot.ProgramPause()   #暂停正在执行的机器人程序
    print("暂停正在执行的机器人程序错误码", ret)
    time.sleep(2)
    print_program_state()
    ret = robot.ProgramResume()  #恢复暂停执行的机器人程序
    print("恢复暂停执行的机器人程序错误码", ret)
    time.sleep(2)
    print_program_state()
    ret = robot.ProgramStop()    #停止正在执行的机器人程序
    print("停止正在执行的机器人程序", ret)
    time.sleep(2)
    print_program_state()
    flag = 1   #0-开机不自动加载默认程序，1-开机自动加载默认程序
    ret = robot.LoadDefaultProgConfig(flag,'/fruser/testPTP.lua')    #设置开机自动加载默认程序
    print("设置开机自动加载默认程序", ret)