import ast

# import randommodule

# c0 = randommodule.C()

# print dir(randommodule)
# print randommodule.__file__

# with open(randommodule.__file__, 'r') as f:
with open('randommodule.py', 'r') as f:
    code = f.read()

# print code

tree = ast.parse(code)
# print ast.dump(tree)
print
print

# print dir()
# print locals().keys()
# print

newmodule = {}
# exec(compile(tree, '<string>', 'exec')) in newmodule
exec compile(tree, '<blash>', 'exec') in newmodule
# exec compile(tree, '<string>', 'exec')

for node in ast.walk(tree):
    # print node

    if isinstance(node, ast.Str):
        # print dir(node)
        # print node.s
        node.s = 'KJHG'

# c1 = newmodule.C()
print dir()
print ast.dump(tree)
# c1 = C()
# c1 = newmodule.C()

# print dir()
print locals().keys()
# print
# print
# print type(newmodule)
# print dir(newmodule)
# print
# print
# print dir(randommodule)
