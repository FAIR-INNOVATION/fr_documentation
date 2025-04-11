机器人外设
============

.. toctree:: 
    :maxdepth: 5

配置夹爪
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  配置夹爪
    * @param  [in] company  夹爪厂商，待定
    * @param  [in] device  设备号，暂不使用，默认为0
    * @param  [in] softvesion  软件版本号，暂不使用，默认为0
    * @param  [in] bus 设备挂在末端总线位置，暂不使用，默认为0
    * @return  错误码
    */
    errno_t  SetGripperConfig(int company, int device, int softvesion, int bus);

获取夹爪配置
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取夹爪配置
    * @param  [in] company  夹爪厂商，待定
    * @param  [in] device  设备号，暂不使用，默认为0
    * @param  [in] softvesion  软件版本号，暂不使用，默认为0
    * @param  [in] bus 设备挂在末端总线位置，暂不使用，默认为0
    * @return  错误码
    */
    errno_t  GetGripperConfig(int *company, int *device, int *softvesion, int *bus);

激活夹爪
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  激活夹爪
    * @param  [in] index  夹爪编号
    * @param  [in] act  0-复位，1-激活
    * @return  错误码
    */
    errno_t  ActGripper(int index, uint8_t act);

控制夹爪
++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
	 * @brief  控制夹爪
	 * @param  [in] index  夹爪编号
	 * @param  [in] pos  位置百分比，范围[0~100]
	 * @param  [in] vel  速度百分比，范围[0~100]
	 * @param  [in] force  力矩百分比，范围[0~100]
	 * @param  [in] max_time  最大等待时间，范围[0~30000]，单位ms
	 * @param  [in] block  0-阻塞，1-非阻塞
	 * @param  [in] type 夹爪类型，0-平行夹爪；1-旋转夹爪
	 * @param  [in] rotNum 旋转圈数
	 * @param  [in] rotVel 旋转速度百分比[0-100]
	 * @param  [in] rotTorque 旋转力矩百分比[0-100]
	 * @return  错误码
	 */
	errno_t MoveGripper(int index, int pos, int vel, int force, int max_time, uint8_t block, int type, double rotNum, int rotVel, int rotTorque);



获取夹爪运动状态
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  获取夹爪运动状态
     * @param  [out] fault  0-无错误，1-有错误
     * @param  [out] staus  0-运动未完成，1-运动完成
     * @return  错误码
     */
    errno_t  GetGripperMotionDone(uint16_t *fault, uint8_t *status);

获取夹爪激活状态
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  获取夹爪激活状态
     * @param  [out] fault  0-无错误，1-有错误
     * @param  [out] status  bit0~bit15对应夹爪编号0~15，bit=0为未激活，bit=1为激活
     * @return  错误码
     */
    errno_t  GetGripperActivateStatus(uint16_t *fault, uint16_t *status);

获取夹爪位置
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  获取夹爪位置
     * @param  [out] fault  0-无错误，1-有错误
     * @param  [out] position  位置百分比，范围0~100%
     * @return  错误码
     */
    errno_t  GetGripperCurPosition(uint16_t *fault, uint8_t *position);

获取夹爪速度
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  获取夹爪速度
     * @param  [out] fault  0-无错误，1-有错误
     * @param  [out] speed  速度百分比，范围0~100%
     * @return  错误码
     */
    errno_t  GetGripperCurSpeed(uint16_t *fault, int8_t *speed);

获取夹爪电流
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  获取夹爪电流
     * @param  [out] fault  0-无错误，1-有错误
     * @param  [out] current  电流百分比，范围0~100%
     * @return  错误码
     */
    errno_t  GetGripperCurCurrent(uint16_t *fault, int8_t *current);

获取夹爪电压
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  获取夹爪电压
     * @param  [out] fault  0-无错误，1-有错误
     * @param  [out] voltage  电压,单位0.1V
     * @return  错误码
     */
    errno_t  GetGripperVoltage(uint16_t *fault, int *voltage);

获取夹爪温度
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  获取夹爪温度
     * @param  [out] fault  0-无错误，1-有错误
     * @param  [out] temp  温度，单位℃
     * @return  错误码
     */
    errno_t  GetGripperTemp(uint16_t *fault, int *temp);

计算预抓取点-视觉
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  计算预抓取点-视觉
     * @param  [in] desc_pos  抓取点笛卡尔位姿
     * @param  [in] zlength   z轴偏移量
     * @param  [in] zangle    绕z轴旋转偏移量
     * @return  错误码 
     */
    errno_t  ComputePrePick(DescPose *desc_pos, double zlength, double zangle, DescPose *pre_pos);

计算撤退点-视觉
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  计算撤退点-视觉
     * @param  [in] desc_pos  抓取点笛卡尔位姿
     * @param  [in] zlength   z轴偏移量
     * @param  [in] zangle    绕z轴旋转偏移量
     * @return  错误码 
     */
    errno_t  ComputePostPick(DescPose *desc_pos, double zlength, double zangle, DescPose *post_pos);

