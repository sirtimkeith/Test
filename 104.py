import glob
import sys
import pandas as pd
import numpy as np
import xlrd
import openpyxl
import time


keptList = []
bob = glob.glob("*.xlsx")
def loc_man():
    user_start = input("\nHi. Want to process some data? Yeah you do.\nPlease make sure none of the files you want processed are open.\nPress c to continue or e to exit. \n \n")
    if user_start == 'c':
        print ("Scanning the current directory for eligible files (.xlsx)")
        print ("\n".join(bob))
        user_contin1 = input("\nDoes this list look correct? Because we're going to combine them.\nPress c to continue or r to restart\n")
        while user_contin1 in bob:
            bob.remove(user_contin1)
            print ("\nRemoved ", user_contin1)
            print ("\nSo now you have ", bob)
            user_contin1 = input()
        if user_contin1 == 'c':
            concat_man()
        elif user_contin1 == 'r':
            del bob[:]
            loc_man()
    elif user_start == 'e':
        print ("\nGoodbye.")
def concat_man():
    df = pd.DataFrame()
    for f in bob:
        data = pd.read_excel(f)
        df = df.append(data)
    writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='1')
    workbook = writer.book
    worksheet = writer.sheets['1']
    user_concat = input("Your concatenated file is in the same directory with the name Output.xlsx.\nYou may want to check that all of your data has been preserved.\nPress c to continue or r to restart\n")
    if user_concat == 'c':
        print ("Okay, time to make the data look nice.\n")
        time.sleep(1)
        spreadsheet_man()
    elif user_concat == 'r':
        return loc_man()
    else:
        print ("Invalid input, sending you to the beginning.")
        loc_man()

def spreadsheet_man():
    time.sleep(3)
    wb = openpyxl.load_workbook('output.xlsx')
    sheet = wb.get_sheet_by_name('1')
    a = sheet['C1']
    b = sheet['D1']
    c = sheet['E1']
    d = sheet['F1']
    e = sheet['G1']
    f = sheet['H1']
    g = sheet['I1']
    h = sheet['J1']
    OUTOFSIGHT = [a.value, b.value, c.value, d.value, e.value, f.value, g.value, h.value]
    print (OUTOFSIGHT)
    print ("This is the list of columns in output.xlsx.\nType the values you want to keep, or type c to keep them all. \nWhen you're done, press enter to see your list.\n")
    spreadsheet_user = input()
    while spreadsheet_user != '':
        while spreadsheet_user in OUTOFSIGHT:
            keptList.append(spreadsheet_user)
            print ("\n \nAdded ", spreadsheet_user, "\n \n")
            spreadsheet_user = input()
            if spreadsheet_user == '':
                print (keptList)
                spreadsheet_user_contin1 = input ("Here's the list of columns you want to keep.\n Press c to continue and r to restart.\n")
                if spreadsheet_user_contin1 == 'c':
                    column_man()
                if spreadsheet_user_contin1 == 'r':
                    del keptList[:]
                    spreadsheet_man()
                else:
                    print ("That value wasn't listed, so I'm sending you back.")
                    spreadsheet_user = input()

loc_man()
