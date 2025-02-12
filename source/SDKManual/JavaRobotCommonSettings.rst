机器人常用设置
=================

.. toctree:: 
    :maxdepth: 5

设置全局速度
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置全局速度
    * @param  [in]  vel  速度百分比，范围[0~100]
    * @return  错误码
    */
    int SetSpeed(int vel); 

设置系统变量值
++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置工具参考点-六点法
    * @param [in] point_num 点编号,范围[1~6]
    * @return 错误码 
    */ 
    int SetToolPoint(int point_num); 

计算工具坐标系--六点法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 计算工具坐标系
    * @param [out] tcp_pose 工具坐标系
    * @return 错误码 
    */ 
    int ComputeTool(DescPose tcp_pose); 

设置工具参考点-四点法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置工具参考点-四点法
    * @param [in] point_num 点编号,范围[1~4]
    * @return 错误码 
    */ 
    int SetTcp4RefPoint(int point_num);

计算工具坐标系-四点法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 计算工具坐标系
    * @param [out] tcp_pose 工具坐标系
    * @return 错误码 
    */ 
    int ComputeTcp4(DescPose tcp_pose);

设置工具坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置工具坐标系 
    * @param [in] id 坐标系编号，范围[0~14]
    * @param [in] coord  工具中心点相对于末端法兰中心位姿
    * @param [in] type  0-工具坐标系，1-传感器坐标系
    * @param [in] install 安装位置，0-机器人末端，1-机器人外部
    * @param [in] toolID  工具ID
    * @param [in] loadNum  负载编号
    * @return 错误码 
    */ 
    int SetToolCoord(int id, DescPose coord, int type, int install, int toolID, int loadNum);  

设置工具坐标系列表
++++++++++++++++++++++++++++++++++
.. code-block:: Java
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

代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        robot.Mode(1);
        robot.SetSpeed(20);
        robot.Mode(0);

        for(int i = 1; i < 10; i++)
        {
            robot.SetSysVarValue(i, i * 10);
        }
        for(int i = 1; i < 10; i++)
        {
            List<Number> rtnArr = robot.GetSysVarValue(i);//获取系统变量
            System.out.println("SysVarValue " +  i  + " is " + rtnArr.get(1));
        }

        JointPos jp1=new JointPos(-89.407,-148.279,-83.169,-45.689,133.689,41.705);
        JointPos jp2=new JointPos(-67.595,-143.7,-88.006,-48.514,57.073,56.189);
        JointPos jp3=new JointPos(-88.229,-152.355,-67.815,-78.07,129.029,58.739);
        JointPos jp4=new JointPos(-77.528,-141.519,-89.826,-37.184,90.274,41.769);
        JointPos jp5=new JointPos(-76.744,-138.219,-97.714,-32.595,90.255,42.558);
        JointPos jp6=new JointPos(-77.595,-138.454,-90.065,-40.014,90.275,41.709);
        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();

        DescPose desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p3 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p4 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p5 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p6 = new DescPose(0, 0, 0, 0, 0, 0);
        robot.GetForwardKin(jp1, desc_p1);
        robot.GetForwardKin(jp2, desc_p2);
        robot.GetForwardKin(jp3, desc_p3);
        robot.GetForwardKin(jp4, desc_p4);
        robot.GetForwardKin(jp5, desc_p5);
        robot.GetForwardKin(jp6, desc_p6);
        robot.MoveJ(jp1, desc_p1,0, 0, 30, 100, 100, epos, -1, 0, offset_pos);
        robot.SetToolPoint(1);

        robot.MoveJ(jp2, desc_p2,0, 0, 30, 100, 100, epos, -1, 0, offset_pos);
        robot.SetToolPoint(2);

        robot.MoveJ(jp3, desc_p3,0, 0, 30, 100, 100, epos, -1, 0, offset_pos);
        robot.SetToolPoint(3);

        robot.MoveJ(jp4, desc_p4,0, 0, 30, 100, 100, epos, -1, 0, offset_pos);
        robot.SetToolPoint(4);

        robot.MoveJ(jp5, desc_p5,0, 0, 30, 100, 100, epos, -1, 0, offset_pos);
        robot.SetToolPoint(5);

        robot.MoveJ(jp6, desc_p6,0, 0, 30, 100, 100, epos, -1, 0, offset_pos);
        robot.SetToolPoint(6);

        DescPose coord = new DescPose();
        robot.ComputeTool(coord);
        System.out.println("result is " + coord.tran.x + "  " + coord.tran.y + "  " + coord.tran.z + "  " + coord.rpy.rx + "  " + coord.rpy.ry + "  " + coord.rpy.rz);

        robot.SetToolCoord(5, coord, 0, 0,0,0);//设置工具坐标系
        robot.SetToolList(5, coord, 0, 0, 0);
    }

