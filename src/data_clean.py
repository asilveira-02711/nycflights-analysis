# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import numpy as np
import re
import logging


def valida_colunas(df, colunas):
    
    usecols = colunas
    
    if not set(usecols).issubset(set(df.columns)):
        logger.error(f"Mudança de schema; {datetime.datetime.now()} ")
        raise Exception("Mudança de schema")
    
    return df

def remove_notnull_duplicates(df, colunas):

    usecols = colunas

    df_raw = df.loc[:, usecols].copy()
    df_raw = df_raw[df_raw["air_time"]>0]
    for col in ["carrier","flight", "year", "month", "day" ,"hour", "minute"]:
        tmp_df = df_raw.loc[~df[col].isnull()]
        df_raw = tmp_df.copy()

    df_raw = df_raw.astype("object")

    df_raw.drop_duplicates(inplace=True)

    return df_raw

def rename_colunas(df, colunas_de, colunas_para):

    usecols2 = colunas_de

    new_columns = colunas_para

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
