import pymysql
import cx_Oracle

from datetime import datetime
import lib.QuerysMysql as msql
import lib.QuerysOracle as mora
import math
import json
import boto3
import io

import os

class querys():
    def __init__(self, id,querySelect, queryDelete,queryInsert):
        self.id = id
        self.querySelect = querySelect
        self.queryDelete = queryDelete
        self.queryInsert = queryInsert

# Obtener la variable de entorno PATH
QueryEjecutar = os.environ.get('qejecutar')
ejecutar=QueryEjecutar
print(f"Query a ejecutar: {QueryEjecutar}")

listQuery = []
listQuery.append(querys("1", mora.PS_FLASH_FOR_CU_VW,msql.DELETE_AMZ_FLASH_FOR_CU_TBL,msql.INSERT_AMZ_FLASH_FOR_CU_TBL))
listQuery.append(querys("2", mora.PS_FLASH_MOD_AL_VW,msql.DELETE_AMZ_FLASH_MOD_AL_TBL,msql.INSERT_AMZ_FLASH_MOD_AL_TBL))
listQuery.append(querys("3", mora.PS_FLASH_CIC_MS_VW,msql.DELETE_AMZ_FLASH_CIC_MS_TBL,msql.INSERT_AMZ_FLASH_CIC_MS_TBL))
listQuery.append(querys("4", mora.PS_UTP_DOC_AL_VW,msql.DELETE_AMZ_UTP_DOC_AL_TBL,msql.INSERT_AMZ_UTP_DOC_AL_TBL))
listQuery.append(querys("5", mora.PS_FLASH_BEN_AL_VW,msql.DELETE_AMZ_FLASH_BEN_AL_TBL,msql.INSERT_AMZ_FLASH_BEN_AL_TBL))
listQuery.append(querys("6", mora.PS_FLASH_DT_ALU_VW,msql.DELETE_AMZ_FLASH_DT_ALU_TBL,msql.INSERT_AMZ_FLASH_DT_ALU_TBL))
listQuery.append(querys("7", mora.PS_EMAIL_ADDR_VW,msql.DELETE_AMZ_EMAIL_ADDR_TBL,msql.INSERT_AMZ_EMAIL_ADDR_TBL))
listQuery.append(querys("8", mora.PS_FLASH_TEL_AL_VW,msql.DELETE_AMZ_FLASH_TEL_AL_TBL,msql.INSERT_AMZ_FLASH_TEL_AL_TBL))
listQuery.append(querys("9", mora.PS_FLASH_ROL_EXAM_VW,msql.DELETE_AMZ_FLASH_ROL_EXAM_TBL,msql.INSERT_AMZ_FLASH_ROL_EXAM_TBL))

def get_db_secret(secret_name, region_name):
    client = boto3.client('secretsmanager', region_name=region_name)
    response = client.get_secret_value(SecretId=secret_name)
    secret_string = response['SecretString']
    return json.loads(secret_string)

# Usage example
secret_name = os.environ.get('SECRET_NAME')#"UTP-A190-SM-DEV-00-Migration/access"#
region_name = 'us-east-1'

# Get the secret from AWS Secrets Manager
secret = get_db_secret(secret_name, region_name)


def connectionOracle():
    conn = cx_Oracle.connect(
        user=secret['db-ps-campus_user'],
        password=secret['db-ps-campus_password'],
        dsn=secret['db-ps-campus_dsn'],
        encoding='UTF-8'
    )
    return conn
"""Conexión Mysql"""

def connectMysql():
    conn = pymysql.connect(host=str(secret['db-bdutpqaflash_host']),
                           user=str(secret['db-bdutpqaflash_user']),
                           password=str(secret['db-bdutpqaflash_password']),
                           db=str(secret['db-bdutpqaflash_db']),
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


"Ejecución de query"
def INSERT_PROGRAMACION_SEMANAL():
    print("INICIO INSERT_PROGRAMACION_SEMANAL" + str(datetime.now()))
    for query in filtrarQuerys():
        try:
            print("INSERT_" + str(query.id) + " " + str(datetime.now()))
            print("Extracción de data " + str(datetime.now()))
            data = run_queryOracle(query.querySelect)
            print("Data extraida " + str(len(data)))
            if len(data) > 0:
                print("Eliminar data " + str(datetime.now()))
                eliminar(query.queryDelete)
                print("insertar Data" + " " + str(datetime.now()))
                insert(query.queryInsert, data)
                print("fin insertar Data" + " " + str(datetime.now()))
        except Exception as e:
            print("Ocurrio un error al ejecutar el paso: " + str(query.id) + " " + str(e))
    print("FIN INSERT_PROGRAMACION_SEMANAL" + str(datetime.now()))


def filtrarQuerys():
    if ejecutar !="0":
        x = ejecutar.split(",")
        filtered_arr = [p for p in listQuery if p.id in x]
        return filtered_arr
    else:
        return listQuery