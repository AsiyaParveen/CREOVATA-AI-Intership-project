# Creovata-Ai-intern-project
## Internship Help Desk Bot – Creovate

This is an AI-powered chatbot developed during my internship at **Creovate**, aimed at helping users with
internship-related queries through a simple, intelligent, and user-friendly interface.

### 📌 Overview

The bot is trained on custom intents using a **Multinomial Naive Bayes classifier** and deployed via a Flask web server. 
It responds to user inputs based on natural language patterns defined in a structured JSON file.

---

### Technologies & Tools Used

* **Programming Languages**: Python, HTML, CSS, JavaScript
* **Model**: Multinomial Naive Bayes (from scikit-learn)
* **Libraries/Frameworks**:

  * `scikit-learn` – for model training
  * `nltk` – for natural language preprocessing
  * `Flask` – for backend API
  * `Pickle` – for saving the trained model
* **Frontend**: HTML, CSS (custom UI styling in `style.css`)
* **Backend**: Python (Flask server in `app.py`)
* **Chat Logic**: Trained using custom intents defined in `intents.json`

---

### 📁 Project Structure

```
internship-chatbot/
├── model/
│   └── trained_model.pkl       # Trained Multinomial Naive Bayes model
├── train_model.py              # Model training script
├── chatbot.py                  # Logic to process user inputs and return responses
├── intents.json                # Training data and intents
├── app.py                      # Flask server
├── templates/
│   └── index.html              # Chatbot UI template
├── static/
│   └── style.css               # Frontend styling
├── requirements.txt            # All required Python packages
└── README.md                   # Project documentation
```

---

### ✅ Features

* AI-powered response generation based on custom intents
* Clean and dynamic web-based UI
* Lightweight and easy to retrain with new intents
* Ideal for helping interns and students get answers quickly

---
