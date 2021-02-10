red = '\033[1;091m'
green = '\033[1;092m'
yellow = '\033[1;093m'
blue = '\033[1;094m'
purpel = '\033[1;095m'
cyan = '\033[1;096m'
import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
you = raw_input('ENTER YOUR MAIL: ')
password = raw_input('ENTER YOUR PASS: ')
massage = raw_input('MESSAGE: ')
target = raw_input('TARGET: ')
server.login(you,password)
server.sendmail(you,target,massage)
send = 'MESSAGE SEND SUCESSFULLY'
print '\n'+red+send
