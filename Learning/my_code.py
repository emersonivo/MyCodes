#
import os
import re
import subprocess
import datetime
import shutil
now = datetime.datetime.now()   # Create var timex as 'YYYYmmddHHMM'
timex = now.strftime('%Y%m%d%H%M%S') # Create var timex as 'YYYYmmddHHMM'
print("Agora 3: ", timex)
#HOMEDIR = os.path.abspath('') # Assign the current path to the var $HOMEDIR

HOMEDIR = os.path.dirname('/bkp_local/temp/')
print("#1 ", HOMEDIR)

datax = HOMEDIR+'/data'
if not os.path.isdir(datax): # Check if the folder '$HOMEDIR/data' exist in the current path, if not, create it
    os.mkdir(datax,666)

tmpx = HOMEDIR+'/tmp'
if not os.path.isdir(tmpx): # Check if the folder '$HOMEDIR/tmp' exist in the current path, if not, create it
    os.mkdir(tmpx, 666)

archive = HOMEDIR+'/archive'
if not os.path.isdir(archive): # Check if the folder '$HOMEDIR/archive' exist in the current path, if not, create it
    os.mkdir(archive, 666)

gwmresoures = ['sysloc', 'windir', 'windfs', 'winperm']

class get_user_data(): # Create the funcion 01-get_gwm-queued-requests
    def __init__(self):
        os.mkdir(archive+"/"+timex, 666)            # Create two folders inside $HOMEDIR/archive ($timex/tmp and $timex/data)
        os.mkdir(archive+"/"+timex+"/tmp", 666)     # Create two folders inside $HOMEDIR/archive ($timex/tmp and $timex/data)
        os.mkdir(archive+"/"+timex+"/data", 666)    # Create two folders inside $HOMEDIR/archive ($timex/tmp and $timex/data)
        for filename in os.listdir(datax):
            shutil.move(datax+"/"+filename, archive+"/"+timex+"/data/"+filename)    # Move files from $HOMEDIR/data into $HOMEDIR/archive/$timex/data

        for filename in os.listdir(tmpx):
            shutil.move(tmpx+"/"+filename, archive+"/"+timex+"/tmp/"+filename) # Move files from $HOMEDIR/tmp into $HOMEDIR/archive/$timex/tmp

#    OUTPUT1 = open(datax+"/01-usr-msfwid.001", 'a+')     # Define the path '$datax/01-usr-msfwid.001 as OUTPUT1
    def get_queued_requests(self, INPUT1):
        if INPUT1 == "all": # If statement checking if INPUT1 == "all"
            for i in gwmresoures: # For loop for gwm resources
                print(i)
                subprocess.call("./test.sh" + " Python " + i, shell=True)   # Call Perl script with args outputting msfwid to the file $tmp/01.2-gwm_queues
                with open(datax+"/pytho2bash-"+i+".txt", "r") as INPUT2:
                    print("INPUT2", INPUT2.read())

                    with open(datax+"/01-usr-msfwid.001", 'a+') as OUTPUT1:     # Define the path '$datax/01-usr-msfwid.001 as OUTPUT1
                        OUTPUT1.write(INPUT2.read())    # Move the content of $tmp/01.2-gwm_queues to OUTPUT1
                        print("OUTPUT1", OUTPUT1.read())
        else:   # ELSE statement
            subprocess.call("./test.sh" + " Python " + INPUT1, shell=True)  # Call Perl code for INPUT1 (!='all')

    def query_user_data(self):  #Subfunction - block 2
        if INPUT1 == "file":
            INPUT2 = input("Type full file name: ")  # Read user's input for filename (INPUT2)
            if not INPUT2:
                print("Missig file name. Bye!!!")
            elif os.path.isfile(INPUT2):
                os.rename(INPUT2, datax + "/01-usr-msfwid.001")  # Move INPUT2 to $datax/01-usr-msfwid.001
            else:
                print("File name does not exist. Bye!!!")

        for x in range(6):
            for y in ['aa', 'bb', 'cc', 'dd', 'ee']:
                with open(datax + "/01-usr-msfwid.001", 'a+') as OUTPUT1:
                    mystring = (str(x)+str(y)+str(timex)+"\n")
                    OUTPUT1.write(mystring)

        with open(datax + "/01-usr-msfwid.001", 'r') as OUTPUT1:
            for line in OUTPUT1.readlines():    # FOR statement reading lines (msfwid) from OUTPUT1
                subprocess.call("./test.sh" + " Python " + line, shell=True)    # call Perl code to query users' accounts outputing to 01.4-usr_data-$msfwid

teste1 = get_user_data()
INPUT1 = input("Type one option: sysloc, windir, windfs winperm, all OR file: ")     # Reads user's input (INPUT1) from a list of options
if not INPUT1:  # IF statment checking if INPUT1 is NULL
    print("No option selected. Try again. Bye!")  # Message the user if INPUT1 is null and exit
    exit()
elif INPUT1 != "file":
    print("input1: ", INPUT1)
    teste1.get_queued_requests(INPUT1)  # Call sub-function 1
    teste1.query_user_data()  # Call sub-function 2
else:  # ELSE statement (INPUT1 == "file")
    teste1.query_user_data()  # Call sub-function 2




