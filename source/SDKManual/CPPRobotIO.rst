机器人IO
============

.. toctree:: 
    :maxdepth: 5

设置控制箱数字量输出
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置控制箱数字量输出
    * @param  [in] id  io编号，范围[0~15]
    * @param  [in] status 0-关，1-开
    * @param  [in] smooth 0-不平滑， 1-平滑
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  错误码
    */
    errno_t  SetDO(int id, uint8_t status, uint8_t smooth, uint8_t block);

设置工具数字量输出
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置工具数字量输出
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in] status 0-关，1-开
    * @param  [in] smooth 0-不平滑， 1-平滑
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  错误码
    */
    errno_t  SetToolDO(int id, uint8_t status, uint8_t smooth, uint8_t block);

设置控制箱模拟量输出
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置控制箱模拟量输出
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in] value 电流或电压值百分比，范围[0~100]对应电流值[0~20mA]或电压[0~10V]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  错误码
    */
    errno_t  SetAO(int id, float value, uint8_t block);

设置工具模拟量输出
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置工具模拟量输出
    * @param  [in] id  io编号，范围[0]
    * @param  [in] value 电流或电压值百分比，范围[0~100]对应电流值[0~20mA]或电压[0~10V]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  错误码
    */
    errno_t  SetToolAO(int id, float value, uint8_t block);

设置数字量、模拟量输出代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestAODO(void)
     {
         ROBOT_STATE_PKG pkg = {};
         FRRobot robot;
         robot.LoggerInit();
         robot.SetLoggerLevel(1);
         int rtn = robot.RPC("192.168.58.2");
         if (rtn != 0)
         {
             return -1;
         }
         robot.SetReConnectParam(true, 30000, 500);
         uint8_t status = 1;
         uint8_t smooth = 0;
         uint8_t block = 0;
         for (int i = 0; i < 16; i++)
         {
             robot.SetDO(i, status, smooth, block);
             robot.Sleep(300);
         }
         status = 0;
         for (int i = 0; i < 16; i++)
         {
             robot.SetDO(i, status, smooth, block);
             robot.Sleep(300);
         }
         status = 1;
         for (int i = 0; i < 2; i++)
         {
             robot.SetToolDO(i, status, smooth, block);
             robot.Sleep(1000);
         }
         status = 0;
         for (int i = 0; i < 2; i++)
         {
             robot.SetToolDO(i, status, smooth, block);
             robot.Sleep(1000);
         }
         for (int i = 0; i < 100; i++)
         {
             robot.SetAO(0, i * 40.96, block);
             robot.Sleep(30);
         }
         for (int i = 0; i < 100; i++)
         {
             robot.SetToolAO(0, i * 40.96, block);
             robot.Sleep(30);
         }
         robot.CloseRPC();
         return 0;
     }

获取控制箱数字量输入
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取控制箱数字量输入
    * @param  [in] id  io编号，范围[0~15]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  0-低电平，1-高电平
    * @return  错误码
    */   
    errno_t  GetDI(int id, uint8_t block, uint8_t *result);

获取工具数字量输入
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取工具数字量输入
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  0-低电平，1-高电平
    * @return  错误码
    */   
    errno_t  GetToolDI(int id, uint8_t block, uint8_t *result);

获取控制箱模拟量输入
+++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取控制箱模拟量输入
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  输入电流或电压值百分比，范围[0~100]对应电流值[0~20mS]或电压[0~10V]
    * @return  错误码
    */   
    errno_t  GetAI(int id, uint8_t block, float *result); 

获取工具模拟量输入
+++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取工具模拟量输入
    * @param  [in] id  io编号，范围[0]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  输入电流或电压值百分比，范围[0~100]对应电流值[0~20mS]或电压[0~10V]
    * @return  错误码
    */   
    errno_t  GetToolAI(int id, uint8_t block, float *result);

