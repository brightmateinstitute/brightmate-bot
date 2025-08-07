from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
user_data = {}

@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get("Body", "").strip()
    from_number = request.values.get("From")

    resp = MessagingResponse()
    msg = resp.message()

    if from_number not in user_data:
        user_data[from_number] = {"stage": "name"}
        msg.body("👋 Hi! Welcome to *Brightmate Institute.*\nWhat's your name?")

    else:
        stage = user_data[from_number]["stage"]

        if stage == "name":
            user_data[from_number]["name"] = incoming_msg.title()
            user_data[from_number]["stage"] = "class"
            msg.body(f"Thanks, *{incoming_msg.title()}*! 🙌\nWhat class or exam are you preparing for? (e.g. 10th, NEET, JEE)")

        elif stage == "class":
            user_data[from_number]["class"] = incoming_msg.upper()
            user_data[from_number]["stage"] = "done"

            # Your brochure and counselling link
            brochure_link = "https://example.com/brightmate-brochure.pdf"
            counselling_link = "https://example.com/book-counselling"

            msg.body(
                f"🎯 Got it! You're interested in *{incoming_msg.upper()}*.\n\n"
                f"📎 Here's our brochure: {brochure_link}\n"
                f"📞 Book a free counselling: {counselling_link}\n\n"
                f"Would you like us to call you for a free consultation? Reply *YES* or *NO*."
            )

        elif stage == "done":
            if "yes" in incoming_msg.lower():
                msg.body("✅ Noted! Our team will call you soon. 😊")
            else:
                msg.body("👍 No problem! If you have any more questions, just message here.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
