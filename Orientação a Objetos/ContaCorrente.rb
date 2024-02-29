class conta_corrente
    def initialize(number, extract)
        @conta = number.to_i
        @extrato = extract.to_f
    end

    # Metodo para realizar deposito em uma conta corrente
    def depositar(valor)
        if valor > 0
            @conta += valor
            puts "o valor foi depositado com sucesso"
        elsif valor  <= 0
            puts "O valor deve ser maior que zero."
    end

    # Metodo para realizar saque em uma conta
    def sacar(valor)
        if valor  <= @conta && valor > 0
            @conta -= valor
            puts "saque realizado com sucesso"
        elsif valor > @conta || valor <= 0
            puts "Valor indisponivel ou invalido."
    end
end
