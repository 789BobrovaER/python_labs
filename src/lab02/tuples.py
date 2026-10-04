Record = tuple[str, str, float]
 
 
def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    fio=fio.split()
    fio=fio[0][0].upper()+ fio[0][1:]+' '+fio[1][0].upper()+'.'+ fio[2][0].upper()+'.'

    if gpa>5: raise ValueError
    if len(fio)==0 or len(group)==0:raise ValueError
    gpa=f'GPA {gpa:.2f}'

    return (f'{fio}, гр. {group}, {gpa}')
print(format_record(["  сидорова  анна   сергеевна ", "ABB-01", 3.999]))
