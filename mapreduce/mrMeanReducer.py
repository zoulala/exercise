import sys
from numpy import mat, mean, power

def read_input(file):
    for line in file:
        yield line.rstrip()


input = read_input(sys.stdin)
mapperOut = [line.split('\t') for line in input]

cumVal = 0.
cumSumSq = 0.
cumN = 0

for instance in mapperOut:
    nj = float(instance[0])
    cumN += nj
    cumVal += nj*float(instance[1])
    cumSumSq += nj*float(instance[2])
means = cumVal/cumN
varSum = (cumSumSq - 2*means*cumVal + cumN*means*means)/cumN
print("%d\t%f\t%f"%(cumN, means, varSum))
print("report:still alive",file=sys.stderr)

# cat inputFile.txt | python mrMeanMapper.py  | python mrMeanReducer.py  ## linux
# python mrMeanMapper.py < inputFile.txt | python mrMeanReducer.py  ## windows
