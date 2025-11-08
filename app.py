from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import openai, os
from dotenv import load_dotenv

load_dotenv()

# Twilio + OpenAI setup (keep using env vars)
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")

client = Client(account_sid, auth_token)
app = Flask(__name__)

# Simple index page using Tailwind CDN

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    # your existing whatsapp webhook code (unchanged)
    try:
        incoming_msg = request.form.get("Body", "").strip()
        sender = request.form.get("From", "")
        print(f"Incoming message from {sender}: {incoming_msg}")

        completion = openai.chat.completions.create(
            model="gpt-5",
            messages=[
                {"role": "system", "content": "You are a friendly and smart WhatsApp assistant."},
                {"role": "user", "content": incoming_msg}
            ],
            max_tokens=512
        )

        gpt_reply = completion.choices[0].message.content.strip()

        resp = MessagingResponse()
        msg = resp.message()
        msg.body(gpt_reply)
        print(f"Replied: {gpt_reply}")
        return str(resp)

    except Exception as e:
        print("Error:", e)
        resp = MessagingResponse()
        resp.message("⚠️ Sorry, something went wrong.")
        return str(resp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
