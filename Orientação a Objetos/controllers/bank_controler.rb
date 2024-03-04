
#criação da classe
class Cliente
  attr_accessor :saldo, :extrato

  def initialize(saldo, extrato)
    @saldo = saldo.to_i
    @extrato = estrato.to_f
  end

  #método para fazer saques
  def sacar(valor)
    if valor <= @saldo && valor > 0
      @saldo -= valor
      puts "Saque de #{valor} concluído, seu saldo atual é de #{@saldo} "
    else
      puts "Erro, confira o valor digitado e tente novamente"
    end
  end

  #metódo para depositar
  def depositar(valor)
    if valor > 0
      @saldo += valor
      puts "Depósito de #{valor} realizado com sucesso, saldo atual é de #{@saldo} "
    else
      puts "valor inválido, tente novamente"
    end
  end

  #método para verificar o extrato do cliente
  def extrato
    puts "Saldo atual: #{@saldo}"
    puts "----------------------"
    puts "Extrato:"
    puts "----------------------"

  end
end
