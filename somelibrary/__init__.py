"""
    The purpose of this __init__ script is to load a.py and b.py,
    note that __all__ handles "from somelibrary import *"
"""

from __future__ import print_function

"""
    This function will print out the value of the variable, if it exists,
    if it doesn't exist, it will print the error message it received when trying to access it
"""
def Dbg_ExamineVariable(varname):
    try:
        varValue = eval(varname)
        print('<', varname, '>=', varValue)
    except Exception as ex:
        print('An error occurred while reading variable' + varname + str(ex))



print('start of somelibrary/__init__.py')
 
import pkgutil

modules = []

# Python seems to be hard coded to look for this directory as the result of using from somelibrary import *
__all__ = []

# Note that __path__ is the absolute directory this script is in
print('__path__ is', __path__)

#%% Iterate over each python file in this script's directory
for loader, module_name, is_pkg in  pkgutil.walk_packages(__path__):
    __all__.append(module_name)
    module = loader.find_module(module_name).load_module(module_name)
    print('(loader, moudle_name, is_pkg)=',(loader, module_name, is_pkg))
    print('=====================================================')
    modules.append(module)

    # Note: interpreted as 
    #       <a variable named module name> = <module>, 
    #       e.g.,
    #       a = <module we just loaded with load_module(...)
    #       NOT
    #       <module name> = literally, module
    #       ALSO NOT
    #       (the string) 'a' = module
    #
    # I was concerned that this exec would not work in Python 3, but it seems to.

    print('Before exec...')
    Dbg_ExamineVariable(module_name)

    # This exec statement just assigns the module to a variable with the same name as the module
    exec('%s = module' % module_name)

    print('After exec...')
    Dbg_ExamineVariable(module_name)

    print('')

print('__all__ is', __all__)
print('modules is', modules)
print('end of somelibrary/__init__.py')
print('')