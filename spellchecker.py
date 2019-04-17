import sys

vocab = {}



#First load the frequency list from the file argument into a python list
freq = []

fd = open('freq.txt', 'r')
for line in fd.readlines():
    line = line.strip('\n')
    (f, w) = line.split('\t')
    freq.append((int(f), w))

#Then read standard input line by line
for line in sys.stdin.readlines():

#Split each line into tokens
	tokens=line.split(' ')

#For each of the tokens, see if it exists in the list
	for word in line.split(' '): 

#If it exists then just print it out, otherwise print it out with an asterix
	for word in line.split(' ')
		print('%d\t%s' % (vocab[], ))

