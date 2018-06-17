#! /usr/bin/env python
# -*- coding: utf-8 -*-

# unread, sort, id_more_than, id_less_than, page, per, search, updated
# @bot.message_handler(func = lambda message: message.text='All notifications')
# .encode(sys.stdout.encoding, errors='replace')

import threading
import vk_requests
import json
import time
import os
import telebot
from telebot import types
from telebot.types import LabeledPrice
from telebot.types import ShippingOption
from datetime import datetime

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


BOT_TOKEN 	= '545147843:AAFioHVAd_h9yPuluw0ENyg5h4iNHND5Yow'
PROVIDER_TOKEN 	= '401643678:TEST:f24cab82-f18b-4ccd-b6d5-23bf8eb9a3b9'
bot 	= telebot.AsyncTeleBot(BOT_TOKEN)


APP_ID 		= 5441642
LOGIN 		= 'jack.in.the.box.jitbone@gmail.com'
PASSWORD 	= '6RY20ML49EU142305+'
SCOPE 		= ['market', 'video']
GROUP_ID 	= 125530231
api 	= None#vk_requests.create_api(app_id = APP_ID, login = LOGIN, password = PASSWORD, scope = SCOPE)

users = {0: {'age': 1337, 'stage': 1337}}
NONE = 1337
# age
ADULT = 1
KID = 0
# stage
NAME = 1001
REVIEW = 1002
QUESTION = 2001

# GENERAL
items = None
settings = None
text_reviews = None
video_reviews = None
questions_kids = None
questions_adult = None

# Payment data
prices = [LabeledPrice(label='Курсы по основам Java', amount=25000), LabeledPrice('Курсы по основам Java', 23000)]
shipping_options = [
	ShippingOption(id='deep', title='Углублённое изучение C++(продолжение)').add_price(LabeledPrice('C++, продолжение', 12000)),
	ShippingOption(id='litedeep', title='Допонительные занятия по Java(продолжение)').add_price(LabeledPrice('Java, продолжение', 7000))
]

def SetBotActiveStatus():
	try:
		f = open("database/stats.txt", "r")
		tmp = f.read()
		tmp = int(tmp)
		tmp += 1
		f.close
		f = open("database/stats.txt", "w")
		f.write(str(tmp))
		f.close()
	except:
		pass

def LoadData():
	global items
	items = json.load(open('database/items.json', 'r'))['items']
	global settings
	settings = json.load(open('database/settings/settings.json', 'r'))['settings']
	global text_reviews
	text_reviews = json.load(open('database/text_reviews.json', 'r'))
	global video_reviews
	video_reviews = json.load(open('database/video_reviews.json', 'r'))
	global questions_kids
	questions_kids = json.load(open('database/faq/kids.json', 'r'))
	global questions_adult
	questions_adult = json.load(open('database/faq/adult.json', 'r'))

def Update():
	global update_time
	threading.Timer(update_time, Update).start ()
	print("Updaing information from VK...")
	items = api.market.get(owner_id = -GROUP_ID)
	with open('database/items.json', 'w') as outfile:
		json.dump(items, outfile)

	text_reviews = api.board.getComments(group_id = GROUP_ID, topic_id = 34109617)
	with open('database/text_reviews.json', 'w') as outfile:
		json.dump(reviews, outfile)

	video_reviews = api.video.get(owner_id = -GROUP_ID, album_id = 1, count = 200, offset = 0)
	with open('database/video_reviews.json', 'w') as outfile:
		json.dump(video_reviews, outfile)

	# questions_kids = api.board.getComments(group_id = GROUP_ID, topic_id = 34101067)
	# with open('database/questions_kids.json', 'w') as outfile:
	# 	json.dump(questions_kids, outfile)

	# questions_adult = api.board.getComments(group_id = GROUP_ID, topic_id = 34140029) 
	# with open('database/questions_adult.json', 'w') as outfile:
	# 	json.dump(questions_adult, outfile)

	# docs.get – Возвращает информацию о документах текущего пользователя или группы.
	# ['items'][12]['title']
	# ['items'][12]['url']

def UsersGetFix(chat_id, stage):
	result = False
	try:
		result = (users.get(chat_id).get('stage') == (stage))
	except:
		print str(chat_id), str(stage)
	return result









