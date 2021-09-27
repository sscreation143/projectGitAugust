d={}
for i in range(2):
    name=input('enter the names')
    marks=float(input('enter the marks'))
    d[name]=marks
v=d.values()
s=sorted(list(set(v)))[-2]
nam=[]
for key,values in d.items():
    if values==s:
        nam.append(key)
        nam.sort()
# for name in nam:
#     print(name)
print(nam)
