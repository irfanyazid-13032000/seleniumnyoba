import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from threading import Thread

# Daftar folder & posisi window
profiles = [
    ("nyobaajakok", 0),
    ("nyobalagi", 400),
]

def buka_dan_klik(folder_name, posisi_x, durasi_detik=1):
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir=C:\\Temp\\{folder_name}")
    options.add_argument("--profile-directory=Default")
    options.add_argument(f"--window-position={posisi_x},0")

    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("https://www.rapidtables.com/tools/click-test.html?t=1")

        tombol = driver.find_element(By.ID, "addbtn")

        start = time.time()
        count = 0
        while time.time() - start < durasi_detik:
            tombol.click()
            count += 1

        print(f"[{folder_name}] ✅ Klik selama {durasi_detik}s, total klik: {count}")
        input(f"[{folder_name}] Tekan Enter untuk menutup...")
        driver.quit()
    except Exception as e:
        print(f"[{folder_name}] ❌ Error: {e}")

# Jalankan semuanya paralel
threads = []
for folder, pos in profiles:
    t = Thread(target=buka_dan_klik, args=(folder, pos, 1))  # 1 detik
    t.start()
    threads.append(t)

for t in threads:
    t.join()
