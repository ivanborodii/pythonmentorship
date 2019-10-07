# FOR COMMAND LINE:
# python task10_2.py C:\Python\sqlite\second_db.db C:\csv_filess

import csv, os, argparse
from sqlalchemy import create_engine, MetaData, Table, Column, Text, Date, Integer, ForeignKey
from datetime import date, datetime

def main():
    parser = argparse.ArgumentParser(description="""This file checks if specified db file exists 
                                                    if yes then drop file and create again 
                                                    else just create file""")
    parser.add_argument("db", help="path to db file")
    parser.add_argument("csv", help="folder where Tasks.csv and Projects.csv are saved")
    try:
        args = parser.parse_args()
        print(args.db)
        engine,projects,tasks = check_file_existing(args.db)
        work_with_csv(engine, projects, tasks, args.csv)
    except Exception as e:
        print("")
        print("The program file was failed due to the issue:")
        print(str(e))

def check_file_existing(db_file):
    if os.path.isfile(db_file):
        print("File exists")
        print("File is dropping...")
        os.remove(db_file)
        engine = create_engine("sqlite:///" + db_file)
        print("Database file was recreated!")
    else:
        print("File doesn't exists")
        print("File is creating...")
        engine = create_engine("sqlite:///" + db_file)
        print("Database file was created!")
    meta = MetaData()
    projects = Table(
        'Projects', meta,
        Column('Name', Text, primary_key=True),
        Column('Description', Text),
        Column('Deadline', Date)
    )
    tasks = Table(
        'Tasks', meta,
        Column('Id', Integer, primary_key=True),
        Column('Priority', Integer),
        Column('Details', Text),
        Column('Status', Text),
        Column('Deadline', Date),
        Column('Completed', Date),
        Column('Project', Text, ForeignKey('Projects.Name'))
    )
    meta.create_all(engine)
    print("Tables 'Projects' and 'Tasks' were created!")
    return engine,projects,tasks

def work_with_csv(engine, projects, tasks, csv_folder):
    conn = engine.connect()
    # Extracting data from Projects.csv file and do INSERT INTO Projects table statement
    Projects_csv = csv_folder + "\Projects.csv"
    pr_list = []
    pr_csv = csv.DictReader(open(Projects_csv))
    for i in pr_csv:
        pr_list.append(dict(i))
    for i in range(0,len(pr_list)): # loop for converting date values
        temp_list = pr_list[i]['Deadline'].split('/')
        pr_list[i]['Deadline'] = datetime(int(temp_list[2]),int(temp_list[0]),
                                          int(temp_list[1])).date()
    conn.execute(projects.insert(), pr_list) # do INSERT INTO as a list of dictionaries
    print("Table 'Projects' was populated!")

    # Extracting data from Tasks.csv file and do INSERT INTO Tasks table statement
    Tasks_csv = csv_folder + "\Tasks.csv"
    ts_list = []
    ts_csv = csv.DictReader(open(Tasks_csv))
    for i in ts_csv:
        ts_list.append(dict(i))

    for i in range(0,len(ts_list)): # loop for converting date values
        temp_list_1 = ts_list[i]['Deadline'].split('/')
        ts_list[i]['Deadline'] = datetime(int(temp_list_1[2]),int(temp_list_1[0]),
                                          int(temp_list_1[1])).date()
        if ts_list[i]['Completed'] != '': # handling empty values
            temp_list_2 = ts_list[i]['Completed'].split('/')
            ts_list[i]['Completed'] = datetime(int(temp_list_2[2]),int(temp_list_2[0]),
                                               int(temp_list_2[1])).date()
        else:
            ts_list[i]['Completed'] = None
    conn.execute(tasks.insert(), ts_list)
    print("Table 'Tasks' was populated!")

    # make SQL query according to the homework conditions
    result = conn.execute(tasks.select().where(tasks.c.Project == 'CTCO-ORKE'))
    print("The result of SELECT statement is:")
    for row in result:
        print(row)

if __name__=="__main__":
    main()