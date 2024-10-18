程序编程
===============

.. toctree:: 
   :maxdepth: 6

简介
~~~~~~~

点击左侧命令可以向程序树添加程序节点。程序运行时，当前执行的程序节点绿色高亮显示。

在手动模式下，点击节点右侧第一个图标可以使机器人单独执行该指令，第二个图标为编辑该节点内容。

.. image:: coding/001.png
   :width: 6in
   :align: center

.. centered:: 图表 9.1-1 程序树界面

点击“⇄”切换模式，可以将示教程序文本变为编辑状态。

.. image:: coding/002.png
   :width: 6in
   :align: center

.. centered:: 图表 9.1‑2 示教程序编辑状态

程序名称右侧图标说明如下：

.. note:: 
   .. image:: coding/003.png
      :height: 0.75in
      :align: left

   名称：**展开/缩放**
   
   作用：展开/缩放程序树界面

.. note:: 
   .. image:: coding/004.png
      :height: 0.75in
      :align: left

   名称：**新增示教点**
   
   作用：新增当前程序的局部示教点

.. note:: 
   .. image:: coding/005.png
      :height: 0.75in
      :align: left

   名称：**重命名**
   
   作用：重新命名当前程序

工具栏
~~~~~~~~~~

使用程序树顶部的工具栏修改程序树。

.. note:: 
   .. image:: coding/006.png
      :height: 0.75in
      :align: left

   名称：**打开**
   
   作用：打开用户程序文件

.. note:: 
   .. image:: coding/007.png
      :height: 0.75in
      :align: left

   名称：**新建**
   
   作用：选择模板新建程序文件
   
.. note:: 
   .. image:: coding/008.png
      :height: 0.75in
      :align: left

   名称：**导入**
   
   作用：导入文件到用户程序文件夹中

.. note:: 
   .. image:: coding/009.png
      :height: 0.75in
      :align: left

   名称：**导出**
   
   作用：导出用户程序文件到本地点。

.. note:: 
   .. image:: coding/010.png
      :height: 0.75in
      :align: left

   名称：**保存**
   
   作用：保存文件编辑内容

.. note:: 
   .. image:: coding/011.png
      :height: 0.75in
      :align: left

   名称：**另存为**
   
   作用：给文件重命名存放到用户程序或模板程序文件夹中。

.. note:: 
   .. image:: coding/012.png
      :height: 0.75in
      :align: left

   名称：**复制**
   
   作用：复制一个节点，并允许将其用于其他操作（例如：将其粘贴到程序树的其他位置）。

.. note:: 
   .. image:: coding/013.png
      :height: 0.75in
      :align: left

   名称：**粘贴**
   
   作用：允许您粘贴之前剪切或复制的节点。

.. note:: 
   .. image:: coding/014.png
      :height: 0.75in
      :align: left

   名称：**剪切**
   
   作用：剪切一个节点，并允许将其用于其他操作（例如：将其粘贴到程序树的其他位置）。

.. note:: 
   .. image:: coding/015.png
      :height: 0.75in
      :align: left

   名称：**删除**
   
   作用：从程序树中删除一个节点。

.. note:: 
   .. image:: coding/016.png
      :height: 0.75in
      :align: left

   名称：**上移**
   
   作用：向上移动该节点。

.. note:: 
   .. image:: coding/017.png
      :height: 0.75in
      :align: left

   名称：**下移**
   
   作用：向下移动该节点。

.. note:: 
   .. image:: coding/018.png
      :height: 0.75in
      :align: left

   名称：**切换编辑模式**
   
   作用：程序树模式和lua编辑模式互相切换。

顶部右侧图标说明如下：

.. note:: 
   .. image:: coding/240.png
      :height: 0.75in
      :align: left

   名称：**程序编程添加/编辑**
   
   作用：添加/编辑当前程序命令的内容

.. note:: 
   .. image:: coding/241.png
      :height: 0.75in
      :align: left

   名称：**机器人模型**
   
   作用：返回机器人3D模型界面

.. note:: 
   .. image:: coding/242.png
      :height: 0.75in
      :align: left

   名称：**NewDofile子程序界面**
   
   作用：当前程序命令中存在NewDofile指令时，点击进入选择子程序名称查看子程序内容。

.. note:: 
   .. image:: coding/243.png
      :height: 0.75in
      :align: left

   名称：**Modbus TCP设置**
   
   作用：配置Modbus TCP通信的参数

.. note:: 
   .. image:: coding/244.png
      :height: 0.75in
      :align: left

   名称：**当前示教程序备份**
   
   作用：记录当前程序的修改内容

.. note:: 
   .. image:: coding/245.png
      :height: 0.75in
      :align: left

   名称：**局部示教点**
   
   作用：仅应用于当前程序的示教点

程序命令
~~~~~~~~~~~

左侧主要是程序命令的添加，点击各关键字上方图标进入右侧程序命令添加的详细界面。程序命令添加到文件中的操作主要分为两种：

- 1、打开相关指令点击应用按键即可将该指令添加到程序中；
- 2、先点击“添加”按键，此时命令并未保存到程序文件中，需要再点击“应用”方可将命令保存到文件中。

第二种方式多出现在同类型指令多条下发的情况，我们对该类型命令增加添加按键和显示已添加指令内容功能，点击添加按键可添加一条指令，已添加指令显示所有已添加的指令，点击“应用”即可将添加的指令保存到右侧已打开的文件中。

逻辑指令界面
~~~~~~~~~~~~~

.. image:: coding/019.png
   :width: 6in
   :align: center

.. centered:: 图表 9.4 逻辑指令界面

循环命令
++++++++++++++++

点击“循环”图标进入While命令编辑界面。

选择While命令的循环场景，场景如下：

- 始终循环
- 有限次数循环：输入循环次数和变量名称
- 表达式为真时循环：点击输入框弹出表达式编辑器，根据使用情形选择相应表达式

.. image:: coding/020.png
   :width: 6in
   :align: center

.. centered:: 图表 9.4-1-1 While指令界面

.. image:: coding/236.png
   :width: 6in
   :align: center

.. centered:: 图表 9.4-1-2 While指令——始终循环

.. image:: coding/237.png
   :width: 6in
   :align: center

.. centered:: 图表 9.4-1-3 While指令——有限次数循环

.. image:: coding/238.png
   :width: 6in
   :align: center

.. centered:: 图表 9.4-1-4 While指令——表达式编辑器

.. image:: coding/239.png
   :width: 6in
   :align: center

.. centered:: 图表 9.4-1-5 While指令——表达式为真时循环

为方便操作，可任意输入do内容，在程序中编辑其他指令插入代替。

判断命令
++++++++++++++++

点击“判断”按钮进入if…else命令编辑界面。

该命令包含以下按钮：

- 添加else if：当不存在“else”表达式时，点击该按钮添加“else if”表达式
- 移除else if：当存在“else if”表达式时，点击该按钮删除“else if”表达式
- 添加 else：点击该按钮添加“else”表达式
- 移除else：点击该按钮删除“else”表达式

点击对应按钮添加后，点击输入框弹出表达式编辑器，根据使用情形选择相应表达式。添加完毕后点击“添加”、“应用”即可。

该指令需要一定编程基础，如需帮助，请联系我们。

.. image:: coding/021.png
   :width: 6in
   :align: center

.. centered:: 图表 9.4-2 if…else指令界面

跳转命令
++++++++++++++++

点击“跳转”按钮进入Goto命令编辑界面。

Goto指令为跳转指令，在右侧输入框中输入语句，编辑完毕后点击“添加”、“应用”即可。（该指令需要一定编程基础，如需帮助，请联系我们）

.. image:: coding/022.png
   :width: 6in
   :align: center

.. centered:: 图表 9.4-3 Goto指令界面

等待命令
++++++++++++++++

点击“等待”图标进入Wait命令编辑界面。

该指令为延时指令，分为“WaitMs”、“WaitDI”和“WaitAI”三部分。

“WaitTime”指令延时等待时间单位为毫秒，输入需要等待的毫秒数，点击“添加”、“应用”即可。

.. image:: coding/023.png
   :width: 6in
   :align: center

.. centered:: 图表 9.4-4 WaitTime指令界面

“WaitDI”指令，即单DI等待，选择需要等待的IO端口号、等待状态、等待最大时间和等待超时处理方式，点击“添加”、“应用”即可。

.. image:: coding/024.png
   :width: 6in
   :align: center

.. centered:: 图表 9.4-5 WaitDI指令界面

“WaitMultiDI”指令，即多DI等待，首先选择多DI成立条件，其次勾选需要等待的DI端口和状态，最后设置等待最大时间和等待超时处理方式，点击“添加”、“应用”即可。

.. image:: coding/025.png
   :width: 6in
   :align: center

.. centered:: 图表 9.4-6 WaitMultiDI指令界面

“WaitAI”指令，选择需要等待的模拟量、数值、等待的最大时间以及等待超时处理方式，点击“添加”、“应用”即可。

.. image:: coding/026.png
   :width: 6in
   :align: center

.. centered:: 图表 9.4-7 WaitAI指令界面

暂停命令
++++++++++++++++

点击“暂停”图标进入Pause命令编辑界面。

该指令为暂停指令，在程序中插入该指令，当程序执行到该指令时，机器人会处于暂停状态，若想继续运行，点击控制区“暂停/恢复”按键即可。

.. image:: coding/027.png
   :width: 6in
   :align: center

.. centered:: 图表 9.4-8 Pause指令界面

子程序命令
++++++++++++++++

点击“子程序”图标进入Dofile命令编辑界面。

Dofile指令调用的是控制器内部程序，使用Dofile指令需要保存被调用的子程序，而主程序若未改变可不用再次保存。Dofile指令支持二级调用，需要注意两个参数设置，一是该调用处于第几层，二是该调用的ID编号，ID编号原则上同一程序不能出现相同ID。

.. image:: coding/028.png
   :width: 6in
   :align: center

.. centered:: 图表 9.4-9 Dofile指令界面

变量命令
++++++++++++++++

点击“变量”图标进入Var命令编辑界面。

该指令为变量系统指令，分为Lua变量定义，变量查询和Sys变量重命名，获取值，设置值两部分，Lua变量定义可以声明一个变量并赋予初始值，与while，if-else等指令配合使用，Lua变量查询指令可以实时查询输入的变量名称的值，显示在状态栏。Sys变量个数是固定的，可以对其重命名，获取变量值以及设置变量值，该变量保存的值不随系统关机而清零。

.. image:: coding/029.png
   :width: 6in
   :align: center

.. centered:: 图表 9.4-10 Var指令界面

.. important:: 变量命名必须以字母或者下划线开头，不能以数字或其他特殊字符开头。

运动指令界面
~~~~~~~~~~~~~

.. image:: coding/030.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5 运动指令界面

点到点命令
++++++++++++++++

点击“点到点”图标进入PTP命令编辑界面。

可以选择需要到达的点，平滑过渡时间设置可以实现该点到下一点的运动是连续的，是否偏移设置，可以选择基于基坐标系偏移和基于工具坐标偏移，并弹出x，y，z，rx，ry，rz偏移量设置，PTP具体路径为运动控制器自动规划的最优路径，点击“添加”、“应用”后可保存该条指令。

.. image:: coding/031.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-1 PTP指令界面

直线命令
++++++++++++++++

点击“直线”图标进入Lin命令编辑界面。

该指令功能与“PTP”指令相似，但该指令所到达点的路径为直线。

.. image:: coding/032.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-2 Lin指令界面

.. important:: 当选择点名称为“seamPos”时，直线命令应用于焊接场景中使用激光传感器。由于焊接使用中的运行累计误差，故增加“是否偏移”和“偏移量”。

   **是否偏移**：否、基坐标系偏移、工具坐标系偏移、激光原始数据偏移；

   **偏移量**：∆x、∆y、∆z、∆rx、∆ry、∆rz，范围：-300~300；

   .. image:: coding/033.png
      :width: 6in
      :align: center

   .. centered:: 图表 9.5-2-1 Lin指令界面（焊接场景）

LIN指令关节超速处理功能
***************************

使用笛卡尔空间直线运动指令LIN时，约束的规划条件是线速度，但是实际运行时受到工作空间的影响，在满足线速度要求时关节角速度可能已经超过限制。本功能实现了可选处理策略以应对LIN运动中关节超速的情况。

**Step1**：点击直线运动指令按钮；

.. image:: coding/034.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-3-1 点击直线运动指令按钮

**Step2**：选择直线运动指令目标路点；

.. image:: coding/035.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-3-2 选择直线运动目标路点

**Step3**：打开关节超速保护开关；

.. image:: coding/036.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-3-3 打开关节超速保护开关按钮

**Step4**：选择关节超速处理策略(选择超速报错或自适应降速，其他均为默认策略无保护)；

.. image:: coding/037.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-3-4 关节超速处理策略

**Step5**：
   设置处理策略及处理策略参数，点击添加按钮即可添加lua指令；

   自适应降速策略下，减速阈值为线速度减少值相对设定线速度的百分比，当减速值超过设定阈值时，机器人会报错停止。

.. image:: coding/038.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-3-5 关节超速处理策略选择与设置

**Step6**：添加的lua指令，形式如图所示；

.. image:: coding/039.png
   :width: 4in
   :align: center

.. centered:: 图表 9.5-3-6 lua指令

**超速保护开始**：JointOverSpeedProtectStart（a，b）；
   a：策略号（参照下拉框顺序）

   b：阈值百分比（0~100，仅自适应降速时起效）

**超速保护结束**：JointOverSpeedProtectEnd（）；

包角姿态过渡角速度可调功能
***************************

当焊接过程中遇到要求包角焊接的工件时，或在一段特定直线规划（姿态变化大且位置变化小，但要求线速度不能加快的情况下快速过渡）时，可以使用本功能完成。

**Step1**：设置工具坐标系，标定焊枪的工具尺寸与姿态。

.. warning:: 界面数值仅为示例，以实际工具状态为准。

.. image:: coding/246.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-3-7 设置工具坐标系

**Step2**：点击“示教程序”，选择“程序编程”，在“运动指令”分类中选择“直线”。

.. image:: coding/247.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-3-8 直线指令设置界面

**Step3**：设置包角焊接每段直线的起始点为过渡点，打开“过渡点角速度可调”按钮，设置最大加速度百分比（默认最大角速度100%为360°/s）。

