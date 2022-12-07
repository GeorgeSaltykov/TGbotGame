import telebot
from telebot import types
from config import token

bot = telebot.TeleBot(token, parse_mode='html')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    start = types.KeyboardButton('НАЧАТЬ ИГРУ')
    markup.add(start)
    bot.reply_to(message, f'Приветствую тебя, <b>{message.from_user.first_name}</b>!\n'
                          'Предлагаю сыграть в игру.\n'
                          'Ты получишь небольшую предысторию и варианты действий. '
                          'Помни! - каждое действие влияет на дальнейший ход истории.', reply_markup=markup)


@bot.message_handler(regexp='НАЧАТЬ ИГРУ')
def start_game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Ах, да! Дома же совсем нет еды!')
    second_choice = types.KeyboardButton('Хотелось что-нибудь интересное, '
                                         'не то, что обычно покупаешь.')
    markup.add(first_choice, second_choice)
    bot.reply_to(message, '<i>Звук из репродуктора: "Добро пожаловать в <b>"Пяторочку"</b>".\n'
                          'Кажется, ты пришел в себя и обнаружил, что находишься в магазине. '
                          'В голове небольшой бардак, но все более-менее встаёт на свои места.</i>\n'
                          '- Однако, зачем же... Зачем я здесь? - <i>спускается мысль\nоткуда-то изнутри. '
                          'И вот, будто бы что-то нащупалось...</i>', reply_markup=markup)


@bot.message_handler(regexp='Ах, да! Дома же совсем нет еды!')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Нет, чего-чего, а пить я не буду.')
    second_choice = types.KeyboardButton('Да что уж там, раз уж пришел, можно и бутылочку-другую...')
    markup.add(first_choice, second_choice)
    bot.reply_to(message, '- Что же взять?.. Может, приготовить курицу в сметане? - <i>размышляешь ты,'
                          ' а в это время ноги ведут тебя сами собой в отдел с алкоголем. '
                          'Так и невольно задумаешься...</i> ', reply_markup=markup)


@bot.message_handler(regexp='Хотелось что-нибудь интересное, '
                            'не то, что обычно покупаешь.')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Я к такому не был готов.')
    second_choice = types.KeyboardButton('Пожалуй, немного спаржи, помидоров, чеснок и лагенарии.')
    markup.add(first_choice, second_choice)
    bot.reply_to(message, 'Вспомнить бы еще, что я обычно беру... Вот, блин. Придумал на свою голову. \n'
                          '<i>Перед тобой лежат овощи в чарующем разнообразии. Чего здесь только нет! '
                          'Артишоки, картошка, батат, лук, брюква, дайкон, картофель фиолетовый, лагенария, '
                          'пастернак, ревень, свекла, скорцонера, капуста, брокколи, цветная, лук-порей,'
                          'огурцы китайские длинные, короткие и средних размеров, топинамбур, помидоры из Узбекистана, '
                          'Дагестана и Твери, черри, черная кукуруза, брюссельская капуста, тыква, капуста романеско, '
                          'арбузный редис, редис обыкновенный, цуккини, морковь, черные томаты, спаржа, перец '
                          'болгарский, чеснок, чеснок черный ферментированный, перец чили, кайенский перец '
                          'шоколадный болгарский перец, оча, чуфа, кольраби, овсяный корень, кай-лан, пекинская капуста'
                          ', горох свежий, нопаль, маниок съедобный, дульсе, стручковая фасоль, побеги папоротника, '
                          'лук белый и красный, и зеленый...</i> <b><s>Кажется, автор слегка долбанутый.</s></b>'
                          '', reply_markup=markup)


@bot.message_handler(regexp='Нет, чего-чего, а пить я не буду.')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Закусывать.')
    second_choice = types.KeyboardButton('Запивать.')
    markup.add(first_choice, second_choice)
    bot.reply_to(message, 'Ха! Так я себе и поверил!\n'
                          '<i>Говоришь ты вслух и протягиваешь руку за виски.</i>\n'
                          'Закусывать или запивать? Вот в чем вопрос.', reply_markup=markup)


@bot.message_handler(regexp='Да что уж там, раз уж пришел, можно и бутылочку-другую...')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Заговорить.')
    second_choice = types.KeyboardButton('Взять творог, сметану и идти дальше.')
    markup.add(first_choice, second_choice)
    bot.reply_to(message, 'Ай, нет. Все-таки не стоит. Пойду я, пожалуй, возьму творог со сметанкой'
                          '.\n<i>Спустя минуту, ты в молочном отделе. Недалеко от тебя девушка стоит в слезах</i>'
                          '', reply_markup=markup)


