function writeToElement(id, data){
  try {
    document.getElementById(id).innerHTML += data;
  }catch(e){
    console.log(`Unable to write to element. Error: ${e}`);
  }
}

function overrideElement(id, data){
  try {
    document.getElementById(id).innerHTML = data;
  }catch(e){
    console.log(`Unable to write to element. Error: ${e}`);
  }
}

function hideElement(id){
  try {
    document.getElementById(id).style.opacity = 0;
  }catch(e){
    console.log(`Unable to hide element. Error: ${e}`);
  }
}

function showElement(id){
  try {
    document.getElementById(id).style.opacity = 100;
  }catch(e){
    console.log(`Unable to show element. Error: ${e}`);
  }
}

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
  var el_output_image = document.getElementById('output_image');

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
      console.log(stats);

      var military_found = 0;
      var civilian_found = 0;
      var military_aircraft_found = 0;
      var military_truck_found = 0;
      var military_tank_found = 0;
      var military_helicopter_found = 0;
      var civilian_aircraft_found = 0;
      var civilian_car_found = 0;

      for(const detection of stats){
        if(detection['class'] == 'military aircraft'){
          military_aircraft_found++;
        } else if(detection['class'] == 'military tank'){
          military_tank_found++;
        } else if(detection['class'] == 'military truck'){
          military_truck_found++;
        } else if(detection['class'] == 'civilian aircraft'){
          civilian_aircraft_found++;
        } else if(detection['class'] == 'civilian car'){
          civilian_car_found++;
        } else if(detection['class'] == 'military helicopter'){
          military_helicopter_found++;
        }

        writeToElement('output_list', `<li>${detection['class']} - <code>${detection['score']*100}%</code></li>`);
      }

      military_found = military_aircraft_found + military_truck_found + military_tank_found;
      civilian_found = civilian_aircraft_found + civilian_car_found;

      overrideElement('output_time', response.time);
      overrideElement('output_military_count', military_found);
      overrideElement('output_civilian_count', civilian_found);
      overrideElement('output_total_count', (military_found + civilian_found));

      el_output_image.src = `data:image/png;base64,${image}`;
    }
  };

  request.open('POST', `http://127.0.0.1:5000/process`, true);
  request.setRequestHeader('Content-Type', 'application/json')
  request.send(JSON.stringify({"image": img}));
}

function processImage(){
  var file = document.getElementById('file_input').files[0];
  var reader = new FileReader();

  overrideElement('output_list', '');
  output.style.opacity = 0;

  var img = getImageFromInput(file, reader, output_image);

  show('output')

  if(img == -1){
    alert('Unable to load that image from your system!');
    hide('output')
    return;
  }
}