代码示例
++++++++++++++++
.. versionchanged:: C++SDK-v2.1.2.0

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

    using namespace std;

    int main(void)
    {
        FRRobot robot; 
        robot.RPC("192.168.58.2"); 

        int company = 4;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int index = 1;
        int act = 0;
        int max_time = 30000;
        uint8_t block = 0;
        uint8_t status;
        uint16_t fault;
        uint16_t active_status = 0;
        uint8_t current_pos = 0;
        int8_t current = 0;
        int voltage = 0;
        int temp = 0;
        int8_t speed = 0;

        robot.SetGripperConfig(company, device, softversion, bus);
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        robot.GetGripperConfig(&company, &device, &softversion, &bus);
        printf("gripper config:%d,%d,%d,%d\n", company, device, softversion, bus);

        robot.ActGripper(index, act);
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        act = 1;
        robot.ActGripper(index, act);
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));

        robot.MoveGripper(index, 100, 50, 50, max_time, block);
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        robot.MoveGripper(index, 0, 50, 0, max_time, block);

        robot.GetGripperMotionDone(&fault, &status);
        printf("motion status:%u,%u\n", fault, status);

        robot.GetGripperActivateStatus(&fault, &active_status);
        printf("gripper active fault is: %u, status is: %u\n", fault, active_status);

        robot.GetGripperCurPosition(&fault, &current_pos);
        printf("fault is:%u, current position is: %u\n", fault, current_pos);

        robot.GetGripperCurCurrent(&fault, &current);
        printf("fault is:%u, current current is: %d\n", fault, current);

        robot.GetGripperVoltage(&fault, &voltage);
        printf("fault is:%u, current voltage is: %d \n", fault, voltage);

        robot.GetGripperTemp(&fault, &temp);
        printf("fault is:%u, current temperature is: %d\n", fault, temp);

        robot.GetGripperCurSpeed(&fault, &speed);
        printf("fault is:%u, current speed is: %d\n", fault, speed);

        int retval = 0;
        DescPose prepick_pose;
        DescPose postpick_pose;
        memset(&prepick_pose, 0, sizeof(DescPose));
        memset(&postpick_pose, 0, sizeof(DescPose));

        DescPose desc_p1;
        desc_p1.tran.x = -351.553;
        desc_p1.tran.y = 87.913;
        desc_p1.tran.z = 354.175;
        desc_p1.rpy.rx = -179.680;
        desc_p1.rpy.ry = -0.133;
        desc_p1.rpy.rz = 2.472;

        DescPose desc_p2;
        desc_p2.tran.x = -351.535;
        desc_p2.tran.y = -247.222;
        desc_p2.tran.z = 354.173;
        desc_p2.rpy.rx = -179.680;
        desc_p2.rpy.ry = -0.137;
        desc_p2.rpy.rz = 2.473;

        retval = robot.ComputePrePick(&desc_p1, 10, 0, &prepick_pose);
        printf("ComputePrePick retval is: %d\n", retval);
        printf("xyz is: %f, %f, %f; rpy is: %f, %f, %f\n", prepick_pose.tran.x, prepick_pose.tran.y, prepick_pose.tran.z, prepick_pose.rpy.rx, prepick_pose.rpy.ry, prepick_pose.rpy.rz);

        retval = robot.ComputePostPick(&desc_p2, -10, 0, &postpick_pose);
        printf("ComputePostPick retval is: %d\n", retval);
        printf("xyz is: %f, %f, %f; rpy is: %f, %f, %f\n", postpick_pose.tran.x, postpick_pose.tran.y, postpick_pose.tran.z, postpick_pose.rpy.rx, postpick_pose.rpy.ry, postpick_pose.rpy.rz);

        return 0;
    }

获取旋转夹爪的旋转圈数
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 3.7.6版本加入

.. code-block:: c++
    :linenos:

    /**
	 * @brief  获取旋转夹爪的旋转圈数
	 * @param  [out] fault  0-无错误，1-有错误
	 * @param  [out] num  旋转圈数
	 * @return  错误码
	 */
	errno_t GetGripperRotNum(uint16_t* fault, double* num);

获取旋转夹爪的旋转速度
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: V3.7.6

.. code-block:: c++
    :linenos:

    /**
	 * @brief  获取旋转夹爪的旋转速度
	 * @param  [out] fault  0-无错误，1-有错误
	 * @param  [out] speed  旋转速度百分比
	 * @return  错误码
	 */
	errno_t GetGripperRotSpeed(uint16_t* fault, int* speed);

获取旋转夹爪的旋转力矩
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: V3.7.6

.. code-block:: c++
    :linenos:

    /**
	 * @brief  获取旋转夹爪的旋转力矩
	 * @param  [out] fault  0-无错误，1-有错误
	 * @param  [out] torque  旋转力矩百分比
	 * @return  错误码
	 */
	errno_t GetGripperRotTorque(uint16_t* fault, int* torque);

示例程序
********************

.. versionadded:: V3.7.6

.. code-block:: c++
    :linenos:

    int MoveRotGripper(FRRobot* robot, int pos, double rotPos)
    {
        robot->ResetAllError();
        robot->ActGripper(1, 1);
        robot->Sleep(1000);
        int rtn = robot->MoveGripper(1, pos, 50, 50, 5000, 1, 1, rotPos, 50, 100);
        printf("move gripper rtn is %d\n", rtn);
        uint16_t fault = 0;
        double rotNum = 0.0;
        int rotSpeed = 0;
        int rotTorque = 0;
        robot->GetGripperRotNum(&fault, &rotNum);
        robot->GetGripperRotSpeed (&fault, &rotSpeed);
        robot->GetGripperRotTorque(&fault, &rotTorque);
        printf("gripper rot num : %lf, gripper rotSpeed : %d, gripper rotTorque : %d\n", rotNum, rotSpeed, rotTorque);

        return 0;
    }
