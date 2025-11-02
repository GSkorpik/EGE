count = 0
for s in open('9-249.csv'):
  data = [int(x) for x in s.split(';')]
  d3 = [x for x in data if data.count(x) >= 3]
  dgt1 = [x for x in data if data.count(x) >= 2]
  d1 = [x for x in data if data.count(x) == 1]
  if len(d3) >= 1 and len(d1) >= 1 and sum(dgt1)/len(dgt1) > sum(d1)/len(d1):
    count += 1
print( count )