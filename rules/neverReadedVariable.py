from .rule import *


def storeOrLoad(node: Name, unused_nodes):
    if isinstance(node.ctx, Store):
        unused_nodes[node.id] = node.lineno
    elif isinstance(node.ctx, Load):
        if node in unused_nodes:
            del unused_nodes[node.id]


class neverReadedVisitor(WarningNodeVisitor):
    def visit_FunctionDef(self, node: FunctionDef):
        unused_nodes = {}
        if node.name != '__init__':
            for line in node.body:
                if isinstance(line, Assign):
                    for target in line.targets:
                        storeOrLoad(target, unused_nodes)
                if isinstance(line, AugAssign):
                    storeOrLoad(line.target, unused_nodes)
                if isinstance(line, Return):
                    if isinstance(line.value.left, Name):
                        storeOrLoad(line.value.left, unused_nodes)
                    if isinstance(line.value.right, Name):
                        storeOrLoad(line.value.right, unused_nodes)

            for lineno in unused_nodes.values():
                self.addWarning('neverReadedWarning', lineno,
                                'this variable is never readed!')


class neverReadedRule(Rule):
    def analyze(self, ast):
        visitor = neverReadedVisitor()
        visitor.visit(ast)
        return visitor.warningsList()
