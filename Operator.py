# a=str(input("enter the comma seprested value"))
# b=a.split(",")
# li=[]
# for i in b:
#     d=li.append(int(i))
# z = max(d)
# while max(d) == z:
#     li.remove(max(li))

# print( max(li))




# i = int(input())
# lis = list(map(int,input().strip().split()))[:i]
# print(lis)
# z = max(lis)
# while max(lis) == z:
#     lis.remove(max(lis))

# print( max(lis))



a=str(input("enter the comma sepreated value"))
b=a.split(",")
li=[]
for i in b:
    d=li.append(int(i))
e=sorted(li)[-2]
print(e)
print(b)
print(a)


# l=[5,8,2,9,4,10,7]
# for j in range(3):
#   max=l[0]
#   for i in l:
#     if i>max: max=i
#   if j==2: print(max)
#   else: l.remove(max)