from itertools import*
k=0
p={''.join(p) for p in permutations('ЕСАУЛ') if 'ЕА' not in ''.join(p) and 'ЕУ' not in ''.join(p) and 'АЕ' not in ''.join(p) and 'АУ' not in ''.join(p) and 'УЕ' not in ''.join(p) and 'УА' not in ''.join(p)}
print(len(p))

'''
130)	Артур составляет 5-буквенные коды из букв Е, С, А, У, Л. 
Каждую букву нужно использовать ровно один раз, при этом нельзя ставить рядом две гласные. 
Сколько различных кодов может составить Артур?
'''