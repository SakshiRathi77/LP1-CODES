from xmlrpc.server import SimpleXMLRPCServer
def add(num1,num2):
    return num1+num2

server=SimpleXMLRPCServer(("localhost",6789))
server.register_function(add,"add")
server.serve_forever()

