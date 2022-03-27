from stack import *
from mini import *
#from list import *
import time

start = time.time()
#filename = "D:/Maro/assignments/data structure xml/data/data-sample.xml"
filename = "xml.txt"  #before minify
filename2 = 'text6.json'  # final

stack = stack_imp()
#linked_list = list_imp()
#linked_list = []
def open_file(filename):
    with open(filename, "r") as f:
        transcript = f.readlines()
        return transcript


def clear(filename2):
    with open(filename2, 'w') as f:
        pass


def write(filename2, line):
    with open(filename2, "a") as f:
        f.write(line)


def replacing(line):
    line = line.replace('<','"')
    line = line.replace('>', '" : ')
    write(filename2,line)

def json(transcript):
    new_line = ''
    word = ''
    word2 = ''
    tab_flag = 0
    curly_braces=0
    lines=0
    qotations_close =0
    comma =0
    repeated = 0
    repated_count=0
    pop=''
    pop_count = 0
    string =''
    square_brac_counter = 0
    not_written = 0
    string_after_tag=''
    name_tag=0
    last_index=''
    enter=0
    for line in transcript:
        i = 0
        lines+=1
        while i < len(line):
            if lines==1 and i==0:
                new_line+='{'
                new_line+='\n'
            #lines+=1
            if line[i] == '<' and line[i + 1] != '/' and line[i + 1] != '!' and line[
                i + 1] != '?':  # open tag <to>gg</to><>''</>
                if line[i - 1] == '>' and i != 0:
                    new_line += '\n'
                    #new_line+='{'

                slash_flag = 0
                space_flag = 0

                j = i
                size = stack.get_size()+1
                while size > 0:
                    new_line += '\t'
                    size -= 1

                if j==i:
                    string+= line[i]
                count = 0
                while line[j] != '>':
                    if line[j] == ' ':
                        space_flag = 1
                        name_tag=1
                        # write(filename2, line[j])
                    if line[j] == '/' and line[j + 1] == '>' and space_flag == 1:
                        slash_flag = 1
                        # break
                    j += 1

                    if space_flag==1:
                        count+=1

                        string_after_tag+=line[j]
                        if count==1:

                            string += '>'
                            string = string.replace(' ', '')
                            string+=' { "__text" : '

                    #new_line = new_line + line[j]

                    # write(filename2, line[j])
                    if space_flag == 0:
                        word = word + line[j]
                        string += line[j]
                count = 0

                i = j
                new_word = word[:len(word) - 1]
                string_after_tag=string_after_tag[:len(string_after_tag)-1]
                #print(string_after_tag)
                if line[i+1] !='<':   #<>"hhh"</>
                    qotations_close=1
                    #if space_flag==0:
                    string+='"'
                    # else:
                    #     string+='{'
                else:
                    #new_line+='{'
                    string+='{'

                if slash_flag == 0:
                    new_word = word[:len(word) - 1]

                    t = stack.get_top()
                    if pop == new_word:
                        repated_count += 1
                        if repated_count >0:

                            #new_line = new_line.replace('<'+new_word+'>', '')
                            string = string.replace('<'+new_word+'>', '')
                            not_written = 1
                            if square_brac_counter==0:
                                index = new_line.rfind(new_word)
                                index=index+len(new_word)+1
                                #print(index)
                                if last_index != index:


                                    new_line = new_line[:index] + '[ ' + new_line[index:]
                                last_index = index
                                print(last_index)
                            square_brac_counter += 1
                            enter=1
                            next=0
                            # if square_brac_counter>0:
                            #     index = new_line.rfind(']')
                            #     #index = index + len(new_word) + 1
                            #     new_line = new_line[:index] + '' + new_line[index:]
                            # #string = string.replace('"', '')
                        repeated=1
                    elif pop != new_word:
                        repated_count=0

                        repeated=0
                        #if not_written==0:
                        square_brac_counter=0
                    # if space_flag==1:
                    #     index=string.rfind(new_word)
                    #     index+=len(new_word)+3
                    #     new_line+=string[:index] + string_after_tag +',' + '__text: ' + string[index:]
                    #     #new_line += string_after_tag + '__text: '+ string +'\n'
                    #     # size=stack.get_size()+1
                    #     # while size>0:
                    #     #     new_line+='\t'
                    #     #     size-=1
                    #     new_line+='}'
                    #else:
                    new_line += string
                    stack.push(word[:len(word) - 1])
                    # print(f'push: {stack.get_top()}')
                # print(word[:len(word)-1])
                word = ''
                string = ''
                slash_flag = 0
                space_flag = 0
                #string_after_tag = ''

            elif line[i] == '<' and line[i + 1] == '/':  # closed tag  <to>gg</to><>''</>
                no_comma=0
                if qotations_close==1:
                    new_line+='"'
                    if repeated == 1:
                        if square_brac_counter>0:
                            l = list(new_line)
                            index=new_line.rfind(']')
                            l[index] = ''
                            l[index-1] ='"'
                            new_line=''.join(l)
                        if name_tag==0:
                            new_line += ']'
                    if name_tag==1:
                        index=string_after_tag.rfind('=')
                        string_after_tag=string_after_tag[:index]+'"'+string_after_tag[index:]
                        string_after_tag=string_after_tag.replace('=',':')
                        new_line += ', "'+string_after_tag +' }'

                        name_tag=0
                        string_after_tag=''
                        if repeated==1:
                            new_line += ']'
                    new_line+=','

                    qotations_close=0
                    no_comma=1
                if line[i - 1] == '>':
                    new_line += '\n'
                    tab_flag = 1
                    curly_braces = 1
                while line[i] != '>':
                    i += 1
                    word2 = word2 + line[i]
                if i+1 <len(line) and i+2<len(line):
                    if line[i+1] == '<' and line[i+2] !='/':
                        comma=1

                word2 = word2[1:len(word2) - 1]
                t = stack.get_top()  # opeining exists and closing is missing or wrong
                if t == word2:
                    if t != None:
                        # print(f'pop: {stack.get_top()}')
                        pop = stack.get_top()
                        stack.pop()
                        pop_count+=1
                        # write(filename2, '</'+word2+'>')
                        if tab_flag == 1 :
                            size = stack.get_size()+1
                            while size > 0:
                                new_line += '\t'
                                size -= 1
                            tab_flag = 0
                        if curly_braces == 1:
                            new_line = new_line + ('}')
                            curly_braces = 0
                            if not_written == 1:
                                index = new_line.rfind('[')
                                index2 = new_line.rfind(']')
                                if index > index2:
                                    new_line += ']'
                                not_written = 0
                                # if enter ==1:
                                #     l = list(new_line)
                                #     index = new_line.rfind(']}')
                                #     l[index] = ''
                                #     l[index +1] = ''
                                #     new_line = ''.join(l)
                                #     enter=0
                                #
                                #     if next==1:
                                #         new_line+=']'
                                    #next = 1
                                #square_brac_counter=0
                                #new_line += ']'
                            #repeated=0

                        if comma==1 and no_comma==0:

                            new_line = new_line + (',')
                            comma=0
                            no_comma=0

                word2 = ''

            # elif line[i] == '<' and line[i + 1] == '!':
            #     new_line += '\n'
            #     size = stack.get_size()
            #     while size > 0:
            #         new_line += '\t'
            #         size -= 1
            #     tab_flag = 0
            #     new_line = new_line + (line[i])

            else:
                if not (line[i] == '<' and line[i + 1] == '!') or (line[i] == '<' and line[i + 1] == '?'):

                    new_line += line[i]


            i += 1

        #write(filename2, new_line)
        if lines==len(transcript):
            new_line+='\n'
            new_line+='}'
        replacing(new_line)
        new_line = ''


filename_after = path()  # after minify
#filename_after ="mynewfile.xml"
clear(filename_after)
transcript = open_file(filename)
minify(transcript)

transcript = open_file(filename_after)
clear(filename2)
json(transcript)
#replacing(transcript)
end = time.time()
print(f'final time : {end - start}')
