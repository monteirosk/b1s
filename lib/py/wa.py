from whatsapp import Client
import sys
args = str(sys.argv[1])
t = args.split("+")
phone_to =t[0]
name =t[1]
mensagem =t[2]
log = t[3]
pwd = t[4]

client = Client(login=log, password=pwd)
client.send_message(phone_to, mensagem)
client.send_message(phone_to, 'Entre em contato conosco para maiores informacoes, 5592994511685')