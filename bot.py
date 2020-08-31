import telebot
import json


bot = telebot.TeleBot("1346425132:AAHZfTwGvYBBDoJpRaFNMzqnXmNSuWxH6hg")
filename = "nums.json"


@bot.message_handler(commands=['start'])
def handle_start(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('/start')
        bot.send_message(message.from_user.id, "Давай начнём.\nПришли данные в формате: день, вода, описание.", reply_markup=user_markup)
        
        
@bot.message_handler(content_types=['text'])
def handle_text(message):
        try:
            
            file = open(filename) 
            rep = json.load(file)
            lst = []
            w = str(water) + ' litres'
            lst = [w, desc]
            rep[day] = lst
            file.close()
            
            bot.send_message(message.chat.id, "Данные добавлены.")   
            
        except:
            
            rep = {}
            file = open(filename, 'w')
            lst = []
            w = str(water) + ' litres'
            lst = [w, desc]
            rep[day] = lst
            file.close()
            
            bot.send_message(message.chat.id, "Данные добавлены.")
             
        
bot.polling(none_stop=True, interval=0)    
