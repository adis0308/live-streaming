# Author: GDPlayer.to
# Menjalankannya pakai perintah: nohup python3 main.py > output.log 2>&1 &
# Syarat sistem: ffmpeg 5+, python 3+

import os
import subprocess

current_dir = os.getcwd()
files_dir = 'files'
tmp_dir = 'tmp'
data_file = 'data.txt'

def jalankanFFmpeg(link, output_dir, ip='[2606:4700:3034::ac43:bd57]'):
    index_file = 'index.m3u8'
    output_segment = os.path.join(current_dir, files_dir, output_dir, 'segment_%Y-%m-%d_%H-%M-%S.ts')
    output_index = os.path.join(current_dir, files_dir, output_dir, index_file)

    # Menyimpan file log pada folder tmp dengan nama sesuai output_dir untuk identifikasi
    log_file = os.path.join(current_dir, tmp_dir, f'ffmpeg_output_{output_dir}.log')

    # Periksa apakah ffmpeg sudah berjalan pada folder ini
    check_command = f"pgrep -f '{output_index}'"
    existing_process = subprocess.run(check_command, shell=True, capture_output=True, text=True)
    
    # Jika tidak ada proses yang berjalan pada output folder ini, jalankan ffmpeg
    if existing_process.stdout == '':
        ffmpeg_command = [
            'ffmpeg',
            '-reconnect', '1',
            '-reconnect_at_eof', '1',
            '-reconnect_streamed', '1', 
            '-reconnect_delay_max', '5',
            '-headers', 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            '-headers', f'cf-connecting-ip: {ip}',
            '-headers', f'x-forwarded-for: {ip}',
            '-i', link,
            '-c', 'copy',
            '-f', 'hls',
            '-hls_time', '4',
            '-hls_list_size', '10',
            '-hls_flags', 'delete_segments+append_list',
            '-strftime', '1',
            '-hls_segment_filename', output_segment, 
            output_index
        ]
        # Membuka file log untuk menulis output ffmpeg
        with open(log_file, 'w') as file_log:
            # Menjalankan proses ffmpeg di latar belakang dengan output diarahkan ke file_log
            subprocess.Popen(ffmpeg_command, stdout=file_log, stderr=file_log)
    else:
        print(f"Proses FFmpeg sudah berjalan untuk folder {output_dir}")

# Buat folder files dan tmp
os.makedirs(os.path.join(current_dir, files_dir), exist_ok=True)
os.makedirs(os.path.join(current_dir, tmp_dir), exist_ok=True)

# Baca file data.txt dan jalankan proses untuk setiap baris
with open(data_file) as file:
    lines = file.readlines()
    for line in lines:
        ex = line.split('|')
        link = ex[0].strip()
        dirname = ex[1].strip()
        ip = ex[2].strip()
        
        # Buat folder jika belum ada
        os.makedirs(os.path.join(current_dir, files_dir, dirname), exist_ok=True)
        
        # Jalankan ffmpeg jika belum ada proses untuk folder ini
        jalankanFFmpeg(link, dirname, ip)
