import sys
import os.path
from quicksort import quicksort
from heapsort import heapsort

# argc = len(sys.argv);
# argv = sys.argv;
#
# sortMode=0 #default
# #beliebige Reihenfolge -quick / -heap <-> filename
# argI=argv[1] #first argument
# argII=argv[argc-1] #last argument
# if argI=="-quick":
#     sortMode=1;
# elif argI=="-heap":
#     sortMode=2;
#
# fileName = argII;
# print(fileName)
# fileContent = None;

#öffne die Datei und lese die Zahlen
# if os.path.isfile(fileName):
#     # testFile=open(fileName,'r')
#     testFile = open(fileName)
#     print(testFile)
#     fileContent = testFile.readlines()
#     testFile.close()
# else:
#     print('File does not exists: '+fileName)
#     sys.exit(-1);
try:
    argc = len(sys.argv);
    argv = sys.argv;

    sortMode = 0  # default
    # beliebige Reihenfolge -quick / -heap <-> filename
    argI = argv[1]  # first argument
    argII = argv[argc - 1]  # last argument
    if argI == "-quick":
        sortMode = 1;
    elif argI == "-heap":
        sortMode = 2;

    fileName = argII;
    print(fileName)
    fileContent = None;
    
    with open(fileName) as file_obj :
        # testFile=open(fileName,'r')

        fileContent = file_obj.readlines()
        file_obj.close()
except FileNotFoundError:
        print('File does not exists: '+fileName)
        sys.exit(-1);

del fileContent[0] #ignore the comment line
for i in range(0, len(fileContent)): #parse into floats
    fileContent[i] = float(fileContent[i]);

if sortMode==1:
    quicksort(fileContent);
elif sortMode==2:
    heapsort(fileContent);

for i in fileContent:
    print('%.5f' % i)
    

sys.exit(0);
