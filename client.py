import xmlrpc.client

server_proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")

def main():
    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    add_result = server_proxy.add(a, b)
    sub_result = server_proxy.subtract(a, b)
    mul_result = server_proxy.multiply(a, b)
    div_result = server_proxy.divide(a, b)

    print(f"{a} + {b} = {add_result}")
    print(f"{a} - {b} = {sub_result}")
    print(f"{a} * {b} = {mul_result}")
    print(f"{a} / {b} = {div_result}")

if __name__ == "__main__":
    main()