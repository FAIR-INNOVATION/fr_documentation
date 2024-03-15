其他接口
=================

.. toctree:: 
    :maxdepth: 5

获取机器人DH参数补偿值
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取机器人DH参数补偿值
    * @param [out] dhCompensation 机器人DH参数补偿值(mm) [cmpstD1,cmpstA2,cmpstA3,cmpstD4,cmpstD5,cmpstD6]
    * @return 错误码
    */
    errno_t GetDHCompensation(double dhCompensation[6]);

下载点位表数据库
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 下载点位表数据库
    * @param [in] pointTableName 要下载的点位表名称    pointTable1.db
    * @param [in] saveFilePath 下载点位表的存储路径   C://test/
    * @return 错误码
    */
    errno_t PointTableDownLoad(const std::string &pointTableName, const std::string &saveFilePath);

上传点位表数据库
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 上传点位表数据库
    * @param [in] pointTableFilePath 上传点位表的全路径名   C://test/pointTable1.db
    * @return 错误码
    */
    errno_t PointTableUpLoad(const std::string &pointTableFilePath);

点位表更新lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 点位表更新lua文件
    * @param [in] pointTableName 要切换的点位表名称   "pointTable1.db",当点位表为空，即""时，表示将lua程序更新为未应用点位表的初始程序
    * @param [in] luaFileName 要更新的lua文件名称   "testPointTable.lua"
    * @param [out] errorStr 切换点位表错误信息
    * @return 错误码
    */
    errno_t PointTableUpdateLua(const std::string &pointTableName, const std::string &luaFileName);

初始化日志参数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 初始化日志参数;
    * @param output_model：输出模式，0-直接输出；1-缓冲输出；2-异步输出;
    * @param file_path: 文件保存路径+名称，,长度上限256，名称必须是xxx.log的形式，比如/home/fr/linux/fairino.log;
    * @param file_num：滚动存储的文件数量，1~20个.单个文件上限50M;
    * @return errno_t 错误码;
    */
	errno_t LoggerInit(int output_model = 0, std::string file_path = "", int file_num = 5);

设置日志过滤等级
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置日志过滤等级;
    * @param lvl: 过滤等级值，值越小输出日志越少，默认值是1. 1-error, 2-warnning, 3-inform, 4-debug;
    */
    void SetLoggerLevel(int lvl = 1);

代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.2.0

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
        robot.LoggerInit(2, "C:/Users/fr/Desktop/c++sdk//sdk_with_log/abcd.log", 2);
        // robot.LoggerInit();
        robot.SetLoggerLevel(3);
        // robot.SetLoggerLevel();
        robot.RPC("192.168.58.2");

        double dh[6] = {0};
        int retval = 0;
        retval = robot.GetDHCompensation(dh);
        cout << "retval is: " << retval << endl;
        cout << "dh is: " << dh[0] << " " << dh[1] << " " << dh[2] << " " << dh[3] << " " << dh[4] << " " << dh[5] << endl;

        string save_path = "D://sharkLog/";
        string point_table_name = "point_table_a.db";
        retval = robot.PointTableDownLoad(point_table_name, save_path);
        cout<<"download : "<<point_table_name<<" fail: "<<retval<< endl;

        string upload_path = "D://sharkLog/0.db";
        retval = robot.PointTableUpLoad(upload_path);
        cout << "retval is: "<<retval<<endl;

        string point_tablename = "point_table_test.db";
        string lua_name = "testPoint.lua";
        retval = robot.PointTableUpdateLua(point_tablename, lua_name);
        cout << "retval is: " << retval << endl;
    }

下载Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 下载Lua文件
    * @param [in] fileName 要下载的lua文件名，例如：“test.lua”
    * @param [in] savePath 保存文件本地路径，例如：“D://Down/”
    * @return 错误码
    */
    errno_t LuaDownLoad(std::string fileName, std::string savePath);

上传Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 上传Lua文件
    * @param [in] filePath 本地lua文件路径名
    * @return 错误码
    */
    errno_t LuaUpload(std::string filePath);

删除Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 删除Lua文件
    * @param [in] fileName 要删除的lua文件名，例如：“test.lua”
    * @return 错误码
    */
    errno_t LuaDelete(std::string fileName);

获取当前所有lua文件名称
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取当前所有lua文件名称
    * @param [out] luaNames lua文件名列表
    * @return 错误码
    */
    errno_t GetLuaList(std::list<std::string>* luaNames);

代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.2.0

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
        robot.SetLoggerLevel(3);
        robot.RPC("192.168.58.2");

        /* 获取lua名称 */
        list<std::string> luaNames;
        int res = robot.GetLuaList(&luaNames);
        std::cout << "res is: " << res << std::endl;
        std::cout << "size is: " << luaNames.size() <<std::endl;
        for(auto it = luaNames.begin(); it != luaNames.end(); it++)
        {
            std::cout << it->c_str() << std::endl;
        }

        /* 下载lua */
        res = robot.LuaDownLoad("test.lua", "D://Down/");
        std::cout << "res is: " << res << std::endl;

        /* 上传lua */
        res = robot.LuaUpload("D://Down/test.lua");
        std::cout << "res is: " << res << std::endl;

        /* 删除lua */
        res = robot.LuaDelete("test.lua");
        std::cout << "res is: " << res << std::endl;

        robot.CloseRPC();
        return 0;
    }
