from itertools import*
k=0
p={p for p in permutations('КАБАКА')}
p1={''.join(p) for p in permutations('КАБАКА')}
p2=[''.join(p) for p in permutations('КАБАКА')]
print(p,len(p))
print(p1,len(p1))
print(p2,len(p2))
'''
114)	Петя составляет четырёхбуквенные слова перестановкой букв слова АБАК.
При этом он избегает слов с двумя подряд одинаковыми буквами.
Сколько всего различных слов может составить Петя?
'''