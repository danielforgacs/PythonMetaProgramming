import ast

src = """
CONST = 3

def func():
    print(CONST)
"""

code = ast.parse(src)

for node in ast.walk(code):
    if isinstance(node, ast.Num):
        node.n = 5

coobj = compile(code, filename='pyfile.py', mode='exec')

exec(coobj)

func()
