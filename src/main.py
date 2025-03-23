# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import numpy as np
import re
import logging
import importlib
import data_clean
import sqlite3
import utils
import transform
from sqlalchemy import create_engine, inspect

importlib.reload(data_clean)

df = pd.read_csv(
    "https://raw.githubusercontent.com/JackyP/testing/master/datasets/nycflights.csv",
    index_col=0
    )

df_raw = data_clean.valida_colunas(df, ["year", "month",  "day", "hour", "minute","arr_delay","carrier","flight","air_time","distance", "origin", "dest"])

df_raw = data_clean.remove_notnull_duplicates(df, ["year", "month",  "day", "hour", "minute","arr_delay","carrier","flight","air_time","distance", "origin", "dest"])

df_raw["date_time"] =  pd.to_datetime(df[["year", "month", "day", "hour", "minute"]],  dayfirst=True)

df_raw = data_clean.rename_colunas(df_raw, ["date_time", "arr_delay","carrier","flight","air_time","distance", "origin", "dest" ], ["data_hora", "atraso_chegada", "companhia", "id_voo","tempo_voo", "distancia", "origem", "destino"])

df_raw = data_clean.def_type_str(df_raw, ["id_voo"])

df_raw_clean = data_clean.ajusta_campo(df_raw, ["companhia", "id_voo", "origem", "destino"])

df_raw_horas_voo = transform.tempo_voo_horas(df_raw_clean, "tempo_voo")

df_transformed = transform.turno_partida(df_raw_horas_voo, "data_hora")

con = sqlite3.connect('projeto_python.db')
cur = con.cursor()
engine = create_engine("sqlite:///projeto_python.db")

with engine.connect() as connection:
    df_transformed.to_sql(name='flights', con=connection, index=False, if_exists='append')

cur.execute('SELECT * from flights limit 10')
result = cur.fetchall()
print(result)

