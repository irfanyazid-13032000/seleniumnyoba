from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from threading import Thread
import time

# Daftar folder & posisi window
profiles = [
    ("nyobaajakok", 0),
    ("nyobalagi", 400),
]

def buka_dan_klik(folder_name, posisi_x):
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir=C:\\Temp\\{folder_name}")
    options.add_argument("--profile-directory=Default")
    options.add_argument(f"--window-position={posisi_x},0")

    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("https://www.rapidtables.com/tools/click-test.html?t=1")
        tombol = driver.find_element(By.ID, "addbtn")
        for _ in range(100):
            tombol.click()
        print(f"[{folder_name}] ✅ Klik 100x selesai")
        input(f"[{folder_name}] Tekan Enter untuk menutup...")
        driver.quit()
    except Exception as e:
        print(f"[{folder_name}] ❌ Error: {e}")

# Jalankan semuanya paralel
threads = []
for folder, pos in profiles:
    t = Thread(target=buka_dan_klik, args=(folder, pos))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
