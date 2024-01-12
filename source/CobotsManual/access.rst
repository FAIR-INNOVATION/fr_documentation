WebApp 访问登录
===================

.. toctree:: 
   :maxdepth: 6

访问登录WebApp界面
--------------------

1. 开启控制箱并将网线连接PC；
2. PC打开chrome浏览器访问目标网址192.168.58.2；
3. 输入用户名和密码点击登录即可登录WebApp。

初始用户名为admin，密码为123。

.. figure:: teaching_pendant_software/002.png
   :width: 6in
   :align: center

.. centered:: 图表 2.1‑1 登录界面

简单认识WebApp界面
--------------------

登录成功后系统进入“初始界面”，初始界面展示了示教器主要包含法奥LOGO及返回初始页面按钮、菜单栏、菜单栏缩放按钮、机器人操作区、控制区、状态区、三维模拟机器人以及位姿及IO信息区，一共八个区域。如下图系统初始界面示意图所示：

.. image:: teaching_pendant_software/003.png
   :align: center
   :width: 6in

.. centered:: 图表 2.2‑1 系统初始界面示意图

控制区
~~~~~~~~~

.. note:: 
   .. image:: teaching_pendant_software/004.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**使能按钮**
   
   作用：使能机器人

.. note:: 
   .. image:: teaching_pendant_software/005.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**开始按钮**
   
   作用：上传并开始运行示教程序

.. note:: 
   .. image:: teaching_pendant_software/006.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**停止按钮**
   
   作用：停止当前示教程序运行

.. note:: 
   .. image:: teaching_pendant_software/007.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名称：**暂停/恢复按钮**
   
   作用：暂停和恢复当前示教程序

.. important::
   暂停指令在程序的末尾，无法进行判断

状态栏
~~~~~~~~~~~~

.. note:: 
   .. image:: teaching_pendant_software/008.png
      :width: 2.25in
      :height: 0.75in
      :align: left

   名称：**机器人状态**
   
   作用：Stopped-停止，Running-运行，Pause-暂停，Drag-拖动

.. note:: 
   .. image:: teaching_pendant_software/009.png
      :width: 2.25in
      :height: 0.75in
      :align: left

   名称：**工具坐标系编号**
   
   作用：展示当前应用的工具坐标系编号
   
.. note:: 
   .. image:: teaching_pendant_software/010.png
      :width: 2.25in
      :height: 0.75in
      :align: left

   名称：**运行速度百分比**
   
   作用：机器人当前模式运行时速度

.. note:: 
   .. image:: teaching_pendant_software/011.png
      :width: 2.25in
      :height: 0.75in
      :align: left

   名称：**机器人运行正常状态**
   
   作用：当前机器人正常运行

.. note:: 
   .. image:: teaching_pendant_software/012.png
      :width: 2.25in
      :height: 0.75in
      :align: left

   名称：**机器人运行错误状态**
   
   作用：当前机器人运行有错误

.. note:: 
   .. image:: teaching_pendant_software/013.png
      :width: 2.25in
      :height: 0.75in
      :align: left

   名称：**自动模式**
   
   作用：机器人自动运行模式，开启手动切自动模式全局速度调整并指定速度时，全局速度会自动调整为指定速度

.. note:: 
   .. image:: teaching_pendant_software/014.png
      :width: 2.25in
      :height: 0.75in
      :align: left

   名称：**示教模式**
   
   作用：机器人示教运行模式

.. note:: 
   .. image:: teaching_pendant_software/015.png
      :width: 2.25in
      :height: 0.75in
      :align: left

   名称：**机器人拖动状态**
   
   作用：当前机器人可拖动

.. note:: 
   .. image:: teaching_pendant_software/016.png
      :width: 2.25in
      :height: 0.75in
      :align: left

   名称：**机器人拖动状态**
   
   作用：当前机器人不可拖动

.. note:: 
   .. image:: teaching_pendant_software/017.png
      :width: 2.25in
      :height: 0.75in
      :align: left

   名称：**连接状态**
   
   作用：机器人已连接

.. note:: 
   .. image:: teaching_pendant_software/001.png
      :width: 2.25in
      :height: 0.75in
      :align: left

   名称：**未连接状态**
   
   作用：机器人未连接

.. note:: 
   .. image:: teaching_pendant_software/018.png
      :width: 2.25in
      :height: 0.75in
      :align: left

   名称：**账户信息**
   
   作用：显示用户名和权限及登出用户
