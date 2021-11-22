const navbarForm = document.getElementById("navbar-form")
const downloadButton = document.createElement("button")
downloadButton.classList.add("btn")
downloadButton.classList.add("text-light")
downloadButton.classList.add("bg-dark")
downloadButton.value = "save"
downloadButton.name = "title"


downloadButton.innerHTML = "<i class=\"bi-download\" style=\"font-size: 150%;\"></i>"

navbarForm.appendChild(downloadButton)