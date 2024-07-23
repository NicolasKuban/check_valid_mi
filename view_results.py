import colorama
from colorama import Fore, Back


CONTRACT_ORG = ('ООО "Феррата"', 'ФБУ "Краснодарский ЦСМ"')
colorama.init()


def view(item, number=1):
    if item['applicability']:
        doc = f'{Fore.GREEN}Свидетельство{Fore.RESET}'
    else:
        doc = f'{Fore.RED}Извещение{Fore.RESET}'
    if item['org_title'] in CONTRACT_ORG:
        org_title = f"{Back.GREEN}{item['org_title']}{Back.RESET}"
    else:
        org_title = item['org_title']
    if item['mi_modification']:
        mod = f'\n{' '*6}Модицфикация: {item['mi_modification']}'
    else:
        mod = ''
    result = f'<{number: >2}>. {doc} от {item['verification_date']} выдано {org_title}'

    return result + mod


def change_str(string):
    return "".join(reversed(string.split('.')))

def view_response(response):
    response = sorted(response, key=lambda item: change_str(item['verification_date']) )
    print(f'Найдено результатов поверки - {len(response)}')
    print('-'*80)
    for number, item in enumerate(response, 1):
        print(view(item, number))
        print('-'*80)


if __name__ == '__main__':

    item = {'vri_id': '1-353711079', 
     'org_title': 'ООО "ТАТИНТЕК"', 
     'mit_number': '35279-07', 
     'mit_title': 'Рулетки измерительные металлические', 
     'mit_notation': 'Р2УЗК, Р5УЗК, Р10УЗК', 
     'mi_modification': 'Р2УЗК', 
     'mi_number': '35', 
     'verification_date': '09.07.2024', 
     'valid_date': '08.07.2025', 
     'result_docnum': 'С-ВШК/09-07-2024/353711079', 
     'applicability': True}
    # print(view(item))

    response = [
        {'vri_id': '1-319188877', 'org_title': 'ФБУ "ЦСМ Татарстан"', 'mit_number': '35279-07', 'mit_title': 'Рулетки измерительные металлические', 'mit_notation': 'Р2УЗК, Р5УЗК, Р10УЗК', 'mi_modification': 'Р10УЗК', 'mi_number': '35', 'verification_date': '26.02.2024', 'valid_date': '25.02.2025', 'result_docnum': 'С-АМ/26-02-2024/319188877', 'applicability': True}, 
        {'vri_id': '1-312655156', 'org_title': 'ФБУ "САРАТОВСКИЙ ЦСМ ИМ. Б.А. ДУБОВИКОВА"', 'mit_number': '35279-07', 'mit_title': 'Рулетки измерительные металлические', 'mit_notation': 'Р2УЗК, Р5УЗК, Р10УЗК', 'mi_modification': 'Р2УЗК', 'mi_number': '35', 'verification_date': '30.01.2024', 'valid_date': '29.01.2025', 'result_docnum': 'С-ВУ/30-01-2024/312655156', 'applicability': True}, 
        {'vri_id': '1-316793270', 'org_title': 'ФБУ "ТОМСКИЙ ЦСМ"', 'mit_number': '35279-07', 'mit_title': 'Рулетки измерительные металлические', 'mit_notation': 'Р2УЗК, Р5УЗК, Р10УЗК', 'mi_modification': 'Р2У3К', 'mi_number': '35', 'verification_date': '18.01.2024', 'valid_date': '17.01.2025', 'result_docnum': 'С-ВЭ/18-01-2024/310544977', 'applicability': True}, 
        {'vri_id': '1-314646463', 'org_title': 'ФБУ "Краснодарский ЦСМ"', 'mit_number': '35279-07', 'mit_title': 'Рулетки измерительные металлические', 'mit_notation': 'Р2УЗК, Р5УЗК, Р10УЗК', 'mi_modification': 'Р5УЗК', 'mi_number': '35', 'verification_date': '06.02.2024', 'valid_date': '05.02.2025', 'result_docnum': 'С-АУ/06-02-2024/314646463', 'applicability': True}, 
        {'vri_id': '1-314662380', 'org_title': 'ФБУ "КУРСКИЙ ЦСМ"', 'mit_number': '35279-07', 'mit_title': 'Рулетки измерительные металлические', 'mit_notation': 'Р2УЗК, Р5УЗК, Р10УЗК', 'mi_modification': 'Р10УЗК', 'mi_number': '35', 'verification_date': '06.02.2024', 'valid_date': '05.02.2025', 'result_docnum': 'С-ВА/06-02-2024/314662380', 'applicability': False}, 
        {'vri_id': '1-319895831', 'org_title': 'ФБУ "АЛТАЙСКИЙ ЦСМ"', 'mit_number': '35279-07', 'mit_title': 'Рулетки измерительные металлические', 'mit_notation': 'Р2УЗК, Р5УЗК, Р10УЗК', 'mi_modification': 'Р10УЗК', 'mi_number': '35', 'verification_date': '15.02.2024', 'valid_date': '14.02.2025', 'result_docnum': 'С-АТ/15-02-2024/319895831', 'applicability': True}, 
        {'vri_id': '1-333393368', 'org_title': 'ФБУ "САРАТОВСКИЙ ЦСМ ИМ. Б.А. ДУБОВИКОВА"', 'mit_number': '35279-07', 'mit_title': 'Рулетки измерительные металлические', 'mit_notation': 'Р2УЗК, Р5УЗК, Р10УЗК', 'mi_modification': 'Р10УЗК', 'mi_number': '35', 'verification_date': '19.04.2024', 'valid_date': '18.04.2025', 'result_docnum': 'С-ВУ/19-04-2024/333393368', 'applicability': True}, 
        {'vri_id': '1-338671749', 'org_title': 'ФБУ "КАМЧАТСКИЙ ЦСМ"', 'mit_number': '35279-07', 'mit_title': 'Рулетки измерительные металлические', 'mit_notation': 'Р2УЗК, Р5УЗК, Р10УЗК', 'mi_modification': 'Р10УЗК', 'mi_number': '35', 'verification_date': '16.05.2024', 'valid_date': '15.05.2025', 'result_docnum': 'С-БХ/16-05-2024/338671749', 'applicability': True}, 
        {'vri_id': '1-338671797', 'org_title': 'ФБУ "КАМЧАТСКИЙ ЦСМ"', 'mit_number': '35279-07', 'mit_title': 'Рулетки измерительные металлические', 'mit_notation': 'Р2УЗК, Р5УЗК, Р10УЗК', 'mi_modification': 'Р10УЗК', 'mi_number': '35', 'verification_date': '16.05.2024', 'valid_date': '15.05.2025', 'result_docnum': 'С-БХ/16-05-2024/338671797', 'applicability': False}, 
        {'vri_id': '1-348193452', 'org_title': 'ФБУ "ЦСМ ИМ. А.М. МУРАТШИНА В РЕСПУБЛИКЕ БАШКОРТОСТАН"', 'mit_number': '35279-07', 'mit_title': 'Рулетки измерительные металлические', 'mit_notation': 'Р2УЗК, Р5УЗК, Р10УЗК', 'mi_modification': 'Нет модификации', 'mi_number': '35', 'verification_date': '20.06.2024', 'valid_date': '19.06.2025', 'result_docnum': 'С-АБ/20-06-2024/348193452', 'applicability': True}, 
        {'vri_id': '1-353711079', 'org_title': 'ООО "ТАТИНТЕК"', 'mit_number': '35279-07', 'mit_title': 'Рулетки измерительные металлические', 'mit_notation': 'Р2УЗК, Р5УЗК, Р10УЗК', 'mi_modification': 'Р2УЗК', 'mi_number': '35', 'verification_date': '09.07.2024', 'valid_date': '08.07.2025', 'result_docnum': 'С-ВШК/09-07-2024/353711079', 'applicability': True}, 
        {'vri_id': '1-355476800', 'org_title': 'ФБУ "Краснодарский ЦСМ"', 'mit_number': '35279-07', 'mit_title': 'Рулетки измерительные металлические', 'mit_notation': 'Р2УЗК, Р5УЗК, Р10УЗК', 'mi_modification': 'Р5У3К', 'mi_number': '35', 'verification_date': '18.07.2024', 'valid_date': '17.07.2025', 'result_docnum': 'С-АУ/18-07-2024/355476800', 'applicability': True}, 
        {'vri_id': '1-355695419', 'org_title': 'ФБУ "Краснодарский ЦСМ"', 'mit_number': '35279-07', 'mit_title': 'Рулетки измерительные металлические', 'mit_notation': 'Р2УЗК, Р5УЗК, Р10УЗК', 'mi_modification': 'Р5УЗК', 'mi_number': '35', 'verification_date': '19.07.2024', 'valid_date': '18.07.2025', 'result_docnum': 'С-АУ/19-07-2024/355695419', 'applicability': True}
        ]
    view_response(response)

print(Back.BLUE + Fore.GREEN + "text"+Back.RESET + "Bddd" + Back.RED + "89999" )