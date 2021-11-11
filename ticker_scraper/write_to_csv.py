import csv
import os
from slowprint.slowprint import slowprint

#region write
def writeToCsv(ticker_price_list, c_price_list):
    """
    Writes provided symbols and prices to a csv file
    """
    with open("./Stock_Info/TopTickerslist.csv", 'w') as f:
        f.truncate()
        wr = csv.writer(f)
        header = ['Symbol:', 'Price:']
        wr.writerow(header)
        for i in ticker_price_list:
            i = i.split("\n")[1:3]
            wr.writerow(i)
    with open("./Stock_Info/CryptoList.csv", 'w') as f:
        f.truncate()
        wr = csv.writer(f)
        header = ['Symbol:', 'Price:']
        wr.writerow(header)
        for i in c_price_list:
            i = i.split("\n")[1:3]
            wr.writerow(i)

def writeToTxt(ticker_price_list, c_price_list):
    """
    Writes provided symbols and prices to a txt file
    """
    with open("./Stock_Info/TopTickerslist.txt", 'w') as f:
        f.truncate()
        for i in ticker_price_list:
            f.write(i)
    with open("./Stock_Info/CryptoList.txt", 'w') as f:
        f.truncate()
        for i in c_price_list:
            f.write(i)
#endregion

def writeToFile(tl, cl):
    slowprint("Do you want to save this information to a text file or a spreadsheet(csv)? (y/n) ", 0.3)
    y_n = input()
    which = ""
    if y_n == "Y" or y_n == "y":
        slowprint("Which file type do you want to save it as? (csv/txt) ", 0.3)
        which = input()
        # Writes data to csv files
        if which == "csv" or which == ".csv" or which == "CSV":
            writeToCsv(tl, cl)
            slowprint("Goodbye.", 0.3)
        # Writes data to txt files
        elif which == "text" or which == ".txt" or which == "txt":
            writeToTxt(tl, cl)
            slowprint("Goodbye.", 0.3)
        else:
            slowprint("Please enter file type.", 0.3)
    elif y_n == "N" or y_n == "n":
        slowprint("Goodbye.", 0.3)
    else:
        slowprint("Please type y or n.", 0.3)
    return which

#region open files
def openFiles(which):
    if which == "csv" or which == ".csv" or which == "CSV":
        os.system("libreoffice " + "Stock_Info/TopTickerslist.csv")
        os.system("libreoffice " + "Stock_Info/CryptoList.csv")
    elif which == "text" or which == ".txt" or which == "txt":
        os.system("gedit " + "Stock_Info/TopTickerslist.txt")
        os.system("gedit " + "Stock_Info/CryptoList.txt")

def writeAndOpen(ticker_list, crypto):
    option = writeToFile(ticker_list, crypto)
    slowprint("Do you want to open the newly created files? (y/n) ", 0.3)
    open = input()
    if open == "Y" or open == "y":
        openFiles(option)
    elif open == "N" or open == "n":
        slowprint("Goodbye.", 0.3)
    else:
        slowprint("Please type y or n.", 0.3)
#endregion
