const navbar = document.getElementById("navbar")
const downloadButton = document.createElement("button")
downloadButton.classList.add("btn")
downloadButton.classList.add("text-light")
downloadButton.classList.add("bg-dark")
downloadButton.value = "save"
downloadButton.innerHTML = "<i class=\"bi-download\" style=\"font-size: 150%;\"></i>"

navbar.appendChild(downloadButton)