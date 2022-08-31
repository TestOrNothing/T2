from .rule import *


class DataClassVisitor(WarningNodeVisitor):
    def visit_ClassDef(self, node: ClassDef):
        dataclass = True
        for func in node.__dict__["body"]:
            if dataclass:
                if func.__dict__["name"] == '__init__':
                    pass
                elif len(func.__dict__["body"]) == 1:
                    if func.__dict__["body"][0].__class__ == Return and func.__dict__["body"][0].__dict__["value"].__class__ == Attribute:
                        pass
                    elif func.__dict__["body"][0].__class__ == Assign and func.__dict__["body"][0].__dict__["targets"][0].__class__ == Attribute:
                        existe = False
                        for val in func.__dict__["args"].__dict__["args"]:
                            if val.arg == func.__dict__["body"][0].__dict__["value"].__dict__["id"]:
                                existe = True
                        if not existe:
                            dataclass = False
                    else:
                        dataclass = False
                else:
                    dataclass = False
            else:
                break
        if dataclass:
            self.addWarning(f'DataClass {node.name}', node.lineno, 'this class is storing data')


class DataClassRule(Rule):
    def analyze(self, ast):
        visitor = DataClassVisitor()
        visitor.visit(ast)
        return visitor.warningsList()