import os.path

def task1():

    filepath = input(str('Enter filepath')).strip()

    directory, file = os.path.split(filepath) # get directory and file names as variables
    print("")
    print('Entered directory is : "{}"'.format(directory))
    print('Entered file is : "{}"'.format(file))
    print("")
    print("Program is checking directory and file on existing in PC...")
    print("")

    if os.path.isdir(directory):
        print('The directory "{}" exists.'.format(directory))
        if os.path.isfile(filepath):
            print('The file "{}" exists in "{}" directory.'.format(file, directory))
        else:
            print('The file "{}" does not exist in "{}" directory.'.format(file, directory))
    else:
        print('The directory "{}" does not exist.'.format(directory))
        print('As a result, the file "{}" does not exist in the directory.'.format(file))