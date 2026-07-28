焊接
======================

.. toctree:: 
    :maxdepth: 5
    
设置焊接工艺曲线参数
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetProcessParam(id, startCurrent, startVoltage, startTime, weldCurrent, weldVoltage, endCurrent, endVoltage, endTime)``"
    "描述", "设置焊接工艺曲线参数"
    "必选参数", "
    - ``id``： 焊接工艺编号(1-99)
    - ``startCurrent``： 起弧电流(A)
    - ``startVoltage``：startVoltage 起弧电压(V)
    - ``startTime``：startTime 起弧时间(ms)
    - ``weldCurrent``：weldCurrent 焊接电流(A)
    - ``weldVoltage``：weldVoltage 焊接电压(V)
    - ``endCurrent``：endCurrent 收弧电流(A)
    - ``endVoltage``：endVoltage 收弧电压(V)
    - ``endTime``：endTime 收弧时间(ms)
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

获取焊接工艺曲线参数
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingGetProcessParam(id)``"
    "描述", "获取焊接工艺曲线参数"
    "必选参数", "
    - ``id``： 焊接工艺编号(1-99)
    "
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``startCurrent``：起弧电流(A)
    - ``startVoltage``： 起弧电压(V)
    - ``startTime``：起弧时间(ms)
    - ``weldCurrent``：焊接电流(A)
    - ``weldVoltage``：焊接电压(V)
    - ``endCurrent``：收弧电流(A)
    - ``endVoltage``：收弧电压(V)
    - ``endTime``：收弧时间(ms)
    " 

设置焊接电流与输出模拟量对应关系
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetCurrentRelation(currentMin, currentMax, outputVoltageMin, outputVoltageMax)``"
    "描述", "设置焊接电流与输出模拟量对应关系"
    "必选参数", "- ``currentMin``： 焊接电流-模拟量输出线性关系左侧点电流值(A)
    - ``currentMax``：  焊接电流-模拟量输出线性关系右侧点电流值(A)
    - ``outputVoltageMin``： 焊接电流-模拟量输出线性关系左侧点模拟量输出电压值(V)
    - ``outputVoltageMax``：焊接电流-模拟量输出线性关系右侧点模拟量输出电压值(V)
    - ``AOIndex``：焊接电流模拟量输出端口"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置焊接电压与输出模拟量对应关系
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetVoltageRelation(weldVoltageMin, weldVoltageMax, outputVoltageMin, outputVoltageMax)``"
    "描述", "设置焊接电压与输出模拟量对应关系"
    "必选参数", "- ``weldVoltageMin``： 焊接电压-模拟量输出线性关系左侧点焊接电压值(A)
    - ``weldVoltageMax``：  焊接电压-模拟量输出线性关系右侧点焊接电压值(A)
    - ``outputVoltageMin``： 焊接电压-模拟量输出线性关系左侧点模拟量输出电压值(V)
    - ``outputVoltageMax``：焊接电压-模拟量输出线性关系右侧点模拟量输出电压值(V)
    - ``AOIndex``：焊接电压模拟量输出端口"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取焊接电流与输出模拟量对应关系
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingGetCurrentRelation()``"
    "描述", "获取焊接电流与输出模拟量对应关系"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``currentMin``：焊接电流-模拟量输出线性关系左侧点电流值(A)
    - ``currentMax``：焊接电流-模拟量输出线性关系右侧点电流值(A)
    - ``outputVoltageMin``：焊接电流-模拟量输出线性关系左侧点模拟量输出电压值(V)
    - ``outputVoltageMax``：焊接电流-模拟量输出线性关系右侧点模拟量输出电压值(V)
    - ``AOIndex``：焊接电压模拟量输出端口"

获取焊接电压与输出模拟量对应关系
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingGetVoltageRelation()``"
    "描述", "获取焊接电压与输出模拟量对应关系"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``weldVoltageMin``: 焊接电压-模拟量输出线性关系左侧点焊接电压值(V)
    - ``weldVoltageMax``: 焊接电压-模拟量输出线性关系右侧点焊接电压值(V)
    - ``outputVoltageMin``: 焊接电压-模拟量输出线性关系左侧点模拟量输出电压值(V)
    - ``outputVoltageMax``: 焊接电流-模拟量输出线性关系右侧点模拟量输出电压值(V)
    - ``AOIndex``：焊接电压模拟量输出端口"

设置焊接电流
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetCurrent(ioType, current, AOIndex, blend)``"
    "描述", "设置焊接电流"
    "必选参数", "- ``ioType``： 类型 0-控制器IO； 1-扩展IO
    - ``current``： 焊接电流值(A)
    - ``AOIndex``： 焊接电流控制箱模拟量输出端口(0-1)
    - ``blend``：是否平滑 0-不平滑，1-平滑"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置焊接电压
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetVoltage(ioType, voltage, AOIndex, blend)``"
    "描述", "设置焊接电压"
    "必选参数", "- ``ioType``： 类型 0-控制器IO； 1-扩展IO
    - ``voltage``： 焊接电压值(V)
    - ``AOIndex``： 焊接电流控制箱模拟量输出端口(0-1)
    - ``blend``：是否平滑 0-不平滑，1-平滑"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置摆动参数
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.1.2
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveSetPara(weaveNum, weaveType, weaveFrequency, weaveIncStayTime, weaveRange, weaveLeftRange, weaveRightRange, additionalStayTime, weaveLeftStayTime, weaveRightStayTime, weaveCircleRadio, weaveStationary, weaveYawAngle, weaveRotAngle)``"
    "描述", "设置摆动参数"
    "必选参数", "- ``weaveNum``： 摆焊参数配置编号
    - ``weaveType``： 摆动类型 0-平面三角波摆动；1-垂直L型三角波摆动；2-顺时针圆形摆动；3-逆时针圆形摆动；4-平面正弦波摆动；5-垂直L型正弦波摆动；6-垂直三角波摆动；7-垂直正弦波摆动
    - ``weaveFrequency``： 摆动频率(Hz)
    - ``weaveIncStayTime``： 等待模式 0-周期不包含等待时间；1-周期包含等待时间必选参数
    - ``weaveRange``： 摆动幅度(mm)
    - ``weaveLeftRange``： 垂直三角摆动左弦长度(mm)
    - ``weaveRightRange``： 垂直三角摆动右弦长度(mm)
    - ``additionalStayTime``： 垂直三角摆动垂三角点停留时间(mm)
    - ``weaveLeftStayTime``： 摆动左停留时间(ms)
    - ``weaveRightStayTime``：  摆动右停留时间(ms)
    - ``weaveCircleRadio``： 圆形摆动-回调比率(0-100%)
    - ``weaveStationary``： 摆动位置等待，0-等待时间内位置继续移动；1-等待时间内位置静止"
    "默认参数", "- ``weaveYawAngle``： 摆动方向方位角（绕摆动Z轴旋转），单位°,默认0
    - ``weaveRotAngle``： 摆动方向方位角（绕摆动X轴旋转），单位°,默认0"
    "返回值", "错误码 成功-0  失败- errcode"

