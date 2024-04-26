扩展轴
=============

.. toctree:: 
    :maxdepth: 5

设置485扩展轴参数
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
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
    errno_t AuxServoSetParam(int servoId, int servoCompany, int servoModel, int servoSoftVersion, int servoResolution, double axisMechTransRatio);

获取485扩展轴配置参数
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
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
    errno_t AuxServoGetParam(int servoId, int* servoCompany, int* servoModel, int* servoSoftVersion, int* servoResolution, double* axisMechTransRatio);
    
代码示例
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    #include "libfairino/robot.h"

    //如果使用Windows，包含下面的头文件
    #include <string.h>
    #include <windows.h>
    //如果使用linux，包含下面的头文件
    /*
    #include <cstdlib>
    #include <iostream>
    #include <stdio.h>
    #include <cstring>
    #include <unistd.h>
    */
    #include <chrono>
    #include <thread>
    #include <string>

    using namespace std;

    int main(void)
    {
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel();
        robot.RPC("192.168.58.2"); 

        int retval = robot.AuxServoSetParam(1, 1, 1, 1, 131072, 15.45);
        std::cout << "AuxServoSetParam is: " << retval << std::endl;

        int servoCompany;
        int servoModel;
        int servoSoftVersion;
        int servoResolution;
        double axisMechTransRatio;
        retval = robot.AuxServoGetParam(1, &servoCompany, &servoModel, &servoSoftVersion, &servoResolution, &axisMechTransRatio);
        std::cout << "servoCompany " << servoCompany<< "\n"
                  << "servoModel " << servoModel << "\n"
                  << "servoSoftVersion " << servoSoftVersion<< "\n"
                  << "servoResolution " << servoResolution<< "\n"
                  << "axisMechTransRatio "<<axisMechTransRatio<< "\n"
                  << std::endl;

        retval = robot.AuxServoSetParam(1, 10, 11, 12, 13, 14);
        std::cout << "AuxServoSetParam is: " << retval << std::endl;

        retval = robot.AuxServoGetParam(1, &servoCompany, &servoModel, &servoSoftVersion, &servoResolution, &axisMechTransRatio);
        std::cout << "servoCompany " << servoCompany<< "\n"
                  << "servoModel " << servoModel << "\n"
                  << "servoSoftVersion " << servoSoftVersion<< "\n"
                  << "servoResolution " << servoResolution<< "\n"
                  << "axisMechTransRatio "<<axisMechTransRatio<< "\n"
                  << std::endl;

        return 0;
    }
    
设置485扩展轴使能/去使能
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置485扩展轴使能/去使能
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID
    * @param [in] status 使能状态，0-去使能， 1-使能
    * @return 错误码
    */
    errno_t AuxServoEnable(int servoId, int status);

设置485扩展轴控制模式
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置485扩展轴控制模式
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID
    * @param [in] mode 控制模式，0-位置模式，1-速度模式
    * @return 错误码
    */
    errno_t AuxServoSetControlMode(int servoId, int mode);

设置485扩展轴目标位置(位置模式)
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置485扩展轴目标位置(位置模式)
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID
    * @param [in] pos 目标位置，mm或°
    * @param [in] speed 目标速度，mm/s或°/s
    * @return 错误码
    */
    errno_t AuxServoSetTargetPos(int servoId, double pos, double speed);

设置485扩展轴目标转矩(力矩模式) - 暂未开放
++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置485扩展轴目标转矩(力矩模式)
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID
    * @param [in] torque 目标力矩，Nm
    * @return 错误码
    */
    errno_t AuxServoSetTargetTorque(int servoId, double torque);

设置485扩展轴回零
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置485扩展轴回零
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID
    * @param [in] mode 回零模式，0-当前位置回零；1-限位回零
    * @param [in] searchVel 回零速度，mm/s或°/s
    * @param [in] latchVel 箍位速度，mm/s或°/s
    * @return 错误码
    */
    errno_t AuxServoHoming(int servoId, int mode, double searchVel, double latchVel);
    
清除485扩展轴错误信息
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 清除485扩展轴错误信息
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID
    * @return 错误码
    */
    errno_t AuxServoClearError(int servoId);

获取485扩展轴伺服状态
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取485扩展轴伺服状态
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID
    * @param [out] servoErrCode 伺服驱动器故障码
    * @param [out] servoState 伺服驱动器状态[十进制数转为二进制，bit0-bit5：伺服使能-伺服运行-正限位触发-负限位触发-定位完成-回零完成]
    * @param [out] servoPos 伺服当前位置 mm或°
    * @param [out] servoSpeed 伺服当前速度 mm/s或°/s
    * @param [out] servoTorque 伺服当前转矩Nm
    * @return 错误码
    */
    errno_t AuxServoGetStatus(int servoId, int* servoErrCode, int* servoState, double* servoPos, double* servoSpeed, double* servoTorque);

