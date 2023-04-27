#!/usr/bin/env python
# coding: utf-8

# https://mindicador.cl/

import json
import requests
import pandas
import datetime

class Mindicador:
    def __init__(self, indicador, year):
        self.indicador = indicador
        self.year = year
    def InfoApi(self):
        # En este caso hacemos la solicitud para el caso de consulta de un indicador en un año determinado
        url = f'https://mindicador.cl/api/{self.indicador}/{self.year}'
        response = requests.get(url)
        data = json.loads(response.text.encode("utf-8"))
        # Para que el json se vea ordenado, retornar pretty_json
        pretty_json = json.dumps(data, indent=2)
        return data

Dic_Elementos={'uf':1977,'ivp':1990,'dolar':1984,'euro':1999,'ipc':1928,'utm':1990,'imacec':1997,'tpm':2001,'libra_cobre':2012,'tasa_desempleo':2009,'bitcoin':2009}

Anno=datetime.date.today().year
Matriz=pandas.DataFrame()
for d in Dic_Elementos.keys():
    print(d)
    for k in range(Dic_Elementos[d],Anno+1):# desde el inicio (Dic_Elementos[d],2023):
        print(k)
        aux=pandas.DataFrame.from_dict(Mindicador(d,str(k)).InfoApi()['serie']).set_index(['fecha'])
        aux=aux.reset_index()
        for j in aux.index:
            Matriz.loc[aux.loc[j,'fecha'],d]=aux.loc[j,'valor']

Matriz.sort_index(ascending=True).to_csv('Matriz_datos.csv')
