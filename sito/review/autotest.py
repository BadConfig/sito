import os
import time
import sys
def runapp(TermComand,inp):
    startTime = time.time()
    os.system(TermComand)
    AppTime = time.time() - startTime 
    a = open('/home/dell/Test/op.txt')
    b = open('/home/dell/.tests')
    a = a.readline()
    b = b.readline()
    c = True 
    for i in range(0,min(len(b),len(a))):
        if a[i] != b[i]:
            c = False
            break;
    if c:
        App = [True,AppTime]
    else:
        App = [False,AppTime]
    return App
#import difflib
def testmodule(inp):
    """
    inp - file input - {'filepath':...,'fileLang':...,
    'istream':...,'ostream':...,'reqTime':...}
    file lang - c c++11 c++14 c++17 python3.6 
    filepath - to file in os
    istream - test input
    ostream - correct test output 

    returns - answer = {'pass':...,'time':...}
    pass if not out of time and correct - [True, time]
    else [False,wrong op string and correct or out of time]
    """
    if inp['fileLang'] == 'c':
        compiler_n_flags = 'gcc -o ~/.testTemp.elf'
    elif inp['fileLang'] == 'c++11':
        compiler_n_flags = 'g++ --std=c++11 -o ~/.testTemp.elf'
    elif inp['fileLang'] == 'c++14':
        compiler_n_flags = 'g++ --std=c++14 -o ~/.testTemp.elf'
    elif inp['fileLang'] == 'c++17':
        compiler_n_flags = 'g++ --std=c++17 -o ~/.testTemp.elf'
    elif inp['fileLang'] == 'python3.6':
        compiler_n_flags = 'python3'
    TermComand = compiler_n_flags + ' ' + inp['filepath'] 
    IOStream = ' < ' + inp['istream'] + ' > ~/.tests'
    if inp['fileLang'] == 'python3.6':
        TermComand += IOStream
        Tests = runapp(TermComand,inp)
    else:
        os.system(TermComand)
        TermComand = '~/.testTemp.elf' + IOStream
        Tests = runapp(TermComand,inp)
    answer = {}
    answer['pass'] = Tests[0]
    answer['time'] = 'runned time: ' + str(Tests[1])  + ' required time : ' + inp['reqTime'] 
    return answer
if __name__ =='__main__':
    a = {}
    a['filepath'] = input("введите файл для теста")
    a['fileLang'] = input('введите язык')
    a['istream'] = input('file with tests')
    a['ostream'] = input('file with op')
    a['reqTime'] = input('time')
    print(testmodule(a))

