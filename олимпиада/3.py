s=str(input())
t=int(input())
n=int(input())
k=0
for i in str(s):
    a=int(i,32)-9
    if a<=15:
        k+=(a%3)
    if 15<a<20:
        k+=(a%4)
    if 19<a<23:
        k+=(a%3)
    if 22<a<27:
        k+=(a%3)
print(k*n)

