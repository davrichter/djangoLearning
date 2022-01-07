function addElementsToNavbar() {
    const navbarForm = document.getElementById("navbar-form")

    navbarForm.innerHTML +=
        `<button id="downloadButton" 
                class="btn bg-dark text-light" 
                value="${articleTitle}" 
                name="title"
                data-bs-toggle="tooltip"
                data-bs-placement="bottom"
                title="Save Article">
            <i class=\"bi-download\" style=\"font-size: 150%;\"></i>
        </button>`

    const navbarList = document.getElementById("navbar-list")

    navbarList.innerHTML +=
        `<button class="btn btn-primary navbar-right" 
                id="textSwitcher"
                data-bs-toggle="tooltip"
                data-bs-placement="bottom"
                title="Show Original">Original</button>` // this must look so terrible because
                                                        // textSwitcher.innerHTML must not contain
                                                        // any spaces or linebreaks
}

window.addEventListener("load", () => {
    addElementsToNavbar()

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