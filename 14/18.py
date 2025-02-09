x=int(input())
n=int(input())
s=''

while x >0:

    s=str( x%n)+s
    x//=n


print(s,s[0], len(s),sum(map(int,s)))

print(int(s,n))