# FastAPI Firestore Challenge

Project ini adalah REST API berbasis FastAPI yang terintegrasi dengan Firebase Firestore.  
**Fitur:** CRUD API, validasi data pake Pydantic, dan dokumentasi otomatis via Swagger UI.

## Cara Install

1. Clone repo: `git clone <repo-url>`
2. Masuk ke folder: `cd fastapi-firestore-challenge`
3. Buat virtual environment: `python -m venv env`
4. Aktifkan virtual environment: `env\Scripts\activate` (Windows)  
   atau `source env/bin/activate` (Linux/Mac)
5. Install dependencies: `pip install fastapi uvicorn firebase-admin`

## Cara Menjalankan Server

Jalankan: `uvicorn main:app --reload`  
Lalu akses [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) buat testing API.

## Keterangan

Jangan lupa masukkan file `serviceAccountKey.json` secara manual, dan pastikan file itu ada di `.gitignore`.

