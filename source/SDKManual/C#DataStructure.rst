数据结构说明
================

.. toctree:: 
    :maxdepth: 5

接口调用返回值类型
+++++++++++++++++++++++++++
.. code-block:: c
    :linenos:

    typedef  int errno_t;

关节位置数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 关节位置数据类型 
    */  
    struct JointPos
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jPos;   /* 六个关节位置，单位deg */
    }

笛卡尔空间位置数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 笛卡尔空间位置数据类型
    */
    struct DescTran
    {
        public double x;    /* x轴坐标，单位mm  */
        public double y;    /* y轴坐标，单位mm  */
        public double z;    /* z轴坐标，单位mm  */
    }

欧拉角姿态数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 欧拉角姿态数据类型
    */
    struct Rpy
    {
    public double rx;   /* 绕固定轴X旋转角度，单位：deg  */
    public double ry;   /* 绕固定轴Y旋转角度，单位：deg  */
    public double rz;   /* 绕固定轴Z旋转角度，单位：deg  */
    }

笛卡尔空间位姿数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    *@brief 笛卡尔空间位姿类型
    */
    struct DescPose
    {
        public DescTran tran;     /* 笛卡尔空间位置  */
        public Rpy rpy;			/* 笛卡尔空间姿态  */
    }

扩展轴位置数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 扩展轴位置数据类型
    */
    struct ExaxisPos
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public double[] ePos;   /* 四个扩展轴位置，单位mm */
    }

力矩传感器数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 力传感器的受力分量和力矩分量
    */
    struct ForceTorque
    {
        public double fx;  /* 沿x轴受力分量，单位N  */
        public double fy;  /* 沿y轴受力分量，单位N  */
        public double fz;  /* 沿z轴受力分量，单位N  */
        public double tx;  /* 绕x轴力矩分量，单位Nm */
        public double ty;  /* 绕y轴力矩分量，单位Nm */
        public double tz;  /* 绕z轴力矩分量，单位Nm */
    }

螺旋参数数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  螺旋参数数据类型
    */
    struct SpiralParam
    {
        public int circle_num;         	  /* 螺旋圈数  */
        public float circle_angle;         /* 螺旋倾角  */
        public float rad_init;             /* 螺旋初始半径，单位mm  */
        public float rad_add;              /* 半径增量  */
        public float rotaxis_add;          /* 转轴方向增量  */
        public uint rot_direction;         /* 旋转方向，0-顺时针，1-逆时针  */
    }
