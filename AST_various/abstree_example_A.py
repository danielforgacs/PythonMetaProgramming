import ast

source = """
x = 2
"""

module = {}
compA = compile(source, '<string>', 'exec')
exec(compA)

tree = ast.parse(source)
print(ast.dump(tree))
for node in ast.walk(tree):
    print(node)
    print(node._fields)

    if isinstance(node, ast.Num):
        node.n = 8

    if isinstance(node, ast.Assign):
        print(node.targets[0]._fields)
        print(node.targets[0].id)
        print(node.targets[0].ctx)
        print(node.targets[0])
        print(node.value)

        for target in node.targets:
            pass
            print('targettype:', type(target))
            target = target.id + '_modified'

print(ast.dump(tree))
module_changed = {}
print(ast.dump(tree))
compB = compile(tree, '<blah>', 'exec')
exec(compB)

exec(compile(tree, '<blah>', 'exec'))
print(x)

print(dir())
print([key for key, item in locals().items()])
