import glob
import sys
import csv
import pandas as pd
import numpy as np
import xlrd
import openpyxl


bob = glob.glob("*.xlsx")
def loc_man():
    user_start = input("\n Hi. Want to process some data? Yeah you do. Please make sure none of the files you want processed are open. Press c to continue, d to skip to processing or e to exit. \n \n")
    if user_start == 'c':
        print ("Scanning the current directory for eligible files (.xlsx)")
        print (bob)
        user_contin1 = input("\n Does this list look correct? Because we're going to combine them.  Press c to continue or r to restart")
        if user_contin1 == 'c':
            concat_man()
        if user_contin1 == 'd':
            spreadsheet_man()
        elif user_contin1 == 'r':
            del bob[:]
            loc_man()
    elif user_start == 'e':
        print ("\n Goodbye.")
def concat_man():
    df = pd.DataFrame()
    for f in bob:
        data = pd.read_excel(f)
        df = df.append(data)
    print ("\n Here's your dataframe! \n \n")
    print (df)
    writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='1')
    workbook = writer.book
    worksheet = writer.sheets['1']
    user_concat = input("Your concatenated file is in the same directory with the name Output.xlsx. You may want to check that all of your data\n has been preserved. Press c to continue or r to restart")
    if user_concat == 'c':
        return spreadsheet_man()
        print ("Okay, time to make the data look nice.")
    elif user_concat == 'r':
        return loc_man()
    else:
        print ("Invalid input, sending you to the beginning.")
        loc_man()
def spreadsheet_man():
    OUTOFSIGHT = []
    keptList = []


loc_man()
