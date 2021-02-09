#include <iostream>

#include "ClientSocket.h"
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




int main ( int argc, int argv[] )
  {
  try
  {
  // Criando um client socket e solicitando a conexão na porta 30000 e IP local.
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
  std::cout << "Excecão foi capturada:" << e.description() << " ";
  }
  
  return 0;
  }