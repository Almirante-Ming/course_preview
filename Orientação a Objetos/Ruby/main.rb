require_relative 'models/user'
require_relative 'models/persona'
require_relative 'models/team'

u1= User.new('Makoto Yuki', 17, 'Fool')
u2= User.new('Mitsuru Kirijo', 18, 'Empress')
u3= User.new('Akihiko Sanada', 18, 'Emperor')
u4= User.new('Yukari Takeba', 17, 'Lovers')
u5= User.new('Junpei Iori', 17, 'Magician')

t1= Team.new('S.E.E.S.', u1.nome)
t1.adicionar_membro([u2, u3, u4, u5])

# puts t1.membros
t1.who
