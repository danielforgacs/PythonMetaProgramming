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
print(ast.dump(source_ast))


class ImportSwapper(ast.NodeTransformer):
    # def generic_visit(self, node):
    #     print(ast.dump(node))
    #     return super().generic_visit(node)

    def visit_Import(self, node):
        return node


tweakedsource_ast = ImportSwapper().visit(source_ast)
print(ast.dump(tweakedsource_ast))
# print(ROOT_DIR)
# print(ROOT_PARENT_DIR)

# import ASTSwapImport.module as module
# print(module.__file__)
# print(MODULEFILE)
# print(sourcecode)
# print(dir(ImportSwapper()))
