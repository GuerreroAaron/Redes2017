import xmlrpclib

class Cliente:
    var=''
    def crea(self,puerto=8000,mem='hola'):
        self.puerto=puerto
        self.s = xmlrpclib.ServerProxy('http://localhost:'+str(puerto))
        #lee el mesanje
        self.var=mem
    
    def respuesta(self):
        claro=self.s.men(self.var)
    
        #lo imprime
        return str(self.puerto) +' dice '+str(claro)+'\n'
    
#c=Cliente()        
#c.crea()
#print c.respuesta()
