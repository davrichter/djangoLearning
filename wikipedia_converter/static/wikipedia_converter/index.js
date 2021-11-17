let themeButton = document.getElementById("themeToggler")
let theme = localStorage.getItem("theme")

function toggleTheme(newTheme, oldTheme) {
    if (newTheme === "dark") {
        let classString = "bg-light text-dark"
        changeTheme(classString)
    } else {
        let classString = "bg-dark text-light"
        changeTheme(classString)
    }

    function changeTheme(classString) {
        let items = document.getElementsByClassName(classString)


        for (let i = 0; i <= 2; i++) {
            for (let i of items) {
                // replace background color
                i.classList.replace("bg-" + oldTheme, "bg-" + newTheme)
                // replace text color
                i.classList.replace("text-" + newTheme, "text-" + oldTheme)
            }
        }
    }
}

document.body.onload = () => {
    if (theme === "light") {
        toggleTheme("light", "dark")
    }
}

themeButton.addEventListener('click', () => {
    theme = localStorage.getItem("theme")

    if (theme === "light") {
        localStorage.setItem("theme", "dark")

        toggleTheme("dark", "light")
    }

    else if (theme === "dark" || theme == null) {
        localStorage.setItem("theme", "light")

        toggleTheme("light", "dark")
    }
})