# START
@bot.message_handler(commands=['start'])
def start_command(message):
	SetBotActiveStatus()
	users[message.chat.id] = {'age': NONE, 'stage': NONE}
	reply = types.ReplyKeyboardMarkup()
	reply.row('Курсы для взрослых', 'Курсы для детей')
	bot.send_message(message.chat.id, 'Здравствуйте! Вас привествует IT-Академия (г. Казань)\nВыберите нужную вам возрастную категорию?', reply_markup = reply)

@bot.message_handler(func = lambda message: message.text == 'Курсы для взрослых'	and UsersGetFix(message.chat.id, NONE))
def adults(message):
	SetBotActiveStatus()
	users[message.chat.id] = {'age': ADULT, 'stage': NONE}
	reply = types.ReplyKeyboardMarkup()
	reply.row('Краткий экскурс')
	reply.row('Я уже обучаюсь', 'Я хочу узнать больше')
	bot.send_message(message.chat.id, 'Хотите узнать подробнее о наших услугах или вы уже являетесь обучяющимся?', reply_markup = reply)

@bot.message_handler(func = lambda message: message.text == 'Курсы для детей'		and UsersGetFix(message.chat.id, NONE)) 
def kids(message):
	SetBotActiveStatus()
	users[message.chat.id] = {'age': KID, 'stage': NONE}
	reply = types.ReplyKeyboardMarkup()
	reply.row('Краткий экскурс')
	reply.row('Я уже обучаюсь', 'Я хочу узнать больше')
	bot.send_message(message.chat.id, 'Хотите узнать подробнее о наших услугах или вы уже являетесь обучяющимся?', reply_markup = reply)











@bot.message_handler(func = lambda message: message.text == 'Краткий экскурс' 		and UsersGetFix(message.chat.id, NONE))
def demo(message):
	SetBotActiveStatus()
	if users.get(message.chat.id).get('age') == ADULT:
		for i in range(14):
			photo = open('database/demo/adult/' + str(i) + '.png', 'rb')
			bot.send_photo(message.chat.id, photo)
			time.sleep(1.3)
		global questions_adult
		text = 'Часто зазаваемые вопросы:\r\n'
		for i in range(len(questions_adult['adult'])):
			text += (questions_adult['adult'][i][0]+ '\n -> ' + questions_adult['adult'][i][1] + '\r\n')
		bot.send_message(message.chat.id, text)
	elif users.get(message.chat.id).get('age') == KID:
		for i in range(8):
			photo = open('database/demo/kids/' + str(i) + '.png', 'rb')
			bot.send_photo(message.chat.id, photo)
			time.sleep(1.3)
		global questions_kids
		text = 'Часто зазаваемые вопросы:\r\n'
		for i in range(len(questions_kids['kids'])):
			text += (questions_kids['kids'][i][0]+ '\n -> ' + questions_kids['kids'][i][1] + '\r\n')
		bot.send_message(message.chat.id, text)
	bot.send_location(message.chat.id, "55.780578", "49.133391")

@bot.message_handler(func = lambda message: message.text == 'Я обучаюсь'			and UsersGetFix(message.chat.id, NONE))
def stedent(message):
	SetBotActiveStatus()
	reply = types.ReplyKeyboardMarkup()
	reply.row('Расписание', 'Новости')
	bot.send_message(message.chat.id, 'IT-Академия к вашим услугам\nКакая инормация вас интересует?', reply_markup = reply)

@bot.message_handler(func = lambda message: message.text == 'Я хочу узнать больше'	and UsersGetFix(message.chat.id, NONE))
def not_student(message):
	SetBotActiveStatus()
	reply = types.ReplyKeyboardMarkup()
	reply.row('Курсы', 'Отзывы')
	reply.row('Часто задаваемые вопросы')
	reply.row('Задать свой вопрос', 'Позвоните мне')
	bot.send_message(message.chat.id, 'IT-Академия к вашим услугам\nКакая инормация вас интересует?', reply_markup = reply)











@bot.message_handler(func = lambda message: message.text == 'Расписание' 			and UsersGetFix(message.chat.id, NONE))
def get_reviews(message):
	SetBotActiveStatus()
	if users.get(message.chat.id).get('age') == ADULT:	
		photo = open('database/docs/adult.jpg', 'rb')
		bot.send_photo(message.chat.id, photo)
	elif users.get(message.chat.id).get('age') == KID:
		photo = open('database/docs/kids.jpg', 'rb')
		bot.send_photo(message.chat.id, photo)










