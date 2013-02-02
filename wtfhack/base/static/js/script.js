function changePage(newLoc)
 {
   nextPage = newLoc.options[newLoc.selectedIndex].value
        
   if (nextPage != "")
   {
      document.location.href = nextPage
   }
 }





