from socket import *


def create_server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    try:
        # disponibilzando a porta 9000 pra receber sockets
        server_socket.bind(('localhost', 9000))

        # setando pro s.o. que ele pode enfileirar ate 5 sockets que estão fazendo requisições pro server
        server_socket.listen(5)
        while(1):
            # aceitando a conexão
            (client_socket, address) = server_socket.accept()

            # o http sabe que eh o client-side que manda a primeira requisicao, por isso, devemos recebe-la
            rd = client_socket.recv(5000).decode()
            pieces = rd.split('\n')
            if len(pieces) > 0: print(pieces[0])

            data = 'HTTP/1.1 200 OK\r\n'
            data += 'Content-Type: text/html; charset=utf-8\r\n'
            data += '\r\n'
            data += '<html><body>Hello World</body></html>\r\n\r\n'
            client_socket.sendall(data.encode())
            client_socket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print('Shutting down...\n')
    except Exception as exp:
        print(f'Error: \n\n{exp}')

    server_socket.close()


print('Access http://localhost:9000')
create_server()
