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

焊接开始
++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 焊接开始
    * @param [in] ioType io类型 0-控制器IO； 1-扩展IO
    * @param [in] arcNum 焊机配置文件编号
    * @param [in] timeout 起弧超时时间
    * @return 错误码
    */
    errno_t ARCStart(int ioType, int arcNum, int timeout);

焊接结束
++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 焊接结束
    * @param [in] ioType io类型 0-控制器IO； 1-扩展IO
    * @param [in] arcNum 焊机配置文件编号
    * @param [in] timeout 熄弧超时时间
    * @return 错误码
    */
    errno_t ARCEnd(int ioType, int arcNum, int timeout);

设置焊接电流与输出模拟量对应关系
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置焊接电流与输出模拟量对应关系
    * @param [in] currentMin 焊接电流-模拟量输出线性关系左侧点电流值(A)
    * @param [in] currentMax 焊接电流-模拟量输出线性关系右侧点电流值(A)
    * @param [in] outputVoltageMin 焊接电流-模拟量输出线性关系左侧点模拟量输出电压值(V)
    * @param [in] outputVoltageMax 焊接电流-模拟量输出线性关系右侧点模拟量输出电压值(V)
    * @return 错误码
    */
    errno_t WeldingSetCurrentRelation(double currentMin, double currentMax, double outputVoltageMin, double outputVoltageMax);

设置焊接电压与输出模拟量对应关系
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置焊接电压与输出模拟量对应关系
    * @param [in] weldVoltageMin 焊接电压-模拟量输出线性关系左侧点焊接电压值(A)
    * @param [in] weldVoltageMax 焊接电压-模拟量输出线性关系右侧点焊接电压值(A)
    * @param [in] outputVoltageMin 焊接电压-模拟量输出线性关系左侧点模拟量输出电压值(V)
    * @param [in] outputVoltageMax 焊接电压-模拟量输出线性关系右侧点模拟量输出电压值(V)
    * @return 错误码
    */
    errno_t WeldingSetVoltageRelation(double weldVoltageMin, double weldVoltageMax, double outputVoltageMin, double outputVoltageMax);

获取焊接电流与输出模拟量对应关系
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取焊接电流与输出模拟量对应关系
    * @param [out] currentMin 焊接电流-模拟量输出线性关系左侧点电流值(A)
    * @param [out] currentMax 焊接电流-模拟量输出线性关系右侧点电流值(A)
    * @param [out] outputVoltageMin 焊接电流-模拟量输出线性关系左侧点模拟量输出电压值(V)
    * @param [out] outputVoltageMax 焊接电流-模拟量输出线性关系右侧点模拟量输出电压值(V)
    * @return 错误码
    */
    errno_t WeldingGetCurrentRelation(double *currentMin, double *currentMax, double *outputVoltageMin, double *outputVoltageMax);

获取焊接电压与输出模拟量对应关系
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取焊接电压与输出模拟量对应关系
    * @param [out] weldVoltageMin 焊接电压-模拟量输出线性关系左侧点焊接电压值(A)
    * @param [out] weldVoltageMax 焊接电压-模拟量输出线性关系右侧点焊接电压值(A)
    * @param [out] outputVoltageMin 焊接电压-模拟量输出线性关系左侧点模拟量输出电压值(V)
    * @param [out] outputVoltageMax 焊接电压-模拟量输出线性关系右侧点模拟量输出电压值(V)
    * @return 错误码
    */
    errno_t WeldingGetVoltageRelation(double *weldVoltageMin, double *weldVoltageMax, double *outputVoltageMin, double *outputVoltageMax);

设置焊接电流
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置焊接电流
    * @param [in] ioType 控制IO类型 0-控制箱IO；1-扩展IO
    * @param [in] current 焊接电流值(A)
    * @param [in] AOIndex 焊接电流控制箱模拟量输出端口(0-1)
    * @return 错误码
    */
    errno_t WeldingSetCurrent(int ioType, double current, int AOIndex);

设置焊接电压
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置焊接电压
    * @param [in] ioType 控制IO类型 0-控制箱IO；1-扩展IO
    * @param [in] voltage 焊接电压值(A)
    * @param [in] AOIndex 焊接电压控制箱模拟量输出端口(0-1)
    * @return 错误码
    */
    errno_t WeldingSetVoltage(int ioType, double voltage, int AOIndex);

设置摆动参数
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
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
    errno_t WeaveSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary);

即时设置摆动参数
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
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
    errno_t WeaveOnlineSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary);

摆动开始
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 摆动开始
    * @param [in] weaveNum 摆焊参数配置编号
    * @return 错误码
    */
    errno_t WeaveStart(int weaveNum);

摆动结束
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 摆动结束
    * @param [in] weaveNum 摆焊参数配置编号
    * @return 错误码
    */
    errno_t WeaveEnd(int weaveNum);

正向送丝
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 正向送丝
    * @param [in] ioType io类型  0-控制器IO；1-扩展IO
    * @param [in] wireFeed 送丝控制  0-停止送丝；1-送丝
    * @return 错误码
    */
    errno_t SetForwardWireFeed(int ioType, int wireFeed);

反向送丝
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 反向送丝
    * @param [in] ioType io类型  0-控制器IO；1-扩展IO
    * @param [in] wireFeed 送丝控制  0-停止送丝；1-送丝
    * @return 错误码
    */
    errno_t SetReverseWireFeed(int ioType, int wireFeed);

