机器人焊接
=============

.. toctree:: 
    :maxdepth: 5

焊接开始
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 焊接开始
    * @param [in] ioType io类型 0-控制器IO； 1-扩展IO
    * @param [in] arcNum 焊机配置文件编号
    * @param [in] timeout 起弧超时时间
    * @return 错误码
    */
    int ARCStart(int ioType, int arcNum, int timeout);

焊接结束
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 焊接结束
    * @param [in] ioType io类型 0-控制器IO； 1-扩展IO
    * @param [in] arcNum 焊机配置文件编号
    * @param [in] timeout 熄弧超时时间
    * @return 错误码
    */
    int ARCEnd(int ioType, int arcNum, int timeout);

设置焊接电流与输出模拟量对应关系
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 设置焊接电流与输出模拟量对应关系
    * @param [in] currentMin 焊接电流-模拟量输出线性关系左侧点电流值(A)
    * @param [in] currentMax 焊接电流-模拟量输出线性关系右侧点电流值(A)
    * @param [in] outputVoltageMin 焊接电流-模拟量输出线性关系左侧点模拟量输出电压值(V)
    * @param [in] outputVoltageMax 焊接电流-模拟量输出线性关系右侧点模拟量输出电压值(V)
    * @return 错误码
    */
    int WeldingSetCurrentRelation(double currentMin, double currentMax, double outputVoltageMin, double outputVoltageMax);

设置焊接电压与输出模拟量对应关系
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 设置焊接电压与输出模拟量对应关系
    * @param [in] weldVoltageMin 焊接电压-模拟量输出线性关系左侧点焊接电压值(A)
    * @param [in] weldVoltageMax 焊接电压-模拟量输出线性关系右侧点焊接电压值(A)
    * @param [in] outputVoltageMin 焊接电压-模拟量输出线性关系左侧点模拟量输出电压值(V)
    * @param [in] outputVoltageMax 焊接电压-模拟量输出线性关系右侧点模拟量输出电压值(V)
    * @return 错误码
    */
    int WeldingSetVoltageRelation(double weldVoltageMin, double weldVoltageMax, double outputVoltageMin, double outputVoltageMax);

获取焊接电流与输出模拟量对应关系
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 获取焊接电流与输出模拟量对应关系
    * @param [out] currentMin 焊接电流-模拟量输出线性关系左侧点电流值(A)
    * @param [out] currentMax 焊接电流-模拟量输出线性关系右侧点电流值(A)
    * @param [out] outputVoltageMin 焊接电流-模拟量输出线性关系左侧点模拟量输出电压值(V)
    * @param [out] outputVoltageMax 焊接电流-模拟量输出线性关系右侧点模拟量输出电压值(V)
    * @return 错误码
    */
    int WeldingGetCurrentRelation(ref double currentMin, ref double currentMax, ref double outputVoltageMin, ref double outputVoltageMax);

获取焊接电压与输出模拟量对应关系
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 获取焊接电压与输出模拟量对应关系
    * @param [out] weldVoltageMin 焊接电压-模拟量输出线性关系左侧点焊接电压值(A)
    * @param [out] weldVoltageMax 焊接电压-模拟量输出线性关系右侧点焊接电压值(A)
    * @param [out] outputVoltageMin 焊接电压-模拟量输出线性关系左侧点模拟量输出电压值(V)
    * @param [out] outputVoltageMax 焊接电压-模拟量输出线性关系右侧点模拟量输出电压值(V)
    * @return 错误码
    */
    int WeldingGetVoltageRelation(ref double weldVoltageMin, ref double weldVoltageMax, ref double outputVoltageMin, ref double outputVoltageMax);

设置焊接电流
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 设置焊接电流
    * @param [in] ioType 控制IO类型 0-控制箱IO；1-扩展IO
    * @param [in] current 焊接电流值(A)
    * @param [in] AOIndex 焊接电流控制箱模拟量输出端口(0-1)
    * @return 错误码
    */
    int WeldingSetCurrent(int ioType, double current, int AOIndex);

