# -*- coding: utf-8 -*-
import os
import time
import threading
import socket

#Clase con el hilo para atender los clientes
class Servidor(threading.Thread):
	#Creamos el constructor padre de tal forma que se inicialice 
	#correctamente la clase thread, usamos como argumentos:
	#self: permite acceder a las propiedades y metodo de un objeto
	
	def __init__(self,addr,datos,servidor):
		threading.Thread.__init__(self)
		#Guardamos los paraetros en las variablas del objeto creado
		self.datos = addr
		self.mensaje = datos
		self.servidor = servidor

	#Metodo run que atiende las peticiones de cada cliente que entra en un hilo
	def run(self):
	

			
			# LEitura dos arquivos da pasta 
                        nomesArq = os.listdir('/home/vm/Documentos/UDP/UDPServerDados/')
    
                        cont=1
                        arquivos=''
                        for nom in nomesArq:
                            arquivos=arquivos+str(cont)+" - "+str(nom)+"\n"    
	                    cont = cont+1	
                        self.servidor.sendto(arquivos,self.datos)                     
			print ("Leitura da pasta",str(nomesArq))
                        print ("Envio dos dados da pasta",arquivos)
                        # Envia a quantidade de arquivos para o cliente
                        tamlista = len(nomesArq)
			self.servidor.sendto(str(tamlista),self.datos)
			print("Envio do tamanho da lista",str(tamlista))
                        # print ("Enviei a quantidade de arquivos para o cliente",str(len(nomesArq)))

                        # Recebe do cliente a resposta se ele deseja ou nao fazer download de algum arquivo
                        decisaodownload , addr = servidor.recvfrom(8)
			time.sleep(1)
			decisaodownload = str(decisaodownload)
			print("Recebi a decisao do download",decisaodownload)
			print("addr",addr,type(addr))
                        if decisaodownload == 's':
                            # Recebe o numero do download que o cliente deseja fazer 
                            print('#####################################################################################################')
			    ndownload,addr = servidor.recvfrom(1024)
			    print("Recebi numero do download para verificar se e valido ou nao",str(ndownload))
                            ndownload = int(ndownload)-1
			    
    
                            # Verifica se o download e valido ou nao
                            if (ndownload >= 0 and ndownload < cont):			
				nomeArqEnvio = nomesArq[ndownload]
				print("EEUUU"+nomeArqEnvio, "nomesArqType"+type(nomesArq[ndownload]))
	                        self.servidor.sendto(str(nomesArq[ndownload]),self.datos)
                                print("Enviei o nome do arquivo a ser feito o download para o cliente",str(nomesArq[ndownload]))
        
                                # Diretorio do arquivo a ser enviado para o servidor
                                download = open('/home/vm/Documentos/UDP/UDPServerDados/'+str(nomesArq[ndownload]), "r")
	                        # download = open('/home/vm/Documentos/dados/clienteteste.py','r')
                                print("nDownload", str(ndownload))
                                print ("Vou tentar enviar o arquivo que o cliente pediu!")
        
                                # Envia o arquivo  a ser salvo
	                        for i in download:
	                            self.servidor.sendto(i,self.datos)
	        		    print(str(i))
                                self.servidor.sendto('concluso',self.datos)
                                download.close()
                                print ("Arquivo solicitado: "+ "/home/vm/Documentos/UDP/UDPServerDados/"+str(nomesArq[ndownload]) )
	                        print ("Terminei de enviar o arquivo que o cliente pediu!")

                        # s armazena a resposta do cliente se quer ou nao gravar um novo arquivo
                        '''s, addr = servidor.recvfrom(1024)
			s = str(s)                        
			# Verifica se vai haver gravacao de um novo arquivo ou nao
                        # print ("Verfica decisao")
                        if s == 's':   
                            # Nome do arquivo a ser salvo
	                    nome, addr=servidor.recvfrom(1024)
                            print ("Nome do arquivo a ser enviado ao servidor:"+str(nome))
	                    # Lugar onde vai ser colocado o arquivo recebido
	                    arq = open('/home/vm/Documentos/UDP/UDPServerDados/'+nome, 'w')
	                    # Recebendo o novo arquivo
	                    while True:
                                print ("Recebendo novo arquivo")
	                        dados, addr = servidor.recvfrom(1024)
                                if not dados: break
                                arq.write(dados)
	                    arq.close()
                            print ("Arquivo Recebido com sucesso!")'''
			print "O cliente:  " + str(self.datos) + "  Foi atendido."


#######################    MODULO PRINCIPAL  ############################
if __name__ == '__main__':
	
	try:
		#Creamos el socket tipo TCP
		servidor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		servidor.bind(('127.0.0.1',5115))
		print "Foi estabelecido a conexão com um socket UDP MultiThread '-'"

		#Creamos un bucle para asignar un hilo a cada cliente que se conecte
		while True:
			print "\nServidor Disponível........"
			#Esperamos una conexion 
			datos, addr = servidor.recvfrom(1024)
			#se crea el hilo por cada conexion entrante
			hilo = Servidor(addr,datos,servidor)
			hilo.start()
			
	except KeyboardInterrupt:
		print "Serviço Finalizado..........\n"
			
	

