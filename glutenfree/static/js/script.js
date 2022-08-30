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

  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.tap-target');
    var instances = M.TapTarget.init(elems, options);
  });
          
  var instance = M.TapTarget.getInstance(elem);

  /* jQuery Method Calls
    You can still use the old jQuery plugin method calls.
    But you won't be able to access instance properties.

    $('.tap-target').tapTarget('methodName');
    $('.tap-target').tapTarget('methodName', paramName);
  */
  instance.next();
  instance.next(3); // Move next n times.

  instance.close();