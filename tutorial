# Tool Restreaming Video Selain FFMpeg

Selain FFmpeg, ada beberapa alat yang bisa Anda pertimbangkan untuk melakukan restreaming video HLS live ke HLS live dengan performa yang lebih ringan, khususnya jika Anda ingin meminimalkan penggunaan CPU. Berikut beberapa alternatif yang layak dipertimbangkan:

### 1. **NGINX dengan Modul RTMP (NGINX-RTMP)**
   - **Deskripsi**: NGINX-RTMP adalah modul untuk NGINX yang dapat digunakan untuk transmuxing (mengubah format container) dari RTMP ke HLS tanpa melakukan transcoding, sehingga jauh lebih ringan dibandingkan FFmpeg.
   - **Kelebihan**: Tidak melakukan transcoding, sehingga sangat hemat CPU. Cocok untuk melakukan transmuxing dari satu protokol ke protokol lain.
   - **Cara Kerja**: Anda bisa menyiarkan stream RTMP yang kemudian dikonversi menjadi HLS menggunakan modul ini. Namun, karena tidak ada transcoding, resolusi atau bitrate tidak akan diubah.
   - **Cocok untuk**: Restreaming HLS ke HLS dengan konfigurasi yang sama (tanpa penurunan resolusi atau pengubahan bitrate).

### 2. **GStreamer**
   - **Deskripsi**: GStreamer adalah framework media open-source yang fleksibel, yang bisa digunakan untuk melakukan berbagai tugas terkait streaming, termasuk restreaming HLS.
   - **Kelebihan**: Dapat dikonfigurasi untuk hanya melakukan transmuxing HLS ke HLS, tanpa transcoding, sehingga sangat menghemat sumber daya CPU.
   - **Cara Kerja**: Menggunakan pipeline sederhana untuk menangkap stream HLS dan mengeluarkannya kembali dalam format HLS yang sama. Dapat disesuaikan untuk berbagai kebutuhan pengaliran.
   - **Cocok untuk**: Pengguna dengan latar belakang teknis yang cukup baik karena konfigurasi GStreamer bisa lebih kompleks dibandingkan alat lain.

### 3. **Nimble Streamer**
   - **Deskripsi**: Nimble Streamer adalah server streaming ringan yang mendukung transmuxing HLS ke HLS dan RTMP ke HLS. 
   - **Kelebihan**: Tidak membutuhkan banyak sumber daya dan dapat digunakan untuk transmuxing, transmisi ulang, serta mendukung penyesuaian CDN.
   - **Cara Kerja**: Nimble Streamer dapat menangani streaming langsung dari HLS atau protokol lainnya dan mengonversinya tanpa transcoding. Antarmuka yang cukup mudah digunakan untuk pengaturan dasar.
   - **Cocok untuk**: Solusi restreaming dengan konsumsi daya rendah dan skalabilitas yang baik.

### 4. **Node Media Server**
   - **Deskripsi**: Node Media Server adalah server streaming berbasis Node.js yang mendukung protokol seperti RTMP, HLS, dan DASH.
   - **Kelebihan**: Ringan karena berbasis Node.js, mendukung transmuxing dan memungkinkan penyesuaian melalui JavaScript.
   - **Cara Kerja**: Anda dapat menggunakan Node Media Server untuk menerima RTMP atau HLS dan mengeluarkan kembali sebagai HLS. Namun, Node Media Server lebih cocok untuk transmuxing daripada transcoding.
   - **Cocok untuk**: Restreaming berbasis HLS yang fleksibel dan ringan dengan penyesuaian menggunakan Node.js.

### 5. **SRS (Simple Realtime Server)**
   - **Deskripsi**: SRS adalah server media yang mendukung RTMP, WebRTC, dan HLS, serta cukup ringan dan cepat.
   - **Kelebihan**: Efisien dalam penggunaan sumber daya, mendukung transmuxing RTMP ke HLS dan transmisi ulang stream HLS ke HLS.
   - **Cara Kerja**: SRS memungkinkan streaming langsung tanpa transcoding dengan mengkonversi RTMP ke HLS atau stream HLS ke HLS secara efisien.
   - **Cocok untuk**: Kebutuhan restreaming HLS dengan beban ringan pada CPU.

### Kesimpulan
Jika Anda hanya perlu transmuxing HLS ke HLS tanpa perubahan bitrate atau resolusi, **NGINX-RTMP**, **Nimble Streamer**, dan **SRS** adalah pilihan yang sangat ringan dan lebih hemat CPU dibandingkan FFmpeg. Namun, jika Anda memerlukan penyesuaian lebih lanjut atau pengelolaan tambahan, **GStreamer** dan **Node Media Server** juga bisa dipertimbangkan.

