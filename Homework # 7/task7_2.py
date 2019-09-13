import pymysql,csv,json,os,argparse
from contextlib import closing
import pandas as pd

def main():
    try:
        mysql_conn = pymysql.connect(host='127.0.0.1', user='root', password='1111', db='test') # connection to my localhost
        temp_csv = 'user_details.csv' # filename of temporary csv
        json_file = console_parser()
        df = sql_query_execution(mysql_conn)
        create_json(df, temp_csv, json_file)
        print('json file is created in specified folder')
    except Exception as e:
        print(str(e))
    finally:
        if os.path.isfile(temp_csv):
            os.remove(temp_csv) # removing temporary csv file

def console_parser(): # function for argparse arguments
                      # the user needs to write filepath where need to save result json file

    parser = argparse.ArgumentParser(description="This file is handling sql file and convert this to json extension")
    parser.add_argument("json", help="path where need to create and save json")
    args = parser.parse_args()

    if args.json[-5:] == '.json':
        return args.json


def reading_file(): # function for retrieving sql file and parsing it as a string

    f = open('user_details.sql','r')
    sqlfile = f.read()
    f.close()
    return sqlfile


def sql_query_execution(mysql_conn): # function for execution sql script in mysql database

    with closing(mysql_conn) as conn:
        with conn.cursor() as c:
            sql_script=reading_file() # get sql script from file
            sql_commands=reading_file().split(';') # split sql script in a list of commands
            sql_commands.pop() # delete the last item in list because it is empty
            c.execute("DROP TABLE IF EXISTS `user_details`")
            for command in sql_commands:
                c.execute(command) # execute CREATE TABLE and then INSERT INTO statements
            data_frame = pd.read_sql('''select user_id,
                                        username,
                                        first_name,
                                        last_name,
                                        gender,
                                        status from user_details'''
                                        , conn)
            return data_frame # the result of function - DataFrame which save data as two-dimensional table

def create_json(data_frame, temp_csv, json_file): # function for creating csv file then convert to json

    list_dict = []
    data_frame.to_csv(temp_csv, index=False)  # create temporary csv file
    with open(temp_csv) as csv_file: # open csv file
        csv_dict = csv.DictReader(csv_file)  # parse csv into dictionary
        for i in csv_dict:
            list_dict.append(dict(i))  # populating data as a list of dictionaries before creating json file
    with open(json_file, 'w+') as json_:  # creating json file
        json.dump(list_dict, json_, indent=0)  # populating json file directly

if __name__=='__main__':
    main()