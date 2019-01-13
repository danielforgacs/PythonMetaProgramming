import ast


class MyTransformer(ast.NodeTransformer):
    def generic_visit(self, node):
        return super().generic_visit(node)

    def visit_Str(self, node):
        return ast.Str(node.s.upper())

    def visit_Num(self, node):
        node.n = 123
        return node

    def visit_BinOp(self, node):
        node.op = ast.Sub()
        node.left = ast.Num(0)
        return node

    def visit_FunctionDef(self, node):
        node = self.generic_visit(node)
        node.name = 'HeyFunc'
        node = ast.FunctionDef(
            name='blabla',
            args=ast.arguments(
                args=[],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[]),
            body=node.body,
            decorator_list=[],
        )
        return node

node = ast.parse("""
def bad_func_name():
    print('this func called.')
    return 5+1
""")

MyTransformer().visit(node)

ast.fix_missing_locations(node)

comp = compile(node, '', 'exec')
exec(comp)

try:
    print('bad_func_name()', bad_func_name())
except:
    pass

try:
    print('HeyFunc()', HeyFunc())
except:
    pass

try:
    print('blabla()', blabla())
except:
    pass
