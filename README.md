# Ohm Bot
Experimental Telegram Bot that knows Ohm's Law (and can do calculations with it)

Ohm's Law : V = IR

Consumo : W = VI

/V@ohm_bot I R -> calcular voltagem baseada I e R

/I@ohm_bot V R -> calcular amperagem baseada V e R

/R@ohm_bot V I -> calcular resistence baseada V e I

/W@ohm_bot I V -> calcular consumo baseada voltagem e amperagem

/A@ohm_bot V W -> calcular amperes baseada voltagem e consumo

## Notes : 
1) This program uses the [pyTelegramBotAPI library](https://github.com/eternnoir/pyTelegramBotAPI) which can be installed with pip.

2) You must have a file called local_credentials.py in this directory, which defines the string TOKEN (containing your Telegram Bot token)