@bot.message_handler(regexp='Я к такому не был готов.')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Помолиться.')
    second_choice = types.KeyboardButton('Закричать и упасть в предсмертной агонии.')
    markup.add(first_choice, second_choice)
    audio = open("deathOze.mp3", 'rb')
    bot.send_audio(message.from_user.id, audio)
    bot.reply_to(message, '<i>Ты все ещё стоишь пред ликом овощей, не в силах оторвать паникующих глаз '
                          'от такого неправдоподобного разнообразия. Ты пытаешься сдинуться с места, но они словно '
                          'овладели тобой и смотрят прямо в душу.</i>\n'
                          '- Господи, ты ли это?..', reply_markup=markup)


@bot.message_handler(regexp='Пожалуй, немного спаржи, помидоров, чеснок и лагенарии.')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Пойти за сливками и сыром.')
    second_choice = types.KeyboardButton('Пойти за медом.')
    markup.add(first_choice, second_choice)
    bot.reply_to(message, 'Сливки, сыр и мед - вот что мне надо.', reply_markup=markup)


@bot.message_handler(regexp='Закусывать.')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Отправиться на кассу.')
    markup.add(first_choice)
    bot.reply_to(message, 'А что, зачем выбирать, если можно взять и того и другого! <i>Решаешь ты и берешь колу, '
                          'грейпфрутовый сок, шоколад, селедку в масле и пельмени.</i>', reply_markup=markup)


@bot.message_handler(regexp='Запивать.')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Отправиться на кассу.')
    markup.add(first_choice)
    bot.reply_to(message, 'А что, зачем выбирать, если можно взять и того и другого! <i>Решаешь ты и берешь колу, '
                          'грейпфрутовый сок, шоколад, селедку в масле и пельмени.</i>', reply_markup=markup)


@bot.message_handler(regexp='Пойти за сливками и сыром.')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Пойду за мёдом!')
    markup.add(first_choice)
    bot.reply_to(message, '<i>В молочном отделе ты выбрал 20% сливки и гауду.</i>\n'
                          'Теперь пора за мёдом!', reply_markup=markup)


@bot.message_handler(regexp='Пойти за медом.')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('А теперь за сливками и сыром!')
    markup.add(first_choice)
    bot.reply_to(message, '<i>Спустя пару минут, ты нашел полку, на которой находится мёд.</i>\nТеперь пора'
                          ' за сливками и сыром!', reply_markup=markup)


@bot.message_handler(regexp='А теперь за сливками и сыром!')
def start_game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Пойти за вином.')
    markup.add(first_choice)
    bot.reply_to(message, 'Ну а ко всему этому, можно взять красное полусухое.', reply_markup=markup)


@bot.message_handler(regexp='Пойду за мёдом!')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Пойти за вином.')
    markup.add(first_choice)
    bot.reply_to(message, 'Ну а ко всему этому, можно взять красное полусухое.', reply_markup=markup)


@bot.message_handler(regexp='Пойти за вином.')
def game(message):
    audio = open('pjaterka.mp3', 'rb')
    bot.send_audio(message.from_user.id, audio)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    choice = types.KeyboardButton('Начать заного.')
    markup.add(choice)
    bot.reply_to(message, '<i>И вот у тебя уже есть все что нужно. До прекрасного ужина осталось всего ничего. '
                          'Ты проходишь на кассу, девушка улыбается тебе и радушно приветствует. Пока она пробивает '
                          'товары, у вас завязывается легкий и непринужденный разговор. Все это кажется весьма '
                          'интересным настолько, что вы обмениваетесь номерами и договариваетесь как-нибудь пообщаться'
                          ' в более непринуждённой обстановке.\nТы выходишь на улицу, вдыхаешь прохладный вечерний '
                          'воздух, а дальше... А дальше решать тебе.</i>', reply_markup=markup)


@bot.message_handler(regexp='Помолиться.')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Аминь.')
    second_choice = types.KeyboardButton('Тьфу. Это уже перебор!')
    markup.add(first_choice, second_choice)
    bot.reply_to(message, 'Отче наш, Иже еси на овощах!\nДа святится имя Твое,\nда приидет Царствие Твое,\n'
                          'да будет воля Твоя,\nяко на овощах и на щах.\nХлеб наш насущный даждь нам днесь;\n'
                          'и остави нам долги наша,\nякоже и мы оставляем должником нашим;\n'
                          'и не введи нас во искушение,\nно избави нас от лукаваго.\n'
                          'Ибо Твое есть Царство и сила и слава во веки.\n', reply_markup=markup)


