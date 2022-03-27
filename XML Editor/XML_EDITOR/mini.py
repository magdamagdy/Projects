import time
#start=time.time()

#filename = "xml.txt"

filename2 = 'text2.xml'

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

def minify(transcript):
    for line in transcript:
        line = line.strip()
        line = line.replace('\n',"")
        write(filename2,line)


def copy_files(fname,fname2):
    with open(fname,'r') as f1, open(fname2,'w') as f2:
        for line in f1:
            f2.write(line)
    return fname2

def path():
    clear('text1.xml')
    fn2= copy_files(filename2,'text1.xml')
    return fn2


def caller2(filename):
    clear(filename2)
    transcript=open_file(filename)
    minify(transcript)
    return filename2
#print(transcript)
#end = time.time()
#print(f'final time:{end-start}' )