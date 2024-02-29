## exemplo em python:

##class Pessoa:
##   def __init__(self, nome, sobrenome, ano_nasc):
##        self.nome = nome
##        self.sobrenome = sobrenome
##        self.ano_nasc = ano_nasc
##    end
##   def nome_completo(self):
##        return ...
##    end
##    def idade(self):
##        return ...
##    end
## end
 
## implantação em ruby:
require Date

class Person
    def initialize(name, nickname, year_born)
        @name = name.to_s
        @nickname = nickname.to_s
        @year_born = year_born.to_i
    end
    
    def full_name
        return "#{@name} #{@nickname}"
    end
    
    def year_old
        return DateTime.now.year - @year_born
    end
end