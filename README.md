# Tutorial video restreaming dengan ffmpeg + python
## Cara Kerja main.py
1. Buat folder files dan tmp;
2. Membaca file data.txt dan mengekstraknya perbaris;
3. Jalankan FFMpeg di latar belakang dan simpan ke dalam folder /files/nama folder/ dan output lognya akan disimpan ke /tmp/ffmpeg_output_nama folder.log;
4. Selesai.

Catatan
---
- Kamu bisa mengakses file dengan url http://situskamu.com/files/nama folder/index.m3u8;
- Pastikan kamu telah menginstall nginx pada server dan mengaturnya supaya dapat diakses;
- Kamu bisa juga menggunakan php untuk mengamankan file index.m3u8 dengan token dan membacanya fitur nginx x-sendfile.
