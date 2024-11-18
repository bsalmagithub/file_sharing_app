
# File Sharing App

This is a simple file-sharing system that supports two types of users: **Ops User** and **Client User**. The application is built using FastAPI and provides a set of REST APIs for file uploading and downloading.

## Setup Instructions

Follow the steps below to set up and run the project locally:

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/file_sharing_app.git
```

### 2. Create and Activate a Virtual Environment

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows**: 
```bash
.env\Scripts\activate
```

- **Mac/Linux**:
```bash
source venv/bin/activate
```

### 3. Install Dependencies

Install the necessary dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Create a Database

Make sure you have a database set up (e.g., SQLite, PostgreSQL, MySQL). Update the `db.py` file to connect to your database.

### 5. Running the Application

Run the application using `uvicorn`:

```bash
uvicorn main:app --reload
```

The application will start at `http://127.0.0.1:8000`.

### 6. API Endpoints

#### **Ops User Endpoints:**

1. **Login (POST)**:
   - **URL**: `/login`
   - **Request Body**: 
   ```json
   {
     "email": "user@example.com",
     "password": "password123"
   }
   ```

2. **Upload File (POST)**:
   - **URL**: `/upload-file`
   - **Request Body**: Form-data with `file` field for the file content and `session_token` as query parameter.
   - Only supports `pptx`, `docx`, and `xlsx` file types.

#### **Client User Endpoints:**

1. **Sign Up (POST)**:
   - **URL**: `/sign-up`
   - **Request Body**: 
   ```json
   {
     "email": "client@example.com",
     "password": "password123"
   }
   ```

2. **Login (POST)**:
   - **URL**: `/login`
   - **Request Body**: 
   ```json
   {
     "email": "client@example.com",
     "password": "password123"
   }
   ```

3. **Email Verify (GET)**:
   - **URL**: `/verify-email/{email_token}`
   - Used to verify the email after sign-up.

4. **List All Files (GET)**:
   - **URL**: `/list-files`
   - Returns a list of all uploaded files.

5. **Download File (GET)**:
   - **URL**: `/download-file/{file_id}`
   - Generates a secure download link for the requested file.

### 7. Notes

- **File Upload Restrictions**: Ops User can only upload files of type `pptx`, `docx`, or `xlsx`.
- **Secure Download Links**: When a Client User requests a file download, an encrypted URL is returned. This URL can only be accessed by the Client User.
- **Database Models**: The database models for file uploads and users are defined in `models.py`. 

### 8. Troubleshooting

- If you encounter errors related to missing dependencies, ensure all required libraries are installed using the `requirements.txt` file.
- For database connection issues, verify the database credentials in `db.py`.

