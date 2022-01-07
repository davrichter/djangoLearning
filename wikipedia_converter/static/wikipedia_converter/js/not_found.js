$.get({
    url: "https://api.giphy.com/v1/gifs/search?q=not+found&api_key=dc6zaTOxFJmzC&rating=pg",
    success: (result) => {
        let data = result.data
        let gifURLs = []
        for (let index in data) {
            let gifObject = data[index]
            gifURLs.push(gifObject.images.original.url)
        }
        let id = Math.floor(50*Math.random())
        document.getElementById("not-found-gif").src = gifURLs[id]
    },
    error: (error) => {
        console.error(error);
    }
});