from agent_core import CodingAgent, ReviewAgent, QAAgent
import json

class Scheduler:
    def __init__(self):
        self.coding = CodingAgent()
        self.review = ReviewAgent()
        self.qa = QAAgent()
        self.knowledge_base = []

    def dispatch(self, task_type, content):
        if task_type == "coding":
            return self.coding.generate(content)
        elif task_type == "review":
            return self.review.review(content)
        elif task_type == "test":
            return self.qa.test(content)
        else:
            return {"error": "unsupported task"}

    def auto_archive(self, task_type, result):
        record = {
            "type": task_type,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "data": result
        }
        self.knowledge_base.append(record)
        return {
            "status": "archived",
            "total": len(self.knowledge_base),
            "index": len(self.knowledge_base) - 1
        }

    def get_system_status(self):
        return {
            "coding_agent": self.coding.get_status(),
            "review_agent": self.review.get_status(),
            "qa_agent": self.qa.get_status(),
            "knowledge_base_count": len(self.knowledge_base)
        }

if __name__ == "__main__":
    scheduler = Scheduler()
    print(scheduler.dispatch("coding", "用户登录模块"))
    print(scheduler.dispatch("review", "登录代码"))
    print(scheduler.dispatch("test", "登录接口"))
