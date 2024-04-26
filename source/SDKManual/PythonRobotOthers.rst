其他接口
=================

.. toctree:: 
    :maxdepth: 5

下载点位表数据库
+++++++++++++++++++++++++++++++

.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PointTableDownLoad(point_table_name, save_file_path)``"
    "描述", "下载点位表数据库"
    "必选参数", "- ``point_table_name``：要下载的点位表名称    pointTable1.db;
    - ``save_file_path``:下载点位表的存储路径   C://test/;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot

    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    error = robot.PointTableDownLoad("point_table_a.db","D://Desktop/testPoint/download/")
    print("PointTableDownLoad错误码:",error)
 
上传点位表数据库
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PointTableUpLoad(point_table_file_path)``"
    "描述", "上传点位表数据库"
    "必选参数", "- ``point_table_file_path``：上传点位表的全路径名   C://test/pointTable1.db"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:   

    from fairino import Robot

    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    error = robot.PointTableUpLoad("D://Desktop/testPoint/point_table_a.db")
    print("PointTableUpLoad错误码:",error)

点位表切换
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PointTableSwitch(point_table_name)``"
    "描述", "点位表切换"
    "必选参数", "- ``point_table_name``：要切换的点位表名称   pointTable1.db,当点位表为空，即""时，表示将lua程序更新为未应用点位表的初始程序"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos: 

    from fairino import Robot

    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    error = robot.PointTableSwitch("point_table_a.db")
    print("PointTableSwitch:",error)

点位表更新lua文件
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PointTableUpdateLua(point_table_name, lua_file_name)``"
    "描述", "点位表更新lua文件"
    "必选参数", "- ``point_table_name``：要切换的点位表名称   pointTable1.db,当点位表为空，即""时，表示将lua程序更新为未应用点位表的初始程序
    - ``lua_file_name``: 要更新的lua文件名称 testPointTable.lua"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    error = robot.PointTableUpdateLua("point_table_a.db","testpoint.lua")
    print("PointTableUpdateLua:",error)

初始化日志参数
+++++++++++++++++++++++++++++++++

.. versionadded:: python SDK-v2.0.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoggerInit(output_model=1, file_path="", file_num=5)``"
    "描述", "初始化日志参数(未初始化不开启日志功能)"
    "必选参数", "无"
    "默认参数", "- ``output_model``：输出模式，0-直接输出；1-缓冲输出；2-异步输出，默认1;
    - ``file_path``: 文件保存路径+名称，名称必须是xxx.log的形式，如D://Desktop /fairino.log。默认执行程序所在路径，默认名称fairino_year+month+ data.log(如:fairino_2024_03_13.log);
    - ``file_num``: 滚动存储的文件数量，1~20个，默认值为5。单个文件上限50M。"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.LoggerInit(output_model=0,file_path="D://Desktop/fairino.log",file_num=3)
    robot.SetLoggerLevel(3)

设置日志过滤等级
+++++++++++++++++++++++++++++++++

.. versionadded:: python SDK-v2.0.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLoggerLevel(lvl=1)``"
    "描述", "设置日志过滤等级"
    "必选参数", "无"
    "默认参数", "- ``lvl``：过滤等级值，值越小输出日志越少, 1-error, 2-warnning, 3-inform, 4-debug,默认值是1"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.LoggerInit(output_model=0,file_path="D://Desktop/fairino.log",file_num=3)
    robot.SetLoggerLevel(3)

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

代码示例
------------
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret =robot.SetExDevProtocol(4098)
    print("SetExDevProtocol",ret)
    ret =robot.GetExDevProtocol()
    print("GetExDevProtocol",ret)

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
    "返回值", "错误码 成功-0  失败- errcode; 
    - ``protocol（调用成功返回）``: 机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster"