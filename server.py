import requests
import subprocess
import json
import pyodbc

class db_connection:
    def __init__(self, server_name, database, login_name, password):
        self.server_name = server_name
        self.database = database
        self.login_name = login_name
        self.password = password

    def db_connect(self) -> pyodbc.Connection:
        conn_str = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={self.server_name};"
            f"DATABASE={self.database};"
            f"UID={self.login_name};"
            f"PWD={self.password}"
        )
        return pyodbc.connect(conn_str)

    def collect_data(self,connection: pyodbc.Connection):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM getlatency")
        print(cursor.fetchall())

    def manage(self):
        connection_ = self.db_connect()
        self.collect_data(connection_)
def git_push(commit_message="Updated metrics.txt"):
    try:
        subprocess.run(["git", "add", "metrics.txt"], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)  
        print("Pushed to GitHub successfully!")      
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e)

def reading_csv_git() -> str:
    with open("metrics.txt", "r") as f:
        text = f.read().split('\n')
        all_line = ""
        for i in text:
            all_line = all_line+i
        return all_line
    
def override_file(list_lines):
    with open("metrics.txt", "w") as f:
        for i in range(0,len(list_lines)):
            f.write(str(list_lines[i])+"\n")
        print("COMPLETED!!!!!!")

obj_sql_con = db_connection(server_name = "UAT-BET-DBA",database = "DBA",login_name = "Grafana",password="Vq3ixSdE1QxJYND")
obj_sql_con.manage()



