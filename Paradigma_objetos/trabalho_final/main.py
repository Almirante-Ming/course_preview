from robo import Robo, RoboLutador, RoboMedico
 


rl1= RoboLutador('atom')
rl2= RoboLutador('zeus')
rm1= RoboMedico('house')

print(rl1)
print(rl2)

c1=rl1.atacar(rl2)
r2=rm1.curar(rl1)
c2=rl2.atacar(rm1)
s1 = rl1 + rl2

print(c1)
print(r2)
print(c2)
print(s1)