设置焊接参数代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.WeldingSetProcessParam(1, 177, 27, 1000, 178, 28, 176, 26, 1000)
    robot.WeldingSetProcessParam(2, 188, 28, 555, 199, 29, 133, 23, 333)
    start_current = 0
    start_voltage = 0
    start_time = 0
    weld_current = 0
    weld_voltage = 0
    end_current = 0
    end_voltage = 0
    end_time = 0
    error, start_current, start_voltage, start_time, weld_current, weld_voltage, end_current,end_voltage, end_time = robot.WeldingGetProcessParam(1)
    print(f"the Num 1 process param is {start_current} {start_voltage} {start_time} {weld_current} {weld_voltage} {end_current} {end_voltage} {end_time}")
    error, start_current, start_voltage, start_time, weld_current, weld_voltage, end_current,end_voltage, end_time = robot.WeldingGetProcessParam(2)
    print(f"the Num 2 process param is {start_current} {start_voltage} {start_time} {weld_current} {weld_voltage} {end_current} {end_voltage} {end_time}")
    rtn = robot.WeldingSetCurrentRelation(0, 400, 0, 10, 0)
    print(f"WeldingSetCurrentRelation rtn is: {rtn}")
    rtn = robot.WeldingSetVoltageRelation(0, 40, 0, 10, 1)
    print(f"WeldingSetVoltageRelation rtn is: {rtn}")
    current_min = 0
    current_max = 0
    vol_min = 0
    vol_max = 0
    output_vmin = 0
    output_vmax = 0
    cur_index = 0
    vol_index = 0
    rtn,current_min, current_max, output_vmin, output_vmax, cur_index = robot.WeldingGetCurrentRelation()
    print(f"WeldingGetCurrentRelation rtn is: {rtn}")
    print(f"current min {current_min} current max {current_max} output vol min {output_vmin} output vol max {output_vmax}")
    rtn,vol_min, vol_max, output_vmin, output_vmax, vol_index = robot.WeldingGetVoltageRelation()
    print(f"WeldingGetVoltageRelation rtn is: {rtn}")
    print(f"vol min {vol_min} vol max {vol_max} output vol min {output_vmin} output vol max {output_vmax}")
    rtn = robot.WeldingSetCurrent(1, 100, 0, 0)
    print(f"WeldingSetCurrent rtn is: {rtn}")
    time.sleep(3)
    rtn = robot.WeldingSetVoltage(1, 10, 0, 0)
    print(f"WeldingSetVoltage rtn is: {rtn}")
    rtn = robot.WeaveSetPara(0, 0, 2.000000, 0, 10.000000, 0.000000, 0.000000, 0, 0, 0, 0, 0,0.0, 60.000000)
    print(f"rtn is: {rtn}")
    robot.WeaveOnlineSetPara(0, 0, 1, 0, 20, 0, 0, 0, 0)
    rtn = robot.WeldingSetCheckArcInterruptionParam(1, 200)
    print(f"WeldingSetCheckArcInterruptionParam {rtn}")
    rtn = robot.WeldingSetReWeldAfterBreakOffParam(1, 5.7, 98.2, 0)
    print(f"WeldingSetReWeldAfterBreakOffParam {rtn}")
    enable = 0
    length = 0
    velocity = 0
    move_type = 0
    check_enable = 0
    arc_interrupt_time_length = 0
    rtn,check_enable, arc_interrupt_time_length = robot.WeldingGetCheckArcInterruptionParam()
    print(f"WeldingGetCheckArcInterruptionParam checkEnable {check_enable} arcInterruptTimeLength {arc_interrupt_time_length}")
    rtn,enable, length, velocity, move_type = robot.WeldingGetReWeldAfterBreakOffParam()
    print(f"WeldingGetReWeldAfterBreakOffParam enable = {enable}, length = {length}, velocity = {velocity}, moveType = {move_type}")
    robot.SetWeldMachineCtrlModeExtDoNum(17)
    for i in range(5):
        robot.SetWeldMachineCtrlMode(0)
        time.sleep(1)
        robot.SetWeldMachineCtrlMode(1)
        time.sleep(1)
    robot.CloseRPC()

即时设置摆动参数
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveOnlineSetPara (weaveNum, weaveType, weaveFrequency, weaveIncStayTime, weaveRange, weaveLeftStayTime, weaveRightStayTime, weaveCircleRadio, weaveStationary)``"
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
    "返回值", "错误码 成功-0  失败- errcode"

获取机器人焊接电弧意外中断检测参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingGetCheckArcInterruptionParam()``"
    "描述", "获取机器人焊接电弧意外中断检测参数"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``checkEnable``：是否使能检测；0-不使能；1-使能
    - ``arcInterruptTimeLength``：电弧中断确认时长(ms)"

设置机器人焊接电弧意外中断检测参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetCheckArcInterruptionParam(checkEnable, arcInterruptTimeLength)``"
    "描述", "设置机器人焊接电弧意外中断检测参数"
    "必选参数", "- ``checkEnable``：是否使能检测；0-不使能；1-使能
    - ``arcInterruptTimeLength``：电弧中断确认时长(ms)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

获取机器人焊接中断恢复参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingGetReWeldAfterBreakOffParam()``"
    "描述", "获取机器人焊接中断恢复参数"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``enable``：是否使能焊接中断恢复
    - ``length``：焊缝重叠距离(mm)
    - ``velocity``：机器人回到再起弧点速度百分比(0-100)
    - ``moveType``：机器人运动到再起弧点方式；0-LIN；1-PTP"

设置机器人焊接中断恢复参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetReWeldAfterBreakOffParam(enable, length, velocity, moveType)``"
    "描述", "设置机器人焊接中断恢复参数"
    "必选参数", "- ``enable``：是否使能焊接中断恢复
    - ``length``：焊缝重叠距离(mm)
    - ``velocity``：机器人回到再起弧点速度百分比(0-100)
    - ``moveType``：机器人运动到再起弧点方式；0-LIN；1-PTP"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

设置焊机控制模式扩展DO端口
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWeldMachineCtrlModeExtDoNum(DONum)``"
    "描述", "设置焊机控制模式扩展DO端口"
    "必选参数", "- ``DONum``：焊机控制模式DO端口(0-127)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

设置焊机控制模式
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWeldMachineCtrlMode(mode, ioType)``"
    "描述", "设置焊机控制模式"
    "必选参数", "
    - ``ioType``：控制类型；0-控制箱IO；1-数字通信协议(UDP);2-数字通信协议(ModbusTCP)
    - ``mode``：焊机控制模式;0-一元化"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

获取焊机控制模式
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v3.9.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetWeldMachineCtrlMode(self)``"
    "描述", "获取焊机控制模式"
    "必选参数", "
    - ``mode``：mode 焊机控制模式;0-直流一元模式；1-脉冲一元模式；2-JOB模式；3-近控模式；4-分别模式；5-CC/CV模式；6-TIG；7-CMT
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

获取焊机控制模式代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v3.9.8

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time

    def main():
        robot = Robot.RPC('192.168.58.2')
        time.sleep(0.5)  

        robot.WeldingSetProcessParam(1, 177, 27, 1000, 178, 28, 176, 26, 1000)
        robot.WeldingSetProcessParam(2, 188, 28, 555, 199, 29, 133, 23, 333)

        start_current = 0
        start_voltage = 0
        start_time = 0
        weld_current = 0
        weld_voltage = 0
        end_current = 0
        end_voltage = 0
        end_time = 0

        error, start_current, start_voltage, start_time, weld_current, weld_voltage, end_current,end_voltage, end_time = robot.WeldingGetProcessParam(1)
        print(f"the Num 1 process param is {start_current} {start_voltage} {start_time} {weld_current} {weld_voltage} {end_current} {end_voltage} {end_time}")

        error, start_current, start_voltage, start_time, weld_current, weld_voltage, end_current,end_voltage, end_time = robot.WeldingGetProcessParam(2)
        print(f"the Num 2 process param is {start_current} {start_voltage} {start_time} {weld_current} {weld_voltage} {end_current} {end_voltage} {end_time}")

        rtn = robot.WeldingSetCurrentRelation(0, 400, 0, 10, 0)
        print(f"WeldingSetCurrentRelation rtn is: {rtn}")

        rtn = robot.WeldingSetVoltageRelation(0, 40, 0, 10, 1)
        print(f"WeldingSetVoltageRelation rtn is: {rtn}")

        current_min = 0
        current_max = 0
        vol_min = 0
        vol_max = 0
        output_vmin = 0
        output_vmax = 0
        cur_index = 0
        vol_index = 0

        rtn,current_min, current_max, output_vmin, output_vmax, cur_index = robot.WeldingGetCurrentRelation()
        print(f"WeldingGetCurrentRelation rtn is: {rtn}")
        print(
            f"current min {current_min} current max {current_max} output vol min {output_vmin} output vol max {output_vmax}")

        rtn,vol_min, vol_max, output_vmin, output_vmax, vol_index = robot.WeldingGetVoltageRelation()
        print(f"WeldingGetVoltageRelation rtn is: {rtn}")
        print(f"vol min {vol_min} vol max {vol_max} output vol min {output_vmin} output vol max {output_vmax}")

        rtn = robot.WeldingSetCurrent(1, 100, 0, 0)
        print(f"WeldingSetCurrent rtn is: {rtn}")

        time.sleep(3)

        rtn = robot.WeldingSetVoltage(1, 10, 0, 0)
        print(f"WeldingSetVoltage rtn is: {rtn}")

        rtn = robot.WeaveSetPara(0, 0, 2.000000, 0, 10.000000, 0.000000, 0.000000, 0, 0, 0, 0, 0,0.0, 60.000000)
        print(f"rtn is: {rtn}")

        robot.WeaveOnlineSetPara(0, 0, 1, 0, 20, 0, 0, 0, 0)

        rtn = robot.WeldingSetCheckArcInterruptionParam(1, 200)
        print(f"WeldingSetCheckArcInterruptionParam {rtn}")

        rtn = robot.WeldingSetReWeldAfterBreakOffParam(1, 5.7, 98.2, 0)
        print(f"WeldingSetReWeldAfterBreakOffParam {rtn}")

        enable = 0
        length = 0
        velocity = 0
        move_type = 0
        check_enable = 0
        arc_interrupt_time_length = 0

        rtn,check_enable, arc_interrupt_time_length = robot.WeldingGetCheckArcInterruptionParam()
        print(
            f"WeldingGetCheckArcInterruptionParam checkEnable {check_enable} arcInterruptTimeLength {arc_interrupt_time_length}")

        rtn,enable, length, velocity, move_type = robot.WeldingGetReWeldAfterBreakOffParam()
        print(
            f"WeldingGetReWeldAfterBreakOffParam enable = {enable}, length = {length}, velocity = {velocity}, moveType = {move_type}")

        robot.SetWeldMachineCtrlModeExtDoNum(17)
        for i in range(5):
            robot.SetWeldMachineCtrlMode(0,1)
            error,getCtrlMode=robot.GetWeldMachineCtrlMode
            print(f"GetWeldMachineCtrlMode = {getCtrlMode}")
            time.sleep(1)
            robot.SetWeldMachineCtrlMode(1,1)
            error, getCtrlMode = robot.GetWeldMachineCtrlMode
            print(f"GetWeldMachineCtrlMode = {getCtrlMode}")
            time.sleep(1)

        robot.CloseRPC()

