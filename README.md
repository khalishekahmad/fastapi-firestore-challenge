# 🚀 FastAPI Firestore CRUD API

[![Linux_CI](https://img.shields.io/badge/Linux--CI-passing-brightgreen)](#) 
[![MacOS_CI](https://img.shields.io/badge/MacOS--CI-passing-brightgreen)](#) 
[![Build_Status](https://img.shields.io/badge/build-passing-brightgreen)](#) 
[![Windows_CI](https://img.shields.io/badge/Windows--CI-passing-brightgreen)](#)  


Proyek ini adalah **CRUD API** sederhana yang dibuat pakai **FastAPI** dan **Firebase Firestore** sebagai database. Semua data divalidasi pakai **Pydantic**, dan dokumentasi API bisa langsung diakses lewat **Swagger UI**.

---

## 📚 Apa Aja yang Ada di Sini?

- [Fitur Utama](#🚀-fitur-utama)
- [Setup Awal & Instalasi](#✅-setup-awal--instalasi)
- [Cara Menjalankan Server](#🚀-cara-menjalankan-server)
- [Struktur Endpoint](#🛠️-struktur-endpoint)
- [Cara Kerja API](#⚙️-cara-kerja-api)
- [Demo & Dokumentasi Tambahan](#🎥-demo--dokumentasi-tambahan)
- [Catatan Penting](#⚠️-catatan-penting)

---

## 🚀 Fitur Utama

- **CRUD (Create, Read, Update, Delete)** buat data pengguna di Firebase Firestore.
- **Validasi data** pakai Pydantic supaya inputnya rapi.
- **Dokumentasi otomatis** tersedia di **Swagger UI** di `/docs`.
- **Struktur kode simpel** dan gampang buat dikembangkan.

---

## ✅ Setup Awal & Instalasi

### 1. Bikin Folder Proyek

Buka terminal dan buat folder proyek, misalnya:

```bash
mkdir fastapi-firestore-challenge
cd fastapi-firestore-challenge
```

### 2. Buat Virtual Environment

Masih di dalam folder proyek, jalankan:

```bash
python -m venv env
```

Terus aktifkan virtual environment:

- **Windows:**
  ```bash
  env\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source env/bin/activate
  ```

---

## 📦 Instalasi Dependensi

Setelah virtual environment aktif, install semua yang dibutuhkan:

```bash
pip install fastapi uvicorn firebase-admin
```

> **Catatan:** Pydantic udah include di FastAPI, jadi nggak perlu install lagi.

---

## 🔥 Setup Firebase Firestore

### 1. Buat Proyek di Firebase

- Buka [Firebase Console](https://console.firebase.google.com/) dan buat proyek baru.

### 2. Aktifkan Cloud Firestore

- Masuk ke **Firestore Database** dan pilih mode **Test Mode** buat pengembangan.

### 3. Unduh Service Account Key

- Pergi ke **Project Settings > Service accounts**, lalu unduh file JSON.

### 4. Simpan File JSON

- Simpan file JSON tadi di folder proyek dengan nama `serviceAccountKey.json`.

---

## 🚀 Cara Menjalankan Server

### 1. Buka Terminal

Pastikan ada di dalam folder proyek dan virtual environment sudah aktif.

### 2. Jalankan Server

```bash
uvicorn main:app --reload
```

- `main:app` maksudnya **main.py** sebagai file utama.
- Opsi `--reload` bikin server otomatis restart kalau ada perubahan kode.

### 3. Cek API di Browser

- **Swagger UI (Dokumentasi API):**
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc UI:**
  [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- Kalau buka http://127.0.0.1:8000/, akan muncul "Not Found".
Itu terjadi karena di kode ini kita tidak mendefinisikan route untuk halaman utama ("/").
Endpoint yang tersedia hanya yang ada di daftar API di Swagger UI atau Redoc UI.
---

## 🛠️ Struktur Endpoint

| Method | Endpoint           | Kegunaan                      |
| ------ | ------------------ | ----------------------------- |
| POST   | `/users`           | Tambah pengguna baru          |
| GET    | `/users`           | Ambil semua data pengguna     |
| GET    | `/users/{user_id}` | Ambil data pengguna by ID     |
| PUT    | `/users/{user_id}` | Update data pengguna tertentu |
| DELETE | `/users/{user_id}` | Hapus data pengguna           |

### 📌 Contoh Request JSON:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 30
}
```

---

## ⚙️ Cara Kerja API

- **FastAPI**: Buat ngatur request dan response.
- **Firebase Firestore**: Jadi database buat nyimpen data user.

### 🔥 Inisialisasi Firebase:

Di dalam `main.py`, Firebase di-setup kayak gini:

```python
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
```

- **Pydantic** dipakai buat validasi input.
- **Swagger UI** otomatis tersedia di `/docs`.

---

## 🎥 Demo & Dokumentasi Tambahan

### 📹 Video Demo (Opsional)

Kalau punya video demo di YouTube, bisa ditambahkan:

```markdown
[Demo Video di YouTube](https://www.youtube.com/watch?v=contohLink)
```

### 📸 GIF atau Screenshot (Opsional)

Bisa juga tambahin gambar atau demo GIF:

```markdown
![Demo GIF](demo.gif)
```

> Pastikan file `demo.gif` ada di dalam repository.

---

## ⚠️ Catatan Penting

- **Jangan upload `serviceAccountKey.json` ke repo publik!**
  Tambahkan ke `.gitignore` biar tetap aman.
- **Keamanan:** Kalau buat produksi, pastikan ada autentikasi dan aturan akses di Firestore.
- **Testing:** Cek semua endpoint pakai **Swagger UI**, **Postman**, atau **cURL** biar nggak ada error.

---

Selamat mencoba! Semoga bermanfaat & happy coding! 🚀😊



