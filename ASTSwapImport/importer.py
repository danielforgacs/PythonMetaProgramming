import os
import sys
import ast

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
compiled = compile(tweakedsource_ast, '', 'exec')
exec(compiled)
