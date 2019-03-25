fin = open("info.txt", "r")
lines = fin.readlines()
    
def temp_read():
    i = 0
    num = ""
    index = lines[1].find('"Temperature":"')+15
    while lines[1][index+i] != '"':
        num += (lines[1][index+i])
        i+=1
    return (float(num))


def humi_read():
    i = 0
    num = ""
    index = lines[1].find('"Humidity":"')+12
    while lines[1][index+i] != '"':
        num += (lines[1][index+i])
        i+=1
    return (float(num))

def pres_read():
    i = 0
    num = ""
    index = lines[1].find('"Pressure":"')+12
    while lines[1][index+i] != '"':
        num += (lines[1][index+i])
        i+=1
    return (float(num))

def tilt_read():
    i = 0
    num = ""
    index = lines[1].find('"Tilt":"')+8
    while lines[1][index+i] != '"':
        num += (lines[1][index+i])
        i+=1
    return (float(num))