焊接开始
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ARCStart(ioType, arcNum, timeout)``"
    "描述", "焊接开始"
    "必选参数", "- ``ioType``：io类型 0-控制器IO； 1-扩展IO
    - ``arcNum``： 焊机配置文件编号
    - ``timeout``： 起弧超时时间"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

焊接结束
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ARCEnd(ioType, arcNum, timeout)``"
    "描述", "焊接结束"
    "必选参数", "- ``ioType``： 类型 0-控制器IO； 1-扩展IO
    - ``arcNum``： 焊机配置文件编号
    - ``timeout``： 起弧超时时间"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

摆动开始
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveStart(weaveNum)``"
    "描述", "摆动开始"
    "必选参数", "- ``weaveNum``： 类型 0-控制器IO； 1-扩展IO"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

摆动结束
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveEnd(weaveNum)``"
    "描述", "摆动结束"
    "必选参数", "- ``weaveNum``： 摆焊参数配置编号"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

正向送丝
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetForwardWireFeed(ioType, wireFeed)``"
    "描述", "正向送丝"
    "必选参数", "- ``ioType``： 0-控制器IO；1-扩展IO
    - ``wireFeed``： 送丝控制  0-停止送丝；1-送丝"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

反向送丝
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetReverseWireFeed(ioType, wireFeed)``"
    "描述", "反向送丝"
    "必选参数", "- ``ioType``： 0-控制器IO；1-扩展IO
    - ``wireFeed``： 送丝控制  0-停止送丝；1-送丝"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

送气
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAspirated(ioType, airControl)``"
    "描述", "送气"
    "必选参数", "- ``ioType``： 0-控制器IO；1-扩展IO
    - ``airControl``： 送气控制  0-停止送气；1-送气"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置机器人焊接中断后恢复焊接
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingStartReWeldAfterBreakOff()``"
    "描述", "设置机器人焊接中断后恢复焊接"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

设置机器人焊接中断后退出焊接
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingAbortWeldAfterBreakOff()``"
    "描述", "设置机器人焊接中断后退出焊接"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

机器人焊接控制代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.SetForwardWireFeed(0, 1)
    time.sleep(1)
    robot.SetForwardWireFeed(0, 0)
    robot.SetReverseWireFeed(0, 1)
    time.sleep(1)
    robot.SetReverseWireFeed(0, 0)
    robot.SetAspirated(0, 1)
    time.sleep(1)
    robot.SetAspirated(0, 0)
    robot.WeldingSetCurrent(1, 230, 0, 0)
    robot.WeldingSetVoltage(1, 24, 0, 1)
    p1Desc = [228.879, -503.594, 453.984, -175.580, 8.293, 171.267]
    p1Joint = [102.700, -85.333, 90.518, -102.365, -83.932, 22.134]
    p2Desc = [-333.302, -435.580, 449.866, -174.997, 2.017, 109.815]
    p2Joint = [41.862, -85.333, 90.526, -100.587, -90.014, 22.135]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    robot.MoveJ(joint_pos=p1Joint, tool=13, user=0)
    robot.ARCStart(1, 0, 10000)
    robot.WeaveStart(0)
    robot.MoveL(desc_pos=p2Desc, tool=13, user=0)
    robot.ARCEnd(1, 0, 10000)
    robot.WeaveEnd(0)
    robot.WeldingStartReWeldAfterBreakOff()
    robot.WeldingAbortWeldAfterBreakOff()
    robot.CloseRPC()

分段焊接启动
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SegmentWeldStart(startDesePos,  endDesePos, startJPos, endJPos, weldLength, noWeldLength, weldIOType, arcNum, weldTimeout, isWeave,weaveNum,tool,user,vel=20.0, acc=0.0, ovl=100.0, blendR=-1.0,exaxis_pos=[0.0, 0.0, 0.0, 0.0],  search=0, offset_flag=0, offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0])``"
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

机器人段焊代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.WeldingSetCurrent(1, 230, 0, 0)
    robot.WeldingSetVoltage(1, 24, 0, 1)
    p1Desc = [228.879, -503.594, 453.984, -175.580, 8.293, 171.267]
    p1Joint = [102.700, -85.333, 90.518, -102.365, -83.932, 22.134]
    p2Desc = [-333.302, -435.580, 449.866, -174.997, 2.017, 109.815]
    p2Joint = [41.862, -85.333, 90.526, -100.587, -90.014, 22.135]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    rtn = robot.SegmentWeldStart(p1Desc, p2Desc, p1Joint, p2Joint, 20, 20, 0, 0, 5000, 0, 0, 0, 0)
    print(f"SegmentWeldStart rtn is {rtn}")
    robot.CloseRPC()

仿真摆动开始
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveStartSim(weaveNum)``"
    "描述", "仿真摆动开始"
    "必选参数", "- ``weaveNum``：摆动参数编号"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

仿真摆动结束
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveEndSim(weaveNum)``"
    "描述", "仿真摆动结束"
    "必选参数", "- ``weaveNum``：摆动参数编号"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

开始轨迹检测预警(不运动)
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveInspectStart(weaveNum)``"
    "描述", "开始轨迹检测预警(不运动)"
    "必选参数", "- ``weaveNum``：摆动参数编号"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

结束轨迹检测预警(不运动)
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveInspectEnd(weaveNum)``"
    "描述", "结束轨迹检测预警(不运动)"
    "必选参数", "- ``weaveNum``：摆动参数编号"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

摆动渐变开始
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveChangeStart(weaveChangeFlag, weaveNum, velStart, velEnd)``"
    "描述", "摆动渐变开始"
    "必选参数", "- ``weaveChangeFlag``：摆动编号 1-变摆动参数；2-变摆动参数+焊接速度
    - ``weaveNum``：摆动编号
    - ``velStart``：焊接开始速度，(cm/min)
    - ``velEnd``：焊接结束速度，(cm/min)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

