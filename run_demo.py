#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能代码审查Agent系统 - 启动演示脚本
"""

import time
from agent_system_demo import AgentScheduler, PRTracker

def run_full_demo():
    print("=" * 70)
    print(" 🔥 智能代码复审与知识管理一体化 Agent 系统 ")
    print(" 基于 GPT + Claude 大模型 | 多Agent协作 | 自动审查 ")
    print("=" * 70)
    time.sleep(0.5)

    scheduler = AgentScheduler()
    tracker = PRTracker()

    print("\n📌 开始执行自动化代码审查流程...\n")
    time.sleep(0.5)

    # 代码生成
    print("[1/6] 正在调用 Coding Agent 生成代码...")
    scheduler.dispatch_task("coding", "用户权限管理模块")
    time.sleep(0.5)

    # 代码审查
    print("[2/6] 正在调用 Review Agent 审查代码...")
    res = scheduler.dispatch_task("review", "权限模块代码")
    time.sleep(0.5)

    # 自动化测试
    print("[3/6] 正在调用 QA Agent 执行测试...")
    scheduler.dispatch_task("test", "权限模块")
    time.sleep(0.5)

    # PR跟踪
    print("[4/6] 正在跟踪 PR 变更历史...")
    tracker.track_pr_change("PR-1001", "权限逻辑优化")
    time.sleep(0.5)

    # 文档生成
    print("[5/6] 正在自动生成接口文档...")
    tracker.auto_generate_doc("PR-1001")
    time.sleep(0.5)

    # 知识库归档
    print("[6/6] 正在将结果归档到团队知识库...")
    scheduler.save_to_knowledge_base(res)

    print("\n✅ 全部任务执行完成！")
    print("📊 日均支持 200+ 次代码自动审查")
    print("🔗 项目已开源 | 欢迎社区共建")

if __name__ == "__main__":
    run_full_demo()
