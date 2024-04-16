from utils import *

# Fetch data for regions, topics, sources, countries and indicators
for item in FIELD_MAPPING.keys():
    if item == "indicators":
        for t in FIELD_MAPPING["topics"]["id_list"]:
            write_unproccessed_data(item = item, topic = t, indicator_list = FIELD_MAPPING[item]["id_list"])
        csv_file_path = '../World-Bank/indicators_data.csv'
        cols = ["code"]
        remove_duplicates(csv_file_path, cols)
    elif 'indicator_x_country' == item:
        for c in FIELD_MAPPING["countries"]["id_list"]:
            for i in FIELD_MAPPING["indicators"]["id_list"]:                    
                write_unproccessed_data(item = item, country = c, indicator = i)
    elif 'indicator_x_region' == item:
        for r in FIELD_MAPPING["regions"]["id_list"]:
            for i in FIELD_MAPPING["indicators"]["id_list"]:                    
                write_unproccessed_data(item = item, country = r, indicator = i)
    elif 'indicator_x_topic' == item:
        for t in FIELD_MAPPING["topics"]["id_list"]:
            for i in FIELD_MAPPING["indicators"]["id_list"]:                    
                write_unproccessed_data(item = item, topic = t, indicator = i)
        csv_file_path = '../World-Bank/indicators_x_topic.csv'
        cols = ["indicator_code", "topic_id"]
        remove_duplicates(csv_file_path, cols)
    else:
        write_unproccessed_data(item)

# ----------------------------------------------------------- 

# WARNINGS:
# a. Hay +1 source para cada indicador.
# b. Tuve que corregir porque tanto indicators, indicators_x_topic tenian duplicados, no esta en el codigo principal esto => CHEQUEAR.
# c. Hay que eliminar los archivos .csv para correr el programa, sino se agregan registros a los ya existentes.

# Errores de la API
# 1. "http://api.worldbank.org/v2/topic/6/indicator?format=json" funciona, pero si reemplazas por /indicators no funciona.
# 2. "http://api.worldbank.org/v2/indicator?format=json" solo te trae algunos indicadores, no todos.
# 3. Can't get country's indicators, only all values of an indicator.
# 4. Hay regiones que remplazan a países individuales, por lo que quita poder de análisis.
# 5. Cuando le pegas a /sources no te trae todos los sources (tuve que agregar el 2 y el 57 de forma manual)