# MAIN
@bot.message_handler(func = lambda message: message.text == 'Курсы'					and UsersGetFix(message.chat.id, NONE))
def get_items(message):
	SetBotActiveStatus()
	global items
	if users.get(message.chat.id).get('age') == ADULT:	
		inline = types.InlineKeyboardMarkup()
		for i, item in enumerate(items):
			button = types.InlineKeyboardButton(text = item['title'], callback_data = 'items_get_' + str(i))
			inline.add(button)
		bot.send_message(message.chat.id, 'Доступные курсы:', reply_markup = inline)
	elif users.get(message.chat.id).get('age') == KID:
		inline = types.InlineKeyboardMarkup()
		for i, item in enumerate(items):
			button = types.InlineKeyboardButton(text = item['title'], callback_data = 'items_get_' + str(i))
			inline.add(button)
		bot.send_message(message.chat.id, 'Доступные курсы:', reply_markup = inline)








@bot.message_handler(func = lambda message: message.text == 'Отзывы' 				and UsersGetFix(message.chat.id, NONE))
def get_reviews(message):
	SetBotActiveStatus()
	reply = types.ReplyKeyboardMarkup()
	reply.row('Видео-отзывы', 'Текстовые отзывы')
	reply.row('Оставить отзыв')
	reply.row('Назад')
	bot.send_message(message.chat.id, 'Какие отзывы вы желаете увидеть?', reply_markup = reply)

@bot.message_handler(func = lambda message: message.text == 'Текстовые отзывы'		and UsersGetFix(message.chat.id, NONE))
def get_text_reviews(message):
	SetBotActiveStatus()
	file = open('database/reviews/confirmed/index.txt', 'r')
	count = int(file.read())
	file.close()
	inline = types.InlineKeyboardMarkup() 
	next_button = types.InlineKeyboardButton(text = 'Следующий', callback_data = 'reviews_text_2')
	prev_button = types.InlineKeyboardButton(text = 'Предыдущий', callback_data = 'reviews_text_' + str(count))
	inline.add(prev_button, next_button)
	file = open('database/reviews/confirmed/1.txt', 'r')
	string = file.read()
	bot.send_message(message.chat.id, text = string, reply_markup = inline)

@bot.message_handler(func = lambda message: message.text == 'Видео-отзывы'			and UsersGetFix(message.chat.id, NONE))
def get_video_reviews(message):
	SetBotActiveStatus()
	global video_reviews
	reviews = video_reviews['items']
	count = video_reviews['count']
	inline = types.InlineKeyboardMarkup()
	next_button = types.InlineKeyboardButton(text = 'Следующий', callback_data = 'reviews_video_1')
	prev_button = types.InlineKeyboardButton(text = 'Предыдущий', callback_data = 'reviews_video_' + str(count - 1))
	inline.add(prev_button, next_button)
	bot.send_message(message.chat.id, text = 'https://vk.com/video-' + str(GROUP_ID) + '_' + str(reviews[0]['id']), reply_markup = inline)

# ADD REVIEW DIALOG
def AddNewReview(name, review):
	file = open('database/reviews/unconfirmed/index.txt', 'r')
	index = int(file.read())
	index += 1
	file.close()
	file = open('database/reviews/unconfirmed/index.txt', 'w')
	file.write(str(index))
	file.close()
	file = open('database/reviews/unconfirmed/' + str(index) + '.txt', 'w')
	review = review.encode("UTF-8")
	name = name.encode("UTF-8")
	file.write(review + '\r\n' + name + ', ' + str(datetime.now()))
	file.close()

@bot.message_handler(func = lambda message: message.text == 'Оставить отзыв'		and UsersGetFix(message.chat.id, NONE))
def add_review(message):
	SetBotActiveStatus()
	bot.send_message(message.chat.id, 'Как вас зовут?')
	users[message.chat.id]['stage'] = NAME

