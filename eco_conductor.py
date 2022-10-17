# -*- coding: utf-8 -*-
import telebot
from telebot import types


# ПОДКЛЮЧЕНИЕ API БОТА
bot = telebot.TeleBot('5486407898:AAG9XIOW2gFgEZv5tKayQW9s2-6dNiVAg1Q')

#5486407898:AAG9XIOW2gFgEZv5tKayQW9s2-6dNiVAg1Q

pount = 235

sbtn1 = types.KeyboardButton('СПРАВКА')
sbtn2 = types.KeyboardButton('МОИ БАЛЛЫ')
sbtn3 = types.KeyboardButton('МЕСТОПОЛОЖЕНИЕ ПУНКТОВ УТИЛИЗАЦИИ')


# ФУНКЦИЯ ДЛЯ СТАРТА ОБЩЕНИЯ
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('СПРАВКА')
    btn2 = types.KeyboardButton('МОИ БАЛЛЫ')
    btn3 = types.KeyboardButton('МЕСТОПОЛОЖЕНИЕ ПУНКТОВ УТИЛИЗАЦИИ')
    markup.add(btn1, btn2, btn3)

#---------------------------------------------------------------------------------------
    # ПРИВЕТСТВИЕ ПОЛЬЗОВАТЕЛЯ
    send_mess = f"<b> Приветсвую вас, {message.from_user.first_name}</b>! 👋🏻\n\n<b>Я Бот Эко-Проводник</b>. Покажу и расскажу вам все, что знаю про утилизацию\n\nВы можете прислать мне название предмета помощь в утилизации которого вам требуется или воспользоваться кнопкой «СПРАВКА» для просмотра полной справки по утилизации\n\nНажав на кнопку «МОИ БАЛЛЫ» вы можете узнать колличество накопленных баллов \n\nКнопка МЕСТОПОЛОЖЕНИЕ ПУНКТОВ УТИЛИЗАЦИИ покажет вам ближайшие пункты \n\n☑️<b>По всем вопросам связанным с работой бота обращаться к главному администратору - @rfdtcg</b>"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

#----------------------------------------------------------------------------------------
@bot.message_handler(content_types=['sticker'])
def stick(message):
    send_mess = 'Прости я не понимаю стикеры('
    bot.send_message(message.chat.id, send_mess)

#----------------------------------------------------------------------------------------
@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()



    if get_message_bot == 'справка':
    	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    	sbtn1
    	sbtn3
    	sbtn3
    	markup.add(sbtn1, sbtn2, sbtn3)
    	send_mess = f'1. Сбор и сортировка. Существенно облегчает задачу службам, занимающимся транспортировкой отходов установка специальных контейнеров, предназначенных для разных типов мусора. Но при этом важно чтобы каждый вид мусора в итоге собирала отдельная машина, в противном случае в контейнере отходы перемешаются.\n2. Перевозка.\n3. Размещение на специально подготовленных полигонах.\n4. Обезвреживание, в том случае если отходы представляют опасность для окружающей среды и здоровья людей.\n5. Захоронение.\n6. Хранение. Мусор перевозится на специально предназначенные участки земли (полигоны), где и хранится некоторое время. Чем быстрее будут проводиться работы по утилизации – тем меньшая площадь потребуется для хранения, а также существенно сократится негативное влияние, оказываемое на окружающую среду.\n7. Вторичная переработка.\n8. Утилизация.'
    	bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup, disable_web_page_preview=True)



    elif get_message_bot == 'мои баллы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('КУДА ПОТРАТИТЬ БАЛЛЫ ?')
        markup.add(btn1)
        send_mess = f"{message.from_user.first_name}, вы накопили " + str(pount) + " баллов "
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup,disable_web_page_preview = True)


    elif get_message_bot == 'куда потратить баллы ?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        sbtn1
        sbtn3
        sbtn3
        markup.add(sbtn1, sbtn2, sbtn3)
        send_mess = f"Простите сейчас нет доступных акций 😪"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup,disable_web_page_preview = True)


    elif get_message_bot == 'местоположение пунктов утилизации':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        sbtn1
        sbtn3
        sbtn3
        markup.add(sbtn1, sbtn2, sbtn3)
        send_mess = f"1. https://yandex.ru/maps/-/CCUZyLFA3B\n\n2. https://yandex.ru/maps/-/CCUZyLFigB \n\n3. https://yandex.ru/maps/-/CCUZyLFygD \n\n4. https://yandex.ru/maps/-/CCUZyLFFDB \n\n5. https://yandex.ru/maps/-/CCUZyLF6gD"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup,disable_web_page_preview = True)


    elif get_message_bot == 'батарейка' or  'батарейки':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        send_mess = f"Как правильно утилизировать батарейки:\n\n1. Отправить требующие утилизации элементы в пункт приема с соседом или знакомым, который едет в ближайший крупный город.\n2. Отправляясь по делам в крупный город, прихватить батарейки с собой и заехать в пункт их приема.\n3. Организовать в своем населенном пункте точку приема батареек и после накопления достаточного количества, или по мере возможности отвозить их в город на утилизацию.\n4. Договориться с местным отделением МЧС, которое имеет все лицензии и сертификаты о регулярных выездах или просто приеме этих отходов.\n5. Договориться с представителями предприятия, занимающегося утилизацией батареек о выезде их представителя."
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup,disable_web_page_preview = True)

    else:
    	send_mess = f"Нажимай на кнопки!"
    	bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup,disable_web_page_preview = True)











    # БОТ АКТИВЕН ВСЕГДА
bot.polling(none_stop=True)