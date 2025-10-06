import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# -------------------------------
# USERS TABLE OPERATIONS
# -------------------------------
def add_user(name, email, password):
    return supabase.table("users").insert({
        "name": name,
        "email": email,
        "password": password
    }).execute()

def get_user(email):
    return supabase.table("users").select("*").eq("email", email).execute()

# -------------------------------
# EMAILS TABLE OPERATIONS
# -------------------------------
def add_email(user_email, subject, body, recipient, scheduled_time, track_code):
    return supabase.table("emails").insert({
        "user_email": user_email,
        "subject": subject,
        "body": body,
        "recipient": recipient,
        "scheduled_time": scheduled_time,
        "track_code": track_code
    }).execute()

def mark_email_sent(user_email, subject, recipient, scheduled_time):
    return supabase.table("emails").update({
        "sent_status": "sent",
        "sent_at": "now()"
    }).match({
        "user_email": user_email,
        "subject": subject,
        "recipient": recipient,
        "scheduled_time": scheduled_time
    }).execute()

def mark_email_opened(track_code):
    return supabase.table("emails").update({
        "open_status": "opened",
        "opened_at": "now()"
    }).eq("track_code", track_code).execute()

# -------------------------------
# EMAIL LOGS TABLE OPERATIONS
# -------------------------------
def add_email_log(user_email, recipient, subject, event_type, message=None):
    return supabase.table("email_logs").insert({
        "user_email": user_email,
        "recipient": recipient,
        "subject": subject,
        "event_type": event_type,
        "message": message
    }).execute()