设置焊接电压
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 设置焊接电压
    * @param [in] ioType 控制IO类型 0-控制箱IO；1-扩展IO
    * @param [in] voltage 焊接电压值(A)
    * @param [in] AOIndex 焊接电压控制箱模拟量输出端口(0-1)
    * @return 错误码
    */
    int WeldingSetVoltage(int ioType, double voltage, int AOIndex);

设置摆动参数
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 设置摆动参数
    * @param [in] weaveNum 摆焊参数配置编号
    * @param [in] weaveType 摆动类型 0-平面三角波摆动；1-垂直L型三角波摆动；2-顺时针圆形摆动；3-逆时针圆形摆动；4-平面正弦波摆动；5-垂直L型正弦波摆动；6-垂直三角波摆动；7-垂直正弦波摆动
    * @param [in] weaveFrequency 摆动频率(Hz)
    * @param [in] weaveIncStayTime 等待模式 0-周期不包含等待时间；1-周期包含等待时间
    * @param [in] weaveRange 摆动幅度(mm)
    * @param [in] weaveLeftStayTime 摆动左停留时间(ms)
    * @param [in] weaveRightStayTime 摆动右停留时间(ms)
    * @param [in] weaveCircleRadio 圆形摆动-回调比率(0-100%)
    * @param [in] weaveStationary 摆动位置等待，0-等待时间内位置继续移动；1-等待时间内位置静止
    * @return 错误码
    */
    int WeaveSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary);

即时设置摆动参数
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 即时设置摆动参数
    * @param [in] weaveNum 摆焊参数配置编号
    * @param [in] weaveType 摆动类型 0-平面三角波摆动；1-垂直L型三角波摆动；2-顺时针圆形摆动；3-逆时针圆形摆动；4-平面正弦波摆动；5-垂直L型正弦波摆动；6-垂直三角波摆动；7-垂直正弦波摆动
    * @param [in] weaveFrequency 摆动频率(Hz)
    * @param [in] weaveIncStayTime 等待模式 0-周期不包含等待时间；1-周期包含等待时间
    * @param [in] weaveRange 摆动幅度(mm)
    * @param [in] weaveLeftStayTime 摆动左停留时间(ms)
    * @param [in] weaveRightStayTime 摆动右停留时间(ms)
    * @param [in] weaveCircleRadio 圆形摆动-回调比率(0-100%)
    * @param [in] weaveStationary 摆动位置等待，0-等待时间内位置继续移动；1-等待时间内位置静止
    * @return 错误码
    */
    int WeaveOnlineSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary);

摆动开始
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 摆动开始
    * @param [in] weaveNum 摆焊参数配置编号
    * @return 错误码
    */
    int WeaveStart(int weaveNum);

摆动结束
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 摆动结束
    * @param [in] weaveNum 摆焊参数配置编号
    * @return 错误码
    */
    int WeaveEnd(int weaveNum);

正向送丝
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 正向送丝
    * @param [in] ioType io类型  0-控制器IO；1-扩展IO
    * @param [in] wireFeed 送丝控制  0-停止送丝；1-送丝
    * @return 错误码
    */
    int SetForwardWireFeed(int ioType, int wireFeed); 	

反向送丝
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 反向送丝
    * @param [in] ioType io类型  0-控制器IO；1-扩展IO
    * @param [in] wireFeed 送丝控制  0-停止送丝；1-送丝
    * @return 错误码
    */
    int SetReverseWireFeed(int ioType, int wireFeed);

送气
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 送气
    * @param [in] ioType io类型  0-控制器IO；1-扩展IO
    * @param [in] airControl 送气控制  0-停止送气；1-送气
    * @return 错误码
    */
    int SetAspirated(int ioType, int airControl);

