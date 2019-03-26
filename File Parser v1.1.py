fin = open('info.txt', 'r')
lines = fin.readlines()

def file_read(lookfor):
    i = 0
    num = ""
    index = lines[1].find('"'+lookfor+'":"')+len(lookfor)+4
    #finds the index of a string, adds the length of the string to get the index of the character that follows
    while lines[1][index+i] != '"':
        num += (lines[1][index+i])
        #stores all values after : and within "  " into a string
        i+=1
    return (float(num))
    #returns a float for numerical operations
