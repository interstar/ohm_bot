import telebot

from id import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Oi!")

@bot.message_handler(commands=['law',"help"])
def law(message):
    bot.reply_to(message, """Ohm's Law : V = IR
Consumo : W = VI
/V@ohm_bot I R -> calcular voltagem baseada I e R
/I@ohm_bot V R -> calcular amperagem baseada V e R
/R@ohm_bot V I -> calcular resistence baseada V e I
/W@ohm_bot I V -> calcular consumo baseada voltagem e amperagem
/A@ohm_bot V W -> calcular amperes baseada voltagem e consumo
""")

def isNum(x) :
    try:
        float(x)
        return True
    except ValueError :
        return False

def nums(s) :
    print s
    return [float(x) for x in s.split(" ")[1:] if isNum(x)]

def error(f) :
    def g(message) :
        try :
            f(message)
        except Exception, e:
            bot.reply_to(message,"ERRO : %s" % e)
    return g


@bot.message_handler(commands=['V'])
@error
def calcV(message):
    items = nums(message.text)
    bot.reply_to(message,"%s volts" % (items[0]*items[1]))

@bot.message_handler(commands=['I'])
@error
def calcI(message):
    items = nums(message.text)
    bot.reply_to(message,"%s amps"%(items[0]/items[1]))

@bot.message_handler(commands=['R'])
@error
def calcR(message):
    items = nums(message.text)
    bot.reply_to(message,"%s ohms" % (items[0]/items[1]))

@bot.message_handler(commands=['A'])
@error
def calcA(message) :
    items = nums(message.text)
    bot.reply_to(message,"%s amps" % (items[1]/items[0]))

@bot.message_handler(commands=['W'])
@error
def calcW(message) :
    items = nums(message.text)
    bot.reply_to(message,"%s watts" % (items[0]*items[1]))


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
