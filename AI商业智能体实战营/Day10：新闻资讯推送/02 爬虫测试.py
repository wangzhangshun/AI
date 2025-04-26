import requests

res = requests.get("https://p9-bot-sign.byteimg.com/tos-cn-i-v4nquku3lp/73f787fceabb416faeae0d64844b5c8a.text~tplv-v4nquku3lp-image.image?rk3s=68e6b6b5&x-expires=1747563016&x-signature=zack8VX5OAFhF8NAS9q%2FsaVLzm8%3D")
print(res.text)
