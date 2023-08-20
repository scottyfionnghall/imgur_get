from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

client = ImgurClient(client_id, client_secret)
url = input('Please enter Imgur post URL:\n')
# cannot use strip becasue it acts weird here
album_id = url[20:]

try:
    imgs = client.get_album_images(album_id)
except ImgurClientError:
    print('Invalid Link')
else:
    text = []
    for img in imgs:
        text.append(f'![]({img.link})')
    path = Path('output.md')
    path.write_text('\n'.join(text))
