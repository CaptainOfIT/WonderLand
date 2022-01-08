
import telebot
from BOT.config import TOKEN, keys
from extensions import ExchangeMoney, ExchangeException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
    text = 'Хей хо! Рад видеть тебя у меня в чате! Если ты хочешь узнать, сколько нынче стоят деньги, то введи, пожалуйста, команду в следующем формате:\n<название валюты>\
    <в какую валюту перевести>\
    <количество переводимой валюты> \nЧтобы узнать каким количеством валют я владею, достаточно ввести команду: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ExchangeException('Слишком много параметров.')

        quote, base, amount = values
        total_base = ExchangeMoney.get_price(quote, base, amount)
    except ExchangeException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()
