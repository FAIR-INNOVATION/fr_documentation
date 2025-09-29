其他接口
================

.. toctree:: 
    :maxdepth: 5

获取SSH公钥
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取SSH公钥 
    * @param [out] keygen 公钥
    * @return 错误码 
    */
    int GetSSHKeygen(ref string keygen);

下发SCP指令
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 下发SCP指令
    * @param [in] mode 0-上传（上位机->控制器），1-下载（控制器->上位机）
    * @param [in] sshname 上位机用户名
    * @param [in] sship 上位机ip地址
    * @param [in] usr_file_url 上位机文件路径
    * @param [in] robot_file_url 机器人控制器文件路径
    * @return 错误码
    */
    int SetSSHScpCmd(int mode, string sshname, string sship, string usr_file_url, string robot_file_url);

计算指定路径下文件的MD5值
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 计算指定路径下文件的MD5值 
    * @param [in] file_path 文件路径包含文件名，默认Traj文件夹路径为:"/fruser/traj/",如"/fruser/traj/trajHelix_aima_1.txt"
    * @param [out] md5 文件MD5值
    * @return 错误码 
    */
    int ComputeFileMD5(string file_path, ref string md5);

机器人SSH、MD5指令代码示例
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    private void button46_Click(object sender, EventArgs e)
    {
        string file_path = "/fruser/airlab.lua";
        string md5 = "";
        byte emerg_state = 0;
        byte si0_state = 0;
        byte si1_state = 0;
        int sdk_com_state = 0;

        string ssh_keygen = "";
        int retval = robot.GetSSHKeygen(ref ssh_keygen);
        Console.WriteLine("GetSSHKeygen retval is: {0}", retval);
        Console.WriteLine("ssh key is: {0}", ssh_keygen);

        string ssh_name = "fr";
        string ssh_ip = "192.168.58.45";
        string ssh_route = "/home/fr";
        string ssh_robot_url = "/root/robot/dhpara.config";
        retval = robot.SetSSHScpCmd(1, ssh_name, ssh_ip, ssh_route, ssh_robot_url);
        Console.WriteLine("SetSSHScpCmd retval is: {0}", retval);
        Console.WriteLine("robot url is: {0}", ssh_robot_url);

        robot.ComputeFileMD5(file_path, ref md5);
        Console.WriteLine("md5 is: {0}", md5);
    }

设置机器人 20004 端口反馈周期
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置机器人 20004 端口反馈周期
    * @param [in] period 机器人 20004 端口反馈周期(ms)
    * @return 错误码
    */
    int SetRobotRealtimeStateSamplePeriod(int period);

