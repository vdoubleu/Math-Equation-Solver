import React from 'react'
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container, Card, Button, Image, Alert} from 'react-bootstrap';
import $ from "jquery";


function App() {

   function httpCall(img_base64){
      var URL = "http://127.0.0.1:5000/imageCalc/";
      var out;

      $.post(URL, {'image_path': img_base64}, function(data){
         out = data
      });
      
      alert('Processing request');
<<<<<<< HEAD
      document.getElementById("returnVal").innerHTML = out; 
=======

      document.getElementById("returnVal").innerHTML = result; 
>>>>>>> 51f2b333f586c01d659b14d10de6bf85c8139a6b
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
         <Card className="text-center" border="dark" style={{marginTop: '40px'}}>
            <Card.Header style={{fontSize: '2rem'}}>Math Equation Solver</Card.Header>
            <div style={{marginTop: '20px', marginBottom: '10px'}}>
               Upload a file of a polynomial equation
            </div>
            <div>
               <input type="file" 
                      id="imgInp" 
                      accept="image/png, image/jpeg" 
                      style={{marginTop: '20px', marginBottom: '20px'}}
                      onChange={loadFile}/>
               <div border='light' style={{display: 'flex', justifyContent: 'center', marginLeft: '10px', marginRight: '10px'}}>
                  <Image id="output" className="image"/>
               </div>
            </div>
            <Card.Footer>
               <Button variant="primary" onClick={uploadFile}>Solve</Button>
            </Card.Footer>
         </Card>
         <Card className='answer' border="dark" style={{marginTop: '20px', fontSize: '1.5rem'}}>
               <Card.Text id="returnVal"></Card.Text>
         </Card>
     </Container>
 );
}

export default App;