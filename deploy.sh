GCP_PROJECT=telegram-shame-bot-277421
APP_NAME=telegram-shame-bot
gcloud config set project $GCP_PROJECT
pack build telegram-shame-bot
pack build --publish gcr.io/$GCP_PROJECT/$APP_NAME
gcloud run deploy telegram-shame-bot --image gcr.io/$GCP_PROJECT/$APP_NAME --region us-central1 --platform managed --allow-unauthenticated
gcloud run services update-traffic telegram-shame-bot --to-latest --platform managed --region us-central1