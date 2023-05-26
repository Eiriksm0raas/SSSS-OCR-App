// Add event handlers
setEventHandlers();
let file;

function handleDrop(event) {
  event.preventDefault();
  
  file = event.dataTransfer.files[0];
  var reader = new FileReader();
  
  reader.onload = function(event) {
    var img = document.createElement('img');
    img.src = event.target.result;

    var dropzone = document.getElementById('dropzone');
    dropzone.innerHTML = '';
    dropzone.appendChild(img);
  };
  
  reader.readAsDataURL(file);
  console.log("picture uploaded");
}

function handleDragOver(event) {
  event.preventDefault();
}

async function processImage() {
    try {
        const input = document.getElementById("fileInput");
        //const file = input.files[0];
        const text = await uploadPicture(file);
        console.log(await text);
    } catch(ex) {
        console.log(ex);
    }
}

function setEventHandlers() {
    // Set the buttons
    document.getElementById("upload-picture-button")
        .addEventListener('click',() => processImage());
    
    document.getElementById("take-picture-button")
        .addEventListener('click', () => takePicture());
}

// Take picture from the Raspberry Pi
function takePicture() {
    return fetch("/api/takepicture")
        .then(response => response.text);
}

// Upload puicture to the API
function uploadPicture(file) {
    let formData = new FormData();
    formData.append("file", file);
    
    return fetch("/api/uploadpicture", {
        method: "POST",
        body: formData
    }).then(response => response.text) 
}