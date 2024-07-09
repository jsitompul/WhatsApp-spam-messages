# Name: Whatsapp Spam Message
# Author: Jimmy Sitompul
#MIT License

# Import modul random untuk memilih pesan secara acak
import random
# Import modul pyautogui dengan alias pg untuk melakukan otomatisasi GUI
import pyautogui as pg
# Import modul time untuk mengatur waktu tunda
import time

# Daftar pesan yang akan dikirimkan secara acak
message = ['Cieee penipu', 'Dasar tukang tipu', 'Ketauan nihh yee', 'Lu kurang jago bro hahaha', 'SDM RENDAH']

# Menunggu selama 5 detik sebelum memulai pengiriman pesan
time.sleep(5)

# Loop untuk mengirimkan pesan sebanyak 1000 kali
for i in range(1000):
    # Memilih pesan secara acak dari daftar pesan
    ejekan = random.choice(message)
    # Menulis pesan terpilih ke dalam jendela chat
    pg.write(ejekan)
    # Menekan tombol enter untuk mengirimkan pesan
    pg.press('enter')