@bot.message_handler(regexp='Тьфу. Это уже перебор!')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Начать заного.')
    markup.add(first_choice)
    audio = open('wolfgang.mp3', 'rb')
    bot.send_audio(message.from_user.id, audio)
    bot.reply_to(message, 'АААААААААА!!!!!!!!!\n <i>Это все, что успевает сорваться с твоих губ, и ты падаешь на земь. '
                          'Вокруг тебя собираются тучи, гремит гром, но гремит он словно голос божества.</i>\n'
                          '<b>Аз есмь брюква и морковка. Ты отказался внемлить мне. И за это не есть тебе овощей '
                          'НИКОГДА!!!</b>\n<i>Эхом разносится ужасающее "НИКОГДА". С глаз твоих стекают слёзы. Тучи '
                          'расходятся.\n Не взяв ни единого продукта, ты убегаешь домой. И до самого конца жизни ты так'
                          ' и не съешь ни единого овоща. Лишь на смертном одре, к тебе снизойдет капуста. И вкусив её, '
                          'ты поймешь - это Его прощение...</i>', reply_markup=markup)


@bot.message_handler(regexp='Аминь.')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Да, Господь. Я пойду разносить молву о тыкве и чесноке.')
    markup.add(first_choice)
    audio = open('amadeus.mp3', 'rb')
    bot.send_audio(message.from_user.id, audio)
    bot.reply_to(message, '<i>Ты откусываешь кусок редиски и запиваешь морковным соком, так проходит причастие '
                          'Овощного Бога. И в этот миг разверзлась картошка, и оттуда снизошел свет и голос Его. </i>'
                          '<b>Аз есмь брюква и морковка. Внемли мне, пророк. Ты пойдешь по свету и будешь нести '
                          'глас мой, дабы люди услыхали Его и узнали кому надобно молиться.'
                          'Дабы огурец сошел на землю и наступил рай.</b>\n'
                          'Офигевая от увиденного, ты говоришь...', reply_markup=markup)


@bot.message_handler(regexp='Да, Господь. Я пойду разносить молву о тыкве и чесноке.')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Начать заного.')
    markup.add(first_choice)
    bot.reply_to(message, '<i>Узрев Его и вкусив плоть и кровь Его, не оплатив покупки, ты выходишь из магазина '
                          'и там, за его дверьми, начинается твой долгий путь...</i>', reply_markup=markup)


@bot.message_handler(regexp='Закричать и упасть в предсмертной агонии.')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Начать заного.')
    markup.add(first_choice)
    audio = open('wolfgang.mp3', 'rb')
    bot.send_audio(message.from_user.id, audio)
    bot.reply_to(message, 'АААААААААА!!!!!!!!!\n <i>Это все, что успевает сорваться с твоих губ, и ты падаешь на земь. '
                          'Вокруг тебя собираются тучи, гремит гром, но гремит он словно голос божества.</i>\n'
                          '<b>Аз есмь брюква и морковка. Ты отказался внемлить мне. И за это не есть тебе овощей '
                          'НИКОГДА!!!</b>\n<i>Эхом разносится ужасающее "НИКОГДА". С глаз твоих стекают слёзы. Тучи '
                          'расходятся.\n Не взяв ни единого продукта, ты убегаешь домой. И до самого конца жизни ты так'
                          ' и не съешь ни единого овоща. Лишь на смертном одре, к тебе снизойдет капуста. И вкусив её, '
                          'ты поймешь - это Его прощение...</i>', reply_markup=markup)


@bot.message_handler(regexp='Заговорить.')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Перекреститься и убежать домой, не оплатив покупки.')
    second_choice = types.KeyboardButton('Продолжить общаться.')
    markup.add(first_choice, second_choice)
    bot.reply_to(message, 'Где, говорю, тебя я видел?\nКто, мне скажи, тебя обидел? Забыл тебя?\nТы Орландина, '
                          'ты судьба моя\nПризнайся мне, ведь я узнал тебя.'
                          '\n<i>А она отвечает, мол да, это она, что это ты её обидел, но для тебя забудет слёзы '
                          'и пойдет с тобой, коль позовешь, и будет твоя.</i>', reply_markup=markup)


