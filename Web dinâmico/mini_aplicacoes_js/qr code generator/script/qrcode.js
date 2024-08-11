const dark = document.querySelector('.dark');
const light = document.querySelector('.light');
const qr_text = document.querySelector('.QRtext');
const sizes = document.querySelector('.sizes');

dark.addEventListener('input', handleDarkCollor);
light.addEventListener('input', handleLightCollor);
qr_text.addEventListener('input', handleQR_Text);
sizes.addEventListener('change', handleSizes);

let colorDark = "#000"
let colorLight = "#fff"
let text = "https://ifms.edu.br"
let size = 300;

function handleDarkCollor(e) {
    colorDark = e.target.value;
}
function handleLightCollor(e) {
    colorLight = e.target.value;
}

function handleQR_Text(e) {
    text = e.target.value;
    if (!text) {
        text = defaultText;
    }
}

function handleSizes(e) {
    size = e.target.value;
    console.log(size);
}

function generateQRCode(){
    new QRCode('.qr_code', {
        text:text,
        height: size,
        width: size,
        colorLight,
        colorDark,
    });
}

generateQRCode()