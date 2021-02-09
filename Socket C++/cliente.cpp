#include <iostream>

#include "ClientSocket.h"
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




int main ( int argc, int argv[] )
  {
  try
  {
  // Criando um client socket e solicitando a conex�o na porta 30000 e IP local.
  ClientSocket client_socket ( "localhost", 30000 );
  
  std::string reply;
  try
  {
  // Envia a string "Test message" ao server
  client_socket << "Test message.";
  
  // Recebe dados do server
  client_socket >> reply;
  std::cout< catch ( SocketException& ) {}
  
  }
  catch ( SocketException& e )
  {
  std::cout << "Excec�o foi capturada:" << e.description() << " ";
  }
  
  return 0;
  }