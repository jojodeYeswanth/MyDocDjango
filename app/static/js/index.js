var home = document.querySelectorAll('.parallax');
M.Parallax.init(home, { responsiveThreshold: 0 });

var scrollspy = document.querySelectorAll('.scrollspy');
M.ScrollSpy.init(scrollspy, {});

  $(document).ready(function(){
    $('select').formSelect();
  });
  
   $(document).ready(function(){
    $('.datepicker').datepicker();
  });
  
  
 