机器人摆动渐变焊接代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    p1Desc = [228.879, -503.594, 453.984, -175.580, 8.293, 171.267]
    p1Joint = [102.700, -85.333, 90.518, -102.365, -83.932, 22.134]
    p2Desc = [-333.302, -435.580, 449.866, -174.997, 2.017, 109.815]
    p2Joint = [41.862, -85.333, 90.526, -100.587, -90.014, 22.135]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    robot.MoveJ(joint_pos= p1Joint,tool= 13,user= 0)
    robot.WeaveStartSim(0)
    robot.MoveL(desc_pos= p2Desc,tool= 13,user= 0)
    robot.WeaveEndSim(0)
    robot.MoveJ(joint_pos= p1Joint,tool= 13,user= 0)
    robot.WeaveInspectStart(0)
    robot.MoveL(desc_pos= p2Desc,tool= 13,user= 0,)
    robot.WeaveInspectEnd(0)
    robot.WeldingSetVoltage(1, 19, 0, 0)
    robot.WeldingSetCurrent(1, 190, 0, 0)
    robot.MoveL(desc_pos= p1Desc,tool= 1,user= 1,vel= 100,acc= 100,ovl= 50)
    robot.ARCStart(1, 0, 10000)
    robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0)
    robot.WeaveStart(0)
    robot.WeaveChangeStart(1, 0, 50, 30)
    robot.MoveL(desc_pos= p2Desc,tool= 1,user= 1,vel= 100)
    robot.WeaveChangeEnd()
    robot.WeaveEnd(0)
    robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0)
    robot.ARCEnd(1, 0, 10000)
    robot.CloseRPC()

摆动渐变结束
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.9-3.7.9

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveChangeEnd()``"
    "描述", "摆动渐变结束"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

扩展IO-配置焊机气体检测信号
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAirControlExtDoNum(DONum)``"
    "描述", "扩展IO-配置焊机气体检测信号"
    "必选参数", "
    - ``DONum``：气体检测信号扩展DO编号
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

扩展IO-配置焊机起弧信号
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetArcStartExtDoNum(DONum)``"
    "描述", "扩展IO-配置焊机起弧信号"
    "必选参数", "
    - ``DONum``：气体检测信号扩展DO编号
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 
        
扩展IO-配置焊机反向送丝信号
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWireReverseFeedExtDoNum(DONum)``"
    "描述", "扩展IO-配置焊机反向送丝信号"
    "必选参数", "
    - ``DONum``：气体检测信号扩展DO编号
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 
        
扩展IO-配置焊机正向送丝信号
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWireForwardFeedExtDoNum(DONum)``"
    "描述", "扩展IO-配置焊机正向送丝信号"
    "必选参数", "
    - ``DONum``：气体检测信号扩展DO编号
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 
        
扩展IO-配置焊机起弧成功信号
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetArcDoneExtDiNum(DINum)``"
    "描述", "扩展IO-配置焊机起弧成功信号"
    "必选参数", "
    - ``DINum``：焊机准备信号扩展DI编号
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 
        
扩展IO-配置焊机准备信号
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetArcDoneExtDiNum(DINum)``"
    "描述", "扩展IO-配置焊机准备信号"
    "必选参数", "
    - ``DINum``：焊机准备信号扩展DI编号
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 
        
扩展IO-配置焊接中断恢复信号
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExtDIWeldBreakOffRecover(reWeldDINum, abortWeldDINum)``"
    "描述", "扩展IO-配置焊接中断恢复信号"
    "必选参数", "
    - ``reWeldDINum``：焊接中断后恢复焊接信号扩展DI编号
    - ``abortWeldDINum``：焊接中断后退出焊接信号扩展DI编号
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

设置扩展IO焊接信号代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.SetArcStartExtDoNum(10)
    print(f"SetArcStartExtDoNum rtn is {rtn}")
    rtn = robot.SetAirControlExtDoNum(20)
    print(f"SetAirControlExtDoNum rtn is {rtn}")
    rtn = robot.SetWireForwardFeedExtDoNum(30)
    print(f"SetWireForwardFeedExtDoNum rtn is {rtn}")
    rtn = robot.SetWireReverseFeedExtDoNum(40)
    rtn = robot.SetWeldReadyExtDiNum(50)
    print(f"SetWeldReadyExtDiNum rtn is {rtn}")
    rtn = robot.SetArcDoneExtDiNum(60)
    print(f"SetArcDoneExtDiNum rtn is {rtn}")
    rtn = robot.SetExtDIWeldBreakOffRecover(70, 80)
    print(f"SetExtDIWeldBreakOffRecover rtn is {rtn}")
    rtn = robot.SetWireSearchExtDIONum(0, 1)
    print(f"SetWireSearchExtDIONum rtn is {rtn}")
    robot.CloseRPC()

获取扩展DI功能配置
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-V3.9.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetExtDIConfig(self)``"
    "描述", "获取扩展DI功能配置"
    "必选参数", "
    - ``DIConfig``：扩展DI输入配置；DIConfig[0]-焊机准备扩展DI端口
    - ``DIConfig[1]``：起弧成功扩展DI端口
    - ``DIConfig[2]``：焊接中断恢复扩展DI端口
    - ``DIConfig[3]``：焊接中断退出扩展DI端口
    - ``DIConfig[4]``：焊丝寻位成功扩展DI端口
    - ``DIConfig[5]``：激光焊机运行状态扩展DI端口
    - ``DIConfig[6]``：激光焊机故障状态扩展DI端口
    - ``DIConfig[7-15]``：预留
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

获取扩展DO功能配置
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-V3.9.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetExtDOConfig(self)``"
    "描述", "获取扩展DO功能配置"
    "必选参数", "
    - ``DOConfig``：扩展DO输入配置；DOConfig[0]-焊机起弧扩展DO端口
    - ``DOConfig[1]``：气体检测扩展DO端口
    - ``DOConfig[2]``：正向送丝扩展DO端口
    - ``DOConfig[3]``：反向送丝扩展DO端口
    - ``DOConfig[4]``：焊丝寻位扩展DO端口
    - ``DOConfig[5]``：焊机控制模式扩展DO端口
    - ``DOConfig[6]``：激光焊机使能扩展DO端口
    - ``DOConfig[7]``：激光焊机启动(出光)扩展DO端口
    - ``DOConfig[8]``：激光焊机复位扩展DO端口
    - ``DOConfig[9-15]``：预留
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

获取扩展DI/DO代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-V3.9.8

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time

    def main():
        robot = Robot.RPC('192.168.58.2')
        time.sleep(0.5)  

    rtn = robot.SetArcStartExtDoNum(10)
        print(f"SetArcStartExtDoNum rtn is {rtn}")

        rtn = robot.SetAirControlExtDoNum(20)
        print(f"SetAirControlExtDoNum rtn is {rtn}")

        rtn = robot.SetWireForwardFeedExtDoNum(30)
        print(f"SetWireForwardFeedExtDoNum rtn is {rtn}")

        rtn = robot.SetWireReverseFeedExtDoNum(40)
        print(f"SetWireReverseFeedExtDoNum rtn is {rtn}")

        rtn = robot.SetWeldReadyExtDiNum(50)
        print(f"SetWeldReadyExtDiNum rtn is {rtn}")

        rtn = robot.SetArcDoneExtDiNum(60)
        print(f"SetArcDoneExtDiNum rtn is {rtn}")

        rtn = robot.SetExtDIWeldBreakOffRecover(70, 80)
        print(f"SetExtDIWeldBreakOffRecover rtn is {rtn}")

        rtn = robot.SetWireSearchExtDIONum(0, 1)
        print(f"SetWireSearchExtDIONum rtn is {rtn}")

        rtn, DIConfig = robot.GetExtDIConfig()
        print(f"GetExtDIConfig rtn is {rtn}")
        print(f"welder ready {DIConfig[0]}")
        print(f"arc done {DIConfig[1]}")
        print(f"reweld start {DIConfig[2]}")
        print(f"abort reweld {DIConfig[3]}")
        print(f"wiresearch done {DIConfig[4]}")
        print(f"Laser welding State {DIConfig[5]}")
        print(f"laser welding error state {DIConfig[6]}")

        rtn, DOConfig = robot.GetExtDOConfig()
        print(f"GetExtDOConfig rtn is {rtn}")
        print(f"Arc Start {DOConfig[0]}")
        print(f"Air Test {DOConfig[1]}")
        print(f"Wire forward {DOConfig[2]}")
        print(f"Wire Inverse {DOConfig[3]}")
        print(f"wiresearch {DOConfig[4]}")
        print(f"Weld Mode {DOConfig[5]}")
        print(f"laser Enable {DOConfig[6]}")
        print(f"Laser On {DOConfig[7]}")
        print(f"Laser Reset Error {DOConfig[8]}")

        robot.CloseRPC()
    
