CNDE
=============

.. toctree:: 
    :maxdepth: 5

配置机器人CNDE状态反馈
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotRealtimeStateConfig(states: List[RobotState], period: int = 500) -> int:``"
    "描述", "设置CNDE默认配置（在RPC连接前调用）"
    "必选参数", "
    - ``states``：RobotState枚举列表
    - ``period``：数据周期(ms)，范围8-1000，默认8ms
    "
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败-errcode"

CNDE状态配置添加机器人状态
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AddRobotRealtimeState(states: List[RobotState], ip: str = None) -> int:``"
    "描述", "在配置基础上添加CNDE状态列表（支持动态维护和IP隔离）"
    "必选参数", "
    - ``states``：RobotState枚举列表，要添加的状态
    - ``ip``：可选，指定机器人IP（用于多机器人隔离配置，不提供则修改全局配置）
    "
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败-errcode"

CNDE状态配置删除机器人状态
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``DeleteRobotRealtimeState(states: List[RobotState], ip: str = None) -> int:``"
    "描述", "在配置基础上删除CNDE状态列表（支持动态维护和IP隔离）"
    "必选参数", "
    - ``states``：RobotState枚举列表，要删除的状态
    - ``ip``：可选，指定机器人IP（用于多机器人隔离配置，不提供则修改全局配置）
    "
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败-errcode"

设置CNDE状态反馈周期
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotRealtimeStatePeriod(period: int, ip: str = None) -> int:``"
    "描述", "设置CNDE状态反馈周期（支持全局或IP隔离）"
    "必选参数", "
    - ``period``：数据周期(ms)，范围8-1000
    - ``ip``：可选，指定机器人IP（不提供则修改全局配置）
    "
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败-errcode"

获取当前CNDE状态反馈所有状态集合
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``CNDEGetConfig(self) -> tuple:``"
    "描述", "获取当前所有状态集合"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败-errcode 包含状态列表的配置结果结构体"

