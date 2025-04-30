# There are the libraries for the project

import socket
import threading
import os
import numpy as np
import pandas as pd
import hashlib

#There is the space for the definition of the class, in this case, CentralServer

import socket


class CentralServer :
    def __init__(self, ip_address, max_clients, db_paths, port=5050) :
        self.ip_address = ip_address
        self.port = port
        self.max_clients = max_clients
        self.db_paths = db_paths  # Se esperan 9 bases de datos

        self.connected_clients = 0
        self.server_socket = None
        self.is_running = False

    def start_server(self) :
        """Inicializa el servidor y comienza a escuchar en la IP y puerto."""
        if self.is_running :
            print ( "Server already running." )
            return

        self.server_socket = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
        self.server_socket.bind ( (self.ip_address, self.port) )
        self.server_socket.listen ( self.max_clients )

        self.is_running = True
        print ( f"Server started on {self.ip_address}:{self.port}. Waiting for connections..." )

    def accept_connections(self) :
        """Acepta conexiones de clientes hasta el máximo permitido."""
        while self.connected_clients < self.max_clients and self.is_running :
            client_socket, client_address = self.server_socket.accept ()
            print ( f"Client {client_address} connected." )
            if self.validate_client_identity ( client_socket ) :
                self.connected_clients += 1
                print ( f"Client {client_address} authenticated successfully." )
                self.handle_client ( client_socket )
            else :
                print ( f"Client {client_address} failed authentication." )
                client_socket.close ()

    def validate_client_identity(self, client_socket) :
        """Método para validar la identidad de un cliente (por ejemplo, usuario y contraseña)."""
        # En este ejemplo, simplemente simulamos que todo cliente es válido.
        client_socket.send ( b"Please send your credentials." )
        credentials = client_socket.recv ( 1024 ).decode ( "utf-8" )
        # Aquí iría la validación de las credenciales (esto es solo un ejemplo).
        if credentials == "valid_user:password" :
            client_socket.send ( b"Authentication successful." )
            return True
        else :
            client_socket.send ( b"Authentication failed." )
            return False

    def handle_client(self, client_socket) :
        """Recibe instrucciones del cliente y responde según sea necesario."""
        while self.is_running :
            data = self.receive_instruction ( client_socket )
            if data :
                print ( f"Received: {data}" )
                response = f"Processed: {data}"
                self.send_instruction ( client_socket, response )
            else :
                break  # Si no se recibe nada, cerramos la conexión.

    def receive_instruction(self, client_socket) :
        """Recibe instrucciones del cliente."""
        try :
            data = client_socket.recv ( 1024 ).decode ( "utf-8" )
            if not data :
                return None
            return data
        except Exception as e :
            print ( f"Error receiving data: {e}" )
            return None

    def send_instruction(self, client_socket, data) :
        """Envía respuestas al cliente."""
        try :
            client_socket.send ( data.encode ( "utf-8" ) )
        except Exception as e :
            print ( f"Error sending data: {e}" )

    def stop_server(self) :
        """Detiene el servidor y cierra todas las conexiones."""
        self.is_running = False
        if self.server_socket :
            self.server_socket.close ()
            print ( "Server stopped." )
