"""
this module shows how to replace an import in
a module dynamically. This module "imports"
the "module" module, replaces the "math"
import with "mockmath" and runs it.

For the imported and tweaked module to
be available here as an actual module,
the AST is executed in a new dynamically
created module's namespace.
"""

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
    # The module is read as text for the update.
    sourcecode = filehandler.read()


# The imported module's code is parsed to an AST
source_ast = ast.parse(sourcecode)

# A new replacement AST node is created
# with the mock modules names.
newimport = ast.Import()
newimport.names = [
    ast.alias(name='mockmath', asname='math')
]


class ImportSwapper(ast.NodeTransformer):
    """
    This nodetransformer replaces the
    "math" import node with the new
    import node that imports "mockmath"
    """
    def visit_Import(self, node):
        ast.copy_location(newimport, node)
        return newimport


tweakedsource_ast = ImportSwapper().visit(source_ast)

# The tweaked AST is compiled
compiled = compile(tweakedsource_ast, 'tweakedmodule', 'exec')


tempnamespace = {}

exec(compiled, tempnamespace)

tweakedmodule = types.ModuleType('tweakedmodule')

for item, value in tempnamespace.items():
    if item[0] == '_':
        continue
    # print(item)
    setattr(tweakedmodule, item, value)

print(tweakedmodule.math)
