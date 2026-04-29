from itertools import*

k=0
for s in product('ОГЭИНФ', repeat=6):
    s=''.join(s)

    if s[0] in 'ОЭ' and s[-2:]=='НФ' and 'ИГ' in s and 'ОГЭ' not in s:
        k+=1

print(k)
