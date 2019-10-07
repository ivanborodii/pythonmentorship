# FOR COMMAND LINE:
# python task10_1.py C:\Python\sqlite\first_db.db C:\csv_files

import sqlite3, os, argparse, csv

def main():
    parser = argparse.ArgumentParser(description="""This file checks if specified db file exists 
                                                    if yes then drop file and create again 
                                                    else just create file""")
    parser.add_argument("db", help="path to db file")
    parser.add_argument("csv", help="folder where Tasks.csv and Projects.csv are saved")
    try:
        args = parser.parse_args()
        check_file_existing(args.db)
        conn = establish_conn(args.db)
        work_with_csv(conn, args.csv)
    except Exception as e:
        print("")
        print("The program file was failed due to the issue:")
        print(str(e))

def check_file_existing(db_file):
    if os.path.isfile(db_file):
        print("File exists")
        print("File is dropping...")
        os.remove(db_file)
        with open(db_file, "w+") as db_f:
            print("Database file was recreated!")
    else:
        print("File doesn't exists")
        print("File is creating...")
        with open(db_file, "w+") as db_f:
            print("Database file was created!")

def establish_conn(db_file):
    sql_create_projects = """ CREATE TABLE IF NOT EXISTS Projects (
                                        Name text NOT NULL,
                                        Description text,
                                        Deadline date
                                    ); """

    sql_create_tasks = """CREATE TABLE IF NOT EXISTS  Tasks (
                                    Id integer PRIMARY KEY,                                    
                                    Priority integer,
                                    Details text,
                                    Status text,
                                    Deadline date,
                                    Completed date,
                                    Project text,
                                    FOREIGN KEY (Project) REFERENCES Projects (Name)
                                );"""
    conn = sqlite3.connect(db_file)
    print("Connection to database was established!")
    c = conn.cursor()
    c.execute(sql_create_projects)
    print("Table 'Projects' was created!")
    c.execute(sql_create_tasks)
    print("Table 'Tasks' was created!")
    return conn

def work_with_csv(conn, csv_folder):
    # Generating INSERT statement for Projects table
    Projects_csv = csv_folder + "\Projects.csv"

    with open(Projects_csv) as pr_csv:
        csv_reader = csv.reader(pr_csv)
        header = next(csv_reader)
        rows = [i for i in csv_reader]
    insert_data_into_projects = ""
    for i in range(0,len(rows)):
        if i != len(rows)-1:
            insert_data_into_projects = insert_data_into_projects + "('" + rows[i][0] + "','" + rows[i][1] + "','" + \
                                        rows[i][2] + "'),"
        else:
            insert_data_into_projects = insert_data_into_projects + "('" + rows[i][0] + "','" + rows[i][1] + "','" + \
                                        rows[i][2] + "');"

    insert_projects = "INSERT INTO Projects (" + header[0] + "," + header[1] + "," + header[2] + ") VALUES " + insert_data_into_projects

    # Generating INSERT statement for Tasks table
    Tasks_csv = csv_folder + "\Tasks.csv"

    with open(Tasks_csv) as tsk_csv:
        csv_reader = csv.reader(tsk_csv)
        header = next(csv_reader)
        rows = [i for i in csv_reader]
    insert_data_into_tasks = ""
    for i in range(0,len(rows)):
        if i != len(rows)-1:
            insert_data_into_tasks = insert_data_into_tasks + "(" + rows[i][0] + "," + rows[i][1] + ",'" + \
                                        rows[i][2] + "','" + rows[i][3] + "','" + rows[i][4] + "','" + rows[i][5] + \
                                        "','" + rows[i][6] + "'),"
        else:
            insert_data_into_tasks = insert_data_into_tasks + "(" + rows[i][0] + "," + rows[i][1] + ",'" + \
                                        rows[i][2] + "','" + rows[i][3] + "','" + rows[i][4] + "','" + rows[i][5] + \
                                        "','" + rows[i][6] + "');"

    insert_tasks = "INSERT INTO Tasks (" + header[0] + "," + header[1] + "," + header[2] + "," + header[3] + "," + \
                   header[4] + "," + header[5] + "," + header[6] + ") VALUES " + insert_data_into_tasks
    print("INSERT statements were generated!")

    # Querying data from db
    c = conn.cursor()
    c.execute(insert_projects)
    c.execute(insert_tasks)
    print("Inserting data into db completed!")
    c.execute("SELECT * FROM Tasks WHERE Project='CTCO-ORKE'")
    result_set = c.fetchall()
    print("Result of SELECT statement is:")
    for row in result_set:
        print(row)
    conn.close()

if __name__=="__main__":
    main()

