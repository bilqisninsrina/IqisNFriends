# IqisNFriends

Website sederhana dengan Django + OAuth Google.

## Fitur
- Landing page dengan navbar yang lebih rapi, tipografi yang lebih kuat, dan tombol login Google.
- 4 kartu biodata dengan layout yang konsisten tanpa overlay guest.
- Login menggunakan Google OAuth (`django-allauth`).
- Setelah login:
  - Navbar menampilkan nama user Google.
  - Tombol logout tersedia.
  - User bisa customize warna latar halaman.

## Setup
1. Install dependency:
   ```bash
   pip install -r requirements.txt
   ```
2. Buat file `.env` dari template:
   ```bash
   copy .env.example .env
   ```
3. Isi kredensial Google OAuth di `.env`:
   ```env
   GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
   GOOGLE_CLIENT_SECRET=your-client-secret
   ```
4. Jalankan migrasi:
   ```bash
   python manage.py migrate
   ```
5. Jalankan server:
   ```bash
   python manage.py runserver
   ```

## Catatan OAuth Google
Di Google Cloud Console, tambahkan redirect URI berikut:
- `http://127.0.0.1:8000/accounts/google/login/callback/`

Lalu pastikan authorized origin untuk local development juga ditambahkan, misalnya:
- `http://127.0.0.1:8000`
- `http://localhost:8000`

Kalau `.env` belum diisi, tombol login akan dinonaktifkan supaya tidak lagi mengarah ke error Google `Missing required parameter: client_id`.
