机器人常用设置
=================

.. toctree:: 
    :maxdepth: 5

设置全局速度
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置全局速度
    * @param  [in]  vel  速度百分比，范围[0~100]
    * @return  错误码
    */
    int SetSpeed(int vel); 

设置系统变量值
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置系统变量值
    * @param  [in]  id  变量编号，范围[1~20]
    * @param  [in]  value 变量值
    * @return  错误码
    */
    int SetSysVarValue(int id, double value); 

设置工具参考点-六点法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置工具参考点-六点法 
    * @param [in] point_num 点编号,范围[1~6] 
    * @return 错误码 
    */ 
    int SetToolPoint(int point_num); 

计算工具坐标系--六点法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 计算工具坐标系
    * @param [out] tcp_pose 工具坐标系
    * @return 错误码 
    */ 
    int ComputeTool(ref DescPose tcp_pose); 

设置工具参考点-四点法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置工具参考点-四点法 
    * @param [in] point_num 点编号,范围[1~4] 
    * @return 错误码 
    */ 
    int SetTcp4RefPoint(int point_num);

计算工具坐标系-四点法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 计算工具坐标系
    * @param [out] tcp_pose 工具坐标系
    * @return 错误码 
    */ 
    int ComputeTcp4(ref DescPose tcp_pose);

设置工具坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置工具坐标系
    * @param  [in] id 坐标系编号，范围[0~14]
    * @param  [in] coord  工具中心点相对于末端法兰中心位姿
    * @param  [in] type  0-工具坐标系，1-传感器坐标系
    * @param  [in] install 安装位置，0-机器人末端，1-机器人外部
    * param   [in] toolID 工具ID
    * @param  [in] loadNum 负载编号
    * @return  错误码
    */
    int SetToolCoord(int id, DescPose coord, int type, int install,int toolID, int loadNum);  

设置工具坐标系列表
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置工具坐标系列表
    * @param  [in] id 坐标系编号，范围[0~14]
    * @param  [in] coord  工具中心点相对于末端法兰中心位姿
    * @param  [in] type  0-工具坐标系，1-传感器坐标系
    * @param  [in] install 安装位置，0-机器人末端，1-机器人外部
    * @param  [in] loadNum 负载编号
    * @return  错误码
    */
    int SetToolList(int id, DescPose coord, int type, int install, int loadNum);  

设置外部工具坐标参考点-三点法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置外部工具参考点-三点法 
    * @param [in] point_num 点编号,范围[1~3] 
    * @return 错误码 
    */ 
    int SetExTCPPoint(int point_num); 

计算外部工具坐标系-三点法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:
    
    /** 
    * @brief 计算外部工具坐标系-三点法
    * @param [out] tcp_pose 外部工具坐标系
    * @return 错误码 
    */ 
    int ComputeExTCF(ref DescPose tcp_pose); 

设置外部工具坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置外部工具坐标系 
    * @param [in] id 坐标系编号，范围[0~14] 
    * @param [in] etcp 工具中心点相对末端法兰中心位姿 
    * @param [in] etool 待定 
    * @return 错误码 
    */
    int SetExToolCoord(int id, DescPose etcp, DescPose etool); 

设置外部工具坐标系列表
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置外部工具坐标系列表
    * @param  [in] id 坐标系编号，范围[0~14] 
    * @param  [in] etcp  工具中心点相对末端法兰中心位姿
    * @param  [in] etool  待定
    * @return  错误码
    */
    int SetExToolList(int id, DescPose etcp, DescPose etool); 

设置工件坐标系参考点-三点法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置工件参考点-三点法 
    * @param [in] point_num 点编号,范围[1~3]  
    * @return 错误码 
    */ 
    int SetWObjCoordPoint(int point_num); 

计算工件坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  计算工件坐标系
    * @param [in] method 计算方法 0：原点-x轴-z轴  1：原点-x轴-xy平面
    * @param [in] refFrame 参考坐标系
    * @param [out] wobj_pose 工件坐标系
    * @return 错误码
    */
    int ComputeWObjCoord(int method, int refFrame, ref DescPose wobj_pose); 

