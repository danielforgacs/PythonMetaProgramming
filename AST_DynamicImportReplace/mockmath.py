"""
this is the mock math module we want to use
for testing. this module is used in the
"module" module. When the importer module
is run, it replaces the "math" import
with this module.
"""
print('>>> MOCK MATH IMPORTED')
