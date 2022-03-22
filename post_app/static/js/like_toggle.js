window.addEventListener('load', () => {
    const likeToggleUrl = window.location + 'like/'
    const message = document.querySelector('#message')
    const btnLikeToggle = document.querySelector('#toggle-like')
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]')
    const likeCount = document.querySelector('#like-count')
    let countInt = parseInt(likeCount.innerHTML)
    async function likeToggleRequest() {
        await fetch(likeToggleUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken.value
            }

        }).then(response => {
            response.text().then((text) => {
                    if (response.status === 400){
                        message.innerHTML = text
                    }
                    else if (response.status === 200){

                        let result = JSON.parse(text)
                        console.log(result)
                        if (result.status === 'dislike_set'){
                            console.log('dislike')
                            countInt -=1
                            likeCount.innerHTML = countInt
                            message.innerHTML = 'Dislike set'
                        }

                        else if (result.status === 'like_set') {
                            countInt +=1
                            likeCount.innerHTML = countInt
                            message.innerHTML = 'Like set'
                        }


                    }
                })
        })
    }

    btnLikeToggle.addEventListener('click', async (e) => {
        await likeToggleRequest()
    })
});
