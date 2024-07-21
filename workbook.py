from pathlib import Path
from openpyxl import load_workbook
from collections import namedtuple
from datetime import date

WORKBOOK = 'check.xlsx'
SHEET = 'ЖурналПоверки'
MNF_NUMBER = 4
FIF_NUMBER = 5
DATE_DISPATCH = 10
APPLICABILITY = 14
VERIFICATION_DATE = 15
DOCNUM = 16

Mi = namedtuple('Mi', 'number fif date_dispatch')
Result = namedtuple('Result', 'applicability result_docnum verification_date')
ItemFields = namedtuple('ItemFields', 'number fif date_dispatch')
ResultFields = namedtuple('ResultFields', 'applicatility date docnum')
item_fields = ItemFields(MNF_NUMBER, FIF_NUMBER, DATE_DISPATCH)
result_fields = ResultFields(APPLICABILITY, VERIFICATION_DATE, DOCNUM)

file = Path.cwd() / WORKBOOK


def get_data(file):
    data = {}
    wb = load_workbook(file, data_only=True)
    sheet = wb[SHEET]

    for row in range(2, sheet.max_row + 1):
        if sheet.cell(row=row, column=DOCNUM).value:
            continue
        data[row] = {
            'mi': Mi(*get_mi(sheet, row, item_fields)),
            'result': Result(*get_result(sheet, row, result_fields))
        }

    wb.close()
    return data


def set_data(file, data):
    wb = load_workbook(file, data_only=True)
    sheet = wb[SHEET]
    for key, value in data:
        print(key, value, sep='\n')
    wb.close()


def get_mi(sheet, row, fields):
    return (
        sheet.cell(row=row, column=fields.number).value,
        sheet.cell(row=row, column=fields.fif).value,
        sheet.cell(row=row, column=fields.date_dispatch).value
    )

def get_result(sheet, row, fields=item_fields):
    return (
        sheet.cell(row=row, column=fields.applicatility).value,
        sheet.cell(row=row, column=fields.date).value,
        sheet.cell(row=row, column=fields.docnum).value
    )


def set_result(sheet, row, item, fields=result_fields):
    sheet.cell(row=row, column=fields.applicatility).value = item['applicability']
    sheet.cell(row=row, column=fields.docnum).value = item['result_docnum']
    sheet.cell(row=row, column=fields.date).value = item['verification_date']


def insert_result(item, result):
    item['result'] = Result(**result)
    return item

if __name__ == '__main__':
    print('=======================')
    # print(get_data(file))
    rrr = {
        'applicability': 'свидетельство',
        'result_docnum': 'С-АУ/18-07-2024/355476803',
        'verification_date': date.today()
    }
    print(rrr)