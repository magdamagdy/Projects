from drawUpdated import *
#no_seg=[]
#p=[]
#memory=[]
#process=[]
def holes_map(start_add,size,total_size):
    #startadd=[]
    #size=[]
    #total_size=t
    print ('start add',start_add)
    print ('size',size)
    print ('mem size',total_size)

    count_oldp=0
    memory=[]
    flag =0
    i=0
    j=0
    while i<len(start_add):
    #for i in range(0,len(start_add)):
        #make holes map (name,address,size)

        if j<len(start_add):
            if (j)!=len(start_add)-1 and start_add[j]+size[j]==start_add[j+1] :
                memory.append((i, start_add[j], size[j]+size[j+1], 'h'))
                #i+=1
                flag=1
            elif flag==0:
                memory.append((i,start_add[j],size[j],'h'))


        if i==0 and start_add[i] !=0:
            memory.append((count_oldp,0,start_add[i],'o'))
            count_oldp += 1
        if i==len(start_add)-1:
            memory.append((count_oldp,start_add[i] + size[i],total_size-(start_add[i] + size[i]),'o'))
            count_oldp += 1
        elif (start_add[i] + size[i])<start_add[i+1]:
            memory.append((count_oldp,start_add[i] + size[i],start_add[i+1]-(start_add[i] + size[i]),'o'))
            count_oldp += 1
        if flag==1:
            j+=1
            flag=0
        i+=1
        j+=1
    memory = sorted(memory, key=lambda k: [k[1], k[0], k[2],k[3]])
    print("mem",memory)
    return memory #ADDED



def process_map(p,no_seg,name,size): #inputs       #function to take the input process attributes:noofsegment,size,name bs shayleen al attributes delwa2ty
    #process_no=0  #name---> p []  no ---> num of seg []  name --> name of seg[] size --> size of seg[]
    #p=[6,7] #num of procces
    #no_seg=[2,1]
    #name=['code','stack','data']
    #size=[5,5,10]
    print('p',p)
    print ('no_seg',no_seg)
    print('arr of names',name)
    print('size',size)
    process=[] #list for the input processes
    count=0 #variable to make the loop iterate on all segments badal j
      #(process_no,name,size)
    for i in range(0,len(no_seg)):
        for j in range(0,no_seg[i]): # i no of process and j no of segment
            process.append((i,j,name[i][j],size[i][j],p[i]))
            #process.append((i,j,name[count],size[count],p[i])) #f'P{i}' is a concatination method between leter p and integer i
            #count +=1
    return process

memory1=holes_map()
memory2=[list(ele) for ele in memory1]
print("new memory:")
print(memory2)
process2=process_map()
process=[list(ele) for ele in process2]
print("process array:")
print(process)

no_seg=[2,1]#segments each process [from GUI]
p=[6,7]#from gui


def ALLOCATION_FIRST_FIT(): #inputs      
    ERROR =[]#rturned from fn 
    COUNT_SEQ = 0
    #p=[6,7,8]#from gui
    #number_of_process = 1 # from GUI
    for j in  range(0,len(no_seg)) :#process
        for k in range (0,len(process)):#segments of all process
          for i in range(0,len(memory2)-1): # memory
             if process[k][0]==j : #segments of process j 
                if memory2[i][3]=='h' and process[k][3] <= memory2[i][2]: #check for hole in memory #process[k][3]size sgment
                    starting_add = memory2[i][1]
                    memory2.insert(i,[process[k][2],starting_add,process[k][3],'P'+str(process[k][4])])
                    memory2[i+1][1]+=process[k][3]#update starting address of hole
                    memory2[i+1][2]-=process[k][3]#update size of hole
                    COUNT_SEQ+=1 #process[k][2]name of sgment  
                    break
        print("count_seq=")
        print(COUNT_SEQ)
        if COUNT_SEQ == no_seg[j] :#check if all segments of this process is allocated
            COUNT_SEQ = 0 
             #fit allocation
            continue
        else :
            ERROR.append(p[j])
            COUNT_SEQ = 0 
            print("gena hena")
            DEALLOCATION(p[j],'P')# process doesn't fit
    return (ERROR) 
   
def ALLOCATION_BEST_FIT(): #inputs       
    ERROR =[] 
    COUNT_SEQ = 0
    FLAG_DONE = 0 
    HOLES_ARRAY=[]
    for v in range(0,len(memory2)):
        if(memory2[v][3]=='h'):
          HOLES_ARRAY.append(tuple(memory2[v]))
    HOLES_ARRAY =sorted(HOLES_ARRAY, key=lambda k: [k[2], k[0], k[1],k[3]])
    #for loop memory w a5od alli fehom nrtb holes de 7asb alsize
    for j in  range(0,len(no_seg)) :#process
        for k in range (0,len(process)):#segments of all process
          for i in range(0,len(HOLES_ARRAY)): # memory
             if process[k][0]==j : #segments of process j 
                if   process[k][3] <= HOLES_ARRAY[i][2]: #check for hole in memory #process[k][3]size sgment
                    #UPDATE_HOLES_ARRAY
                    FLAG_DONE = 1
                    SAVED_SIZE = HOLES_ARRAY[i][2]
                    SAVED_add = HOLES_ARRAY[i][1]
                    R = list(HOLES_ARRAY[i])
                    R[2] = R[2]-process2[k][3] #update size
                    R[1] = R[1]+process2[k][3] #update starting_address 
                    z = tuple(R)
                    HOLES_ARRAY.insert(i,z)
                    HOLES_ARRAY.pop(i+1)
                    
                    #UPDATE_IN_MEMORY
                    for E in range (0,len(memory2)):
                        if (memory2[E][3]=='h') and (memory2[E][1]==SAVED_add) and (memory2[E][2]==SAVED_SIZE) :
                            starting_add = memory2[E][1]
                            memory2.insert(E,[process[k][2],starting_add,process[k][3],'P'+str(process[k][4])])
                            memory2[E+1][1]+=process[k][3]#update starting address of hole
                            memory2[E+1][2]-=process[k][3]#update size of hole
                            COUNT_SEQ+=1 #process[k][2]name of sgment  
                            break
                    if FLAG_DONE == 1 : 
                        FLAG_DONE = 0
                        #resorting holes array for the next loop
                        HOLES_ARRAY =sorted(HOLES_ARRAY, key=lambda k: [k[2], k[0], k[1],k[3]])
                        break
                    else : #complete searching for hole  
                        continue   
        if COUNT_SEQ == no_seg[j] :
            COUNT_SEQ = 0 
             #fit allocation
            continue
        else :
            ERROR.append(p[j])
            COUNT_SEQ = 0 
            DEALLOCATION(p[j],'P')# process doesn't fit allocation
            #DEALLOCATE SEGMENTS OF PROCESS J 
    return (ERROR)