电弧跟踪控制
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.9-3.7.9

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceControl(flag,delaytime, isLeftRight, klr, tStartLr, stepMaxLr, sumMaxLr, isUpLow, kud, tStartUd, stepMaxUd, sumMaxUd, axisSelect, referenceType, referSampleStartUd, referSampleCountUd, referenceCurrent, offsetType, offsetParameter)``"
    "描述", "电弧跟踪控制"
    "必选参数", "- ``flag``： 开关，0-关；1-开
    - ``delayTime``：滞后时间，单位ms
    - ``isLeftRight``：左右偏差补偿 0-关闭，1-开启
    - ``klr``：左右调节系数(灵敏度)
    - ``tStartLr``：左右开始补偿时间cyc
    - ``stepMaxLr``：左右每次最大补偿量 mm
    - ``sumMaxLr``：左右总计最大补偿量 mm
    - ``isUpLow``：上下偏差补偿 0-关闭，1-开启
    - ``kud``：上下调节系数(灵敏度)
    - ``tStartUd``：上下开始补偿时间cyc
    - ``stepMaxUd``：上下每次最大补偿量 mm
    - ``sumMaxUd``：上下总计最大补偿量
    - ``axisSelect``：上下坐标系选择，0-摆动；1-工具；2-基座
    - ``referenceType``：上下基准电流设定方式，0-反馈；1-常数
    - ``referSampleStartUd``：上下基准电流采样开始计数(反馈)，cyc
    - ``referSampleCountUd``：上下基准电流采样循环计数(反馈)，cyc
    - ``referenceCurrent``：上下基准电流mA
    - ``offsetType``：偏置跟踪类型，0-不偏置；1-采样；2-百分比
    - ``offsetParameter``：偏置参数；采样(偏置采样开始时间，默认采一周期)；百分比(偏置百分比(-100 ~ 100))"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

电弧跟踪AI通带选择
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceExtAIChannelConfig(channel)``"
    "描述", "电弧跟踪AI通带选择"
    "必选参数", "- ``channel``：电弧跟踪AI通带选择,[0-3]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

电弧追踪 + 多层多道补偿开启
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceReplayStart()``"
    "描述", "电弧追踪 + 多层多道补偿开启"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

电弧追踪 + 多层多道补偿关闭
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceReplayEnd()``"
    "描述", "电弧追踪 + 多层多道补偿关闭"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

偏移量坐标变化-多层多道焊
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MultilayerOffsetTrsfToBase(pointo, pointX, pointZ, dx, dy, db)``"
    "描述", "偏移量坐标变化-多层多道焊"
    "必选参数", "- ``pointo``：基准点笛卡尔位姿
    - ``pointX``：基准点X向偏移方向点笛卡尔位姿
    - ``pointZ``：基准点Z向偏移方向点笛卡尔位姿
    - ``dx``：x方向偏移量(mm)
    - ``dz``：z方向偏移量(mm)
    - ``dry``：绕y轴偏移量(°)"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``offset``：计算结果偏移量"

多层多道焊电弧跟踪代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    mulitilineorigin1_joint = [-24.090, -63.501, 84.288, -111.940, -93.426, 57.669]
    mulitilineorigin1_desc = [-677.559, 190.951, -1.205, 1.144, -41.482, -82.577]
    mulitilineX1_desc = [-677.556, 211.949, -1.206]
    mulitilineZ1_desc = [-677.564, 190.956, 19.817]
    mulitilinesafe_joint = [-25.734, -63.778, 81.502, -108.975, -93.392, 56.021]
    mulitilinesafe_desc = [-677.561, 211.950, 19.812, 1.144, -41.482, -82.577]
    mulitilineorigin2_joint = [-29.743, -75.623, 101.241, -116.354, -94.928, 55.735]
    mulitilineorigin2_desc = [-563.961, 215.359, -0.681, 2.845, -40.476, -87.443]
    mulitilineX2_desc = [-563.965, 220.355, -0.680]
    mulitilineZ2_desc = [-563.968, 215.362, 4.331]
    epos = [0, 0, 0, 0]
    offset = [0, 0, 0, 0, 0, 0]
    time.sleep(0.01)
    error = robot.MoveJ(joint_pos= mulitilinesafe_joint,tool= 13,user= 0,vel= 10)
    print(f"MoveJ return: {error}")
    error = robot.MoveL(desc_pos= mulitilineorigin1_desc,tool= 13,user= 0,vel= 10,speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.MoveJ(joint_pos= mulitilinesafe_joint,tool= 13,user= 0,vel= 10)
    print(f"MoveJ return: {error}")
    error = robot.MoveL(desc_pos= mulitilineorigin2_desc,tool= 13,user= 0,vel= 10,speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.MoveJ(joint_pos= mulitilinesafe_joint,tool= 13,user= 0,vel= 10)
    print(f"MoveJ return: {error}")
    error = robot.MoveL(desc_pos= mulitilineorigin1_desc,tool= 13,user= 0,vel= 10,speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.ARCStart(1, 0, 3000)
    print(f"ARCStart return: {error}")
    error = robot.WeaveStart(0)
    print(f"WeaveStart return: {error}")
    error = robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10,0,0)
    print(f"ArcWeldTraceControl return: {error}")
    error = robot.MoveL(desc_pos= mulitilineorigin2_desc,tool= 13,user= 0,vel= 1,speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10,0,0)
    print(f"ArcWeldTraceControl return: {error}")
    error = robot.WeaveEnd(0)
    print(f"WeaveEnd return: {error}")
    error = robot.ARCEnd(1, 0, 10000)
    print(f"ARCEnd return: {error}")
    error = robot.MoveJ(joint_pos= mulitilinesafe_joint,tool= 13,user= 0,vel= 10)
    print(f"MoveJ return: {error}")
    error,offset = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc[:3], mulitilineX1_desc, mulitilineZ1_desc, 10.0, 0.0, 0.0)
    print(f"MultilayerOffsetTrsfToBase return: {error}")
    error = robot.MoveL(desc_pos= mulitilineorigin1_desc,tool= 13,user= 0,vel= 10,speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.ARCStart(1, 0, 3000)
    print(f"ARCStart return: {error}")
    error, offset = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc[:3], mulitilineX2_desc, mulitilineZ2_desc, 10, 0, 0)
    print(f"MultilayerOffsetTrsfToBase return: {error}")
    error = robot.ArcWeldTraceReplayStart()
    print(f"ArcWeldTraceReplayStart return: {error}")
    error = robot.MoveL(desc_pos= mulitilineorigin2_desc,tool= 13,user= 0,vel= 2,speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.ArcWeldTraceReplayEnd()
    print(f"ArcWeldTraceReplayEnd return: {error}")
    error = robot.ARCEnd(1, 0, 10000)
    print(f"ARCEnd return: {error}")
    error = robot.MoveJ(joint_pos= mulitilinesafe_joint,tool= 13,user= 0,vel= 10)
    print(f"MoveJ return: {error}")
    error, offset = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc[:3], mulitilineX1_desc, mulitilineZ1_desc, 0, 10, 0)
    print(f"MultilayerOffsetTrsfToBase return: {error}")
    error = robot.MoveL(desc_pos= mulitilineorigin1_desc,tool= 13,user= 0,vel= 10,speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.ARCStart(1, 0, 3000)
    print(f"ARCStart return: {error}")
    error, offset = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc[:3], mulitilineX2_desc, mulitilineZ2_desc, 0, 10, 0)
    error = robot.ArcWeldTraceReplayStart()
    print(f"ArcWeldTraceReplayStart return: {error}")
    error = robot.MoveL(desc_pos= mulitilineorigin2_desc,tool= 13,user= 0,vel= 2,speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.ArcWeldTraceReplayEnd()
    print(f"ArcWeldTraceReplayEnd return: {error}")
    error = robot.ARCEnd(1, 0, 3000)
    print(f"ARCEnd return: {error}")
    error = robot.MoveJ(joint_pos= mulitilinesafe_joint,tool= 13,user= 0,vel= 10)
    print(f"MoveJ return: {error}")
    robot.CloseRPC()

电弧跟踪焊机电流反馈AI通道选择
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceAIChannelCurrent(channel)``"
    "描述", "电弧跟踪焊机电流反馈AI通道选择"
    "必选参数", "- ``channel``：通道；0-扩展AI0；1-扩展AI1；2-扩展AI2；3-扩展AI3；4-控制箱AI0；5-控制箱AI1"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

电弧跟踪焊机电压反馈AI通道选择
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceAIChannelVoltage(channel)``"
    "描述", "电弧跟踪焊机电压反馈AI通道选择"
    "必选参数", "- ``channel``：通道；0-扩展AI0；1-扩展AI1；2-扩展AI2；3-扩展AI3；4-控制箱AI0；5-控制箱AI1"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

电弧跟踪焊机电流反馈转换参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceCurrentPara(AILow, AIHigh, currentLow, currentHigh)``"
    "描述", "电弧跟踪焊机电流反馈转换参数"
    "必选参数", "无"
    "默认参数", "- ``AILow``：AI通道下限，默认值0V，范围[0-10V]
    - ``AIHigh``：AI通道上限，默认值10V，范围[0-10V]
    - ``currentLow``：AI通道下限对应焊机电流值，默认值0V，范围[0-200V]
    - ``currentHigh``：AI通道上限对应焊机电流值，默认值100V，范围[0-200V]"
    "返回值", "错误码 成功-0  失败- errcode"

电弧跟踪焊机电压反馈转换参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceVoltagePara(AILow, AIHigh, voltageLow, voltageHigh)``"
    "描述", "电弧跟踪焊机电压反馈转换参数"
    "必选参数", "无"
    "默认参数", "- ``AILow``：AI通道下限，默认值0V，范围[0-10V]
    - ``AIHigh``：AI通道上限，默认值10V，范围[0-10V]
    - ``voltageLow``：AI通道下限对应焊机电压值，默认值0V，范围[0-200V]
    - ``voltageHigh``：AI通道上限对应焊机电压值，默认值100V，范围[0-200V]"
    "返回值", "错误码 成功-0  失败- errcode"

电弧跟踪代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')

    safetydescPose = [-504.043,275.181,40.908,-28.002,-42.025,-14.044]
    safetyjointPos = [-39.078,-76.732,87.227,-99.47,-94.301,18.714]
    startdescPose = [-473.86,257.879,-20.849,-37.317,-42.021,2.543]
    startjointPos = [-43.487,-76.526,95.568,-104.445,-89.356,3.72]
    enddescPose = [-499.844,141.225,7.72,-34.856,-40.17,13.13]
    endjointPos = [-31.305,-82.998,99.401,-104.426,-89.35,3.696]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    robot.MoveJ(joint_pos=safetyjointPos, tool=1, user=0, vel=20, acc=100)
    robot.WeldingSetCurrentRelation(0, 495, 1, 10, 0)
    robot.WeldingSetVoltageRelation(10, 45, 1, 10, 1)
    robot.WeldingSetVoltage(0, 25, 1, 0)  # ----设置电压
    robot.WeldingSetCurrent(0, 260, 0, 0)  # ----设置电流
    rtn = robot.ArcWeldTraceAIChannelCurrent(4)
    print("ArcWeldTraceAIChannelCurrent rtn is", rtn)
    rtn = robot.ArcWeldTraceAIChannelVoltage(5)
    print("ArcWeldTraceAIChannelVoltage rtn is", rtn)
    rtn = robot.ArcWeldTraceCurrentPara(0, 5, 0, 500)
    print("ArcWeldTraceCurrentPara rtn is", rtn)
    rtn = robot.ArcWeldTraceVoltagePara(1.018, 10, 0, 50)
    print("ArcWeldTraceVoltagePara rtn is", rtn)
    robot.MoveJ(joint_pos=startjointPos, tool=1, user=0, vel=20, acc=100)
    robot.ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0)
    robot.ARCStart(0, 0, 10000)
    robot.WeaveStart(0)
    robot.MoveL(desc_pos=enddescPose, tool=1, user=0, vel=100, ovl= 2, acc=100)
    robot.ARCEnd(0, 0, 10000)
    robot.WeaveEnd(0)
    robot.ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0)
    robot.MoveJ(joint_pos=safetyjointPos, tool=1, user=0, vel=20, acc=100)

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

