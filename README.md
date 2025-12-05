# University Course Management System 🎓

A full-stack application designed to manage university course records. This project demonstrates a decoupled **client-server architecture** using a **Flask REST API** for the backend and a **Streamlit** dashboard for the frontend interface.

## 🚀 Features

* **Full CRUD Operations:** Create, Read, Update, and Delete course information.
* **RESTful API:** Robust backend handling JSON requests and responses.
* **Interactive Dashboard:** User-friendly Streamlit interface to test API endpoints without code.
* **Database Persistence:** MySQL database integration using SQLAlchemy ORM.
* **Data Visualization:** View course lists in formatted Pandas dataframes.

## 🛠️ Tech Stack

* **Backend:** Python, Flask, Flask-SQLAlchemy
* **Database:** MySQL (connected via PyMySQL)
* **Frontend:** Streamlit, Pandas
* **Utilities:** Requests

## 📂 Project Structure

```text
├── api.py               # Flask backend server containing API routes and DB model
├── client.py            # Streamlit frontend application for user interaction
├── requirements.txt     # Python dependencies
├── University_API.ipynb # Original development notebook (reference)
└── README.md            # Project documentation
```
⚙️ Setup & Installation
-----------------------
### 1\. Prerequisites
-   Python 3.8+
-   MySQL Server running locally

### 2\. Install Dependencies
Run the following command to install the required libraries:
Bash
```
pip install -r requirements.txt
```
Modern Linux distro like Debian 12/Ubuntu 24.04 now block you from running pip install globally to prevent breaking core system tools that rely on Python.
To fix this, you must create a Virtual Environment:

```bash
# 1. Create a virtual environment named 'venv'
python3 -m venv venv

# 2. Activate the environment
source venv/bin/activate
# (You will see '(venv)' appear at the start of your terminal line)

# 3. Now you can install your requirements safely
pip install -r requirements.txt
```

### 3\. Database Configuration
1.  Create a MySQL database named `university_db`:
    ```sql
    CREATE DATABASE university_db;
    ```

2.  Security Setup: This project uses a .env file to manage database passwords securely so they are not exposed in the code.
    - Create a file named .env in the root folder.
    - Add your MySQL password inside it:
    ```
    DB_PASSWORD=your_actual_sql_password
    ```
    - Note: If your local MySQL (e.g., XAMPP/WAMP) has no password, you can skip this step. The app defaults to an empty password if no .env file is found.

🏃‍♂️ How to Run
----------------
You need to run the backend and frontend in separate terminals.
**Step 1: Start the Backend (Terminal 1)**
```bash
python api.py
```
*The server will start on `http://127.0.0.1:5000`*.

**Step 2: Start the Frontend (Terminal 2)**
```bash
streamlit run client.py
```
*The Streamlit app will open automatically in your browser.*


🔌 API Endpoints
----------------
The Flask API provides the following endpoints:

| **Method** | **Endpoint** | **Description** |
| --- | --- | --- |
| `POST` | `/api/courses` | Create a new course |
| `GET` | `/api/courses` | Retrieve all courses |
| `GET` | `/api/course/<id>` | Retrieve a specific course by Subject Code |
| `PUT` | `/api/course/<id>` | Update an existing course |
| `DELETE` | `/api/course/<id>` | Delete a course |

📜 License
----------
This project is open source and available under the MIT License.
