'''
Pentru RadixSort Acesta este facut pt orice baza naturala deci va trebui introdusa baza in citirea din fisiere (R = radix)



'''

f = open("teste.txt")
g = open("output.txt","w")

import random
from time import perf_counter

def RadixSort():
    global vector,radix;
    impartitor = 1
    max = vector[0]
    for x in vector:
     if x > max:
         max = x

    lungima_maxima = len(str(max))
    lungime = 0
    while lungime < lungima_maxima:
        d = dict()
        for x in vector:
            nr = (x//impartitor)%radix
            if nr in d.keys():
                d[nr].append(x)
            else:
                d[nr] = [x]

        impartitor *= radix
        vector = []
        for index in range(radix):
            if index in d.keys():
                for element in d[index]:
                    vector.append(element)
        lungime += 1
def CountingSort():
    global vector
    max = vector[0]
    for x in vector:
        if x > max:
            max = x
    count = [0] * (max+1)
    for x in vector:
        count[x] += 1
    for index in range(1,max+1):
        count[index] += count[index-1]
    out = [0]*len(vector)
    for index in range(max,0,-1):
        count[index] = count[index-1]
    count[0] = 0;
    for x in vector:
        poz = count[x]
        out[poz] = x
        count[x]+=1
    vector = out
def MergeSort():
    global vector
    mergeSort(vector)
def mergeSort(vector):
    if len(vector) > 1:

        # Finding the mid of the vectoray
        mid = len(vector) // 2

        # Dividing the vectoray elements
        L = vector[:mid]

        # into 2 halves
        R = vector[mid:]

        # Sorting the first half
        mergeSort(L)

        mergeSort(R)

        i = 0
        j = 0
        k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                vector[k] = L[i]
                i += 1
            else:
                vector[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            vector[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            vector[k] = R[j]
            j += 1
            k += 1
def InsertSort():
    global vector
    for i in range(len(vector)):
        j =i
        while j>0 and vector[j-1] > vector[j]:
            vector[j-1],vector[j] = vector[j],vector[j-1]
            j = j-1
def ShellSort():
    global vector
    gap = len(vector)//2
    while gap > 0:
        j = gap
        while j < len(vector):
            i = j - gap
            while i >= 0:
                if vector[i + gap] > vector[i]:

                    break
                else:
                    vector[i + gap], vector[i] = vector[i], vector[i + gap]
                i = i - gap
            j += 1
        gap = gap // 2

def IsSorted():
    global vector
    for index in range (1,len(vector)):
        if vector[index] < vector[ index-1]:
            return False
    return True

def randomVector(N,M):
    v =[]
    for i in range(N):
        v.append(random.randint(0,M))
    return  v


sorts = [RadixSort,MergeSort,ShellSort,InsertSort,CountingSort]

s = f.readline()
NrTeste = int(s[2])
for index in range(NrTeste):
    g.write(f"Testul cu numarul : {index+1}\n")
    print(f"Testul cu nr {index+1}")
    s = f.readline().split()
    N = int(s[1])
    M = int(s[3])
    radix = int(s[5])
    vector = randomVector(N,M)
    for sort in sorts:
        time_start = perf_counter()
        sort()
        time_stop = perf_counter()
        g.write(f"{sort}:{time_stop - time_start} a sortat? {IsSorted()}\n")

