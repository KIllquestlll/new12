const modal = document.getElementById("RegisterModal");
const openBtn = document.getElementById("openRegister");


  openBtn.onclick = () => {
    modal.style.display = "flex";
  };


  modal.onclick = (e) => {
    if (e.target === modal) { 
      modal.style.display = "none";
    }
  };

const modal2 = document.getElementById("LoginModal");
const openBtn2 = document.getElementById("openLogin");


  openBtn2.onclick = () => {
    modal2.style.display = "flex";
  };


 modal2.onclick = (e) => {
    if (e.target === modal2) { 
      modal2.style.display = "none";
    }
  };