设置工件坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置工件坐标系
    * @param  [in] id 坐标系编号，范围[1~15]
    * @param  [in] coord  工件坐标系相对于末端法兰中心位姿
    * @param  [in] refFrame 参考坐标系
    * @return  错误码
    */
    int SetWObjCoord(int id, DescPose coord, int refFrame);

设置工件坐标系列表
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置工件坐标系列表
    * @param  [in] id 坐标系编号，范围[0~14] 
    * @param  [in] coord  工件坐标系相对于末端法兰中心位姿
    * @param  [in] refFrame 参考坐标系
    * @return  错误码
    */    
    int SetWObjList(int id, DescPose coord, int refFrame);

设置末端负载重量
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置末端负载重量
    * @param  [in] loadNum 负载编号
    * @param  [in] weight  负载重量，单位kg
    * @return  错误码
    */
    int SetLoadWeight(int loadNum, float weight)

设置末端负载质心坐标
+++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置末端负载质心坐标
    * @param  [in] coord 质心坐标，单位mm
    * @return  错误码
    */
    int SetLoadCoord(DescTran coord); 

设置机器人安装方式
+++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置机器人安装方式
    * @param  [in] install  安装方式，0-正装，1-侧装，2-倒装
    * @return  错误码
    */
    int SetRobotInstallPos(byte install); 

设置机器人安装角度
+++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置机器人安装角度，自由安装
    * @param  [in] yangle  倾斜角
    * @param  [in] zangle  旋转角
    * @return  错误码
    */
    int SetRobotInstallAngle(double yangle, double zangle); 

代码示例
++++++++++
.. code-block:: c#
    :linenos:

    private void btnCommonSets_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        int i;
        double value = 0;
        int id;
        int type;
        int install;

        DescTran coord = new DescTran();
        DescPose t_coord, etcp, etool, w_coord;
        t_coord = new DescPose();
        etcp = new DescPose();
        w_coord = new DescPose();

        robot.SetSpeed(20);

        for (i = 1; i < 21; i++)
        {
            robot.SetSysVarValue(i, (float)(i + 0.5));
            robot.WaitMs(100);
        }

        for (i = 1; i < 21; i++)
        {
            robot.GetSysVarValue(i, ref value);
            Console.WriteLine($"sys value : {value}");
        }

        robot.SetLoadWeight((float)2.5);
        coord.x = 3.0;
        coord.y = 4.0;
        coord.z = 5.0;
        robot.SetLoadCoord(coord);
                
        id = 3;
        t_coord.tran.x = 1.0;
        t_coord.tran.y = 2.0;
        t_coord.tran.z = 300.0;
        t_coord.rpy.rx = 4.0;
        t_coord.rpy.ry = 5.0;
        t_coord.rpy.rz = 6.0;
        type = 0;
        install = 0;

        int rtn1 = -1;
        int rtn2 = -1;
        rtn1 = robot.SetToolCoord(id, t_coord, type, install);
        rtn2 = robot.SetToolList(id, t_coord, type, install);
        Console.WriteLine($"set tool coord result {rtn1}, set tool list rtn{rtn2}");
            
        etcp.tran.x = 1.0;
        etcp.tran.y = 2.0;
        etcp.tran.z = 3.0;
        etcp.rpy.rx = 4.0;
        etcp.rpy.ry = 5.0;
        etcp.rpy.rz = 6.0;
        etool.tran.x = 11.0;
        etool.tran.y = 22.0;
        etool.tran.z = 330.0;
        etool.rpy.rx = 44.0;
        etool.rpy.ry = 55.0;
        etool.rpy.rz = 66.0;
        id = 5;
        robot.SetExToolCoord(id, etcp, etool);
        robot.SetExToolList(id, etcp, etool);

        w_coord.tran.x = 110.0;
        w_coord.tran.y = 12.0;
        w_coord.tran.z = 13.0;
        w_coord.rpy.rx = 14.0;
        w_coord.rpy.ry = 15.0;
        w_coord.rpy.rz = 16.0;
        id = 12;
        robot.SetWObjCoord(id, w_coord);
        //robot.SetWObjList(id, w_coord);

        double yangle = 0, zangle = 0;
        robot.SetRobotInstallPos(1);//侧装
        robot.SetRobotInstallAngle(15.0, 25.0);
        Thread.Sleep(1000);
        robot.GetRobotInstallAngle(ref yangle, ref zangle);
        Console.WriteLine($"yangle  {yangle}   zangle  {zangle}");
        robot.SetRobotInstallAngle(10.0, 10.0);
        Thread.Sleep(1000);
        robot.GetRobotInstallAngle(ref yangle, ref zangle);
        Console.WriteLine($"yangle  {yangle}   zangle  {zangle}");
    }

