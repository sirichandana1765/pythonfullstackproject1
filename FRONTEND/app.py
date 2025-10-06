import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="📧 Email Automation System")
st.title("📧 Gmail Email Automation")

# ----------------------
# User Login
# ----------------------
st.sidebar.header("User Login")
user_email = st.sidebar.text_input("Your Email")
user_password = st.sidebar.text_input("Password", type="password")

# ----------------------
# Session state for date/time
# ----------------------
if "scheduled_date" not in st.session_state:
    st.session_state.scheduled_date = datetime.now().date()
if "scheduled_time_str" not in st.session_state:
    st.session_state.scheduled_time_str = datetime.now().strftime("%I:%M %p")  # 12-hour format

if user_email and user_password:
    st.success(f"Logged in as {user_email}")

    st.header("Send / Schedule Email")
    recipient = st.text_input("Recipient Email")
    subject = st.text_input("Subject")
    body = st.text_area("Email Body (HTML supported)")

    st.subheader("Schedule Email (Optional)")
    st.session_state.scheduled_date = st.date_input(
        "Select Date", value=st.session_state.scheduled_date
    )

    st.session_state.scheduled_time_str = st.text_input(
        "Enter Time (hh:mm AM/PM)", value=st.session_state.scheduled_time_str
    )

    # Validate & parse manual time input
    try:
        scheduled_time = datetime.strptime(st.session_state.scheduled_time_str, "%I:%M %p").time()
        scheduled_datetime = datetime.combine(st.session_state.scheduled_date, scheduled_time)
        valid_time = True
    except ValueError:
        st.error("Invalid time format! Use hh:mm AM/PM, e.g., 02:30 PM")
        valid_time = False

    if st.button("Send / Schedule Email") and valid_time:
        if not recipient or not subject or not body:
            st.error("Please fill in all fields!")
        else:
            data = {
                "user_email": user_email,
                "recipient": recipient,
                "subject": subject,
                "body": body,
                "scheduled_time": scheduled_datetime.isoformat()
            }
            try:
                res = requests.post("http://127.0.0.1:8000/send", json=data, timeout=10)
                if res.status_code == 200:
                    st.success(res.json().get("message", "Email scheduled successfully!"))
                else:
                    st.error("Failed to send/schedule email. Check backend.")
            except requests.exceptions.ConnectionError:
                st.error("Cannot connect to backend. Is FastAPI running?")
else:
    st.warning("Please log in first.")
