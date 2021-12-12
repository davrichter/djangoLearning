const navbarForm = document.getElementById("navbar-form")
const downloadButton = document.createElement("button")
downloadButton.classList.add("btn", "bg-dark", "text-light")
downloadButton.value = "save"
downloadButton.name = "title"

const textSwitcher = document.createElement("button")
const navbarList = document.getElementById("navbar-list")
textSwitcher.classList.add("btn", "btn-primary", "navbar-right")
textSwitcher.innerHTML = "Original"

downloadButton.innerHTML = "<i class=\"bi-download\" style=\"font-size: 150%;\"></i>"

navbarForm.appendChild(downloadButton)
navbarList.appendChild(textSwitcher)

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