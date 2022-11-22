import xmlrpc.client

proxy=xmlrpc.client.ServerProxy("http://localhost:6789")

num1=10
num2=20
result=proxy.add(num1,num2)
print("result is",result)

