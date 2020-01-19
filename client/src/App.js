import React from 'react'
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container, Card, Button, Image} from 'react-bootstrap';
import $ from "jquery";

function App() {
   function httpCall(img_base64){
      var URL = "http://127.0.0.1:5000/imageCalc/";
      var out;
      
      $.post(URL, {'image_path': img_base64}, function(data){
         out = data
      });

      alert('Please wait patiently while your request is being processed');

     document.getElementById("returnVal").innerHTML = out; 
   }

   function uploadFile(){
      var input = document.getElementById("imgInp").files;
      var fileToLoad = input[0];
      
      var reader = new FileReader();
      reader.readAsBinaryString(fileToLoad);
      
      reader.onload = function() {
         httpCall(btoa(reader.result));
       };

       reader.onerror = function() {
        alert('there are some problems');
       };      

   }

   var loadFile = function(event) {
     var output = document.getElementById("output");
     output.src = URL.createObjectURL(event.target.files[0]);
   };

  return (
     <Container className = "App">
         <Card className="text-center" border="dark">
            <Card.Header as="h5">Math Equation Solver</Card.Header>
            <div>
               <input type="file" 
                      id="imgInp" 
                      accept="image/png, image/jpeg" 
                      onChange={loadFile}/>
               <div border='light' style={{display: 'flex', justifyContent: 'center'}}>
                  <Image id="output" className="image"/>
               </div>
            </div>
            <Card.Footer>
               <Button variant="primary" onClick={uploadFile}>Solve</Button>
            </Card.Footer>
            <Card className="answer" border="dark">
               <Card.Text id="returnVal"></Card.Text>
            </Card>
         </Card>
     </Container>
  );
}

export default App;
