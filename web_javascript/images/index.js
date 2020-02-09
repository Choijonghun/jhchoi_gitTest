/*
js에서는 무엇을 생성할때 선언을 해줘야 한다

자바스크립트엔 스페이스를 변수명이 쓸 수 없음 따라서 변수명은 항상 소문자로 시작하고 스페이스가 필요하면 다음 단어에 대문자로 시작함

let : 변수
const : 상수
string : 텍스트 뭉치
boolean : True and False (1 or 0)
float : 소숫점이 있는 숫자
array : string을 하나로 묶는것 = 리스트
[] : 브라켓
{} : 컬리 브라켓

const object = {
  name: "jonghun",
  age: 33,
  gender: "male",
  isHandsome: true,
  obArray: ["object", "안의", "array", "입니다."],
  obArObject: [
    {
      this: "이것은",
      is: "오브젝트 안의"
    },
    {
      this: "어레이 안의",
      is: "오브젝트 이다"
    }
  ]
}

console.log(object);
object.age = 26; // object의 변수 변경
console.log(object.age); //object의 age에만 접근하는 방법
console.log(object.obArObject);

console.log("\n", "\n", "\n");//자바스크립트에서 함수만들기

//매우 중요 !!!! JS에서는 백틱(`)을 이용하여 콘솔로그 에서 함수를 끌어다 쓸 수 있음
function sayHello(name, age) {
  console.log(`hello ${name} you are ${age} years old`);
}
sayHello("jonghun", 26);

const calculator = {
  plus: function (a, b) {
    return a + b;
  },
  minus: function (a, b) {
    return a - b;
  },
  multiply: function (a, b) {
    return a * b;
  },
  divide: function (a, b) {
    return a / b;
  },
  power: function (a, b) {
    return a ** b;
  }
}

const plusResult = calculator.plus(5, 5);
const minusResult = calculator.minus(5, 5);
const multiplyResult = calculator.multiply(5, 5);
const divideResult = calculator.divide(5, 5);
const powerResult = calculator.power(5, 5);

console.log(`plus: ${plusResult}, minus: ${minusResult}, multiply: ${multiplyResult}, divide: ${divideResult}, power: ${powerResult}`);
*/

const title = document.querySelector("#title")
title.innerHTML = "하이 잉츄쓰";
document.title = "잉츄쓰의 블로그"
const CLICK_CLASS = "clicked";

function handleclick(event){
  const currentName = title.className
  title.classList.toggle(CLICK_CLASS);
}

function init(){
  title.addEventListener("click", handleclick);
}

init();