@bot.message_handler(regexp='Продолжить общаться.')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Ну тут уж извиняй, теперь не убежать.')
    markup.add(first_choice)
    bot.reply_to(message, 'Ах как хочу тебя обнять я\nПоцеловать рукав от платья\nНу, так приди в мои объятья... '
                          '<i>\nИ в этот миг\nШерстью покрылся лоб девичий\nКрасен стал глаз, а голос птичий\nИ '
                          'волчий лик, меня чудовище схватило\nИ сладострастно испустило мерзостный крик</i>'
                          '', reply_markup=markup)


@bot.message_handler(regexp='Ну тут уж извиняй, теперь не убежать.')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Начать заного.')
    markup.add(first_choice)
    audio = open('Orlandina.mp3', 'rb')
    bot.send_audio(message.from_user.id, audio)
    bot.reply_to(message, '<i>Ну и чудовище продолжает:\n'
                          'Видишь ли, я не Орландина\nДа, я уже не Орландина\nЗнай, я вообще не Орландина, я ― '
                          'Люцифер!\nВидишь, теперь в моих ты лапах\nСлышишь ужасный серый запах? И гул огня?\nТак '
                          'завопил он и вонзил свой зуб\nВ твой бедный лоб свой древний медный зуб\nСам сатана, сам '
                          'сатана</i>', reply_markup=markup)


@bot.message_handler(regexp='Перекреститься и убежать домой, не оплатив покупки.')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Начать заного.')
    markup.add(first_choice)
    audio = open('Orlandina.mp3', 'rb')
    bot.send_audio(message.from_user.id, audio)
    bot.reply_to(message, '<i>Ты сумел убежать от дьявола. А все потому что знаешь текст песни)).</i>'
                          '', reply_markup=markup)


@bot.message_handler(regexp='Взять творог, сметану и идти дальше.')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Пойти взять апельсиновый сок.')
    markup.add(first_choice)
    bot.reply_to(message, 'Пожалуй возьму еще апельсиновый сок.', reply_markup=markup)


@bot.message_handler(regexp='Пойти взять апельсиновый сок.')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('На кассу.')
    markup.add(first_choice)
    bot.reply_to(message, 'Ну, кажется, мне пока больше ничего не нужно.', reply_markup=markup)


@bot.message_handler(regexp='Отправиться на кассу.')
def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Начать заного.')
    markup.add(first_choice)
    audio = open('toska.mp3', 'rb')
    bot.send_audio(message.from_user.id, audio)
    bot.reply_to(message, '<i>Ты расплачиваешься за все и выходишь на улицу. Улыбка проявляется на твоем лице, а внутри'
                          ' чувствуешь себя свободным. Сегодня ты разрешил себе отдохнуть. Скоро ты будешь дома. '
                          'Позвонишь парочке близких друзей. Они приедут, и вы просто приятно проведёте время...</i>'
                          '', reply_markup=markup)


@bot.message_handler(regexp='На кассу.')
def game(message):
    audio = open('pjaterka.mp3', 'rb')
    bot.send_audio(message.from_user.id, audio)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    choice = types.KeyboardButton('Начать заного.')
    markup.add(choice)
    bot.reply_to(message, '<i>И вот у тебя уже есть все что нужно. До прекрасного ужина осталось всего ничего. '
                          'Ты проходишь на кассу, девушка улыбается тебе и радушно приветствует. Пока она пробивает '
                          'товары, у вас завязывается легкий и непринужденный разговор. Все это кажется весьма '
                          'интересным настолько, что вы обмениваетесь номерами и договариваетесь как-нибудь пообщаться'
                          ' в более непринуждённой обстановке.\nТы выходишь на улицу, вдыхаешь прохладный вечерний '
                          'воздух, а дальше... А дальше решать тебе.</i>', reply_markup=markup)



@bot.message_handler(regexp='Начать заного.')
def start_game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_choice = types.KeyboardButton('Ах, да! Дома же совсем нет еды!')
    second_choice = types.KeyboardButton('Хотелось что-нибудь интересное, '
                                         'не то, что обычно покупаешь.')
    markup.add(first_choice, second_choice)
    bot.reply_to(message, '<i>Звук из репродуктора: "Добро пожаловать в <b>"Пяторочку"</b>".\n'
                          'Кажется, ты пришел в себя и обнаружил, что находишься в магазине. '
                          'В голове небольшой бардак, но все более-менее встаёт на свои места.</i>\n'
                          '- Однако, зачем же... Зачем я здесь? - <i>спускается мысль\nоткуда-то изнутри. '
                          'И вот, будто бы что-то нащупалось...</i>', reply_markup=markup)


bot.infinity_polling()
