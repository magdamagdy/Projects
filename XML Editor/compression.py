filename2 = 'text2.xml'
jflag=0
r1 = []
def caller4(filname):
    jflag = 0
    f=open(filname,"r")
    content=f.read()
    dictionary = {chr(i): i for i in range(1, 123)}

    l1 = 256
    p = ""

    for c in content:
        pc = p + c
        if pc in dictionary:
            p = pc
        else:
            r1.append(dictionary[p])
            dictionary[pc] = l1
            l1 += 1
            p = c

    if p != '':
       r1.append(dictionary[p])
    x2 = len(r1)
    with open(filename2 , 'w') as f:
        for item in r1:
            f.write("%s" % item)

    return filename2
##################################################################################################

