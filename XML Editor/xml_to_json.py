
class Node:
    def __init__(self, value, l):
        self.tag_name = value
        self.text = ""
        self.children = []
        self.level = l
    def child_names(self):
        names = []
        for x in range(len(self.children)):
            names.append([(self.children[x].tag_name, self.children[x].text, self.children[x].level, self.children[x].children)])
        return names

class Stack:
    def __init__(self):
        #self.top = None
        self.size = 0
        self.s = []
    def is_empty(self):
        if self.size == 0 :
            return True
        else:
            return False
    def push(self,item):
        #if self.top is None:
            #new_node = node()
            #new_node.item = item
            #new_node.next = None
        self.s.append(item)
        #self.top = item
        self.size += 1
        """else:
            new_node = node()
            new_node.item = item
            new_node.next = self.top
            self.top = new_node
            self.size+=1"""
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.s.pop(self.size)
    def get_top(self):
        return self.s[self.size - 1]
    def get_size(self):
        return self.size

sourceFile = open('demo.txt', 'w')
def traversePreorder(node):
    if node is not None:
        i = 0
        str = " "
        while i < node.level:
            str += "  "
            i += 1
        #print(str, '"', node.tag_name, '"', ":", end=" ", file=sourceFile)
        if node.children:
            print(str, '"', node.tag_name, '"', ":", end=" ", file=sourceFile)#####################

            print("{", file=sourceFile)

            n = node.child_names()###################3

            for i in range(len(node.children)):
                cnt = n.count(node.children[i].tag_name)#################3
                if cnt > 1: ###########
                    print(str, '"', node.tag_name, '"', ": [", end=" ", file=sourceFile)
                    j = i

                    traversePreorder(node.children[j])

                else:
                    traversePreorder(node.children[i])
                    if i < (len(node.children) - 1):
                        # print(",", file=sourceFile)
                        y = 98
            #################33
            k = 0
            str = " "
            while k < node.level:
                str += "  "
                k += 1
            #################33
            print(str, "}", file=sourceFile)
        if node.text != "":
            ########## bs kda el tag eli leha children mlhash text 34an mitb3osh marten
            print(str, '"', node.tag_name, '"', ":", end=" ", file=sourceFile)
            print('"', node.text, '"', file=sourceFile)

def xmlTree(file):
    count_closed_tag = 0
    count_open_tag = 0
    i = 0
    count = 1
    stack_of_nodes = Stack()
    stack_of_names = Stack()

    print("length of file= ", len(file))
    #for i in range(len(file)):
    while i < len(file):
        #closed tag
        if file[i] == "<" and file[i+1] == "/":
            count_closed_tag += 1
            stack_of_nodes.pop()
            count -= 1
            #i += 2
            while file[i] != ">":
                i += 1
        ## comments
        if file[i] == "<" and file[i+1] == "!":
            while file[i] != ">":
                i += 1
        ## versioning
        if file[i] == "<" and file[i+1] == "?":
            while file[i] != ">":
                i += 1
        #open tag
        elif file[i] == "<":
            count_open_tag += 1
            tag = ""
            i += 1
            while file[i] != ">":
                #we may handle the attributes here
                tag += file[i]
                i += 1
            stack_of_names.push(tag)
            new_node = Node(tag, count)
            print("tag & level ", tag, count)
            if count == 1:
                root = new_node
                #print("root")
            count += 1
            if stack_of_nodes.is_empty():
                stack_of_nodes.push(new_node)
            else:
                prev_node = stack_of_nodes.get_top()
                prev_node.children.append(new_node)
                stack_of_nodes.push(new_node)
        elif file[i] == ">":
            #print("came here")
            i += 1
        elif file[i] == "\n":
            i += 1
        else:
            txt = ""
            while file[i] != "<":
                if file[i] != "\n":
                    txt += file[i]
                i += 1
            #to check that str contain only spaces
            space_count = 0
            for j in range(len(txt)):
                if txt[j] == " ":
                    space_count += 1
            if space_count == len(txt):
                txt = ""
            #####################################
            if txt != "":
                print("text:", txt)
                prev_node = stack_of_nodes.get_top()
                prev_node.text = txt


    return [count_open_tag, count_closed_tag, stack_of_nodes, stack_of_names, root]

def main():
    f = open("xmlfile.txt", "r")
    fi = f.read()
    #print(f.read())
    result = xmlTree(fi)
    print("stack of names", result[3].s)
    print("stack of nodes", result[2].s)
    print("count of open tag= ", result[0])
    print("count of closed tag= ", result[1])
    print("{", file=sourceFile)
    traversePreorder(result[4])
    print("}", file=sourceFile)
main()

