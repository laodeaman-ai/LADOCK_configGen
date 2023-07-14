# LADOCK_configGen
Script untuk generate file config banyak ligan alami dari PDB ID untuk simulasi autodock-vina.

Cara menggunakan paket ini:

1. Persiapan:
   - Pastikan Anda memiliki Python terinstal di sistem Anda. Jika belum, instal Python terlebih dahulu.
   - Pastikan Anda telah menginstal Biopython, modul yang digunakan dalam script ini. Jika belum, Anda dapat menginstalnya menggunakan pip dengan menjalankan perintah `pip install biopython`.
   - Pastikan file-file PDB dari ligan alami yang ingin Anda proses berada dalam direktori kerja yang sama dengan script Python ini.

2. Modifikasi script:
   - Anda dapat membuka script Python di editor teks atau lingkungan pengembangan Python.
   - Anda dapat memodifikasi nilai variabel `size_x`, `size_y`, dan `size_z` sesuai dengan ukuran grid box yang Anda inginkan.
   - Jika Anda ingin mengubah pesan informasi penulis, Anda dapat memodifikasi bagian yang ditambahkan di akhir script dengan informasi yang sesuai dengan Anda.

3. Menjalankan script:
   - Simpan script Python setelah melakukan modifikasi.
   - Buka terminal atau command prompt, lalu arahkan ke direktori tempat Anda menyimpan script tersebut.
   - Jalankan script dengan perintah `python nama_script.py`, di mana `nama_script.py` adalah nama file dari script Python yang telah Anda simpan.

4. Proses eksekusi:
   - Script akan membaca setiap file PDB dalam direktori kerja.
   - Untuk setiap file PDB, script akan menghitung koordinat titik pusat grid box berdasarkan struktur molekul menggunakan Biopython.
   - Script akan membuat direktori output dengan nama yang sesuai dengan nama file PDB.
   - Script akan menulis koordinat titik pusat, ukuran grid box, dan parameter tambahan dalam file "config.txt" di direktori output yang sesuai.
   - Informasi penulis juga akan ditampilkan di output konsol.

5. Hasil:
   - Setelah proses eksekusi selesai, Anda akan memiliki direktori output untuk setiap file PDB yang berisi file "config.txt" dengan koordinat titik pusat, ukuran grid box, dan parameter tambahan yang telah ditentukan.
   - Selain itu, informasi penulis juga akan ditampilkan di output konsol.

Pastikan Anda telah memahami dan mengikuti langkah-langkah di atas dengan benar untuk menggunakan script tersebut secara efektif. Jika Anda menghadapi masalah atau memiliki pertanyaan tambahan, jangan ragu untuk menghubungi penulis:
   La Ode Aman
   laodeaman.ai@gmail.com
   laode_aman@ung.ac.id
   Universitas Negeri Gorontalo, Indonesia
