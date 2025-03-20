require 'bank_controler'
require 'sqlite3'

# Insert data into the table
db.execute "INSERT INTO users (nome, saldo) VALUES (?, ?)", ['John Doe', '1337']
db.execute "INSERT INTO users (nome, saldo) VALUES (?, ?)", ['Jane Doe', '2275']
