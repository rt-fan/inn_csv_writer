import csv


def get_inn(inn):
    with open('kl_to_1c.txt', 'r') as file:
        lines_iter = iter(file.readlines())

    pl_kpp = ''
    pl_rasch_schet = ''
    pl_bank = ''
    pl_bik = ''

    for line in lines_iter:
        if inn in line:
            pl_kpp = next(lines_iter, None).split("=")[1].strip()
            pl_rasch_schet = next(lines_iter, None).split("=")[1].strip()
            pl_bank = next(lines_iter, None).split("=")[1].strip()
            pl_bik = next(lines_iter, None).split("=")[1].strip()
            break
    return pl_kpp, pl_rasch_schet, pl_bank, pl_bik


with open('list.csv', newline='', encoding='windows-1251') as csvfile, open('output.csv', 'w', newline='', encoding='windows-1251') as csvfile_write:
    reader = csv.reader(csvfile, delimiter=';')
    writer = csv.writer(csvfile_write, delimiter=';', lineterminator="\r")
    for row in reader:
        kpp, schet, bank, bik = get_inn(row[1])
        row.append(kpp)
        row.append(schet)
        row.append(bank)
        row.append(bik)
        writer.writerow(row)
