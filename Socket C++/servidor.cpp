#include <iostream>

 #include "ServerSocket.h"
  #include "SocketException.h"

using namespace std;


//Processo seguido:

// Servidor: Estabiliza o modo ouvinte, aguardando a conex�o com um processo cliente
// Cliente: Cria um socket e tenta conectar-se com um servidor
// Servidor: Aceita uma conex�o cliente
// Cliente: Envia e recebe dados
// Servidor: Envia e recebe dados
// Cliente: Fecha conex�o
// Servidor: Fecha conex�o

