puts "digite o valor do logaritimando: "
val = gets.chomp.to_f

puts "Digite o valor da base: "
bas = gets.chomp.to_f

if val > 0 && val != 1;
  res = Math.log(val, bas)
  puts res

else
  puts "digite valores válidos!"
end
