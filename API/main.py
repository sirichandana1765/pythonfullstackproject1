from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from SRC.logic import send_email
from SRC.db import add_email, mark_email_opened

scheduler = BackgroundScheduler()
scheduler.start()

app = FastAPI()

@app.post("/send")
async def send_email_api(data: dict):
    user_email = data["user_email"]
    recipient = data["recipient"]
    subject = data["subject"]
    body = data["body"]
    scheduled_time = datetime.fromisoformat(data["scheduled_time"])

    # Schedule email
    def job():
        track_code = send_email(user_email, recipient, subject, body, scheduled_time)
        if track_code:
            add_email(user_email, subject, body, recipient, scheduled_time.isoformat(), track_code)

    scheduler.add_job(job, 'date', run_date=scheduled_time)
    return {"message": f"Email scheduled for {scheduled_time}"}

@app.get("/track/{track_code}", response_class=HTMLResponse)
async def track_email(track_code: str):
    mark_email_opened(track_code)
    pixel = (
        b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00'
        b'\xFF\xFF\xFF\x21\xF9\x04\x01\x00\x00\x00\x00\x2C\x00\x00\x00\x00'
        b'\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3B'
    )
    return HTMLResponse(content=pixel, media_type="image/gif")
