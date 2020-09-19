string = input()
index = 0
check = ""

def isAnagram(check,string):
    window = len(check)
    for i in range(0,len(string)):
        if((i+window-1)<len(string))
for _ in range(int(input())):
    direction,s = input().strip().split()
    s = int(s)
    if direction=="L":
        index = (index+s)%len(string)
    else:
        index = (index-s) % len(string)
    check += string[index]
    if(isAnagram(check,string)):
        print("YES")
    else:
        print("NO")