import React from 'react'
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container} from 'react-bootstrap';
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
      <header className="App-header">
       Math Equation Solver
      </header>
   

   <div className="content">
      <label> input an image of a math equation to solve</label>

      
         <input type="file" id="imgInp" accept="image/png, image/jpeg" onChange={loadFile}/>

         <img id="output" className="image"/>
        
      
      <button className="button" onClick={uploadFile}>submit</button>

      <p id="returnVal"></p>

   </div>


   </Container>
  );
}

export default App;
