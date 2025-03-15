# -*- coding: utf-8 -*-
def tempo_voo_horas(df, tempo_voo_horas):

    df["tempo_minutos"] = df[tempo_voo_horas] / 60

    return df


def calcular_periodo(hora_voo):
    hh = hora_voo.hour
    if 6 <= hh < 12:
        return "manhã"
    elif 12 <= hh < 18:
        return "tarde"
    elif 18 <= hh < 24:
        return "noite"
    else:
        return "madrugada"

def turno_partida(df, campo_hora_voo):
    df["periodo"] = df[campo_hora_voo].apply(lambda x: calcular_periodo(x))
    return df
