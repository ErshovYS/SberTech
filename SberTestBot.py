# -*- coding: utf-8 -*-
'''
Создать телеграм-бота - гида по Википедии По запросу пользователя бот возвращает:
1) выдержку из максимально релевантной статьи из Википедии
2) ссылку на эту статью
3) кнопки, на которых написаны названия топ-3 рекомендуемых к последующему прочтению статей. По нажатию на кнопку бот обновляет текущее сообщение новой статьёй и новыми кнопками
'''

import telebot

from wikifinder import WikiFinder


bot = telebot.TeleBot("536182287:AAFOc8-IFuqknT4Tby5e6jDioMivIi0NnOI")
finder = WikiFinder()

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет! Я wiki_bot!')

@bot.message_handler(commands=['get'])
def get(message):
    bot.send_message(message.chat.id, 'What you want?')
    #get_answer

@bot.message_handler(content_telebot.types=['text'])
def get_answer(message):
    answer = finder.search(message.text)
    keyboard = telebot.types.InlineKeyboardMarkup()
    i = 0
    while i < len(finder.links):
        callback_button = telebot.types.InlineKeyboardButton(text=finder.links[i], callback_data="link")
        keyboard.add(callback_button)
        i+=1
    bot.send_message(message.chat.id, answer, reply_markup=keyboard)
    return False

# Можно разбить этот хэндлер на несколько маленьких
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "link":
            answer = finder.search(call.message.text)
            keyboard = telebot.types.InlineKeyboardMarkup()
            i = 0
            while i < len(finder.links):
                callback_button = telebot.types.InlineKeyboardButton(text=finder.links[i], callback_data="link")
                keyboard.add(callback_button)
                i+=1
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=answer, reply_markup=keyboard)
    # Если сообщение из инлайн-режима
    elif call.inline_message_id:
        if call.data == "link":
            answer = finder.search(call.message.text)
            keyboard = telebot.types.InlineKeyboardMarkup()
            i = 0
            while i < len(finder.links):
                callback_button = telebot.types.InlineKeyboardButton(text=finder.links[i], callback_data="link")
                keyboard.add(callback_button)
                i+=1
            bot.edit_message_text(inline_message_id=call.inline_message_id, text=answer, reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)