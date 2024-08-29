from flask import Flask , jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests


def synx(v):
        url = f'https://images.search.yahoo.com/search/images;_ylt=AwrO_FdQi6NmDbAQsIyLuLkF;_ylu=c2VjA3NlYXJjaARzbGsDYnV0dG9u;_ylc=X0kDTlNOYnZqRXlOeTdzenNlcFpuMGtrQUpwTWpRd09RQUFBQUQ4aDRvUARfUwM5NjA1NzQ4MwRfcgMyBGNzcmNwdmlkA05TTmJ2akV5Tnk3c3pzZXBabjBra0FKcE1qUXdPUUFBQUFEOGg0b1AEZnIDBGZyMgNzYi10b3AEZ3ByaWQDBG5fcnNsdAMwBG5fc3VnZwMwBG9yaWdpbgNpbWFnZXMuc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAzAEcXN0cmwDNgRxdWVyeQNnb29nbGUEdF9zdG1wAzE3MjE5OTQwNjcEdnRlc3RpZANTUFIyNDI3LURJTVQ-?p={v}&ei=&iscqry=&fr=&fr2=sb-top'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
        }

        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.content, 'lxml')

        link = soup.find_all('img')
        gr = [i.get('src') for i in link]
    
        return gr

app = Flask(__name__)
CORS(app)

@app.route('/data/<image>')
def going_for_images(image):
    structure ={
        'result':synx(image)
    }
    return jsonify(structure)
