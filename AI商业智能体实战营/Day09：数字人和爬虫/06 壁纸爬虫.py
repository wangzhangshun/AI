import requests

import requests

cookies = {
    'cf_clearance': 'KaSKuUXQrcr9Tr5uA4F62fhOrLNxdDAn7Lm3RU0KrZ4-1745337099-1.2.1.1-p5d72uo8XL4pNuQolgoWwM_VWpdprLivUiXSDQG2ZWU8Bkv1B3LysB79L3DyUC.WeueeIcbKGjZ7wXh2IKYBRMcR7oeyor7LaCf1mlXL4t7EbUkIqNH3Od6RpZDPpnAjQTXq2n6q0yePay_xlXWQa1Vy0l1quqNSloQFu9RsoCwJm0.GfhkBhA2.TynoD4zKPcyomdvMEEEBG.FvuRPi0Lxznczp4DGEnyr9IBDSAk.r9JFcwvWBlomeR.Xper.a2FY3.7sC0B2t3GEb2xhVHAeGZv7Ja6_NQ1onVZOqIl2fDJ6ODKEG2ahHccBiVDKGl9NXpb15zZFsVXluQF7cJU5d4jERl04F0r0TZaJSIx8Jq_S59asnAFokRZTPX1DU',
    'zkhanecookieclassrecord': '%2C54%2C66%2C59%2C53%2C55%2C',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-arch': '"arm"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"135.0.7049.96"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    # 'cookie': 'cf_clearance=KaSKuUXQrcr9Tr5uA4F62fhOrLNxdDAn7Lm3RU0KrZ4-1745337099-1.2.1.1-p5d72uo8XL4pNuQolgoWwM_VWpdprLivUiXSDQG2ZWU8Bkv1B3LysB79L3DyUC.WeueeIcbKGjZ7wXh2IKYBRMcR7oeyor7LaCf1mlXL4t7EbUkIqNH3Od6RpZDPpnAjQTXq2n6q0yePay_xlXWQa1Vy0l1quqNSloQFu9RsoCwJm0.GfhkBhA2.TynoD4zKPcyomdvMEEEBG.FvuRPi0Lxznczp4DGEnyr9IBDSAk.r9JFcwvWBlomeR.Xper.a2FY3.7sC0B2t3GEb2xhVHAeGZv7Ja6_NQ1onVZOqIl2fDJ6ODKEG2ahHccBiVDKGl9NXpb15zZFsVXluQF7cJU5d4jERl04F0r0TZaJSIx8Jq_S59asnAFokRZTPX1DU; zkhanecookieclassrecord=%2C54%2C66%2C59%2C53%2C55%2C',
}

response = requests.get(
    'https://pic.netbian.com/uploads/allimg/250421/201317-1745237597a15c.jpg',
    cookies=cookies,
    headers=headers,
)


# 将数据写入一个

with open("a.jpg","wb") as f:
    f.write(response.content)