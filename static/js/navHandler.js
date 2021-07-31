var a = document.getElementById("nav_bar_tab");

var navHandler = () => {
 if (a.classList.value.indexOf("action") === -1) {
  a.classList.add("action");
  console.log(a.classList);
 } else {
  a.classList.remove("action");
  console.log(a.classList);
 }
};
