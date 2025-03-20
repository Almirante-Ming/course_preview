class User
  attr_reader :nome, :idade, :arcana

  def initialize(nome, idade, arcana)
    @nome = nome
    @idade = idade
    @arcana = arcana
  end
end
