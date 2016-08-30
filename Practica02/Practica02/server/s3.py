from SimpleXMLRPCServer import SimpleXMLRPCServer

class MyFuncs:
    def men(self, x):
        return x 

# Funcion server
class FuncionS():
    
    def abre(self,puerto=8000):
        self.server = SimpleXMLRPCServer(("localhost", puerto))
        self.server.register_instance(MyFuncs())
        self.server.serve_forever()

    def cerrar(self):
        self.server.shutdown()
        self.server.server_close()
        
        
#ser=FuncionS() 
#ser.abre()
