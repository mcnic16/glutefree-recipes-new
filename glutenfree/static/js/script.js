$(document).ready(function(){
    $('.sidenav').sidenav();
  });
        
 // select initialization
 let selects = document.querySelectorAll("select");
 M.FormSelect.init(selects);

 // collapsible initializataion
 let collapsibles = document.querySelectorAll(".collapsible");
 M.Collapsible.init(collapsibles);

 $(document).ready(function() {
    $('input#input_text, textarea#textarea2').characterCounter();
  });

  $(document).ready(function(){
    $('.modal').modal();
  });

  var instance = M.Modal.getInstance(elem);