.. image:: coding/248.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-3-9 过渡点角速度调整参数配置界面

**Step4**：点击“添加”按钮，生成包含过渡姿态角速度调整的直线指令。

.. image:: coding/249.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-3-10 添加过渡点直线运动指令

**Step5**：机器人在起点处完成姿态过渡，正常执行直线指令运动到该段终点，关闭“过渡点角速度可调”按钮，添加终止路点。

.. image:: coding/250.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-3-11 插入直线终点

**Step6**：点击“应用”按钮，生成对应LUA指令。

.. image:: coding/251.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-3-12 生成包含过渡点的直线LUA指令


一组完整的包角焊通常具有多个过渡点，在图7所示的包角的情况下，在焊接过程中有两个位置变化小且姿态变化大的姿态过渡点。

点1是焊接第一段的起点，点2是焊接第一段的终点；

点3是焊接第二段的起点，点4是焊接第二段的终点；

点5是焊接第三段的起点，点6是焊接第三段的终点。

姿态过渡发生在上一段焊接的终点到下一段焊接的起点，所以需要在下一段焊接的起点增加姿态角速度调整指令，这样在包角姿态过渡期间最大线速度保持不变、最大角速度增加，使包角焊接过程流畅运行。

.. image:: coding/252.png
   :width: 4in
   :align: center

.. centered:: 图表 9.5-3-13 包角焊接流程示例

圆弧命令
++++++++++++++++

点击“圆弧”图标进入Arc命令编辑界面。

“Arc”指令为圆弧运动，包含三个点，第一点为圆弧起始点，第二点为圆弧中间过渡点，第三点为终点。

过渡点和终点都可以对是否偏移进行设置，可以选择基于基坐标系偏移和基于工具坐标偏移，并弹出x，y，z，rx，ry，rz偏移量设置，终点可以设置平滑过渡半径，实现运动连续效果。

.. important::
   圆弧运动需要先添加PTP或者Lin指令先运动到起始点。

.. image:: coding/040.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-4 Arc指令界面

整圆命令
++++++++++++++++

点击“整圆”图标进入Circle命令编辑界面。

协作机器人通过添加整圆指令可以进行整圆轨迹运动，在添加整圆指令前需要先示教出整圆轨迹上的3个路径点，假设整圆轨迹上三个路径点分别为“P1”、“P2”、“P3”，其中“P1”为整圆轨迹起点，“P2”和“P3”分别为整圆轨迹中间点1和中间点2，分别移动机器人至上述三个点，并添加示教点位名称分别为“P1”、“P2”、“P3”。

.. important::
   整圆轨迹运动需要先添加PTP或者Lin指令先运动到起始点。

.. image:: coding/042.png
   :width: 3in
   :align: center

.. centered:: 图表 9.5-5 整圆轨迹

.. image:: coding/043.png
   :width: 3in
   :align: center

.. image:: coding/044.png
   :width: 3in
   :align: center

.. image:: coding/045.png
   :width: 3in
   :align: center

.. centered:: 图表 9.5-6 示教“P1”、“P2”、“P3”点

整圆指令添加
**************

**Step1**：新建用户程序“testCircle.lua”，点击“整圆”按钮，打开整圆指令添加页面。

.. image:: coding/046.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-7 添加整圆指令按钮

**Step2**：在整圆指令添加页面中选择起始点运动方式和起始点为“P1”。

.. image:: coding/050.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-8 起始点运动方式和起始点“P1”

**Step3**：在整圆指令添加页面中选择“整圆中间点1”为“P2”点。

.. image:: coding/047.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-9 整圆中间点1

**Step4**：选择“整圆中间点2”为“P3”点，依次点击“添加”按钮和“应用”按钮。

.. image:: coding/048.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-10 整圆中间点2

**Step5**：此时“testCircle.lua”已经增加整圆运动指令。

.. image:: coding/049.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-11 整圆运动指令添加

将机器人切换到自动模式，在确保安全的前提下启动该程序，机器人即按整圆轨迹进行运动。

整圆轨迹偏移
**************

协作机器人的整圆运动支持对整圆轨迹中间点1和整圆轨迹中间点2的位置进行偏移，偏移类型包括以下两种类型；

**整圆两个轨迹中间点相同偏移量**：整圆轨迹中间点1（“P2”点）和整圆轨迹中间点2（“P3”点）采用相同的偏移量∆(dx, dy, dz, drx, dry, drz)进行偏移。

**整圆两个轨迹中间点不同偏移量**：整圆轨迹中间点1（“P2”点）和整圆轨迹中间点2（“P3”点）分别采用两个不同的偏移量∆1(dx1, dy1, dz1, drx1, dry1, drz1)和∆2(dx2, dy2, dz2, drx2, dry2, drz2)进行偏移。

下面分别演示“相同偏移量”和“不同偏移量”的用法。

1. 相同偏移量

所示，打开整圆指令添加页面，“偏移类型”选择“相同偏移量”，同样选择起始点运动方式和起始点为“P1”，整圆中间点1为“P2”点。

.. image:: coding/051.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-12 整圆相同偏移量

整圆中间点2选择“P3”，“是否偏移”选择“基座标偏移”。

.. note:: 您可以根据实际的工作情况选择“工具坐标偏移”。

输入偏移量dx为10mm，依次点击页面下方的“添加”按钮和“应用”按钮。

.. image:: coding/052.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-13 设置偏移量

此时一条整圆起始点为“P1”，两个中间点“P2”和“P3”均沿基座标系的X轴方向偏移10mm的整圆指令已经添加到“testCircle.lua”程序中。

.. image:: coding/053.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-14 整圆相同偏移量程序

将机器人切换至自动模式，在保证安全的情况下启动该程序，机器人的实际运动轨迹中穿过“P1”、“P2”和“P3”的圆，其中“P2”为原“P2”点沿X方向偏移10mm后的点，其中“P3”为原“P3”点沿X方向偏移10mm后的点。

.. image:: coding/054.png
   :width: 3in
   :align: center

.. centered:: 图表 9.5-15 相同偏移量X10mm轨迹

2. 不同偏移量

打开整圆指令添加页面，“偏移类型”选择“不同偏移量”，同样选择起始点运动方式和起始点为“P1”，整圆中间点1为“P2”点，“是否偏移”选择为“基座标偏移”。

.. note:: 
   您可以根据实际的工作情况选择“工具坐标偏移”。

输入偏移量dy为10mm。

.. image:: coding/055.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-16 不同偏移量

整圆中间点选择“P3”，“是否偏移”选择“基座标偏移”。

.. note:: 您可以根据实际的工作情况选择“工具坐标偏移”。

输入偏移量dx为10mm，依次点击页面下方的“添加”按钮和“应用”按钮。

.. image:: coding/056.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-17 不同偏移量设置中间点2偏移

此时一条整圆起始点为“P1”，中间点“P2”沿基座标系Y方向偏移10mm和“P3”沿基座标系的X轴方向偏移10mm的整圆指令已经添加到“testCircle.lua”程序中。    

.. image:: coding/057.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-18 整圆两点不同偏移量程序

将机器人切换至自动模式，在保证安全的情况下启动该程序，机器人的实际运动轨迹中穿过“P1”、“P2’”和“P3’”的圆，其中“P2’”为原“P2”点沿Y方向偏移10mm后的点，其中“P3’”为原“P3”点沿X方向偏移10mm后的点。

.. image:: coding/058.png
   :width: 3in
   :align: center

.. centered:: 图表 9.5-19 整圆两轨迹点分别偏移轨迹

螺旋命令
++++++++++++++++

点击“螺旋”图标进入Spiral命令编辑界面。

“Spiral”指令为螺旋线运动，包含三个点，该三个点组成一个圆，在第三点设置页面，包含螺旋圈数，姿态修正角，半径增量和转轴方向增量这几个参数设置，螺旋圈数即该螺旋线的运动圈数，姿态修正角修正的是螺旋线结束时的姿态与螺旋线第一点的姿态，半径增量即每一圈半径的增量，转轴方向增量即螺旋轴方向的增量。设置
是否偏移，该偏移量生效于整个螺旋线的轨迹。

.. image:: coding/059.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-20 Spiral指令界面

新螺旋命令
++++++++++++++++

点击“新螺旋”图标进入N-Spiral命令令编辑界面

“N-Spiral”指令为优化版螺旋线运动，该指令只需要一个点加各参数的配置实现螺旋线运动。机器人以当前位置作为起点，用户设置调试速度，是否偏移，螺旋圈数，螺旋倾角，初始半径，半径增量，转轴方向增量和旋转方向这几个参数，螺旋圈数即该螺旋线的运动圈数，螺旋倾角即工具Z轴与水平方向的夹角，姿态修正角修正的是螺旋线结束时的姿态与螺旋线第一点的姿态，初始半径即第一圈半径大小，半径增量即每一圈半径的增量，转轴方向增量即螺旋轴方向的增量，旋转方向即顺时针和逆时针。

.. image:: coding/060.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-21 N-Spiral指令界面

水平螺旋命令
++++++++++++++++

点击“水平螺旋”图标进入H-Spiral命令令编辑界面

“H-Spiral”指令为水平空间螺旋线运动，该指令设置于单段运动（直线）指令之后。

   - 螺旋半径: 0~100mm
   - 螺旋角速度: 0~2rev/s
   - 旋转方向: 螺旋顺/逆时针
   - 螺旋倾角: 0~40°

.. image:: coding/061.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-22 H-Spiral指令界面

样条命令
++++++++++++++++

点击“样条”图标进入Spline命令编辑界面。

该指令分为样条组起始，样条段和样条组结束三部分，样条组开始是样条运动的起始标志，样条段包含SPL、SLIN和SCIRC段，点击对应图标进入指令添加界面，样条组结束是样条运动的结束标志。

.. image:: coding/062.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-23 Spline指令界面

新样条命令
++++++++++++++++

点击“新样条”图标进入N-Spline命令编辑界面。

该指令为Spline指令算法优化指令，后续会替代现有的Spline指令。

该指令分为多点轨迹起始，多点轨迹段和多点轨迹结束三部分，多点轨迹开始是多点轨迹运动的起始标志，多点轨迹段即设置各个轨迹点。

点击图标进入点位添加界面，多点轨迹结束是多点轨迹运动的结束标志，在此可以设置控制模式和调试速度。

- 控制模式：圆弧过渡点/给定路径点
- 全局平均衔接时间：整数型，大于10，默认值为2000

.. image:: coding/063.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-24 N-Spline指令界面

摆动命令
++++++++++++++++

点击“摆动”图标进入Weave命令编辑界面。“Weave”指令包含两部分：

- 选择配置好参数的摆焊编号，点击“开始摆焊”和“停止摆焊”并应用可将相关指令添加到程序中。

.. image:: coding/064.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-25 Weave指令界面

- 点击“配置与测试”，可以根据使用场景选择摆动类型，对摆焊的参数进行配置，配置完成后可通过开始摆焊测试和停止摆焊测试按键测试该摆焊轨迹。目前摆动类型有：

   - 三角波摆动（LIN/ARC）
   - 垂直L型三角波摆动（LIN/ARC）
   - 圆形摆动-顺时针（LIN）
   - 圆形摆动-逆时针（LIN）
   - 正弦波摆动（LIN/ARC）
   - 垂直L型正弦波摆动（LIN/ARC）
   - 立焊三角摆动

.. image:: coding/065.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-26 Weave配置与测试指令界面

斜锯齿摆动功能
*********************

使用斜锯齿摆动功能能使机器人工具末端在笛卡尔空间内形成倾斜锯齿状摆动轨迹。斜锯齿摆动叠加于直线规划，倾斜量受方位角参数控制，在指定的摆焊平面上摆焊的方位角的倾斜度（单位deg）；

值为正时，左端点向前进方向倾斜，为负时，右端点向前进方向倾斜；若为90deg或-90deg时，可以沿着前进方向进行摆动。

.. image:: coding/066.png
   :width: 4in
   :align: center

.. centered:: 图表 9.5-26-1 摆动方位角影响

**Step1**：编辑设置基本直线运动。

.. image:: coding/067.png
   :width: 4in
   :align: center

.. centered:: 图表 9.5-26-2 基本直线运动lua程序示例

**Step2**：点击添加摆动指令。

.. image:: coding/068.png
   :width: 1.5in
   :align: center

.. centered:: 图表 9.5-26-3 点击添加摆动指令

**Step3**：摆动指令参数配置页面点击“配置”按钮，“摆动类型”下拉框选择“三角波摆动”或“正弦波摆动”，输入相应“摆动方向方位角”，点击“应用”。

.. image:: coding/069.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-26-4 摆动参数配置

**Step4**：点击“开始摆动”按钮，将摆动指令添加到直线运动上方；点击“结束摆动”按钮，将摆动指令添加到直线运动下方。

.. image:: coding/070.png
   :width: 4in
   :align: center

.. centered:: 图表 9.5-26-5 添加摆动指令后lua程序

**Step5**：点击“开始运行”，机器人末端轨迹如图所示。

.. image:: coding/071.png
   :width: 3in
   :align: center

.. image:: coding/072.png
   :width: 3in
   :align: center

.. centered:: 图表 9.5-26-6 锯齿摆动（左） 斜锯齿摆动（右）

轨迹复现命令
++++++++++++++++

点击“轨迹复现”按钮进入TPD命令编辑界面。

在该指令中，用户首先需要有记录好的轨迹。

关于轨迹记录：在准备记录轨迹之前，先保存下轨迹的起始点。在机器人处于拖动模式下，输入文件名，选择周期（假设数值为x，即每隔x毫秒记录一个点，推荐4毫秒记录一个点），点开始记录，用户可以根据需求拖动机器人进行指定运动，记录完成后，点击停止记录，即可保存之前机器人的运动轨迹。当一条运动无法完全记录，会提
示记录点数超限提示，用户需要将运动分几次进行记录。

进行程序编程时，首先用PTP指令到达对应轨迹起始点，然后在TPD轨迹复现指令中选择轨迹，选择是否平滑，设置调试速度，依次点击“添加”、“应用”，即可插入程序。轨迹加载指令主要用于预先读取轨迹文件，提取成轨迹指令，更好的应用于传送带跟踪场景。

.. note:: 
   关于TPD详细操作可见示教编程（TPD）功能操作说明模块。

.. image:: coding/073.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-27 TPD指令界面

