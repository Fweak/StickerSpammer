import requests
from colorama import Fore, init
init(convert=True)

class StickerAssult:
    def __init__(self, token, channel):
        self.token = token
        self.channelId = channel
        self.headers = {
            'Authorization': self.token,
            'via': '1.1 google',
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
        }

    def getStickersFromPacks(self):
        data = requests.get('https://discord.com/api/v8/users/@me/sticker-packs', headers=self.headers)
        if data.status_code == 200:
            return data.json()[0]['sticker_pack']['stickers']
        else:
            return None

    def sendSticker(self, channelId, stickerId):
        data = requests.post(f'https://discord.com/api/v8/channels/{channelId}/messages', json={'content': '', 'nonce': '', 'tts': False, 'sticker_ids': [ stickerId ]}, headers=self.headers)
        if data.status_code == 200:
            print(f'[{Fore.CYAN}Sticker Assult{Fore.RESET}] -> {Fore.GREEN}Success{Fore.RESET} : Sent a message')
        elif data.json() and data.json()['retry_after']:
            print(f'[{Fore.CYAN}Sticker Assult{Fore.RESET}] -> {Fore.RED}Error{Fore.RESET} : Rate limited stopping...')
            input("Just input any key to closeee")
            exit(0)
            
if __name__ == "__main__":
    print(f'[{Fore.CYAN}Sticker Assult{Fore.RESET}] -> {Fore.MAGENTA}Token{Fore.RESET} : ', end='')
    token = input()
    print(f'[{Fore.CYAN}Sticker Assult{Fore.RESET}] -> {Fore.MAGENTA}Channel Id{Fore.RESET} : ', end='')
    channelId = input()
    # Spammer Bottom
    assulter = StickerAssult(token, channelId)
    for sticker in assulter.getStickersFromPacks():
        assulter.sendSticker(channelId, sticker['id'])
