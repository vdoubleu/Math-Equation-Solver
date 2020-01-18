import React from 'react'
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container} from 'react-bootstrap';
import $ from "jquery";


function App() {
   function uploadFile(){
      var input = document.getElementById("imgInp").files;
      
      var fileReader = new FileReader();

      var fileToLoad = input[0];

      fileReader.onload = function(fileLoadedEvent){
         var srcData = fileLoadedEvent.target.result;

         var newImage = document.createElement("img");
         newImage.src = srcData;

         document.getElementById("imgTest").innerHTML = newImage.outerHTML;
   

         alert(document.getElementById("ImgTest").innerHTML);
      }

      //alert(JSON.stringify(input));   
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
   </div>

   </Container>
  );
}

export default App;