获取机器人 20004 端口反馈周期
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取机器人 20004 端口反馈周期
    * @param [out] period 机器人 20004 端口反馈周期(ms)
    * @return 错误码
    */
    int GetRobotRealtimeStateSamplePeriod((ref int period);   

机器人20004端口状态反馈周期配置代码示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button47_Click(object sender, EventArgs e)
    {
        robot.SetRobotRealtimeStateSamplePeriod(10);
        int getPeriod = 0;
        robot.GetRobotRealtimeStateSamplePeriod(ref getPeriod);
        Console.WriteLine("period is {0}", getPeriod);
        Thread.Sleep(1000);
    }

机器人软件升级
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 机器人软件升级
    * @param [in] filePath 软件升级包全路径
    * @param [in] block 是否阻塞至升级完成 true:阻塞；false:非阻塞
    * @return  错误码
    */
    int SoftwareUpgrade(string filePath, bool block);

获取机器人软件升级状态
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取机器人软件升级状态
    * @param [out] state 机器人软件包升级状态  0-空闲中或上传升级包中；1~100：升级完成百分比；-1:升级软件失败；-2：校验失败；-3：版本校验失败；-4：解压失败；-5：用户配置升级失败；-6：外设配置升级失败；-7：扩展轴配置升级失败；-8：机器人配置升级失败；-9：DH参数配置升级失败
    * @return  错误码
    */
    int GetSoftwareUpgradeState(ref int state);

机器人软件升级代码示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button48_Click(object sender, EventArgs e)
    {
        robot.SoftwareUpgrade("D://zUP/QNX382/software.tar.gz", false);
        while (true)
        {
            int curState = -1;
            robot.GetSoftwareUpgradeState(ref curState);
            Console.WriteLine("upgrade state is {0}", curState);
            Thread.Sleep(300);
        }
    }

下载点位表
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 点位表从机器人控制器下载到本地计算机 
    * @param [in] pointTableName 控制器中的点位表名称：pointTable1.db
    * @param [in] saveFilePath 点位表下载到计算机的路径 C://test/
    * @return 错误码 
    */
    int PointTableDownLoad(string pointTableName, string saveFilePath);

上传点位表
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 点位表从本地计算机上传至机器人控制器 
    * @param [in] pointTableFilePath 点位表在本地计算机的绝对路径C://test/pointTabl e1.db
    * @return 错误码 
    */
    int PointTableUpLoad(string pointTableFilePath);

点位表更新Lua程序
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 使用给定的点位表更新lua程序中的点
    * @param [in] pointTableName 控制器中的点位表名称："pointTable1.db", 当点位表为空，即""时，表示将lua程序更新为未应用点位表的初始程序
    * @param [in] luaFileName 要更新的lua文件名称   "test.lua"
    * @param [out] errorStr 点位表更新lua错误信息  
    * @return 错误码 
    */
    int PointTableUpdateLua(string pointTableName, string luaFileName, ref string errorStr);

切换点位表并应用
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 切换点位表并应用
    * @param [in] pointTableName 要切换的点位表名称   "pointTable1.db"
    * @param [out] errorStr 切换点位表错误信息   
    * @return 错误码 
    */
    int PointTableSwitch(string pointTableName, ref string errorStr);

机器人点位表操作代码示例
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnUpload_Click(object sender, EventArgs e)
    {
        string save_path = "D://zDOWN/";
        string point_table_name = "test_point_A.db";
        int rtn = robot.PointTableDownLoad(point_table_name, save_path);
        Console.WriteLine("download : {0} fail: {1}", point_table_name, rtn);

        string upload_path = "D://zUP/test_point_A.db";
        rtn = robot.PointTableUpLoad(upload_path);
        Console.WriteLine("retval is: {0}", rtn);

        string point_tablename = "test_point_A.db";
        string lua_name = "Text1.lua";

        string errorStr = "";
        rtn = robot.PointTableUpdateLua(point_tablename, lua_name, ref errorStr);
        Console.WriteLine("retval is: {0}", rtn);
    }

控制器日志下载
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  控制器日志下载
    * @param [in] savePath 保存文件路径"D://zDown/"
    * @return  错误码
    */
    int RbLogDownload(string savePath);

所有数据源下载
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 所有数据源下载
    * @param [in] savePath 保存文件路径"D://zDown/"
    * @return  错误码
    */
    int AllDataSourceDownload(string savePath);

数据备份包下载
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 数据备份包下载
    * @param [in] savePath 保存文件路径"D://zDown/"
    * @return  错误码
    */
    int DataPackageDownload(string savePath);

下载控制器数据代码示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button50_Click(object sender, EventArgs e)
    {
        int rtn = robot.RbLogDownload("D://zDOWN/");
        Console.WriteLine("RbLogDownload rtn is {0}", rtn);

        rtn = robot.AllDataSourceDownload("D://zDOWN/");
        Console.WriteLine("AllDataSourceDownload rtn is {0}", rtn);

        rtn = robot.DataPackageDownload("D://zDOWN/");
        Console.WriteLine("DataPackageDownload rtn is {0}", rtn);
    }

机器人操作系统升级(LA控制箱)
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
     * @brief 机器人操作系统升级(LA控制箱)
     * @param [in] filePath 操作系统升级包全路径
     * @return  错误码
     */
    public int KernelUpgrade(string filePath)

获取机器人操作系统升级结果(LA控制箱)
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
     * @brief 获取机器人操作系统升级结果(LA控制箱)
     * @param [out] result 升级结果：0:成功；-1:失败
     * @return  错误码
     */
    public int GetKernelUpgradeResult(ref int[] result)









