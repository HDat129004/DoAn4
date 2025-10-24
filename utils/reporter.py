import csv

class Reporter:
    def __init__(self, file="report.csv"):
        self.file = file
        with open(self.file, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(["Câu", "Đáp án chọn", "Kết quả"])

    def add_result(self, cau, dap_an, ket_qua):

        with open(self.file, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow([cau, dap_an, ket_qua])
