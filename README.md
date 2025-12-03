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
├── api.py           # Flask backend server containing API routes and DB model
├── client.py        # Streamlit frontend application for user interaction
├── University_API.ipynb # Original development notebook (reference)
└── README.md        # Project documentation
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
pip install flask flask-sqlalchemy mysql-connector-python pymysql requests streamlit pandas
```

### 3\. Database Configuration
1.  Create a MySQL database named `university_db`:
    ```sql
    CREATE DATABASE university_db;
    ```

2.  The application is configured to connect to `localhost` with the user `root` and no password.
    -   *Note:* If your MySQL setup has a password, update the `SQLALCHEMY_DATABASE_URI` in `api.py`:
    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:YOUR_PASSWORD@localhost/university_db'
    ```

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