CNDE状态反馈使用代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    from fairino.Robot import RobotState, SetRobotRealtimeStateConfig, DEFAULT_CNDE_STATES, AddRobotRealtimeState, DeleteRobotRealtimeState, SetRobotRealtimeStatePeriod
    import time

    # ==================== 全局配置参数 ====================
    ROBOT_IP = '192.168.58.2'       # 机器人IP地址
    # ========== Test1: CNDE配置与数据获取测试 =============
    # 测试步骤:
    # 1. 设置CNDE配置 (JointCurPos, ToolCurPos, 20ms周期)
    # 2. 建立RPC连接
    # 3. 打印机器人关节和TCP位姿数据
    # 4. 获取时间戳并验证周期
    # 5. 修改配置 (RobotMode, RbtEnableState, 10ms周期)
    # 6. 验证新配置生效

    def test1_cnde_config_and_data():
        """Test1: CNDE配置与数据获取测试 - 验证配置设置和数据实时性"""
        print_separator("Test1: CNDE配置与数据获取测试")

        # ===== 步骤1: 设置CNDE配置 (JointCurPos, ToolCurPos, 20ms) =====
        print("\n【步骤1】设置CNDE配置...")
        print("  配置字段: JointCurPos, ToolCurPos")
        print("  反馈周期: 20ms")

        custom_states = [
            RobotState.JointCurPos,   # 关节当前位置
            RobotState.ToolCurPos,    # 工具(TCP)当前位置
        ]

        rtn = SetRobotRealtimeStateConfig(custom_states, 20)
        if rtn != 0:
            print(f"✗ 配置设置失败，错误码: {rtn}")
            return None
        print("✓ CNDE配置设置成功")

        # ===== 步骤2: 建立RPC连接 =====
        print(f"\n【步骤2】建立RPC连接 ({ROBOT_IP})...")
        robot = Robot.RPC(ROBOT_IP)
        time.sleep(0.5)  # 等待连接和数据接收

        # 验证配置
        config = robot.CNDEGetConfig()
        if config:
            states, period = config
            print(f"✓ 连接成功，当前配置: {len(states)} 个字段, 周期 {period}ms")
        else:
            print("✗ 无法获取CNDE配置")
            return robot

        # ===== 步骤3: 打印机器人关节和TCP位姿 =====
        print("\n【步骤3】打印机器人关节和TCP位姿...")
        print("  (提示: 可拖动机器人观察数据变化)")
        print("  按 Ctrl+C 停止数据打印")
        print("  (使用 Wireshark 抓包验证实际数据周期)\n")

        sample_count = 0
        try:
            while sample_count < 100:  # 采集100个样本
                pkg = robot.robot_state_pkg

                # 每10帧打印一次
                if sample_count % 10 == 0:
                    print(f"--- 样本 #{sample_count} ---")
                    print(f"  关节位置 (deg): [{', '.join([f'{x:.3f}' for x in pkg.jt_cur_pos])}]")
                    print(f"  TCP位姿 (mm/deg): [{', '.join([f'{x:.3f}' for x in pkg.tl_cur_pos])}]")
                    print(f"  当前帧计数: {pkg.frame_cnt}")
                    print()

                sample_count += 1
                time.sleep(0.02)  # 20ms

        except KeyboardInterrupt:
            print("\n  用户中断数据打印")

        # 关闭连接
        robot.CloseRPC()
        time.sleep(1)

        # ===== 步骤4: 修改配置并验证 =====
        print("\n【步骤4】修改CNDE配置...")
        print("  新配置字段: RobotMode, RbtEnableState")
        print("  新反馈周期: 10ms")

        new_states = [
            RobotState.RobotMode,
            RobotState.RbtEnableState,
        ]

        # 设置新配置
        rtn = SetRobotRealtimeStateConfig(new_states, 10)
        if rtn != 0:
            print(f"✗ 新配置设置失败，错误码: {rtn}")
            return robot
        print("✓ 新配置设置成功")

        # 重新连接
        robot = Robot.RPC(ROBOT_IP)
        time.sleep(0.5)

        # 验证新配置
        config = robot.CNDEGetConfig()
        if config:
            states, period = config
            print(f"✓ 当前配置: {[s.name for s in states]}")
            print(f"✓ 当前周期: {period}ms")

            if period == 10:
                print("✓ 配置修改验证通过 (周期已变为10ms)")
            else:
                print(f"⚠ 周期未生效 (期望10ms, 实际{period}ms)")

            # 打印新数据
            pkg = robot.robot_state_pkg
            print(f"\n【新配置数据】")
            print(f"  robot_mode: {pkg.robot_mode}")
            print(f"  rbtEnableState: {pkg.rbtEnableState}")
        else:
            print("✗ 无法获取新配置")

        print("\n✓ Test1 完成")
        return robot


    if __name__ == "__main__":
        test1_cnde_config_and_data()


    # ======== Test2: Add/Delete 状态字段测试 ====================
    # 功能: 测试 AddRobotRealtimeState() 和 DeleteRobotRealtimeState()
    # 测试步骤:
    #   1. 使用 AddRobotRealtimeState() 添加 SpeedScaleManual 和 SpeedScaleAuto
    #   2. 连接机器人，打印手动/自动模式全局速度
    #   3. 在 WebApp 修改全局速度，观察 SDK 数据变化
    #   4. 使用 DeleteRobotRealtimeState() 删除添加的字段
    #   5. 重新连接，验证速度值是否为 0（字段不再更新）


    def test2_add_delete_state():
        """Test2: Add/Delete 状态字段测试 - 验证动态添加和删除 CNDE 状态"""
        print_separator("Test2: Add/Delete 状态字段测试")

        # ===== 步骤1: 添加 SpeedScaleManual 和 SpeedScaleAuto 字段 =====
        print("\n【步骤1】使用 AddRobotRealtimeState() 添加速度比例字段...")
        print("  添加字段: SpeedScaleManual, SpeedScaleAuto")

        rtn = AddRobotRealtimeState([
            RobotState.SpeedScaleManual,
            RobotState.SpeedScaleAuto,
        ])

        if rtn != 0:
            print(f"✗ 添加字段失败，错误码: {rtn}")
            return None
        print("✓ 字段添加成功")

        # ===== 步骤2: 建立 RPC 连接并打印速度 =====
        print(f"\n【步骤2】建立 RPC 连接 ({ROBOT_IP})...")
        robot = Robot.RPC(ROBOT_IP)
        time.sleep(0.5)  # 等待连接和数据接收

        # 验证配置
        config = robot.CNDEGetConfig()
        if config:
            states, period = config
            print(f"✓ 连接成功，当前配置: {len(states)} 个字段")
            # 检查是否包含添加的字段
            has_manual = RobotState.SpeedScaleManual in states
            has_auto = RobotState.SpeedScaleAuto in states
            if has_manual and has_auto:
                print("✓ 配置验证通过: SpeedScaleManual 和 SpeedScaleAuto 已添加")
            else:
                print(f"⚠ 配置验证警告: Manual={has_manual}, Auto={has_auto}")
        else:
            print("✗ 无法获取 CNDE 配置")

        # 打印速度数据
        print("\n【当前速度数据】(请在 WebApp 中修改全局速度观察变化)")
        print("  提示: 拖动机器人使能并切换手/自动模式，观察速度值")
        print("  按 Ctrl+C 停止数据打印\n")

        sample_count = 0
        try:
            while sample_count < 100:  # 采集 100 个样本 (约 10 秒，按 100ms 间隔)
                pkg = robot.robot_state_pkg
                print(f"  [{sample_count:3d}] SpeedScaleManual: {pkg.speedScaleManual:.2f}, "
                    f"SpeedScaleAuto: {pkg.speedScaleAuto:.2f}, "
                    f"Mode: {pkg.robot_mode}")
                sample_count += 1
                time.sleep(0.1)  # 100ms 间隔
        except KeyboardInterrupt:
            print("\n  用户中断数据打印")

        print(f"\n✓ 数据采集完成，共 {sample_count} 个样本")

        # ===== 步骤3: 断开连接 =====
        print("\n【步骤3】断开当前连接...")
        robot.CloseRPC()
        time.sleep(1.0)  # 等待CNDE完全关闭

        # ===== 步骤4: 删除添加的字段 =====
        print("\n【步骤4】使用 DeleteRobotRealtimeState() 删除速度比例字段...")
        rtn = DeleteRobotRealtimeState([
            RobotState.SpeedScaleManual,
            RobotState.SpeedScaleAuto,
        ])

        if rtn != 0:
            print(f"✗ 删除字段失败，错误码: {rtn}")
            return robot
        print("✓ 字段删除成功")

        # ===== 步骤5: 重新连接并验证字段值为 0 =====
        print(f"\n【步骤5】重新连接并验证删除后的字段值...")

        robot = Robot.RPC(ROBOT_IP)
        time.sleep(0.5)

        # 读取速度值
        pkg = robot.robot_state_pkg
        manual_speed = pkg.speedScaleManual
        auto_speed = pkg.speedScaleAuto

        print(f"\n  删除后 SpeedScaleManual: {manual_speed:.2f}")
        print(f"  删除后 SpeedScaleAuto: {auto_speed:.2f}")

        # 验证是否为 0
        if manual_speed == 0 and auto_speed == 0:
            print("\n✓ Test2 验证通过: 删除字段后速度值为 0")
        else:
            print(f"\n⚠ Test2 警告: 删除字段后速度值非零")

        print("\n✓ Test2 完成")
        return robot

    if __name__ == "__main__":
        test2_add_delete_state()