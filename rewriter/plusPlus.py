from . rewriter import *
import ast 


class PlusPlusTransformer(NodeTransformer):
    def visit_Assign(self, node: Assign):
        target = node.targets[0]
        if isinstance(node.value, BinOp):
            binop = node.value
            left = binop.left
            right = binop.right
            op = binop.op
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