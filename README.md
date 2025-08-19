# Blog API with Role-Based Access Control (RBAC)

A Django REST Framework API for managing blog posts with **role-based access control** and **soft delete** functionality.

Roles supported:
- **Admin** → Full access (manage all posts + users).
- **Editor** → Can create, update, delete **only own posts**.
- **Viewer** → Read-only access to posts.

---

##  Tech Stack
- Python 3.10+
- Django 5+
- Django REST Framework (DRF)
- JWT Authentication (`djangorestframework-simplejwt`)
- PostgreSQL / SQLite (default)

---

##  Setup & Run Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/blog-rbac-api.git
cd blog-rbac-api
```

### 2. Create & activate virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create superuser (for Admin role)
```bash
python manage.py createsuperuser
```

### 6. Run the server
```bash
python manage.py runserver
```

Server runs at: `http://127.0.0.1:8000/`

---

##  Authentication
We use **JWT authentication**.  
Obtain tokens at:
- `POST /api/auth/token/` → get access & refresh tokens
- `POST /api/auth/token/refresh/` → refresh access token

Authorization header format:
```
Authorization: Bearer <your_access_token>
```

---

##  API Endpoints

### Auth
- `POST /api/auth/register/` → Register new user
- `POST /api/auth/token/` → Get JWT tokens
- `POST /api/auth/token/refresh/` → Refresh JWT

### Users (Admin only)
- `GET /api/users/` → List all users
- `DELETE /api/users/{id}/` → Soft delete user

### Posts
- `GET /api/posts/` → List all posts (public)
- `POST /api/posts/` → Create new post (Admin, Editor)
- `GET /api/posts/{id}/` → Retrieve post
- `PUT /api/posts/{id}/` → Update post (Admin or owner if Editor)
- `DELETE /api/posts/{id}/` → Soft delete post (Admin or owner if Editor)

---

##  Sample Requests & Responses

### 1. Register User
**Request**
```http
POST /api/auth/register/
Content-Type: application/json

{
  "username": "editor1",
  "password": "pass1234",
  "role": "Editor"
}
```

**Response**
```json
{
  "id": 2,
  "username": "editor1",
  "role": "Editor"
}
```

---

### 2. Login (Get Tokens)
**Request**
```http
POST /api/auth/token/
Content-Type: application/json

{
  "username": "editor1",
  "password": "pass1234"
}
```

**Response**
```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI...",
  "access": "eyJ0eXAiOiJKV1QiLCJh..."
}
```

---

### 3. Create Post (Editor/Admin)
**Request**
```http
POST /api/posts/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "title": "My First Post",
  "content": "This is a blog post content."
}
```

**Response**
```json
{
  "id": 1,
  "title": "My First Post",
  "content": "This is a blog post content.",
  "author": "editor1",
  "is_deleted": false,
  "created_at": "2025-08-19T10:30:00Z"
}
```

---

### 4. Viewer Access (Read Only)
**Request**
```http
GET /api/posts/
```

**Response**
```json
[
  {
    "id": 1,
    "title": "My First Post",
    "content": "This is a blog post content.",
    "author": "editor1",
    "is_deleted": false
  }
]
```

---

## Postman Collection

A ready-to-use Postman Collection + Environment is included:

- `Blog_RBAC_API.postman_collection.json`
- `Blog_RBAC_API.postman_environment.json`

### 🔹 How to Use
1. Open Postman → Import → choose both JSON files.
2. Select the environment (`Blog_RBAC_API`).
3. Update the `base_url` variable if needed (default: `http://127.0.0.1:8000/api`).
4. Run requests in order:
   - **Register → Login → Copy access token → Test posts/users with role-based access.**

---

## ✅ Role-Based Access Demo
- **Admin** → Can list/delete users, manage any post.
- **Editor** → Can only manage (create, update, delete) own posts.
- **Viewer** → Can only read posts.

---

## PROJECT-DEMO ##

<img width="1367" height="682" alt="1" src="https://github.com/user-attachments/assets/36d3eb5e-9774-4b22-9464-804d695f7ed1" />
<img width="1387" height="663" alt="2" src="https://github.com/user-attachments/assets/6ad17c25-0a91-4ead-9003-a0c5b1430535" />
<img width="1385" height="684" alt="3" src="https://github.com/user-attachments/assets/c139dee1-ab4a-421f-aeab-122ee2724c2d" />
<img width="1379" height="670" alt="4" src="https://github.com/user-attachments/assets/342b1741-9208-4593-b0f9-18e49a65651d" />
<img width="1370" height="676" alt="5" src="https://github.com/user-attachments/assets/0fa3a81e-f55b-4eb0-8451-efca1f281582" />
<img width="1370" height="663" alt="6" src="https://github.com/user-attachments/assets/f01fb314-8952-48ec-a753-73a6e86c1e7d" />
<img width="1376" height="457" alt="7" src="https://github.com/user-attachments/assets/b1752796-e6b6-4683-abbd-0732153010a7" />
<img width="1393" height="880" alt="8" src="https://github.com/user-attachments/assets/b695c4ee-908b-4f13-b3f7-a5198cc5169d" />
<img width="1380" height="498" alt="9" src="https://github.com/user-attachments/assets/53f13078-e597-4b92-b37a-ce0520dfa174" />
<img width="1353" height="745" alt="10" src="https://github.com/user-attachments/assets/d2591b72-ccd2-49e7-8526-aa068ec7a69d" />
<img width="1379" height="731" alt="11" src="https://github.com/user-attachments/assets/c9d52d9e-38d4-4e7d-b536-b8f26cbdb248" />
<img width="1384" height="577" alt="12" src="https://github.com/user-attachments/assets/57e77178-1fd7-450f-b64a-a74132ee6bbe" />

