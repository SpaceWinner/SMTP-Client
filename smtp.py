import socket
import ssl
import base64

image = base64.b64encode(open('apple.png', 'rb').read())

def send_recv(string, socket):
    string += b'\n'
    socket.send(string)
    return socket.recv(1024).decode(encoding='utf-8')

def create(txt):
    return b'''From: ivanugriumov@yandex.ru
To: ivanugriumov@yandex.ru
Subject: Test_message1
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="----==--bound.217241.web41g.yandex.ru"

--bound.217241.web41g.yandex.ru
Content-Type: text/plain;

Some txt
--bound.217241.web41g.yandex.ru

Content-Disposition: attachment;
	filename="apple.png"
Content-Transfer-Encoding: base64
Content-Type: image/png; name="apple.png"


''' + image + b'\n --bound.217241.web41g.yandex.ru-- \n.'



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s = ssl.wrap_socket(s)
    s.connect(('smtp.yandex.ru', 465))
    print(s.recv(1024))
    login = base64.b64encode(b'ivanugriumov@yandex.ru')
    password = base64.b64encode(b'alinor99')
    print(send_recv(b'EHLO ivanugriumov@yandex.ru', s))
    print(send_recv(b'AUTH LOGIN', s))
    print(send_recv(login, s))
    print(send_recv(password, s))
    print(send_recv(b'MAIL FROM: ivanugriumov@yandex.ru', s))
    print(send_recv(b'RCPT TO: ivanugriumov@yandex.ru', s))
    print(send_recv(b'DATA', s))
    print(send_recv(create(b'Some text'), s))
