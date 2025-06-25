from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def buka_profil(folder_name, posisi_x):
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir=C:\\Temp\\{folder_name}")
    options.add_argument("--profile-directory=Default")
    options.add_argument(f"--window-position={posisi_x},0")

    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("https://www.rapidtables.com/tools/click-test.html?t=1")
        print(f"[{folder_name}] ✅ Halaman dibuka")
        return driver
    except Exception as e:
        print(f"[{folder_name}] ❌ Gagal buka Chrome: {e}")
        return None

def klik_100_kali(driver):
    try:
        tombol = driver.find_element(By.ID, "addbtn")
        for i in range(100):
            tombol.click()
        print("✅ Klik 100x selesai")
    except Exception as e:
        print(f"❌ Gagal klik tombol: {e}")

# Buka profil pertama
driver1 = buka_profil("nyobaajakok", 0)
time.sleep(1)

# Buka profil kedua
driver2 = buka_profil("nyobalagi", 400)
time.sleep(1)

# Klik tombol 100x di masing-masing browser
if driver1:
    klik_100_kali(driver1)

if driver2:
    klik_100_kali(driver2)

input("Tekan Enter jika ingin menutup semua browser...")

if driver1: driver1.quit()
if driver2: driver2.quit()
