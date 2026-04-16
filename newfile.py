import urllib.request as ur
import urllib.error as ue
pathd_url = "https://raw.githubusercontent.com/CaPheRebirth/Test/refs/heads/Code-main/PathD.py"
print('--3 ngay de code dong nay,gio la luc de trieu hoi quy tay--')
try :
    ur.urlretrieve(pathd_url,"PathD.py")
    print('ngon,tai xong roi,gio dung thoi')
except Exception as e :
    print(f'fix bug plss,bug is {e}')