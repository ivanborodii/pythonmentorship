import argparse,csv,json

def main():
    parser = argparse.ArgumentParser(description="This file is receiving csv file and convert this to json extension")
    parser.add_argument("csv", help="path to existing csv file")
    parser.add_argument("json", help="path where need to create and save json")
    args = parser.parse_args()
    try:
        if args.csv[-4:]=='.csv' and args.json[-5:]=='.json':
            deleted_column = 'password' # column which shouldn't be shown in json file according to task
            list_dict = [] # variable for saving csv rows as a list of dictionaries
            csv_dict = csv.DictReader(open(args.csv))  # open csv file and parse into dictionary
            for i in csv_dict:
                del i[deleted_column] # delete all data which are related to Password column
                list_dict.append(dict(i)) # populating data before creating json file
            with open(args.json, 'w+') as json_file: # creating json file
                json.dump(list_dict,json_file, indent=0) # populating json file directly
            print('json file is created in specified folder')
        else:
            print("You've entered parameters with invalid values")
    except Exception as e:
        print(str(e))

if __name__=='__main__':
    main()