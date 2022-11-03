el_output_image = document.getElementById('output_image');

// TODO: Move into front-end when ready.
function getImageFromInput(file, reader, output_image) {
  reader.onloadend = function() {
    var data = reader.result;

    if(data.indexOf('data:image/png;base64,') >= 0){
      data = data.split('data:image/png;base64,')[1];

      transmitToServer(data);
    } else if(data.indexOf('data:image/jpeg;base64,') >= 0){
      data = data.split('data:image/jpeg;base64,')[1];

      transmitToServer(data);
    } else{
      alert('Unknown type of image. Please choose another')
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

      if(response.error){
        alert('Error in fetching processed image. Please try again.');
        el_output_image.src = '';
        return;
      }

      var image = response.image;
      var stats = response.stats;

      el_output_image.src = `data:image/png;base64,${image}`;
    }
  };

  request.open('GET', `http://127.0.0.1:5000/process?image=${encodeURIComponent(img)}`, true);
  request.send();
}

function processImage(){
  var file = document.getElementById('file_input').files[0];
  var reader = new FileReader();

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
