import os
import sys

ROOT_DIR = (
    os.path.dirname(
        os.path.abspath(__file__)
))
ROOT_PARENT_DIR = os.path.dirname(ROOT_DIR)

sys.path += [ROOT_PARENT_DIR]
MODULEFILE = os.path.join(ROOT_PARENT_DIR, 'ASTSwapImport/module.py')

print(ROOT_DIR)
print(ROOT_PARENT_DIR)

import ASTSwapImport.module as module
print(module.__file__)
print(MODULEFILE)