送气
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 送气
    * @param [in] ioType io类型  0-控制器IO；1-扩展IO
    * @param [in] airControl 送气控制  0-停止送气；1-送气
    * @return 错误码
    */
    errno_t SetAspirated(int ioType, int airControl);

段焊开始
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
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
    * @param [in] vel 速度百分比，范围[0~100]
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl 速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param [in] epos 扩展轴位置，单位mm
    * @param [in] search 0-不焊丝寻位，1-焊丝寻位
    * @param [in] offset_flag 0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos 位姿偏移量
    * @return 错误码
    */
    errno_t SegmentWeldStart(DescPose *startDesePos, DescPose *endDesePos, JointPos *startJPos, JointPos *endJPos, double weldLength, double noWeldLength, int weldIOType, int arcNum, int weldTimeout, bool isWeave, int weaveNum, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos *epos, uint8_t search, uint8_t offset_flag, DescPose *offset_pos);

代码示例
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    #include "libfairino/robot.h"
    #ifdef WINDOWS_OPTION
    #include <string.h>
    #include <windows.h>
    #elif LINUX_OPTION
    #include <cstdlib>
    #include <iostream>
    #include <stdio.h>
    #include <cstring>
    #include <unistd.h>
    #endif

    #include <chrono>
    #include <thread>

    using namespace std;

    int main(void)
    {
        printf("start to debug\n");
        FRRobot robot;            
        robot.RPC("192.168.58.2"); 

        double current_min = 0;
        double current_max = 0;
        double vol_min = 0;
        double vol_max = 0;
        double output_vmin = 0;
        double output_vmax = 0;

        DescPose start_descpose;
        start_descpose.rpy.rx = 2.243;
        start_descpose.rpy.ry = 0.828;
        start_descpose.rpy.rz = -148.894;
        start_descpose.tran.x = -208.064;
        start_descpose.tran.y = 412.155;
        start_descpose.tran.z = 1.926;

        JointPos start_jointpose;
        start_jointpose.jPos[0] = -51.489;
        start_jointpose.jPos[1] = -105.721;
        start_jointpose.jPos[2] = 130.695;
        start_jointpose.jPos[3] = -108.338;
        start_jointpose.jPos[4] = -91.356;
        start_jointpose.jPos[5] = 62.014;

        DescPose end_descpose;
        end_descpose.rpy.rx = 2.346;
        end_descpose.rpy.ry = -3.633;
        end_descpose.rpy.rz = -106.313;
        end_descpose.tran.x = -425.087;
        end_descpose.tran.y = 389.637;
        end_descpose.tran.z = -9.249;

        JointPos end_jointpose;
        end_jointpose.jPos[0] = -47.137;
        end_jointpose.jPos[1] = -102.345;
        end_jointpose.jPos[2] = 127.607;
        end_jointpose.jPos[3] = -108.526;
        end_jointpose.jPos[4] = -91.407;
        end_jointpose.jPos[5] = 23.537;

        ExaxisPos ex_axis_pose;
        memset(&ex_axis_pose, 0, sizeof(ExaxisPos));
        DescPose offset_pose;
        memset(&offset_pose, 0, sizeof(DescPose));
        int retval = 0;

        retval = robot.WeldingSetCurrentRelation(0, 400, 0, 10);
        cout << "WeldingSetCurrentRelation retval is: " << retval << endl;

        retval = robot.WeldingSetVoltageRelation(0, 40, 0, 10);
        cout << "WeldingSetVoltageRelation retval is: " << retval << endl;

        retval = robot.WeldingGetCurrentRelation(&current_min, &current_max, &output_vmin, &output_vmax);
        cout << "WeldingGetCurrentRelation retval is: " << retval << endl;
        cout << "current min " << current_min << " current max " << current_max << " output vol min " << output_vmin << " output vol max "<< output_vmax<<endl;

        retval = robot.WeldingGetVoltageRelation(&vol_min, &vol_max, &output_vmin, &output_vmax);
        cout << "WeldingGetVoltageRelation retval is: " << retval << endl;
        cout << "vol min " << vol_min << " vol max " << vol_max << " output vol min " << output_vmin << " output vol max "<< output_vmax<<endl;

        retval = robot.WeldingSetCurrent(1, 100, 0);
        cout << "WeldingSetCurrent retval is: " << retval << endl;

        this_thread::sleep_for(chrono::seconds(3));

        retval = robot.WeldingSetVoltage(1, 10, 0);
        cout << "WeldingSetVoltage retval is: " << retval << endl;
        
        retval = robot.WeaveSetPara(0, 0, 2.0, 0, 10, 0, 0, 0, 0);
        cout << "retval is: " << retval << endl;

        retval = robot.MoveJ(&start_jointpose, &start_descpose, 1, 0, 50, 50, 50, &ex_axis_pose, 0, 0, &offset_pose);
        if (retval != 0)
        {
            cout << "movej fail " << retval << endl;
            return 0;
        }

        retval = robot.WeaveStart(0);
        cout << "retval is: " << retval << endl;

        retval = robot.MoveL(&end_jointpose, &end_descpose, 1, 0, 50, 50, 50, 0, &ex_axis_pose, 0, 0, &offset_pose);
        if (retval != 0)
        {
            cout << "MoveL fail " << retval << endl;
            robot.WeaveEnd(0);
            return 0;
        }

        retval = robot.WeaveEnd(0);
        cout << "retval is: " << retval << endl;
        
        return 0;
    }