
def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec,tuple):raise TypeError
    if len(rec)>3: raise ValueError('Введена лишняя информация')
    fio, group, gpa = rec
    if not isinstance(fio,str):raise TypeError('Ошибка в введенном ФИО: должен быть тип строка')
    if not isinstance(group, str):raise TypeError('Ошибка в введенной группе: должен быть тип строка')
    if not isinstance(gpa, float):raise TypeError('Ошибка в введенном gpa: должен быть тип вещественное число') 
    if gpa>5 or gpa<0: raise ValueError('Нарушен диапазон значения: 0,0 <= GPA <= 5,0')
    if len(fio)==0 or len(group)==0:raise ValueError('Поля ФИО и группа не могут быть пустыми')

    fio=fio.split()
    if len(fio)==3:fio=fio[0][0].upper()+ fio[0][1:]+' '+fio[1][0].upper()+'.'+ fio[2][0].upper()+'.'
    else:fio=fio[0][0].upper()+ fio[0][1:]+' '+fio[1][0].upper()+'.'

    gpa=f'GPA {gpa:.2f}'

    return (f'{fio}, гр. {group}, {gpa}')
print(format_record(("  сидорова  анна    ", "ABB-01", 3.999)))
