# DoAn4 - Selenium Pytest POM Framework

## Giới thiệu
Dự án kiểm thử tự động cho hệ thống ôn thi, sử dụng Python, Selenium, Pytest và mô hình Page Object Model (POM).

## Cấu trúc thư mục
```
DoAn4/
├── pages/         # Các Page Object cho từng trang web
├── tests/         # Các file test case sử dụng pytest
├── utils/         # Các hàm tiện ích: logger, reporter, screenshot...
├── data/          # Dữ liệu test (CSV, Excel...)
├── reports/       # Kết quả test, log, báo cáo
├── requirements.txt # Danh sách package cần cài
├── .gitignore     # Loại trừ file không cần thiết
├── pytest.ini     # Cấu hình cho pytest
├── README.md      # Giới thiệu dự án
```

## Hướng dẫn cài đặt
```bash
pip install -r requirements.txt
```

## Chạy test
```bash
pytest tests/
```

## Đóng góp
Vui lòng đọc file CONTRIBUTING.md để biết quy tắc đóng góp.

## License
MIT
