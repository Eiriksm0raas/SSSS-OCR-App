const BASE_ADDRESS = "http://127.0.0.1:8000/api";

export async function getImageConverted(imgUrl) {
    return await fetch(BASE_ADDRESS + "/read/?" + new URLSearchParams({
        img_url: imgUrl
    }))
    .then(response => response.text());
}