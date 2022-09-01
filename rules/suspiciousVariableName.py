from .rule import *


class suspiciousVariableVisitor(WarningNodeVisitor):
    def visit_Assign(self, node: Assign):
        if isinstance(node.targets[0], Name):
            if len(node.targets[0].id) == 1:
                self.addWarning('suspiciousVariableWarning',
                                node.targets[0].lineno, 'this variable is suspicious')
        elif isinstance(node.targets[0], Attribute):
            if len(node.targets[0].attr) == 1:
                self.addWarning('suspiciousVariableWarning',
                                node.targets[0].lineno, 'this variable is suspicious')


class suspiciousVariableRule(Rule):
    def analyze(self, ast):
        visitor = suspiciousVariableVisitor()
        visitor.visit(ast)
        return visitor.warningsList()
