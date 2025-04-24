import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Cookie': 'BD_UPN=123253; PSTM=1740040530; BAIDUID=F22AA2608BE07EEBDF09A680B6B283CF:FG=1; BIDUPSID=10BEFB9ED77AD9EF189F465D0F7587BE; sugstore=0; H_WISE_SIDS=61027_62325_62344_62484_62867_62880_62892_62927_62969_62959_63019_63047; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID_BFESS=F22AA2608BE07EEBDF09A680B6B283CF:FG=1; RT="z=1&dm=baidu.com&si=1fbbd195-65c1-4333-a5ce-a8a6cad1f858&ss=m9sc711m&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=3ec&ul=3k6ob&hd=3k6ol"; COOKIE_SESSION=10471_0_9_9_12_28_0_4_8_8_16420_0_423169_0_0_0_1745305772_0_1745305760%7C9%2310_58_1743678437%7C9; H_PS_PSSID=61027_62325_62344_62484_62867_62880_62892_62927_62969_62959_63019_63047_63056; BD_HOME=1; BA_HECTOR=a104al0ga18005250g2h808l2p3pp41k0farp23; ZFY=TTwG:A2h:AL1ihZxYDe5eCoT2fJ2hEBnjr0G:AmYxMTrjo:C',
}
url = 'https://www.baidu.com/'
response = requests.get(url, headers=headers)

print(response.text)
