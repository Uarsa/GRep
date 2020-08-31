import telebot
import json


bot = telebot.TeleBot("1346425132:AAHZfTwGvYBBDoJpRaFNMzqnXmNSuWxH6hg")
filename = "nums.json"


def report(text):
    
    s = text.split("; ")
    day = s[0]
    water = s[1]
    desc = s[2]
    
    try:
        file = open(filename) 
        rep = json.load(file)
        lst = []
        w = str(water)
        lst = [w, desc]
        rep[day] = lst
        file.close()
        
    except FileNotFoundError:
        rep = {}
        file = open(filename, 'w')
        lst = []
        w = str(water)
        lst = [w, desc]
        rep[day] = lst
        file.close()
    
    filea = open(filename, 'w')
    json.dump(rep, filea)
    filea.close()
    
       
@bot.message_handler(commands=['start'])
def handle_start(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row("/start", "/show")
        bot.send_message(message.from_user.id, "Пришли данные в формате:\nдень; вода; описание.", reply_markup=user_markup)
        
        
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "/show":
        
        try:
            rep = json.load(open(filename))
            for i in range(150):
                for k, v in rep.items():
                    if i == int(k):
                        bot.send_message(message.chat.id, "ДЕНЬ " + str(i) + ":\n" + "полив: " + rep.get(str(k))[0] + " л.\n" + "описание: " + rep.get(str(k))[1] + ".")
                        
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Записи отсутствуют.")
            
    else:    
        try:
            
            report(str(message.text))
            bot.send_message(message.chat.id, "Данные добавлены.")   
            
        except:
            bot.send_message(message.chat.id, "Ошибка...")
             
        
bot.polling(none_stop=True, interval=0)    
