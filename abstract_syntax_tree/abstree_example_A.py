import ast

source = """
x = 2
"""

# /* exec the source as-is
module = {}
exec compile(source, '<string>', 'exec') in module
# print dir()
# print module
print(module['x'])
# /* prints 2

tree = ast.parse(source)
print
print ast.dump(tree)
# /* change all numerical constants to 8
for node in ast.walk(tree):
    print
    print node
    print node._fields

    if isinstance(node, ast.Num):
        node.n = 8

    if isinstance(node, ast.Assign):
        # print dir(node.targets[0])
        print node.targets[0]._fields
        print node.targets[0].id
        print node.targets[0].ctx
        print node.targets[0]
        print node.value
        # node.targets[0].id = node.targets[0].id + '_MODIFIED'

        for target in node.targets:
            pass
            print 'targettype:', type(target)
            target = target.id + '_modified'

print ast.dump(tree)
# /* exec the modified AST
module_changed = {}
print
print ast.dump(tree)
exec compile(tree, '<blah>', 'exec') in module_changed
print(module_changed['x'])

exec compile(tree, '<blah>', 'exec')
print x
# /* prints 8

print
print dir()
print
print [key for key, item in locals().items()]