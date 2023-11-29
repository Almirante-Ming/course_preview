#!/usr/bin/env ruby
require 'ascii_charts'

#coleta de variáveis
puts "digite o valor da frequencia de referência (f⁰), ou pressione enter para usar o padrão: "
f0 = gets.chomp.to_f

puts "Digite o valor do tom de referência (p⁰), ou pressione enter para usar o valor padrão: "
p0 = gets.chomp.to_f

puts "Digite a frequência desejada: "
f = gets.chomp.to_f


  def calc_pitch(f, f0=1, p0=1)
    p=p0+12*Math.log2(f/f0)
    return p
  end

  # imprimir o gráfico

  ## draw p=p0+12*Math.log2(f/f0) for 0 <= x < 3000
puts AsciiCharts::Cartesian.new((0...3000).to_a.map{|x| [x, calc_pitch(f, f0, p0)]}, :title => 'p=p0+12*Math.log2(f/f0)').draw
# puts AsciiCharts::Cartesian.new([[0,1],[1,3],[2,7],[2.5,12],[3,15]]).draw