根据点位信息计算工具坐标系
++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
    :linenos:

    /** 
    * @brief 根据点位信息计算工具坐标系
    * @param [in] method 计算方法；0-四点法；1-六点法
    * @param [in] pos 关节位置组，四点法时数组长度为4个，六点法时数组长度为6个
    * @param [in] tool_pose 输出的工具坐标系
    * @return 错误码 
    */ 
    int ComputeToolCoordWithPoints(int method, JointPos[] pos,DescPose tool_pose);

根据点位信息计算工件坐标系
++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
    :linenos:

    /** 
    * @brief 根据点位信息计算工件坐标系
    * @param [in] method 计算方法；0：原点-x轴-z轴  1：原点-x轴-xy平面
    * @param [in] pos 三个TCP位置组
    * @param [in] refFrame 参考坐标系
    * @param [in] tcp_pose 输出工件坐标系
    * @return 错误码 
    */ 
    int ComputeWObjCoordWithPoints(int method, DescPose[] pos, int refFrame,DescPose tcp_pose);

代码示例
++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        
        DescPose p1Desc=new DescPose(-394.073, -276.405, 399.451, -133.692, 7.657, -139.047);
        JointPos p1Joint=new JointPos(15.234, -88.178, 96.583, -68.314, -52.303, -122.926);

        DescPose p2Desc=new DescPose(-187.141, -444.908, 432.425, 148.662, 15.483, -90.637);
        JointPos p2Joint=new JointPos(61.796, -91.959, 101.693, -102.417, -124.511, -122.767);

        DescPose p3Desc=new DescPose(-368.695, -485.023, 426.640, -162.588, 31.433, -97.036);
        JointPos p3Joint=new JointPos(43.896, -64.590, 60.087, -50.269, -94.663, -122.652);

        DescPose p4Desc=new DescPose(-291.069, -376.976, 467.560, -179.272, -2.326, -107.757);
        JointPos p4Joint=new JointPos(39.559, -94.731, 96.307, -93.141, -88.131, -122.673);

        DescPose p5Desc=new DescPose(-284.140, -488.041, 478.579, 179.785, -1.396, -98.030);
        JointPos p5Joint=new JointPos(49.283, -82.423, 81.993, -90.861, -89.427, -122.678);

        DescPose p6Desc=new DescPose(-296.307, -385.991, 484.492, -178.637, -0.057, -107.059);
        JointPos p6Joint=new JointPos(40.141, -92.742, 91.410, -87.978, -88.824, -122.808);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);

        JointPos[] posJ = { p1Joint , p2Joint , p3Joint , p4Joint , p5Joint , p6Joint };
        DescPose coordRtn = new DescPose();
        int rtn = robot.ComputeToolCoordWithPoints(1, posJ, coordRtn);
        System.out.println("ComputeToolCoordWithPoints: "+rtn+ ", coord is :"+ coordRtn.tran.x+","+coordRtn.tran.y+","+coordRtn.tran.z+","+ coordRtn.rpy.rx+","+ coordRtn.rpy.ry+","+coordRtn.rpy.rz);


        robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetToolPoint(1);
        robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetToolPoint(2);
        robot.MoveJ(p3Joint, p3Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetToolPoint(3);
        robot.MoveJ(p4Joint, p4Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetToolPoint(4);
        robot.MoveJ(p5Joint, p5Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetToolPoint(5);
        robot.MoveJ(p6Joint, p6Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetToolPoint(6);
        robot.ComputeTool(coordRtn);
        System.out.println("ComputeTool :"+rtn+",coord is :"+coordRtn.tran.x+","+ coordRtn.tran.y+","+ coordRtn.tran.z+","+ coordRtn.rpy.rx+","+ coordRtn.rpy.ry+","+ coordRtn.rpy.rz);
    }

设置外部工具坐标参考点-三点法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置外部工具参考点-三点法 
    * @param [in] point_num 点编号,范围[1~3]
    * @return 错误码 
    */ 
    int SetExTCPPoint(int point_num); 

计算外部工具坐标系-三点法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:
    
    /** 
    * @brief 计算外部工具坐标系-三点法
    * @param [out] tcp_pose 外部工具坐标系
    * @return 错误码 
    */ 
    int ComputeExTCF(DescPose tcp_pose); 

设置外部工具坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置外部工具坐标系 
    * @param [in] id 坐标系编号，范围[0~14]
    * @param [in] etcp  工具中心点相对末端法兰中心位姿
    * @param [in] etool  待定
    * @return 错误码 
    */
    int SetExToolCoord(int id, DescPose etcp, DescPose etool); 

设置外部工具坐标系列表
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置外部工具坐标系列表
    * @param  [in] id 坐标系编号，范围[0~14]
    * @param  [in] etcp  工具中心点相对末端法兰中心位姿
    * @param  [in] etool  待定
    * @return  错误码
    */
    int SetExToolList(int id, DescPose etcp, DescPose etool); 

代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        robot.Mode(1);
        robot.SetSpeed(20);
        robot.Mode(0);

        for(int i = 1; i < 10; i++)
        {
            robot.SetSysVarValue(i, i * 10);
        }
        for(int i = 1; i < 10; i++)
        {
            List<Number> rtnArr = robot.GetSysVarValue(i);//获取系统变量
            System.out.println("SysVarValue " +  i  + " is " + rtnArr.get(1));
        }

        JointPos j1 = new JointPos(-84.787, -152.056,-75.689 , -37.899, 94.486,41.709);
        JointPos j2 = new JointPos(-79.438,-152.139,-75.634,-37.469,94.065,47.058);
        JointPos j3 = new JointPos(-84.788,-145.179,-77.119,-43.345,94.487,41.709);


        DescPose desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p3 = new DescPose(0, 0, 0, 0, 0, 0);

        robot.GetForwardKin(j1, desc_p1);
        robot.GetForwardKin(j2, desc_p2);
        robot.GetForwardKin(j3, desc_p3);

        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();

        robot.MoveJ(j1, desc_p1,0, 0, 20, 100, 100, epos, -1, 0, offset_pos);
        robot.SetExTCPPoint(1);

        robot.MoveJ(j2, desc_p2,0, 0, 20, 100, 100, epos, -1, 0, offset_pos);
        robot.SetExTCPPoint(2);

        robot.MoveJ(j3, desc_p3,0, 0, 20, 100, 100, epos, -1, 0, offset_pos);
        robot.SetExTCPPoint(3);

        DescPose coordE = new DescPose();
        robot.ComputeExTCF(coordE);
        System.out.println("result is " + coordE.tran.x + "  " + coordE.tran.y + "  " + coordE.tran.z + "  " + coordE.rpy.rx + "  " + coordE.rpy.ry + "  " + coordE.rpy.rz);

        robot.SetExToolCoord(5, coordE, coordE);
        robot.SetExToolList(5,coordE, coordE);
    }

设置工件坐标系参考点-三点法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置工件参考点-三点法 
    * @param [in] point_num 点编号,范围[1~3]
    * @return 错误码 
    */ 
    int SetWObjCoordPoint(int point_num); 

计算工件坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 计算工件坐标系
    * @param [in]  method 计算方式 0：原点-x轴-z轴  1：原点-x轴-xy平面
    * @param [in]  refFrame 参考坐标系
    * @param [out]  wobj_pose 工件坐标系
    * @return 错误码 
    */ 
    int ComputeWObjCoord(int method, int refFrame, DescPose wobj_pose); 

设置工件坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置工件坐标系列表
    * @param  [in] id 坐标系编号，范围[1~15]
    * @param  [in] coord  工件坐标系相对于末端法兰中心位姿
    * @param  [in] refFrame 参考坐标系
    * @return  错误码
    */    
    int SetWObjList(int id, DescPose coord, int refFrame);

代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }

        JointPos j1 = new JointPos(-84.787, -152.056,-75.689,-37.899,94.486,41.709);
        JointPos j2 = new JointPos(-79.438,-152.139,-75.634,-37.469,94.065,47.058);
        JointPos j3 = new JointPos(-84.788,-145.179,-77.119,-43.345,94.487,41.709);
        DescPose desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p3 = new DescPose(0, 0, 0, 0, 0, 0);

        robot.GetForwardKin(j1, desc_p1);
        robot.GetForwardKin(j2, desc_p2);
        robot.GetForwardKin(j3, desc_p3);

        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();

        robot.MoveJ(j1, desc_p1,0, 0, 20, 100, 100, epos, -1, 0, offset_pos);
        robot.SetWObjCoordPoint(1);

        robot.MoveJ(j2, desc_p2,0, 0, 20, 100, 100, epos, -1, 0, offset_pos);
        robot.SetWObjCoordPoint(2);

        robot.MoveJ(j3, desc_p3,0, 0, 20, 100, 100, epos, -1, 0, offset_pos);
        robot.SetWObjCoordPoint(3);

        DescPose coordE = new DescPose();
        robot.ComputeWObjCoord(0, coordE);
        System.out.println("result is " + coordE.tran.x + "  " + coordE.tran.y + "  " + coordE.tran.z + "  " + coordE.rpy.rx + "  " + coordE.rpy.ry + "  " + coordE.rpy.rz);

        robot.SetWObjCoord(5, coordE,0);
        robot.SetWObjList(5,coordE,0);
    }

