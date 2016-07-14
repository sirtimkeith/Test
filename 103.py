import sys
import os
import xlrd
from openpyxl import load_workbook

dataList = []
EXTENSION = (".xls")
#opening the files
def cat_man():
    while True:
        bob = '\n'.join(dataList)
        print ("Cleaning the list...")
        load_workbook(*bob[5:],'r+')
        input()
#locating the files
def loc_man():
    while True:
        try:
            user_files = input("Enter the path of your file(s) or hit enter to see your current list. ")
            if user_files.endswith(EXTENSION) + os.path.exists(user_files):
                f = open(user_files,'r+')
                dataList.append(user_files)
                print("Found the file, adding it")
                f.close()
            elif user_files == '':
                print (dataList)
                continue_user = input("This is your file-list, press c to continue or b to add more files ")
                if continue_user == 'b':
                    loc_man()
                elif continue_user == 'c':
                    return cat_man()
            else:
                print("I either can't find it, or it's not a .xls file :(")
                loc_man()
        except OSError:
            print ("I either can't find it, or it's not a .xls file :(")
            loc_man()

loc_man()
