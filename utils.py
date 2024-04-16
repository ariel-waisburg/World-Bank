from constants import FIELD_MAPPING
from api_fetch import fetch_data
from csv_writer import write_to_csv
import pandas as pd

def extract_endpoint(item):
    if '_x_' in item:
        if "topic" in item:
            return "topic"
        elif "country" in item or "region" in item:
            return "country"
    elif item == "indicators":
        return "topic"
    return item

def process_data(data, item, keys, region_codes, indicator_list = None, indicator_value_row = False):
    id_list = []
    processed_data = []
    for element in data:
        if (indicator_value_row == True and element["value"] is None) or ((item == "countries") and (element["id"] in region_codes or "IBRD" in element["name"])):
            continue
        if indicator_list == None or element["id"] not in indicator_list:
            row_data = []
            for key in keys['api']:
                if not isinstance(key, dict):
                    row_data.append(element[key])
                else:
                    if item == 'indicator_x_topic':
                        row_data.append(element[list(key.keys())[0]][0][list(key.values())[0]])
                    else:
                        row_data.append(element[list(key.keys())[0]][list(key.values())[0]])
            id_list.append(row_data[0])
            processed_data.append(row_data)
    return id_list, processed_data

def write_unproccessed_data(item, topic = None, indicator_list = None, country = None, indicator = None):
    arg1 = extract_endpoint(item)
    data = fetch_data(endpoint = arg1, topic_id = topic, country_code = country, indicator_id = indicator)
    indicator_value_row = country != None
    if data and ("message" not in list(data[0].keys())) and (int(data[0]["page"]) > 0):
        csv_file_path = item + "_data.csv"
        headers = FIELD_MAPPING[item]['db']
        processed_data = process_data(data[1], item, FIELD_MAPPING[item], FIELD_MAPPING["regions"]["id_list"], indicator_list, indicator_value_row = indicator_value_row)
        item_id_list = processed_data[0]
        FIELD_MAPPING[item]["id_list"] = item_id_list
        if csv_file_path == "countries_data.csv":
            print("tiene un superpoder")
        write_to_csv(csv_file_path, headers, processed_data[1])
    else:
        print("Failed to fetch data for", item)

def remove_duplicates(csv_file_path, cols):
    df = pd.read_csv(csv_file_path)
    df_cleaned = df.drop_duplicates(subset=cols, keep='first')
    df_cleaned.to_csv(csv_file_path, index=False, mode='w')
    print(f"Duplicate records have been removed from '{csv_file_path}'.")

def print_missing_sources():
    indicators_file_path = '../World-Bank/indicators_data.csv'
    df1 = pd.read_csv(indicators_file_path)
    # Extract unique source_ids
    unique_source_ids = df1['source_id'].unique().tolist()
    print("Unique source_ids from the first CSV:")
    print(unique_source_ids)

    sources_file_path = '../World-Bank/sources_data.csv'
    df2 = pd.read_csv(sources_file_path)
    # Extract ids from the second CSV
    ids_in_second_csv = df2['id'].tolist()
    print("\nIDs from the second CSV:")
    print(ids_in_second_csv)

    # Find source_ids that are in the first list but not in the second list
    missing_ids = [source_id for source_id in unique_source_ids if source_id not in ids_in_second_csv]
    print("\nIDs present in the first list but missing in the second list:")
    print(missing_ids)