

def view(item):
    doc = 'Свидетельство' if item['applicability'] else 'Извещение'
    result = f"""
Организация: {item['org_title']}
Модицфикация: {item['mi_modification']}
{doc} от {item['verification_date']}
"""
    return result
    

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
    print(view(item))