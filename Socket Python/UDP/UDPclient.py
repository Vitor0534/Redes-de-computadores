# -*- coding: utf-8 -*-
import os
import time
#import socket module
import socket
#create socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverAddr = (('127.0.0.1',5115))
'''
############################################################################################################

print "digite nombre de la pagina"
#filename = raw_input(">>>> ")
#Envio los datos al servidor HTTP
client.sendto('127.0.0.1',serverAddr)
#Espero respuesta del servidor
# message, addrServer = client.recv(1024)
arq = open('/home/vm/Documentos/DownloadsSocket/grande.jpg', 'w')
    # Recebendo o novo arquivo
while True:
    dados, addrServer = client.recvfrom(1024)
    if str(dados)=='concluso':
	 break
    arq.write(dados)
print("recebi a imagem.")	
#dados, addrServer = client.recvfrom(400000)
arq.write(dados)
arq.close()
#receive and print webpage
############################################################################################################'''



client.sendto('127.0.0.1',serverAddr)
# Recebe a informacao sobre os arquivos do servidor
dados, addrServer = client.recvfrom(1024)
print ("Recebi todos os dados")
dados = str(dados)
print (dados)
# print ("Recebi todos os dados")
# Recebe a quantidade de arquivos que tem no servidor
tamdados, addrServer = client.recvfrom(1024)
tamdados = int(tamdados)
# Verifica se o cliente quer fazer download de algum arquivo
print ("Caso queira fazer download tecle [s] para sim: ")
decisaodownload = str(raw_input())
# Envia para o servidor se o cliente vai ou nao fazer download
print("decisaodownload", decisaodownload)
client.sendto('s',serverAddr)
time.sleep(1)
if decisaodownload == 's':
    print ("Digite o numero correspondente para o download!")
    ndownload = int(raw_input())
    # Envia o numero do download desejado a o servidor
    client.sendto(str(ndownload), serverAddr)
    print ("Enviei o numero do download para o servidor", str(ndownload))
  
    # Recebe o nome do download
    nomedownload, addrServer = client.recvfrom(1024)
    print("O nome para download"+str(nomedownload))
    nomedownload = str(nomedownload)
    if ndownload >= 0 and ndownload <= tamdados:
        # print ("Entrei no if de que tem dados para receber")
        # Recebe o arquivo do servidor
        print ('/home/vm/Documentos/arquivosbaixados/',nomedownload)
        download = open('/home/vm/Documentos/DownloadsSocket/'+nomedownload, 'w')
        # download = open('/home/vm/Documentos/arquivosbaixados/teste.py', 'w')

        # Recebendo o novo arquivo
        print ("Comecei a receber o arquivo")
        while True:
            # print ("Recebendo novo arquivo")
            line, addrServer = client.recvfrom(1024)       
            if str(line)=='concluso': break
            #if str() == '\n' : break 
            download.write(line)
        download.close()
        print ("Arquivo recebido com sucesso!")


'''
print ("Deseja encaminha um novo arquivo para o servidor ? digite s para sim.")
# Deciso para o servidor saber se vai haver gravacao de um novo arquivo
decisao = raw_input()


# Encaminha decisao ao servidor
# print("Enviou a decisao")
client.sendto(decisao,serverAddr)

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
                client.sendto(nome,serverAddr)
		# Diretorio do arquivo a ser enviado para o servidor
		arq = open(caminho, "r")
                # Envia o arquivo  a ser salvo
		for i in arq.readlines():    
		    client.sendto(i,serverAddr)
		arq.close()
		print ("Arquivo enviado com sucesso!")'''
print("Conexão Finalizada")




