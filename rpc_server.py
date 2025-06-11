from xmlrpc.server import SimpleXMLRPCServer

def square(n):
    return n * n

server = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor RPC en espera en el puerto 8000...")
server.register_function(square, "square")
server.serve_forever()