段焊
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /** 
    * @brief 段焊开始
    * @param [in] startDesePos 起始点笛卡尔位置
    * @param [in] endDesePos 结束点笛卡尔位姿
    * @param [in] startJPos 起始点关节位姿
    * @param [in] endJPos 结束点关节位姿
    * @param [in] weldLength 焊接段长度(mm)
    * @param [in] noWeldLength 非焊接段长度(mm)
    * @param [in] weldIOType 焊接IO类型(0-控制箱IO；1-扩展IO)
    * @param [in] arcNum 焊机配置文件编号
    * @param [in] weldTimeout 起/收弧超时时间
    * @param [in] isWeave 是否摆动
    * @param [in] weaveNum 摆焊参数配置编号
    * @param [in] tool 工具号
    * @param [in] user 工件号
    * @param [in] vel  速度百分比，范围[0~100]
    * @param [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm	 
    * @param [in] epos  扩展轴位置，单位mm
    * @param [in] search  0-不焊丝寻位，1-焊丝寻位
    * @param [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos  位姿偏移量
    * @return 错误码 
    */
    int SegmentWeldStart(DescPose startDesePos, DescPose endDesePos, JointPos startJPos, JointPos endJPos, double weldLength, double noWeldLength, int weldIOType, int arcNum, int weldTimeout,bool isWeave, int weaveNum, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos epos, byte search, byte offset_flag, DescPose offset_pos);

代码示例
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    private void btnWeldStart_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");
        DescPose startdescPose = new DescPose(-525.55, 562.3, 417.199, -178.325, 0.847, 31.109);
        JointPos startjointPos = new JointPos(-58.978, -76.817, 112.494, -127.348, -89.145, -0.063);
        DescPose enddescPose = new DescPose(-345.155, 535.733, 421.269, 179.475, 0.571, 18.332);
        JointPos endjointPos = new JointPos(-71.746, -87.177, 123.953, -126.25, -89.429, -0.089);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        robot.WeldingSetCurrentRelation(0, 400, 0, 10);
        robot.WeldingSetVoltageRelation(0, 40, 0, 10);
        double curmin = 0;
        double curmax = 0;
        double vurvolmin = 0;
        double curvolmax = 0;
        double volmax = 0;
        double volmin = 0;
        double volvolmin = 0;
        double volvolmax = 0;

        robot.WeldingGetCurrentRelation(ref curmin, ref curmax, ref vurvolmin, ref curvolmax);
        robot.WeldingGetVoltageRelation(ref volmin, ref volmax, ref volvolmin, ref volvolmax);

        robot.WeldingSetCurrent(0, 100, 0); 
        robot.WeldingSetVoltage(0, 19, 1);

        robot.WeaveSetPara(0,0,1,0,10,100,100,0,0);

        robot.SetForwardWireFeed(0, 1);
        Thread.Sleep(1000);
        robot.SetForwardWireFeed(0, 0);
        robot.SetReverseWireFeed(0, 1);
        Thread.Sleep(1000);
        robot.SetReverseWireFeed(0, 0);
        robot.SetAspirated(0, 1);
        Thread.Sleep(1000);
        robot.SetAspirated(0, 0);

        robot.SetSpeed(5);
        robot.MoveL(startjointPos, startdescPose, 1, 0, 100, 100, 100, 0, exaxisPos, 0, 0, offdese);
        robot.ARCStart(0, 0, 1000);
        robot.WeaveStart(0);
        robot.MoveL(endjointPos, enddescPose, 1, 0, 100, 100, 100, 0, exaxisPos, 0, 0, offdese);
        robot.ARCEnd(0, 0, 1000);
        robot.WeaveEnd(0);
    }

焊丝寻位开始
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief  焊丝寻位开始
    * @param  [in] refPos  1-基准点 2-接触点
    * @param  [in] searchVel   寻位速度 %
    * @param  [in] searchDis  寻位距离 mm
    * @param  [in] autoBackFlag 自动返回标志，0-不自动；-自动
    * @param  [in] autoBackVel  自动返回速度 %
    * @param  [in] autoBackDis  自动返回距离 mm
    * @param  [in] offectFlag  1-带偏移量寻位；2-示教点寻位
    * @return  错误码
    */
    int WireSearchStart(int refPos, double searchVel, int searchDis, int autoBackFlag, double autoBackVel, int autoBackDis, int offectFlag);

