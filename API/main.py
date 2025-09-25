# main.py
import sys
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

# Add src folder to path to import EmailManager
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from logic import EmailManager

# Initialize FastAPI app
app = FastAPI(
    title="Email Automation System",
    version="1.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize EmailManager
email_manager = EmailManager()

# -----------------------------
# Pydantic Models
# -----------------------------
class UserModel(BaseModel):
    name: str
    email: str
    password_hash: str

class ContactModel(BaseModel):
    user_id: int
    name: str
    email: str

class ScheduledEmailModel(BaseModel):
    user_id: int
    subject: str
    body: str
    scheduled_time: datetime

class EmailLogModel(BaseModel):
    email_id: int
    recipient_email: str
    status: str = "Pending"

# -----------------------------
# Users Routes
# -----------------------------
@app.post("/users")
def create_user(user: UserModel):
    result = email_manager.add_user(user.name, user.email, user.password_hash)
    if not result:
        raise HTTPException(status_code=400, detail="Failed to create user")
    return {"message": "User created successfully", "data": result}

@app.get("/users")
def get_users():
    return email_manager.list_users()

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserModel):
    return email_manager.update_user_info(user_id, user.name, user.email, user.password_hash)

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return email_manager.remove_user(user_id)

# -----------------------------
# Contacts Routes
# -----------------------------
@app.post("/contacts")
def create_contact(contact: ContactModel):
    return email_manager.add_contact(contact.user_id, contact.name, contact.email)

@app.get("/contacts/{user_id}")
def get_contacts(user_id: int):
    return email_manager.list_contacts(user_id)

@app.put("/contacts/{contact_id}")
def update_contact(contact_id: int, contact: ContactModel):
    return email_manager.update_contact_info(contact_id, contact.name, contact.email)

@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):
    return email_manager.remove_contact(contact_id)

# -----------------------------
# Scheduled Emails Routes
# -----------------------------
@app.post("/emails")
def create_email(email: ScheduledEmailModel):
    return email_manager.add_scheduled_email(
        email.user_id, email.subject, email.body, email.scheduled_time
    )

@app.get("/emails/{user_id}")
def get_emails(user_id: int):
    return email_manager.list_scheduled_emails(user_id)

@app.put("/emails/{email_id}")
def update_email_status(email_id: int, status: str):
    return email_manager.update_email_status(email_id, status)

@app.delete("/emails/{email_id}")
def delete_email(email_id: int):
    return email_manager.remove_scheduled_email(email_id)

# -----------------------------
# Email Logs 
# -----------------------------
@app.post("/email-logs")
def create_email_log(log: EmailLogModel):
    return email_manager.add_email_log(log.email_id, log.recipient_email, log.status)

@app.get("/email-logs/{email_id}")
def get_email_logs(email_id: int):
    return email_manager.list_email_logs(email_id)

@app.put("/email-logs/{log_id}")
def update_email_log(log_id: int, status: str):
    return email_manager.update_email_log(log_id, status)
