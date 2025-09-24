# Email Automation System
An Email Automation System is a software application that allows users to compose, schedule, and send emails automatically to one or multiple recipients. It is designed to save time, improve efficiency, and enable users to manage email campaigns without manual intervention.

# keyfeatures
Key Features

Users

Sign up, log in, and manage campaigns.

Contacts

Save contacts and group them.

Templates

Create reusable emails.

Personalize with names.

Sending Emails

Send now or schedule for later.

Works with Gmail, Outlook, or email services.

Tracking

See if emails are sent or failed.

Track opens and clicks.
# project structure
EMAIL/
├── src/ # Core application logic
│ ├── logic.py # Business logic and task operations
│ └── db.py # Database operations
│
├── api/ # Backend API
│ └── main.py # FastAPI endpoints
│
├── frontend/ # Frontend application
│ └── app.py # Streamlit web interface
│
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .env # Environment variables

# quick start
python 3.8 or higher
a supabase account
git(push,cloning)
### 1.cone or download the project
# option 1:clone with Git
git clone <repository url>
# option 2:Download and extract the zip file
### 2. install dependencies
# Install all required python packages
pip install -r requirements.txt
### 3.set up supabase database
1.create a supabase  project:
2.create the task table
-go to the sql editor in your supase
run the sql command;

--sql











##  4 configure environment variables
1.create a .env file in the project root
2.add your supabase credentials to '.env':
SUPABASE_URL=""
SUPABASE_KEY="your key"
# Example
SUPABASE_URL="https://pqtjslcsijjynnexboqj.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFpaHp4eG9zZXR0b3JmcmFraXpjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODIwNDQsImV4cCI6MjA3MzY1ODA0NH0.Ebw2ZwEymICaYg6_mmSSNzajiy5joIQW9DGHdNBepE4"
# run the application
## streamlit frontend
streamlit run frontend/app.py
the app will open in your browser at "http://localhost:8501"
# Fast api
cd api
python main.py
 the app will be available at 'http://localhost:8000'
 # how to use 
# technologies used
# technologies used
" frontend":streamlit (python web frame work)
"backend":FASTAPI(python RESTAPI framework)
"database":supabase(postgresql:based backend as-a-sevice)
**language**:python 3.8+
## key components
1.**`SRC/db.py`**:database operatation handels all CRUD operations with supabase
2.**`src/logic.py`**:busisness logic
-task validation and processing
## Troublesshooting
## common issues
1.**"trouble not found" errors**
-make sure you've installed all dependencies:`pip install -r requirements.txt`
-check that you've  running commands from the correct directory 
# future enchancements 
ideas for extending this projects 
**user authentication**:add your accounts and login 
**task categories**:organise task by subject or category 
**notification**:email or push  notifications for due dates 
**file attachments**:attach files to tasks
**collaboration**:share tasks with classmates
**mobileapp**:react value 