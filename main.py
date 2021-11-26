import telebot
from telebot import types
import sqlite3
from sqlite3 import Error
from time import sleep, ctime
import random
from random import randint

# тут токен бота
bot = telebot.TeleBot("2129257343:AAHtUDqslOo54RJWSPMjDOk-sBgM9BXHkgc")

# переменные с данными
supportid = "AngelinaAvdeeva"
tokenqiwi = ""
numberqiwi = ""
admin = 2146218025
password = "3331"

list1 = ["Название: 😼 Мини 99₽ Скидка 32%🔥", "Название: 👧🏼 Юные создания 10-16 💧 ЦЕНА: 199₽", "Название: ❤️ lllкоLьные Секс 12-16 😜 ЦЕНА: 277₽ [-70%]",
					"Название: 👨‍👩‍👧‍👦 ИNСЕSТЫ 👨‍👩‍👧‍👦 ЦЕНА: 339₽ [-50%]", "Название: 👧🏻 Мега Приват 👧🏻 ЦЕНА: 345₽", "Название: 🍌САМАЯ Жесть🍌+🧨Apxивчик🧨 ЦЕНА: 415₽",
					"Название: 🤑Все включено🤑 ЦЕНА: 520₽ [-35%]", "Название: 🥵 UZНОСЫ 🥵 ЦЕНА: 435₽ [-75%]", "Название: 🔞 FULL BIG PACK 🍭 ЦЕНА: 1000₽", "Название: ✅ PORNHUB PREMIUM ACCOUNT ✅ ЦЕНА: 49₽"]


# создание и подключение к бд
def post_sql_query(sql_query):
	with sqlite3.connect('my.db') as connection:
		cursor = connection.cursor()
		try:
			cursor.execute(sql_query)
		except Error:
			pass
		result = cursor.fetchall()
		return result


def create_tables():
	users_query = '''CREATE TABLE IF NOT EXISTS USERS 
                        (user_id INTEGER PRIMARY KEY NOT NULL,
                        username TEXT,
                        first_name TEXT,
                        last_name TEXT,
                        reg_date TEXT);'''
	post_sql_query(users_query)

def register_user(user, username, first_name, last_name):
	user_check_query = f'SELECT * FROM USERS WHERE user_id = {user};'
	user_check_data = post_sql_query(user_check_query)
	if not user_check_data:
		insert_to_db_query = f'INSERT INTO USERS (user_id, username, first_name,  last_name, reg_date) VALUES ({user}, "{username}", "{first_name}", "{last_name}", "{ctime()}");'
		post_sql_query(insert_to_db_query )
create_tables()

@bot.message_handler(commands=['start'])
def start_message(message):
	markup_reply = telebot.types.InlineKeyboardMarkup()
	markup_reply.add(telebot.types.InlineKeyboardButton(text='😼 Мини 99₽ Скидка 32% 🔥 ЦЕНА: 99₽', callback_data=1))
	markup_reply.add(telebot.types.InlineKeyboardButton(text='👧🏼 Юные создания 10-16 💧 ЦЕНА: 199₽', callback_data=2))
	markup_reply.add(telebot.types.InlineKeyboardButton(text='❤️ lllкоLьные Секс 12-16 😜 ЦЕНА: 277₽ [-70%]', callback_data=3))
	markup_reply.add(telebot.types.InlineKeyboardButton(text='👨‍👩‍👧‍👦 ИNСЕSТЫ 👨‍👩‍👧‍👦 ЦЕНА: 339₽ [-50%]', callback_data=4))
	markup_reply.add(telebot.types.InlineKeyboardButton(text='👧🏻 Мега Приват 👧🏻 ЦЕНА: 345₽', callback_data=5))
	markup_reply.add(telebot.types.InlineKeyboardButton(text='🍌САМАЯ Жесть🍌+🧨Apxивчик🧨 ЦЕНА: 415₽', callback_data=6))
	markup_reply.add(telebot.types.InlineKeyboardButton(text='🤑Все включено🤑 ЦЕНА: 520₽ [-35%]', callback_data=7))
	markup_reply.add(telebot.types.InlineKeyboardButton(text='🥵 UZНОСЫ 🥵 ЦЕНА: 435₽ [-75%]', callback_data=8))
	markup_reply.add(telebot.types.InlineKeyboardButton(text='🔞 FULL BIG PACK 🍭 ЦЕНА: 1000₽', callback_data=9))
	markup_reply.add(telebot.types.InlineKeyboardButton(text='✅ PORNHUB PREMIUM ACCOUNT ✅ ЦЕНА: 49₽', callback_data=10))


	register_user(message.from_user.id, message.from_user.username,
	              message.from_user.first_name, message.from_user.last_name)
	familiya = message.from_user.last_name

	if familiya is not None:
		bot.send_message(message.chat.id, f'<b>Ваш профиль:</b> \n\n<b>Ваш ID:</b> {message.from_user.id}\n'
											f'<b>Ваш Username:</b> {message.from_user.username}\n'
											f'<b>Ваше имя:</b> {message.from_user.first_name}\n'
											f'<b>Ваша фамилия:</b> {familiya}\n'
											f'<b>Дата регистрации:</b> {ctime()}\n\n'
											'🔥 <b>Привет! Через этого бота можно приобрести доступ к npивaткaм с зanpeтными видocaми</b> \n'
											'📌<i>У нас количество материала в описании полностью совпадает с действительностью, без выдуманных цифр, всё честно и по факту</i> 💕\n'
											'✅ Один из наших паков в качестве доказательства - https://ibb.co/64Yg2Qv\n'									
											'👇🏻ℹ️ <i>Жми на интересующий тебя товар для получения более подробной информации</i>\n', parse_mode='html', reply_markup=markup_reply)

	elif familiya is None:
		bot.send_message(message.chat.id, f'<b>Ваш профиль:</b> \n\n<b>Ваш ID:</b> {message.from_user.id}\n'
											f'<b>Ваш Username:</b> {message.from_user.username}\n'
											f'<b>Ваше имя:</b> {message.from_user.first_name}\n'
											f'<b>Ваша фамилия:</b> не указана\n'
											f'<b>Дата регистрации:</b> {ctime()}\n\n'
											'🔥 <b>Привет! Через этого бота можно приобрести доступ к npивaткaм с зanpeтными видocaми</b> \n'
											'📌<i>У нас количество материала в описании полностью совпадает с действительностью, без выдуманных цифр, всё честно и по факту</i> 💕\n'
											'✅ Один из наших паков в качестве доказательства - https://ibb.co/64Yg2Qv\n', parse_mode='html', reply_markup=markup_reply)



