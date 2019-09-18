import ast

code = """import sys

class C(object):
    def __init__(self):
        pass
        print('original')
"""

tree = ast.parse(code)
newmodule = {}
comp = compile(tree, '<blash>', 'exec')

exec(comp)

for node in ast.walk(tree):
    if isinstance(node, ast.Str):
        node.s = 'KJHG'

print(ast.dump(tree))
