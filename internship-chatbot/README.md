# 🤖 Internship Help Desk Chatbot

A simple FAQ chatbot built using Python and Flask to help interns find answers about their program.

## 🛠️ Technologies Used
- Python 3
- Flask
- JSON

## 🚀 How to Run

1. Clone this repo or download the folder.
2. Run:

```bash
pip install flask
python app.py
Zaroor! Neeche is **Internship Help Desk Chatbot Project** ka **Roman Urdu** mein asaan aur simple explanation diya gaya hai:

---

### 🔍 **Project Overview - Internship Help Desk Chatbot**

Ye project ek **FAQ chatbot** hai jo interns ke common sawalon ka jawab dene ke liye banaya gaya hai. Isme Python, Flask (web framework), aur ek simple AI model (`Naive Bayes classifier`) use kiya gaya hai.

---

### 🗂 **Har File ka Kaam (Roman Urdu)**

#### ✅ `app.py`

* **Purpose:** Ye main file hai jo chatbot ko web pe chalanay ka kaam karti hai.
* **Kaise Kaam Karti Hai:**

  * Flask web app start karti hai.
  * User ka message receive karti hai.
  * Us message ko `chatbot.py` ko bhejti hai.
  * Wahan se AI response aata hai aur chat history mein show hota hai.
  * Ek `clear` route bhi hai jo pura chat history delete kar deta hai.

#### ✅ `chatbot.py`

* **Purpose:** Ye file AI model aur chatbot ka dimaagh hai.
* **Kaise Kaam Karti Hai:**

  * `intents.json` file se chatbot ke sawal-jawab load karti hai.
  * `trained_model.pkl` se trained AI model load karti hai.
  * User ka message predict karke relevant jawab nikalti hai.

#### ✅ `intents.json`

* **Purpose:** Ye file chatbot ka syllabus hai — isme likha hota hai:

  * Kis topic pe sawal aasakta hai (e.g., "greeting", "project").
  * Us topic se related kya-kya sawalat ho sakte hain (patterns).
  * Aur un sawalon ke possible answers (responses).

#### ✅ `train_model.py`

* **Purpose:** Ye script AI model train karne ke liye use hoti hai.
* **Kaise Kaam Karti Hai:**

  * `intents.json` se data uthati hai.
  * Har pattern ko ek number form mein convert karti hai (using `CountVectorizer`).
  * `MultinomialNB` model train hota hai.
  * Trained model aur vectorizer ko `trained_model.pkl` mein save karti hai.

#### ✅ `trained_model.pkl`

* **Purpose:** Ye file AI ka trained dimaagh store karti hai.
* **Kaise Kaam Karti Hai:** Ye ek binary file hai jo trained model aur text vectorizer ka data rakhti hai.

#### ✅ `index.html`

* **Purpose:** Ye chatbot ka front-end design banata hai (user jo dekhta hai).
* **Kaise Kaam Karti Hai:**

  * Chat box banata hai jahan user message type karta hai.
  * Jinja2 templating use karta hai taake Flask se data display ho.

#### ✅ `style.css`

* **Purpose:** Chatbot ka look aur feel is file se tay hota hai.
* **Kaise Kaam Karti Hai:** Fonts, colors, box design, layout sab CSS se design kiya gaya hai.

#### ✅ `README.md`

* **Purpose:** Project ka manual ya user guide hai.
* **Kaise Kaam Karti Hai:** Isme likha hota hai project ka overview, kaise run karna hai, aur kaun se tools use hue hain.

#### ✅ `requirements.txt`

* **Purpose:** Python libraries ka list hota hai jise `pip install -r requirements.txt` se install kiya jata hai.
* **Kaise Kaam Karti Hai:** Is file mein likhe libraries chatbot ko run karne ke liye zaroori hain.

#### ✅ `chatbot.cpython-313.pyc`

* **Purpose:** Ye ek auto-generated file hoti hai jab Python koi file run karta hai.
* **Kaise Kaam Karti Hai:** Ye file Python code ka fast version hoti hai (bytecode form).

---

### 🤖 **AI Chatbot Kaise Kaam Karta Hai? (Simple Roman Urdu)**

1. **Training Phase:**

   * `train_model.py` se AI model train hota hai `intents.json` ke patterns se.
2. **Prediction Phase:**

   * Jab user koi sawal bhejta hai, `chatbot.py` us sawal ka intent predict karta hai.
3. **Response Generation:**

   * Predict kiya gaya intent match hone pe, uska jawab `intents.json` se randomly diya jata hai.
4. **User Interface:**

   * `index.html` aur `style.css` mil ke chatbot ka UI banate hain.
   * `app.py` user ke message ko `chatbot.py` tak bhejta hai aur wapas response user ko dikhata hai.

---

