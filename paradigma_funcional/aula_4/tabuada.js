
const numeros = [1,2,3,4,5,6,7,8,9,10];

tabuada = (fator) => {
    return fator * 2;
}

const novoArray = numeros.map(tabuada);
document.getElementById("demo").innerHTML = novoArray;