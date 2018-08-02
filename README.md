# Perapor Kurtilas

Pengisi Rapor Kurikulum 2013

Sebuah alat bantu yang dapat digunakan oleh guru yang menggunakan kurikulum 2013

## Cara menjalankan
### Menggunakan python
1. Jalankan `app.py` dalam virtual environment yang telah disediakan
2. Buka browser, arahkan ke `http://127.0.0.1:port`
### Tanpa menggunakan python
1. Jalankan `app` yang sebelumnya telah dibuat oleh PyInstaller (cara dibawah)
2. Buka browser, arahkan ke `http://127.0.0.1:port`

## Menjalankan di komputer lain tanpa Python
Agar dapat berjalan di komputer lain tanpa menggunakan python, semua berkas harus dikumpulkan dan dibuat _executable_ menggunakan [PyInstaller](https://pythonhosted.org/PyInstaller/operating-mode.html).
Pembuatan _executable_ harus menggunakan komputer dengan sistme operasi yang __sama dengan komputer target__.

Untuk mempermudah pembuatan, dapat digunakan `specfile` yang disediakan, dengan menjalankan PyInstaller dengan perintah dibawah ini
```pyinstaller app.spec``` 

## Pengaturan
Terdapat berkas `config.txt` yang dapat digunakan untuk menentukan _bind address_, _port_, serta mode server (_debug_ atau tidak)

Setelan asali :
- Host : `0.0.0.0`
- Port : `12345`
- Debug : `0`