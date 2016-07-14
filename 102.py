import sys
import os
import time
import pandas as pd

dataList = []
EXTENSION = (".xls")
#locating the files
def locator_man():
    while True:
        user_files = input("Enter the path of your file(s) or hit enter to see your current list. ")
        if user_files.endswith(EXTENSION) + os.path.exists(user_files): #does it have the .xls extension and does it exist?
            f = open(user_files,'r+')
            dataList.append(user_files)
            print("Found the file, adding it")
            locator_man()
        elif user_files == '':
            print (dataList)
            continue_user = input ("This is your file-list, press c to continue or b to add more files ")
            if continue_user == 'b':
                locator_man()
            return
        if user_files == 'c':
            print ("test")
            concatenation_man()
        else:
            print("I either can't find it or it's not a .xls file :(")
            locator_man()

locator_man()
input()
'''
#concatenation
def concatenation_man():
df = pd.DataFrame()
for f in dataList:
    data = pd.read_excel(f, 'Sheet1')
    df = df.append(data)
df

'''