点偏移命令
++++++++++++++++

点击“点偏移”图标进入Offset命令编辑界面。

该指令为整体偏移指令，输入各个偏移量，将开启指令和关闭指令添加到程序中，在开始和关闭中间的运动指令会基于基坐标（或工件坐标）进行偏移。

.. image:: coding/074.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-28 Offset指令界面

伺服命令
++++++++++++++++

点击“伺服”图标进入ServoCart命令编辑界面。

ServoCart伺服控制（笛卡尔空间运动）指令，该指令可以通过绝对位姿控制或基于当前位姿偏移来控制机器人运动。

.. image:: coding/075.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-29 ServoCart指令界面

绝对位姿控制程序实例：

.. image:: coding/076.png
   :width: 6in
   :align: center

此例中，x，y，z，rx，ry，rz（笛卡尔位置）是获取的机器人当前位置，此外，用户可以通过读取轨迹数据文件，socket通讯发送轨迹数据等方式，控制机器人运动。

基于当前位姿偏移（基坐标偏移）控制程序实例：

.. image:: coding/077.png
   :width: 6in
   :align: center

轨迹命令
++++++++++++++++

点击“轨迹”图标进入Trajctory命令编辑界面。

.. image:: coding/078.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-30 Trajctory指令界面

轨迹J命令
++++++++++++++++

点击“轨迹J”图标进入TrajctoryJ命令编辑界面。

Trajctory指令和TrajctoryJ指令适用于相机直接给定轨迹的通用接口，满足在已有固定格式的离散的轨迹点文件时，可导入系统使得机器人按照导入文件的轨迹进行运动。

1. 轨迹文件导入功能：选择本地计算机文件导入机器人控制系统。

2. 轨迹预加载：选择已导入的轨迹文件通过指令加载。

3. 轨迹运动：通过预加载的轨迹文件和选择的调试速度组合指令下发机器人运动。

4. 打印轨迹点编号：在机器人运行轨迹的过程中打印轨迹点编号，以便查看当前运动的进度。

.. image:: coding/079.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-31 TrajctoryJ指令界面

DMP命令
++++++++++++++++

点击“DMP”图标进入DMP命令编辑界面。

DMP是一种轨迹模仿学习的方法，需要事先规划参考轨迹。在命令编辑界面。 ，选择示教点作为新的起点，点击“添加”、“应用”后可保存该指令。DMP具体路径为以新的起点模仿参考轨迹的新轨迹。

.. image:: coding/080.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-32 DMP指令界面

工件转换命令
++++++++++++++++

点击“工件转换”图标进入WPTrsf命令编辑界面。

选择所要进行自动转换的工件坐标系，点击“添加”、“应用”后可保存该指令，该指令实现在执行内部的PTP、LIN指令时，工件坐标系下点位自动转换。使用示例区域展示并提示了指令的正确使用方式组合，具体指令在添加后可依据实际场景自行调整组合。

.. image:: coding/081.png
   :width: 6in
   :align: center

.. centered:: 图表 9.5-33 WPTrsf指令界面

控制指令界面
~~~~~~~~~~~~~

.. image:: coding/082.png
   :width: 6in
   :align: center

.. centered:: 图表 9.6 控制指令界面

数字IO命令
++++++++++++++++

点击“数字IO”图标进入IO命令编辑界面。

“IO”指令分为设置IO（SetDO/SPLCSetDO）和获取IO（GetDI/SPLCGetDI）两部分。

“SetDO/SPLCSetDO”该指令可设定指定的输出DO状态，包括16路控制箱数字输出和2路工具数字输出，状态选项“False”为闭，“True”为开，是否阻塞选项选择“阻塞”表示运动停止后设置DO状态，选择“非阻塞”选项表示在上一条运动过程中设置DO状态。平滑轨迹选项选择“Break”表示在平滑过渡半径结束后设置DO状态，选择“Serious”表示在平滑过渡半径运动过程中设置DO状态。当该指令是添加在辅助线程中，是否应用线程需要选择是，其他地方使用该指令选择否。点击“添加”、“应用”即可。

.. image:: coding/083.png
   :width: 6in
   :align: center

.. centered:: 图表 9.6-1 SetDO指令界面

在“GetDI/SPLCGetDI”指令中，选择想要获取端口号的数值，是否阻塞选项选择“阻塞”表示运动停止后获取DI状态，选择“非阻塞”选项表示在上一条运动过程中获取DI状态。当该指令是添加在辅助线程中，是否应用线程需要选择是，其他地方使用该指令选择否。选择完毕后点击“添加”、“应用”按钮即可。

.. image:: coding/084.png
   :width: 6in
   :align: center

.. centered:: 图表 9.6-2 GetDI指令界面

模拟AI命令
++++++++++++++++

点击“模拟AI”图标进入AI命令编辑界面。

在该指令中，分为设置模拟输出（SetAO/SPLCSetAO）和获取模拟输入（GetAI/SPLCGetAI）两部分功能。

“SetAO/SPLCSetAO”选择需要设置的模拟输出，输入需要设置的值，范围为0-10，是否阻塞选项选择“阻塞”表示运动停止后设置AO状态，选择“非阻塞”选项表示在上一条运动过程中设置AO状态。当该指令是添加在辅助线程中，是否应用线程需要选择是，其他地方使用该指令选择否。点击“添加”、“应用”即可。

.. image:: coding/085.png
   :width: 6in
   :align: center

.. centered:: 图表 9.6-3 SetAO指令界面

“GetAI/SPLCGetAI”选择需要获取的模拟输入，是否阻塞选项选择“阻塞”表示运动停止后获取AI状态，选择“非阻塞”选项表示在上一条运动过程中获取AI状态。当该指令是添加在辅助线程中，是否应用线程需要选择是，其他地方使用该指令选择否。点击“添加”、“应用”即可。

.. image:: coding/086.png
   :width: 6in
   :align: center

.. centered:: 图表 9.6-4 GetAI指令界面

虚拟IO命令
++++++++++++++++

点击“虚拟IO”图标进入Vir-IO命令编辑界面。

该指令虚拟的IO控制指令，可以实现设置模拟外部DI和AI状态，获取模拟DI和AI状态。

.. image:: coding/087.png
   :width: 6in
   :align: center

.. centered:: 图表 9.6-5 Vir-IO指令界面

扩展IO命令
++++++++++++++++

点击“扩展IO”图标进入Aux-IO命令编辑界面。

Aux-IO是机器人与PLC通讯控制外部扩展IO的指令功能，需要机器人与PLC建立UDP通讯，在原有的16路输入输出基础上，可以扩展128路输入输出，该指令用法与前文所讲的通用IO用法类似。使用此功能，有一定技术难度，前请联系我们咨询。

.. image:: coding/088.png
   :width: 6in
   :align: center

.. centered:: 图表 9.6-6 Aux-IO指令界面

运动DO命令
++++++++++++++++

点击“运动DO”图标进入MoveDO命令编辑界面。

该指令分为连续输出模式和单次输出模式。

- 连续输出模式：实现直线运动过程中，根据设定的间隔，连续输出DO信号功能。

.. image:: coding/089.png
   :width: 6in
   :align: center

.. centered:: 图表 9.6-7 MoveDO指令连续输出界面

- 单次输出模式：可进行匀速段输出和自由配置两种选择。运动开始后输出置位时间，运动结束前输出复位时间，范围[0, 1000]。

.. image:: coding/090.png
   :width: 6in
   :align: center

.. centered:: 图表 9.6-8 MoveDO指令单次输出界面

运动AO命令
++++++++++++++++

点击“运动AO”图标进入MoveAO命令编辑界面。

1. 概述

该指令配合运动指令使用时，可实现在运动过程中，根据实时TCP速度按比例输出AO信号。

2. 运动AO指令说明

运动AO指令位于示教模拟-程序示教指令编辑区域中，图标为控制指令-运动AO。

.. image:: coding/091.png
   :width: 6in
   :align: center

.. centered:: 图表 9.6-9 运动AO指令

.. image:: coding/092.png
   :width: 6in
   :align: center

.. centered:: 图表 9.6-10 运动AO指令明细

- AO编号：下拉列表选择，Ctrl-AO0对应控制箱AO0，Ctrl-AO1对应控制箱AO1，End-AO0对应末端AO0。
  
- 最大TCP速度：机器人最大TCP速度值；作用：与实时TCP速度形成比例。
  
- 最大TCP速度AO百分比：机器人最大TCP速度值对应的AO百分比；作用：设置AO输出的上限值。
  
- 死区补偿值AO百分比：当比例阀存在死区时，可设置该参数以保证AO输出；作用：设置AO输出的下限值。

.. important:: 
   计算公式：输出AO百分比=实时TCP速度/设置最大TCP速度*设置最大TCP速度AO百分比。

   该指令配套的运动指令如下：PTP/LIN/ARC/CIRCLE/SPLINE/NSPLINE/SERVOJ。

坐标系命令
++++++++++++++++

点击“坐标系”图标进入ToolList命令编辑界面。

选择工具坐标系名称，点击“应用”添加该指令到程序中，当程序运行该语句，会设定机器人的工具坐标系。

.. image:: coding/093.png
   :width: 6in
   :align: center

.. centered:: 图表 9.6-11 ToolList指令界面

模式切换命令
++++++++++++++++

点击“模式切换”图标进入Mode命令编辑界面。

该指令可切换机器人到手动模式，通常在一个程序结尾处添加，以便用户在程序运行结束后，使机器人自动切换到手动模式，拖动机器人。

.. image:: coding/094.png
   :width: 6in
   :align: center

.. centered:: 图表 9.6-12 Mode指令界面

碰撞等级命令
++++++++++++++++

点击“碰撞等级”图标进入Collision命令编辑界面。

该指令碰撞等级设置，通过该指令可以在程序运行中实时调节各轴碰撞等级，更灵活的部署应用场景。

.. image:: coding/095.png
   :width: 6in
   :align: center

.. centered:: 图表 9.6-13 Collision指令界面

加速度命令
++++++++++++++++

点击“加速度”图标进入Acc命令编辑界面。

Acc指令是实现机器人加速度可单独设置功能，通过调节运动指令加速度缩放因子，可以增加或减小加减速时间，实现机器人动作节拍时间可调。

.. image:: coding/096.png
   :width: 6in
   :align: center

.. centered:: 图表 9.6-14 Acc指令界面

外设指令界面 
~~~~~~~~~~~~~

.. image:: coding/097.png
   :width: 6in
   :align: center

.. centered:: 图表 9.7 外设指令界面  

夹爪命令
++++++++++++++++

点击“夹爪”图标进入Gripper命令编辑界面。

在该指令中，分为夹爪运动控制指令和夹爪激活/复位指令，夹爪控制指令中，显示完成配置并且已被激活的夹爪编号，用户可以通过编辑框编辑，或者滑动条滑动至所需的值来完成对夹爪开闭、开闭速度和开闭力矩的设置，数值为百分比，是否阻塞功能选项，选择阻塞即夹爪运动需等待上一条运动指令执行完才执行，选择非阻塞即夹爪运动与上一条运动指令并行。点击“添加”、“应用”按钮，即可将设置的值保存至示教文件中。夹爪复位/激活指令，显示已经配置的夹爪编号，可以添加复位/激活指令到程序中。

.. image:: coding/098.png
   :width: 6in
   :align: center

.. centered:: 图表 9.7-1 Gripper指令界面

喷枪命令
++++++++++++++++

点击“喷枪”图标进入Spray命令编辑界面。

该指令为喷涂相关指令，控制喷枪“开始喷涂”、“停止喷涂”、“开始清枪”和“停止轻枪”。在编辑该程序命令时，需确认已经配置好喷枪外设，详见机器人外设章节。

.. image:: coding/099.png
   :width: 6in
   :align: center

.. centered:: 图表 9.7-2 Spray指令界面

外部轴命令
++++++++++++++++

点击“外部轴”图标进入EAxis命令编辑界面。，选择组合模式：

- 控制器+伺服驱动器(485)
- 控制器+PLC(UDP)

选择控制器+PLC(UDP)，该指令针对使用外部轴的场景，与PTP指令组合使用，可将空间上一点X轴方向上的移动分解到外部轴运动。选择外部轴编号，运动方式选同步，选择需要到达的点，点击“添加”、“应用”后可保存该条指令。

.. image:: coding/100.png
   :width: 6in
   :align: center

.. centered:: 图表 9.7-3 EAxis指令界面

选择控制器+伺服驱动器(485)，该指令可对扩展轴参数进行配置。根据不同的控制模式设置不同的参数。已配置好的扩展轴，可对其零点设定。

.. image:: coding/101.png
   :width: 6in
   :align: center

.. centered:: 图表 9.7-4 扩展轴指令界面

传送带命令
++++++++++++++++

点击“传送带”图标进入Convey命令编辑界面。

该指令包含位置实时检测，IO实时检测，跟踪开启和跟踪关闭四条命令。详见机器人外设章节。

.. image:: coding/102.png
   :width: 6in
   :align: center

.. centered:: 图表 9.7-5 Conveyor指令界面

打磨设备命令
++++++++++++++++

点击“打磨设备”图标进入Polish命令编辑界面。

该指令可设置打磨设备的转速、接触力、伸出距离和控制模式。

.. image:: coding/103.png
   :width: 6in
   :align: center

.. centered:: 图表 9.7-6 Polish命令界面

焊接指令界面
~~~~~~~~~~~~~

.. image:: coding/104.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8 焊接指令界面  

焊接命令
++++++++++++++++

点击“焊接”图标进入Weld命令编辑界面。

该指令主要用于焊机外设，在添加该指令前请确认在用户外设中焊机配置是否完成，详见机器人外设章节。

- 焊接电压范围： 0~700V 
- 焊接电流范围： 0~1000A

.. important:: 配置输出AO、焊接电流、焊接电压时，需要选择I/O类型。若选择控制器I/O，则需选择对应得输出AO。

.. image:: coding/105.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-1 Weld指令界面

段焊命令
++++++++++++++++

点击“段焊”图标进入Segment命令编辑界面。

协作机器人通过添加段焊指令可以进行段焊操作，在添加段焊指令前需要先选择段焊模式，并示教起始点和终点。段焊模式分为不变化姿态和变化姿态，机器人根据所选段焊模式，来考虑焊接轨迹过程中是否变化姿态。

