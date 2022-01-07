window.addEventListener("load", () => {
    let article = document.getElementById("article")
    article.innerHTML = articleTextFormatted

    const textSwitcher = document.getElementById("textSwitcher")

    console.log(textSwitcher.innerHTML)
    textSwitcher.addEventListener('click', () => {
        let article = document.getElementById("article")

        if (textSwitcher.innerHTML === "Original") {
            article.innerHTML = articleTextOriginal
            article.classList.remove("text-lowercase")
            textSwitcher.innerHTML = "Formatted"
            textSwitcher.title = "Show formatted"
        } else {
            article.innerHTML = articleTextFormatted
            article.classList.add("text-lowercase")
            textSwitcher.innerHTML = "Original"
            textSwitcher.title = "Show Original"
        }
    })
})