// reusable function to handle from submission
function handleFormSubmit(formId,graphClass,endpoint) {
document.getElementById(formId).addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent the default form submission

  // run the formn handle function

  let formData = new FormData(this); // this refers to element that triggers the submit event
  // create a plain object
  let jsonData = {};
  // iterate through obj
  formData.forEach((value,key) => {
    jsonData[key] = value;
  });

    // send JSON data to flask
// This initiates a fetch request to the server at the /submit endpoint.
fetch(endpoint, {
  method: 'POST',
  // This line sets the headers for the request, specifically telling the server that the content being sent is in JSON format.
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(jsonData)
})

// get the response as a blob
  .then(response => response.blob())
  // create a url for the blob
  // create an img element

  .then(blob => {
    const url =URL.createObjectURL(blob);
    let img =document.createElement('img');
    img.src = url;
     // Find the div with class 'graph' and append the image
     const graphDiv = document.querySelector(graphClass);
     graphDiv.innerHTML = ''; // Clear any existing content
     graphDiv.appendChild(img);
     // after img is loaded revoke url
     img.onload = () => URL.revokeObjectURL(url);
  })
  .catch(error => console.error('Error:', error));
})
}

// attach listeners to both forms
handleFormSubmit('SimpleSIRForm', '.graphSimple', '/submit');
handleFormSubmit('ComplexSIRForm', '.graphComplex', '/submit_complex');





