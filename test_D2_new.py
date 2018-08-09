import os
import time
import shutil

get_path = os.getcwd()
print(get_path)
copyfile = get_path+"/configure/d2_new_testconfig.ini"
srcfile = get_path+"/configure/testconfig.ini"
os.remove(srcfile)
time.sleep(1)
shutil.copy(copyfile, srcfile)