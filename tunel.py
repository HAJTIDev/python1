import random,sys,time

try:
    szerokosc=100
    x=random.randint(-1,szerokosc)
    a=int(input("agresywne czy nie ?"))
    if a==1:
        print("aby skończyć kliknij ctrl + c")
        while True:
            if x<11:
                x+=1
            elif x>szerokosc-15:
                x-=1
            else:
                x+=random.randint(-1,1)
                time.sleep(0.02)
            for i in range(szerokosc):
                if i-x<10 and i-x>0:
                    print("   ", end="")
                else:
                    print("##", end="") 
            print()
    else:
        while True:
            if x<11:
                x+=4
            elif x>szerokosc-15:
                x-=4
            else:
                x+=random.randint(-4,4)
                time.sleep(0.02)
            for i in range(szerokosc):
                if i-x<10 and i-x>0:
                    print("   ", end="")
                else:
                    print("##", end="") 
            print()

except KeyboardInterrupt:
    print("Stop")
    sys.exit()