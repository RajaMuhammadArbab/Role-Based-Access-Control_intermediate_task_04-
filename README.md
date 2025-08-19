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


