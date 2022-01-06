function addElementsToNavbar() {
    const navbarForm = document.getElementById("navbar-form")

    navbarForm.innerHTML +=
        `<button id="downloadButton" class="btn bg-dark text-light" value="${articleTitle}" name="title">
            <i class=\"bi-download\" style=\"font-size: 150%;\"></i>
        </button>`

    const navbarList = document.getElementById("navbar-list")

    navbarList.innerHTML +=
        `<button class="btn btn-primary navbar-right" id="textSwitcher">Original</button>`
}

window.addEventListener("load", () => {
    addElementsToNavbar()

    let article = document.getElementById("article")
    article.innerHTML = articleTextFormatted

    const textSwitcher = document.getElementById("textSwitcher")

    textSwitcher.addEventListener('click', () => {
        let article = document.getElementById("article")

        if (textSwitcher.innerHTML === "Original") {
            article.innerHTML = articleTextOriginal
            article.classList.remove("text-lowercase")
            textSwitcher.innerHTML = "Formatted"
        } else {
            article.innerHTML = articleTextFormatted
            article.classList.add("text-lowercase")
            textSwitcher.innerHTML = "Original"
        }
    })
})