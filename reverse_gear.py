#Reverse Gear : Added by Kavin
for _ in range(int(input('Enter any range'))):
    f,b,t,d = map(int,input().split())
    d = -d
    calc = 0
    count = 0
    rem_to_ditch = 0
    while(calc!=d):
        if(calc-b<=d):
            rem_to_ditch = -d-(-calc)
            break
        calc = (calc - b) + f
        count+=1

    print(((count*(b+f))+rem_to_ditch)*(t))

