import os
import pathlib

#WSL Ubuntu 환경에서 pydeface 자동화
#Pydeface, FSL 설치 필요

filename = []
data_root = pathlib.Path('/mnt/e/deface/IXI-T1/') #경로 설정
for item in data_root.iterdir():
  filename.append(os.path.basename(item)) #파일명만 추출

for i in range(len(filename)):
    os.system('pydeface {}'.format(filename[i]))  #pydeface 실행