示教起始点位“segment01”和终点“segment02”，确认焊接轨迹起始点和终点位置，如下图。

.. image:: coding/106.png
   :width: 3in
   :align: center

.. centered:: 图表 9.8-2-1 起始点位“segment01”

.. image:: coding/107.png
   :width: 3in
   :align: center

.. centered:: 图表 9.8-2-2 终点“segment02”

段焊指令添加
**************

**Step1**：新建用户程序“testSegment1.lua”，点击“段焊”按钮，打开段焊指令添加页面。

.. image:: coding/108.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-2-3 添加段焊指令按钮

**Step2**：在段焊指令添加页面中选择“起始点”为“segment01”，选择“终点”为“segment02”。

.. image:: coding/109.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-2-4 段焊起始点、终点

**Step3**：配置调试速度、执行长度、非执行长度、功能模式、摆动选择和取整规则，依次点击“添加”按钮和“应用”按钮。

**Step4**：此时“testSegment1.lua”已经增加段焊运动指令。

.. image:: coding/110.png
   :width: 4in
   :align: center

.. centered:: 图表 9.8-2-5 段焊运动指令添加

段焊运动轨迹姿态变化
**********************

协作机器人的段焊运动可选择段焊模式，模式类型包括以下两种类型；

**不变化姿态**：机器人在焊接轨迹过程中始终保持焊接轨迹起始点姿态运行。

**变化姿态**：机器人在焊接轨迹过程中，计算每一段轨迹的笛卡尔位姿和关节位置，在段焊运行过程中变化姿态。

下面分别演示“不变化姿态”和“变化姿态”的用法。

1. 不变化姿态
   
打开段焊指令添加页面，“段焊模式”选择“不变化姿态”，同样选择起始点”为“segment01”，“终点”为“segment02”，执行长度设置100，非执行长度设置成50，并选择其他相关配置后保存程序。

.. image:: coding/111.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-2-6 不变化姿态段焊模式

2. 变化姿态
   
打开段焊指令添加页面，“段焊模式”选择“变化姿态”，同样选择起始点”为“segment01”，“终点”为“segment02”，执行长度设置100，非执行长度设置成50，并选择其他相关配置后保存程序。

.. image:: coding/112.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-2-7 变化姿态段焊模式

3. 段焊运行类型

运行程序，机器人段焊运行情况分为如下几种：

1) 若功能模式选择第一段执行功能，摆动选择执行段摆动，取整规则不取整。则机器人100mm执行摆动运动，50mm执行直线运动交替进行，到终点时停止；

.. image:: coding/113.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-2-8 第一段执行摆动功能不取整

2) 若功能模式选择第一段不执行功能，摆动选择不执行段摆动，取整规则不取整。则机器人50mm执行摆动运动，100mm执行直线运动交替进行，到终点时停止；

.. image:: coding/114.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-2-9 第一段不执行摆动功能不取整

3) 若功能模式选择第一段执行功能，摆动选择执行段摆动，取整规则取整。则机器人100mm执行摆动运动，50mm执行直线运动交替进行，最后一段整体循环结束后，如果剩余距离小于150mm，则停止摆动；

.. image:: coding/115.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-2-10 第一段执行摆动功能循环取整

4) 若功能模式选择第一段执行功能，摆动选择不执行段摆动，取整规则取整。则机器人50mm执行摆动运动，100mm执行直线运动交替进行，最后一段整体循环结束后，如果剩余距离小于150mm，则停止摆动；

.. image:: coding/116.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-2-11 第一段不执行摆动功能循环取整

5) 若功能模式选择第一段执行功能，摆动选择执行段摆动，取整规则单段取整。则机器人100mm执行摆动运动，50mm执行直线运动交替进行，最后一段循环结束后，如果下一段是100mm执行摆动规划且剩余距离小于100mm，则停止摆动；如果下一段是50mm执行直线运动规划且剩余距离小于50mm，则运动停止；

.. image:: coding/117.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-2-12 第一段执行摆动功能单段取整

6) 若功能模式选择第一段执行功能，摆动选择不执行段摆动，取整规则单段取整。则机器人50mm执行摆动运动，100mm执行直线运动交替进行，最后一段循环结束后，如果下一段是50mm执行摆动规划且剩余距离小于50mm，则停止摆动；如果下一段是100mm执行直线运动规划且剩余距离小于100mm，则运动停止。

.. image:: coding/118.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-2-13 第一段不执行摆动功能单段取整

4. 姿态对比
   
配置不同段焊模式时，机器人焊接轨迹运行中的姿态也会不同，运行过程中姿态对比如下：

.. image:: coding/119.png
   :width: 3in
   :align: center

.. centered:: 图表 9.8-2-14 焊接轨迹初始姿态

.. image:: coding/120.png
   :width: 3in
   :align: center

.. centered:: 图表 9.8-2-15 运行过程中不变化姿态

.. image:: coding/121.png
   :width: 3in
   :align: center

.. centered:: 图表 9.8-2-16 运行过程中变化姿态

段焊实际场景
**************
在实际测试环境中，机器人需要安装焊枪等配置，根据创建的段焊指令，在焊接板上进行焊接操作，实际场景图如下：

.. image:: coding/122.png
   :width: 3in
   :align: center

.. centered:: 图表 9.8-2-17 段焊实际场景

激光跟踪命令
++++++++++++++++

点击“激光跟踪”图标进入Laser命令编辑界面。

该指令包含激光命令、跟踪命令和寻位命令三部分，在添加该指令前，请确认用户外设中激光跟踪传感器是否已经配置成功。详见机器人外设章节。

传感器加载模块中，根据功能选择显示相应“传感器命令”界面后，进行传感器命令配置：

**睿牛/创想**：输入焊缝类型，范围：0~49整数

.. image:: coding/123.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-3-1 Laser指令界面(焊缝类型)

**全视**：输入任务号，范围：0~255整数

.. image:: coding/124.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-3-2 Laser指令界面(任务号)

激光记录命令
++++++++++++++++

点击“激光记录”图标进入LT-Rec命令编辑界面。

该指令实现激光跟踪记录起点、终点取出功能，使机器人可以自动运动到起点位置，适用于从工件外部开始运动并进行激光跟踪记录的场合，同时上位机可获取记录数据中起点、终点的信息，用于后续运动。

实现激光跟踪复现速度可调功能，使机器人可以用一个很快的速度进行记录，然后按照正常焊接速度进行复现，可以提高作业效率。

.. image:: coding/125.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-4 LT-Rec指令界面

焊丝寻位命令
++++++++++++++++

点击“焊丝寻位”图标进入W-Search命令编辑界面。

该指令为焊丝寻位指令，包含寻位开始，寻位结束和计算偏移量三个指令，该指令一般应用于焊接场景中，需要焊机与机器人IO和运动指令相结合使用。

.. image:: coding/126.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-5 W-Search指令界面

在编写程序中，通常先设置寻位开始指令，之后添加两条LIN指令，确定寻位的方向，寻位成功后，获取计算出来的偏移量，将该偏移量通过整体偏移指令，生效到真正的焊接运动指令中，程序示例如下。

.. image:: coding/127.png
   :width: 4in
   :align: center

.. centered:: 图表 9.8-5-1 W-Search示例（1D）

电弧跟踪命令
++++++++++++++++

点击“电弧跟踪”图标进入Weld-Trc命令编辑界面。

该指令实现机器人焊缝跟踪利用焊缝的偏差检测进行补偿轨迹，可以使用电弧传感器来检测焊缝偏差。

**Step1**：上下补偿基准电流设定方式：反馈，设置上下基准电流开始计数和上下基准电流计数

.. image:: coding/128.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-6-1 Weld-Trc指令界面-反馈

**Step2**：上下补偿基准电流设定方式：常数，设置上下基准电流

.. image:: coding/129.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-6-2 Weld-Trc指令界面-常数

**Step3**：左右补偿参数交互页面

.. image:: coding/130.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-6-3 Weld-Trc指令界面-左右补偿参数

电弧跟踪功能操作
++++++++++++++++

焊机当前已测试可适配焊机型号型号与设定
****************************************

.. centered:: 表格 9.8-1 当前已测试可适配焊机型号

.. list-table::
   :widths: 70
   :header-rows: 0
   :align: center

   * - **当前已测试可适配焊机型号**

   * - 麦格米特ArtsenII CM350焊机
  
.. centered:: 表格 9.8-2 焊机功能设定

.. list-table::
   :widths: 100 100
   :header-rows: 0
   :align: center

   * - **功能号**
     - **设定参数**

   * - F18
     - 20

   * - F19
     - 56

PLC型号与设定
************************
.. centered:: 表格 9.8-3 PLC型号与设定

.. list-table::
   :widths: 70
   :header-rows: 0
   :align: center

   * - **当前已测试可适配PLC型号**

   * - 汇川Easy521
  
.. centered:: 表格 9.8-4 PLC关键设定

.. list-table::
   :widths: 70 70
   :header-rows: 0
   :align: center

   * - **设定项**
     - **设定内容**

   * - 通信协议
     - CANOPEN

   * - 反馈电流采样源
     - 焊机CANOPEN反馈数据

   * - 同步周期
     - 2ms

:download:`附件：PLC程序 <../_static/_doc/麦格米特焊机plc.zip>`

电弧跟踪功能
*********************

**1）设定电流电压与功能跟踪性能关系简介**

设定焊接电流电压与反馈焊接电流信号，如下图:

.. image:: coding/131.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-7-1  短路过渡->半射流过渡->射流过渡

.. note:: 电流与电压设定值越高，反馈焊接电流的毛刺幅值越小，焊接过程更稳定，焊缝跟踪更准确。

**2）功能界面参数简介**

.. centered:: 表格 9.8-5 电弧跟踪上下补偿模块

.. list-table::
   :widths: 70 70 70
   :header-rows: 0
   :align: center

   * - **参数名称**
     - **含义**
     - **参数说明**

   * - 电弧跟踪滞后时间
     - 反馈电流滞后的时间
     - 默认0ms，请勿调整

   * - 上下偏差补偿
     - 上下补偿开关
     - 可选择“开启”或“关闭”

   * - 上下调节系数
     - 电流与补偿距离的关系系数（调节灵敏度）
     - 焊接趋于短路过渡状态，电流信噪比逐渐变低，建议调低灵敏度

   * - 上下开始补偿时间
     - 最快开始上下补偿的周期
     - 与摆动频率相关，起弧后3~4s电流趋于稳定时开启较好。若摆动频率为1Hz，参数可为4；若频率2Hz，参数可为8，以此类推

   * - 上下每次最大补偿量
     - 每个上下补偿周期的最大补偿量
     - 根据焊接场景设定，摆动频率越快补偿量越小

   * - 上下总计最大补偿量
     - 单次完整焊接过程最大累积补偿量
     - 根据焊接场景设定，焊缝偏差越大设定相应越大

   * - 上下坐标系选择
     - 补偿值所补偿在的坐标系
     - 若存在焊接摆动可选“摆动”，否则选择“工具”或“机座”

   * - 上下基准电流设定方式
     - 基准电流获得方式选择
     - 可选择“反馈”通过读取反馈电流获得；或“常数”通过直接填写电流值获得

   * - 上下基准电流采样开始计数
     - 延迟开始采集基准电流的周期数
     - 与摆动频率相关，起弧后3~4s电流趋于稳定时开启较好。若摆动频率为1Hz，参数可为4；若频率2Hz，参数可为8，以此类推

   * - 上下基准电流采样计数
     - 基准电流反馈模式，采集基准电流的统计周期
     - 默认1cyc

   * - 上下基准电流
     - 基准电流常数模式，基准电流数值
     - 可手动填写以达到预期的补偿高度

.. centered:: 表格 9.8-6 电弧跟踪左右补偿模块

.. list-table::
   :widths: 70 70 70
   :header-rows: 0
   :align: center

   * - **参数名称**
     - **含义**
     - **参数说明**

   * - 电弧跟踪滞后时间
     - 反馈电流滞后的时间
     - 默认0ms，请勿调整

   * - 左右偏差补偿
     - 左右补偿开关
     - 可选择“开启”或“关闭”

   * - 左右调节系数
     - 电流与补偿距离的关系系数（调节灵敏度）
     - 焊接趋于短路过渡状态，电流信噪比逐渐变低，建议调低灵敏度

   * - 左右开始补偿时间
     - 最快开始左右补偿的周期
     - 与摆动频率相关，起弧后3~4s电流趋于稳定时开启较好。若摆动频率为1Hz，参数可为4；若频率2Hz，参数可为8，以此类推

   * - 左右每次最大补偿量
     - 每个左右补偿周期的最大补偿量
     - 根据焊接场景设定，摆动频率越快补偿量越小

   * - 左右总计最大补偿量
     - 单次完整焊接过程最大累积补偿量
     - 根据焊接场景设定，焊缝偏差越大设定相应越大

**3）适用范围**

.. centered:: 表格 9.8-7 上下补偿开启左右补偿关闭

.. list-table::
   :widths: 70 70
   :header-rows: 0
   :align: center

   * - **关键参数**
     - **参数范围**

   * - 摆动频率Hz
     - 0(不使用焊接摆动)，0.5 到 2(使用焊接摆动)

   * - 摆动幅度mm
     - 0(不使用焊接摆动)，3 到 7(使用焊接摆动)

   * - 设定电压V
     - >17

   * - 设定电流A
     - >160
  
.. centered:: 表格 9.8-8 上下补偿关闭左右补偿开启

.. list-table::
   :widths: 70 70
   :header-rows: 0
   :align: center

   * - **关键参数**
     - **参数范围**

   * - 摆动频率Hz
     - 0.5 到 2

   * - 摆动幅度mm
     - 3 到 7

   * - 设定电压V
     - >17

   * - 设定电流A
     - >160
  
.. centered:: 表格 9.8-9 上下、左右补偿均开启

.. list-table::
   :widths: 70 70
   :header-rows: 0
   :align: center

   * - **关键参数**
     - **参数范围**

   * - 摆动频率Hz
     - 0.5 到 2

   * - 摆动幅度mm
     - 3 到 7

   * - 设定电压V
     - >19

   * - 设定电流A
     - >210

**4）注意事项**

