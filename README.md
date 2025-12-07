# ⚡ AI Text Detector — Detect AI vs Human-Written Text

A full-stack machine learning web application that analyzes writing patterns to determine whether a piece of text is **AI-generated** or **human-written**, along with a probability score.

## 🚀 Live Demo
🔗 https://ai-text-detector.vercel.app/ 

---

## 🧠 Features
- Classifies text as **AI-generated** or **Human-written**
- Shows **probability score** for clarity
- Fast and lightweight **Logistic Regression** model
- Beautiful **futuristic neon hacker UI**
- Real-time inference using **FastAPI**
- Deployed with **Vercel (frontend)** and **Render (backend)**

---

## 🛠️ Tech Stack

### **Machine Learning**
- Python  
- Scikit-learn  
- Logistic Regression  
- Joblib  

### **Backend**
- FastAPI  
- Uvicorn  
- Render deployment  

### **Frontend**
- HTML  
- CSS (Neon Hacker Theme)  
- JavaScript (fetch API)  
- Vercel deployment  

---

## 📂 Project Structure

ai-text-detector/
├── data/ # Training data (ignored in production)
├── models/
│ └── ai_detector.joblib # Trained model
├── src/
│ ├── app.py # FastAPI backend
│ ├── combine_data.py # Dataset merging script
│ └── train_model.py # Model training script
├── frontend/
│ ├── index.html
│ └── styles.css
├── requirements.txt
└── README.md

---

## 🔧 How It Works

1. User enters text in the UI  
2. Frontend sends a POST request to `/detect`  
3. Backend loads the ML model and predicts AI vs Human  
4. Result + probability is returned to the frontend  
5. UI displays a glowing classification panel + animations  

---

## 🏁 Local Development

### Clone repository:
```bash
git clone https://github.com/<username>/ai-text-detector
cd ai-text-detector
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Run backend:
bash
Copy code
uvicorn src.app:app --reload
Open frontend:
Open frontend/index.html with Live Server or browser.

🌐 Deployment
Backend (Render)
Use:

nginx
Copy code
uvicorn src.app:app --host 0.0.0.0 --port $PORT
Frontend (Vercel)
Deploy frontend/ as root folder
Update API URL in index.html:

js
Copy code
fetch("https://your-backend.onrender.com/detect")
🤝 Contributing
Pull requests are welcome.

📬 Contact
Portfolio: https://my-portfolio-website-seven-lemon.vercel.app/
Made by Apoorwa Kumar
