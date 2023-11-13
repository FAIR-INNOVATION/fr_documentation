机器人轨迹复现
=================

.. toctree:: 
    :maxdepth: 5

设置轨迹记录参数
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置轨迹记录参数
    * @param  [in] type  记录数据类型，1-关节位置
    * @param  [in] name  轨迹文件名
    * @param  [in] period_ms  数据采样周期，固定值2ms或4ms或8ms
    * @param  [in] di_choose  DI选择,bit0~bit7对应控制箱DI0~DI7，bit8~bit9对应末端DI0~DI1，0-不选择，1-选择
    * @param  [in] do_choose  DO选择,bit0~bit7对应控制箱DO0~DO7，bit8~bit9对应末端DO0~DO1，0-不选择，1-选择
    * @return  错误码
    */
    errno_t  SetTPDParam(int type, char name[30], int period_ms, uint16_t di_choose, uint16_t do_choose);

开始轨迹记录
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  开始轨迹记录
    * @param  [in] type  记录数据类型，1-关节位置
    * @param  [in] name  轨迹文件名
    * @param  [in] period_ms  数据采样周期，固定值2ms或4ms或8ms
    * @param  [in] di_choose  DI选择,bit0~bit7对应控制箱DI0~DI7，bit8~bit9对应末端DI0~DI1，0-不选择，1-选择
    * @param  [in] do_choose  DO选择,bit0~bit7对应控制箱DO0~DO7，bit8~bit9对应末端DO0~DO1，0-不选择，1-选择
    * @return  错误码
    */
    errno_t  SetTPDStart(int type, char name[30], int period_ms, uint16_t di_choose, uint16_t do_choose); 

停止轨迹记录
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  停止轨迹记录
    * @return  错误码
    */
    errno_t  SetWebTPDStop();

删除轨迹记录
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  删除轨迹记录
    * @param  [in] name  轨迹文件名
    * @return  错误码
    */   
    errno_t  SetTPDDelete(char name[30]);

代码示例
++++++++++++++
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

        int type = 1;
        char name[30] = "tpd2023";
        int period_ms = 4;
        uint16_t di_choose = 0;
        uint16_t do_choose = 0;

        robot.SetTPDParam(type, name, period_ms, di_choose, do_choose);

        robot.Mode(1);
        sleep(1);
        robot.DragTeachSwitch(1);
        robot.SetTPDStart(type, name, period_ms, di_choose, do_choose);
        sleep(30);
        robot.SetWebTPDStop();
        robot.DragTeachSwitch(0);

        //robot.SetTPDDelete(name);

        return 0;
    }

轨迹预加载
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  轨迹预加载
    * @param  [in] name  轨迹文件名
    * @return  错误码
    */      
    errno_t  LoadTPD(char name[30]);

获取轨迹起始位姿
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  获取轨迹起始位姿
     * @param  [in] name 轨迹文件名,不需要文件后缀
     * @return  错误码
     */     
    errno_t  GetTPDStartPose(char name[30], DescPose *desc_pose);

轨迹复现
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  轨迹复现
    * @param  [in] name  轨迹文件名
    * @param  [in] blend 0-不平滑，1-平滑
    * @param  [in] ovl  速度缩放百分比，范围[0~100]
    * @return  错误码
    */
    errno_t  MoveTPD(char name[30], uint8_t blend, float ovl);

轨迹预处理
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  轨迹预处理
     * @param  [in] name  轨迹文件名
     * @param  [in] ovl 速度缩放百分比，范围[0~100]
     * @param  [in] opt 1-控制点，默认为1
     * @return  错误码
     */     
    errno_t  LoadTrajectoryJ(char name[30], float ovl, int opt);

轨迹复现
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  轨迹复现
     * @return  错误码
     */     
    errno_t  MoveTrajectoryJ();

获取轨迹起始位姿
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  获取轨迹起始位姿
     * @param  [in] name 轨迹文件名
     * @return  错误码
     */     
    errno_t  GetTrajectoryStartPose(char name[30], DescPose *desc_pose);

获取轨迹点编号
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  获取轨迹点编号
     * @return  错误码
     */     
    errno_t  GetTrajectoryPointNum(int *pnum);

设置轨迹运行中的速度
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  设置轨迹运行中的速度
     * @param  [in] ovl 速度百分比
     * @return  错误码
     */     
    errno_t  SetTrajectoryJSpeed(float ovl);

设置轨迹运行中的力和扭矩
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  设置轨迹运行中的力和扭矩
     * @param  [in] ft 三个方向的力和扭矩，单位N和Nm
     * @return  错误码
     */     
    errno_t  SetTrajectoryJForceTorque(ForceTorque *ft);

设置轨迹运行中的沿x方向的力
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  设置轨迹运行中的沿x方向的力
     * @param  [in] fx 沿x方向的力，单位N
     * @return  错误码
     */     
    errno_t  SetTrajectoryJForceFx(double fx);

设置轨迹运行中的沿y方向的力
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  设置轨迹运行中的沿y方向的力
     * @param  [in] fy 沿y方向的力，单位N
     * @return  错误码
     */     
    errno_t  SetTrajectoryJForceFy(double fy);

设置轨迹运行中的沿z方向的力
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  设置轨迹运行中的沿z方向的力
     * @param  [in] fz 沿x方向的力，单位N
     * @return  错误码
     */     
    errno_t  SetTrajectoryJForceFz(double fz);

设置轨迹运行中的绕x轴的扭矩
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  设置轨迹运行中的绕x轴的扭矩
     * @param  [in] tx 绕x轴的扭矩，单位Nm
     * @return  错误码
     */     
    errno_t  SetTrajectoryJTorqueTx(double tx);

设置轨迹运行中的绕y轴的扭矩
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  设置轨迹运行中的绕y轴的扭矩
     * @param  [in] ty 绕y轴的扭矩，单位Nm
     * @return  错误码
     */     
    errno_t  SetTrajectoryJTorqueTy(double ty);

设置轨迹运行中的绕z轴的扭矩
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  设置轨迹运行中的绕z轴的扭矩
     * @param  [in] tz 绕z轴的扭矩，单位Nm
     * @return  错误码
     */     
    errno_t  SetTrajectoryJTorqueTz(double tz);

代码示例
++++++++++++++++++
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

        char name[30] = "tpd2023";
        int tool = 1;
        int user = 0;
        float vel = 100.0;
        float acc = 100.0;
        float ovl = 100.0;
        float blendT = -1.0;
        int config = -1;
        uint8_t blend = 1;

        DescPose desc_pose;
        memset(&desc_pose, 0, sizeof(DescPose));   

        desc_pose.tran.x = -378.9;
        desc_pose.tran.y = -340.3;
        desc_pose.tran.z = 107.2;
        desc_pose.rpy.rx = 179.4;
        desc_pose.rpy.ry = -1.3;
        desc_pose.rpy.rz = 125.0;

        robot.LoadTPD(name);
        robot.MoveCart(&desc_pose, tool, user, vel, acc, ovl, blendT, config);
        robot.MoveTPD(name, blend, ovl);

        return 0;
    }