## NGINX dengan Modul RTMP (NGINX-RTMP)

Berikut adalah cara dan konfigurasi untuk melakukan restreaming video HLS live ke HLS live menggunakan **NGINX dengan modul RTMP**. Dalam contoh ini, NGINX-RTMP akan digunakan untuk menerima stream dari sumber dan mengubahnya menjadi format HLS tanpa melakukan transcoding, sehingga penggunaan CPU tetap minimal.

### Langkah 1: Instalasi NGINX dengan Modul RTMP

1. **Install dependensi** (contoh di Ubuntu):
   ```bash
   sudo apt update
   sudo apt install -y build-essential libpcre3 libpcre3-dev libssl-dev zlib1g-dev
   ```

2. **Unduh NGINX dan modul RTMP**:
   ```bash
   wget http://nginx.org/download/nginx-1.20.1.tar.gz
   wget https://github.com/arut/nginx-rtmp-module/archive/master.zip
   ```

3. **Ekstrak file**:
   ```bash
   tar -zxvf nginx-1.20.1.tar.gz
   unzip master.zip
   ```

4. **Kompilasi NGINX dengan modul RTMP**:
   ```bash
   cd nginx-1.20.1
   ./configure --with-http_ssl_module --add-module=../nginx-rtmp-module-master
   make
   sudo make install
   ```

5. **Jalankan NGINX**:
   ```bash
   sudo /usr/local/nginx/sbin/nginx
   ```

### Langkah 2: Konfigurasi NGINX-RTMP untuk Restreaming HLS

Setelah instalasi selesai, kita akan mengatur `nginx.conf` untuk menerima dan mengeluarkan HLS stream.

1. **Edit file konfigurasi NGINX**:
   Lokasi file konfigurasi biasanya di `/usr/local/nginx/conf/nginx.conf`. Buka file tersebut dengan editor teks:

   ```bash
   sudo nano /usr/local/nginx/conf/nginx.conf
   ```

2. **Tambahkan blok konfigurasi RTMP dan HLS**:
   Tambahkan konfigurasi berikut untuk melakukan restreaming HLS.

   ```nginx
   # nginx.conf

   # HTTP server untuk mengakses HLS stream
   http {
       include       mime.types;
       default_type  application/octet-stream;

       server {
           listen 8080;
           server_name localhost;

           location /hls {
               # Folder untuk menyimpan segmen HLS
               types {
                   application/vnd.apple.mpegurl m3u8;
                   video/mp2t ts;
               }
               root /tmp;  # Sesuaikan folder root sesuai kebutuhan Anda
               add_header Cache-Control no-cache;
           }
       }
   }

   # RTMP server untuk menerima dan memproses stream
   rtmp {
       server {
           listen 1935;  # Port RTMP

           application live {
               live on;

               # Output HLS stream
               hls on;
               hls_path /tmp/hls;   # Lokasi output HLS segmen
               hls_fragment 5s;      # Durasi tiap segmen HLS
               hls_playlist_length 60s;  # Durasi playlist HLS

               # Sesuaikan nama stream di URL input
               allow play all;  # Izinkan akses untuk semua klien
           }
       }
   }
   ```

   **Penjelasan**:
   - `hls_path`: Lokasi tempat NGINX-RTMP menyimpan segmen HLS (.ts) dan daftar playlist (.m3u8).
   - `hls_fragment`: Durasi setiap segmen HLS (misalnya 5 detik).
   - `hls_playlist_length`: Durasi daftar playlist HLS.
   - **URL Akses**: Setelah konfigurasi, stream HLS akan tersedia di `http://your_server_ip:8080/hls/stream_name.m3u8`.

3. **Simpan dan tutup file konfigurasi**.

4. **Restart NGINX** untuk menerapkan konfigurasi baru:
   ```bash
   sudo /usr/local/nginx/sbin/nginx -s reload
   ```

### Langkah 3: Menyiarkan Stream ke NGINX

Anda sekarang dapat mengirimkan stream video ke NGINX-RTMP menggunakan FFmpeg atau aplikasi lain yang mendukung RTMP.

Misalnya, menggunakan FFmpeg untuk menyiarkan stream dari URL HLS ke RTMP server:

```bash
ffmpeg -i https://source-url/stream.m3u8 -c copy -f flv rtmp://your_server_ip/live/stream_name
```

**Penjelasan**:
- `-i https://source-url/stream.m3u8`: URL sumber HLS yang ingin Anda restream.
- `-c copy`: Menyalin codec asli tanpa melakukan transcoding (lebih hemat CPU).
- `-f flv rtmp://your_server_ip/live/stream_name`: URL RTMP tujuan di NGINX-RTMP untuk restreaming.

