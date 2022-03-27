from compression import *
def caller5():
    #with open(filename, "r") as f:
     #   r1 = f.readlines()
    #r1 =filename
    #print (r1)
    dictionary2 = {i: chr(i) for i in range(1, 123)}
    l2 = 256

    r2= []
    p = r1.pop(0)
    r2.append(dictionary2[p])

    for c in r1:
        if c in dictionary2:
            entry = dictionary2[c]
        r2.apend(entry)
        dictionary2[l2] = dictionary2[p] + entry[0]
        l2 += 1
        p = c


    with open(filename2 , 'w') as f2:
        for i in r2:
            f2.write("%s" % i)


    return filename2