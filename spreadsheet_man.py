import openpyxl

keptList = []
def spreadsheet_man():
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
spreadsheet_man()
