Record = tuple[str, str, float]
 
 
def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    fio=fio.split()
    if len(fio)==3:fio=fio[0][0].upper()+ fio[0][1:]+' '+fio[1][0].upper()+'.'+ fio[2][0].upper()+'.'
    else:fio=fio[0][0].upper()+ fio[0][1:]+' '+fio[1][0].upper()+'.'

    if gpa>5 or gpa<0: raise ValueError('0,0 <= GPA <= 5,0')
    if len(fio)==0 or len(group)==0:raise ValueError('Поля ФИО и группа не могут быть пустыми')
    gpa=f'GPA {gpa:.2f}'

    return (f'{fio}, гр. {group}, {gpa}')
print(format_record(["  сидорова  анна    ", "ABB-01", 3.999]))
