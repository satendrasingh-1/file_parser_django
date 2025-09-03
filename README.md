📂 Django File Upload & Processing API
This is a Django REST Framework project that allows users to upload files (CSV, XLSX, TXT, PDF), automatically parse their contents, and track upload progress dynamically.
Uploaded files are stored in the database with their metadata, progress status, and parsed content.

🚀 Features
Upload files (CSV, XLSX, TXT, PDF supported).
Process files asynchronously with background threads.
Store uploaded files in SQL database.
Track upload progress dynamically (uploading → processing → ready).
Retrieve parsed file contents.
Delete files.
Django Admin integration to view/manage uploaded files.

🛠️ Tech Stack
Backend: Django, Django REST Framework
Database: SQLite (default) – can be replaced with PostgreSQL/MySQL
File Parsing: csv, openpyxl, PyPDF2
API Testing: Postman / cURL

📦 Installation
1️⃣ Clone the repo
git clone https://github.com/your-username/file_parser_django.git
cd file_service

2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Apply migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create superuser (to access Django Admin)
python manage.py createsuperuser

6️⃣ Run server
python manage.py runserver

📡 API Endpoints
🔹 Upload File
POST /files/upload/
Form-data:
file: <your_file>
Response
{
  "id": "uuid",
  "filename": "data.csv",
  "status": "uploading",
  "progress": 0
}

🔹 Get File List
GET /files/

🔹 Check File Progress
GET /files/<uuid:file_id>/progress/
Response
{
  "file_id": "uuid",
  "status": "ready",
  "progress": 100
}

🔹 Get File Content
GET /files/<uuid:file_id>/content/

🔹 Delete File
DELETE /files/<uuid:file_id>/delete/

⚙️ Admin Panel
Go to:
👉 http://127.0.0.1:8000/admin/
Login with your superuser credentials.
You’ll see UploadedFile model to manage all files.

✅ Now your API is ready for file uploads and processing!

Contributions are welcome! 🚀
📧 Contact
If you have ideas, issues, or suggestions, feel free to open an Issue or contact me at:
your-satendraprataps56@gmail.com
