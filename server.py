import xmlrpc.server

with xmlrpc.server.SimpleXMLRPCServer(("localhost", 9000)) as server:

    # Server functions
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    # Makes functions accessible to the client
    server.register_function(add, "add")
    server.register_function(subtract, "subtract")
    server.register_function(multiply, "multiply")
    server.register_function(divide, "divide")

    server.serve_forever()
