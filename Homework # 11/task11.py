# FOR COMMAND LINE:
# python task11.py C:\csv_files

from pymongo import MongoClient
import csv, argparse
from datetime import date,datetime

def convert_from_csv_projects(csv_file):
    projects_csv = csv_file + '\Projects.csv'
    csv_dict_projects = csv.DictReader(open(projects_csv))
    list_dict_projects = [] # list of dictionaries which will be used for inserting into mongodb collection
    for i in csv_dict_projects:
        list_dict_projects.append(dict(i))  # populating data before insert into mongodb
    for i in range(0,len(list_dict_projects)): # in the loop body makes convertion date column
                                                # to consistensy with python
                                                # because csv is reading all values as string
        temp_list = list_dict_projects[i]['Deadline'].split('/')
        list_dict_projects[i]['Deadline'] = datetime(int(temp_list[2]),int(temp_list[0]),
                                          int(temp_list[1]),0,0)
    return list_dict_projects

def convert_from_csv_tasks(csv_file):
    tasks_csv = csv_file + '\Tasks.csv'
    csv_dict_tasks = csv.DictReader(open(tasks_csv))
    list_dict_tasks = [] # list of dictionaries which will be used for inserting into mongodb collection

    for i in csv_dict_tasks:
        list_dict_tasks.append(dict(i))  # populating data before insert into mongodb
    for i in range(0, len(list_dict_tasks)):    # in the loop body makes convertion date and int columns
                                                # to consistensy with python
                                                # because csv is reading all values as string
        list_dict_tasks[i]['Id'] = int(list_dict_tasks[i]['Id'])
        list_dict_tasks[i]['Priority'] = int(list_dict_tasks[i]['Priority'])
        temp_list = list_dict_tasks[i]['Deadline'].split('/')
        list_dict_tasks[i]['Deadline'] = datetime(int(temp_list[2]), int(temp_list[0]),
                                                        int(temp_list[1]),0,0)
        if list_dict_tasks[i]['Completed'] != '':  # handling empty values
            temp_list_2 = list_dict_tasks[i]['Completed'].split('/')
            list_dict_tasks[i]['Completed'] = datetime(int(temp_list_2[2]), int(temp_list_2[0]),
                                              int(temp_list_2[1]),0,0)
        else:
            list_dict_tasks[i]['Completed'] = None
    return list_dict_tasks

def connect_to_mongo(projects, tasks):
    conn = MongoClient('mongodb://localhost:27017/')
    db = conn['test']
    tasks_coll, projects_coll = db['tasks'], db['projects']

    projects_coll.drop()
    tasks_coll.drop()

    projects_coll.insert_many(projects)
    tasks_coll.insert_many(tasks)

    query_result = tasks_coll.find({"Status":"cancelled"}).distinct("Project")
    print("The result of 'Вивести на екран назви всіх проектів в яких є таски зі статусом cancelled.' is:")
    print(query_result)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""This file takes csv files from specified folder, 
                                                    parse these files and make insert into mongodb tables""")
    parser.add_argument("csv", help="folder where Tasks.csv and Projects.csv are saved")
    try:
        args = parser.parse_args()
        projects = convert_from_csv_projects(args.csv)
        tasks = convert_from_csv_tasks(args.csv)
        connect_to_mongo(projects, tasks)
    except Exception as e:
        print("")
        print("The program file was failed due to the issue:")
        print(str(e))
