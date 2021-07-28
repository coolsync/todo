# import 包名.模块名

# 包名.模块名.⽬标

# method 1
import my_package.mod1

my_package.mod1.print_info()

# method 2： in my_package __init__.py, set __all__, allow exported module
from my_package import *
mod1.print_info()