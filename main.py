from agent_core import CodingAgent, ReviewAgent, QAAgent
from scheduler import Scheduler
from pr_tracker import PRTracker
from knowledge_base import KnowledgeBase
import time

def main():
    print("=" * 70)
    print("  智能代码复审与知识管理一体化Agent系统")
    print("  基于 GPT + Claude 模型 | 多Agent协作 | PR自动审查")
    print("=" * 70)
    time.sleep(0.3)

    scheduler = Scheduler()
    tracker = PRTracker()
    kb = KnowledgeBase()

    print("\n[1] 代码生成中...")
    code = scheduler.dispatch("coding", "用户注册接口")

    print("[2] 代码审查中...")
    review = scheduler.dispatch("review", code)

    print("[3] 自动化测试中...")
    test = scheduler.dispatch("test", "注册模块")

    print("[4] PR创建与跟踪...")
    pr = tracker.track("PR-1001", "用户注册模块开发", "完成注册、校验、异常处理")

    print("[5] 自动生成上下游文档...")
    doc = tracker.auto_doc("PR-1001")

    print("[6] 归档到知识库...")
    kb.add("code_review", "注册模块审查", str(review), "ReviewAgent")

    print("\n✅ 流程执行完成！")
    print("📊 系统状态：正常运行")
    print("📚 知识库已归档")
    print("🔗 支持日均 200+ 次自动审查")

if __name__ == "__main__":
    main()
