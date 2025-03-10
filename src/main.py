# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import numpy as np
import re
import logging
import importlib
import data_clean

importlib.reload(data_clean)

#source
df = pd.read_csv(
    "https://raw.githubusercontent.com/JackyP/testing/master/datasets/nycflights.csv",
    index_col=0
    )

#data_clean
df_raw = data_clean.remove_colunas(df)

df_raw = data_clean.rename_colunas(df_raw)

df_raw = data_clean.def_type_str(df_raw, ["id_voo"])

df_raw_clean = data_clean.ajusta_campo(df_raw, ["companhia", "id_voo", "origem", "destino"])

#data_transformation
