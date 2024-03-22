function validar() {
    const nome = document.getElementById('name').value;
    const valName = nome.value.length;
    const error = document.getElementsByClassName('error');

    if (valName == 0) {
        error[0].inerHTML = "o campo nome é obrigatório";
    }
    else {
        error[0].innerHTML = '';
    }   
}