设置末端负载重量
++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
    :linenos:

    /**
    * @brief  设置末端负载重量
    * @param  [in] loadNum 负载编号
    * @param  [in] weight  负载重量，单位kg
    * @return  错误码
    */
    int SetLoadWeight(int loadNum,double weight);

设置末端负载质心坐标
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置末端负载质心坐标
    * @param  [in] coord 质心坐标，单位mm
    * @return  错误码
    */
    int SetLoadCoord(DescTran coord); 

设置机器人安装方式
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置机器人安装方式
    * @param  [in]  install  安装方式，0-正装，1-侧装，2-倒装
    * @return  错误码
    */
    int SetRobotInstallPos(int install); 

设置机器人安装角度
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置机器人安装角度，自由安装
    * @param  [in] yangle  倾斜角
    * @param  [in] zangle  旋转角
    * @return  错误码
    */
    int SetRobotInstallAngle(double yangle, double zangle); 

代码示例
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        robot.SetLoadWeight(2);
        robot.SetLoadCoord(new DescTran(1.0, 2.0, 3.0));
        robot.SetRobotInstallPos(0);
        robot.SetRobotInstallAngle(0, 0);
    }

等待指定时间
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  等待指定时间
    * @param  [in]  t_ms  单位ms
    * @return  错误码
    */
    int WaitMs(int t_ms);

设置机器人加速度
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置机器人加速度
    * @param [in] acc 机器人加速度百分比
    * @return 错误码
    */
    int SetOaccScale(double acc);