import time
import glob
import os
import sys

args = sys.argv

from_dir = './' + args[1] + '/'
to_dir = './' + args[1] +'_txtin/'

start = time.time()

os.makedirs(to_dir, exist_ok=True)
for path in glob.glob(os.path.join(from_dir, '*.txt')):
  with open(path,'r',encoding="utf-8") as f:
    basename = os.path.basename(path)
    data = f.readlines()
    data.insert(0, basename + '\n')
    to_path = os.path.join(to_dir, basename)

  with open(to_path, mode='w',encoding="utf-8") as f:
    f.writelines(data)

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")