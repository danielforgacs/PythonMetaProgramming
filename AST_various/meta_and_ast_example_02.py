import ast

SOURCE = """
import dis

def func(this=None):
    print('YAAAAAH')

    return 5


K = type('K', (object,), {'a': 'x'})
# print(dir(K))
# print(K.__dict__.keys())

# print('\\n\\n')

K.BLABLA = BLABLA
"""


syntree = ast.parse(SOURCE, 'alskdfh', 'exec')
print(syntree)

for node in ast.walk(syntree):
    if isinstance(node, ast.FunctionDef):
        print(node.name)
        node.name = 'BLABLA'


print(ast.dump(syntree))


sourcecomp = compile(syntree, 'akjhf.py', 'exec')
exec(sourcecomp)

dis.dis(sourcecomp)

BLABLA()


k = K()
k.BLABLA() == K.BLABLA(k)
K.BLABLA()
print(globals()['K'].__dict__['BLABLA']())
print(globals()['k'].__dict__)


print(dir(globals()['K']))
