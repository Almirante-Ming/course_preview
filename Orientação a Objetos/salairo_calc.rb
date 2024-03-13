class funcionario:
    def initialize(nome, cargo, valor_hora)
        @nome=nome.to_s
        @cargo=cargo.to_s
        @valor_hora=valor_hora.to_f
        valor_hora=0
        salario=0
    end
    #registro de horas trabalhadas
    def reg_hr_trab(self)
        hora_trabalhada += 1
    end
    
    #calcular o salário
    def calc_salario(self)
        salario=valor_hora*hora_trabalhada
    end