焊丝寻位开始
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WireSearchStart(refPos,searchVel,searchDis,autoBackFlag,autoBackVel,autoBackDis,offectFlag)``"
    "描述", "焊丝寻位开始"
    "必选参数", "- ``refPos``： 1-基准点 0-接触点
    - ``searchVel``： 寻位速度 %
    - ``searchDis``： 寻位距离 mm
    - ``autoBackFlag``： 自动返回标志，0-不自动；-自动
    - ``autoBackVel``： 自动返回速度 %
    - ``autoBackDis``： 自动返回距离 mm
    - ``offectFlag``： 1-带偏移量寻位；0-示教点寻位"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

焊丝寻位结束
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WireSearchEnd(refPos,searchVel,searchDis,autoBackFlag,autoBackVel,autoBackDis,offectFlag)``"
    "描述", "焊丝寻位结束"
    "必选参数", "- ``refPos``： 1-基准点 2-接触点
    - ``searchVel``： 寻位速度 %
    - ``searchDis``： 寻位距离 mm
    - ``autoBackFlag``： 自动返回标志，0-不自动；-自动
    - ``autoBackVel``： 自动返回速度 %
    - ``autoBackDis``： 自动返回距离 mm
    - ``offectFlag``： 1-带偏移量寻位；2-示教点寻位"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

计算焊丝寻位偏移量
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetWireSearchOffset(seamType, method,varNameRef,varNameRes)``"
    "描述", "计算焊丝寻位偏移量"
    "必选参数", "- ``seamType``： 焊缝类型
    - ``method``： 计算方法
    - ``varNameRef``： 基准点1-6，“#”表示无点变量
    - ``varNameRes``： 接触点1-6，“#”表示无点变量"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``offsetFlag``： 0-偏移量直接叠加到指令点；1-偏移量需要对指令点进行坐标变换
    - ``offset``： 偏移位姿[x, y, z, a, b, c]"

等待焊丝寻位完成
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WireSearchWait(varname)``"
    "描述", "等待焊丝寻位完成"
    "必选参数", "- ``varName``： 接触点名称 “RES0” ~ “RES99”"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

焊丝寻位接触点写入数据库
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetPointToDatabase(varName,pos)``"
    "描述", "焊丝寻位接触点写入数据库"
    "必选参数", "- ``varName``： 接触点名称 “RES0” ~ “RES99”
    - ``pos``：接触点数据[x, y, x, a, b, c]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

机器人焊丝寻位代码示例
++++++++++++++++++++++++++++++++++
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

设置焊接电压渐变开始
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetVoltageGradualChangeStart(IOType, voltageStart, voltageEnd, AOIndex, blend)``"
    "描述", "设置焊接电压渐变开始"
    "必选参数", "- ``IOType``：控制类型；0-控制箱IO；1-数字通信协议(UDP);2-数字通信协议(ModbusTCP)
    - ``voltageStart``：起始焊接电压(V)
    - ``voltageEnd``：终止焊接电压(V)
    - ``AOIndex``：控制箱AO端口号(0-1)
    - ``blend``：是否平滑 0-不平滑；1-平滑"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置焊接电压渐变结束
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetVoltageGradualChangeEnd()``"
    "描述", "设置焊接电压渐变结束"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置焊接电流渐变开始
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetCurrentGradualChangeStart(IOType, currentStart, currentEnd, AOIndex, blend)``"
    "描述", "设置焊接电流渐变开始"
    "必选参数", "- ``IOType``：控制类型；0-控制箱IO；1-数字通信协议(UDP);2-数字通信协议(ModbusTCP)
    - ``currentStart``：起始焊接电流(A)
    - ``currentEnd``：终止焊接电流(A)
    - ``AOIndex``：控制箱AO端口号(0-1)
    - ``blend``：是否平滑 0-不平滑；1-平滑"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置焊接电流渐变结束
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetCurrentGradualChangeEnd()``"
    "描述", "设置焊接电流渐变结束"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