name = ' '
@bot.message_handler(func = lambda message: message.text != None					and UsersGetFix(message.chat.id, NAME))
def add_review_name(message):
	SetBotActiveStatus()
	global name 
	name = message.text
	bot.send_message(message.chat.id, 'Напишите отзыв')
	users[message.chat.id]['stage'] = REVIEW

@bot.message_handler(func = lambda message: message.text != None					and UsersGetFix(message.chat.id, REVIEW))
def add_review_review(message):
	SetBotActiveStatus()
	review = message.text
	bot.send_message(message.chat.id, 'Спасибо за ваш отзыв!')
	users[message.chat.id]['stage'] = NONE
	AddNewReview(name, review)
# ADD REVIEW DIALOG

@bot.message_handler(func = lambda message: message.text == 'Назад'					and UsersGetFix(message.chat.id, NONE))
def back(message):
	SetBotActiveStatus()
	reply = types.ReplyKeyboardMarkup()
	reply.row('Курсы', 'Отзывы')
	reply.row('Часто задаваемые вопросы')
	reply.row('Задать свой вопрос')
	bot.send_message(message.chat.id, 'Какая инормация вас интересует?', reply_markup = reply)







@bot.message_handler(func = lambda message: message.text == 'Часто задаваемые вопросы'				and UsersGetFix(message.chat.id, NONE))
def get_questions(message):
	SetBotActiveStatus()
	if users.get(message.chat.id).get('age') == ADULT:
		global questions_adult
		text = 'Часто зазаваемые вопросы:\r\n'
		for i in range(len(questions_adult['adult'])):
			text += (questions_adult['adult'][i][0]+ '\n -> ' + questions_adult['adult'][i][1] + '\r\n')
		bot.send_message(message.chat.id, text)
	elif users.get(message.chat.id).get('age') == KID:
		global questions_kids
		text = 'Часто зазаваемые вопросы:\r\n'
		for i in range(len(questions_kids['kids'])):
			text += (questions_kids['kids'][i][0]+ '\n -> ' + questions_kids['kids'][i][1] + '\r\n')
		bot.send_message(message.chat.id, text)

@bot.message_handler(func = lambda message: message.text == 'Задать свой вопрос'  and UsersGetFix(message.chat.id, NONE))
def ask(message):
	SetBotActiveStatus()
	bot.send_message(message.chat.id, 'Напишите ваш вопрос: (Помните, в 99% случаев на ваш вопрос уже ответили в "Часто задаваемые вопросы"')
	users[message.chat.id]['stage'] = QUESTION

@bot.message_handler(func = lambda message: message.text != None          and UsersGetFix(message.chat.id, QUESTION))
def question(message):
	SetBotActiveStatus()
	question = message.text
	bot.send_message(message.chat.id, 'Наши менеджеры ответят вам в течении XX минут')
	users[message.chat.id]['stage'] = NONE

@bot.message_handler(func = lambda message: message.text == 'Позвоните мне'  and UsersGetFix(message.chat.id, NONE))
def call(message):
	SetBotActiveStatus()
	keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
	button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
	keyboard.add(button_phone)
	bot.send_message(message.chat.id, "Подтвердите отправку номера телефона", reply_markup=keyboard)