获取机器人末端点记录按钮状态
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 获取机器人末端点记录按钮状态
     * @param [out] state 按钮状态，0-按下，1-松开
     * @return 错误码
     */
    errno_t  GetAxlePointRecordBtnState(uint8_t *state);

获取机器人末端DO输出状态
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 获取机器人末端DO输出状态
     * @param [out] do_state DO输出状态，do0~do1对应bit1~bit2,从bit0开始
     * @return 错误码
     */
    errno_t  GetToolDO(uint8_t *do_state);

获取机器人控制器DO输出状态
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 获取机器人控制器DO输出状态
     * @param [out] do_state_h DO输出状态，co0~co7对应bit0~bit7
     * @param [out] do_state_l DO输出状态，do0~do7对应bit0~bit7
     * @return 错误码
     */
    errno_t  GetDO(uint8_t *do_state_h, uint8_t *do_state_l);

获取机器人DI、DO状态代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestGetDIAI(void)
     {
         ROBOT_STATE_PKG pkg = {};
         FRRobot robot;
         robot.LoggerInit();
         robot.SetLoggerLevel(1);
         int rtn = robot.RPC("192.168.58.2");
         if (rtn != 0)
         {
             return -1;
         }
         robot.SetReConnectParam(true, 30000, 500);
         uint8_t status = 1;
         uint8_t smooth = 0;
         uint8_t block = 0;
         uint8_t di = 0, tool_di = 0;
         float ai = 0.0, tool_ai = 0.0;
         float value = 0.0;
         robot.GetDI(0, block, &di);
         printf("di0:%u\n", di);
         tool_di = robot.GetToolDI(1, block, &tool_di);
         printf("tool_di1:%u\n", tool_di);
         robot.GetAI(0, block, &ai);
         printf("ai0:%f\n", ai);
         tool_ai = robot.GetToolAI(0, block, &tool_ai);
         printf("tool_ai0:%f\n", tool_ai);
         uint8_t _button_state = 0;
         robot.GetAxlePointRecordBtnState(&_button_state);
         printf("_button_state is: %u\n", _button_state);
         uint8_t tool_do_state = 0;
         robot.GetToolDO(&tool_do_state);
         printf("tool DO state is: %u\n", tool_do_state);
         uint8_t do_state_h = 0;
         uint8_t do_state_l = 0;
         robot.GetDO(&do_state_h, &do_state_l);
         printf("DO state high is: %u \n DO state low is: %u\n", do_state_h, do_state_l);
         robot.CloseRPC();
         return 0;
     }

等待控制箱数字量输入
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 等待控制箱数字量输入
    * @param  [in] id  io编号，范围[0~15]
    * @param  [in]  status 0-关，1-开
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    errno_t  WaitDI(int id, uint8_t status, int max_time, int opt);

等待控制箱多路数字量输入
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 等待控制箱多路数字量输入
    * @param  [in] mode 0-多路与，1-多路或
    * @param  [in] id  io编号，bit0~bit7对应DI0~DI7，bit8~bit15对应CI0~CI7
    * @param  [in]  status 0-关，1-开
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    errno_t  WaitMultiDI(int mode, int id, uint8_t status, int max_time, int opt);

等待工具数字量输入
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 等待工具数字量输入
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in]  status 0-关，1-开
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    errno_t  WaitToolDI(int id, uint8_t status, int max_time, int opt);

等待控制箱模拟量输入
+++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 等待控制箱模拟量输入
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in]  sign 0-大于，1-小于
    * @param  [in]  value 输入电流或电压值百分比，范围[0~100]对应电流值[0~20mS]或电压[0~10V]
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    errno_t  WaitAI(int id, int sign, float value, int max_time, int opt);  

等待工具模拟量输入
+++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 等待工具模拟量输入
    * @param  [in] id  io编号，范围[0]
    * @param  [in]  sign 0-大于，1-小于
    * @param  [in]  value 输入电流或电压值百分比，范围[0~100]对应电流值[0~20mS]或电压[0~10V]
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    errno_t  WaitToolAI(int id, int sign, float value, int max_time, int opt); 

