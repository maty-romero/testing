#imports
import socket
import threading
import time

class Nodo():
    def __init__(self):
        self.host = socket.gethostbyname(socket.gethostname())
        self.puerto_local = 9090
        self.escuchando=False
        self.hilo_escucha = None
        self.hilo_heartbeat  = None
        self.socket_local = None
        self.conexion = None
        
    def iniciar_socket(self):
        """Permite inicializar el socket"""
        try:
            self.socket_local  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket_local.bind((self.host, self.puerto_local))
            self.socket_local.listen()
            self.escuchando = True
            print(f"Servidor escuchando en {self.host}:{self.puerto_local}")
            self.hilo_escucha = threading.Thread(target=self.escuchar, daemon=True).start()
            self.hilo_heartbeat = threading.Thread(target=self._enviar_heartbeat, daemon=True)
        except Exception as e:
            print(f"Error al iniciar el manejador de socket: {e}")
            self._escuchando = False
            if self.socket_local:
                self.cerrar()
                self.socket_local = None

    def escuchar(self):
        while self.escuchando:
            self.conexion, addr = self.socket_local.accept()
            print(f"Se registro una conexion desde {addr}")
            


    def cerrar(self):
        """cierra el socket que se habia iniciado"""
        print("Cerrando manejador de socket...")
        self._escuchando = False

        with self.lock:
            if self.socket_local:
                try:
                    self.socket_local.shutdown(socket.SHUT_RDWR)
                    self.socket_local.close()
                except Exception as e:
                    print(f"Error al cerrar socket principal: {e}")
                finally:
                    self.socket = None


if __name__ == "__main__":

    

    #abrir un puerto socket
    
    
    #ejecutar nodo y comunicarse con el siguiente


    pass