### Langkah 4: Mengakses Stream HLS

Setelah streaming berhasil, Anda dapat mengakses stream HLS hasil restreaming dari URL berikut:

```
http://your_server_ip:8080/hls/stream_name.m3u8
```

**Catatan**: Gantilah `your_server_ip` dan `stream_name` dengan IP server NGINX Anda dan nama stream yang Anda pilih.

### Tips dan Optimasi

1. **Gunakan Cache dan CDN**: Untuk distribusi stream yang lebih efisien, gunakan cache dan CDN, terutama jika Anda memiliki banyak pemirsa.
2. **Monitoring Koneksi**: NGINX-RTMP tidak memiliki dashboard GUI, tetapi Anda bisa menambahkan `stat` module untuk memantau sesi.
3. **Pemeliharaan Direktori HLS**: Secara berkala hapus file .ts dan .m3u8 lama di direktori HLS agar tidak memenuhi disk.

Dengan setup ini, NGINX-RTMP dapat menangani restreaming HLS ke HLS secara efisien dan hemat CPU, terutama karena tidak melakukan transcoding.

## GStreamer

Untuk melakukan **restreaming video HLS live ke HLS live** menggunakan **GStreamer**, Anda dapat memanfaatkan pipeline GStreamer yang memungkinkan transmuxing HLS dari satu sumber ke tujuan lainnya. GStreamer adalah framework media yang kuat, dan meskipun GStreamer lebih sering digunakan untuk berbagai operasi video, ia dapat digunakan untuk mengalirkan video tanpa perlu transcoding.

Berikut adalah langkah-langkah dan pengaturan yang diperlukan untuk melakukan restreaming HLS ke HLS menggunakan GStreamer:

### Langkah 1: Instalasi GStreamer
Jika Anda belum menginstal GStreamer di server Anda, Anda perlu menginstalnya terlebih dahulu.

1. **Instal GStreamer pada sistem berbasis Ubuntu**:
   ```bash
   sudo apt update
   sudo apt install -y gstreamer1.0-tools gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav
   ```

2. **Periksa instalasi GStreamer**:
   Setelah GStreamer terinstal, Anda dapat memverifikasi instalasi dengan menjalankan perintah berikut:
   ```bash
   gst-launch-1.0 --version
   ```

### Langkah 2: Konfigurasi Restreaming HLS ke HLS menggunakan GStreamer

Setelah GStreamer terinstal, kita dapat membuat pipeline GStreamer untuk menerima stream HLS dari sumber dan menyiarkannya kembali sebagai HLS.

1. **Perintah GStreamer untuk Restreaming HLS**:

   GStreamer menyediakan kemampuan untuk transmuxing HLS, yang berarti kita dapat mengubah stream HLS menjadi HLS lainnya tanpa mengubah codec atau melakukan transcoding.

   Berikut adalah contoh perintah GStreamer yang digunakan untuk menerima stream HLS dan menyiarkannya kembali sebagai HLS:

   ```bash
   gst-launch-1.0 \
   playbin uri=http://source-url/stream.m3u8 \
   ! hlsdemux \
   ! queue \
   ! mpegtsmux \
   ! hlssink location=/path/to/output/hls/segment_%05d.ts playlist-location=/path/to/output/hls/playlist.m3u8
   ```

   **Penjelasan**:
   - **`playbin uri=http://source-url/stream.m3u8`**: Sumber stream HLS yang akan diambil.
   - **`hlsdemux`**: Demuxer untuk stream HLS.
   - **`queue`**: Memungkinkan pemrosesan secara paralel, menjaga aliran stream tetap stabil.
   - **`mpegtsmux`**: Multiplexer untuk membuat kembali stream dalam format MPEG-TS.
   - **`hlssink`**: Sink GStreamer untuk menghasilkan stream HLS. Anda dapat menentukan lokasi untuk file segment `.ts` dan playlist `.m3u8` di direktori output.

2. **Parameter hlsdemux**: 
   Anda dapat menyesuaikan berbagai parameter `hlsdemux` untuk mengatur durasi segmen, playlist, dan sebagainya. Misalnya:
   - **`playlist-length`**: Menentukan panjang playlist (dalam detik).
   - **`target-duration`**: Durasi segmen HLS.
   - **`location`**: Lokasi penyimpanan file segmen `.ts` yang akan dihasilkan.

3. **Contoh dengan pengaturan durasi dan playlist**:
   ```bash
   gst-launch-1.0 \
   playbin uri=http://source-url/stream.m3u8 \
   ! hlsdemux \
   ! queue \
   ! mpegtsmux \
   ! hlssink target-duration=5 location=/path/to/output/hls/segment_%05d.ts playlist-location=/path/to/output/hls/playlist.m3u8
   ```

   **Penjelasan**:
   - **`target-duration=5`**: Setiap segmen HLS akan memiliki durasi 5 detik.
   - **`playlist-location`**: Lokasi file playlist `.m3u8` yang baru.

