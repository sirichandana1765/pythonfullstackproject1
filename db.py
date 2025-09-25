# db_manager.py
import os
from supabase import create_client
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

# -----------------------------
# app_users Table Operations
# -----------------------------
def create_user(name, email, password_hash):
    return supabase.table("app_users").insert({
        "name": name,
        "email": email,
        "password_hash": password_hash,
        "created_at": datetime.now()
    }).execute()

def get_all_users():
    return supabase.table("app_users").select("*").execute()

def update_user(user_id, name=None, email=None, password_hash=None):
    data = {}
    if name:
        data["name"] = name
    if email:
        data["email"] = email
    if password_hash:
        data["password_hash"] = password_hash
    return supabase.table("app_users").update(data).eq("id", user_id).execute()

def delete_user(user_id):
    return supabase.table("app_users").delete().eq("id", user_id).execute()


# -----------------------------
# user_contacts Table Operations
# -----------------------------
def create_contact(user_id, name, email):
    return supabase.table("user_contacts").insert({
        "user_id": user_id,
        "name": name,
        "email": email,
        "created_at": datetime.now()
    }).execute()

def get_contacts(user_id):
    return supabase.table("user_contacts").select("*").eq("user_id", user_id).execute()

def update_contact(contact_id, name=None, email=None):
    data = {}
    if name:
        data["name"] = name
    if email:
        data["email"] = email
    return supabase.table("user_contacts").update(data).eq("id", contact_id).execute()

def delete_contact(contact_id):
    return supabase.table("user_contacts").delete().eq("id", contact_id).execute()


# -----------------------------
# scheduled_emails Table Operations
# -----------------------------
def create_email(user_id, subject, body, scheduled_time):
    return supabase.table("scheduled_emails").insert({
        "user_id": user_id,
        "subject": subject,
        "body": body,
        "scheduled_time": scheduled_time,
        "status": "Pending",
        "created_at": datetime.now()
    }).execute()

def get_emails(user_id):
    return supabase.table("scheduled_emails").select("*").eq("user_id", user_id).execute()

def update_email_status(email_id, status):
    return supabase.table("scheduled_emails").update({"status": status}).eq("id", email_id).execute()

def delete_email(email_id):
    return supabase.table("scheduled_emails").delete().eq("id", email_id).execute()


# -----------------------------
# email_logs Table Operations
# -----------------------------
def create_email_log(email_id, recipient_email, status="Pending", sent_at=None):
    return supabase.table("email_logs").insert({
        "email_id": email_id,
        "recipient_email": recipient_email,
        "status": status,
        "sent_at": sent_at
    }).execute()

def get_email_logs(email_id):
    return supabase.table("email_logs").select("*").eq("email_id", email_id).execute()

def update_email_log_status(log_id, status, sent_at=None):
    data = {"status": status}
    if sent_at:
        data["sent_at"] = sent_at
    return supabase.table("email_logs").update(data).eq("id", log_id).execute()
