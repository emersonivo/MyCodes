with open('file1') as f1:
  lines1 = f1.readlines()

with open('file2','r') as f2:
    import re
    import os

    #print(os.path.isdir("/home/el"))
    #print(os.path.exists("/home/el/myfile.txt"))
    if os.path.isfile('file3'):
        import datetime
        now = datetime.datetime.now()
        string_date = now.strftime('%Y%m%d%H%M%S')
        #print("Agora 3: ", string_date)
        oldfile = open('file3', 'a')
        oldfile.write(string_date)
        oldfile.close()
        os.rename('file3', string_date + '-' + 'file3')
    outfile = open('file3', 'w')
        # r	Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.
        # r+	Opens a file for both reading and writing. The file pointer placed at the beginning of the file.
        # w	Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
        # w+	Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
        # a	Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
        # a+	Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

    for line in f2:
        if any(line.startswith(x.strip()) for x in lines1):
            print(line)
            outfile.write(line)
    outfile.close()
