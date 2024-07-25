document.addEventListener("DOMContentLoaded", function () {
  const path = window.location.pathname;

  if (path === "/dashboard") {
    document.getElementById("home-div").classList.remove("hidden");
  } else if (path === "/dasboard/flota") {
    document.getElementById("flota-div").classList.remove("hidden");
  } else if (path === "/dasboard/newcar") {
    document.getElementById("newcar-div").classList.remove("hidden");
  }
});
