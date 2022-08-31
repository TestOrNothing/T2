from .rule import *
import ast


class neverReadedVisitor(WarningNodeVisitor):
    def visit_FunctionDef(self, node: FunctionDef):
        unusedVars = {}
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


class neverReadedRule(Rule):
    def analyze(self, ast):
        visitor = neverReadedVisitor()
        visitor.visit(ast)
        return visitor.warningsList()
