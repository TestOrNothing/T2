from . rewriter import *
import ast 


class PlusPlusTransformer(NodeTransformer):
    def visit_Assign(self, node: Assign):
        target = node.__dict__["targets"][0]
        if isinstance(node.__dict__["value"], BinOp):
            binop = node.__dict__["value"]
            left = binop.__dict__["left"]
            right = binop.__dict__["right"]
            op = binop.__dict__["op"]
            if isinstance(op, Add) and (isinstance(left, Name) or isinstance(right, Name)) and ((isinstance(left, Constant) or isinstance(right, Constant))):
                if isinstance(left, Name):
                    new = AugAssign(target, Add(), right)
                else:
                    new = AugAssign(target, Add(), left)
                return new
        return node



class PlusPlusRewriterCommand(RewriterCommand):
    def apply(self, ast):
        new_tree = fix_missing_locations(PlusPlusTransformer().visit(ast))
        return new_tree