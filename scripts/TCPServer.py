import socket
import os
import time

TAM_PCKG = 1024
CAMINHO  = '/home/ipv6br/imagens_turma3/'
PORTA    = 50000
HOST     = "192.0.2.10"

s = socket.socket()
s.bind((HOST, PORTA))
s.listen(5)

print 'Servidor pronto.'

while True:
    conn, addr = s.accept()
    print 'Conectado em ', addr

    arquivo = conn.recv(TAM_PCKG)

    if len(arquivo) == 0:
      arquivo = 'semnome.png'

    print "> ", arquivo

    dados = conn.recv(TAM_PCKG)
    with open(CAMINHO + arquivo, 'wb') as f:
        print 'Imagem aberta.'
        while len(dados) > 0:
            print 'Recebendo dados...'
            f.write(dados)
            dados = conn.recv(TAM_PCKG)
    f.close()
    conn.close()