1) 左右补偿电弧跟踪功能只可适配直线轨迹搭配对称的三角波或正弦波摆动情况。
2) 使用补偿功能焊接起始位置一定需要准确处于焊缝上方（焊枪轴线处于角焊缝中心），焊枪距离焊缝不可过近，否则有撞焊枪的风险。

.. image:: coding/132.png
   :width: 4in
   :align: center

.. centered:: 图表 9.8-7-2 焊枪处于焊缝上方

3) 设定轨迹与焊缝的偏差越大，每次最大补偿量与总计最大补偿量相应越大。
4) 设定轨迹与焊缝的终止点偏差不应大于100mm/m，偏差过大可能会导致焊丝甚至焊枪撞工件，使焊接位置偏离预设轨迹(摆动不到位)，导致电弧跟踪功能无法正常起效。
5) 程序开始WeaveStart摆动指令前需先加入ARCStart起弧判断指令。
6) 关于电弧跟踪补偿坐标系与调节系数正负号关系：

.. image:: coding/133.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-7-3 焊接场景

当焊接上下补偿方向与所选定的任意坐标系Z轴正方向一致时，调节系数为正值。

案例：如图9‑8-7-6，若上下补偿坐标系选定“基座”或“工具”，当工件处于所示位置，不补偿时焊枪逐渐向上远离工件表面，需要向下补偿（基座坐标系-Z方向），则上下补偿系数符号应为负号。

.. important:: 
   注意选择“摆动”坐标系时，摆动坐标系Z轴与工具坐标系Z轴为反向状态，若以上述案例情况，补偿系数符合应为正。
   
   焊接左右补偿调节系数无需更改，默认为正值。

7) 若选择较小设定电流电压进行焊接时，电弧跟踪上下左右调节系数应相应减小，以减小反馈电流毛刺导致的不稳定补偿。

姿态调整命令
++++++++++++++++

点击“姿态调整”图标进入Adjust命令编辑界面。

该指令针对焊接跟踪自适应调整焊枪姿态场景，记录好三个对应的姿态点后，根据机器人实际运动方向，添加姿态自适应调整指令。详见机器人外设章节。

.. image:: coding/134.png
   :width: 6in
   :align: center

.. centered:: 图表 9.8-8 Adjust指令界面

力控指令界面 
~~~~~~~~~~~~~

.. image:: coding/135.png
   :width: 6in
   :align: center

.. centered:: 图表 9.9 力控指令界面 

力控集命令
++++++++++++++++

点击“力控集”图标进入F/T命令编辑界面。

该指令包含FT_Guard(碰撞检测)，FT_Control(恒力控制)，FT_Compliance(柔顺控制)，FT_Spiral(螺旋插入)，FT_Rot(旋转插入)，FT_Lin(直线插入)，FT_FindSurface(表面定位) ，FT_CalCenter(中心定位)八个指令，详见机器人外设章节。

.. image:: coding/136.png
   :width: 6in
   :align: center

.. centered:: 图表 9.9-1 F/T指令界面

扭矩记录命令
++++++++++++++++

点击“扭矩记录”图标进入Torque命令编辑界面。

该指令为扭矩记录指令，实现扭矩实时记录碰撞检测功能。点击“扭矩记录启动”按钮，持续记录运动指令运行过程中的碰撞情况，记录的实时扭矩作为碰撞检测判断的理论值，以减少误报错概率。当超出设定阈值范围时，记录碰撞检测持续时间。点击“扭矩记录停止”按钮，停止记录。点击“扭矩记录复位”，状态恢复默认状态。

.. image:: coding/137.png
   :width: 6in
   :align: center 

.. centered:: 图表 9.9-2 Torque指令界面

视觉指令界面
~~~~~~~~~~~~~

.. image:: coding/138.png
   :width: 6in
   :align: center

.. centered:: 图表 9.10 视觉指令界面 

3D视觉命令
++++++++++++++++

点击“3D视觉”图标进入3D命令编辑界面。

该指令为3D视觉程序实例生成指令，用户可以根据生成的程序进行参考，与其他视觉设备进行通讯工作，包含相机标定和相机抓取两个程序案例参考。

.. image:: coding/139.png
   :width: 6in
   :align: center

.. centered:: 图表 9.10-1 3D指令界面

码垛指令界面
~~~~~~~~~~~~~

.. image:: coding/140.png
   :width: 6in
   :align: center

.. centered:: 图表 9.11 码垛指令界面 

矩阵移动命令
++++++++++++++++

点击“矩阵移动”图标进入Pallet命令编辑界面。

该指令为码垛程序生成指令。

.. image:: coding/141.png
   :width: 6in
   :align: center

.. centered:: 图表 9.11-1 Pallet指令界面

此功能通过设定三点坐标及行列层和层高等数值，来控制机器手规则移动，适用于常见的码垛应用。第一步选择机器人运动方式，“PTP”或者“Line”，第二步设定机器人运动路径，“头到尾走法”或“弓字形走法”，第三步设定堆叠方式，“堆垛”或“卸垛”。

.. image:: coding/142.png
   :width: 6in
   :align: center

.. centered:: 图表 9.11‑2 矩阵移动

第四步根据路径示教三个点，第一点为第一排起点，整个运动过程手臂姿态由该点决定，第二点为第一排终点，第三点为最后一排终点。第五步设点行数和列数，第六步设定层数和每一层高度。

.. image:: coding/143.png
   :width: 6in
   :align: center

.. centered:: 图表 9.11‑3 矩阵移动

通讯指令界面
~~~~~~~~~~~~~

.. image:: coding/144.png
   :width: 6in
   :align: center

.. centered:: 图表 9.12 通讯指令界面

Modbus命令
++++++++++++++++

点击“Mobus”图标进入Modbus命令编辑界面。

该指令功能为基于ModbusTCP协议的总线功能，用户可以通过相关指令控制机器人与ModbusTCP client或server通讯（主站与从站通讯），对线圈，离散量，寄存器进行读写操作。

.. image:: coding/145.png
   :width: 6in
   :align: center

.. centered:: 图表 9.12-1 modbus指令主站界面

.. image:: coding/146.png
   :width: 6in
   :align: center

.. centered:: 图表 9.12-2 modbus指令从站界面

关于ModbusTCP更多操作功能，请联系我们咨询。

Xmlrpc命令
++++++++++++++++

点击“Xmlroc”图标进入Xmlrpc命令编辑界面。

XML-RPC是一种通过sockets使用xml在程序之间传输数据的远程过程调用方法。通过这种方法，机器人控制器可以在远端的程序/服务调用功能函数（可带参数）并获取返回的结构性数据。机器人控制器负责处理编写XML-RPC客户端消息以及处理数据类型与XML之间转换的所有细节。

.. image:: coding/147.png
   :width: 6in
   :align: center

.. centered:: 图表 9.12-3 Xmlrpc指令界面

.. important:: 
  1) 控制器作为客户端连接远端自定义端口；

  2) 控制器作为客户端调用远端功能函数；

  3) 支持调用远端不同功能函数；

  4) 支持字符串数组参数传入与字符数组结果返回，数组元素个数可自定义；

  支持double型数组参数传入与double型数组结果返回，数组元素个数个数可自定义；

::

   XmlrpcClientCall(serverUrl，methodName，tableType，param)

   serverUrl 服务端url，例如："http://192.168.58.29:50000/RPC2"

   methodName 调用函数名，“example.add”

   tableType 1-double型数组，2-string型数组

   param 调用函数参数

::

   XmlrpcClientCall(error， result)

   error 0-无错误，1-错误

   result 若参数传入为double型数组，则result为double型数组，

   若参数传入为string型数组，则result为string型数组

辅助指令界面
~~~~~~~~~~~~~

.. image:: coding/148.png
   :width: 6in
   :align: center

.. centered:: 图表 9.13 辅助指令界面

辅助线程命令
++++++++++++++++

点击“辅助线程”图标进入Thread命令编辑界面。

Thread命令为辅助线程功能，用户可以定义一个辅助线程与主线程同时运行，辅助线程主要与外部设备进行数据交互，支持socket通信，机器人DI状态获取，机器人DO状态设置，机器人状态信息获取，与主线程数据交互，主线程通过辅助线程获取的数据用于控制机器人运动逻辑的判断，用户程序示例截图：

.. image:: coding/149.png
   :width: 6in
   :align: center

.. centered:: 图表 9.13-1 Thread程序示例

调用函数命令
++++++++++++++++

点击“调用函数”图标进入Function命令编辑界面。

该指令为调用函数接口功能，将机器人接口函数提供给客户选择，并提示客户该函数所需要的参数，方便客户编写脚本指令，更多函数陆续添加中。

.. image:: coding/150.png
   :width: 6in
   :align: center

.. centered:: 图表 9.13-2 Function指令界面

点位表命令
++++++++++++++++

点击“点位表”图标进入PT-Mode命令编辑界面。

该指令主要用于系统模式和点位表模式之间的模式切换，通过切换点位表来应用不同点位表内的示教点位。详情见章节11——示教点。

.. image:: coding/151.png
   :width: 6in
   :align: center

.. centered:: 图表 9.13-3 点位表指令界面

示教程序未保存验证
~~~~~~~~~~~~~~~~~~~

在程序示教页面，打开/新建程序后，若示教程序发生改动未保存程序。

若点击“打开”、“新建”、“导出”、“重命名”等相关文件操作，则触发“是否保存此程序”弹出框，提示“当前程序已发生改变，是否保存此程序的更改？”，如下图。

.. image:: coding/152.png
   :width: 6in
   :align: center

.. centered:: 图表 9.14-1 当前页面程序未保存验证

**Step1**：点击“不保存”按钮，程序恢复未修改之前数据，并继续执行之前的相关文件操作。

**Step2**：点击“保存”按钮，未保存的lua程序保存成功，并继续执行之前的相关文件操作。

若离开程序示教页面，切换到其他页面时，同样触发“是否保存此程序”提示，且仍然停留在当前示教程序页面，如下图。

.. image:: coding/153.png
   :width: 6in
   :align: center

.. centered:: 图表 9.14-2 切换页面程序未保存验证

**Step1**：点击“不保存”按钮，跳转到之前选择的页面。

**Step2**：点击“保存”按钮，未保存的lua程序保存成功，并跳转到之前选择的页面。

示教程序加密
~~~~~~~~~~~~~~

示教程序分为加密和不加密的状态。加密级别分为一级加密和二级加密，其中一级加密保护程度最高，二级次之。
所有示教程序在“系统设置--自定义信息”中以表格形式进行程序加密信息展示与设置。表格右侧配有加密级别说明。

.. image:: coding/154.png
   :width: 6in
   :align: center

.. centered:: 图表 9.15-1 示教程序加密

当程序为一级加密状态时，打开该程序后：
操作栏中对应的“导出”、“保存”、“另存为”、“复制”、“剪切”、“粘贴”、“删除”、“上移”、“下移”和“编辑模式切换”等按钮图标都会变灰，点击图标无效并会提示当前程序处于加密状态。
程序“重命名”图标将会隐藏。
添加指令栏和程序编辑区域都会不可见且提示已处于一级加密锁定。

.. image:: coding/155.png
   :width: 6in
   :align: center

.. centered:: 图表 9.15-2 程序一级加密界面

当程序为二级加密时，在“程序示教”页面打开该程序后：
操作栏中对应的“保存”、“复制”、“剪切”、“粘贴”、“删除”、“上移”和“下移”等按钮图标都会变灰。点击图标无效并会提示当前程序处于加密状态。
程序“重命名”图标将会隐藏。
添加指令栏不可见且提示已处于二级加密锁定。
程序编辑区域可正常浏览阅读程序。

.. image:: coding/156.png
   :width: 6in
   :align: center

.. centered:: 图表 9.15-3 程序二级加密界面

一级加密和二级加密都可以使用“导出”功能，在导入时会进行验证操作，如果存在同名程序为加密文件，则会中断导入操作并提示不可导入覆盖加密程序。

.. image:: coding/157.png
   :width: 3in
   :align: center

.. centered:: 图表 9.15-4 程序导入

局部示教点位
~~~~~~~~~~~~~~

局部示教点位和当前示教程序绑定。添加程序命令时，只能应用于当前示教程序，不可用于其它示教程序。

**新增**：点击程序文件名最右侧的“新增局部示教点”图标，进行局部示教点的添加。(局部示教点位详情记录请翻阅机器人操作中的示教点记录)

.. image:: coding/158.png
   :width: 6in
   :align: center

.. centered:: 图表 9.16-1 新增局部示教点

**删除**：点击表格序号栏选择需要删除的局部示教点后，点击局部示教点位标题右上角的“删除”图标，进行局部示教点的删除。

.. image:: coding/159.png
   :width: 6in
   :align: center

.. centered:: 图表 9.16-2 删除局部示教点

**运行**：点击局部示教点位表格数据操作栏中的“开始运行”图标，进行局部示教点的单点运行，将机器人移动到该点的位置。

.. image:: coding/160.png
   :width: 6in
   :align: center

.. centered:: 图表 9.16-3 运行局部示教点

**详情**：点击局部示教点位表格数据操作栏中的“详情”图标，查看局部示教点的详情。

.. image:: coding/161.png
   :width: 3in
   :align: center

.. centered:: 图表 9.16-4 局部示教点详情

当前程序备份
~~~~~~~~~~~~~~

用户修改示教程序点击保存后，触发当前程序的“备份”功能(备份时间为1年)，将当前程序的初始内容进行保存展示在右侧，方便用户对比修改的内容。
用户选择日期可以查看对应的程序备份内容，点击右上角“删除”图标可以删除当前程序备份内容。当前程序备份的内容只可查看，不可修改。

.. image:: coding/162.png
   :width: 6in
   :align: center

.. centered:: 图表 9.17 当前程序备份

Modbus TCP通信
~~~~~~~~~~~~~~~~~
ModbusTCP是工业生产中常用的通信协议，法奥协作机器人提供ModbusTCP主站和ModbusTCP从站两种方式与您的设备进行通信。

协作机器人最多支持8个ModbusTCP主站同时与外部设备进行通信，每个主站最多支持128个寄存器；协作机器人ModbusTCP从站具有128个线圈、128个离散输入、64个保持寄存器和64 个输入寄存器(保持寄存器和输入寄存器数据类型包含无符号、有符号和浮点型三种类型)，同时协作机器人部分ModbusTCP从站输入寄存器地址专用于反馈当前机器人的关节位置、运动速度等信息，部分线圈寄存器地址专用于控制机器人启动程序、停止程序、设置控制箱DO等功能。

