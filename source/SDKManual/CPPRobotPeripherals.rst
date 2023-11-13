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
    * @return  错误码
    */
    errno_t  MoveGripper(int index, int pos, int vel, int force, int max_time, uint8_t block);



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
.. code-block:: c++
    :linenos:

    #include <cstdlib>
    #include <iostream>
    #include <stdio.h>
    #include <cstring>
    #include <unistd.h>
    #include "FRRobot.h"
    #include "RobotTypes.h"

    using namespace std;

    int main(void)
    {
        FRRobot robot;                 //实例化机器人对象
        robot.RPC("192.168.58.2");     //与机器人控制器建立通信连接

        int company = 4;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int index = 1;
        int act = 0;
        int max_time = 30000;
        uint8_t block = 0;
        uint8_t status, fault;

        robot.SetGripperConfig(company, device, softversion, bus);
        sleep(1);
        robot.GetGripperConfig(&company, &device, &softversion, &bus);
        printf("gripper config:%d,%d,%d,%d\n", company, device, softversion, bus);

        robot.ActGripper(index, act);
        sleep(1);
        act = 1;
        robot.ActGripper(index, act);
        sleep(2);

        robot.MoveGripper(index, 100, 50, 50, max_time, block);
        sleep(3);
        robot.MoveGripper(index, 0, 50, 0, max_time, block);

        robot.GetGripperMotionDone(&fault, &status);
        printf("motion status:%u,%u\n", fault, status);

        return 0;
    }
