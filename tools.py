from datetime import datetime
from telebot import types
import json

def save_json(user):
    with open('user_data/' + str(user.id) + '.json', 'w+') as f:
        json.dump(user.__dict__, f, indent = 4)

def load_json(user_id):
    with open('user_data/' + str(user_id) + '.json', 'r') as f:
        return json.load(f)

def yes_no_buttons():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
    markup.add('Yes', 'No')
    return markup

def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            m_details = (datetime.now().strftime('%Y.%m.%d %H:%M:%S ') 
                          + str(m.chat.first_name) 
                          + " [" + str(m.from_user.id) + "]: " 
                          + m.text)
            with open('messages.txt', 'a+') as f:
                f.write(m_details + '\n')
            print(m_details)