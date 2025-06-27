import pyautogui
from PIL import ImageGrab
import time

def pular():
    pyautogui.press('space')

def obstaculo_na_frente(x=640, y=410, largura=60, altura=10):
    img = ImageGrab.grab(bbox=(x, y, x + largura, y + altura))
    img = img.convert('L')
    pixels = img.getdata()
    for pixel in pixels:
        if pixel < 100:
            return True
    return False

print("Bot iniciará em 3 segundos...")
time.sleep(3)                          
pular()

while True:                                          
    if obstaculo_na_frente():
        pular()
    time.sleep(0.01)
