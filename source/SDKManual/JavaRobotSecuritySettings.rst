机器人安全设置
=================

.. toctree:: 
    :maxdepth: 5

设置碰撞等级
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置碰撞等级
    * @param  [in]  mode  0-等级，1-百分比
    * @param  [in]  level 碰撞阈值，等级对应范围[1 - 10对应等级1-10， 100-关闭],百分比对应范围[0~10 对应 0% - 100%]
    * @param  [in]  config 0-不更新配置文件，1-更新配置文件
    * @return  错误码
    */
    int SetAnticollision(int mode, Object[] level, int config); 

设置碰撞后策略
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置碰撞后策略
    * @param  [in] strategy  0-报错停止，1-继续运行
    * @param  [in] safeTime  安全停止时间[1000 - 2000]ms
    * @param  [in] safeDistance  安全停止距离[1-150]mm
    * @param  [in] safetyMargin  j1-j6安全系数[1-10]
    * @return  错误码  
    */
    int SetCollisionStrategy(int strategy, int safeTime, int safeDistance, int safetyMargin[]); 

自定义碰撞检测阈值功能开始
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.3-3.8.0

.. code-block:: Java
    :linenos:

    /**
    * @brief  自定义碰撞检测阈值功能开始，设置关节端和TCP端的碰撞检测阈值
    * @param  [in] flag 1-仅关节检测开启；2-仅TCP检测开启；3-关节和TCP检测同时开启
    * @param  [in] jointDetectionThreshould 关节碰撞检测阈值 j1-j6
    * @param  [in] tcpDetectionThreshould  TCP碰撞检测阈值，xyzabc
    * @param  [in] block 0-非阻塞；1-阻塞
    * @return  错误码
    */   
    public int CustomCollisionDetectionStart(int flag, double[] jointDetectionThreshould, double[] tcpDetectionThreshould, int block);

自定义碰撞检测阈值功能关闭
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.3-3.8.0

.. code-block:: Java
    :linenos:

    /**
    * @brief  自定义碰撞检测阈值功能关闭
    * @return  错误码
    */   
    public int CustomCollisionDetectionEnd();

机器人碰撞等级设置代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestCollision(Robot robot)
    {
        int mode = 0;
        int config = 1;
        Object[] level1 = new Object[]{ 1.0,2.0,3.0,4.0,5.0,6.0 };
        Object[] level2 = new Object[]{ 50.0,20.0,30.0,40.0,50.0,60.0 };

        int rtn = robot.SetAnticollision(mode, level1, config);
        System.out.println("SetAnticollision mode 0 rtn is: "+ rtn);
        mode = 1;
        rtn = robot.SetAnticollision(mode, level2, config);
        System.out.println("SetAnticollision mode 1 rtn is :"+ rtn);

        JointPos p1Joint=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos p2Joint=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        DescPose p1Desc=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose p2Desc=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        ExaxisPos exaxisPos=new ExaxisPos(0.0, 0.0, 0.0, 0.0);
        DescPose offdese=new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        robot.MoveL(p2Joint, p2Desc, 0, 0, 100, 100, 100, 2,0, exaxisPos, 0, 0, offdese,0,10);
        robot.ResetAllError();
        int[] safety = new int[]{ 5,5,5,5,5,5 };
        rtn = robot.SetCollisionStrategy(3, 1000, 150, 250, safety);
        System.out.println("SetCollisionStrategy rtn is:"+ rtn);

        double[] jointDetectionThreshould = new double[]{ 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 };
        double[] tcpDetectionThreshould =new double[] { 60,60,60,60,60,60 };
        rtn = robot.CustomCollisionDetectionStart(3, jointDetectionThreshould, tcpDetectionThreshould, 0);
        System.out.println("CustomCollisionDetectionStart rtn is :"+ rtn);

        robot.MoveL(p1Joint, p1Desc, 0, 0, 100, 100, 100, -1,0, exaxisPos, 0, 0, offdese,0,10);
        robot.MoveL(p2Joint, p2Desc, 0, 0, 100, 100, 100, -1,0, exaxisPos, 0, 0, offdese,0,10);
        rtn = robot.CustomCollisionDetectionEnd();
        System.out.println("CustomCollisionDetectionEnd rtn is: "+ rtn);
        return 0;
    }

