import firebase_admin
from firebase_admin import credentials, firestore
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

# Inisialisasi Firebase Admin pake file service account
cred = credentials.Certificate("serviceAccountKey.json")  # Pastikan path sesuai
firebase_admin.initialize_app(cred)
db = firestore.client()

# Inisialisasi FastAPI
app = FastAPI(
    title="FastAPI Firestore CRUD API",
    description="API sederhana buat CRUD data user dengan Firebase Firestore",
    version="1.0.0"
)

# Model data user pake Pydantic buat validasi input
class User(BaseModel):
    id: Optional[str] = Field(None, example="user123")  # Auto generate dari Firestore
    name: str = Field(..., example="John Doe")
    email: str = Field(..., example="john@example.com")
    age: Optional[int] = Field(None, example=30)

# Endpoint buat create user
@app.post("/users", response_model=User)
async def create_user(user: User):
    try:
        # Buat document baru di collection 'users' dengan auto id
        doc_ref = db.collection("users").document()
        user_data = user.dict(exclude_unset=True)
        doc_ref.set(user_data)
        # Update field id supaya data lengkap
        db.collection("users").document(doc_ref.id).update({"id": doc_ref.id})
        user_data["id"] = doc_ref.id
        return user_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint buat ambil semua user
@app.get("/users", response_model=list[User])
async def get_users():
    try:
        users_ref = db.collection("users")
        docs = users_ref.stream()
        users = [doc.to_dict() for doc in docs]
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint buat ambil 1 user berdasarkan id
@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: str):
    try:
        doc = db.collection("users").document(user_id).get()
        if doc.exists:
            return doc.to_dict()
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint buat update data user
@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: str, user: User):
    try:
        doc_ref = db.collection("users").document(user_id)
        if not doc_ref.get().exists:
            raise HTTPException(status_code=404, detail="User not found")
        user_data = user.dict(exclude_unset=True)
        doc_ref.update(user_data)
        return doc_ref.get().to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint buat hapus user
@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    try:
        doc_ref = db.collection("users").document(user_id)
        if not doc_ref.get().exists:
            raise HTTPException(status_code=404, detail="User not found")
        doc_ref.delete()
        return {"message": "User deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
