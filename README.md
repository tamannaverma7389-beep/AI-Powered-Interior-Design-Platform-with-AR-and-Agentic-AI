🏠 Gruha Alankara
AI Powered Interior Design Platform with AR and Agentic AI
📌 Overview

Gruha Alankara is an innovative interior design application that integrates Artificial Intelligence, Computer Vision, Augmented Reality (AR) simulation, and Agentic AI to deliver personalized interior design recommendations.

The platform allows users to upload room images, detect interior styles automatically, generate AI-based design suggestions, visualize furniture placement through AR overlay, and book furniture with multilingual voice confirmation.

The system is fully cloud-independent and operates using local infrastructure.

🚀 Key Features

🧠 AI-based Room Style Detection (CLIP Model)

🖼 Computer Vision Room Analysis (OpenCV)

✨ AI Design Recommendation (Transformers – FLAN-T5)

📷 AR Camera Integration (WebRTC + Canvas Overlay)

🖱 Drag & Scale Furniture Placement

🤖 Agentic AI Booking Assistant (LangChain)

🔊 Multilingual Voice Confirmation (English, Hindi, Telugu)

🗄 SQLite Database with SQLAlchemy ORM

📊 User Dashboard for Designs & Bookings

🎨 Dark Themed Modern UI

🛠 Technologies Used

Python

Flask

SQLAlchemy

Transformers (HuggingFace)

OpenCV

LangChain

gTTS (Google Text-to-Speech)

WebRTC API

SQLite

HTML, CSS, JavaScript

🏗 System Architecture

The application follows a modular three-layer architecture:

1️⃣ Application Layer

Flask backend

API routing

Session management

Request handling

2️⃣ AI/ML Services

Style Detection (CLIP Zero-shot Image Classification)

Room Analysis (OpenCV Edge Detection)

AI Recommendation Generator (FLAN-T5)

Agentic Booking System (LangChain)

Multilingual Voice Output (gTTS)

3️⃣ Data Layer

SQLite Database

User Management

Design History

Booking Records

Furniture Catalog

📂 Project Structure
alaknkar/
│
├── app.py
├── config.py
├── requirements.txt
│
├── models/
├── services/
├── static/
│   ├── css/
│   ├── js/
│   ├── furniture/
│   └── uploads/
│
└── templates/
⚙ Installation & Setup
Step 1: Clone Repository
git clone YOUR_GITHUB_LINK
cd alaknkar
Step 2: Create Virtual Environment
python -m venv venv
venv\Scripts\activate
Step 3: Install Dependencies
pip install -r requirements.txt
Step 4: Run Application
python app.py

Open browser:

http://127.0.0.1:5000
🖥 Deployment

The application can be deployed using:

Render (with Gunicorn)

PythonAnywhere

Local Network Deployment

Procfile for Deployment
web: gunicorn app:app
🤖 How Agentic AI Works

The Buddy AI agent:

Receives booking intent

Processes user request

Executes booking tool

Generates voice confirmation

Stores transaction in database

This demonstrates basic agent-based task automation.

🎯 Project Workflow

User uploads room image

AI detects interior style

OpenCV analyzes room structure

AI generates decor recommendations

User visualizes furniture via AR overlay

User books furniture

Agent confirms booking via voice

Data saved in database

📊 Database Models

User

Design

Booking

Furniture

All managed using SQLAlchemy ORM.

🔐 Security & Configuration

Environment-based secret key

Production-ready Gunicorn setup

Debug disabled for deployment

📌 Future Enhancements

Real 3D object rendering

Advanced depth-based AR placement

Improved object detection models

Cloud storage integration

Real e-commerce API integration

👩‍💻 Team Members

Tamanna Verma

Tanishka Sharma

Sreya Sethu 

## 📸 Project Screenshots

### 🏠 Home Page
<img width="871" height="767" alt="Screenshot 2026-03-02 142855" src="https://github.com/user-attachments/assets/64244a32-1915-44da-8249-d370ba2703a1" />


### 📤 Upload Room Image
<img width="814" height="581" alt="image" src="https://github.com/user-attachments/assets/42f8c0cb-6a3b-4309-a034-e221ed19509b" />


### 🤖 AI Recommendation
<img width="871" height="869" alt="Screenshot 2026-03-02 143112" src="https://github.com/user-attachments/assets/43a547c7-f3b1-4b2f-8fcb-b0ef28924e3c" />

📜 Conclusion

Gruha Alankara demonstrates how AI, AR simulation, and intelligent automation can transform interior design experiences. The project showcases integration of machine learning, computer vision, web development, and database management into a unified system.
