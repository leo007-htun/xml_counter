import time
import sys
import glob
import xml.etree.ElementTree as ET
df = []
timeout = time.time() + 3   # 5 secs from now
def animate():
    while True:
        sys.stdout.write('\rloading |')
        time.sleep(0.1)
        sys.stdout.write('\rloading /')
        time.sleep(0.1)
        sys.stdout.write('\rloading -')
        time.sleep(0.1)
        sys.stdout.write('\rloading \\')
        time.sleep(0.1)
        test = 0
        if test == 3 or time.time() > timeout:
            break
        test = test - 1
    sys.stdout.write('\rDone!     \n')

for file in glob.glob('cleaned_2/*.xml'):  
    tree = ET.parse(file)
    root = tree.getroot()
    for child in root.findall('object'):
        total_child = child.find('name').text
        # print(total_child)
        df.append(total_child)
animate()
print('\n'.join(map(str, df)))
print("Num of Eri :", df.count('Erithacus_Rubecula'))
print("Num of Peri :", df.count('Periparus_ater'))
print("Num of Pica:", df.count('Pica_pica'))
print("Num of Tur:", df.count('Turdus_merula'))













