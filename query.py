# pip install mysql-connector-python
# pip install streamlit
import mysql.connector 
import streamlit as st


# Conexão

conn = mysql.connector.connect(
    host="http://projetointegrador-graduacao.mysql.database.azure.com/",
    port="3306",
    user="jessica",
    password="senai@134",
    db="medidor"
    )

if conn.is_connected():
    print("Conexão bem-sucedida ao banco de dados!")
else:
    print("Falha na conexão ao banco de dados.")

c=conn.cursor()

# fetch
def view_all_data():
    c.execute('select * from registro order by id asc')
    data=c.fetchall()
    return data