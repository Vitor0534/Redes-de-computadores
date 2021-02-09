# -*- coding: utf-8 -*-
import os
import socket
import time
import thread

HOST = '127.0.0.1'              # Endereco IP do Servidor
PORT = 3333            # Porta que o Servidor esta

def conectado(con, cliente):
    print 'Conectado por', cliente

    while True:
        # LEitura dos arquivos da pasta
        nomesArq = os.listdir('/home/vm/Documentos/TCP/TCPServerDados')
    
        cont=1
        arquivos=''
        for nom in nomesArq:
            arquivos=arquivos+str(cont)+" - "+str(nom)+"\n"    
	    cont = cont+1	
        con.send(arquivos)
        print ("Leitura da pasta",str(nomesArq))
        print ("Envio dos dados da pasta",arquivos)
        # Envia a quantidade de arquivos para o cliente
        con.send(str(len(nomesArq)))
        # print ("Enviei a quantidade de arquivos para o cliente",str(len(nomesArq)))

        # Recebe do cliente a resposta se ele deseja ou nao fazer download de algum arquivo
        decisaodownload=con.recv(1024)

        if decisaodownload == 's':
            # Recebe o numero do download que o cliente deseja fazer 
            ndownload = int(con.recv(1024))-1
            print("Recebi numero do download para verificar se e valido ou nao",str(ndownload))
    
            # Verifica se o download e valido ou nao
            if (ndownload >= 0 and ndownload < cont):
	        con.send(str(nomesArq[ndownload]))
                print("Enviei o nome do arquivo a ser feito o download para o cliente",str(nomesArq[ndownload]))
        
                # Diretorio do arquivo a ser enviado para o servidor
                download = open('/home/vm/Documentos/TCP/TCPServerDados/'+str(nomesArq[ndownload]), "r")
	        # download = open('/home/vm/Documentos/dados/clienteteste.py','r')
                print("nDownload", str(ndownload))
                print ("Vou tentar enviar o arquivo que o cliente pediu!")
        
                # Envia o arquivo  a ser salvo
	        for i in download:
	            con.send(i)
	        
                time.sleep(3)
                con.send('concluso')
                download.close()
                # con.send('concluso')
                print ("Arquivo solicitado: "+ "/home/vm/Documentos/TCP/TCPServerDados/"+str(nomesArq[ndownload]) )
	        print ("Terminei de enviar o arquivo que o cliente pediu!")

        # s armazena a resposta do cliente se quer ou nao gravar um novo arquivo
        s = str(con.recv(1024))
        # Verifica se vai haver gravacao de um novo arquivo ou nao
        # print ("Verfica decisao")
        if s == 's':   
            # Nome do arquivo a ser salvo
	    nome=con.recv(1024)
            print ("Nome do arquivo a ser enviado ao servidor:"+str(nome))
	    # Lugar onde vai ser colocado o arquivo recebido
	    arq = open('/home/vm/Documentos/TCP/TCPServerDados'+nome, 'w')
	    # Recebendo o novo arquivo
	    while True:
                print ("Recebendo novo arquivo")
	        dados = con.recv(1024)
                if not dados: break
                arq.write(dados)
	    arq.close()
            print ("Arquivo Recebido com sucesso!")
        con.close()
        print ('Finalizado conexao do cliente', cliente)
        thread.exit()
        print ('Saiu da thread')

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    thread.start_new_thread(conectado, tuple([con, cliente]))

tcp.close()
