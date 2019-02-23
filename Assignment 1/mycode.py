from collections import Counter

def readData(filename):
  with open('categories.txt') as f:
    dataset = f.readlines()
    dataset = [x.strip() for x in dataset]
    dataset = [x.split(';') for x in dataset]
    dataset = [item for sublist in dataset for item in sublist]
  return dataset

def countfreq(dataset):
  '''
  dict1={}
  for a in dataset:
    if a in dict1:
      dict1[a] +=1
    else:
      dict1[a]=1
  print(dict1)'''
  counter= dict([(i, dataset.count(i)) for i in set(dataset)])
  return counter
  
def freq1itemset(dict1,support):
  file  = open('patterns.txt', 'w')
  for x,y in dict1.items():
    if y>support:
      file.write(str(y)+':')
      file.write(x+'\n')
  
def main():
  dataset = readData('categories.txt')
  dict1 = countfreq(dataset)
  support= 771
  freq1itemset(dict1,support)
main()