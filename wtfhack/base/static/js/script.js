/* Authenticate AJAX requests */
var csrftoken = $.cookie('csrftoken');
$.ajaxSetup({
          crossDomain: false, // obviates need for sameOrigin test
          beforeSend: function(xhr, settings) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
              xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
          }
      });

function changePage(newLoc)
 {
   nextPage = newLoc.options[newLoc.selectedIndex].value
        
   if (nextPage != "")
   {
      document.location.href = nextPage
   }
 }

