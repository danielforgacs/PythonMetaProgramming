import ast


SOURCE = """
classes = ('CA', 'CB', 'CC')

def demofunc(this=None):
    return 5

for cls in classes:
    clsdict = {'funcy': func}
    globals()[cls] = type(cls, (), clsdict)
"""

sourceast = ast.parse(SOURCE)

for node in ast.walk(sourceast):
    if isinstance(node, ast.FunctionDef):
        node.name = 'func'

compsource = compile(sourceast, 'fakemodule.py', 'exec')
exec(compsource)


a = CA()
b = CB()
b = CC()
assert a.funcy() == 5
assert b.funcy() == 5
assert b.funcy() == 5
