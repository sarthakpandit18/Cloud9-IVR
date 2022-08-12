# Cloud9-IVR

### This is cloud-based application that helps creating IVR services for any business model. The busienss model used here is courier tracking system. 


Steps :

1. Clone the repository
2. Follow the below setup steps 

**venv setup** 

$ python -m venv venv

$ source venv/bin/activate

$ venv\Scripts\activate

**Setup django project, twilio, boto3**

(venv) $ pip install django

(venv) $ pip install twilio

(venv) $ pip3 install boto3

**Run python server**

(venv) $ python manage.py runserver

**Run ngrok tunnel to make a call to IVR**

ngrok http 8000

**Setup via Docker**

1. Add the twilio authentication credentials to scripts/ngrok.sh
2. Build and run the docker image (This runs the application by updating the ngrok link in your twilio account)
Eg : docker build --no-cache --platform linux/amd64 -t <image name> .
	 docker run -it -p 127.0.0.1:8000:8000 <image name>
3. Call to your IVR number to verify