# обработка callback клавиатуры
@bot.callback_query_handler(func=lambda message: True)
def KeyboardInline(call):
	register_user(call.message.from_user.id, call.message.from_user.username,
	              call.message.from_user.first_name, call.message.from_user.last_name)
	if call.data == '1':
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='❤️‍🔥 Купить', callback_data='buy'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"{list1[0]}\n💰 Цена: 99₽\n\n💭 Описание: 💟Считается пробной мини версией наших приваток💟", reply_markup = markup_reply)

	elif call.data == '2':
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='❤️‍🔥 Купить', callback_data='buy'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"{list1[1]}\n💰 Цена: 199₽\n\n💭 Описание: 💟💫Здесь находится уже больше контента, чем в мини💫💟", reply_markup = markup_reply)

	elif call.data == '3':
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='❤️‍🔥 Купить', callback_data='buy'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"{list1[2]}\n💰 Цена: 277₽\n\n💭 Описание: 💟Много фоток и видео прямо из школы, более 3000 видео хорошего качества💟", reply_markup = markup_reply)

	elif call.data == '4':
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='❤️‍🔥 Купить', callback_data='buy'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"{list1[3]}\n💰 Цена: 339₽\n\n💭 Описание: 💟Вы получите доступ к диску, одержание которого более 20.000 видео 👩🧑, паки в облаках. Пополнение почти ежедневно новым контентом.💟", reply_markup = markup_reply)

	elif call.data == '5':
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='❤️‍🔥 Купить', callback_data='buy'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"{list1[4]}\n💰 Цена: 345₽\n\n💭 Описание: 💟Вы получите доступ к контенту. Содержание: более 5000 запрещённых видео и фото со школьницами. Пополнение почти ежедневно новым контентом.💟", reply_markup = markup_reply)

	elif call.data == '6':
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='❤️‍🔥 Купить', callback_data='buy'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"{list1[5]}\n💰 Цена: 415₽\n\n💭 Описание: 💟Более 3100 видео лучшего качества, а также более 2000 различных фотографий💟\nЕсть много ссылок, переписок, что в этом канале только нет\nBoзраст: 14-16", reply_markup = markup_reply)

	elif call.data == '7':
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='❤️‍🔥 Купить', callback_data='buy'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"{list1[6]}\n💰 Цена: 520₽\n\n💭 Описание: 💟СЮДА ВХОДЯТ АБСОЛЮТНО ВЕСЬ КОНТЕНТ БОЛЕЕ 33.000 ВИДЕО! ВСЕ КРОМЕ БИГПАКА💟", reply_markup = markup_reply)

	elif call.data == '8':
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='❤️‍🔥 Купить', callback_data='buy'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"{list1[7]}\n💰 Цена: 435₽\n\n💭 Описание: 💟Закрытый канал для клиентов\nРезервные группы на случай блокировки\nНеобходимые инструкции, промоакции и тд\nИзносы (против воли)💟", reply_markup = markup_reply)

	elif call.data == '9':
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='❤️‍🔥 Купить', callback_data='buy'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"{list1[8]}\n💰 Цена: 1000₽\n\n💭 Описание: 💟ЭТО САМЫЙ КРУТОЙ ПРИВАТ\n-Шкодные впиsки🎒🍷 [2052 VIDEO] (канал)\n-Самое сокровенное 🍼👶 [4402 VIDEO] (канал)\n"
			"👩🏻NЗНОSЫ🩸 Wkoдnиц 🔪 [4035 VIDEO] \n -Nnцесты👨‍👩‍👧‍👦 (канал)\n-Юnые девочки👩🏽🍪 (канал) \n\n И МНОГО МНОГО ВСЕГО ДРУГОГО.", reply_markup = markup_reply)

	elif call.data == '10':
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='❤️‍🔥 Купить', callback_data='buy'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"{list1[9]}\n💰 Цена: 49₽\n\n💭 Описание: Вам выдаётся примиум аккаунт PornHub с различными подписками, самый дешёвый, но не менее качественный товар!", reply_markup = markup_reply)


	elif call.data == 'back':
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='😼 Мини 99₽ Скидка 32% 🔥 ЦЕНА: 99₽', callback_data=1))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='👧🏼 Юные создания 10-16 💧 ЦЕНА: 199₽', callback_data=2))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='❤️ lllкоLьные Секс 12-16 😜 ЦЕНА: 277₽ [-70%]', callback_data=3))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='👨‍👩‍👧‍👦 ИNСЕSТЫ 👨‍👩‍👧‍👦 ЦЕНА: 339₽ [-50%]', callback_data=4))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='👧🏻 Мега Приват 👧🏻 ЦЕНА: 345₽', callback_data=5))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🍌САМАЯ Жесть🍌+🧨Apxивчик🧨 ЦЕНА: 415₽', callback_data=6))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🤑Все включено🤑 ЦЕНА: 520₽ [-35%]', callback_data=7))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🥵 UZНОСЫ 🥵 ЦЕНА: 435₽ [-75%]', callback_data=8))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔞 FULL BIG PACK 🍭 ЦЕНА: 1000₽', callback_data=9))
		bot.send_message(call.message.chat.id, "❕ <b>Вы вернулись в меню</b>",parse_mode='html', reply_markup=markup_reply)

	elif call.data == 'buy':
		comment = random.randint(5000, 9999)
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='✅ Я оплатил', callback_data='imbuy'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))

		bot.send_message(call.message.chat.id, f"<b>👇 Для того, что бы купить товар, переведите точную сумму на QIWI кошелёк или КАРТУ.</b>\n❗️ <b>При переводе на QIWI кошелёк укажите комментарий (БЕЗ НЕГО ПЛАТЁЖ АНУЛИРУЕТСЯ)</b>\n\n🥝 <b>QIWI кошелёк:</b> +79672449984\n💭 <b>Комментарий к QIWI:</b> {comment}\n<b>💳 Номер карты:</b> 4890 4947 3261 6792\n\n❕ <i>После успешной оплаты, нажмите на кнопку 'Я оплатил'</i>", reply_markup=markup_reply, parse_mode='html')

	elif call.data == 'imbuy':
		bot.send_message(call.message.chat.id, "Платёж не был найден, попробуйте ещё раз через 30 секунд.\nЕсли появилась проблема с платежём, отпишите нашему оператору: ❕ @operatorqqq")


@bot.message_handler(commands=['admin'])
def adminka(message):
	if message.chat.id == admin:
		bot.send_message(message.chat.id, "Введите пароль от админки: ")

	@bot.message_handler(content_types=['text'])
	def getpassword(message):
		getpassword = message.text
		if getpassword == password:
			markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
			stats = types.KeyboardButton("📈 Колличество пользователей")
			rass = types.KeyboardButton("📢 Рассылка сообщений")
			markup_reply.add(stats, rass)
			bot.send_message(message.chat.id, "🤙 Вы в Админке! Воспользуйтесь кнопками ниже.", reply_markup = markup_reply)

		elif message.text == "📈 Колличество пользователей":
			connection = sqlite3.connect("my.db")
			cursor = connection.cursor()
			cursor.execute("SELECT COUNT(user_id) from USERS	")
			stata_users_ids_message = str(cursor.fetchone()[0])
			bot.send_message(message.chat.id, '📈 Пользователей бота: ' + stata_users_ids_message)
			cursor.close()
			connection.close()


	





bot.polling(none_stop=True)
