# -*- coding: utf-8 -*-
import socket
import os
import time
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 3333            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

# Recebe a informacao sobre os arquivos do servidor
dados = str(tcp.recv(1024))
print (dados)
# print ("Recebi todos os dados")
# Recebe a quantidade de arquivos que tem no servidor
tamdados = (int(tcp.recv(1024)))
# print ("Recebi a quantidade de arquivos que tem no servidor",str(tamdados))


# Verifica se o cliente quer fazer download de algum arquivo
print ("Caso queira fazer download tecle [s] para sim:  \10")
decisaodownload =raw_input()

# Envia para o servidor se o cliente vai ou nao fazer download
tcp.send(decisaodownload)
if decisaodownload == 's':
    print ("Digite o numero correspondente para o download!")
    ndownload = int(raw_input())
    if ndownload:
        # Envia o numero do download desejado a o servidor
        tcp.send(str(ndownload))
        print ("Enviei o numero do download para o servidor", str(ndownload))
  
        # Recebe o nome do download
        nomedownload = str(tcp.recv(1024))

    if ndownload >= 0 and ndownload <= tamdados:
        # print ("Entrei no if de que tem dados para receber")
    
        # Recebe o arquivo do servidor
        # print ('/home/vm/Documentos/arquivosbaixados/',nomedownload)
        download = open('/home/vm/Documentos/DownloadsSocket/'+nomedownload, 'w')
        # download = open('/home/vm/Documentos/arquivosbaixados/teste.py', 'w')

        # Recebendo o novo arquivo
        print ("Comecei a receber o arquivo")
        while True:
            # print ("Recebendo novo arquivo")
            line = tcp.recv(1024)       
            if str(line)=='concluso': break
            #if str() == '\n' : break 
            download.write(line)
        download.close()
        print ("Arquivo recebido com sucesso!")



print ("Deseja encaminha um novo arquivo para o servidor ? digite s para sim.")
# Deciso para o servidor saber se vai haver gravacao de um novo arquivo
decisao = raw_input()


# Encaminha decisao ao servidor
print("Enviou a decisao")
tcp.send(decisao)

if decisao == 's':
	# Entrada de Dados
	print "Digite o caminho do arquivo a ser enviado ao servidor"
	caminho = raw_input()
	print "Digite o nome do arquivo a ser enviado ao servidor"
	nome = raw_input()
	if caminho:
	    if nome:
		# Enviar o nome do arquivo a ser salvo
		print("Enviou o nome")
                tcp.send(nome)
		# Diretorio do arquivo a ser enviado para o servidor
		arq = open(caminho, "r")
                # Envia o arquivo  a ser salvo
		for i in arq.readlines():    
		    tcp.send(i)
		arq.close()
		print ("Arquivo enviado com sucesso!")
print("Conexão Finalizada")
tcp.close()
