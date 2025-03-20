class Team
  attr_reader :nome, :team_mate, :lider

  def initialize(nome, lider)
    @nome = nome
    @lider = lider
    @team_mate = Array.new
  end

  def adicionar_membro(membro)
    @team_mate << membro
  end

  def who
    puts "o time se chama #{@nome} liderado por #{@lider} e seus membros são: "
    integrantes
  end

  private
  def integrantes
    @team_mate.each do |team_mate|
      puts "nome: #{team_mate.nome}, idade: #{team_mate.idade}, arcanas: #{team_mate.arcana}"
    end
  end
end
