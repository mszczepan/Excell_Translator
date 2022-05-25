import openpyxl


def open_file(path):
    wb = openpyxl.load_workbook(path)
    return wb


def read_file(wb, sheet, column, start_row, end_row):
    ws = wb[sheet]
    read_list = [ws[column + str(row)].value for row in range(start_row, end_row)]
    return read_list

