require 'sqlite3'
#criar um banco de dados
db = SQLite3::Database.new "test.db"

#criar uma tabela para guardar os valores
db.execute <<-SQL
  CREATE TABLE IF NOT EXISTS extrato (
    nome TEXT NOT NULL UNIQUE,
    saldo INT NOT NULL
  );
SQL
