扩展轴
=================

.. toctree:: 
    :maxdepth: 5

设置485扩展轴参数
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置485扩展轴参数
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @param [in] servoCompany 伺服驱动器厂商，1-戴纳泰克
    * @param [in] servoModel 伺服驱动器型号，1-FD100-750C
    * @param [in] servoSoftVersion 伺服驱动器软件版本，1-V1.0
    * @param [in] servoResolution 编码器分辨率
    * @param [in] axisMechTransRatio 机械传动比
    * @return 错误码 
    */
    int AuxServoSetParam(int servoId, int servoCompany, int servoModel, int servoSoftVersion, int servoResolution, double axisMechTransRatio);
    
获取485扩展轴参数
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取485扩展轴配置参数
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @param [out] servoCompany 伺服驱动器厂商，1-戴纳泰克
    * @param [out] servoModel 伺服驱动器型号，1-FD100-750C
    * @param [out] servoSoftVersion 伺服驱动器软件版本，1-V1.0
    * @param [out] servoResolution 编码器分辨率
    * @param [out] axisMechTransRatio 机械传动比
    * @return 错误码 
    */
    int AuxServoGetParam(int servoId, ref int servoCompany, ref int servoModel, ref int servoSoftVersion, ref int servoResolution, ref double axisMechTransRatio);
    
设置485扩展轴使能/去使能
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置485扩展轴使能/去使能
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @param [in] status 使能状态，0-去使能， 1-使能
    * @return 错误码 
    */
    int AuxServoEnable(int servoId, int status);
        
设置485扩展轴控制模式
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置485扩展轴控制模式
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @param [in] mode 控制模式，0-位置模式，1-速度模式
    * @return 错误码 
    */
    int AuxServoSetControlMode(int servoId, int mode);

代码示例
++++++++++
.. versionadded:: C#SDK-v1.0.6
    
.. code-block:: c#
    :linenos:

    private void btnWeldStart_Click(object sender, EventArgs e)
    {
    Robot robot = new Robot();
    robot.RPC("192.168.58.2");

    robot.AuxServoSetParam(1, 1, 1, 1, 131072, 36);//设置配置参数
    int ID = -1, company = -1, model = -1, soft = -1, servoResolution= -1;
    int radio = -1;
        robot.AuxServoGetParam(1, ref company, ref model, ref soft, ref servoResolution, ref radio);//获取配置参数
        
        Thread.Sleep(100);
        robot.AuxServoEnable(1, 0);//去使能伺服
        Thread.Sleep(100);
        robot.AuxServoSetControlMode(1, 0);//设置位置模式
        Thread.Sleep(100);
        robot.AuxServoEnable(1, 1);//使能伺服
    }

设置485扩展轴回零
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置485扩展轴回零
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @param [in] mode 回零模式，1-当前位置回零；2-负限位回零；3-正限位回零
    * @param [in] searchVel 回零速度，mm/s或°/s
    * @param [in] latchVel 箍位速度，mm/s或°/s
    * @return 错误码 
    */
    int AuxServoHoming(int servoId, int mode, double searchVel, double latchVel);

设置485扩展轴目标位置(位置模式)
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置485扩展轴目标位置(位置模式)
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @param [in] pos 目标位置，mm或°
    * @param [in] speed 目标速度，mm/s或°/s
    * @return 错误码 
    */
    int AuxServoSetTargetPos(int servoId, double pos, double speed);

设置485扩展轴目标速度(速度模式)
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置485扩展轴目标速度(速度模式)
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @param [in] speed 目标速度，mm/s或°/s
    * @return 错误码 
    */
    int AuxServoSetTargetSpeed(int servoId, double speed);

代码示例
++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    private void btnWeldStart_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        robot.AuxServoEnable(1, 0);//去使能
        Thread.Sleep(100);
        robot.AuxServoSetControlMode(1, 0);//设置位置模式
        Thread.Sleep(100);
        robot.AuxServoEnable(1, 1);//使能
        Thread.Sleep(100);
        robot.AuxServoHoming(1, 1, 20, 5);//回零
        Thread.Sleep(4000);//伺服回零需要一定的时间
                
        robot.AuxServoSetTargetPos(1, 1000, 100);//设置目标位置
        Thread.Sleep(1000);
        robot.AuxServoSetTargetPos(1, 0, 100);//再次设置目标位置
        Thread.Sleep(1000);

        robot.AuxServoEnable(1, 0);//去使能
        Thread.Sleep(100);
        robot.AuxServoSetControlMode(1, 1);//设置速度模式
        Thread.Sleep(100);
        robot.AuxServoEnable(1, 1);//使能
        Thread.Sleep(100);
        robot.AuxServoHoming(1, 1, 20, 5);//回零
        Thread.Sleep(4000);//回零需要一定时间
        robot.AuxServoSetTargetSpeed(1, 50);//设置目标速度
        Thread.Sleep(3000);

        robot.AuxServoSetTargetSpeed(1, -300);//设置目标速度
        Thread.Sleep(3000);
        robot.AuxServoSetTargetSpeed(1, 0);//伺服停止
        Thread.Sleep(100);
    }
    
设置485扩展轴目标转矩(力矩模式)--暂未开放
++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置485扩展轴目标转矩(力矩模式)--暂未开放
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @param [in] torque 目标力矩，Nm
    * @return 错误码 
    */
    int AuxServoSetTargetTorque(int servoId, double torque);
        
清除485扩展轴错误信息
++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 清除485扩展轴错误信息
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @return 错误码 
    */
    int AuxServoClearError(int servoId);

获取485扩展轴伺服状态
++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取485扩展轴伺服状态
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @param [out] servoErrCode 伺服驱动器故障码
    * @param [out] servoState 伺服驱动器状态  bit0:0-未使能；1-使能;  bit1:0-未运动；1-正在运动;  bit2 0-正限位未触发；1-正限位触发；bit3 0-负限位未触发；1-负限位触发；bit4 0-未定位完成；1-定位完成；  bit5：0-未回零；1-回零完成
    * @param [out] servoPos 伺服当前位置 mm或°
    * @param [out] servoSpeed 伺服当前速度 mm/s或°/s
    * @param [out] servoTorque 伺服当前转矩Nm
    * @return 错误码 
    */
    int AuxServoGetStatus(int servoId, ref int servoErrCode, ref int servoState, ref double servoPos, ref double servoSpeed, ref double servoTorque);
    
设置状态反馈中485扩展轴数据轴号
++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6
    
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置状态反馈中485扩展轴数据轴号
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @return 错误码 
    */
    int AuxServosetStatusID(int servoId);

代码示例
+++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    private void btnWeldStart_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

            robot.AuxServoClearError(1);
        int errCode = 0;
        int servoState = 0;
        double pos = 0;
        double speed = 0;
        double torque = 0;
        robot.AuxServoGetStatus(1, ref errCode, ref servoState, ref pos, ref speed, ref torque);

        robot.AuxServosetStatusID(1);
        ROBOT_STATE_PKG pKG = new ROBOT_STATE_PKG();
        robot.GetRobotRealTimeState(ref pKG);
        Console.WriteLine($"the state is {pKG.auxState.servoPos}");
    }