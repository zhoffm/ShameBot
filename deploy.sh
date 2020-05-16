export PROJECT_ID=telegram-shame-bot-277421
gcloud builds submit --tag gcr.io/$PROJECT_ID/ShameBot
gcloud run deploy --image gcr.io/$PROJECT_ID/helloworld --platform managed