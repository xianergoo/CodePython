import os

# start a exe file
# os.system('notepad.exe')


# Function to Get the current   
# working directory  
def current_path():  
    print("Current working directory before")  
    print(os.getcwd())  
    print()  
    
    
# Driver's code  
# Printing CWD before  
# current_path()  
    
# Changing the CWD  
# os.chdir('../')  
    
# Printing CWD after  
# current_path() 

#  list dir
# print(os.listdir())

curdir = os.getcwd()
newdir = os.path.join(curdir, 'newdir')
# print('curdir {}, newdir : {}'.format(curdir, newdir))
if not os.path.exists(newdir):
    os.mkdir(newdir)
if os.path.exists(newdir):
    os.rmdir(newdir)

muti_dir = os.path.join(curdir, 'A\B\C')
if not os.path.exists(muti_dir):
    os.makedirs(muti_dir)

if os.path.exists(muti_dir):
    os.removedirs(muti_dir)

# print(os.listdir())

print('-' * 35)
print(os.path.abspath(__file__))
print(os.path.exists(__file__))
print(os.path.join(os.getcwd(), __file__))
print(os.path.split(__file__))
print(os.path.splitext(__file__))
print(os.path.basename(__file__))

print('-' * 35)
print('walk func')
# print all the python file in current dir
for filepath, dir, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        if filename.endswith('.py'):
            print(filename)
    # print('dirpath: {}, dirname: {}, filename: {}'.format(filepath, dir, filename))
    print()
    # if filename.endwith('.py'):
    #     print(filename)

