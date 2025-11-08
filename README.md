# 📱 WhatsApp ChatGPT Bot (Flask + Twilio + OpenAI GPT-5)

A simple Python web app that connects **WhatsApp** messages to **ChatGPT (GPT-5)** using **Twilio’s WhatsApp API** and **Flask**.  
The bot listens for incoming WhatsApp messages and replies intelligently using OpenAI’s GPT-5 model.

----------

## 🚀 Features

-   💬 Real-time WhatsApp replies powered by ChatGPT (GPT-5)
    
-   🔐 Secure environment variable management (`.env`)
    
-   🌐 Local testing with `ngrok`
    
-   ⚡ Lightweight Flask backend
    
-   🧠 Optional conversation memory support
    
-   🎨 TailwindCSS-based homepage to confirm the server is running
    

----------

## 🏗️ Project Structure

```
whatsapp-gpt-bot/
│
├── app.py                # Main Flask app (Twilio + GPT logic)
├── requirements.txt      # Python dependencies
├── .env                  # API keys (excluded via .gitignore)
├── .gitignore            # Ignore sensitive and generated files
└── templates/
    └── index.html        # Simple TailwindCSS server page

```

----------

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/abdellahaarab/WhatsApp-bot-in-Python-that-replies-using-ChatGPT.git
cd WhatsApp-bot-in-Python-that-replies-using-ChatGP
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows

```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt

```

----------

## 🔑 Environment Setup

Create a file named `.env` in your project root:

```bash
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxx
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx

```

⚠️ **Do NOT commit this file to GitHub** — your API keys are private.

----------

## 💬 Twilio WhatsApp Sandbox Setup

1.  Go to [Twilio WhatsApp Sandbox](https://www.twilio.com/console/sms/whatsapp/learn)
    
2.  Follow the setup instructions to join the sandbox (send the join code via WhatsApp)
    
3.  Copy the **sandbox number** (e.g., `+14150000000`)
    
4.  Under “**When a message comes in**”, add your webhook URL — you’ll configure it next using **ngrok**
    

----------

## 🌐 Running the App Locally

### 1️⃣ Start Flask server

```bash
python app.py

```

You’ll see something like:

```
* Running on http://127.0.0.1:5000

```

### 2️⃣ Expose the server using ngrok

Install ngrok if you don’t have it:

```bash
npm install -g ngrok

```

Run:

```bash
ngrok http 5000

```

Copy your HTTPS link, e.g.:

```
Forwarding  https://abcd1234.ngrok.io -> http://localhost:5000

```

Then go back to your **Twilio Sandbox settings** and paste it in:

```
https://abcd1234.ngrok.io/whatsapp

```

✅ Save changes.

----------

## 📲 Test It!

Now, send a WhatsApp message to your Twilio sandbox number:

```
You: Hello bot!
Bot: Hello there 👋 How can I help you today?

```



----------

## 🚀 Deployment Options

You can deploy your bot on any free hosting service:

Platform

Notes

[Render](https://render.com/)

Free Flask hosting

[Railway](https://railway.app/)

Easiest one-click deployment

[Replit](https://replit.com/)

Runs directly in the browser

[Fly.io](https://fly.io/)

Scalable + simple Docker setup

----------

## 🧰 Technologies Used

-   **Python 3.8+**
    
-   **Flask** – lightweight backend framework
    
-   **Twilio API** – WhatsApp messaging gateway
    
-   **OpenAI GPT-5** – AI language model
    
-   **TailwindCSS** – clean UI styling via CDN
    
-   **Ngrok** – local HTTPS tunneling
    

----------

## 🧑‍💻 Author

**Dr. Abdellah**  
📺 YouTube: [@aarabxdrg](https://www.youtube.com/@)  
💡 Developer & Educator — programming, robotics, and AI automation tutorials.

----------

## 🛡️ License

This project is licensed under the **MIT License** — you’re free to use, modify, and distribute it with attribution.