机器人焊接电流电压渐变代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    startdescPose = [-484.707, 276.996, -14.013, -37.657, -40.508, -1.548]
    startjointPos = [-45.421, -75.673, 93.627, -104.302, -87.938, 6.005]
    enddescPose = [-508.767, 137.109, -13.966, -37.639, -40.508, -1.559]
    endjointPos = [-32.768, -80.947, 100.254, -106.201, -87.201, 18.648]
    safedescPose = [-484.709, 294.436, 13.621, -37.660, -40.508, -1.545]
    safejointPos = [-46.604, -75.410, 89.109, -100.003, -88.012, 4.823]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    robot.WeldingSetCurrentRelation(0, 495, 1, 10, 0)
    robot.WeldingSetVoltageRelation(10, 45, 1, 10, 1)
    robot.WeldingSetVoltage(0, 25, 1, 0)  # ----设置电压
    robot.WeldingSetCurrent(0, 260, 0, 0)  # ----设置电流
    robot.MoveJ(joint_pos=safejointPos, tool=1, user=0, vel=5, acc=100)
    rtn = robot.WeldingSetCurrentGradualChangeStart(0, 260, 220, 0, 0)
    print("WeldingSetCurrentGradualChangeStart rtn is", rtn)
    rtn = robot.WeldingSetVoltageGradualChangeStart(0, 25, 22, 1, 0)
    print("WeldingSetVoltageGradualChangeStart rtn is", rtn)
    rtn = robot.ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0)
    print("ArcWeldTraceControl rtn is", rtn)
    robot.MoveJ(joint_pos=startjointPos, tool=1, user=0, vel=5, acc=100)
    robot.ARCStart(0, 0, 10000)
    robot.WeaveStart(0)
    robot.WeaveChangeStart(2, 1, 24, 36)
    robot.MoveL(desc_pos=enddescPose, tool=1, user=0, vel=100, ovl=2, acc=100)
    robot.ARCEnd(0, 0, 10000)
    robot.WeaveChangeEnd()
    robot.WeaveEnd(0)
    robot.ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0)
    robot.WeldingSetCurrentGradualChangeEnd()
    robot.WeldingSetVoltageGradualChangeEnd()

设置自定义摆动参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``CustomWeaveSetPara(id, pointNum, point, stayTime, frequency, incStayType, stationary)``"
    "描述", "设置自定义摆动参数"
    "必选参数", "- ``id``：自定义摆动编号：0-2
    - ``pointNum``：摆动点位个数 0-10
    - ``point``：移动端点数据x,y,z
    - ``stayTime``：摆动停留时间ms
    - ``frequency``：摆动频率 Hz
    - ``incStayType``：等待模式：0-周期不包含等待时间；1-周期包含等待时间
    - ``stationary``：摆动位置等待：0-等待时间内继续运动；1-等待时间内位置静止"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取自定义摆动参数
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``CustomWeaveGetPara(id)``"
    "描述", "获取自定义摆动参数"
    "必选参数", "- ``id``：自定义摆动编号：0-2"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``pointNum``：摆动点位个数 0-10
    - ``point``：移动端点数据x,y,z
    - ``stayTime``：摆动停留时间ms
    - ``frequency``：摆动频率 Hz
    - ``incStayType``：等待模式：0-周期不包含等待时间；1-周期包含等待时间
    - ``stationary``：摆动位置等待：0-等待时间内继续运动；1-等待时间内位置静止"

自定义摆动参数代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    point = [0.0] * 30
    point[0] = -3.0
    point[1] = -3.0
    point[2] = 0.0
    point[3] = -6.0
    point[4] = 0.0
    point[5] = 0.0
    point[6] = -3.0
    point[7] = 3.0
    point[8] = 0.0
    point[9] = 0.0
    point[10] = 0.0
    point[11] = 0.0
    stayTime = [0.0] * 10
    rtn = robot.CustomWeaveSetPara(2, 4, point, stayTime, 1.000, 0, 0)
    print(f"CustomWeaveSetPara rtn is {rtn}")
    time.sleep(1)
    pointNum = 0
    frequency = 0.0
    incStayType = 0
    stationary = 0
    rtn, pointNum, point, stayTime, frequency, incStayType, stationary = robot.CustomWeaveGetPara(2)
    print(f"pointNum is {pointNum}")
    for i in range(pointNum):
        print(f"point {i}, point x y z {point[i * 3 + 0]},{point[i * 3 + 1]},{point[i * 3 + 2]}")
    print(f"fre is {frequency}, stay is {incStayType},{stationary}")
    robot.WeaveSetPara(0, 9, 1.000000, 1, 5.000000, 6.000000, 5.000000, 50, 100, 100, 0, 1, 0.000000, 0.000000)
    desc_p1 = [-288.650, 367.807, 288.404, 0.000, -0.001, 0.001]
    desc_p2 = [-431.714, 367.815, 288.415, 0.001, 0.001, 0.000]
    desc_p3 = [-348.666, 427.798, 288.404, -0.000, -0.000, 0.001]
    j1 = [140.656, -84.560, -91.707, -93.734, 90.000, 50.655]
    j2 = [149.873, -98.298, -77.599, -94.103, 90.000, 59.873]
    j3 = [139.773, -96.173, -80.014, -93.814, 90.000, 49.772]
    epos = [0.0] * 4
    offset_pos = [0.0] * 6
    robot.MoveJ(joint_pos=j1, tool=3, user=0, vel=100)
    robot.WeaveStart(0)
    robot.Circle(desc_pos_p=desc_p3, tool_p=3, user_p=0, vel_p=50, desc_pos_t=desc_p2, tool_t=3, user_t=0, vel_t=50, oacc=10)
    robot.WeaveEnd(0)
    robot.MoveJ(joint_pos=j1, tool=3, user=0, vel=100)
    robot.WeaveStart(0)
    robot.MoveC(desc_pos_p=desc_p3, tool_p=3, user_p=0, vel_p=50, desc_pos_t=desc_p2, tool_t=3, user_t=0, vel_t=50)
    robot.WeaveEnd(0)
    robot.MoveJ(joint_pos=j1, tool=3, user=0, vel=100)
    robot.WeaveStart(0)
    robot.MoveL(desc_pos=desc_p2, tool=3, user=0, vel=100, ovl=10, speedPercent=100)
    robot.WeaveEnd(0)
    robot.CloseRPC()

激光焊机参数配置
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLaserWeldingParam(self, num, scanSpeed, scanWidth, peakPower, dutyCycle, Freq, io_type=1)``"
    "描述", "写入激光焊机10个工艺组中某一个的配置参数并配置给焊机"
    "必选参数", "
    - ``io_type``:通信类型 0-IO 1-UDP
    - ``Num``:需要设置的组号（1~10）
    - ``scanSpeed``:扫描速度
    - ``scanWidth``:扫描宽度
    - ``peakPower``:峰值功率
    - ``dutyCycle``:占空比
    - ``Freq``:频率
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置激光焊接开始停止
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLaserWeldingStartEnd(self, status, io_type=1, max_waittime=10000)``"
    "描述", "设置激光焊机开启关闭"
    "必选参数", "
    - ``io_type``:通信类型 0-IO 1-UDP
    - ``status``:控制字 0-收光 1-出光
    - ``max_waittime``:最大等待时间
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

激光焊机使能去使能
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLaserWeldingEnable(self, status, io_type=1)``"
    "描述", "激光焊机使能去使能"
    "必选参数", "
    - ``io_type``:通信类型 0-IO 1-UDP
    - ``status``:0-去使能 1-使能
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

激光焊机故障复位
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ResetLaserWeldingErr(self,status, io_type=1)``"
    "描述", "激光焊机故障复位"
    "必选参数", "
    - ``io_type``:通信类型 0-IO 1-UDP
    - ``status``:控制字 0-无效 1-故障复位
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取激光焊机运行状态
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetLaserWeldingRunningState(self, io_type=1)``"
    "描述", "获取激光焊机运行状态"
    "必选参数", "
    - ``io_type``:通信类型 0-IO 1-UDP
    - ``status``:控制字 0-停机 1-运行
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取激光焊机故障状态
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetLaserWeldingErrState(self, io_type=1)``"
    "描述", "获取激光焊机故障状态"
    "必选参数", "
    - ``io_type``:通信类型 0-IO 1-UDP
    - ``status``:0-无故障 1-存在故障
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取激光焊机配置参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetLaserWeldingParamTarget(self, num)``"
    "描述", "获取激光焊机10个工艺组中某一个的配置参数"
    "必选参数", "
    - ``Num``:需要设置的组号（1~10）
    - ``scanSpeed``:扫描速度
    - ``scanWidth``:扫描宽度
    - ``peakPower``:峰值功率
    - ``dutyCycle``:占空比
    - ``Freq``:频率
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取当前激光焊机生效的配置参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetLaserWeldingParamActual(self, io_type=1)``"
    "描述", "获取当前激光焊机生效的配置参数"
    "必选参数", "
    - ``io_type``:通信类型 0-IO 1-UDP
    - ``scanSpeed``:扫描速度
    - ``scanWidth``:扫描宽度
    - ``peakPower``:峰值功率
    - ``dutyCycle``:占空比
    - ``Freq``:频率
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