焊丝寻位结束
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief  焊丝寻位结束
    * @param  [in] refPos  1-基准点 2-接触点
    * @param  [in] searchVel   寻位速度 %
    * @param  [in] searchDis  寻位距离 mm
    * @param  [in] autoBackFlag 自动返回标志，0-不自动；-自动
    * @param  [in] autoBackVel  自动返回速度 %
    * @param  [in] autoBackDis  自动返回距离 mm
    * @param  [in] offectFlag  1-带偏移量寻位；2-示教点寻位
    * @return  错误码
    */
    int WireSearchEnd(int refPos, double searchVel, int searchDis, int autoBackFlag, double autoBackVel, int autoBackDis, int offectFlag);

计算焊丝寻位偏移量
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief  计算焊丝寻位偏移量
    * @param  [in] seamType  焊缝类型
    * @param  [in] method   计算方法
    * @param  [in] varNameRef 基准点1-6，“#”表示无点变量
    * @param  [in] varNameRes 接触点1-6，“#”表示无点变量
    * @param  [out] offectFlag 0-偏移量直接叠加到指令点；1-偏移量需要对指令点进行坐标变换
    * @param  [out] offect 偏移位姿[x, y, z, a, b, c]
    * @return  错误码
    */
    int GetWireSearchOffset(int seamType, int method, string[] varNameRef, string[] varNameRes, ref int offsetFlag, ref DescPose offset);

等待焊丝寻位完成
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief  等待焊丝寻位完成
    * @return  错误码
    */
    int WireSearchWait(string name);

焊丝寻位接触点写入数据库
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief  焊丝寻位接触点写入数据库
    * @param  [in] varName  接触点名称 “RES0” ~ “RES99”
    * @param  [in] pos  接触点数据[x, y, x, a, b, c]
    * @return  错误码
    */
    int SetPointToDatabase(string varName, DescPose pos);

电弧跟踪控制
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief  电弧跟踪控制
    * @param  [in] flag 开关，0-关；1-开
    * @param  [in] dalayTime 滞后时间，单位ms
    * @param  [in] isLeftRight 左右偏差补偿
    * @param  [in] klr 左右调节系数(灵敏度)
    * @param  [in] tStartLr 左右开始补偿时间cyc
    * @param  [in] stepMaxLr 左右每次最大补偿量 mm
    * @param  [in] sumMaxLr 左右总计最大补偿量 mm
    * @param  [in] isUpLow 上下偏差补偿
    * @param  [in] kud 上下调节系数(灵敏度)
    * @param  [in] tStartUd 上下开始补偿时间cyc
    * @param  [in] stepMaxUd 上下每次最大补偿量 mm
    * @param  [in] sumMaxUd 上下总计最大补偿量
    * @param  [in] axisSelect 上下坐标系选择，0-摆动；1-工具；2-基座
    * @param  [in] referenceType 上下基准电流设定方式，0-反馈；1-常数
    * @param  [in] referSampleStartUd 上下基准电流采样开始计数(反馈)，cyc
    * @param  [in] referSampleCountUd 上下基准电流采样循环计数(反馈)，cyc
    * @param  [in] referenceCurrent 上下基准电流mA
    * @return  错误码
    */
    int ArcWeldTraceControl(int flag, double delaytime, int isLeftRight, double klr, double tStartLr, double stepMaxLr, double sumMaxLr, int isUpLow, double kud, double tStartUd, double stepMaxUd, double sumMaxUd, int axisSelect, int referenceType, double referSampleStartUd, double referSampleCountUd, double referenceCurrent);

电弧跟踪AI通带选择
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief  电弧跟踪AI通带选择
    * @param  [in] channel 电弧跟踪AI通带选择,[0-3]
    * @return  错误码
    */
    int ArcWeldTraceExtAIChannelConfig(int channel);