# INLINE BUTTONS
@bot.callback_query_handler(func = lambda call: True)
def callback_inline(call):
	SetBotActiveStatus()
	if call.message:
		prefix = call.data.split('_')
		# ITEMS
		if prefix[0] == 'items':
			global items
			if prefix[1] == 'list':
				inline = types.InlineKeyboardMarkup()
				for i, item in enumerate(items):
					button = types.InlineKeyboardButton(text = item['title'], callback_data = 'items_get_' + str(i))
					inline.add(button)
				bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'Доступные курсы: ', reply_markup = inline)
			elif prefix[1] == 'get':
				itemId = prefix[2]
				item = items[int(itemId)]
				inline = types.InlineKeyboardMarkup()
				buy_button = types.InlineKeyboardButton(text = 'Приобрести',	callback_data = 'items_buy_' + itemId)
				inline.add(buy_button)
				back_button = types.InlineKeyboardButton(text = 'Назад',		callback_data = 'items_back')
				inline.add(back_button)
				bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = item['title'] + '\n' + item['price']['text'] + '\n\n' + item['description'], reply_markup = inline)
			elif prefix[1] == 'back':
				inline = types.InlineKeyboardMarkup()
				for i, item in enumerate(items):
					button = types.InlineKeyboardButton(text = item['title'], callback_data = 'items_get_' + str(i))
					inline.add(button)
				bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'Доступные курсы:', reply_markup = inline)
			elif prefix[1] == 'buy':
				item = items[int(prefix[2])]
				global PROVIDER_TOKEN
				global prices
				#bot.send_message(call.message.chat.id, 'Вы хотите купить курс:')
				bot.send_invoice(call.message.chat.id, title = item['title'],
					description=item['title'],
					provider_token=PROVIDER_TOKEN,
					currency='rub',
					photo_url=item['thumb_photo'], #'https://pp.userapi.com/c840537/v840537929/47684/fHHRxZQlt0o.jpg',
					photo_height=512,
					photo_width=384,
					photo_size=384,
					is_flexible=False,
					prices=[LabeledPrice(item['title'], int(item['price']['amount']))],
					start_parameter='ITEM',
					invoice_payload='item')
				#bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'Вы хотите купить курс ' + item['title'],)
		# REVIEWS
		elif prefix[0] == 'reviews':
			if prefix[1] == 'text':
				file = open('database/reviews/confirmed/index.txt', 'r')
				count = int(file.read())
				file.close()
				reviewId = int(prefix[2])
				inline = types.InlineKeyboardMarkup()
				if reviewId == 1:
					next_button = types.InlineKeyboardButton(text = 'Следующий', callback_data = 'reviews_text_2')
					prev_button = types.InlineKeyboardButton(text = 'Предыдущий', callback_data = 'reviews_text_' + str(count))
					inline.add(prev_button, next_button)
				elif reviewId == count:
					next_button = types.InlineKeyboardButton(text = 'Следующий', callback_data = 'reviews_text_1')
					prev_button = types.InlineKeyboardButton(text = 'Предыдущий', callback_data = 'reviews_text_' + str(reviewId - 1))
					inline.add(prev_button, next_button)
				else:
					next_button = types.InlineKeyboardButton(text = 'Следующий', callback_data = 'reviews_text_' + str(reviewId + 1))
					prev_button = types.InlineKeyboardButton(text = 'Предыдущий', callback_data = 'reviews_text_' + str(reviewId - 1))
					inline.add(prev_button, next_button)
				try:
					file = open('database/reviews/confirmed/' + str(reviewId) + '.txt')
					string = file.read()
					bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = string, reply_markup = inline)
				except:
					bot.send_message(call.message.chat.id, 'lael')
			elif prefix[1] == 'video':
				global video_reviews
				reviews = video_reviews['items']
				last = video_reviews['count'] - 1
				reviewId = int(prefix[2])
				review = reviews[reviewId]
				inline = types.InlineKeyboardMarkup()
				if reviewId == 0:
					next_button = types.InlineKeyboardButton(text = 'Следующий', callback_data = 'reviews_video_1')
					prev_button = types.InlineKeyboardButton(text = 'Предыдущий', callback_data = 'reviews_video_' + str(last))
					inline.add(prev_button, next_button)
				elif reviewId == last:
					next_button = types.InlineKeyboardButton(text = 'Следующий', callback_data = 'reviews_video_0')
					prev_button = types.InlineKeyboardButton(text = 'Предыдущий', callback_data = 'reviews_video_' + str(reviewId - 1))
					inline.add(prev_button, next_button)
				else:
					next_button = types.InlineKeyboardButton(text = 'Следующий', callback_data = 'reviews_video_' + str(reviewId + 1))
					prev_button = types.InlineKeyboardButton(text = 'Предыдущий', callback_data = 'reviews_video_' + str(reviewId - 1))
					inline.add(prev_button, next_button)
				bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = 'https://vk.com/video-' + str(GROUP_ID) + '_' + str(review['id']), reply_markup = inline)
		# QUESTIONS
		elif prefix[0] == 'questions':
			if prefix[1] == 'l':
				pass
			elif call.data[3] == 'q':
				pass


def BotStart():
	#Update()
	LoadData()
	#Update()
	f = open("database/stats.txt", "w")
	f.write("0")
	f.close()
	print("[i] Initializing telegram-bot...")
	bot.polling(none_stop = True)

