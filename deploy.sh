gcloud builds submit --tag gcr.io/telegram-shame-bot-277421/telegram-shame-bot
gcloud run deploy --image gcr.io/telegram-shame-bot-277421/telegram-shame-bot --platform managed