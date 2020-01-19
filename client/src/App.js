import React from 'react'
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container, Card, Button, Image} from 'react-bootstrap';
import $ from "jquery";


function App() {
   function httpCall(){
      var URL = "http://0.0.0.0:80/";
      var out;

      $.get(URL, {}, function(data){
         out = data
      });

     document.getElementById("returnVal").innerHTML = JSON.stringify(out); 
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
         <Card className="text-center" border="dark" padding-to='10rem'>
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
               <Button variant="primary">Solve</Button>
            </Card.Footer>
         </Card>
     </Container>
 );
}

export default App;
