require_relative 'user'

class Persona < User
 attr_reader :local, :nivel

  def initialize(local, nivel)
    super(nome, idade, arcana)
    @local = local
    @nivel = nivel
  end

  # def evoker(nome, arcana, nivel)

  # end
end
