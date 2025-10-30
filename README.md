# 🧩 Django Blog Mini Project

A simple blog web application built with **Django**  where users can 
- create an account, 
- log in, 
- write posts with images, 
- edit or delete them, and 
- comment under each post.

---

## 🚀 Features

✅ User Authentication  
- Register new users  
- Login & Logout functionality  

✅ Blog System  
- Create new blog posts  
- Edit and delete existing posts  
- Upload images for each post  

✅ Comment System  
- Add comments under each post  
- Display comments with author name & created date  

✅ Media Handling  
- Image upload and display using `MEDIA_URL` and `MEDIA_ROOT`  

---

## 🛠️ Tech Stack

| Component | Description |
|------------|-------------|
| **Backend** | Django 5.x |
| **Frontend** | HTML, CSS (Django Templates) |
| **Database** | SQLite (default) |
| **Auth System** | Django's built-in authentication |
| **Image Handling** | Django `ImageField` |

---

## 📂 Project Structure
blog_project/
|
├── blog/
│ ├── migrations/
│ ├── templates/blog/
│ │ ├── base.html        * You can create your own template style with 'Base.html'. *
│ │ ├── blog_post.html
│ │ ├── post_form.html
│ │ └── post_detail.html + (authentication --> register, login, logout)
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── forms.py
│ └── admin.py
│
├── blog_project/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── media/
|
├── manage.py
└── requirements.txt

---

## ⚙️ Installation & Setup

1. ** Clone the Repository **
   ```bash
   git clone https://github.com/your-username/django-blog.git
   cd django-blog


2. Create & activate virtual environment
    python -m venv venv
    source venv/bin/activate       # macOS / Linux
    venv\Scripts\activate          # Windows

3. Install dependencies
    pip install django pillow

4. Run Migrations
    python manage.py makemigrations
    python manage.py migrate

5. Create Super User
    python manage.py createsuperuser

6. Run the Server
    python manage.py runserver

7. Open in Browser
    http://127.0.0.1:8000/
