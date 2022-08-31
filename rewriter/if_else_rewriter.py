from .rewriter import *


class IfElseTransformer(NodeTransformer):
    def visit_If(self, node):
        NodeTransformer.generic_visit(self, node)
        statements = node
        if isinstance(node.orelse[0], Pass):
            # el body puede ser una lista de statement
            statements.orelse = []
        return statements


class IfElseRewriterCommand(RewriterCommand):
    def apply(self, ast):
        new_tree = fix_missing_locations(IfElseTransformer().visit(ast))
        return new_tree
