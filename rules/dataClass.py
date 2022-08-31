from .rule import *


class DataClassVisitor(WarningNodeVisitor):
    def visit_ClassDef(self, node: ClassDef):
        dataclass = True
        for func in node.body:
            if dataclass:
                if func.name == '__init__':
                    pass
                elif len(func.body) == 1:
                    if func.body[0].__class__ == Return and func.body[0].value.__class__ == Attribute:
                        pass
                    elif func.body[0].__class__ == Assign and func.body[0].targets[0].__class__ == Attribute and isinstance(func.body[0].value, Name):
                        existe = False
                        for val in func.args.args:
                            if val.arg == func.body[0].value.id:
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