机器人ModbusTCP从站仅支持与一个主站建立连接，机器人可同时作为主站和从站与不同的设备通信。下面是详细使用方法。
 
ModbusTCP主站
+++++++++++++++++

在使用协作机器人做ModbusTCP主站与您的设备进行通信前，请先检查您的设备与机器人的网络连接，并确认网络接口在同一网段。

使用机器人ModbusTCP主站有以下几个步骤：

- 添加主站；
- 添加寄存器；
- 通信测试；
- 编写用户程序；
- 执行用户程序。

添加ModbusTCP主站
********************

打开WebApp，依次点击“示教模拟”、“程序示教”，新建用户程序“testModbusMaster.lua”。

.. image:: coding/163.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-1 创建ModbusTCP主站用户程序

点击“ModbusTCP设置”按钮，打开ModbusTCP功能配置页面。

.. image:: coding/164.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-2 打开ModbusTCP设置

依次点击“主站设置”、“添加Modbus主站”，即完成添加一个ModbusTCP主站。

.. image:: coding/165.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-3 添加“ModbusTCP主站”

根据您的设备情况依次输入“名称”、“从站ip”、“端口号”、“从站号”和“通信周期”，上述参数的具体含义如下：

**名称**：机器人ModbusTCP主站名称，机器人最大支持创建8个主站与相应从站建立连接，不同主站可设置唯一的名称进行区分，如“PLC”、“相机”、“数据采集卡”、“FRRobot1”等；

**从站ip**：机器人ModbusTCP主站要连接的从站IP地址；

.. note:: 要先通过网线连接机器人与从站设备，并保证机器人与从站设备的IP地址在同一网段。

**端口号**：要连接的ModbusTCP从站端口号；

**从站号**：要连接的ModbusTCP从站号；

**通信周期**：机器人ModbusTCP主站查询从站状态的周期(ms)，该周期仅影响“ModbusTCP设置”页面查看从站寄存器数据的更新速度，而不影响用户lua程序中读取或写入ModbusTCP从站寄存器数值的速度。

.. image:: coding/166.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-4 设置ModbusTCP主站参数

正确输入上述参数后，机器人ModbusTCP主站自动与配置的从站建立连接，连接成功后，页面上的“连接状态”指示灯亮起。

.. note:: 
   若您已经确认对ModbusTCP主站的相关参数进行了正确的配置，但机器人与您的设备没有成功连接，请检查以下配置：
   
   ①机器人与从站设备的物理网络连接；

   ②机器人示教器和控制箱两个网络物理端口的IP地址不同，请确认是否连接到正确的网络端口；

   ③请确认机器人网络端口与从站设备的网络端口是否在同一网段，如机器人的IP地址为192.168.58.2，则从站设备的IP地址必须为192.168.58.0~192.168.58.255，且不能与机器人IP地址相同；
   
   ④检查从站设备的端口号与设置的端口号是否相同。若连接状态指示灯处于闪烁状态，则表示该主站中的寄存器地址有误，请检查寄存器类型和地址是否正确。

.. image:: coding/167.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-5 ModbusTCP主站连接状态

至此我们已经完成一个机器人ModbusTCP主站的创建，若您再次点击“添加Modbus主站”，即可再次创建一个新的ModbusTCP主站，机器人最多支持8个主站同时与外部设备通信，双击Modbus主站右上角的“删除”按钮，即可删除该Modbus主站。

.. image:: coding/168.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-6 再次添加ModbusTCP主站

ModbusTCP主站添加寄存器
***************************

点击“添加主站寄存器”按钮即可为该主站添加一个寄存器。

.. image:: coding/169.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-7 添加ModbusTCP主站寄存器

依次选择主站寄存器类型、输入地址编号和名称，各参数意义如下：

**类型**：寄存器类型，DI-离散输入；DO-线圈；AI无符号-无符号型输入寄存器(0-65535)；AI有符号-有符号型输入寄存器(-32768-32767)；AI浮点型-浮点数型输入寄存器(浮点型寄存器数据长度32位，占用两个有符号或无符号型寄存器)；AO无符号-无符号型保持寄存器(0-65535)；AI有符号-有符号型保持寄存器(-32768-32767)；AI浮点型-浮点数型保持寄存器(浮点型寄存器数据长度32位，占用两个有符号或无符号型寄存器)，其中AI、AO中的浮点型寄存器为大端显示；

**地址编号**：要读取或写入的ModbusTCP从站寄存器地址；

**名称**：寄存器的别名，机器人ModbusTCP主站最多可设置128个不同的寄存器，每个寄存器可根据实际意义设置不同的名称进行区分，如“开始”，“伺服到位”、“液位”等。

.. image:: coding/170.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-8 设置ModbusTCP主站寄存器参数

再次点击“添加主站寄存器”按钮即可再添加一个主站寄存器，双击寄存器右侧的“删除”按钮，即可删除该寄存器，如下图为每种类型都添加了一个寄存器。

.. note:: 若添加主站寄存后，主站连接状态指示灯闪烁，则表示该主站寄存器地址无法读取，请检查该寄存器类型和地址是否正确。

.. image:: coding/171.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-9 添加多个主站寄存器

ModbusTCP主站通信测试
***********************

在通信测试前，请先检查ModbusTCP主站“连接状态”指示灯是否处于常亮状态，若指示灯常亮则表示当前连接已成功。

机器人Modbus主站寄存器有“地址值”数值框用于显示当前寄存器的值，其中DI(离散输入)和AI(输入寄存器)类型的寄存器为只读类型，对应的地址值为灰色不可编辑数值框。

当从站相应地址的数值改变时，机器人主站对应寄存器地址值同步显示当前的数值，而DO(线圈)和AO(保持寄存器)为可读可写寄存器，因此它的地址为白色可编辑数值框，既可以读取ModbusTCP从站相应寄存器的数值，也可以在机器人Modbus主站设置页面修改该寄存器数值。

.. image:: coding/172.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-10 Modbus主站地址值

1. 主站DI、AI类型寄存器数值监控

在外部ModbusTCP从站设备上将DI(离散输入)寄存器的255号地址值设为1，将AI(输入寄存器)的257号地址值改为123，258号寄存器地址值改为-123，259号寄存器地址值改为123.3。此时机器人Modbus主站设置页面对应寄存器的地址值将进行相应的显示。

.. note:: 
   由于设置地址259的寄存器为浮点型寄存器，因此它实际占用了259和260两个16位寄存器来存储一个浮点数，因此您不能再单独设置一个寄存器来操作AI的260号寄存器，否则会产生数值错误。

.. image:: coding/173.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-11 Modbus主站显示DI、AI寄存器数值

2. 主站DO、AO类型寄存器数值写入

在机器人Modbus主站设置页面中将名称为“开始”的DO(线圈)类型寄存器的255号地址值输入框中输入1，名称为“目标位置A”、“目标位置B”和“目标位置C”的AO(保持寄存器)的260、261、262号寄存器地址值输入框中分别输入65535、-32768和128.78，此时Modbus从站的相应寄存器地址已被写入相应的数值。

.. image:: coding/174.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-12 Modbus主站写入DO、AO寄存器

3. 主站DO、AO类型寄存器数值监控

在ModbusTCP从站中更改DO(线圈)、AO(保持寄存器)的值，ModbusTCP主站设置页面的寄存器地址值不会立即更新显示，需要点击主站配置右上角的“刷新”按钮，此时页面上DO、AO寄存器地址值才会更新。

.. image:: coding/175.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-13 刷新ModbusTCP主站DO、AO地址值

编写ModbusTCP主站程序
++++++++++++++++++++++++++

依次点击“全部”、“通讯指令”，打开通讯指令添加页面。

.. image:: coding/176.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-14 打开通讯指令添加页面

点击“Modbus”。

.. image:: coding/177.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-15 选择Modbus

点击“Modbus_TCP”。

.. image:: coding/178.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-16 选择Modbus_TCP
   
选择“主站(客户端)”，打开ModbusTCP主站指令添加页面。

.. image:: coding/179.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-17 ModbusTCP主站指令添加

1. 写单个数字输出DO(线圈)

选择“Modbus主站名称”为之前在Modbus主站设置页面添加的主站“PLC”，DO名称为“开始”，寄存器数量为1，寄存器值为1，点击“写数字输出”按钮。最后翻至该页面最底端，点击“应用”按钮。

.. image:: coding/180.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-18 添加写单个数字输出

此时机器人程序“testModbusMaster.lua”中已经添加一条机器人Modbus主站写单个数字输出的指令，将机器人切换到自动模式，点击启动按钮，机器人将主站“PLC”对应的线圈寄存器“启动”的地址值写为1。

.. image:: coding/181.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-19 写单个线圈LUA程序

2. 写多个数字输出DO(线圈)

打开ModbusTCP主站指令添加页面，选择“Modbus主站名称”为之前在Modbus主站设置页面添加的主站“PLC”，DO名称为“开始”，寄存器数量为5，寄存器值为1,0,1,0,1，其中寄存器值的个数要与设置的寄存器数量对应，且多个寄存器值之间用英文逗号隔开，点击“写数字输出”按钮。最后翻至该页面最底端，点击“应用”按钮。

.. image:: coding/182.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-20 配置写多个数字输出

此时机器人程序“testModbusMaster.lua”中已经添加一条机器人Modbus主站写多个数字输出的指令，将机器人切换到自动模式，点击启动按钮，机器人将主站“PLC”对应的线圈寄存器“启动”及其后面4个线圈的值分别写为1、0、1、0、1。
   
.. image:: coding/183.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-21 写多个线圈LUA程序

3. 读单个数字输出DO(线圈)
   
打开ModbusTCP主站指令添加页面，选择“Modbus主站名称”为之前在Modbus主站设置页面添加的主站“PLC”，DO名称为“开始”，寄存器数量为1，寄存器值不需要填写，点击“读数字输出”。最后翻至该页面最底端，点击“应用”按钮。
   
.. image:: coding/184.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-22 配置读单个数字输出

此时机器人程序“testModbusMaster.lua”中已经添加一条机器人Modbus主站读单个数字输出的指令。
      
.. image:: coding/185.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-23 读单个线圈程序

通常读Modbus寄存器后将读到的数值存入变量里，因此需要定义一个变量用于存储读取的数值。点击“切换模式”按钮，将机器人lua程序切换至可编辑状态，在“ModbusMasterReadDO”指令前编写填加返回值变量“startValue”，执行程序后读到的数值将存在“startValue”里。
      
.. image:: coding/186.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-24 读单个数字输出存入变量

线圈类型的寄存器值只有0和1两种数值，在机器人程序中可以通过判断寄存器数值不同来进行不同的操作。点击“切换模式”按钮将机器人示教程序切换至不可编辑模式，添加两个关节运动指令分别运动到两个不同的点位“P1”和“P2”。
      
.. image:: coding/187.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-25 添加不同点位的运动指令

再次将程序切换至可编辑模式，并编写线圈值“startValue”的判断条件，当“startValue”值为1时，机器人运动到“P1”点，否则机器人运动到“P2”点。
      
.. image:: coding/188.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-26 根据线圈值不同运动到不同的点位

最后再将机器人程序切换至不可编辑模式，将机器人切换到自动模式，在确认安全的前提下启动运行程序。由于该程序的前两行都将名称为“开始”线圈DO值设为1，因此执行程序后机器人将运动到“P1”点。
      
.. image:: coding/189.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-27 读取单个线圈寄存器数值并运动

4. 读多个数字DO(线圈)

打开ModbusTCP主站指令添加页面，选择“Modbus主站名称”为之前在Modbus主站设置页面添加的主站“PLC”，DO名称为“开始”，寄存器数量为6，寄存器值不需要填写，点击“读数字输出”。最后翻至该页面最底端，点击“应用”按钮。
      
.. image:: coding/190.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-28 配置读多个数字输出

此时机器人程序“testModbusMaster.lua”中已经添加一条机器人Modbus主站读多个数字输出的指令。
         
.. image:: coding/191.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-29 读多个数字输出程序

点击“切换模式”按钮，将机器人lua程序切换至可编辑状态，由于读取的数量为6个，因此需要在“ModbusMasterReadDO”指令前编写填加6个返回值变“value1,value2,value3,value4,value5,value6”，执行程序后读到的6个寄存器数值将分别存在上述6个变量里，同样您可以判断“value1”~“value6”的值使机器人进行不同的动作。
         
.. image:: coding/192.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-30 读多个数字输出存入变量

5. 读数字输入DI(离散输入)

打开ModbusTCP主站指令添加页面，选择“Modbus主站名称”为之前在Modbus主站设置页面添加的主站“PLC”，DI名称为“伺服到位”，寄存器数量为2，点击“读数字输入”。最后翻至该页面最底端，点击“应用”按钮。
         
.. image:: coding/193.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-31 配置读数字输入

此时机器人程序“testModbusMaster.lua”中已经添加一条机器人Modbus主站读数字输入的指令。
            
.. image:: coding/194.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-32 读数字输入程序指令

点击“切换模式”按钮，将机器人lua程序切换至可编辑状态，在“ModbusMasterReadDO”指令前编写返回值变量“state1,state2”，执行程序后读到的两个数字输入数值将分别存在变量“state1”和“state2”里，您可以通过判断变量数值进而控制机器人做不同的操作。
            
.. image:: coding/195.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-33 读数字输入存入变量

6. 模拟输入AI(输入寄存器)和模拟输出AO(保持寄存器)的读写操作

模拟输入AI(输入寄存器)、模拟输出AO(保持寄存器)的读写操作与数字输入DI(离散输入)、数字输出DO(线圈)的操作基本一致，区别在于后者的数据范围仅限于0或1，而前者的数据范围更大，因此具体的操作可参考数字输入和数字输出程序的编写，在此仅展示模拟输入AI的读操作和模拟输出AO的读写操作程序示例。
            
.. image:: coding/196.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-34 读模拟输入AI
            
.. image:: coding/197.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-35 读写模拟输出AO

7. 等待数字输入

打开ModbusTCP主站指令添加页面，找到“等待数字输入设置”即等待DI离散输入设置，选择DI名称为配置的“伺服到位”寄存器，等待状态为“True”，超时时间为5000ms。点击“添加”按钮，最后点击“应用”按钮。
            
