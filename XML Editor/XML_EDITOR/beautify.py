from stack import *
from mini import *
import time

#start=time.time()
#filename = "D:/Maro/assignments/data structure xml/data/data.adj.xml"
#filename = "xml.txt"  #before minify

filename2 = 'text2.xml'  #final

stack = stack_imp()

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


def format(transcript):
    new_line = ''
    word = ''
    word2=''
    tab_flag=0

    for line in transcript:
        i=0

        while i<len(line):
            # if line[i] == '>' and line[i+1] =='<' :  #and line[i+2]!='/'
            #     new_line+='\n'
            #     tab_flag=1

            if line[i] == '<' and line[i + 1] != '/' and line[i + 1] != '!' and line[i + 1] != '?':  # open tag <to>gg</to><>''</>
                if line[i-1] == '>' and i!=0:
                    new_line+='\n'
                slash_flag = 0
                space_flag = 0
                j = i
                size=stack.get_size()
                while size>0:
                    new_line+='\t'
                    size-=1
                new_line = new_line + line[i]
                while line[j] != '>':
                    if line[j] == ' ':
                        space_flag = 1
                        # write(filename2, line[j])
                    if line[j] == '/' and line[j + 1] == '>' and space_flag == 1:
                        slash_flag = 1
                        # break
                    j += 1
                    new_line = new_line + line[j]
                    # write(filename2, line[j])
                    if space_flag == 0:
                        word = word + line[j]
                i = j
                space_flag = 0
                if slash_flag == 0:
                    stack.push(word[:len(word) - 1])
                    #print(f'push: {stack.get_top()}')
                # print(word[:len(word)-1])
                word = ''
                slash_flag = 0

            elif line[i] == '<' and line[i + 1] == '/':  # closed tag  <to>gg</to><>''</>
                if line[i-1] == '>':
                    new_line+='\n'
                    tab_flag=1
                while line[i] != '>':
                    i += 1
                    word2 = word2 + line[i]

                word2 = word2[1:len(word2) - 1]
                t = stack.get_top()  # opeining exists and closing is missing or wrong
                if t == word2:
                    if t != None :
                        #print(f'pop: {stack.get_top()}')
                        stack.pop()
                        # write(filename2, '</'+word2+'>')
                        if tab_flag==1:
                            size = stack.get_size()
                            while size > 0:
                                new_line += '\t'
                                size -= 1
                            tab_flag=0
                        new_line = new_line + ('</' + t + '>')
                word2=''

            elif line[i]=='<' and line[i+1]=='!':
                new_line+='\n'
                size = stack.get_size()
                while size > 0:
                    new_line += '\t'
                    size -= 1
                tab_flag = 0
                new_line = new_line + (line[i])

            else:
                new_line+=line[i]
            i+=1
        write(filename2,new_line)
        new_line=''

#def caller3(filename):
#    filename_after=path()  #after minify
#    clear(filename_after)
#    transcript=open_file(filename)
#    minify(transcript)

 #   transcript = open_file(filename_after)
  #  clear(filename2)
   # format(transcript)
    #return filename2

def caller3(filename):
    clear(filename2)
    transcript=open_file(filename)
    minify(transcript)
    filename_after = path()  # after minify


    transcript = open_file(filename_after)
    clear(filename2)
    format(transcript)
    return filename2


#end = time.time()
#print(f'final time : {end-start}')
