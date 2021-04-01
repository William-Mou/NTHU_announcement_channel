import os 
import time
print("run.py")
Token = os.environ.get('TELEPOT_TOKEN')
print(Token)
for f in os.listdir("/usr/src/app/crawler"):
    print(f)
    if f.endswith(".py"):
        print("Excute : python " + f)
        os.system("python crawler/" + f)

