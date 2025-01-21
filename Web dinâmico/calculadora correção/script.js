function ConverterReal() {
  var valorElementoEuro = document.getElementById("euro");
  var valorEuro = valorElementoEuro.value;
  var valorEuro = parseFloat(valor);
  var valorEmReal = valorEuro * 5.40;
  var elementoValorConvertido = document.getElementById("valorConvertido")
  var valorConvertido = "o valor em R$ é" +  valorEmReal;
  elementoValorConvertido.innerHTML = valorConvertido;
}
var valorEmDolar = valorEuro * 1.09;