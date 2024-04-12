import telebot

API_TOKEN = '7058753529:AAHEKGkWEwclTCOM6W8VG-AunOU-fu1QzpI'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am ArmanBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

# Handle '/joke'
@bot.message_handler(commands=['joke'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am ArmanBot.
В Англии не играют в шахматы потомучто у них нет королевы!\
""")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text) 

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, """
I am sorry, but i don't understand your command
""")

@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)

bot.infinity_polling()