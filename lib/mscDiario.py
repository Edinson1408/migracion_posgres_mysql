import cx_Oracle
import psycopg2
import pymysql
import lib.QuerysMysql as msql
import lib.QuerysOracle as mora
from email.message import EmailMessage
import smtplib
import ssl
from lib.email import my_function_email
from datetime import datetime
# import boto3
import os
import json
from dotenv import load_dotenv
load_dotenv()

class querys():
    def __init__(self, id,querySelect, queryDelete,queryInsert):
        self.id = id
        self.querySelect = querySelect
        self.queryDelete = queryDelete
        self.queryInsert = queryInsert

# Obtener la variable de entorno PATH
# QueryEjecutar = os.environ.get('qejecutar')
ejecutar="0"
# print(f"Query a ejecutar: {QueryEjecutar}")

listQuery = []
listQuery.append(querys("1", mora.PS_UTP_GRP_HIB2TBL,msql.TRUNCATE_IRL_PS_UTP_GRP_HIB2TBL,msql.INSERT_IRL_PS_UTP_GRP_HIB2TBL))
listQuery.append(querys("2", mora.PS_CLASS_TBL,msql.TRUNCATE_IRL_PS_CLASS_TBL,msql.INSERT_IRL_PS_CLASS_TBL))
listQuery.append(querys("3", mora.PS_CLASS_MTG_PAT,msql.TRUNCATE_IRL_PS_CLASS_MTG_PAT,msql.INSERT_IRL_PS_CLASS_MTG_PAT))
listQuery.append(querys("4", mora.PS_CLASS_INSTR,msql.TRUNCATE_IRL_PS_CLASS_INSTR,msql.INSERT_IRL_PS_CLASS_INSTR))
listQuery.append(querys("5", mora.PS_CRSE_CATALOG,msql.TRUNCATE_IRL_PS_CRSE_CATALOG,msql.INSERT_IRL_PS_CRSE_CATALOG))
listQuery.append(querys("6", mora.PS_LVF_EMPL_AS400,msql.TRUNCATE_IRL_PS_LVF_EMPL_AS400,msql.INSERT_IRL_PS_LVF_EMPL_AS400))
listQuery.append(querys("7", mora.PS_HOLIDAY_DATE,msql.TRUNCATE_IRL_PS_HOLIDAY_DATE,msql.INSERT_IRL_PS_HOLIDAY_DATE))
listQuery.append(querys("8", mora.PS_TERM_TBL,msql.TRUNCATE_IRL_PS_TERM_TBL,msql.INSERT_IRL_PS_TERM_TBL))
listQuery.append(querys("9", mora.PS_UTP_PARAM_VARIO,msql.TRUNCATE_IRL_PS_UTP_PARAM_VARIO,msql.INSERT_IRL_PS_UTP_PARAM_VARIO))


# notifiacion al correo
pass_email= os.getenv('APP_EMAIL'), 
hour_init=str(datetime.now())
my_function_email(pass_email,hour_init,'Inicio')



"""Conexión Oracle"""
def connectionOracle():
    conn = psycopg2.connect(
        database = os.getenv('POSTGRE_DB'), 
        user = os.getenv('POSTGRE_USER'), 
        host= os.getenv('POSTGRE_HOST'),
        password = os.getenv('POSTGRE_PASS'),
        port = 5432
    )
    return conn
"""Conexión Mysql"""

def connectMysql():
    conn = pymysql.connect(host=os.getenv('MYSQL_HOST'), 
                           user=os.getenv('MYSQL_USER'), 
                           password=os.getenv('MYSQL_PASS'), 
                           db=os.getenv('MYSQL_DB'), 
                           charset='utf8mb4')
    return conn

"""Ejecución Querys Oracle"""
def run_queryOracle(sql):
    print(sql)
    conn = connectionOracle()
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
         print("Error "+str(e))
    finally:
        conn.close()

"""Ejecución Querys Mysql"""
def run_queryMysqlInsert(sql,valores):
    conn = connectMysql()
    cursor = conn.cursor()
    cursor.executemany(sql,valores)
    conn.commit()

def run_queryMysqlDelete(sql):
    print(sql)
    try:
        conn = connectMysql()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
            print("Error al eliminar: " + str(e))

"""Querys oracle"""

def insert(sql,valores):
    run_queryMysqlInsert(sql,valores)

def eliminar(sql):
    run_queryMysqlDelete(sql)


def INSERT_PROGRAMACION_DIARIA():
    print("INICIO INSERT_PROGRAMACION_DIARIA " + str(datetime.now()))
    for query in filtrarQuerys():
        try:
            print("INSERT_" + str(query.id) + " " + str(datetime.now()))
            print("Extracción de data " + str(datetime.now()))
            data = run_queryOracle(query.querySelect)
            print("Data extraida " + str(len(data)))
            if len(data) > 0:
                print("Eliminar data " + str(datetime.now()))
                eliminar(query.queryDelete)
                print("insertar Data " + str(datetime.now()))
                insert(query.queryInsert, data)
                print("fin insertar Data" + " " + str(datetime.now()))
        except Exception as e:
            print("Ocurrio un error al ejecutar el paso: " + str(query.id) + " " + str(e))
    print("FIN INSERT_PROGRAMACION_DIARIA" + str(datetime.now()))
    my_function_email(pass_email,str(datetime.now()),'finalizo')

def filtrarQuerys():
    if ejecutar !="0":
        x = ejecutar.split(",")
        filtered_arr = [p for p in listQuery if p.id in x]
        return filtered_arr
    else:
        return listQuery




