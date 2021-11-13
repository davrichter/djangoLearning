let themeButton = document.getElementById("themeToggler")
const theme = localStorage.getItem("theme")

function toggleTheme(newTheme, oldTheme) {
    if (newTheme === "dark") {
        var classString = "bg-light text-dark"
    } else {
        var classString = "bg-dark text-light"
    }
    console.log(classString)
    let items = document.getElementsByClassName(classString)
    console.log(items)

    for (let i = 0; i < 5; i++) {
        for (let i of items) {
            console.log("i:" + i)
            // replace background color
            console.log("bg-" + oldTheme, "bg-" + newTheme)
            i.classList.replace("bg-" + oldTheme, "bg-" + newTheme)
            // replace text color
            console.log("text-" + newTheme, "text-" + oldTheme)
            i.classList.replace("text-" + newTheme, "text-" + oldTheme)
        }
    }
    console.log(items)

    /*
    for (let i = 0; i < items.length; i++) {
        console.log("i:" + i)
        // replace background color
        items[i].classList.replace("bg-" + oldTheme, "bg-" + newTheme)
        // replace text color
        items[i].classList.replace("text-" + newTheme, "text-" + oldTheme)
    }
    console.log(items)
    */
}

document.body.onload = () => {
    if (theme === "light") {
        toggleTheme("light", "dark")
    }
}

themeButton.addEventListener('click', () => {
    if (theme === "light") {
        localStorage.setItem("theme", "dark")

        toggleTheme("dark", "light")
    }

    else if (theme === "dark" || theme == null) {
        console.log("switching from dark to light...")
        localStorage.setItem("theme", "light")

        toggleTheme("light", "dark")
    }
})