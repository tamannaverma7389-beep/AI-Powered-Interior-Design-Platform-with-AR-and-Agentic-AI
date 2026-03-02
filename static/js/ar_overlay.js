const video = document.getElementById("camera");
const canvas = document.getElementById("overlay");
const ctx = canvas.getContext("2d");

navigator.mediaDevices.getUserMedia({ video: true })
.then(stream => {
    video.srcObject = stream;
})
.catch(err => {
    console.error("Camera error:", err);
});

let scale = 1;
let posX = 100;
let posY = 100;
let currentImage = null;

function placeFurniture(imgSrc) {
    currentImage = new Image();
    currentImage.src = imgSrc;

    currentImage.onload = function() {
        drawImage();
    };
}

canvas.addEventListener("wheel", function(e) {
    scale += e.deltaY * -0.001;
    if (scale < 0.2) scale = 0.2;
    if (scale > 3) scale = 3;
    drawImage();
});

canvas.addEventListener("mousemove", function(e) {
    if (e.buttons === 1 && currentImage) {
        posX = e.offsetX;
        posY = e.offsetY;
        drawImage();
    }
});

function drawImage() {
    if (!currentImage) return;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(currentImage, posX, posY, 200 * scale, 200 * scale);
}