.. image:: coding/198.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-36 添加等待DI输入指令

此时机器人程序“testModbusMaster.lua”中已经添加一条机器人Modbus主站等待数字输入DI的指令，启动程序后，机器人会一直等待“PLC”主站的“伺服到位”寄存器值变为true，也就是数值1，由于设置的超时时间为5s，因此当机器人等待5s后“伺服到位”信号仍为0时，机器人程序将会报超时错误，程序也自动停止运行。
            
.. image:: coding/199.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-37 等待数字输入DI程序

8. 等待模拟输入

打开ModbusTCP主站指令添加页面，找到“等待模拟输入设置”即等待AI输入寄存器设置，选择AI名称为配置的“液位”寄存器，等待状态为“>”，寄存器值为255，超时时间为5000ms。点击“添加”按钮，最后点击“应用”按钮。
            
.. image:: coding/200.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-38 添加等待模拟输入

此时机器人程序“testModbusMaster.lua”中已经添加一条机器人Modbus主站等待AI输入寄存器值的指令，启动程序后，机器人会一直等待“PLC”主站的“液位”寄存器数值大于255，由于设置的超时时间为5s，因此当机器人等待5s后“液位”信号仍不大于255时，机器人程序将会报超时错误，程序也自动停止运行。
            
.. image:: coding/201.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-39 等待AI输入寄存器程序

ModbusTCP从站
++++++++++++++++++

机器人ModbusTCP从站提供通用数字输入(线圈)，通用数字输出(离散输入)，通用模拟输入(保持寄存器)和通用模拟输出(输入寄存器)四种类型的寄存器，其中通用数字输入和模拟输入主要用于机器人读取外部ModbusTCP主站数据从而控制机器人操作，而通用数字输出和模拟输出主要用于机器人向外部ModbusTCP主站设备发送数据信号，由外部主站设备读取相关寄存器数值进而控制其设备运行。除上述通用输入输出外，机器人还提供部分“功能数字输入(线圈)”用于外部主站设备控制机器人启动程序、停止程序等操作，提供部分输入寄存器用于显示当前机器人的状态信息，包括机器人当前笛卡尔位置、机器人当前运行状态等(具体定义请查看附件一：ModbusTCP从站地址映射表)。机器人ModbusTCP从站使用过程主要包括：①参数配置；②通讯测试；③程序编写。

ModbusTCP从站通讯参数配置
*******************************

打开WebApp，依次点击“示教模拟”、“程序示教”，新建用户程序“testModbusSlave.lua”。
            
.. image:: coding/202.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-40 创建ModbusTCP从站用户程序

点击“ModbusTCP设置”按钮，打开ModbusTCP功能配置页面。
            
.. image:: coding/203.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-41 打开ModbusTCP设置

依次点击“从站设置”，输入机器人从站的IP，端口号和从站号，其中“IP”为机器人从站ip地址，法奥协作机器人具有示教器和控制箱两个网络端口，两个端口的IP地址不同，根据外部设备连接机器人从站的网络端口输入正确的IP地址（推荐您使用控制箱上的网络端口），更改机器人ModbusTCP从站IP地址、端口号或从站号后需要重新启动机器人使其生效。
            
.. image:: coding/204.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-42 ModbusTCP从站设置

ModbusTCP从站参数设置完成并重启机器人后，外部主站设备即可通过设置的参数与机器人从站建立连接，连接成功后，机器人从站设置页面“连接状态”指示灯会亮起。
            
.. image:: coding/205.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-43 从站连接状态指示灯

ModbusTCP从站通讯测试
*****************************

1. 通用数字输入(线圈)

机器人ModbusTCP从站提供128个线圈寄存器，它们的寄存器地址为100~127。

.. note:: 具体定义请查看附件一：ModbusTCP从站地址映射表。

机器人ModbusTCP从站的通用寄存器均可设置别名，修改机器人从站线圈寄存器DI0的名称为“A到位”，DI1的名称为“B到位”，根据地址映射表，“A到位”和“B到位”的Modbus线圈地址分别为100和101，在外部ModbusTCP主站设备上将机器人从站线圈寄存器地址100和101都置1，此时机器人ModbusTCP从站监控页面上两寄存器指示灯亮起。
            
.. image:: coding/206.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-44 ModbusTCP从站线圈状态监控

2. 通用数字输出(离散输入)

机器人ModbusTCP从站提供128个离散输入寄存器，它们的寄存器地址为100~127。

.. note:: 具体定义请查看附件一：ModbusTCP从站地址映射表。

同样机器人ModbusTCP从站的离散输入寄存器也可以设置别名，点击“通用数字输出(离散输入)”修改机器人从站离散输入寄存器DO0的名称为“A启动”，DO1的名称为“B启动”，根据地址映射表，“A启动”和“B启动”的Modbus离散输入地址分别为100和101，点击“A启动”对应离散输入指示灯，该指示灯亮起，相应寄存器地址100的数值变为1，从外部ModbusTCP主站设备上可读到该寄存器数值。

.. image:: coding/207.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-45 ModbusTCP从站离散输入控制

1. 模拟输入(保持寄存器)

机器人提供无符号、有符号和浮点型三种类型的保持寄存器共64个，AI0~AI63的地址为100~195

.. note:: text
   具体定义请查看附件一：ModbusTCP从站地址映射表，其中无符号类型寄存器数据范围为0~65535，有符号型寄存器数据范围为-32768~32767，浮点型寄存器为大端显示。
   
   更改AI0和AI1的名称分别为“电压”和“电流”，从ModbusTCP从站地址映射表中查出两寄存器的地址分别为100和101，因此当连接的主站设备修改保持寄存器100和101寄存器地址值时，机器人ModbusTCP从站监控页面“电压”和“电流”寄存器地址值相应同步更新显示，机器人的模拟输入主要用于机器人读取外部主站设备数值信号。

.. image:: coding/208.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-46 ModbusTCP从站模拟输入监控

4. 模拟输出(输入寄存器)

机器人提供无符号、有符号和浮点型三种类型的输入寄存器共64个，AO0~AO63的地址为100~195
   
.. note:: text
   具体定义请查看附件一：ModbusTCP从站地址映射表，其中无符号类型寄存器数据范围为0~65535，有符号型寄存器数据范围为-32768~32767，浮点型寄存器为大端显示。
   
   更改AO0和AO1的名称分别为“目标位置A”和“目标位置B”，输入量寄存器数值分别为2000和1500，从ModbusTCP从站地址映射表中查出两寄存器的地址分别为100和101，因此当连接的主站设备读取输入寄存器100和101寄存器地址值时，即可得到所设置的数值，机器人从站模拟输出主要用于机器人向外部主站设备传递数值信号。

.. image:: coding/209.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-47 Modbus从站修改模拟输入

ModbusTCP从站程序编写
**************************

依次点击“全部”、“通讯指令”，打开通讯指令添加页面。

.. image:: coding/210.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-48 打开通讯指令添加页面

点击“Modbus”。

.. image:: coding/211.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-49 选择Modbus

点击“Modbus_TCP”。

.. image:: coding/178.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-50 选择Modbus_TCP

选择“从站”，打开ModbusTCP从站指令添加页面。

.. image:: coding/212.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-51 ModbusTCP从站指令添加

1. 写单个数字输出DO(离散输入)

选择DO名称为“A启动”，寄存器数量为1，寄存器值为0，点击“写单个数字输出”。最后翻至该页面最底端，点击“应用”按钮。

.. image:: coding/213.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-52 添加写单个数字输出指令

此时机器人程序“testModbusSlave.lua”中已经添加一条机器人Modbus从站写单个数字输出的指令，将机器人切换到自动模式，点击启动按钮，机器人将名称为“A启动”对应的数字输出的地址值写为0。
   
.. image:: coding/214.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-53 写单个数字输出LUA程序

2. 写多个数字输出DO(离散输入)

打开ModbusTCP从站指令添加页面，找到“数字输出设置”，选择DO名称为“A启动”，寄存器数量为5，寄存器值为1,0,1,0,1，其中寄存器值的个数要与设置的寄存器数量对应，且多个寄存器值之间用英文逗号隔开，点击“写数字输出”。最后翻至该页面最底端，点击“应用”按钮。
   
.. image:: coding/215.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-54 配置写多个数字输出

此时机器人程序“testModbusSlave.lua”中已经添加一条机器人Modbus从站写多个数字输出的指令，将机器人切换到自动模式，点击启动按钮，机器人将从站“A启动”其后面4个离散输入寄存器的值分别写为1、0、1、0、1。
      
.. image:: coding/216.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-55 写多个数字输出LUA程序

3. 读单个数字输出DO(离散输入)

打开ModbusTCP主站指令添加页面，找到“数字输出设置”，DO名称为“A启动”，寄存器数量为1，寄存器值不需要填写，点击“读数字输出”。最后翻至该页面最底端，点击“应用”按钮。
      
.. image:: coding/217.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-56 配置读单个数字输出

此时机器人程序“testModbusSlave.lua”中已经添加一条机器人Modbus从站读单个数字输出的指令。
         
.. image:: coding/218.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-57 读单个数字输出程序

通常读Modbus寄存器后将读到的数值存入变量里，因此需要定义一个变量用于存储读取的数值。点击“切换模式”按钮，将机器人lua程序切换至可编辑状态，在“ModbusSlaveReadDO”指令前编写填加返回值变量“AStartValue”，执行程序后读到的数值将存在“AStartValue”里。
         
.. image:: coding/219.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-58 读单个数字输出存入变量

线圈类型的寄存器值只有0和1两种数值，在机器人程序中可以通过判断寄存器数值不同来进行不同的操作。点击“切换模式”按钮将机器人示教程序切换至不可编辑模式，添加两个关节运动指令分别运动到两个不同的点位“P1”和“P2”。
         
.. image:: coding/220.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-59 添加不同点位的运动指令

再次将程序切换至可编辑模式，并编写数字输出值“AStartValue”的判断条件，当“AStartValue”值为1时，机器人运动到“P1”点，否则机器人运动到“P2”点。
         
.. image:: coding/221.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-60 根据数字输出值不同运动到不同的点位

最后再将机器人程序切换至不可编辑模式，将机器人切换到自动模式，在确认安全的前提下启动运行程序。由于该程序的第二行将名称为“A启动”数字输出DO值设为1，因此执行程序后机器人将运动到“P1”点。
         
.. image:: coding/222.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-61 读取单个线圈寄存器数值并运动

4. 读多个数字输出DO(离散输入)

打开ModbusTCP主站指令添加页面，找到“数字输出设置”，选择DO名称为“A启动”，寄存器数量为2，寄存器值不需要填写，点击“读数字输出”。最后翻至该页面最底端，点击“应用”按钮。
         
.. image:: coding/223.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-62 配置读多个数字输出

此时机器人程序“testModbusSlave.lua”中已经添加一条机器人Modbus从站读多个数字输出的指令。
            
.. image:: coding/224.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-63 读多个数字输出程序

点击“切换模式”按钮，将机器人lua程序切换至可编辑状态，由于读取的数量为2个，因此需要在“ModbusSlaveReadDO”指令前编写填加2个返回值变“value1,value2”，执行程序后读到的2个数字输出寄存器数值将分别存在上述2个变量里，同样您可以判断“value1”、“value6”的值使机器人进行不同的动作。
            
.. image:: coding/225.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-64 读多个数字输出存入变量

5. 读数字输入DI(线圈)

打开ModbusTCP从站指令添加页面，找到“数字输入设置”，选择DI名称为“A到位”，寄存器数量为2，点击“读数字输入”。最后翻至该页面最底端，点击“应用”按钮。
            
.. image:: coding/226.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-65 配置读数字输入

此时机器人程序“testModbusSlave.lua”中已经添加一条机器人Modbus从站读数字输入的指令。
               
.. image:: coding/227.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-66 读数字输入程序指令

点击“切换模式”按钮，将机器人lua程序切换至可编辑状态，在“ModbusSlaveReadDI”指令前编写返回值变量“AState,BState”，执行程序后读到的两个数字输入数值将分别存在变量“AState”和“BState”里，您可以通过判断变量数值进而控制机器人做不同的操作。
              
.. image:: coding/228.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-67 读数字输入程序

6. 模拟输出AO(输入寄存器)和模拟输入AI(保持寄存器)的读写操作

模拟输出(输入寄存器)、模拟输入(保持寄存器)的读写操作与数字输出(离散输入)、数字输入(线圈)的操作基本一致，区别在于后者的数据范围仅限于0或1，而前者的数据范围更大，因此具体的操作可参考数字输出和数字输入程序的编写，在此仅展示模拟输入的读操作和模拟输出的读写操作程序示例。
              
.. image:: coding/229.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-68 读模拟输入
              
.. image:: coding/230.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-69 读写模拟输出

7. 等待数字输入

打开ModbusTCP从站指令添加页面，找到“等待数字输入设置”，选择DI名称为配置的“A到位”寄存器，等待状态为“True”，超时时间为5000ms。点击“添加”按钮，最后点击“应用”按钮。
              
.. image:: coding/231.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-70 添加等待数字输入指令

此时机器人程序“testModbusSlave.lua”中已经添加一条机器人Modbus从站等待数字输入的指令，启动程序后，机器人会一直等待从站的“A到位”线圈寄存器值变为true，也就是数值1，由于设置的超时时间为5s，因此当机器人等待5s后“A到位”信号仍为0时，机器人程序将会报超时错误，程序也自动停止运行。
              
.. image:: coding/232.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-71 等待数字输入程序

8. 等待模拟输入

打开ModbusTCP从站指令添加页面，找到“等待模拟输入设置”选择AI名称为配置的“电压”寄存器，等待状态为“>”，寄存器值为255，超时时间为5000ms。点击“添加”按钮，最后点击“应用”按钮。

.. image:: coding/233.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-72 添加等待模拟输入指令

此时机器人程序“testModbusSlave.lua”中已经添加一条机器人Modbus从站等待模拟输入值的指令，启动程序后，机器人会一直等待从站的“电压”寄存器数值大于255，由于设置的超时时间为5s，因此当机器人等待5s后“电压”信号仍不大于255时，机器人程序将会报超时错误，程序也自动停止运行。
              
.. image:: coding/234.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-73 等待模拟输入寄存器程序

ModbusTCP从站机器人状态反馈与控制
***********************************

