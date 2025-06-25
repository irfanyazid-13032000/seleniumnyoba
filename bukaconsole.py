import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from threading import Thread

profiles = [
    ("nyobaajakok", 0),
    ("nyobalagi", 400),
]

SPAMMER_JS = """
let countol = 0;
let spammer = setInterval(() => {
  const btn = document.querySelector("#addbtn");
  if (btn) {
    const evt = new MouseEvent("mouseup", {
      bubbles: true,
      cancelable: true,
      view: window
    });
    btn.dispatchEvent(evt);
    countol++;
    console.log("🖱️ MouseUp:", countol);
  } else {
    console.log("❌ Tombol tidak ditemukan");
    clearInterval(spammer);
  }
}, 1);

window.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    clearInterval(spammer);
    console.log("🛑 Auto-click dihentikan dengan ESC");
  }
});
"""

def buka_dan_inject(folder_name, posisi_x):
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir=C:\\Temp\\{folder_name}")
    options.add_argument("--profile-directory=Default")
    options.add_argument(f"--window-position={posisi_x},0")

    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.set_window_size(400, 800)  # ✅ Lebar 400px, tinggi 800px
        driver.get("https://www.rapidtables.com/tools/click-test.html?t=1")

        time.sleep(2)
        driver.execute_script(SPAMMER_JS)
        print(f"[{folder_name}] ✅ JavaScript spammer diinject!")

        input(f"[{folder_name}] Tekan Enter jika ingin menutup browser...")
        driver.quit()
    except Exception as e:
        print(f"[{folder_name}] ❌ Error: {e}")

# Jalankan paralel
threads = []
for folder, pos in profiles:
    t = Thread(target=buka_dan_inject, args=(folder, pos))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
