window.addEventListener('load', () => {
    const username = document.querySelector('input[name="username"]')
    const email = document.querySelector('input[name="email"]')
    const password = document.querySelector('input[name="password"]')
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]')
    const signupUrl = window.location + 'api/'
    const message = document.querySelector('#message')
    const form = document.querySelector('form')

    async function sendSignupRequest(data) {
        await fetch(signupUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken.value
            },
            body: JSON.stringify(data)
        }).then(response => {
            response.text().then((errorText) => {
                    if (response.status === 400){
                        message.classList.remove('d-none')
                        message.innerHTML = errorText
                    }
                    else if (response.status === 201){
                        window.location.href = '../login';
                    }
                })
        })
    }

    form.addEventListener('submit', async (e) => {
        e.preventDefault()
        const data = {
            'user': {
                'username': username.value,
                'email': email.value,
                'password': password.value
            }
        }
        await sendSignupRequest(data)
    })
});
