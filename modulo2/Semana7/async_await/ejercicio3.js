const button = document.getElementById('get-btn');
const input = document.getElementById('id-input');
const showInfo = document.getElementById('show');
const errorInfo = document.getElementById('error');

async function getUser(userId) {
    try {
        showInfo.innerHTML = '';
        errorInfo.innerHTML = '';

        const response = await fetch(`https://reqres.in/api/users/${userId}`, {
            headers: { 'x-api-key': 'reqres-free-v1' }
        });

        if (response.status === 404) {
            errorInfo.innerHTML = `<strong>Usuario ${userId} no encontrado.</strong>`;
            showInfo.innerHTML = '';
            return;
        }

        const data = await response.json();
        const user = data.data;

        showInfo.innerHTML = `
        <p><strong>Nombre:</strong> ${user.first_name} ${user.last_name} </p>
        <p><strong>Correo:</strong> ${user.email}</p>`;

    } catch (error) {
        errorInfo.innerHTML = `<strong>Hubo un problema: ${error}</strong>`;
    }
}

button.addEventListener('click', () => {
    const userId = input.value;

    if (userId === '') {
        showInfo.innerHTML = '';
        errorInfo.innerHTML = 'Por favor ingresa un id.';
        return;
    }

    getUser(userId);
});