设置正限位
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置正限位
    * @param  [in] limit 六个关节位置，单位deg
    * @return  错误码
    */
    int SetLimitPositive(Object[] limit); 

设置负限位
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置负限位
    * @param  [in] limit 六个关节位置，单位deg
    * @return  错误码
    */
    int SetLimitNegative(Object[] limit); 

获取关节软限位角度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取关节软限位角度
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] negative  负限位角度，单位deg
    * @param  [out] positive  正限位角度，单位deg
    * @return  错误码
    */
    int GetJointSoftLimitDeg(int flag, Object[] negative, Object[] positive); 

机器人限位设置代码示例
++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestLimit(Robot robot)
    {
        Object[] plimit =new Object[] { 170.0,80.0,150.0,80.0,170.0,160.0 };
        robot.SetLimitPositive(plimit);
        Object[] nlimit =new Object[] { -170.0,-260.0,-150.0,-260.0,-170.0,-160.0 };
        robot.SetLimitNegative(nlimit);

        Object[] neg_deg =new Object[] {0, 0 , 0, 0, 0, 0}, pos_deg = new Object[]{0, 0 , 0, 0, 0, 0};
        robot.GetJointSoftLimitDeg(1,  neg_deg,  pos_deg);
        System.out.println("neg limit deg:"+ neg_deg[0]+","+ neg_deg[1]+","+ neg_deg[2]+","+ neg_deg[3]+","+ neg_deg[4]+","+ neg_deg[5]);
        System.out.println("pos limit deg:"+pos_deg[0]+","+ pos_deg[1]+","+ pos_deg[2]+","+ pos_deg[3]+","+ pos_deg[4]+","+pos_deg[5]);
        return 0;
    }

设置机器人碰撞检测方法
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief 设置机器人碰撞检测方法
    * @param [in] method 碰撞检测方法：0-电流模式；1-双编码器；2-电流和双编码器同时开启
    * @param [in] thresholdMode 碰撞等级阈值方式；0-碰撞等级固定阈值方式；1-自定义碰撞检测阈值
    * @return 错误码
    */
    int SetCollisionDetectionMethod(int method,int thresholdMode)

设置静态下碰撞检测开始关闭
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置静态下碰撞检测开始关闭
    * @param  [in] status 0-关闭；1-开启
    * @return  错误码
    */
    public int SetStaticCollisionOnOff(int status)

设置机器人碰撞检测方法代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestCollisionMethod(Robot robot)
    {
        int rtn = robot.SetCollisionDetectionMethod(0);

        rtn = robot.SetStaticCollisionOnOff(1);
        System.out.println("SetStaticCollisionOnOff On rtn is:"+ rtn);
        robot.Sleep(5000);
        rtn = robot.SetStaticCollisionOnOff(0);
        System.out.println("SetStaticCollisionOnOff Off rtn is:"+ rtn);

        robot.CloseRPC();
        return 0;
    }

关节扭矩功率检测
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 关节扭矩功率检测
    * @param  [in] status 0-关闭；1-开启
    * @param  [in] power 设定最大功率(W)
    * @return  错误码
    */
    public int SetPowerLimit(int status, double power)

关节扭矩功率检测代码示例
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestPowerLimit(Robot robot)
    {
        robot.DragTeachSwitch(1);
        robot.SetPowerLimit(1, 200);
        List<Number> joint_toq=new ArrayList<>();
        joint_toq=robot.GetJointTorques(1);

        int count = 100;
        robot.ServoJTStart(); //   #servoJT开始
        int error = 0;
        while (count > 0)
        {
            count = count - 1;
            robot.Sleep(1);
        }
        error = robot.ServoJTEnd();
        robot.DragTeachSwitch(0);

        robot.CloseRPC();
        return 0;
    }