from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def buka_profil(folder_name, posisi_x):
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir=C:\\Temp\\{folder_name}")
    options.add_argument("--profile-directory=Default")
    options.add_argument(f"--window-position={posisi_x},0")

    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("https://www.youtube.com")
        print(f"[{folder_name}] ✅ YouTube dibuka")
        return driver
    except Exception as e:
        print(f"[{folder_name}] ❌ Gagal buka Chrome: {e}")
        return None

# Buka profil pertama
driver1 = buka_profil("nyobaajakok", 0)

# Delay 1 detik
time.sleep(1)

# Buka profil kedua
driver2 = buka_profil("nyobalagi", 400)

input("Tekan Enter jika ingin menutup semua browser...")


# Tutup dua-duanya
if driver1: driver1.quit()
if driver2: driver2.quit()
