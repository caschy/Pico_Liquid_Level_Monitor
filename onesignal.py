

try:
    import requests
    import json
    
except:
    import urequests as requests
    import ujson as json
    
class  Messenger():
    def __init__(self, __app_id,__api_key,__language="en"):
        self.app_id=__app_id
        self.api_key= __api_key
        self.language =__language
        self.header = {"Content-Type": "application/json; charset=utf-8",
                     "Authorization": "Basic "+self.api_key}
    
# Notifier inherits the class Messenger
class Notifier(Messenger):
    def __init__(self, __app_id,__api_key,__language="en"):
        Messenger.__init__(self, __app_id,__api_key,__language)
    
    
    def notify_segment(self,segment,message):

#         header = {"Content-Type": "application/json; charset=utf-8",
#                      "Authorization": "Basic "+self.api_key}
        
        payload = {"app_id": self.app_id,
                   "included_segments": [segment],
                   "contents": {self.language: message}}
        #print(payload)
        
        req = requests.post("https://onesignal.com/api/v1/notifications", headers=self.header, data=json.dumps(payload))
 
        print(req.status_code, req.reason)
        print(req.text)
        
    def notify_user(self,player_id,message):
        payload = {"app_id": self.app_id,
                   "include_player_ids": [player_id],
                   "contents": {self.language: message}}
        req = requests.post("https://onesignal.com/api/v1/notifications", headers=self.header, data=json.dumps(payload))
 
        print(req.status_code, req.reason)
        print(req.text)
        
        
        
class SMS_Messenger(Messenger):
    def __init__(self, __app_id,__api_key,__sender,__name,__language="en"):
        Messenger.__init__(self, __app_id,__api_key,__language)
        self.sender=__sender #sender's phone number
        self.name=__name #sender's name
        
        
    def send_text(self,message,receiver,image_urls=[]):
        payload = {
            "app_id": self.app_id,
            "name": self.name,
            "sms_from": self.sender,
            "contents": { self.language: message },
            "sms_media_urls": image_urls,
            "include_phone_numbers": receiver
           }
        print(payload)
        req = requests.post("https://onesignal.com/api/v1/notifications", headers=self.header, data=json.dumps(payload))
 
        print(req.status_code, req.reason)
        print(req.text)

class Mailer(Messenger):
    def __init__(self, __app_id,__api_key,__language="en"):
        Messenger.__init__(self, __app_id,__api_key,__language)

    def send_mail(self,subject,body,player_id):
        payload = {
            "app_id": self.app_id,
           "include_player_ids": [player_id],
           "email_subject": subject,
           "email_body": body 
           }
        req = requests.post("https://onesignal.com/api/v1/notifications", headers=self.header, data=json.dumps(payload))
 
        print(req.status_code, req.reason)
        print(req.text)





       
        
        

        