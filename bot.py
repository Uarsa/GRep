import telebot
import json


bot = telebot.TeleBot("1346425132:AAHZfTwGvYBBDoJpRaFNMzqnXmNSuWxH6hg")
filename = "nums.json"

def report(text):
    
    s = text.split(",")
    day = s[0]
    water = s[1]
    desc = s[2]
    
    try:
        file = open(filename) 
        rep = json.load(file)
        lst = []
        w = str(water) + ' litres'
        lst = [w, desc]
        rep[day] = lst
        file.close()
        
    except FileNotFoundError:
        rep = {}
        file = open(filename, 'w')
        lst = []
        w = str(water) + ' litres'
        lst = [w, desc]
        rep[day] = lst
        file.close()
    
    filea = open(filename, 'w')
    json.dump(rep, filea)
    filea.close()
    
    
def go(text):
    s = str(text) + " lol"
    
    
def out():
    
    rep = json.load(open(filename))
    
    for i in range(100):
        for k, v in rep.items():
            if i == int(k):
                print("day " + str(i) + ": ")
                print(rep.get(str(k)))


@bot.message_handler(commands=['start'])
def handle_start(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('/start')
        bot.send_message(message.from_user.id, "Давай начнём.\nПришли данные в формате: день, вода, описание.", reply_markup=user_markup)
        
        
@bot.message_handler(content_types=['text'])
def handle_text(message):
        try:
                go(message.text)
                
                bot.send_message(message.chat.id, "Данные добавлены.")   
            
        except:
                bot.send_message(message.chat.id, "Ошибка...")
             
        
bot.polling(none_stop=True, interval=0)    
