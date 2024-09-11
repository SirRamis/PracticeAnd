# Плохой пример
class GenAndSend:
    def __init__(self,sms):
        self.sms = sms
    def gen_and_send(self):
        print('I gen sms')
        print('I send sms')

#Хороший пример

class GenSMS:
    def __init__(self, sms):
        self.sms = sms
    def gen(self):
        print('I gen sms')

class SendSMS:
    def __init__(self, sms):
        self.sms = sms
    def send(self):
        print('I send sms')
