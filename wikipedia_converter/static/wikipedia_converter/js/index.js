window.addEventListener("load", () => {
        function getLang() {
            const radioButtons = document.querySelectorAll('input[name="language"]')

            for (let i = 0; i < radioButtons.length; i++) {
                if (radioButtons[i].checked) {
                    return radioButtons[i].value
                }
            }
        }


        const input = document.getElementById("autoComplete")

        async function getSuggestions(request, lang) {
            let initObject = {
                method: 'GET',
            }

            let response = await fetch(`https://${lang}.wikipedia.org/w/api.php?action=query&origin=*&format=json&generator=search&gsrnamespace=0&gsrlimit=5&gsrsearch='${request}'`, initObject)

            response = response.json()
            try {
                let pages = response.then((r => r.query.pages))
                let titles = []
                pages.then(r => {
                    for (let i in r) {
                        titles.push(r[i].title)
                    }
                })

                return titles
            } catch (e) {
                return []
            }
        }

        input.addEventListener("keydown", () => {
            getSuggestions(input.value, getLang()).then(r => {
                $("#autoComplete").autocomplete({
                    source: r
                });
            })
        })
    }
)