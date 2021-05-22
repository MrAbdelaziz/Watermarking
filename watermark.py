import os
import subprocess
import pathlib
import re

"""                                        E-mail:
   [[[[[[[[[[[[[[[      ]]]]]]]]]]]]]]] █▀▀▀▀▀█ ▄█ ▄▄█▀▄█ █▀▀▀▀▀█
   [:::::[                      ]:::::] █ ███ █ ▄█▀█▄ ▄▀  █ ███ █
   [:::::[                      ]:::::] █ ▀▀▀ █ ▄ █ ▀  ▄▀ █ ▀▀▀ █
   [:::::[                      ]:::::] ▀▀▀▀▀▀▀ ▀ ▀ ▀ ▀ ▀ ▀▀▀▀▀▀▀
   [:::::[                      ]:::::] ▀█▀██▄▀▀▀█▀█▀▀▀ █▀ █ ▀▄▀ 
   [:::::[ CODED BY MrAbdelaziz ]:::::] ▄  ▀  ▀ ▄█▄▄ ▀██▀▄█▄█ ▀▀█
   [:::::[ Github:MrAbdelaziz   ]:::::] ▄█▄█ ▀▀ ▀▀▄█▀█▀▀▄▀▀ ▀ ▀▀ 
   [:::::[                      ]:::::] █ █▄ ▀▀▄▀▄ ▄▄ ██▄ ▀ ▀  ██
   [:::::[                      ]:::::] ▀ ▀▀▀▀▀▀█▀▄▄▀▀▀▄█▀▀▀██▀▀▀
   [:::::[                      ]:::::] █▀▀▀▀▀█ ▀▀█▄▀ ▄ █ ▀ █  ▀█
   [:::::[                      ]:::::] █ ███ █ █▀▀███▀▀▀██▀████▄
   [:::::[                      ]:::::] █ ▀▀▀ █ ██▄ ▀ ▄▄▄▄▄█ ▀  █
   [[[[[[[[[[[[[[[      ]]]]]]]]]]]]]]] ▀▀▀▀▀▀▀ ▀▀ ▀▀▀▀   ▀  ▀▀▀▀"""
   
path = pathlib.Path(__file__).parent.absolute()

files = []

for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:
            files.append(file)
         """ select certin images id = re.findall(r'\d+', file)
            if int(id[0]) >= 12:
                files.append(file)"""

for f in files:
    print(f)
    subprocess.call(f"magick composite -dissolve 10% -gravity center logo.png {f} -resize 2480x3508 {f}")
