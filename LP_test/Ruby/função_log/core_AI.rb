require 'ascii_charts'
import 'calc_pitch'

# coleta as variáveis
puts "Digite a frequência desejada: "
f = gets.chomp.to_f
puts "digite o valor da frequencia de referência (f⁰), ou pressione enter para usar o padrão: "
f0 = gets.chomp.to_f
puts "Digite o valor do tom de referência (p⁰), ou pressione enter para usar o valor padrão: "
p0 = gets.chomp.to_f

#cria a variável "graph e define uma função para ela"
graph = calc_pitch(f, f0, p0)

#define um array com os valores que serão usados no gráfico
data = (0...10).to_a.map { |x| [x, graph] }

#cria o gráfico
chart = AsciiCharts::Cartesian.new(data, title: 'y = e^x')
puts chart.draw
