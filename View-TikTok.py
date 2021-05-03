#KING M3GON
#This Tool By instagram @_m3gon
try:#m3gon
        import requests#m3gon
except:#m3gon
        print('[-] pip install requests')#m3gon
try:#m3gon
        import colorama#m3gon
        from colorama import Fore#m3gon
        colorama.init(autoreset=colorama)#m3gon
except:#m3gon
        print('[-] pip install colorama')#m3gon
import re
def banner():#m3gon
        Bb = Fore.LIGHTYELLOW_EX#m3gon
        print(Bb + """
            __  __ ____   _____  ____  _   _ 
            |  \/  |___ \ / ____|/ __ \| \ | |
            | \  / | __) | |  __| |  | |  \| |
            | |\/| ||__ <| | |_ | |  | | . ` |
            | |  | |___) | |__| | |__| | |\  |
            |_|  |_|____/ \_____|\____/|_| \_|
        """, Fore.LIGHTGREEN_EX + "\n                       ( @_m3gon )",
              Fore.LIGHTBLUE_EX + "\n        (This tool is programmed by the programmer : @_m3gon)              \n",
              Fore.LIGHTYELLOW_EX + "                  ( View TikTok )\n\n" + Fore.RESET)#m3gon
banner()#m3gon
link_id = input('[?] Enter Url Post : ')
Thread = int(input('[?] Enter Thread : '))
def get_id_vedio():
        headers_id = {
                'Connection': 'close',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.9',
                'Cookie': 'tt_webid_v2=6940688826462406145; tt_webid=6940688826462406145; ttwid=1%7Cbza8rvLOfNRPRwC43Zn3utwgngykYIkkhCtiFchZVMA%7C1616005073%7C1dd5efed4a61e4b1654f08f10a6ff7b85e3d57622a4d6011f6642b1bbf785fcb; passport_csrf_token=bb82884d8da300de0ce4f8508694e635; passport_csrf_token_default=bb82884d8da300de0ce4f8508694e635; store-country-code=sa; tta_attr_id=0.1616499265.6942811476331593729; store-idc=alisg; sid_guard=5c3ba51706c6f27ef59bb4fcaf0d282b%7C1617813999%7C5184000%7CSun%2C+06-Jun-2021+16%3A46%3A39+GMT; uid_tt=9896d319adfbb4f4f7a56b2122e84ef36354da5b7a766c3d93f08771723b2e3f; uid_tt_ss=9896d319adfbb4f4f7a56b2122e84ef36354da5b7a766c3d93f08771723b2e3f; sid_tt=5c3ba51706c6f27ef59bb4fcaf0d282b; sessionid=5c3ba51706c6f27ef59bb4fcaf0d282b; sessionid_ss=5c3ba51706c6f27ef59bb4fcaf0d282b; odin_tt=530994ec29b8076689f2e696e07f7968d74abe62dc6990364400b7b666b98e83afe2d12f34a5c717c851ce41d2368908d1f4c45a8c3974fb4230088b6d230969a128029a783f0ae00352b0d06fa62e0a; R6kq3TV7=AMgpub14AQAASGoycNrCjOkGEeZn3OSfPJcGlZpRyawc4vVW0_K5JN1ScBmQ|1|0|427184ccd78b46f2f1443048844aba7bf6064745; cmpl_token=AgQQAPO_F-RMpY4vzNb-op0_-jPehXJPv4M0YPgasw; tt_csrf_token=Ev5Kwld907oqGN2T1k0HrHWF; ak_bmsc=ED95FE19720A8F91CACBCE8408BFC78E56335E9519250000BF887260FE32B047~pl7zsPkhgfEfP2YwW3Ph6y02EtVXax7QH9oUN1eMfTdDnvOlFJcDXESyLLkFAXRIaueH2qItg4EdfKBI5loXsbdYeZAAy2oCOz7PNDhyQvstusWjR1M6xBMzpFKRcIXuEXMwtrfBx4nQLynJxNr7CJOOKb02W/y1LENhAnX2p+eHB4S6HL5PRUVaJXx6xqRPtjaFzenP3I/+Wx44jRsDjDNlxmlM7krZQs+TzdJApyqZ4=; bm_sz=F1634B2D883BE7F7F8E55AF4D48798F6~YAAQlV4zViahf3R4AQAAIitmvwtx/krEk+BEEQt4CoGeEB0X2JTHtZKLSBFVXxGgh8oLe8VcsrGqbUWhtO2eK/fhU6tdNs4C36OkPBJt7HlGRC07i6coxuZO1bcf0pxWJoJppYUoC9vPHQYh1++jflOXTPVSS0hw/W++SqiceRZkS+Q5SWGwWgWnx6hP4VB1; bm_sv=5AF097FF6E9C14E8BF077EE5BD7D126D~LBiUQfj1jYvhXvESNmEdfPzQcX6s8MGsQ79mJvSVV/OclkEWqotEPinlq8GADZ+tDMWTfCrS+nQ/dH0mG7bwj0L/5a8LC5sn4KJC+CEzqxHnt2JcMCSmRrYV5vO6sJDXY01ZEpWWSdJTGeCbBD7l2DPIFidy9J5ujWVeVBBbY6I=; _abck=494D5CEEE963A444A9BFED1397AE4A1A~-1~YAAQl14zVjHK03V4AQAAfJRovwV3ujEp8mNTnNKx5q6XhLXbDZgBUZwYi8ZS6N3zYCWz6lpsDgFzXfDQT7dKaxDyijowI/MIW0aLuDCIUFU5bw1xBMaKFv4tvXv8QfiThLmgZh3ihOCUJ9xBvVcf9Aw3OQ0YIpDK7oCidJ7WeQkT5jGIhm9yXvB6zUde3/xrOzZyDyxLO6qbSuunOwTmgGN/+qoNcrE82ZJDp3faWXgLMEtgi22ui9gENAV5rnlzEZll3e8AZMn9xZbq+9Aa7SAtgmih3i4WTgyPxwR7DXjPNZ+pnnAb/qJ+JCI+TFIiRW31KVuqy0A6142qz3Whm+XM++sQIWOuThkmXtEh25NeYtyKV3LwWDHMPg7sICqWEjOtgCLPh4lUxLpZaroVbcn0hnVZQ/ab~0~-1~-'
        }
        try:
                req_id = requests.get(link_id, headers=headers_id).text
                id_post1 = re.findall('"video":{"id":"(.*?)"', req_id)
                id_post = "".join(id_post1)
                print('[+] Done Get Id Post ..')
        except:
                print('[-] Not Found Id Post')
                exit(0)
        def View():
                url_view = 'https://api16-core-c-alisg.tiktokv.com/aweme/v1/aweme/stats/?ac=WIFI&op_region=SA'
                headers_view = {
                        'Host': 'api16-core-c-alisg.tiktokv.com',
                        'Content-Length': '138',
                        'Sdk-Version': '2',
                        'Passport-Sdk-Version': '5.12.1',
                        'X-Tt-Token': '01de097c7d0877a06067897aabb4bf27970263ef2c096122cc1a97dec9cd12a6c75d81d3994668adfbb3ffca278855dd15c8056ad18161b26379bbf95d25d1f065abd5dd3a812f149ca11cf57e4b85ebac39d - 1.0.0',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'User-Agent': 'TikTok 17.4.0 rv:174014 (iPhone; iOS 14.2; ar_SA@calendar=gregorian) Cronet',
                        'X-Ss-Stub': '727D102356930EE8C1F61B112F038D96',
                        'X-Tt-Store-Idc': 'alisg',
                        'X-Tt-Store-Region': 'sa',
                        'X-Ss-Dp': '1233',
                        'X-Tt-Trace-Id': '00-33c8a619105fd09f13b65546057d04d1-33c8a619105fd09f-01',
                        'Accept-Encoding': 'gzip, deflate',
                        'X-Khronos': '1620071457',
                        'X-Gorgon': '840280416000d88c456af519b3652ea63974e294429b0041db20',
                        'X-Common-Params-V2': 'pass-region=1&pass-route=1&language=ar&version_code=17.4.0&app_name=musical_ly&vid=0F62BF08-8AD6-4A4D-A870-C098F5538A97&app_version=17.4.0&carrier_region=SA&channel=App%20Store&mcc_mnc=42001&device_id=6904193135771207173&tz_offset=10800&account_region=&sys_region=SA&aid=1233&residence=SA&screen_width=1125&uoo=1&openudid=c0c519b4e8148dec69410df9354e6035aa155095&os_api=18&os_version=14.2&app_language=ar&tz_name=Asia/Riyadh&current_region=SA&device_platform=iphone&build_number=174014&device_type=iPhone10,6&iid=6958149070179878658&idfa=00000000-0000-0000-0000-000000000000&locale=ar&cdid=D1D404AE-ABDF-4973-983C-CC723EA69906&content_language=',
                        'Connection': 'close'
                }
                cookie_view = {'sessionid': 'de097c7d0877a06067897aabb4bf2797'}
                data_view = f'action_time=1620071984&aweme_type=0&first_install_time=1607507898&item_id={id_post}&play_delta=1&tab_type=4'
                while True:
                        req_explore = requests.post(url_view, data=data_view, headers=headers_view,cookies=cookie_view).text
                        if ('"status_code":0') in req_explore:
                                print('[+] Done View')
                        else:
                                print('[-] Error View')
        import threading
        Threads = []
        for i in range(Thread):
                thread1 = threading.Thread(target=View)
                thread1.start()
                Threads.append(thread1)
        for thread2 in Threads:
                thread2.join()
get_id_vedio()