配置激光焊机扩展IO使能DO端口
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLaserWeldingEnableExtDoNum(self, ctrlModeDONum)``"
    "描述", "配置激光焊机扩展IO使能DO端口"
    "必选参数", "
    - ``ctrlModeDONum``:激光焊机使能的扩展DO端口号
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

配置激光焊机扩展IO启动DO端口
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLaserWeldingStartExtDoNum(self, ctrlModeDONum)``"
    "描述", "激光焊机设置扩展IO，启动的DO端口"
    "必选参数", "
    - ``ctrlModeDONum``:激光焊机启动（出光收光）的扩展DO端口号
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

配置激光焊机扩展IO故障复位DO端口
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLaserWeldingErrResetExtDoNum(self, ctrlModeDONum)``"
    "描述", "激光焊机设置扩展IO，故障复位的DO端口"
    "必选参数", "
    - ``ctrlModeDONum``:激光焊机故障复位的扩展DO端口号
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

配置激光焊机扩展IO运行状态（出光状态）DI端口
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLaserWeldingRunningStateExtDiNum(self, diNum)``"
    "描述", "配置激光焊机扩展IO运行状态（出光状态）DI端口"
    "必选参数", "
    - ``diNum``:配置激光焊机运行状态（出光状态）扩展DI端口
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

配置激光焊机扩展IO故障状态DI端口
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLaserWeldingErrStateExtDiNum(self, diNum)``"
    "描述", "配置激光焊机扩展IO故障状态DI端口"
    "必选参数", "
    - ``diNum``:配置激光焊机故障状态 扩展DI端口
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

激光焊接代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos: 

    from time import sleep
    from fairino import Robot
    import time

    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')

    def testLsaerWeld():
        robot.ExtDevLoadUDPDriver()
        time.sleep(1)

        robot.SetLaserWeldingParam(num = 3, scanSpeed = 2000, scanWidth = 3, peakPower = 1500, dutyCycle = 100, Freq = 1000, io_type=1)
        robot.SetLaserWeldingStartExtDoNum(ctrlModeDONum=1)

        robot.Mode(0)
        time.sleep(1)

        desc_pos1 = [-303.721, -206.960, 297.105, 152.209, 19.857, 109.166]
        desc_pos2 = [-301.575, -254.888, 284.786, 155.919, 26.946, 111.629]
        desc_safe = [-344.386, -280.830, 435.073, 173.835, 15.333, 124.931]
        jointPos1 = [9.827, -99.740, 120.088, -78.900, -77.241, -17.904]
        jointPos2 = [15.251, -96.456, 120.138, -84.664, -68.542, -17.843]
        jointSafe = [19.142, -98.078, 101.493, -83.078, -77.070, -17.794]

        error = robot.MoveL(desc_pos=desc_pos1,joint_pos=jointPos1, tool=1, user=0, vel=100, ovl= 2, acc=100)
        print("MoveL return:", error)
        robot.SetLaserWeldingStartEnd(1, io_type=1, max_waittime=10000)

        error = robot.MoveL(desc_pos=desc_pos2, joint_pos=jointPos2, tool=1, user=0, vel=100, ovl= 2, acc=100)
        print("MoveL return:", error)
        robot.SetLaserWeldingStartEnd(0, io_type=1, max_waittime=10000)

        error = robot.MoveL(desc_pos=desc_safe, joint_pos=jointSafe, tool=1, user=0, vel=100, ovl= 2, acc=100)
        print("MoveL return:", error)

        robot.Mode(1)
        time.sleep(1)

        # 关闭连接
        robot.CloseRPC()
        time.sleep(1)

    # 调用测试函数
    testLsaerWeld()

设置摆动结束回周期零点
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWeaveBackCenterConfig(self, flag)``"
    "描述", "设置摆动结束回周期零点"
    "必选参数", "
    - ``flag``: 摆动结束是否回周期零点；0-不回周期零点；1-回周期零点
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"    

获取摆动结束回周期零点参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetWeaveBackCenterConfig(self)``"
    "描述", "获取摆动结束回周期零点参数"
    "必选参数", "
    - ``flag``: 摆动结束是否回周期零点；0-不回周期零点；1-回周期零点
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"   

摆动结束回周期零点代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time

    def main():
        robot = Robot.RPC('192.168.58.2')
        time.sleep(0.5)  

        def callback(src_type, count, cmd_id, data_len, content):
            print(" cmd_id={} count={} data_len={} content={}".format(cmd_id, count, data_len, content))
            return 0

        robot.SetUDPCmdRpyCallback(callback)

        j1 = [9.000, -66.067, 67.706, -103.217, -90.151, 100.669]
        j2 = [-4.660, -107.973, 103.734, -76.214, -89.999, 90.886]
        j3 = [-36.762, -77.380, 91.364, -127.159, -90.024, 54.833]
        j4 = [-62.875, -89.460, 86.437, -77.030, -90.012, 31.539]

    
        desc_pos1 = [-654.129, -235.344, 246.543, 6.010, -11.535, -176.787]
        desc_pos2 = [-273.710, -100.871, 280.935, 5.692, 9.522, 179.512]
        desc_pos3 = [-566.093, 311.278, 215.008, -10.453, -17.486, -174.209]
        desc_pos4 = [-246.558, 328.240, 292.173, 13.912, 4.437, -179.067]

        offset_pos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        epos = [0.0, 0.0, 0.0, 0.0]

        tool = 2
        user = 0
        vel = 100.0
        acc = 100.0
        ovl = 20.0
        oacc = 100.0
        blendT = 0.0
        blendR = 0.0
        flag = 0
        search = 0
        blendMode = 0
        velAccMode = 0

        robot.SetSpeed(1)

        robot.WeaveEnd(0)

        rtn = robot.SetWeaveBackCenterConfig(1)
        print(f"SetWeaveBackCenterConfig rtn is {rtn}")

        rtn, weaveBackConfig = robot.GetWeaveBackCenterConfig()
        print(f"GetWeavebackCenterConfig {weaveBackConfig}")

        rtn = robot.MoveJ(joint_pos=j1, desc_pos=desc_pos1, tool=tool, user=user,
                        vel=vel, acc=acc, ovl=100.0, exaxis_pos=epos,
                        blendT=blendT, offset_flag=flag, offset_pos=offset_pos)
        print(f"MoveJ rtn is {rtn}")

        robot.WeaveStart(0)

        robot.NewSplineStart(0, 6000)

        rtn = robot.NewSplinePoint(joint_pos=j1, desc_pos=desc_pos1, tool=tool, user=user,lastFlag=0,
                                vel=vel, acc=acc, ovl=ovl, blendR=-1, config=0)
        print(f"NewSplinePoint 1 rtn is {rtn}")

        rtn = robot.NewSplinePoint(joint_pos=j2, desc_pos=desc_pos2, tool=tool, user=user,lastFlag=0,
                                vel=vel, acc=acc, ovl=ovl, blendR=-1, config=0)
        print(f"NewSplinePoint 2 rtn is {rtn}")

        rtn = robot.NewSplinePoint(joint_pos=j3, desc_pos=desc_pos3, tool=tool, user=user,lastFlag=0,
                                vel=vel, acc=acc, ovl=ovl, blendR=-1, config=0)
        print(f"NewSplinePoint 3 rtn is {rtn}")

        rtn = robot.NewSplinePoint(joint_pos=j4, desc_pos=desc_pos4, tool=tool, user=user,lastFlag=1,
                                vel=vel, acc=acc, ovl=ovl, blendR=-1, config=1)
        print(f"NewSplinePoint 4 rtn is {rtn}")

        robot.NewSplineEnd()

        robot.CloseRPC()


    if __name__ == "__main__":
        main()