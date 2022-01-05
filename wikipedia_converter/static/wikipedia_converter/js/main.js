const themeButton = document.getElementById("themeToggler")
const systemTheme = window.matchMedia("(prefers-color-scheme: dark)")
let theme

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
        let table = document.getElementsByClassName("table-" + oldTheme)
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

            for (let i of table) {
                i.classList.replace("table-" + oldTheme, "table-" + newTheme)
            }
        }
    }
}

window.addEventListener("load", () => {
    console.log("Helo")
    let theme = localStorage.getItem("theme")

    if (theme !== null) {
        if (theme === "light" || (!systemTheme.matches && theme !== "dark")) {
            toggleTheme("light", "dark")
        }
    }
    else {
        if (systemTheme.matches) {
            toggleTheme("dark", "light")
        }
        else {
            toggleTheme("light", "dark")
        }
    }
})