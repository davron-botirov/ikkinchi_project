# Botirov Davronbek
import os
os.system('cls')
os.system('color 2')

sardor,buvi  = map(int, input().split())
if sardor >= buvi:
    print(-1)
    quit()

if buvi // 2 < sardor:
    print(-1)
    quit()

def ortacha_yosh( sardor,buvi):
    yosh = 0
    while sardor != buvi // 2:
        sardor += 1 
        buvi += 1
        yosh += 1
    return yosh

jami = ortacha_yosh( sardor,buvi)
print(jami + 1)
 