### Langkah 3: Jalankan Perintah Restreaming

Untuk menjalankan restreaming, cukup jalankan perintah di terminal yang sesuai dengan pengaturan yang telah ditentukan.

- **Contoh 1**:
  Jika Anda hanya ingin mengalirkan stream HLS dari sumber ke output HLS tanpa mengubah pengaturan apa pun:

  ```bash
  gst-launch-1.0 \
  playbin uri=http://source-url/stream.m3u8 \
  ! hlsdemux \
  ! queue \
  ! mpegtsmux \
  ! hlssink location=/path/to/output/hls/segment_%05d.ts playlist-location=/path/to/output/hls/playlist.m3u8
  ```

- **Contoh 2**:
  Jika Anda ingin menyesuaikan durasi segmen HLS:

  ```bash
  gst-launch-1.0 \
  playbin uri=http://source-url/stream.m3u8 \
  ! hlsdemux \
  ! queue \
  ! mpegtsmux \
  ! hlssink target-duration=10 location=/path/to/output/hls/segment_%05d.ts playlist-location=/path/to/output/hls/playlist.m3u8
  ```

### Langkah 4: Mengakses Stream HLS yang Dihasilkan

Setelah stream berhasil disiarkan ulang (restream), Anda dapat mengakses stream HLS baru melalui URL HLS yang sudah disediakan, seperti:

```
http://your-server-ip/path/to/output/hls/playlist.m3u8
```

**Catatan**: Gantilah `your-server-ip` dengan IP server atau domain tempat Anda menyimpan stream HLS yang dihasilkan.

### Tips dan Optimasi

- **Optimasi I/O**: Jika server Anda memiliki banyak pemirsa, pastikan Anda menggunakan penyimpanan SSD atau sistem I/O yang cepat untuk menangani banyak segmen HLS.
- **Distribusi CDN**: Untuk skala besar, Anda dapat mempertimbangkan menggunakan CDN untuk mendistribusikan stream HLS agar lebih efisien dan mengurangi beban pada server utama.
- **Pemantauan**: GStreamer tidak memiliki antarmuka pemantauan GUI secara default, tetapi Anda dapat memonitor proses menggunakan alat seperti `top`, `htop`, atau `systemd` untuk memastikan server tidak kelebihan beban.

Dengan menggunakan GStreamer, Anda dapat melakukan restreaming HLS ke HLS dengan cukup ringan tanpa perlu transcoding, serta memberikan fleksibilitas dalam pengaturan segmentasi dan playlist.

## Nimble Streamer

Untuk melakukan **restreaming HLS live ke HLS live** menggunakan **Nimble Streamer**, Anda dapat mengikuti langkah-langkah di bawah ini. Nimble Streamer adalah server media yang ringan dan efisien, dirancang untuk streaming HLS, RTMP, MPEG-DASH, dan format lainnya. Dengan Nimble Streamer, Anda dapat mengonfigurasi server untuk mengambil aliran HLS dari sumber dan kemudian menyiarkannya kembali ke pelanggan sebagai stream HLS.

### Langkah 1: Instalasi Nimble Streamer

