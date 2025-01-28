import os
from flask import Blueprint, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

bp = Blueprint('routes', __name__)

# Twilio credentials
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Mock database for order tracking
orders = {
    "12345": {"status": "Shipped", "delivery_date": "2025-02-01"},
    "67890": {"status": "Processing", "delivery_date": "2025-02-05"}
}

@bp.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.form.get('Body').strip()
    sender = request.form.get('From')

    response = MessagingResponse()

    if incoming_msg.isdigit() and incoming_msg in orders:
        order = orders[incoming_msg]
        reply = (
            f"📦 Order ID: {incoming_msg}\n"
            f"✅ Status: {order['status']}\n"
            f"🚚 Expected Delivery: {order['delivery_date']}"
        )
    else:
        reply = "❌ Invalid Order ID. Please send a valid Order ID to track."

    response.message(reply)
    return str(response)
