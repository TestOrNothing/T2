from .rule import *


class suspiciousVariableVisitor(WarningNodeVisitor):
    def visit_Name(self, node: Name):
        if len(node.id) == 1:
            self.addWarning('suspiciousVariableWarning', node.lineno,
                            'this variable is suspicious!')


class suspiciousVariableRule(Rule):
    def analyze(self, ast):
        visitor = suspiciousVariableVisitor()
        visitor.visit(ast)
        return visitor.warningsList()
