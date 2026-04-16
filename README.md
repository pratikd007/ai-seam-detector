# 🚨 AI Scam Detector Pro

## 📌 Overview

AI Scam Detector Pro is a web-based application that analyzes messages and detects whether they are **SCAM or SAFE** using Machine Learning.

This project helps users identify phishing attempts, fake offers, and fraud messages in real time.

---

## 🚨 Problem

Scam messages are increasing rapidly:

* Fake lottery messages
* Phishing links
* OTP & bank fraud

Many users cannot easily identify these scams.

---

## 💡 Solution

This project uses **Machine Learning (Naive Bayes)** to:

* Analyze text messages
* Predict scam probability
* Display a risk score

---

## ⚙️ Features

* ✅ Scam / Safe classification
* 📊 Risk score (%)
* 🌐 Web-based interface
* 💻 C version (basic logic demo)

---

## 🧠 Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, JavaScript
* **Machine Learning:** Scikit-learn (Naive Bayes)
* **Other:** Flask-CORS

---

## 📂 Project Structure

```
scam-detector/
│
├── backend/
│   ├── app.py
│   ├── model.py
│   ├── train_model.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│
├── c_version/
│   ├── scam_detector.c
│
└── README.md
```

---

## 🚀 How to Run

### 2️⃣ Install Dependencies

```
pip install flask flask-cors scikit-learn pandas
```

---

### 3️⃣ Train Model

```
cd backend
python train_model.py
```

---

### 4️⃣ Run Backend Server

```
python app.py
```

Server runs on:

```
http://127.0.0.1:5000
```

---

### 5️⃣ Run Frontend

* Open `frontend/index.html`
  OR
* Use Live Server in VS Code

---

---

## 🧪 Example

**Input:**

```
Congratulations! You won a lottery. Click here now!
```

**Output:**

```
SCAM (Risk Score: 85%)
```

---

## 🔮 Future Improvements

* 📧 Email phishing detection
* 🌐 Chrome Extension
* 📱 Mobile App
* 📊 Advanced ML models (Deep Learning)

---

## 👨‍💻 Author

Pratik Dhumale

---

## ⭐ Contribute

Feel free to fork this repo and improve the project!

---

## 📜 License

This project is open-source and free to use.
