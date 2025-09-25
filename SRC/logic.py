# src/logic.py
from src.db_manager import *

class EmailManager:
    """
    Handles the core logic of the Email Automation System:
    - Users
    - Contacts
    - Scheduled Emails
    - Email Logs
    """

    def __init__(self):
        # No initialization required; db_manager functions are standalone
        pass

    # -----------------------------
    # User Operations
    # -----------------------------
    def add_user(self, name, email, password_hash):
        """Add a new user to the database."""
        try:
            return create_user(name, email, password_hash)
        except Exception as e:
            print("Error adding user:", e)
            return None

    def list_users(self):
        """Return all users"""
        return get_all_users()

    def update_user_info(self, user_id, name=None, email=None, password_hash=None):
        """Update user details"""
        return update_user(user_id, name, email, password_hash)

    def remove_user(self, user_id):
        """Delete a user"""
        return delete_user(user_id)

    # -----------------------------
    # Contact Operations
    # -----------------------------
    def add_contact(self, user_id, name, email):
        """Add a contact for a specific user"""
        return create_contact(user_id, name, email)

    def list_contacts(self, user_id):
        """List all contacts for a user"""
        return get_contacts(user_id)

    def update_contact_info(self, contact_id, name=None, email=None):
        """Update contact details"""
        return update_contact(contact_id, name, email)

    def remove_contact(self, contact_id):
        """Delete a contact"""
        return delete_contact(contact_id)

    # -----------------------------
    # Scheduled Emails Operations
    # -----------------------------
    def add_scheduled_email(self, user_id, subject, body, scheduled_time):
        """Add a new scheduled email for a user"""
        return create_email(user_id, subject, body, scheduled_time)

    def list_scheduled_emails(self, user_id):
        """List all scheduled emails for a user"""
        return get_emails(user_id)

    def update_email_status(self, email_id, status):
        """Update the status of a scheduled email (Pending/Sent/Failed)"""
        return update_email_status(email_id, status)

    def remove_scheduled_email(self, email_id):
        """Delete a scheduled email"""
        return delete_email(email_id)

    # -----------------------------
    # Email Logs Operations
    # -----------------------------
    def add_email_log(self, email_id, recipient_email, status="Pending", sent_at=None):
        """Add a log entry for an email sent to a recipient"""
        return create_email_log(email_id, recipient_email, status, sent_at)

    def list_email_logs(self, email_id):
        """List all email logs for a scheduled email"""
        return get_email_logs(email_id)

    def update_email_log(self, log_id, status, sent_at=None):
        """Update the status of an email log"""
        return update_email_log_status(log_id, status, sent_at)