协作机器人ModbusTCP从站输入寄存器地址310~473用于反馈机器人实时状态(具体地址定义见附件一：ModbusTCP从站地址映射表)，您只需要用主站设备读取对应寄存器的数值即可获取对应的机器人实时状态数据。

协作机器人ModbusTCP从站线圈寄存器地址300~599用于主站设备对机器人进行控制(具体地址定义见附件一：ModbusTCP从站地址映射表)，以线圈地址502为例，该地址功能表示“启动程序”。

当机器人处于自动模式下，主站设备将地址502的值从0置1时，机器人自动开始运行当前配置的程序；再以线圈地址300为例，它用于控制机器人控制箱DO0的输出，当外部主站将线圈地址300从0置1时，控制箱DO0自动输出有效，同样外部主站将线圈地址300从1置0时，控制箱DO0输出无效。在ModbusTCP从站设置页面点击“功能数字输入(线圈)”，即可监控当前所有的功能数字输入情况。
              
.. image:: coding/235.png
   :width: 6in
   :align: center

.. centered:: 图表 9.18-74 机器人从站功能数字输入

附件一：Modbus从站地址映射表

.. list-table::
   :widths: 10 20 25 15 15 10 10
   :header-rows: 0
   :align: center

   * - **地址**
     - **类型**
     - **名称**
     - **数据类型**
     - **功能码**
     - **读/写**
     - **备注**

   * - 100
     - 
     - DI0
     -  
     -  
     -   
     -   

   * - 101
     - 
     - DI1
     -  
     -  
     -   
     -  

   * - 102
     - 通用数字输入(线圈)
     - DI2
     - BOOL 
     - 0x02 
     -   
     - 读写 
  
   * - 103
     - 
     - DI3
     -  
     -   
     -  
     -  
  
   * - ...
     - 
     - ...
     -  
     -   
     -  
     -  
  
   * - 227
     - 
     - DI127
     -  
     -   
     -  
     -  
  
   * - 
     - 
     -   
     - 
     -  
     -  
     -  

   * - 100
     - 
     - DO0
     -   
     -  
     -  
     -  

   * - 101
     - 
     - DO1
     -   
     -  
     -  
     -  

   * - 102
     - 通用数字输出(离散)
     - DO2
     - BOOL 
     - 0x01、0x05、0x15 
     - 只读 
     -   
  
   * - 103
     - 
     - DO3
     -  
     -  
     -   
     -  
  
   * - ...
     - 
     - ...
     -  
     -  
     -   
     -  
  
   * - 227
     - 
     - DO127
     -  
     -  
     -   
     -  
  
   * - 
     - 
     - 
     -   
     -  
     -  
     -  

   * - 100
     - 
     - AI0
     -  
     -   
     -  
     -  

   * - 101
     - 
     - AI1
     -   
     -  
     -  
     -  

   * - 102
     - 
     - AI2
     - UINT16
     - 
     -   
     -  
  
   * - ...
     - 
     - ...
     -  
     -   
     -  
     -  
  
   * - 115
     - 
     - AI15
     -  
     -  
     -   
     -  
  
   * - 116
     - 
     - AI16
     -  
     -   
     -  
     -  
  
   * - 117
     - 
     - AI17
     -  
     -   
     -  
     -  
  
   * - 118
     - 模拟输入(保持寄存器)
     - AI18
     - INT16 
     - 0x04 
     - 只读 
     -   
  
   * - ...
     - 
     - ...
     -   
     -  
     -  
     -
  
   * - 131
     - 
     - AI31
     -   
     -  
     -  
     -
  
   * - 132
     - 
     - AI32
     -   
     -  
     -  
     -
  
   * - 133
     - 
     - AI33
     - FLOAT32(大端显示) 
     -   
     -  
     -
  
   * - ...
     - 
     - ...
     -   
     -  
     -  
     -
  
   * - 194
     - 
     - AI63
     -  
     -   
     -  
     -
  
   * - 195
     - 
     - 
     -  
     -   
     -  
     -
  
   * - 
     - 
     - 
     -   
     -  
     -  
     -  

   * - 100
     - 
     - AO0
     -  
     -   
     -  
     -  

   * - 101
     - 
     - AO1
     -  
     -  
     -   
     -  

   * - 102
     - 
     - AO2
     - UINT16
     - 
     -   
     -  
  
   * - ...
     - 
     - ...
     -  
     -  
     -   
     -  
  
   * - 115
     - 
     - AO15
     -  
     -  
     -   
     -  
  
   * - 116
     - 
     - AO16
     -  
     -  
     -   
     -  
  
   * - 117
     - 
     - AO17
     -  
     -   
     -  
     -  
  
   * - 118
     - 模拟输出(输入寄存器)
     - AO18
     - INT16 
     - 0x03、0x06、0x16
     - 读写 
     -   
  
   * - ...
     - 
     - ...
     -  
     -  
     -   
     -
  
   * - 131
     - 
     - AO31
     -  
     -  
     -   
     -
  
   * - 132
     - 
     - AO32
     -  
     -   
     -  
     -
  
   * - 133
     - 
     - AO33
     - FLOAT32(大端显示) 
     -  
     -   
     -
  
   * - ...
     - 
     - ...
     -  
     -  
     -   
     -
  
   * - 194
     - 
     - AO63
     -  
     -  
     -   
     -
  
   * - 195
     - 
     - 
     -  
     -   
     -  
     -
       
   * - 
     - 
     - 
     -  
     -  
     -   
     -
       
   * - 机器人状态反馈 
     - 
     - 
     - 
     -  
     -   
     -
       
   * - 310 
     - 
     - 使能状态 0-未使能，1-使能
     -  
     -   
     -  
     -
       
   * - 311 
     - 
     - 机器人模式，1-手动模式，0-自动模式
     -  
     -   
     -  
     -
       
   * - 312 
     - 
     - 机器人运行状态 1-停止，2-运行，3-暂停，4-拖动
     -  
     -   
     -  
     -
       
   * - 313 
     - 机器人状态(输入寄存器)
     - 工具号
     -  
     -   
     -  
     -
       
   * - 314 
     - 
     - 工件号
     -  
     -   
     -  
     -
       
   * - 315 
     - 
     - 急停状态 0-未急停，1-急停
     -  
     -   
     -  
     -
     
   * - 316 
     - 
     - 超软限位故障
     -  
     -  
     -   
     -

   * - 317
     - 
     - 主故障码
     -  
     -   
     -  
     -

   * - 318
     - 
     - 子故障码
     -  
     -   
     -  
     -

   * - 319
     - 
     - 碰撞检测，1-碰撞，0-无碰撞
     -  
     -   
     -  
     -

   * - 320
     - 
     - 运动到位信号
     -  
     -   
     -  
     -

   * - 321
     - 
     - 安全停止信号SI0
     -  
     -  
     -   
     -

   * - 322
     - 
     - 安全停止信号SI1
     -  
     -  
     -
     -

   * - 330
     - 
     - TCP速度
     -  
     -  
     -   
     -

   * - 340
     - 
     - 关节1位置
     -  
     -  
     -   
     -

   * - 342
     - 
     - 关节2位置
     -  
     -  
     -   
     -

   * - 344
     - 
     - 关节3位置
     -  
     -   
     -  
     -

   * - 346
     - 
     - 关节4位置
     -   
     -  
     -  
     -

   * - 348
     - 
     - 关节5位置
     -  
     -  
     -   
     -

   * - 350
     - 
     - 关节6位置
     -   
     -  
     -  
     -

   * - 352
     - 
     - 关节1速度
     -   
     -  
     -  
     -

   * - 354
     - 
     - 关节2速度
     -  
     -   
     -  
     -

   * - 356
     - 
     - 关节3速度
     -  
     -  
     -   
     -

   * - 358
     - 
     - 关节4速度
     -  
     -  
     -   
     -

   * - 360
     - 
     - 关节5速度
     -  
     -   
     -  
     -

   * - 362
     - 
     - 关节6速度
     -  
     -   
     -  
     -

   * - 364
     - 
     - 关节1电流
     - FLOAT32(大端显示) 
     -   
     -  
     -

   * - 366
     - 
     - 关节2电流
     -  
     -   
     -  
     -

   * - 368
     - 
     - 关节3电流
     -  
     -   
     -  
     -

   * - 370
     - 
     - 关节4电流
     -  
     -   
     -  
     -

   * - 372
     - 
     - 关节5电流
     -  
     -  
     -   
     -

   * - 374
     - 
     - 关节6电流
     -  
     -   
     -  
     -

   * - 376
     - 
     - 关节1扭矩
     -  
     -   
     -  
     -

   * - 378
     - 
     - 关节2扭矩
     -  
     -   
     -  
     -

   * - 380
     - 
     - 关节3扭矩
     -  
     -  
     -   
     -

   * - 382
     - 
     - 关节4扭矩
     -  
     -   
     -  
     -

   * - 384
     - 
     - 关节5扭矩
     -  
     -  
     -   
     -

   * - 386
     - 
     - 关节6扭矩
     -  
     -   
     -  
     -

   * - 388
     - 
     - TCP位置X
     -  
     -  
     -   
     -

   * - 390
     - 
     - TCP位置Y
     -  
     -  
     -   
     -

   * - 392
     - 
     - TCP位置Z
     -  
     -   
     -  
     -

   * - 394
     - 
     - TCP位置RX
     -  
     -   
     -  
     -

   * - 396
     - 
     - TCP位置RY
     -  
     -   
     -  
     -

   * - 398
     - 
     - TCP位置RZ
     -   
     -  
     -  
     -

   * - 400
     - 
     - TCP速度X
     -  
     -  
     -   
     -

   * - 402
     - 
     - TCP速度Y
     -  
     -   
     -  
     -

   * - 404
     - 
     - TCP速度Z
     -  
     -   
     -  
     -

   * - 406
     - 
     - TCP速度RX
     -  
     -   
     -  
     -

   * - 408
     - 
     - TCP速度RY
     -  
     -   
     -  
     -

   * - 410
     - 
     - TCP速度RZ
     -  
     -   
     -  
     -

   * - 430
     - 
     - 控制箱模拟量输入AI0
     -  
     -  
     -   
     -

   * - 432
     - 
     - 控制箱模拟量输入AI1
     -  
     -  
     -   
     -

   * - 438
     - 
     - 工具模拟量输入AI0
     -  
     -  
     -   
     -

   * - 450
     - 
     - 控制箱模拟量输出AO0
     -  
     -  
     -   
     -

   * - 452
     - 
     - 控制箱模拟量输出AO1
     -  
     -   
     -  
     -

   * - 458
     - 
     - 工具模拟量输出AO0
     -  
     -   
     -  
     -

   * - 470
     - 
     - 控制箱数字输入Bit0-Bit7对应DI0-DI7，Bit8-Bit15对应CI0-CI7
     - UINT16 
     -   
     -  
     -

   * - 471
     - 
     - 工具端数字输入 Bit0-Bit15对应DI0-DI15
     -  
     -   
     -  
     -

   * - 472
     - 
     - 控制箱数字输出Bit0-Bit7对应DO0-DO7，Bit8-Bit15对应CO0-CO7
     -  
     -   
     -  
     -

   * - 473
     - 
     - 工具端数字输出 Bit0-Bit15对应DO0-DO15
     -  
     -  
     -   
     -

机器人控制表格如下：

.. list-table::
   :widths: 10 20 25 15 15 10 10
   :header-rows: 0
   :align: center
   
   * - **地址**
     - **类型**
     - **名称**
     - **数据类型**
     - **功能码**
     - **读/写**
     - **备注**

   * - 300
     - 数字输入(线圈)
     - 控制箱DO0
     - BOOL 
     - 0x02 
     - 读写
     - 

   * - 301
     - 
     - 控制箱DO1
     -  
     -  
     - 
     - 

   * - 302
     - 
     - 控制箱DO2
     -  
     -  
     - 
     - 

   * - 303
     - 
     - 控制箱DO3
     -  
     -  
     - 
     - 

   * - 304
     - 
     - 控制箱DO4
     -  
     - 
     -  
     - 

   * - 305
     - 
     - 控制箱DO5
     -  
     -  
     - 
     - 

   * - 306
     - 
     - 控制箱DO6
     -  
     - 
     -  
     - 

   * - 307
     - 
     - 控制箱DO7
     -  
     -  
     - 
     - 

   * - 308
     - 
     - 控制箱CO0
     -  
     - 
     -  
     - 

   * - 309
     - 
     - 控制箱CO1
     - 
     -  
     -  
     - 

   * - 310
     - 
     - 控制箱CO2
     -  
     - 
     -  
     - 

   * - 311
     - 
     - 控制箱CO3
     -  
     - 
     -  
     - 

   * - 312
     - 
     - 控制箱CO4
     - 
     -  
     -  
     - 

   * - 313
     - 
     - 控制箱CO5
     -  
     - 
     -  
     - 

   * - 314
     - 
     - 控制箱CO6
     -  
     - 
     -  
     - 

   * - 315
     - 
     - 控制箱CO7
     -  
     - 
     -  
     - 

   * - 316
     - 
     - 工具DO0
     -  
     - 
     -  
     - 

   * - 317
     - 
     - 工具DO1
     -  
     -  
     - 
     - 

   * - 318 - 499
     - 
     - 预留
     - 
     -  
     -  
     - 

   * - 500
     - 
     - 暂停
     - 
     -  
     -  
     - 

   * - 501
     - 
     - 恢复
     -  
     - 
     -  
     - 


   * - 502
     - 
     - 启动
     - 
     -  
     -  
     - 

   * - 503
     - 
     - 停止
     -  
     - 
     -  
     - 

   * - 504
     - 
     - 移至作业原点
     -  
     - 
     -  
     - 

   * - 505
     - 
     - 手自动切换
     - 
     -  
     -  
     - 

   * - 506
     - 
     - 启动主程序
     -  
     - 
     -  
     - 

   * - 507
     - 
     - 一级缩减模式
     -  
     - 
     -  
     - 

   * - 508
     - 
     - 二级缩减模式
     - 
     -  
     -  
     - 

   * - 509
     - 
     - 三级缩减模式(停止)
     - 
     -  
     -  
     - 

   * - 510
     - 
     - 清除所有故障
     - 
     -  
     -  
     - 

   * - 511 - 599
     - 
     - 预留
     -  
     - 
     -  
     - 


