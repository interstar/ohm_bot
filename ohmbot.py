import telebot


class Transcript :

	def __init__(self,fName) :
		self.f = open(fName,"a")
	
	def write(self,message) :
		self.f.write("%s\n"%message.text)
		self.f.flush()
	
TXT = Transcript("transcript.txt")
		
from local_credentials import TOKEN

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
/A@ohm_bot W V -> calcular amperes baseada voltagem e consumo
""")

def isNum(x) :
    try:
        float(x)
        return True
    except ValueError :
        return False

def nums(s) :
    return [float(x) for x in s.split(" ")[1:] if isNum(x)]

def error(f) :
    def g(message) :
        TXT.write(message)
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
    bot.reply_to(message,"%s amps" % (items[0]/items[1]))

@bot.message_handler(commands=['W'])
@error
def calcW(message) :
    items = nums(message.text)
    bot.reply_to(message,"%s watts" % (items[0]*items[1]))




@bot.message_handler(func=lambda message: True)
@error
def echo_all(message):
    #print message.text
    #bot.reply_to(message, message.text)
    pass
	
bot.polling()
