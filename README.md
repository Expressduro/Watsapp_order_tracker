# **WhatsApp Order Tracker** 🚀  
A **Flask-based WhatsApp bot** for **order tracking**, integrated with **Twilio's WhatsApp API** and exposed using **Ngrok**.

---

## **📌 Features**
✅ Receive WhatsApp messages via Twilio  
✅ Process order tracking requests  
✅ Send automated order status responses  
✅ Expose local Flask server using Ngrok  
✅ Debug and deploy easily  

---

## **🛠 Prerequisites**  
Ensure you have the following installed:  
- **Python (≥3.8)** → [Download Here](https://www.python.org/downloads/)  
- **Flask** (Web framework)  
- **Twilio API Account** → [Sign up](https://www.twilio.com/)  
- **Ngrok** (To expose Flask) → [Download](https://ngrok.com/download)  

---

## **📥 Installation**  
### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/watsapp_order_tracker.git
cd watsapp_order_tracker
```

### **2️⃣ Create a Virtual Environment (Optional, Recommended)**  
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### **3️⃣ Install Dependencies**  
Since you only have two Python files, install required libraries manually:  
```bash
pip install flask twilio python-dotenv
```

---

## **📂 Project Structure**  
```
watsapp_order_tracker/
│── app.py               # Main Flask App
│── routes.py            # Routes for handling WhatsApp messages
│── .env                 # Twilio API Keys & Config
│── README.md            # Documentation
```

---

## **🔑 Setting Up `.env` File**  
Create a `.env` file inside the project folder and add:  
```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
FLASK_APP=app.py
FLASK_ENV=development
```
Replace `your_account_sid` and `your_auth_token` with values from your **[Twilio Console](https://www.twilio.com/console).**  

---

## **🚀 Running the Flask App**
### **1️⃣ Start the Flask Server**
Run the Flask app and make sure it is running on:  
```
http://127.0.0.1:5000
```

---

## **🌍 Expose Flask Using Ngrok**
### **1️⃣ Start Ngrok**
Open a new terminal and run:  
```bash
ngrok http 5000
```
Ngrok will generate a **public URL**, like:  
```
https://abcd-xyz.ngrok-free.app
```
Copy this URL for the **Twilio Webhook setup.**  

---

## **🔑 Twilio WhatsApp Webhook Setup**
### **1️⃣ Get a Twilio Account**
- Sign up at **[Twilio Console](https://www.twilio.com/console)**
- Get a **Twilio WhatsApp Sandbox Number**

### **2️⃣ Link Your WhatsApp to Twilio Sandbox**
#### **Option 1: Using Code**
Send this message on WhatsApp to **+1 415 523 8886**:
```
join drew-than
```
#### **Option 2: Using QR Code**
- Scan the QR code from your **Twilio Console**.
- Send the prefilled message.

✅ **Now your WhatsApp number is linked!**

---

### **3️⃣ Set Webhook in Twilio**
Go to **Twilio Console** → **Messaging** → **WhatsApp Senders** → **Sandbox Settings**.  
- Find **“When a message comes in”**.  
- **Paste your Ngrok URL** + `/webhook`, like:  
  ```
  https://abcd-xyz.ngrok-free.app/webhook
  ```
- **Click "Save".**

---

## **🧪 Testing**
- Open WhatsApp and **send an order ID** (e.g., `12345`) to the Twilio number.  
- The Flask bot should respond with order details.

---

## **🐞 Debugging**
### **1️⃣ Flask Debug Mode**
Run Flask in debug mode to enable **hot reloading** for code changes.

### **2️⃣ Ngrok Debugging**
Check Ngrok logs to ensure requests are being forwarded correctly.

### **3️⃣ Flask Error Debugging**
Use debugging tools and logs to track errors efficiently.

---

## **🚀 Deployment**
For **production deployment**, use **Gunicorn & a Cloud Server (AWS, Heroku, etc.).**  
### **1️⃣ Install Gunicorn**
```bash
pip install gunicorn
```
### **2️⃣ Run with Gunicorn**
```bash
gunicorn -w 4 app:app
```
### **3️⃣ Deploy to Cloud**
- **Heroku** → [Guide](https://devcenter.heroku.com/articles/getting-started-with-python)  
- **AWS EC2** → [Guide](https://aws.amazon.com/getting-started/hands-on/deploy-python-application/)  
- **Railway.app** (Simple Deployment) → [Guide](https://railway.app/)  

---

## **📌 Common Issues & Fixes**
| Issue | Fix |
|-------|-----|
| `ModuleNotFoundError: No module named 'flask'` | Run `pip install flask` |
| `Ngrok Authentication Error` | Run `ngrok config add-authtoken YOUR_AUTH_TOKEN` |
| `Twilio Webhook Not Working` | Check if your **Ngrok URL** is correct in Twilio |

---

## **📜 License**
This project is **MIT Licensed**.
