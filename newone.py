import os
dataList = []
def loc_man():
    user_direc = input ("Enter the folder where you have all your data.")
    while True:
        for file in os.listdir(user_direc):
            if file.endswith(".xls"):
                dataList.append(file)
                print (dataList)
                return
loc_man()
