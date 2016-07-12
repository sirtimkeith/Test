import sys
import os


dataList = []
maxLengthList = 20
EXTENSION = (".xls")
#locating the files
while len(dataList) < maxLengthList:
    user_files = input("Enter the path of your file(s) or type 'list' to see your current files ")
    if user_files.endswith(EXTENSION) + os.path.exists(user_files): #does it have the .xls extension and does it exist?
        f = open(user_files,'r+')
        dataList.append(user_files)
        print("Found the file, adding it")
    elif user_files == '':
        print (dataList)
        break
    else:
        print("I either can't find it or it's not a .xls file :(")

input()

'''        
    if user_files == '':
        print (dataList)
        break
input()
        


while(True):
    print(user)
    if user == '':
        print ("Does this look like all the file(s) you have listed?")
        print (dataList)
        break

if user_files.endswith(EXTENSION) + os.path.exists(user_files): #does it have the .xls extension and does it exist?
    f = open(user,'r+')
    print("Found the file")
else:
    print("I either can't find it or it's not a .xls file :(")

    
#stuff you do with the file goes here
input()
'''
