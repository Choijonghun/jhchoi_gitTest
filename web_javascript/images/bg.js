const body = document.querySelector("body");

const IMG_NUMBER = 3;

function paintImage(imgNumber) {
    const image = new Image();
    image.src = `${imgNumber + 1}.jpg`
    image.classList.add("bgimage"); //img에 bgbgimage 클래스 생성 (css 적용을 위함)
    body.appendChild(image); //body에 자식 노드(image)를 추가
}

function genRandom() {
    const number = Math.floor(Math.random() * IMG_NUMBER);
    return number;
}

function init() {
    const randomNumber = genRandom();
    paintImage(randomNumber);
}

init();