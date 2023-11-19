#!/usr/bin/env ruby

require 'ascii_charts.rb'

puts "digite o valor do logaritimando: "
val = gets.chomp.to_f

puts "Digite o valor da base: "
bas = gets.chomp.to_f

if val > 0 && val != 1;

  res = Math.log(val, bas)
  puts "o logarítmo de #{val}, na base #{bas}, é:  #{res}"

else
  puts "digite valores válidos !"
end

puts AsciiCharts::Cartesian.new([[0,1],[1,3],[2,7],[2.5,12],[3,15]]).draw
