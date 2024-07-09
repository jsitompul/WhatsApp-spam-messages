
# WhatsApp Spam Message (Written in Indonesian)

Script ini dibuat untuk mengirimkan pesan spam secara otomatis melalui WhatsApp Web, terutama ditujukan untuk MELAWAN dan MENGGANGGU `scammer` atau `penipu`. Script ini menggunakan `pyautogui` untuk melakukan otomatisasi input pesan di WhatsApp Web.

## PERINGATAN! 🛑🛑
Penggunaan script ini untuk mengirim spam dapat melanggar ketentuan layanan dari WhatsApp dan dapat mengakibatkan pemblokiran akun. JANGAN GUNAKAN KODE INI TANPA IZIN. Setelah mendapat izin, gunakan dengan bijak dan bertanggung jawab. 

## Persyaratan

- Python 3.x
- Modul `pyautogui`
- Modul `time`

## Instalasi

1. Clone repositori ini:
   ```bash
   git clone https://github.com/username/WhatsAppSpamMessage.git

2. Install modul yang diperlukan:
   ```bash
   pip install pyautogui

## Penggunaan

1. Buka WhatsApp Web di browser Anda dan buka chat dengan scammer atau penipu yang ingin Anda kirimi spam pesan.

2. Jalankan script Python:
    ```bash
   python spam_message.py

3. Anda akan memiliki waktu 5 detik untuk kembali ke jendela chat WhatsApp Web sebelum script mulai mengirim pesan spam.
  
4. Script akan mengirimkan pesan secara berulang sebanyak 1000 kali. Anda dapat mengubah jumlah pesan dengan mengubah nilai pada `for i in range(1000)`.

## Kode

```bash
# Author: Jimmy Sitompul

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
```



