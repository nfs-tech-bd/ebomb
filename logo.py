# -*- coding: utf-8 -*-
import time,sys
logo= '''
███████╗███╗   ███╗███████╗
██╔════╝████╗ ████║██╔════╝
█████╗  ██╔████╔██║███████╗
██╔══╝  ██║╚██╔╝██║╚════██║
███████╗██║ ╚═╝ ██║███████║
╚══════╝╚═╝     ╚═╝╚══════╝

CODED BY B14CK-KN1GH7 (NAFIS) 
FACEBOOK : http://facebook.com/nafis.fuad.904
WEBSITE : http://entertainbd.wapkiz.com
'''
def logop(z):
	for word in z + '\n':
		sys.stdout.write(word)
		sys.stdout.flush()
		time.sleep(0.01)
logop(logo)
