import csv
import itertools
import operator
from collections import defaultdict
import argparse
import difflib

parser=argparse.ArgumentParser(description="Calculate how many times combinations of genes appear together");
parser.add_argument("filename")

args=parser.parse_args()
filename=args.filename
print "Opening %r." % filename

#open the initial file and generate a file of genes together in each lesion
fileReader = csv.reader(open(filename, 'rb'), delimiter=',',skipinitialspace=True,dialect=csv.excel_tab)
lesionDict = defaultdict(list)
fileReader.next()
for row in fileReader:
  geneName = row[0]
  lesions = row[7]
  lesions=lesions.split(';')
  for lesion in lesions:
    lesionDict[lesion].append(geneName)

print lesionDict.keys()
print lesionDict.values()

lesions=lesionDict.keys()
outputfileName=filename[0:len(filename)-4]+'-genesPerLesion.csv'
f=open(outputfileName,'w')
writer=csv.writer(f)
for lesion in lesions:
  writer.writerow(lesionDict[lesion])

f.close()
#now open the file we just created and create the genes per lesion file needed for import into cytoscape
print outputfileName
fileReader = csv.reader(open(outputfileName, 'rb'), delimiter=',',skipinitialspace=True,dialect=csv.excel_tab)

genesTogetherInLesions = defaultdict(int)
pairsOfGenesTogetherInLesion= defaultdict(int)

for row in fileReader:
  row = filter(None, row)
  
  for lengthOfGroup in range(2,len(row)+1):
    for subset in itertools.combinations(row, lengthOfGroup):
      genesTogetherInLesions[subset]+=1
      if lengthOfGroup==2:
        pairsOfGenesTogetherInLesion[subset]+=1
      

sorted_genes=sorted(genesTogetherInLesions.items(), key=operator.itemgetter(1), reverse=True)
sorted_pairs=sorted(pairsOfGenesTogetherInLesion.items(), key=operator.itemgetter(1), reverse=True)
writer = csv.writer(open(filename+"-output.csv",'w'))
writer2 = open(filename+"-outputPairs.csv",'w')
for row in sorted_genes:
  writer.writerow(row)
for key,value in sorted_pairs:
  writer2.write(str(key[0])+","+str(key[1])+","+str(value)+"\n")
writer2.close()
