exchange = int(input())

five_hundreds, exchange = divmod(exchange, 500)
hundred, exchange = divmod(exchange, 100)
fifty, exchange = divmod(exchange, 50)
ten, exchange = divmod(exchange, 10)

print(five_hundreds + hundred + fifty + ten)
