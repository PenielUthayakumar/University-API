# Streamlit Client
import streamlit as st
import requests
import json
import pandas as pd

st.set_page_config(page_title="University Courses API", layout="wide")

st.title("University Courses — Streamlit API Client")

st.sidebar.header("API Settings")
base_url = st.sidebar.text_input("API Base URL", value="http://localhost:5000/api")

st.sidebar.markdown("Ensure the Flask API is running before using this client.")

tabs = st.tabs(["Create", "List", "Get", "Update", "Delete"])

def safe_request(method, url, **kwargs):
    try:
        resp = requests.request(method, url, timeout=8, **kwargs)
        try:
            data = resp.json()
        except Exception:
            data = resp.text
        return resp.status_code, data
    except requests.exceptions.RequestException as e:
        return None, str(e)

with tabs[0]:
    st.subheader("Create Course")
    with st.form("create_form"):
        subject_code = st.number_input("Subject Code", min_value=1, step=1)
        subject_name = st.text_input("Subject Name")
        lecturer = st.text_input("Lecturer")
        venue = st.text_input("Venue")
        capacity = st.number_input("Capacity", min_value=0, step=1)
        submitted = st.form_submit_button("Create")
    if submitted:
        payload = {
            "subject_code": int(subject_code),
            "subject_name": subject_name,
            "lecturer": lecturer,
            "venue": venue,
            "capacity": int(capacity)
        }
        status, data = safe_request("POST", f"{base_url}/courses", json=payload)
        if status and 200 <= status < 300:
            st.success("Course created successfully")
            st.json(data)
        else:
            st.error(f"Error: {status} — {data}")

with tabs[1]:
    st.subheader("List All Courses")
    if st.button("Get all courses"):
        status, data = safe_request("GET", f"{base_url}/courses")
        if status and 200 <= status < 300:
            # try to normalize to table
            courses = data.get("courses") if isinstance(data, dict) else None
            if courses and isinstance(courses, list):
                df = pd.json_normalize(courses)
                st.dataframe(df)
            else:
                st.json(data)
        else:
            st.error(f"Error: {status} — {data}")

with tabs[2]:
    st.subheader("Get Course by Subject Code")
    code = st.number_input("Subject Code", min_value=1, step=1, key="get_code")
    if st.button("Get course"):
        status, data = safe_request("GET", f"{base_url}/course/{int(code)}")
        if status and 200 <= status < 300:
            st.json(data)
        elif status == 404:
            st.warning("Course not found")
        else:
            st.error(f"Error: {status} — {data}")

with tabs[3]:
    st.subheader("Update Course")
    with st.form("update_form"):
        upd_code = st.number_input("Subject Code to update", min_value=1, step=1)
        upd_name = st.text_input("Subject Name (leave blank to keep)")
        upd_lecturer = st.text_input("Lecturer (leave blank to keep)")
        upd_venue = st.text_input("Venue (leave blank to keep)")
        upd_capacity = st.number_input("Capacity (0 to keep)", min_value=0, step=1)
        update_submitted = st.form_submit_button("Update")
    if update_submitted:
        payload = {}
        if upd_name:
            payload["subject_name"] = upd_name
        if upd_lecturer:
            payload["lecturer"] = upd_lecturer
        if upd_venue:
            payload["venue"] = upd_venue
        if upd_capacity != 0:
            payload["capacity"] = int(upd_capacity)
        if not payload:
            st.info("No fields provided to update.")
        else:
            status, data = safe_request("PUT", f"{base_url}/course/{int(upd_code)}", json=payload)
            if status and 200 <= status < 300:
                st.success("Course updated")
                st.json(data)
            else:
                st.error(f"Error: {status} — {data}")

with tabs[4]:
    st.subheader("Delete Course")
    del_code = st.number_input("Subject Code to delete", min_value=1, step=1, key="del_code")
    if st.button("Delete"):
        url = f"{base_url}/course/{int(del_code)}"
        status, data = safe_request("DELETE", url)
        if status and 200 <= status < 300:
            st.success(f"Deleted course (endpoint: {url})")
            st.json(data)
        elif status == 404:
            st.warning("Course not found")
        else:
            st.error(f"Delete failed: {status} — {data}")

st.markdown("---")
st.caption("Note: This client assumes the Flask API is reachable at the provided Base URL and that CORS/networking allow local requests.")
