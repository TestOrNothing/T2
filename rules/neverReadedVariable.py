from .rule import *
import ast


class neverReadedVisitor(WarningNodeVisitor):
    def __init__(self):
        super().__init__()
        self.functionLines = []
        self.unusedVars = {}

    def visit_FunctionDef(self, node: FunctionDef):
        unusedVars = {}
        self.functionLines.append((node.lineno, node.end_lineno))
        for child in ast.walk(node):
            if isinstance(child, ast.Name):
                if child.id not in unusedVars:
                    unusedVars[child.id] = child.lineno
                if isinstance(child.ctx, ast.Load):
                    if child.id in unusedVars.keys():
                        del unusedVars[child.id]

        for var in unusedVars.values():
            self.addWarning('neverReadedWarning', var,
                            'this variable is never readed')

    def visit_Name(self, node: Name):
        for funct in self.functionLines:
            if node.lineno >= funct[0] and node.lineno <= funct[1]:
                return
        if node.id not in self.unusedVars:
            self.unusedVars[node.id] = node.lineno
        if isinstance(node.ctx, ast.Load):
            if node.id in self.unusedVars.keys():
                del self.unusedVars[node.id]

    def sendNameWarnings(self):
        for var in self.unusedVars.values():
            self.addWarning('neverReadedWarning', var,
                            'this variable is never readed')


class neverReadedRule(Rule):
    def analyze(self, ast):
        visitor = neverReadedVisitor()
        visitor.visit(ast)
        visitor.sendNameWarnings()
        return visitor.warningsList()
