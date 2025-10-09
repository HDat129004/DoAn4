import os
import csv
from openpyxl import load_workbook

# Lấy thư mục gốc của project
BASE_DIR = r"C:\Users\Admin\Desktop\DoAn4"

def read_csv(filename):
    """Đọc dữ liệu từ CSV trong thư mục project"""
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


def read_excel(filename, sheet_name=None):
    """Đọc dữ liệu từ Excel trong thư mục project"""
    filepath = os.path.join(BASE_DIR, filename)
    wb = load_workbook(filename=filepath, data_only=True)
    sheets = [sheet_name] if sheet_name else wb.sheetnames
    data = {}

    for sheet in sheets:
        ws = wb[sheet]
        headers = [cell.value for cell in ws[1]]
        rows = []
        for row in ws.iter_rows(min_row=2, values_only=True):
            if any(row):  # Bỏ qua hàng trống
                rows.append(dict(zip(headers, row)))
        data[sheet] = rows

    return data[sheet_name] if sheet_name else data



