// Captura de elementos
const contactForm = document.getElementById("contactForm");
const contactList = document.getElementById("contactList");
const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const phoneInput = document.getElementById("phone");

// Eventos
contactForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const name = nameInput.value;
    const email = emailInput.value;
    const phone = phoneInput.value;

    const contact = { name, email, phone };
    
    const contacts = JSON.parse(localStorage.getItem("contacts")) || [];
    contacts.push(contact);
    localStorage.setItem("contacts", JSON.stringify(contacts));

    contactForm.reset();

    loadContacts();
});

// Funcoes
function loadContacts() {
    const contacts = JSON.parse(localStorage.getItem("contacts")) || [];
    contactList.innerHTML = "";
    contacts.forEach(contact => {
        const li = document.createElement("li");
        li.className = "list-group-item";
        li.textContent = `Nome: ${contact.name}, E-mail: ${contact.email}, Telefone: ${contact.phone}`;
        contactList.appendChild(li);
    });
}

loadContacts();