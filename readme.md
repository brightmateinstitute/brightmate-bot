# Brightmate Institute WhatsApp Bot

This is a ready-to-deploy WhatsApp bot for Brightmate Institute to help increase admissions.

## Features

- Collects student name and class
- Sends brochure and counselling link
- Handles replies (YES/NO)
- Deployable on platforms like Render or locally with ngrok

## Setup Instructions

1. Clone the repo:
```
git clone https://github.com/yourusername/brightmate-bot.git
cd brightmate-bot
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run locally:
```
python app.py
```

4. Expose using ngrok:
```
ngrok http 5000
```

5. Use the HTTPS ngrok URL in Twilio WhatsApp Sandbox settings.

## Twilio Setup

- Sign up at https://www.twilio.com
- Go to Messaging → Try It Out → WhatsApp Sandbox
- Set the webhook to: `https://your-domain.com/bot`

## Customize

- Edit brochure and counselling links in `app.py`
- Add more stages if needed

## License

MIT
