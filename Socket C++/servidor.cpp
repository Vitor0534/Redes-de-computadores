#include <iostream>

 #include "ServerSocket.h"
  #include "SocketException.h"

using namespace std;


//Processo seguido:

// Servidor: Estabiliza o modo ouvinte, aguardando a conexão com um processo cliente
// Cliente: Cria um socket e tenta conectar-se com um servidor
// Servidor: Aceita uma conexão cliente
// Cliente: Envia e recebe dados
// Servidor: Envia e recebe dados
// Cliente: Fecha conexão
// Servidor: Fecha conexão

