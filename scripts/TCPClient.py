import socket
import sys
import time

TAM_PCKG = 1024

MSG_AJUDA  = "\nComandos disponiveis:\n"
MSG_AJUDA += "\tpython TCPClienteEnviarImagens.py enviar <caminho da imagem>\n"
MSG_AJUDA += "\tpython TCPClienteEnviarImagens.py ajuda\n"

s = socket.socket()
servidor = "192.0.2.10"
porta = 50000

s.connect((servidor, porta))

if len(sys.argv) == 3:
  comando = sys.argv[1]
  caminho = sys.argv[2]
  arquivo = caminho.split('/')[-1]
  
  if comando == 'enviar':
    print "Enviando arquivo: ", arquivo    
 
    s.send(arquivo.split('/')[-1])

    f = open(caminho,'rb')
    l = f.read(TAM_PCKG)
    while (l):
      s.send(l)
      print 'Enviando...'
      l = f.read(TAM_PCKG)
    f.close()
  else:
    print(MSG_AJUDA)
else:
  print(MSG_AJUDA)

s.close()
print "Conexao fechada."