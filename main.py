import pyautogui
import time
import keyboard  # pip install keyboard

print("Tahan SHIFT untuk auto-click terus menerus. Tekan ESC untuk keluar.")

try:
    while True:
        if keyboard.is_pressed('esc'):
            print("Dihentikan oleh pengguna.")
            break

        if keyboard.is_pressed('shift'):
            while keyboard.is_pressed('shift'):
                pyautogui.click()
                # time.sleep(0.00000001) 
        else:
            time.sleep(0.01)  # hemat CPU

except KeyboardInterrupt:
    print("Dihentikan dengan Ctrl+C.")
