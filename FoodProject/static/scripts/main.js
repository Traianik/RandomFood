
function show_description() {
    var x = document.getElementById("description_box");
    
    if (x.style.display === "none") { 
      x.style.display = "block";
      var scrollToElement = function(el, ms){
          var speed = (ms) ? ms : 600;
          $('html,body').animate({
              scrollTop: $(el).offset().top
          }, speed);
      }
      
      // specify id of element and optional scroll speed as arguments
      scrollToElement('#description_box', 600);
    } else {  
      x.style.display = "none";
    }
  }

window.onload = function() {
    document.body.className += " loaded";
} 
