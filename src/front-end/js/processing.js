
function to_base64(event){
    const output = document.getElementById("output");
    if (output.style.opacity == 0) {
        output.style.opacity = 100;
      } else {
        output.style.opacity = 0;
      }
    event.preventDefault(); // Prevents page from reloading
}

function init(){
    const form = document.getElementById("form");
    form.addEventListener('submit', to_base64);
}

window.onload = init; // Makes sure script only runns when page has finished loading