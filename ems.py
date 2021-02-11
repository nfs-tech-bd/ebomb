red = '\033[1;091m'
green = '\033[1;092m'
yellow = '\033[1;093m'
blue = '\033[1;094m'
purpel = '\033[1;095m'
cyan = '\033[1;096m'
import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
email = raw_input('Enter Your Gmail: ')
password = raw_input('Enter your Password: ')
msg = raw_input ('Enter Your Massege: ')
target = raw_input('Your Target: ')
number = input('Number of Message : ')
server.login(email,password)
for i in range(number):
	server.sendmail(email,target,msg)
	send = 'MASSEGE HAS BEEN SENT SUCESSFULLY'
	print '\n'+red+send
