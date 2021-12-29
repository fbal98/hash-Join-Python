########
#Author: Faras Al kharusi
#date: 12/11/2020
########

#imports
from os import path, remove



#This function reads the file and returns a list of the lines.
#each line will be a tuple in this case
def readFile(fileName):
    listOfLines = list()
    with open(fileName, 'r') as inputFile:
        line = inputFile.readline()
        while line:
            #append line to list
            listOfLines.append(line.rstrip('\n'))
            line = inputFile.readline()

    return listOfLines


#this function appends tuple at the end of file if the file doesn't exist it creates one.
def appendToFile(fileName, theTuple):
    ##open file in append mode
    with open(fileName, 'a') as bucketFile:
        ##append tuple and newline
        bucketFile.write(theTuple)
        bucketFile.write('\n')




#This function will hash and then append to the corresponding file(buckets)
#file name is the key
def hashFunction(relation, index):
    ### f(k) = k mod N
    for r in relation:
        #check if out of range
        if index > len(r)-1 or index < 0:
            print('error table 1: the index provided is out of range')
            return

        #here is the hashing
        k = r[index]
        N = 3
        result = int(k) % N

        #formating the file name
        #so if the result of the hash is 0 I will store it into 0.txt and so on
        fileName = str(result) + '.txt'

        #here I will use the helper function I made
        #to append the tuple to the bucket file
        appendToFile(fileName, r)

#returns string with comma between elements
def formatResult(string):
    return ','.join(string)

#This function will do the hash join on relation 1 and 2
def hashJoin(relation, index1, index2):
    #to count if the are no results
    iterations = 0

    #main loop; this loops in relation 2
    #and opens the file to compare if there any matches
    #if there are any they will be printed
    #otherwise a message of empty result will be printed
    for r in relation:
        if int(index2) > len(r)-1 or index2 < 0:
            print('table 2 index is out of range')
            return

        #do the hash to get the bucket file
        k = r[index2]
        N = 3
        result = int(k) % N
        fileName = str(result) + '.txt'

        #if the path exists we will enter the comparison if not nothing will happen
        #and no result message will be printed at the end
        if path.exists(fileName):

            with open(fileName) as f:
                line = f.readline()
                while line:
                    if r[index2] == line[index1]:
                        iterations += 1
                        resultTuple = '[(' + formatResult(line.strip('\n')) + ')' + ',' + '(' + formatResult(r) + ')'
                        print(resultTuple, end='')
                        print(']')
                    line = f.readline()
    if not iterations:
        print('There are no matches')

def main():
    ###remove bucket files if any(previous run)
    if path.exists("0.txt"):
        remove("0.txt")
    if path.exists("1.txt"):
        remove("1.txt")
    if path.exists("2.txt"):
        remove("2.txt")


    ###define and initialize the relations
    relation1 = readFile('rel1.txt')
    relation2 = readFile('rel2.txt')

    ###ask for join index
    firstAttribute = input('please enter the first attribute:')
    secondAttribute = input('please enter the second attribute:')

    #hash then partition the first relation to buckets(files)
    hashFunction(relation1, int(firstAttribute)-1)

    ###now compare the then join
    hashJoin(relation2, int(secondAttribute)-1, int(firstAttribute)-1)


#the call of the main
main()
