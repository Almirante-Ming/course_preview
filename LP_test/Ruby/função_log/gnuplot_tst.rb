require 'gnuplot'

#calcula a oitava usando uma notade referência
def calc_pitch(f, f0=1, p0=0)
 pitch = p0 + 12 * Math.log2(f / f0)
end

# coleta os dados nescessários
puts "Digite a frequência desejada: "
f = gets.chomp.to_f
puts "digite o valor da frequencia de referência (f⁰), ou pressione enter para usar o valor padrão: "
f0 = gets.chomp.to_f
puts "Digite o valor do tom de referência (p⁰), ou pressione enter para usar o valor padrão: "
p0 = gets.chomp.to_f

# Frequency values for x-axis
x = (200..1000).step(50).to_a

# Function values for y-axis
y = x.map { |f| calc_pitch(f, f0, p0) }

Gnuplot.open do |gp|
 Gnuplot::Plot.new(gp) do |plot|
    plot.xrange "[200:1000]"
    plot.yrange "[41:108]"
    plot.title "Pitch per Frequency"
    plot.xlabel "Frequency (Hz)"
    plot.ylabel "Pitch (s)"

    plot.data << Gnuplot::DataSet.new([x, y]) do |ds|
      ds.with "lines"
      ds.notitle
    end
 end
end
