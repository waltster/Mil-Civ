function init(){
    const form = document.getElementById("form");
    form.addEventListener('submit', to_base64);
}

// TODO: Move into front-end when ready.
function getImageFromInput(file, reader, output_image) {
  reader.onloadend = function() {
    var data = reader.result;

    console.log(data);

    if(data.indexOf('data:image/png;base64,') >= 0 || data.indexOf('data:image/jpeg,') >= 0){
      data = data.split('data:image/png;base64,')[1];

      console.log(transmitToServer(data));
    } else{
      console.log('Unknown type')
      return -1;
    }
  }

  if(file) {
    reader.readAsDataURL(file);
  } else{
    output_image.src = '';
    return -1;
  }
}

function transmitToServer(img){
  var request = new XMLHttpRequest();

  request.onreadystatechange = function() {
    if(this.readyState == 4 && this.status == 200){
      var response = JSON.parse(request.responseText);

      document.getElementById('output_image').src = `data:image/png;base64,${response.image}`;
    }
  };

  request.open('GET', `http://127.0.0.1:5000/process?image=${encodeURIComponent(img)}`, true);
  request.send();
}

function processImage(){
  var file = document.getElementById('file_input').files[0];
  var reader = new FileReader();
  var output_image = document.getElementById('output_image');

  var img = getImageFromInput(file, reader, output_image);

  const output = document.getElementById("output");

  if (output.style.opacity == 0) {
    output.style.opacity = 100;
  } else {
    output.style.opacity = 0;
  }

  if(img == -1){
    alert('Unable to load that image from your system!');
    return;
  }
}