等待控制箱数字、模拟输入信号代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionchanged:: C++SDK-v2.1.2.0
    
.. code-block:: c++
    :linenos:

     int TestWaitDIAI(void)
     {
         ROBOT_STATE_PKG pkg = {};
         FRRobot robot;
         robot.LoggerInit();
         robot.SetLoggerLevel(1);
         int rtn = robot.RPC("192.168.58.2");
         if (rtn != 0)
         {
             return -1;
         }
         robot.SetReConnectParam(true, 30000, 500);
         uint8_t status = 1;
         uint8_t smooth = 0;
         uint8_t block = 0;
         uint8_t di = 0, tool_di = 0;
         float ai = 0.0, tool_ai = 0.0;
         float value = 0.0;
         rtn = robot.WaitDI(0, 1, 1000, 1);
         cout << "WaitDI over; rtn is: " << rtn << endl;
         robot.WaitMultiDI(1, 3, 3, 1000, 1);
         cout << "WaitDI over; rtn is: " << rtn << endl;
         robot.WaitToolDI(1, 1, 1000, 1);
         cout << "WaitDI over; rtn is: " << rtn << endl;
         robot.WaitAI(0, 0, 50, 1000, 1);
         cout << "WaitDI over; rtn is: " << rtn << endl;
         robot.WaitToolAI(0, 0, 50, 1000, 1);
         cout << "WaitDI over; rtn is: " << rtn << endl;
         robot.CloseRPC();
         return 0;
     }


设置控制箱DO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 设置控制箱DO停止/暂停后输出是否复位
    * @param [in] resetFlag 0-不复位；1-复位
    * @return 错误码
    */
    errno_t SetOutputResetCtlBoxDO(int resetFlag);

设置控制箱AO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置控制箱AO停止/暂停后输出是否复位
     * @param [in] resetFlag 0-不复位；1-复位
     * @return 错误码
     */
    errno_t SetOutputResetCtlBoxAO(int resetFlag);

设置末端工具DO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置末端工具DO停止/暂停后输出是否复位
     * @param [in] resetFlag 0-不复位；1-复位
     * @return 错误码
     */
    errno_t SetOutputResetAxleDO(int resetFlag);

设置末端工具AO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置末端工具AO停止/暂停后输出是否复位
     * @param [in] resetFlag 0-不复位；1-复位
     * @return 错误码
     */
    errno_t SetOutputResetAxleAO(int resetFlag);

设置扩展DO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置扩展DO停止/暂停后输出是否复位
     * @param [in] resetFlag 0-不复位；1-复位
     * @return 错误码
     */
    errno_t SetOutputResetExtDO(int resetFlag);

设置扩展AO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置扩展AO停止/暂停后输出是否复位
     * @param [in] resetFlag 0-不复位；1-复位
     * @return 错误码
     */
    errno_t SetOutputResetExtAO(int resetFlag);

设置SmartTool停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置SmartTool停止/暂停后输出是否复位
     * @param [in] resetFlag 0-不复位；1-复位
     * @return 错误码
     */
    errno_t SetOutputResetSmartToolDO(int resetFlag);

设置LUA程序停止/暂停后输出复位代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int TestDOReset(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      for (int i = 0; i < 16; i++)
      {
        robot.SetDO(i, 1, 0, 0);
        robot.Sleep(300);
      }
      int resetFlag = 1;
      rtn = robot.SetOutputResetCtlBoxDO(resetFlag);
      robot.SetOutputResetCtlBoxAO(resetFlag);
      robot.SetOutputResetAxleDO(resetFlag);
      robot.SetOutputResetAxleAO(resetFlag);
      robot.SetOutputResetExtDO(resetFlag);
      robot.SetOutputResetExtAO(resetFlag);
      robot.SetOutputResetSmartToolDO(resetFlag);
      robot.ProgramLoad("/fruser/test.lua");
      robot.ProgramRun();
      robot.CloseRPC();
      return 0;
    }