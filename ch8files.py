# ..= parent folder, . = this directory, two types of paths, relative and absolute, relative is compared to the files own path,
# absolute means start at root folder of C:\\
import os
def main():
    # os.makedirs('c:\\yes\\what\\python') makes a new directory with this path
    #ose = os.getcwd() gets current directory
    os.chdir('C:\\Windows\\System32')
    ose = os.getcwd()
    #pat = os.path.abspath('skype')
    try:
        size = os.path.getsize('C:\\Users\Hunter\PycharmProjects\ch6strings') #returns bytes
        direc = os.listdir('C:\\Users\Hunter\PycharmProjects')
        print(direc)
        print(size)
        first = open('C:\\Users\Hunter\Documents\pythonstuff\written', 'r')
    except:
        print('you messed up dawg')

main()