代码示例
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    #include "libfairino/robot.h"

    //如果使用Windows，包含下面的头文件
    #include <string.h>
    #include <windows.h>
    //如果使用linux，包含下面的头文件
    /*
    #include <cstdlib>
    #include <iostream>
    #include <stdio.h>
    #include <cstring>
    #include <unistd.h>
    */
    #include <chrono>
    #include <thread>
    #include <string>

    using namespace std;

    int main(void)
    {
        FRRobot robot; 
        robot.LoggerInit();
        robot.SetLoggerLevel();
        robot.RPC("192.168.58.2");
        int retval = 0;

        retval = robot.AuxServoSetParam(1, 1, 1, 1, 131072, 36);
        std::cout << "AuxServoSetParam is: " << retval << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(3));

        retval = robot.AuxServoEnable(1, 0);
        std::cout << "AuxServoEnable disenable " << retval << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
        int servoerrcode = 0;
        int servoErrCode;
        int servoState;
        double servoPos;
        double servoSpeed;
        double servoTorque;
        retval = robot.AuxServoGetStatus(1, &servoErrCode, &servoState, &servoPos, &servoSpeed, &servoTorque);
        std::cout << "AuxServoGetStatus servoState "<< servoState << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));

        retval = robot.AuxServoEnable(1, 1);
        std::cout << "AuxServoEnable enable " << retval << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
        retval = robot.AuxServoGetStatus(1, &servoErrCode, &servoState, &servoPos, &servoSpeed, &servoTorque);
        std::cout << "AuxServoGetStatus servoState "<< servoState << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));

        retval = robot.AuxServoHoming(1, 1, 5, 1);
        std::cout << "AuxServoHoming " << retval << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(3));

        retval = robot.AuxServoSetTargetPos(1, 200, 30);
        std::cout << "AuxServoSetTargetPos " << retval << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
        retval = robot.AuxServoGetStatus(1, &servoErrCode, &servoState, &servoPos, &servoSpeed, &servoTorque);
        std::cout << "AuxServoGetStatus servoSpeed "<< servoSpeed << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));

        return 0;
    }

设置485扩展轴目标速度(速度模式)
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置485扩展轴目标速度(速度模式)
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID
    * @param [in] speed 目标速度，mm/s或°/s
    * @return 错误码
    */
    errno_t AuxServoSetTargetSpeed(int servoId, double speed);
    
设置状态反馈中485扩展轴数据轴号
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置状态反馈中485扩展轴数据轴号
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID
    * @return 错误码
    */
    errno_t AuxServosetStatusID(int servoId);
        
获取机器人实时状态结构体
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取机器人实时状态结构体
    * @param [out] pkg 机器人实时状态结构体
    * @return 错误码
    */
    errno_t GetRobotRealTimeState(ROBOT_STATE_PKG *pkg);
        
获取机器人外设协议
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取机器人外设协议
    * @param [out] protocol 机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 错误码
    */
    errno_t GetExDevProtocol(int *protocol);

设置机器人外设协议
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置机器人外设协议
    * @param [in] protocol 机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 错误码
    */
    errno_t SetExDevProtocol(int protocol);

代码示例
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:
    
    #include "libfairino/robot.h"
    //如果使用Windows，包含下面的头文件
    #include <string.h>
    #include <windows.h>
    //如果使用linux，包含下面的头文件
    /*
    #include <cstdlib>
    #include <iostream>
    #include <stdio.h>
    #include <cstring>
    #include <unistd.h>
    */
    #include <chrono>
    #include <thread>
    #include <string>

    using namespace std;

    int main(void)
    {
        FRRobot robot; 
        robot.LoggerInit();
        robot.SetLoggerLevel();
        robot.RPC("192.168.58.2");
        int retval = 0;

        ROBOT_STATE_PKG robot_pkg;
        int i = 0;
        while (i < 5)
        {
            std::this_thread::sleep_for(std::chrono::seconds(1));
            memset(&robot_pkg, 0, sizeof(ROBOT_STATE_PKG));
            retval = robot.GetRobotRealTimeState(&robot_pkg);
            std::cout << "program_state " << (int)robot_pkg.program_state<< "\n"
                << "data_len " << (int)robot_pkg.data_len << "\n"
                << "robot_state " << (int)robot_pkg.robot_state << "\n"
                << "robot_mode " << (int)robot_pkg.robot_mode << std::endl;
            i++;
        }

        int protocol = 4096;
        retval = robot.SetExDevProtocol(protocol);
        std::cout << "SetExDevProtocol retval " << retval << std::endl;
        retval = robot.GetExDevProtocol(&protocol);
        std::cout << "GetExDevProtocol retval " << retval <<" protocol is: " << protocol << std::endl;

        return 0;
    }
