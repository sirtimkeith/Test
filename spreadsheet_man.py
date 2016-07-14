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

    spreadsheet_user = input("This is the list of columns in output.xlsx. Type the values you want to keep, or if you want to keep them all press c. When you're done, press enter to see your list.")
    while spreadsheet_user is not '':
        if spreadsheet_user in OUTOFSIGHT:
            keptList.append(spreadsheet_user)
        elif spreadsheet_user == '':
            print (keptList)
        else:
            print ("That value wasn't listed, so I'm sending you back.")
        spreadsheet_man()
spreadsheet_man()
