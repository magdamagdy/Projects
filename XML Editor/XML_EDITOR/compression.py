filename2 = 'text2.xml'
jflag=0
result1 = []
def caller4(filname):
    jflag = 0
    f=open(filname,"r")
    content=f.read()
    dictionary = {chr(i): i for i in range(1, 123)}

    last = 256
    p = ""

    for c in content:
        pc = p + c
        if pc in dictionary:
            p = pc
        else:
            result1.append(dictionary[p])
            dictionary[pc] = last
            last += 1
            p = c

    if p != '':
       result1.append(dictionary[p])
    x2 = len(result1)
    with open(filename2 , 'w') as f:
        for item in result1:
            f.write("%s" % item)

    return filename2
##################################################################################################

