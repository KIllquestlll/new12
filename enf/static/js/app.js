// let popup-log = document.getElementById("popup-log");
// document.onmouseleave = function(e) {
//     popup-log.style.display = "block";
// }
// function closeLog() {
//     popup-log.style.display = "none";
// }
const modal = document.getElementById("myModal");
const openBtn = document.getElementById("openModal");

  // открыть
  openBtn.onclick = () => {
    modal.style.display = "flex";
  };

  // закрыть кликом по пустоте
  modal.onclick = (e) => {
    if (e.target === modal) { // кликнули по фону, а не по .modal-content
      modal.style.display = "none";
    }
  };

const modal2 = document.getElementById("myModal2");
const openBtn2 = document.getElementById("openModal2");

  // открыть
  openBtn2.onclick = () => {
    modal2.style.display = "flex";
  };

  // закрыть кликом по пустоте
  modal2.onclick = (e) => {
    if (e.target === modal2) { // кликнули по фону, а не по .modal-content
      modal2.style.display = "none";
    }
  };