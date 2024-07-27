from pathlib import Path
from collections import namedtuple
from datetime import datetime as dt

import workbook
import requests_arshin
import view_results

WORKBOOK = 'check.xlsx'
MNF_NUMBER = 4
FIF_NUMBER = 5
DATE_DISPATCH = 10
APPLICABILITY = 14
VERIFICATION_DATE = 15
DOCNUM = 16
DATE_FORMAT = 'DD.MM.YYYY'
URL = 'https://fgis.gost.ru/fundmetrology/eapi/vri?'
DATE_URL = '%Y-%m-%d'
DATE_XLS = '%d.%m.%Y'

Mi = namedtuple('Mi', 'number fif date_dispatch')
Result = namedtuple('Result', 'applicability docnum date')
ItemFields = namedtuple('ItemFields', 'number fif date_dispatch')
ResultFields = namedtuple('ResultFields', 'applicability date docnum')
item_fields = ItemFields(MNF_NUMBER, FIF_NUMBER, DATE_DISPATCH)
result_fields = ResultFields(APPLICABILITY, VERIFICATION_DATE, DOCNUM)


file = Path.cwd() / WORKBOOK

def mi_set_result(mi, result, record):
    applicability = 'свидетельство' if result[record]['applicability'] else 'извещение'
    result_docnum = result[record]['result_docnum']
    verification_date =  dt.strptime(result[record]['verification_date'], DATE_XLS)
    mi['result'] = Result(
        applicability,
        result_docnum,
        verification_date,
    )

data = workbook.get_data(file)
for key, item in data.items():
    # print("="*80)
    # print(key, '>>>>>', item)
    print('-'*80)
    result = requests_arshin.get_response(item['mi'])
    print(f'Для зав.номер {item['mi'].number} ', end=' ')
    print(f'найдено результатов поверки - {len(result)}')
    if result:
        view_results.view_response(result)
        record = view_results.get_record()
        mi_set_result(item, result, record)

save_file = input('Сохранить результаты в файл?\n==>')
if save_file in ('1', 'y', 'д'):
    workbook.set_data(file, data)
if __name__ == '__main__':
    print('-')
    # print(data)
