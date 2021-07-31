//Javascript
// var lastScrollTop = 0;
// var delta = 5;
// var fixBox = document.querySelector("#main_page");
// var fixBoxHeight = fixBox.offsetHeight;
// console.log(document.querySelector("#main_page").scrollY);

// var didScroll;
// //스크롤 이벤트

// window.onscroll = function (e) {
//  didScroll = true;
// };

// //0.25초마다 스크롤 여부 체크하여 스크롤 중이면 hasScrolled() 호출
// setInterval(function () {
//  if (didScroll) {
//   hasScrolled();
//   didScroll = false;
//  }
// }, 250);

// function hasScrolled() {
//  var nowScrollTop = window.scrollY;
//  if (Math.abs(lastScrollTop - nowScrollTop) <= delta) {
//   return;
//  }
//  if (nowScrollTop > lastScrollTop && nowScrollTop > fixBoxHeight) {
//   //Scroll down
//   console.log("scroll down");
//  } else {
//   if (nowScrollTop + window.innerHeight < document.body.offsetHeight) {
//    //Scroll up
//    console.log("scroll up");
//   }
//  }
//  lastScrollTop = nowScrollTop;
// }

// function getScrollY() {
//  var scrOfY = 0;
//  if (typeof window.pageYOffset == "number") {
//   //Netscape compliant
//   scrOfY = window.pageYOffset;
//   console.log(scrOfY);
//  } else if (document.body && (document.body.scrollLeft || document.body.scrollTop)) {
//   //DOM compliant
//   scrOfY = document.body.scrollTop;
//   console.log(scrOfY);
//  } else if (document.documentElement && (document.documentElement.scrollLeft || document.documentElement.scrollTop)) {
//   //IE6 standards compliant mode
//   scrOfY = document.documentElement.scrollTop;
//   console.log(scrOfY);
//  }

//  console.log(scrOfY);

//  if (scrOfY === 1050) {
//   document.getElementById("nav_1").className = "current";
//  } else {
//   document.getElementById("nav_1").className = "no";
//  }
//  if (scrOfY === 1050) {
//   document.getElementById("nav_2").className = "current";
//  } else {
//   document.getElementById("nav_2").className = "no";
//  }
//  if (scrOfY === 2026) {
//   document.getElementById("nav_3").className = "current";
//  } else {
//   document.getElementById("nav_3").className = "no";
//  }
//  if (scrOfY === 3352) {
//   document.getElementById("nav_4").className = "current";
//  } else {
//   document.getElementById("nav_4").className = "no";
//  }

//  return scrOfY;
// }

// console.log(getScrollY());

document.addEventListener("scroll", function () {
 var currentScrollValue = document.documentElement.scrollTop; //스크롤 위치 구하기
 var nav1 = document.getElementById("nav_1");
 var nav2 = document.getElementById("nav_2");
 var nav3 = document.getElementById("nav_3");
 var nav4 = document.getElementById("nav_4");

 // 위치에 따라 class 추가
 if (currentScrollValue >= 0 && currentScrollValue <= 1049) {
  nav1.classList.add("current");
  nav2.classList.remove("current");
  nav3.classList.remove("current");
  nav4.classList.remove("current");
 } else if (currentScrollValue >= 1050 && currentScrollValue <= 2025) {
  nav1.classList.remove("current");
  nav2.classList.add("current");
  nav3.classList.remove("current");
  nav4.classList.remove("current");
 } else if (currentScrollValue >= 2026 && currentScrollValue <= 3351) {
  nav1.classList.remove("current");
  nav2.classList.remove("current");
  nav3.classList.add("current");
  nav4.classList.remove("current");
 } else if (currentScrollValue >= 3352) {
  nav1.classList.remove("current");
  nav2.classList.remove("current");
  nav3.classList.remove("current");
  nav4.classList.add("current");
 }
});
