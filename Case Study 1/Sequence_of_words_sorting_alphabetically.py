# Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them
# alphabetically. Hint: In case of input data being supplied to the question, it should be assumed to be a console
# input.

def sequencesort(x):
    y = ''
    x.sort()
    for i in x:
        y = y + i
    return y


def seqjoin(x):
    i = 0
    z = ''
    for i in range(len(x)):
        print(f"{sequencesort(list(x[i]))}", end=" ")


seq = list(input("Enter words to sort: ").split())

seqjoin(seq)
