file1 = open('Two_strings.txt', 'r')
Lines = file1.readlines() 

Lines2 = []
for line in Lines:
    line = line.strip()
    Lines2.append(line)
X = Lines2[0]
Y = Lines2[1]


def createtable(X,Y): 
    #create table
    m = len(X)
    n = len(Y)
    S = [[0]*(m+1) for i in range (n+1)]
    for j in range (n+1):
        for i in range (m+1):
            #fill up first row and first column
            if (j == 0 or i == 0):
                S[j][i] = max(i,j)
            #if vertical and horizontal letter is the same, increase from diagonal by 1
            elif X[i-1] == Y[j-1]:
                S[j][i] = S[j-1][i-1] + 1
            #if not same, increase from min(horizontal,vertical) by 1 as we want shortest path 
            else:
                S[j][i] = min(S[j-1][i], S[j][i-1]) + 1
    return S

def get_scs(X,Y):
#create table
    S = createtable(X,Y)
    #backtrack the table
    scs = ""
    j = len(Y)
    i = len(X)
    while j > 0 and i > 0:
        #if letter is same, append X or Y to scs and decrease i and j pointers by 1
        if X[i-1] == Y[j-1]:
            scs += X[i-1]
            j -= 1
            i -= 1
        #if horizontal counter smaller than vertical counter, append letter from horizontal string, and decrease horizontal pointer by 1 
        elif S[j][i-1] < S[j-1][i]:
            scs += X[i-1]
            i -= 1
        #if vertical counter smaller, append vertical string letter; or if they are the same, append vertical string letter first (in this case does not matter which string to append first)
        else:
            scs += Y[j-1]
            j -= 1
    while j > 0:
        scs += Y[j-1]
        j -= 1
    while i > 0:
        scs += X[i-1]
        i -= 1
    
    #reverse slicing to reverse string -> sequence[start:stop:step]
    scs = scs[::-1]
    return scs

scs = get_scs(X,Y)
print(scs)