等待指定时间
+++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  等待指定时间
    * @param  [in]  t_ms  单位ms
    * @return  错误码
    */
    int WaitMs(int t_ms);

设置机器人加速度
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置机器人加速度
    * @param [in] acc 机器人加速度百分比
    * @return 错误码
    */
    int SetOaccScale(double acc)

根据点位信息计算工具坐标系
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 根据点位信息计算工具坐标系
    * @param [in] method 计算方法；0-四点法；1-六点法
    * @param [in] pos 关节位置组，四点法时数组长度为4个，六点法时数组长度为6个
    * @return 错误码
    */

    int ComputeToolCoordWithPoints(int method, JointPos[] pos, ref DescPose coordRtn)

根据点位信息计算工件坐标系
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 根据点位信息计算工件坐标系
    * @param [in] method 计算方法；0：原点-x轴-z轴  1：原点-x轴-xy平面
    * @param [in] pos 三个TCP位置组
    * @param [in] refFrame 参考坐标系
    * @return 错误码
    */
    int ComputeWObjCoordWithPoints(int method, DescPose[] pos, int refFrame, ref DescPose coordRtn)

代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8
    
.. code-block:: c#
    :linenos:

    private void TestTCP_Click(object sender, EventArgs e)
    {
      DescPose p1Desc = new DescPose(-394.073, -276.405, 399.451, -133.692, 7.657, -139.047);
      JointPos p1Joint = new JointPos(15.234, -88.178, 96.583, -68.314, -52.303, -122.926);

      DescPose p2Desc = new DescPose( -187.141, -444.908, 432.425, 148.662, 15.483, -90.637);
      JointPos p2Joint = new JointPos(61.796, -91.959, 101.693, -102.417, -124.511, -122.767);

      DescPose p3Desc = new DescPose(-368.695, -485.023, 426.640, -162.588, 31.433, -97.036);
      JointPos p3Joint = new JointPos(43.896, -64.590, 60.087, -50.269, -94.663, -122.652);

      DescPose p4Desc = new DescPose(-291.069, -376.976, 467.560, -179.272, -2.326, -107.757);
      JointPos p4Joint = new JointPos(39.559, -94.731, 96.307, -93.141, -88.131, -122.673);

      DescPose p5Desc = new DescPose(-284.140, -488.041, 478.579, 179.785, -1.396, -98.030);
      JointPos p5Joint = new JointPos(49.283, -82.423, 81.993, -90.861, -89.427, -122.678);

      DescPose p6Desc = new DescPose(-296.307, -385.991, 484.492, -178.637, -0.057, -107.059);
      JointPos p6Joint = new JointPos(40.141, -92.742, 91.410, -87.978, -88.824, -122.808);

      ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
      DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

      JointPos[] posJ = new JointPos[6]{ p1Joint, p2Joint, p3Joint, p4Joint, p5Joint, p6Joint };
      DescPose coordRtn = new DescPose(0, 0, 0, 0, 0, 0); 
      int rtn = robot.ComputeToolCoordWithPoints(0, posJ,ref coordRtn);
      Console.WriteLine("ComputeToolCoordWithPoints {0}  coord is {1} {2} {3} {4} {5} {6}", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);


      robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
      robot.SetTcp4RefPoint(1);
      robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
      robot.SetTcp4RefPoint(2);
      robot.MoveJ(p3Joint, p3Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
      robot.SetTcp4RefPoint(3);
      robot.MoveJ(p4Joint, p4Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
      robot.SetTcp4RefPoint(4);
      robot.ComputeTcp4(ref coordRtn);
      Console.WriteLine("ComputeTcp4 {0}  coord is {1} {2} {3} {4} {5} {6}", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
      //robot.MoveJ(p5Joint, p5Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
      //robot.MoveJ(p6Joint, p6Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
    }




