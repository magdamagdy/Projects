from compression import *
def caller5():
    #with open(filename, "r") as f:
     #   result1 = f.readlines()
    #result1 =filename
    #print (result1)
    dictionary2 = {i: chr(i) for i in range(1, 123)}
    last2 = 256

    result2 = []
    p = result1.pop(0)
    result2.append(dictionary2[p])

    for c in result1:
        if c in dictionary2:
            entry = dictionary2[c]
        result2.append(entry)
        dictionary2[last2] = dictionary2[p] + entry[0]
        last2 += 1
        p = c


    with open(filename2 , 'w') as f2:
        for i in result2:
            f2.write("%s" % i)


    return filename2