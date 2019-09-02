import csv

def Main():
    try:
        command_line = input('Enter command line for csv filepath and column name. Use -path and -col_name parameters: ')
        command_line=list(command_line.split(' ')) # parse command_line as list
        if len(command_line)==4 and command_line[0]=='-path' and command_line[2]=='-col_name' and command_line[1][-4:]=='.csv': # validation of entered command_line

            path,column = command_line[1],command_line[3] # initialize entered filepath and column_name
            print('Entered filepath is "{}", entered column is "{}"'.format(path,column))
            file = open(path,newline='') # open csv file

            csvreader = csv.reader(file)

            header = next(csvreader) # extracting header of csv file
            header = [i.replace(' ', '_') for i in header] # insert '_' instead of ' ' in csv file header items

            data = [i for i in csvreader] # list of data csv file without header

            for i in range(0,len(data)):
                print(data[i][header.index(column)]) # printing all data of entered column
        else:
            print('Something went wrong...')
            print('You\'ve used invalid syntax. The command line format should be: -path [your filepath to csv file] -col_name [column name of csv file]')
            print('Please, try again')
            print('')
            Main()
    except FileNotFoundError:
        print('Something went wrong...')
        print('You\'ve entered filepath which is not existing. You should enter filepath to existing csv file.')
        print('Please, try again')
        print('')
        Main()
    except ValueError:
        print('Something went wrong...')
        print('You\'ve entered column name which is not existing in csv file.')
        print('Please, try again')
        print('')
        Main()

if __name__=='__main__':
    Main()
