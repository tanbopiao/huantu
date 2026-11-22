"""圜土（HUANTU）· 高危隔离沙箱

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：高危隔离沙箱。

边界：本件为算子骨架 v0——接口先立、实现随进化轮补齐；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Huantu:
    """圜土（HUANTU）算子骨架 v0。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "HUANTU"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "huantu",
            "cn": "圜土",
            "code": self.CODE,
            "duty": "高危隔离沙箱",
            "mingwen": "闭邪于内，清白于外",
            "anchor": self.ANCHOR,
        }

    def isolate(self, fn, args):
        """高危调用入圜土执行，闭邪于内（骨架桩：实现随进化轮补齐）。"""
        raise NotImplementedError("HUANTU.isolate 骨架桩，候进化轮补齐")

    def check_escape(self, event):
        """越界事件核验，逾圜必报（骨架桩：实现随进化轮补齐）。"""
        raise NotImplementedError("HUANTU.check_escape 骨架桩，候进化轮补齐")
