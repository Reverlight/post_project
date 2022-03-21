window.addEventListener('load', () => {
    const email = document.querySelector('input[name="email"]')
    const password = document.querySelector('input[name="password"]')
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]')
    const loginUrl = window.location + 'api/'
    const message = document.querySelector('#message')
    const form = document.querySelector('form')

    async function sendLoginRequest(data) {
        await fetch(loginUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken.value
            },
            body: JSON.stringify(data)
        }).then(response => {
            response.text().then((errorText) => {
                    if (response.status === 400){
                        message.innerHTML = errorText
                    }
                    else if (response.status === 200){
                        message.innerHTML = 'Success!!!'
                    }
                })
        })
    }

    form.addEventListener('submit', async (e) => {
        e.preventDefault()
        const data = {
            'user': {
                'email': email.value,
                'password': password.value
            }
        }
        await sendLoginRequest(data)
    })
});