1. **Unduh dan Instal Nimble Streamer**:
   Anda perlu mengunduh Nimble Streamer dan menginstalnya di server Anda. Nimble Streamer dapat diinstal di berbagai sistem operasi seperti Linux (Ubuntu, CentOS, dll.).

   - Kunjungi halaman resmi Nimble Streamer di [Softvelum](https://softvelum.com/nimble/) dan unduh versi terbaru sesuai dengan sistem operasi Anda.
   - Ikuti petunjuk instalasi yang tersedia di situs mereka.

2. **Verifikasi Instalasi**:
   Setelah diinstal, verifikasi apakah Nimble Streamer berjalan dengan benar dengan membuka URL admin di browser:
   ```
   http://<server-ip>:8080
   ```

   Biasanya, port `8080` digunakan untuk antarmuka web administratif.

### Langkah 2: Mengonfigurasi Restreaming HLS ke HLS

Untuk mengonfigurasi **restreaming HLS ke HLS**, Anda perlu mengonfigurasi Nimble Streamer agar mengambil aliran HLS dari sumber dan kemudian menyiarkannya kembali ke output HLS.

1. **Tambahkan Sumber HLS (Input Stream)**:
   Pada halaman konfigurasi Nimble Streamer, Anda perlu menambahkan **sumber input stream HLS** yang ingin Anda restream.

   - Buka antarmuka web Nimble Streamer di `http://<server-ip>:8080`.
   - Pilih menu **Live Streams** di bagian kiri.
   - Klik **Add stream** dan pilih **HLS** sebagai jenis input.
   - Masukkan URL stream HLS sumber yang ingin Anda terima (misalnya, `http://source-url/stream.m3u8`).

2. **Menyiarkan Stream HLS Kembali (Output Stream)**:
   Setelah Anda menambahkan sumber HLS, Anda bisa mengonfigurasi Nimble Streamer untuk menyiarkannya kembali dalam format HLS.

   - Di bagian **Output settings**, pilih **HLS** sebagai format output.
   - Tentukan path untuk file segment `.ts` dan playlist `.m3u8` yang akan dihasilkan, misalnya:
     ```
     http://<server-ip>/hls/stream/playlist.m3u8
     ```
   - Tentukan **target duration** untuk segmen HLS, misalnya 6 detik.
   - Anda dapat menyesuaikan pengaturan seperti **bitrate**, **resolusi**, atau **jumlah segmen** sesuai dengan kebutuhan Anda.

3. **Pengaturan Konfigurasi HLS**:
   Pada bagian ini, Anda bisa mengatur lebih lanjut beberapa opsi terkait HLS, seperti:
   - **Segment size**: Ukuran segmen dalam detik.
   - **Playlist length**: Jumlah segmen dalam playlist.
   - **TTL (Time-to-Live)**: Durasi waktu segmen akan disimpan.

   Setelah Anda mengatur konfigurasi, klik **Save** untuk menyimpan pengaturan.

4. **Konfigurasi Live Transcoding (Opsional)**:
   Jika Anda ingin melakukan transcoding untuk mengubah resolusi atau bitrate dari stream HLS yang masuk, Nimble Streamer menyediakan fitur transcoding live. Anda dapat mengaktifkan **Live Transcoding** melalui menu **Live Transcoding** dan menambahkan pengaturan untuk mengonversi stream sesuai kebutuhan.

   Untuk mengonversi stream dari satu resolusi ke resolusi lain (misalnya, dari 1080p ke 480p), pilih profil transcoding yang sesuai dan tentukan resolusi serta bitrate yang diinginkan.

### Langkah 3: Memantau dan Mengelola Restreaming

Setelah konfigurasi selesai, Anda bisa memantau dan mengelola stream HLS Anda melalui antarmuka web Nimble Streamer.

1. **Memantau Stream**:
   Di menu **Live Streams**, Anda dapat melihat status stream yang aktif, jumlah pemirsa, serta statistik terkait.

2. **Mengakses Stream HLS**:
   Setelah stream berhasil diatur, Anda dapat mengakses stream HLS yang diproses ulang melalui URL HLS yang ditentukan, misalnya:
   ```
   http://<server-ip>/hls/stream/playlist.m3u8
   ```

### Langkah 4: Menggunakan API Nimble Streamer (Opsional)

Nimble Streamer juga menawarkan **REST API** untuk mengelola stream secara otomatis, jika Anda membutuhkan integrasi otomatis atau pengaturan dinamis untuk aliran HLS.

**Contoh API untuk menambahkan stream HLS**:
```bash
curl -X POST "http://<server-ip>:8080/api/v1/streams" \
    -d "url=http://source-url/stream.m3u8&app=hls&stream=streamname"
```

**API untuk mengelola stream HLS**:
Dengan API, Anda dapat memulai, menghentikan, atau mengonfigurasi stream secara otomatis sesuai kebutuhan.

### Tips dan Pertimbangan

- **Kinerja dan Scalability**: Pastikan server Nimble Streamer memiliki kapasitas yang cukup (CPU, RAM, I/O) untuk menangani jumlah stream yang tinggi, terutama jika Anda berencana untuk melakukan restreaming dari beberapa sumber atau menyediakan streaming untuk banyak pengguna.
- **CDN**: Untuk performa lebih baik dan distribusi yang lebih efisien, pertimbangkan menggunakan **CDN** untuk mengirimkan stream HLS ke pemirsa global.
- **Transcoding**: Jika Anda ingin menyediakan beberapa resolusi untuk stream HLS yang berbeda (misalnya, untuk adaptasi bandwidth), Anda bisa menambahkan profil transcoding di Nimble Streamer untuk membuat output multi-resolusi.

### Ringkasan
Dengan **Nimble Streamer**, Anda dapat dengan mudah melakukan restreaming HLS ke HLS dengan konfigurasi yang sangat fleksibel. Anda cukup menambahkan URL stream HLS sumber, mengatur output HLS, dan mengelola pengaturan segmentasi, durasi, serta transcoding (jika diperlukan). Nimble Streamer adalah solusi ideal untuk skala besar karena ringan dan efisien dalam menangani stream live.

## Node Media Server

Untuk melakukan **restreaming video HLS live ke HLS live** menggunakan **Node Media Server (NMS)**, Anda perlu mengonfigurasi server untuk menerima stream HLS dari sumber (input) dan kemudian menyiarkannya kembali dalam format HLS ke output. Node Media Server adalah server streaming media berbasis Node.js yang mendukung berbagai protokol, termasuk RTMP, HLS, dan lainnya.

Berikut adalah langkah-langkah untuk melakukan restreaming HLS live ke HLS live menggunakan Node Media Server:

### Langkah 1: Instalasi Node Media Server

1. **Persyaratan**:
   Pastikan Anda telah menginstal **Node.js** dan **npm** di server Anda. Anda bisa memverifikasi dengan menjalankan perintah:
   ```bash
   node -v
   npm -v
   ```
   Jika belum terinstal, Anda dapat mengunduh dan menginstal Node.js dari [nodejs.org](https://nodejs.org/).

2. **Instalasi Node Media Server**:
   Install Node Media Server menggunakan npm. Jalankan perintah berikut di terminal:
   ```bash
   npm install node-media-server
   ```

3. **Verifikasi Instalasi**:
   Setelah menginstal Node Media Server, Anda dapat memverifikasi instalasi dengan memulai server:
   ```bash
   node_modules/.bin/node-media-server
   ```
   Server akan mulai berjalan di port default yang telah ditentukan dalam konfigurasi.

### Langkah 2: Konfigurasi Node Media Server untuk Restreaming HLS ke HLS

1. **Buat File Konfigurasi**:
   Anda perlu membuat file konfigurasi untuk Node Media Server, di mana Anda akan mengonfigurasi input stream dan output stream. Buat file bernama `nms.js` dan tambahkan konfigurasi berikut:

   ```javascript
   const NodeMediaServer = require('node-media-server');

   const config = {
     rtmp: {
       port: 1935,           // Port untuk RTMP
       chunk_size: 4096,     // Ukuran chunk
       auto_publish: true    // Menyediakan fitur auto-publish
     },
     http: {
       port: 8000,           // Port untuk HTTP (untuk HLS)
       mediaroot: './media', // Direktori tempat media disimpan
       allow_origin: '*'     // Untuk mengizinkan permintaan dari semua origin
     },
     hls: {
       path: './hls',        // Direktori output HLS
       hls_time: 10,         // Durasi segmen HLS dalam detik
       hls_list_size: 6,     // Ukuran playlist
       hls_flags: '[hls_list_flags+delete_segments]'
     },
     trans: {
       ffmpeg: '/usr/bin/ffmpeg', // Path ke ffmpeg untuk transcoding
       tasks: [{
         app: 'live',
         stream: 'stream',   // Nama stream
         transcoding: {
           enabled: true,     // Aktifkan transcoding
           width: 1280,       // Resolusi output
           height: 720,       // Resolusi output
           bitrate: 1500,     // Bitrate output dalam kbps
           preset: 'ultrafast' // Pengaturan ffmpeg
         }
       }]
     }
   };

   var nms = new NodeMediaServer(config)
   nms.run();
   ```

   Penjelasan pengaturan di atas:
   - **RTMP**: Node Media Server mendengarkan di port 1935 untuk menerima stream RTMP.
   - **HTTP**: Server HTTP untuk menyediakan stream HLS melalui port 8000.
   - **HLS**: Pengaturan untuk output HLS yang ditulis ke direktori `./hls`.
   - **Transcoding**: Menambahkan transcoding dengan `ffmpeg` untuk mengonversi stream input ke resolusi dan bitrate yang diinginkan.

2. **Jalankan Server**:
   Setelah konfigurasi selesai, jalankan server Node Media Server:
   ```bash
   node nms.js
   ```

   Server akan berjalan dan siap menerima stream melalui RTMP dan menyediakan stream dalam format HLS.

### Langkah 3: Mengonfigurasi Restreaming HLS

Untuk melakukan restreaming HLS live ke HLS live, Anda harus melakukan dua hal utama:

1. **Menerima Stream HLS Sumber**:
   Pada Node Media Server, Anda bisa menyiapkan URL HLS yang akan diterima oleh server untuk diproses ulang. Misalnya, jika sumber stream HLS Anda adalah `http://source-url/stream.m3u8`, Anda bisa mengonfigurasi server untuk menerima stream tersebut.

2. **Menyediakan Stream HLS Kembali**:
   Setelah stream diterima, server akan menyiarkannya kembali dalam format HLS. Anda dapat mengakses stream yang telah diproses melalui URL HLS yang disediakan oleh server.

   Sebagai contoh, stream yang diproses oleh server dapat diakses melalui:
   ```
   http://<server-ip>:8000/hls/stream.m3u8
   ```

### Langkah 4: Menambahkan Transcoding (Opsional)

Jika Anda ingin melakukan transcoding saat menerima stream HLS, Anda bisa mengaktifkan opsi transcoding dalam file konfigurasi, seperti yang telah ditunjukkan di langkah konfigurasi sebelumnya. Misalnya, jika Anda ingin mengonversi stream HLS dari resolusi tinggi ke resolusi lebih rendah (misalnya 1080p ke 480p), Anda bisa menyesuaikan pengaturan transcoding dengan `ffmpeg`.

### Langkah 5: Memantau dan Mengelola Stream

1. **Memantau Stream**:
   Anda dapat memantau stream yang sedang aktif dengan melihat log output di terminal tempat Node Media Server berjalan. Setiap kali stream diterima, Anda akan melihat informasi terkait stream yang masuk dan keluar.

2. **Mengakses Stream HLS**:
   Setelah konfigurasi selesai dan stream diproses, Anda dapat mengakses stream HLS yang diproses dari server dengan URL HLS:
   ```
   http://<server-ip>:8000/hls/stream.m3u8
   ```

   Anda bisa menguji URL ini di pemutar HLS seperti video player berbasis web atau aplikasi media player yang mendukung HLS.

### Tips dan Pertimbangan

- **Kinerja dan Scalability**: Pastikan server yang digunakan memiliki sumber daya yang cukup (CPU, RAM, bandwidth) untuk menangani streaming langsung, terutama jika Anda merencanakan banyak stream atau audiens besar.
- **CDN untuk Distribusi**: Jika Anda memiliki audiens global, Anda dapat mengonfigurasi CDN untuk mendistribusikan stream HLS secara lebih efisien dan mengurangi beban pada server utama.
- **Keamanan**: Pertimbangkan untuk menggunakan protokol HTTPS untuk mengamankan transmisi data dan melakukan autentikasi jika diperlukan untuk membatasi akses ke stream.

### Ringkasan

Dengan **Node Media Server**, Anda dapat dengan mudah melakukan restreaming HLS live ke HLS live dengan konfigurasi yang sederhana. Cukup atur server untuk menerima stream HLS, sesuaikan output HLS, dan jika perlu, aktifkan transcoding untuk mengonversi stream ke resolusi atau bitrate yang berbeda. Node Media Server adalah solusi yang sangat fleksibel dan ringan untuk melakukan restreaming HLS.

<h2 style="text-align: center">SRS (Simple Realtime Server)</h2>

Untuk melakukan **restreaming video HLS live ke HLS live menggunakan SRS (Simple Real-time Server)**, Anda perlu mengonfigurasi server SRS untuk menerima stream dari sumber HLS dan menyediakannya kembali dalam format HLS. SRS adalah server streaming yang populer, ringan, dan open-source, mendukung berbagai protokol termasuk RTMP, HLS, dan lainnya.

Berikut adalah langkah-langkah untuk mengonfigurasi **SRS** agar dapat melakukan **restreaming HLS ke HLS**:

### Langkah 1: Instalasi SRS

1. **Persyaratan Sistem**:
   Sebelum menginstal SRS, pastikan server Anda memiliki persyaratan sistem berikut:
   - Linux (Ubuntu, CentOS, atau distribusi lainnya)
   - **GCC** untuk kompilasi
   - **CMake** dan **Make**

2. **Clone Repositori SRS**:
   Anda dapat mengunduh kode sumber SRS dari GitHub dan mengkompilasinya.
   ```bash
   git clone https://github.com/ossrs/srs.git
   cd srs
   ```

3. **Kompilasi SRS**:
   Setelah meng-clone repositori, jalankan perintah berikut untuk mengkompilasi SRS:
   ```bash
   ./configure
   make
   ```

4. **Jalankan SRS**:
   Setelah proses kompilasi selesai, Anda bisa memulai SRS dengan perintah:
   ```bash
   ./objs/srs
   ```

### Langkah 2: Konfigurasi SRS untuk Restreaming HLS

Setelah SRS terinstal dan berjalan, Anda perlu mengonfigurasi server untuk menerima stream HLS dan menyiarkannya kembali dalam format HLS. Untuk ini, Anda akan mengedit file konfigurasi SRS.

1. **Edit File Konfigurasi**:
   Buka file konfigurasi `conf/live.conf` yang terletak di direktori instalasi SRS. Anda akan menambahkan pengaturan untuk HLS dan RTMP.

   Contoh konfigurasi `live.conf`:
   ```ini
   listen              1935;
   max_connections     1000;

   vhost __defaultVhost__ {
       hls {
           enabled         on;
           hls_path        ./hls;
           hls_fragment    10s;
           hls_window      60s;
           hls_cleanup     on;
       }

       # Konfigurasi untuk menerima stream RTMP
       app live {
           live on;
           hls on;
           hls_path ./hls;
           hls_fragment 10;
           hls_window 60;
       }

       # Restream HLS source to HLS destination
       # This is the input source
       hls {
           enabled on;
           hls_path ./hls;
           hls_fragment 10s;
           hls_window 60s;
       }
   }
   ```

   Penjelasan:
   - **listen 1935**: Mengatur port RTMP untuk menerima stream dari klien RTMP.
   - **vhost __defaultVhost__**: Vhost default untuk streaming.
   - **hls**: Mengaktifkan HLS dan mengonfigurasi jalur untuk menyimpan segmen HLS.
   - **app live**: Mengaktifkan aplikasi live untuk menerima stream RTMP yang akan diproses menjadi HLS.
   - **hls_cleanup on**: Menghapus segmen HLS lama untuk menghemat ruang disk.

2. **Konfigurasi Input Stream HLS**:
   Jika Anda ingin menerima stream HLS sebagai input dan kemudian melakukan restreaming, pastikan sumber HLS tersebut sudah dapat diakses. Anda dapat mengonfigurasi SRS untuk menerima stream dari URL HLS eksternal dengan cara mengatur `http_flv` atau `http_hls` di bagian server.

   Misalnya, untuk menambahkan stream HLS eksternal:
   ```ini
   hls {
       enabled         on;
       hls_path        ./hls;
       hls_fragment    10s;
       hls_window      60s;
   }
   ```

3. **Menambahkan URL Stream Sumber**:
   Jika sumber HLS berasal dari URL lain (misalnya, dari server lain), Anda dapat mengonfigurasi server untuk melakukan **pull stream** dari URL HLS tersebut. Dalam SRS, Anda bisa menggunakan modul `pull` untuk menarik stream eksternal.

   Berikut adalah contoh konfigurasi untuk menarik stream dari sumber HLS eksternal:
   ```ini
   vhost __defaultVhost__ {
       # Mengambil stream HLS dari sumber lain
       pull http://source-hls-url/stream.m3u8 name=stream;
       hls {
           enabled on;
           hls_path ./hls;
           hls_fragment 10s;
           hls_window 60s;
       }
   }
   ```

### Langkah 3: Menyiapkan Output Stream HLS

Setelah SRS menerima stream HLS, Anda dapat mengonfigurasi server untuk menyiarkannya kembali dalam format HLS ke URL tertentu.

Misalnya, Anda dapat mengakses stream yang telah diproses di:
```
http://<server-ip>/hls/stream.m3u8
```

### Langkah 4: Mulai Server SRS

Setelah konfigurasi selesai, restart server SRS agar pengaturan diterapkan. Jalankan perintah berikut untuk memulai kembali SRS dengan pengaturan baru:
```bash
./objs/srs -c conf/live.conf
```

### Langkah 5: Mengakses Stream HLS

Setelah server SRS berjalan, stream yang diterima dari sumber HLS akan diproses dan disediakan kembali sebagai stream HLS yang dapat diakses di URL yang telah dikonfigurasi. Anda dapat mengakses stream HLS yang diproses menggunakan player HLS (seperti pemutar web yang mendukung HLS atau aplikasi lain) di:
```
http://<server-ip>/hls/stream.m3u8
```

### Tips dan Pertimbangan

1. **Kinerja**: Jika Anda melakukan restreaming dalam jumlah besar atau streaming dengan banyak resolusi, pastikan server memiliki kapasitas CPU dan bandwidth yang cukup untuk menangani beban tersebut.
2. **Scalability**: Pertimbangkan untuk menggunakan CDN (Content Delivery Network) jika Anda memiliki audiens yang tersebar secara geografis agar streaming lebih efisien dan mengurangi beban pada server utama.
3. **Keamanan**: Pastikan untuk mengonfigurasi firewall dan pengaturan akses agar hanya klien yang sah yang dapat mengakses stream.

### Ringkasan

Dengan **SRS (Simple Real-time Server)**, Anda dapat melakukan restreaming HLS live ke HLS live dengan cukup mudah menggunakan konfigurasi yang tepat. Anda dapat menarik stream dari sumber eksternal menggunakan modul `pull`, dan menyediakannya kembali dalam format HLS. SRS adalah solusi server yang ringan dan efisien untuk streaming live, yang dapat disesuaikan dengan berbagai kebutuhan transmisi media.
