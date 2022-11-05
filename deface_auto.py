import os
import pathlib

filename = []
data_root = pathlib.Path('/mnt/e/deface/IXI-T1/')
for item in data_root.iterdir():
  filename.append(os.path.basename(item))

for i in range(len(filename)):
    os.system('pydeface {}'.format(filename[i]))

