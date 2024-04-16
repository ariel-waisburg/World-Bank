BASE_URL = "http://api.worldbank.org/v2/"

# Mapping dictionary for API to DB field names
FIELD_MAPPING = {
    "regions": {
        'api': ['code', 'name', 'iso2code'],
        'db': ['code', 'name', 'iso_2_code'],
        "id_list": []
    },
    "topics": {
        'api': ['id', 'value', 'sourceNote'],
        'db': ['id', 'name', 'source_note'],
        "id_list": []
    },
    "sources": {
        'api': ["id", "lastupdated", "name", "code"],
        'db': ["id", "last_updated", "name", "code"],
        "id_list": []
    },
    "countries": {
        'api': ["id", "iso2Code", "name", "longitude", "latitude", {"region": "id"}],
        'db': ["code", "iso_2_code", "name", "longitude", "latitude", "region_code"],
        "id_list": []
    },
    "indicators": {
        'api': ["id", "name", {"source": "id"}, "sourceNote", "sourceOrganization"],
        'db': ["code", "name", "source_id", "source_note", "source_organization"],
        "id_list": []
    },
    "indicator_x_topic": {
        'api': ['id', {"topics": "id"}],
        'db': ['indicator_code', "topic_id"]
    },
    "indicator_x_country": {
        'api': [{"indicator": "id"}, 'countryiso3code', 'date', 'value'],
        'db': ['indicator_code', 'country_code', 'year', 'value']
    },
    "indicator_x_region": {
        'api': [{"indicator": "id"}, 'countryiso3code', 'date', 'value'],
        'db': ['indicator_code', 'region_code', 'year', 'value']
    }
}