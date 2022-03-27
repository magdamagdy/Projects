import time
from stack import *
#start=time.time()
#filename = 'nmnm.xml'

filename2 = 'text2.xml'
stack = stack_imp()
error_list = []
def open_file(filename):
    with open(filename,"r") as f:
        transcript = f.readlines()
        return transcript


def clear(filename2):
    with open(filename2,'w') as f:
        pass


def write (filename2,line):
    with open(filename2,"a") as f:
        f.write(line)


def check_error(transcript):
    word=''
    word2=''
    new_line = ''
    index_counter = -1

    for line in transcript:

        index_counter+=1
        if index_counter == 0:
            #index = line.rfind('>')
            #index+=1
            #line = line[:index] +'\n'+ line[index:]

            if line[len(line)-1] =='\n':
                last_letter = line[len(line) - 2]
                last_letter_index=len(line) - 2
            else:
                last_letter = line[len(line) - 1]
                last_letter_index = len(line) - 1
            #print(last_letter)
        i=0
        #for i in range(len(line)):
        while i < len(line):
            if line[i] == '<' and line[i+1] !='/'  and line[i+1] !='!' and line[i+1]!='?':  #open tag
                # modifing the old line
                if last_letter != '>' or (i!=0 and line[i-1] !='>' and line[i-1] !=' '):
                    ### missing case #####
                    t = stack.get_top()
                    if t != None:
                        #print(f'pop: {stack.get_top()}')
                        stack.pop()
                        error_list.append((t, index_counter-1, last_letter_index))
                        new_line = new_line + ('</' + t + '>' + '\n')
                        #write(filename2, '</' + t + '>')
                        #write(filename2,'\n')
                    #stack.push(word[:len(word) - 1])

                    ## new line
                new_line = new_line + line[i]
                #write(filename2, line[i])
                j=i
                slash_flag=0
                space_flag=0
                while line[j] !='>' :
                    if line[j] == ' ':
                        space_flag=1
                        #write(filename2, line[j])
                    if line[j] == '/' and line[j+1] == '>' and space_flag==1:
                        slash_flag=1
                        #break
                    j += 1
                    new_line = new_line + line[j]
                    #write(filename2, line[j])
                    if space_flag==0:
                        word = word + line[j]
                i = j
                space_flag=0
                if slash_flag==0:
                    stack.push(word[:len(word) - 1])
                    #print(f'push: {stack.get_top()}')
                #print(word[:len(word)-1])
                word=''
                slash_flag=0

            elif line[i] == '<' and line[i+1] =='/' :
                error_index=i
                #stack.append(line[i])
                while line[i] !='>':
                    i += 1
                    word2 = word2 + line[i]

                word2=word2[1:len(word2)-1]
                #print(word2)
                #stack.append(word)
                enter_flag = 0
                t=stack.get_top()     #opeining exists and closing is missing or wrong
                if  t==word2:
                    if index_counter != len(transcript) - 1 and stack.get_size() == 1 :  #---> (2 -> 1) missing parent
                        enter_flag = 1
                        error_list.append((word2, index_counter, error_index))

                    if t != None and enter_flag==0:
                        #print(f'pop: {stack.get_top()}')
                        stack.pop()
                        #write(filename2, '</'+word2+'>')
                        new_line=new_line+('</'+word2+'>')

                    if index_counter == len(transcript)-1 and enter_flag==0:

                        while not stack.is_empty():
                            t = stack.get_top()
                            if t !=None:
                                #print(f'pop: {stack.get_top()}')
                                stack.pop()
                                #write(filename2,'\n')
                                #write(filename2, '</' + t + '>')
                                new_line=new_line+('\n'+'</' + t + '>')
                    enter_flag=0

                else: ######################
                    if index_counter != len(transcript) - 1 and stack.get_size() == 1 or (len(transcript) == 1 and stack.get_size() == 1 ):
                        enter_flag = 1
                        error_list.append((word2, index_counter, error_index))
                    if t != None and enter_flag==0:
                        #write(filename2, '</' + t + '>')
                        new_line = new_line +('</' + t + '>')
                        error_list.append((word2,index_counter,error_index))  ### t --> word2
                        #print(f'pop: {stack.get_top()}')
                        stack.pop()
                    if index_counter == len(transcript)-1 and enter_flag==0:

                        while not stack.is_empty():
                            t = stack.get_top()
                            if t !=None:
                                #print(f'pop: {stack.get_top()}')
                                stack.pop()
                                # write(filename2,'\n')
                                # write(filename2, '</' + t + '>')
                                new_line=new_line+('\n'+'</' + t + '>')
                    enter_flag=0
                    #print(error_list)
                word2=''
            else:
                #write(filename2, line[i])
                new_line=new_line+line[i]
            i += 1
        if index_counter !=0:
            last_letter = line[len(line) - 2] #---->
            last_letter_index = len(line) - 2
            #print(last_letter)
        write(filename2,new_line)
        new_line=''

        #write(filename2,'\n')
def caller (filename):
    transcript = open_file(filename)
    #print(transcript)
    clear(filename2)
    check_error(transcript)
    return filename2

#caller(filename)
if error_list==[]:
    print('NO ERRORS')
else:
    print('there is error in this file')
    print(error_list)
#end=time.time()
#print("final is in ",end-start)