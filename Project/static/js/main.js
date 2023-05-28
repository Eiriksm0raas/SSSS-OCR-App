// Add event handlers
setEventHandlers();
let file;
const modal = new bootstrap.Modal(document.getElementById('myModal'));

// Set dropped files in memory and display the image
function handleDrop(event) {
  event.preventDefault();
  
  file = event.dataTransfer.files[0];
  var reader = new FileReader();
  
  reader.onload = loadReader;
  
  reader.readAsDataURL(file);
  console.log("picture uploaded");
}

// Simulate clicking the file input button
function clickUpload(event) {
    document.getElementById('fileInput').click();
}

// Prevent the default behaviour for dragover for the "dropzone"
function handleDragOver(event) {
    event.preventDefault();
}

// Upload the image to the api and display returned text
async function processImage() {
    if(file != null) {
        try {
            const input = document.getElementById("fileInput");
            const text = await uploadPicture(file);
            displayInModal(text);
        } catch(ex) {
            console.log(ex);
        }
    }
}

// Display text in modal and show modal
function displayInModal(text) {
    document.getElementById('modal-text').innerHTML = 
        replaceNewLines(text);

    modal.show();
}

// Handle manual uploads when the user clicks the 
function handleUpload(event) {
    file = document.getElementById('fileInput').files[0];
    console.log(file);

    var reader = new FileReader();
  
    reader.onload = loadReader;
  
    reader.readAsDataURL(file);
}

// Event handler for the loader we use in handleUpload and handleDrop
function loadReader(event) {
    let img = document.createElement('img');
    img.src = event.target.result;

    let dropzone = document.getElementById('dropzone');
    dropzone.innerHTML = '';
    dropzone.appendChild(img);
}

// Set event handlers for buttons
function setEventHandlers() {
    // Set the buttons
    document.getElementById("upload-picture-button")
        .addEventListener('click',() => processImage());
    
    document.getElementById("take-picture-button")
        .addEventListener('click', () => takePicture());

    document.getElementById("remove-picture-button")
        .addEventListener('click', () => { 
            document.getElementById('dropzone').innerHTML = `
                <p style="margin-top: calc(50% - 0.5rem);">
                    Drag and drop an image here, or click here and choose an image
                </p>`;
            document.getElementById('fileInput').files = new DataTransfer().files;
            file = null;
        });
}


// Replace \n character with br tag to render in html
function replaceNewLines(text) {
    text = text.replace(/"/g, "");
    return text.replace(/\\n/g, "<br>");
}

// Take picture from the Raspberry Pi
function takePicture() {
    return fetch("/api/takepicture")
        .then(response => response.text());
}

// Upload picture to the API
async function uploadPicture(file) {
    let formData = new FormData();
    formData.append("file", file);
    
    return fetch("/api/uploadpicture", {
        method: "POST",
        body: formData
    }).then(response => response.text()) 
}