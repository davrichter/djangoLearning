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
        let dropdownButton = document.getElementsByClassName("btn-outline-" + newTheme)

        // i have no idea why but for some reason if the loops just runs once not all
        // htmlelements are actually converted but whatever this way it works
        for (let i = 0; i <= 3; i++) {
            for (let i of items) {
                // replace background color
                i.classList.replace("bg-" + oldTheme, "bg-" + newTheme)
                // replace text color
                i.classList.replace("text-" + newTheme, "text-" + oldTheme)
            }

            for (let i of dropdownButton) {
                i.classList.replace("btn-outline-" + newTheme, "btn-outline-" + oldTheme)
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