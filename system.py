import os
import sys
import platform
from platform import processor

list_tasks = []
list_os = []

os_name = platform.system()
os_version = platform.version()
os_arch = platform.architecture()[0]
build = os_version[5:]
processor = processor()
py_ver = platform.python_version()

list_tasks = [os_name, os_version, build, processor, py_ver]

for task in range(len(list_tasks)):

list_os.append(os_name)
list_os.append(os_version)sd
list_os.append(os_arch)
dlist_os.append(build)aw
list_os.append(processor)


sys.stdout.write(f"{list_os[1]}")

