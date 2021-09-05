import requests
from multiprocessing.dummy import Pool as ThreadPool
from colorama import init, deinit, Fore, Back, Style 
init()

def checker(proxy):
    proxy=proxy.split(':')  
    data = {"ip_addr": proxy[0],"port": proxy[1]}

    response = requests.post('https://api.proxyscrape.com/v2/online_check.php', data=data)
    x=response.json()
    print(x)
    ip=x["ip"]
    port=x["port"]
    type=x["type"]
    country=x["country"]
    working=x["working"]
    if working is True:
        working_proxy = ip+":"+port+" "+type+" "+country
        print(Fore.LIGHTGREEN_EX + working_proxy)
    else:
        return '0'
    return working_proxy

def calculateParallel(numbers, threads=2):
    pool = ThreadPool(threads)
    results = pool.map(checker, numbers)
    pool.close()
    pool.join()
    return results

def proxytypecheck(proxys):
    print("\n")
    print(Fore.LIGHTYELLOW_EX + "Processing...")
    print("\n")
    proxys = proxys.text
    proxy_List=proxys.split("\r\n")
    proxy_List.remove('')
    if proxy_List != '' or None:
            workingproxy=calculateParallel(proxy_List, 100)
            if workingproxy != []:
                print(Fore.CYAN + "\nProxy Type Country\n==================\n")
                for prox in workingproxy:
                    if(prox != '0'):
                        print(Fore.LIGHTBLUE_EX + prox)
                print(Fore.LIGHTWHITE_EX + "[Note: Try repeatations to get stable proxy to stream!]")
                print("\n")
            else:
                print(Fore.LIGHTRED_EX + "Not available right now.\nCheck back in 10min!")
    else:
        print(Fore.LIGHTRED_EX + "Not available right now.\nCheck back in 10min!")
 

def provideinput():
    info_list = """
    1.HTTP/s
    2.Socks4
    3.Socks5
    q.Quit
    """
    print(Fore.LIGHTGREEN_EX + info_list)
    print(Fore.LIGHTCYAN_EX + "Choose input: ",end="")
    user_input = input()
    if(user_input == '1' or user_input == '2' or user_input == '3'):
        print(Fore.LIGHTCYAN_EX + "Enter ping (10 - 10000)\n(Hint: Lower is better!): ",end="")
        ping_input = input()
        print("\nCountry inputs [options:all,US,GB,DE,...]: ",end='')
        country_input = input()
        
    if(user_input == '1'):
        proxys = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout='+ping_input+'&country='+country_input+'&ssl=yes&anonymity=all')
        proxytypecheck(proxys)
    elif(user_input == '2'):
        proxys = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout='+ping_input+'&country='+country_input)
        proxytypecheck(proxys)
    elif(user_input == '3'):
        proxys = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout='+ping_input+'&country='+country_input)
        proxytypecheck(proxys)
    elif(user_input == 'q' or user_input == 'Q'):
        deinit()
        exit()
    else:
        print(Fore.LIGHTRED_EX + "Invalid Input!")
        provideinput()
while True:
    print(Fore.LIGHTYELLOW_EX + "====> Thanks to Believer! https://ttttt.me/believerseller <====")
    provideinput()