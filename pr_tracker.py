import json
from datetime import datetime

class PRTracker:
    def __init__(self):
        self.pr_list = []
        self.change_log = []

    def track(self, pr_id, title, content):
        item = {
            "pr_id": pr_id,
            "title": title,
            "content": content,
            "update_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.pr_list.append(item)
        self.change_log.append({
            "action": "create",
            "pr": pr_id,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        return item

    def get_relation(self, pr_id):
        return {
            "pr_id": pr_id,
            "upstream": ["用户中心", "权限服务"],
            "downstream": ["前端页面", "数据统计"],
            "affect_modules": ["登录", "鉴权"]
        }

    def auto_doc(self, pr_id):
        info = self.get_relation(pr_id)
        doc = f"""
自动生成文档
PR-ID: {pr_id}
上游依赖: {info['upstream']}
下游影响: {info['downstream']}
影响模块: {info['affect_modules']}
文档生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""
        return doc

    def history(self):
        return {
            "total_pr": len(self.pr_list),
            "total_change": len(self.change_log),
            "list": self.pr_list
        }
