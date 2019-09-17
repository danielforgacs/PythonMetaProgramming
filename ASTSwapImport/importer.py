import os
import sys
import ast
import types

ROOT_DIR = (
    os.path.dirname(
        os.path.abspath(__file__)
))
ROOT_PARENT_DIR = os.path.dirname(ROOT_DIR)
MODULEFILE = os.path.join(ROOT_PARENT_DIR, 'ASTSwapImport/module.py')

sys.path += [ROOT_PARENT_DIR]


with open(MODULEFILE, 'r') as filehandler:
    sourcecode = filehandler.read()

source_ast = ast.parse(sourcecode)
newimport = ast.Import()
newimport.names = [ast.alias(name='mockmath', asname='math')]


class ImportSwapper(ast.NodeTransformer):
    def visit_Import(self, node):
        ast.copy_location(newimport, node)
        return newimport


tweakedsource_ast = ImportSwapper().visit(source_ast)
compiled = compile(tweakedsource_ast, 'tweakedmodule', 'exec')
tempnamespace = {}
# exec(compiled)
exec(compiled, tempnamespace)

# print(math)
# print(dir())

tweakedmodule = types.ModuleType('tweakedmodule')

# print(tweakedmodule)
# print(tempnamespace.keys())

for item, value in tempnamespace.items():
    if item[0] == '_':
        continue
    # print(item)
    setattr(tweakedmodule, item, value)

print(tweakedmodule.math)
