# Cách chạy source code:
## 1. Trong folder "testcases" - folder chứa các file test case:
- Có $n$ file test case với định dạng `input<i>.txt`, với $1 \leq i \leq n$.
- Sau khi chạy file main.py, kết quả giải ra sẽ được lưu vào file `output<i>.txt` tương ứng với mỗi file `input<i>.txt`.
## 2. Trong hàm main() của file main.py:
- Thay đổi giá trị của biến `test_case_folder` để thay đổi đường dẫn đến folder chứa các file test case (nếu cần).
- Thay đổi giá trị của biến `test_case_number` để thay đổi số lượng file test case (nếu cần).
## 3. Chạy file main.py:
- **B0**: Cài các thư viện cần thiết trong file. (Nếu đã làm rồi thì những lần chạy sau bắt đầu ở **B1**)
- **B1**: Mở terminal/command prompt.
- **B2**: Di chuyển đến folder chứa file main.py.
- **B3**: Chạy lệnh `python main.py` để giải các file test case trong folder "testcases".