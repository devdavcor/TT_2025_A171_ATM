import socket
import threading
import os
import numpy as np
import pandas as pd
import hashlib


class CentralServer :
    def __init__(self, ip_address, max_clients, db_paths, port=5050) :
        self.ip_address = ip_address
        self.port = port
        self.max_clients = max_clients
        self.db_paths = db_paths  # Se esperan 9 bases de datos

        self.connected_clients = 0
        self.server_socket = None
        self.is_running = False

        self.lock = threading.Lock ()
        self.users_df = pd.read_parquet (
            "C:\\Users\\devdavcor\\Documents\\tt\\TT_2025_A171_SC\\db\\sucursales.parquet" )

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

        accept_thread = threading.Thread ( target=self.accept_connections )
        accept_thread.start ()

    def stop_server(self) :
        """Detiene el servidor y cierra todas las conexiones."""
        self.is_running = False
        if self.server_socket :
            self.server_socket.close ()
            print ( "Server stopped." )

    def settings_server(self, ip_address, port, max_clients) :
        """Reconfigura el servidor con nueva IP, puerto y máximo de clientes."""
        print ( "Applying new server settings..." )
        if self.is_running :
            self.stop_server ()

        self.ip_address = ip_address
        self.port = port
        self.max_clients = max_clients

        self.start_server ()

    def branches(self) :
        """Mostrar información de sucursales."""
        pass

    def clients(self) :
        """Mostrar información de clientes conectados."""
        pass

    def logs(self) :
        """Mostrar logs del servidor."""
        pass

    def accept_connections(self) :
        """Acepta conexiones de clientes hasta el máximo permitido."""
        while self.is_running :
            try :
                client_socket, client_address = self.server_socket.accept ()
                print ( f"Client {client_address} connected." )
                client_thread = threading.Thread ( target=self.client_session, args=(client_socket, client_address) )
                client_thread.start ()
            except Exception as e :
                print ( f"Error accepting connections: {e}" )

    def client_session(self, client_socket, client_address) :
        """Hilo que maneja la autenticación y comunicación con un cliente."""
        authenticated = self.validate_client_identity ( client_socket )
        if authenticated :
            with self.lock :
                self.connected_clients += 1
            print ( f"Client {client_address} authenticated successfully." )
            self.handle_client ( client_socket )
        else :
            print ( f"Client {client_address} failed authentication." )
            client_socket.close ()

    def validate_client_identity(self, client_socket) :
        """Valida la identidad del cliente usando sucursales.parquet"""
        client_socket.send ( b"Please send your credentials in format 'username:password'." )
        credentials = client_socket.recv ( 1024 ).decode ( "utf-8" )

        try :
            username, password = credentials.split ( ":" )

            result = self.users_df.loc[self.users_df['user'] == username, 'password'].values
            if len ( result ) == 0 :
                client_socket.send ( b"Authentication failed. User not found." )
                return False

            stored_password = result[0]
            input_hash = hashlib.sha512 ( (username + password).encode () ).hexdigest ()
            stored_hash = hashlib.sha512 ( (username + stored_password).encode () ).hexdigest ()

            if input_hash == stored_hash :
                client_socket.send ( b"Authentication successful." )
                return True
            else :
                client_socket.send ( b"Authentication failed. Incorrect password." )
                return False

        except Exception as e :
            client_socket.send ( f"Authentication error: {e}".encode () )
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
        client_socket.close ()

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


# ⬇️ Iniciar servidor desde aquí si corres este archivo directamente
if __name__ == "__main__" :
    # Parámetros iniciales

    ip_address = "0.0.0.0"
    port = 5050
    max_clients = 3
    db_paths = []  # Si tienes más bases de datos, las puedes usar aquí

    server = CentralServer ( ip_address, max_clients, db_paths, port )
    server.start_server ()
    server.settings_server(ip_address, port, max_clients)