仿真摆动开始
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief  仿真摆动开始
    * @param  [in] weaveNum  摆动参数编号
    * @return  错误码
    */
    int WeaveStartSim(int weaveNum);

仿真摆动结束
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief  仿真摆动结束
    * @param  [in] weaveNum  摆动参数编号
    * @return  错误码
    */
    int WeaveEndSim(int weaveNum);

开始轨迹检测预警(不运动)
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief  开始轨迹检测预警(不运动)
    * @param  [in] weaveNum   摆动参数编号
    * @return  错误码
    */
    int WeaveInspectStart(int weaveNum);

结束轨迹检测预警(不运动)
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 结束轨迹检测预警(不运动)
    * @param  [in] weaveNum   摆动参数编号
    * @return  错误码
    */
    int WeaveInspectEnd(int weaveNum);

扩展IO-配置焊机气体检测信号
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 扩展IO-配置焊机气体检测信号
    * @param  [in] DONum  气体检测信号扩展DO编号
    * @return  错误码
    */
    int SetAirControlExtDoNum(int DONum);

扩展IO-配置焊机起弧信号
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 扩展IO-配置焊机起弧信号
    * @param  [in] DONum  焊机起弧信号扩展DO编号
    * @return  错误码
    */
    int SetArcStartExtDoNum(int DONum);

扩展IO-配置焊机反向送丝信号
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 扩展IO-配置焊机反向送丝信号
    * @param  [in] DONum  反向送丝信号扩展DO编号
    * @return  错误码
    */
    int SetWireReverseFeedExtDoNum(int DONum);

扩展IO-配置焊机正向送丝信号
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 扩展IO-配置焊机正向送丝信号
    * @param  [in] DONum  正向送丝信号扩展DO编号
    * @return  错误码
    */
    int SetWireForwardFeedExtDoNum(int DONum);

扩展IO-配置焊机起弧成功信号
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 扩展IO-配置焊机起弧成功信号
    * @param  [in] DINum  起弧成功信号扩展DI编号
    * @return  错误码
    */
    int SetArcDoneExtDiNum(int DINum);

扩展IO-配置焊机准备信号
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 扩展IO-配置焊机准备信号
    * @param  [in] DINum  焊机准备信号扩展DI编号
    * @return  错误码
    */
    int SetWeldReadyExtDiNum(int DINum);

扩展IO-配置焊接中断恢复信号
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 扩展IO-配置焊接中断恢复信号
    * @param  [in] reWeldDINum  焊接中断后恢复焊接信号扩展DI编号
    * @param  [in] abortWeldDINum  焊接中断后退出焊接信号扩展DI编号
    * @return  错误码
    */
    nt SetExtDIWeldBreakOffRecover(int reWeldDINum, int abortWeldDINum);

电弧追踪 + 多层多道补偿开启
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 电弧追踪 + 多层多道补偿开启
    * @return 错误码
    */
    int ArcWeldTraceReplayStart();

电弧追踪 + 多层多道补偿关闭
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

        /**
         * @brief 电弧追踪 + 多层多道补偿关闭
         * @return 错误码
         */
    int ArcWeldTraceReplayEnd();

偏移量坐标变化-多层多道焊
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

     /**
     * @brief 偏移量坐标变化-多层多道焊
     * @param [in] pointO 基准点笛卡尔位姿
     * @param [in] pointX 基准点X向偏移方向点笛卡尔位姿
     * @param [in] pointZ 基准点Z向偏移方向点笛卡尔位姿
     * @param [in] dx x方向偏移量(mm)
     * @param [in] dz z方向偏移量(mm)
     * @param [in] dry 绕y轴偏移量(°)
     * @param [out] offset 计算结果偏移量
     * @return 错误码
     */
    int MultilayerOffsetTrsfToBase(DescTran pointO, DescTran pointX, DescTran pointZ, double dx, double dz, double dry, ref DescPose offset);

