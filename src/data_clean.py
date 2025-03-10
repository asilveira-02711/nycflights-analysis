# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import numpy as np
import re
import logging

def remove_colunas(df):
    
    usecols=["year", "month",  "day", "hour", "minute","arr_delay","carrier","flight","air_time","distance", "origin", "dest"]
    
    if not set(usecols).issubset(set(df.columns)):
        logger.error(f"Mudança de schema; {datetime.datetime.now()} ")
        raise Exception("Mudança de schema")

    df_raw = df.loc[:, usecols].copy()
    df_raw = df_raw[df_raw["air_time"]>0]
    for col in ["carrier","flight", "year", "month", "day" ,"hour", "minute"]:
        tmp_df = df_raw.loc[~df[col].isnull()]
        df_raw = tmp_df.copy()

    df_raw = df_raw.astype("object")

    df_raw.drop_duplicates(inplace=True)

    return df_raw

#inserir coluna

def rename_colunas(df):

    if df is None or df.empty:
        raise ValueError("DataFrame vazio ou inválido recebido na função rename_colunas")
    
    df["date_time"] =  pd.to_datetime(df[["year", "month", "day", "hour", "minute"]],  dayfirst=True)

    usecols2 =["date_time", "arr_delay","carrier","flight","air_time","distance", "origin", "dest" ]

    new_columns = ["data_hora", "atraso_chegada", "companhia", "id_voo","tempo_voo", "distancia", "origem", "destino"]

    columns_map = {usecols2[i]: new_columns[i] for i in range(len(usecols2))}

    df_work = df.loc[:, usecols2].copy()
    df_work.rename(columns=columns_map, inplace=True)

    return df_work

def padroniza_str(obs):
    return re.sub('[^A-Za-z0-9]+', '', obs.upper())

def def_type_str(df, campos):
    for campo in campos:
        df[campos] = df.loc[:,campos].astype(str)
    
    return df

def ajusta_campo(df, campos):
    for campo in campos:
        df[campo] = df[campo].apply(lambda x: padroniza_str(x))
    
    return df
