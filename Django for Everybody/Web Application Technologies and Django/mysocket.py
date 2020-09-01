import socket

# o socket é como se fosse um arquivo/endpoint dentro do pc que pode requisitar receber informações da web
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# Fazemos a requisicao e deixamos uma linha em branco pra indicar que não há headers na requisicao
# encode() = comprimindo a string no formato UTF-8
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    # faz o python receber os próximos 512 caracteres
    data = mysock.recv(512)
    if len(data) < 1:
        break

    # decode = convertendo string UTF8 para string Unicode (a string "normal")
    print(data.decode(), end=' ')

mysock.close()