设置机器人焊接电弧意外中断检测参数
++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 设置机器人焊接电弧意外中断检测参数
    * @param [in] checkEnable 是否使能检测；0-不使能；1-使能
    * @param [in] arcInterruptTimeLength 电弧中断确认时长(ms)
    * @return 错误码
    */
    int WeldingSetCheckArcInterruptionParam(int checkEnable, int arcInterruptTimeLength)

获取机器人焊接电弧意外中断检测参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 获取机器人焊接电弧意外中断检测参数
    * @param [out] checkEnable 是否使能检测；0-不使能；1-使能
    * @param [out] arcInterruptTimeLength 电弧中断确认时长(ms)
    * @return 错误码
    */
    int WeldingGetCheckArcInterruptionParam(ref int checkEnable, ref int arcInterruptTimeLength)

设置机器人焊接中断恢复参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 设置机器人焊接中断恢复参数
    * @param[in] enable 是否使能焊接中断恢复
    * @param[in] length 焊缝重叠距离(mm)
    * @param[in] velocity 机器人回到再起弧点速度百分比(0-100)
    * @param[in] moveType 机器人运动到再起弧点方式；0-LIN；1-PTP
    * @return 错误码
    */
    int WeldingSetReWeldAfterBreakOffParam(int enable, double length, double velocity, int moveType)

获取机器人焊接中断恢复参数
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 获取机器人焊接中断恢复参数
    * @param [out] enable 是否使能焊接中断恢复
    * @param [out] length 焊缝重叠距离(mm)
    * @param [out] velocity 机器人回到再起弧点速度百分比(0-100)
    * @param [out] moveType 机器人运动到再起弧点方式；0-LIN；1-PTP
    * @return 错误码
    */
    int WeldingGetReWeldAfterBreakOffParam(ref int enable, ref double length, ref double velocity, ref int moveType)

设置机器人焊接中断后恢复焊接
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 设置机器人焊接中断后恢复焊接
    * @return 错误码
    */
    int WeldingStartReWeldAfterBreakOff()

设置机器人焊接中断后退出焊接
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 设置机器人焊接中断后退出焊接
    * @return 错误码
    */
    int WeldingAbortWeldAfterBreakOff()

代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    private void button7_Click(object sender, EventArgs e)
    {
        int rtn = -1;
        rtn = robot.WeldingSetCheckArcInterruptionParam(1, 200);
        Console.WriteLine("WeldingSetCheckArcInterruptionParam  {0}", rtn);
        rtn = robot.WeldingSetReWeldAfterBreakOffParam(1, 5.7, 98.2, 0);
        Console.WriteLine("WeldingSetReWeldAfterBreakOffParam {0}", rtn);
        int enable = 0;
        double length = 0;
        double velocity = 0;
        int moveType = 0;
        int checkEnable = 0;
        int arcInterruptTimeLength = 0;
        rtn = robot.WeldingGetCheckArcInterruptionParam(ref checkEnable, ref arcInterruptTimeLength);
        Console.WriteLine($"WeldingGetCheckArcInterruptionParam  checkEnable {checkEnable} - arcInterruptTimeLength {arcInterruptTimeLength}");

        rtn = robot.WeldingGetReWeldAfterBreakOffParam(ref enable, ref length, ref velocity,ref moveType);
        Console.WriteLine("WeldingGetReWeldAfterBreakOffParam  enable = {0}, length = {1}, velocity = {2}, moveType = {3}", enable, length, velocity, moveType);

        robot.ProgramLoad("/fruser/test.lua");
        robot.ProgramRun();

        Thread.Sleep(5000);

        while (true)
        {
            ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG { };
            robot.GetRobotRealTimeState(ref pkg);
            Console.WriteLine("welding breakoff state is     {0}", pkg.weldingBreakOffState.breakOffState);
            if (pkg.weldingBreakOffState.breakOffState == 1)
            {
                Console.WriteLine("welding breakoff ! \n");
                Thread.Sleep(2000);
                rtn = robot.WeldingStartReWeldAfterBreakOff();
                Console.WriteLine("WeldingStartReWeldAfterBreakOff    %d\n", rtn);
                break;
            }
            Thread.Sleep(100);
        }
    }