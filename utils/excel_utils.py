import openpyxl

def get_data(file, sheet):
    workbook = openpyxl.load_workbook(file)
    sheet_obj = workbook[sheet]
    data = []
    for row in sheet_obj.iter_rows(min_row=2, values_only=True):
        data.append(row)
    return data
