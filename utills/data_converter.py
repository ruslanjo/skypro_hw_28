import json
from data.unrefined_csv.constants import PATH_TO_REFINED_FOLDER, PATH_TO_UNREFINED_ADS, \
    PATH_TO_UNREFINED_CATEGORIES, PATH_TO_UNREFINED_USERS, PATH_TO_UNREFINED_LOCATIONS
import csv


class DataConverter:
    def __init__(self, data_path: str, output_path: str, app_model: str):
        self.data_path = data_path
        file_name = self.data_path.split('\\')[-1].split('.csv')[0]
        self.output_path = f'{output_path}/{file_name}.json'
        self.app_model = app_model

    def _convert_csv_to_json(self) -> list[dict]:
        with open(self.data_path, 'r', encoding='utf-8') as csv_data:
            result = []
            for idx, row in enumerate(csv.DictReader(csv_data), start=1):
                del row['id']
                row = self._convert_str_to_bool(row)
                fixture_obj = {'model': self.app_model,
                               'pk': idx,
                               'fields': row}

                result.append(fixture_obj)
            return result

    @staticmethod
    def _convert_str_to_bool(row: dict):
        if 'is_published' in row:
            if row['is_published'] == 'TRUE':
                row['is_published'] = True
            if row['is_published'] == 'FALSE':
                row['is_published'] = False

        return row

    def publish_json(self) -> None:
        data_dict_format = self._convert_csv_to_json()
        with open(self.output_path, 'w', encoding='utf-8') as json_file:
            json_file.write(json.dumps(data_dict_format,
                                       ensure_ascii=False,
                                       indent=4
                                       )
                            )


ads_data_converter = DataConverter(PATH_TO_UNREFINED_ADS,
                                   PATH_TO_REFINED_FOLDER,
                                   'ads.Ads')
categories_data_converter = DataConverter(PATH_TO_UNREFINED_CATEGORIES,
                                          PATH_TO_REFINED_FOLDER,
                                          'ads.Categories')

locations_data_converter = DataConverter(PATH_TO_UNREFINED_LOCATIONS,
                                         PATH_TO_REFINED_FOLDER,
                                         'ads.Locations')

users_data_converter = DataConverter(PATH_TO_UNREFINED_USERS,
                                     PATH_TO_REFINED_FOLDER,
                                     'ads.Users')

ads_data_converter.publish_json()
categories_data_converter.publish_json()
locations_data_converter.publish_json()
users_data_converter.publish_json()
