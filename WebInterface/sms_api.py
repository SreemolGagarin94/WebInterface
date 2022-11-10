from WebInterface.forms import sms_sendingForm
import requests
import json

def authenticate():
    CLIENT_ID= '0HHvPbWNKCPBKJsVCXHNZwnwNCswm7aUmACH05LO'
    CLIENT_SECRET='c8fbXesUQphs3rGYaNtzw4uxEGl7jWu9D9shODapXo5SdzOx5MwJ4JA43iXEwEx5qDG28zXubP3DogqbpWlri8qIQps61RI6wsTnGO0KMx7X1mAZm3Ugo40cPMONL728'
    url = "https://api.d7networks.com/auth/v1/login/application"
    payload={'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET}
    files=[

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    access_key=json.loads(response.text)
    return access_key['access_token']

def sendSMS(form):     
    URL = "https://api.d7networks.com/messages/v1/send"
    KEY = authenticate()
    payload = json.dumps({
    "messages": [
        {
        "channel": "sms",
        "recipients": form.recipients.data,
        "content": form.content.data,
        "msg_type": "text",
        "data_coding": "text"
        }
    ],
    "message_globals": {
        "originator": form.originator.data,
        "report_url": "https://the_url_to_recieve_delivery_report.com"
    }
    })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {KEY}'
    }
    print(payload)
    print(headers)
    response = requests.request("POST", URL, headers=headers, data=payload)
    return