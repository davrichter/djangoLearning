function addElementsToNavbar() {
    const navbarForm = document.getElementById("navbar-form")

    const downloadButton = $("<button>")
    downloadButton.attr("id", "downloadButton")
    downloadButton.attr(
        "class", "btn"
    )
    console.log(downloadButton)
    downloadButton.html("<i class=\"bi-download\" style=\"font-size: 150%;\"></i>")


    const navbarList = document.getElementById("navbar-list")

    const textSwitcher = document.createElement("button")
    textSwitcher.classList.add("btn", "btn-primary", "navbar-right")
    textSwitcher.innerHTML = "Original"
    textSwitcher.id = "textSwitcher"


    $("#navbar-form").append(downloadButton)
    navbarList.appendChild(textSwitcher)
}

document.body.onload = () => {
    addElementsToNavbar()

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
}