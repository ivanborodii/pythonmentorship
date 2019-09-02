import os.path
import time

def task2():

    filepath = input(str('Enter filepath: ')).strip()

    directory, file = os.path.split(filepath) # get directory and file names as variables
    print("")
    print('Entered directory is : "{}"'.format(directory))
    print('Entered file is : "{}"'.format(file))
    print("")
    print("Program is checking directory and file on existing in PC...")
    print("")

    try:
        if not os.path.exists(directory): # check if filepath is existing
            os.makedirs(directory) # create directory with sub directories if doesn't exists
            print("Directory \"{}\" is created".format(directory))
            with open(filepath, 'w+'): pass
            print('File "{}" is created'.format(file))
        else:
            print("Directory \"{}\" already exists".format(directory))
            if os.path.isfile(filepath):
                print('The file "{}" already exists in directory "{}"'.format(file,directory))
            else:
                with open(filepath, 'w+'): pass
                print('File "{}" is created'.format(file))
        print("")
        GetReport(directory, file)
    except OSError:
        print("Something went wrong..." )
        print("Please try again")
        print("")
        task2()

def GetReport(directory, file):
    filelist = os.listdir(directory)  # get list of files in specified directory
    filesize = [directory + '\\' + i for i in filelist]
    fsd = []  # list for storing tuples of filename, size and datemodified
    byte = 0  # variable for counting byte size of the directory
    for i in filesize:  # loop for generating list fsd
        file1 = os.path.split(str(i))[1] # get list of files from directory
        dateTimeModify_raw = os.path.getmtime(i)  # get datetime modified value in decimal format
        dateTimeModify = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(
            dateTimeModify_raw))  # get datetime modified value in datetime format
        fsd.append((file1, str(os.path.getsize(str(i))) + ' Bytes', dateTimeModify))
        byte += int(os.path.getsize(str(i)))
    kbyte = round(byte / 1024, 4)  # kbyte, mbyte, gbyte - variables for counting the general size of entered directory in diferrent prefixes
    mbyte = round(kbyte / 1024, 4)
    gbyte = round(mbyte / 1024, 4)
    dateTimeModify_raw = os.path.getmtime(directory)  # get datetime modified value in decimal format
    dateTimeModify = time.strftime('%Y-%m-%d %H:%M:%S',
                                   time.localtime(dateTimeModify_raw))  # get datetime modified value in datetime format
    print('General size the directory "{}" is: {} GB = {} MB = {} KB = {} Bytes'.format(directory, gbyte, mbyte, kbyte,
                                                                                        byte))
    print('Last datetime directory "{}" modification is: {}'.format(directory, dateTimeModify))
    print("")
    print("The directory contains:")
    print("")
    print("{:<50} {:^50} {:>50}".format('File', 'Size', 'Date Modified'))
    for i in fsd:
        print("{:<50} {:^50} {:>50}".format(i[0], i[1], i[2]))
    print("")