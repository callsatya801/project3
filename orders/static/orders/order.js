document.addEventListener('DOMContentLoaded', () => {
    //set_Your_channel_links();
                    document.querySelectorAll('.table-row').forEach(button => {
                    button.onclick = () => {
                        console.log(button.dataset.itemid);
                        console.log(button.dataset.itemcat);
                        console.log(button.dataset.nooftop);
                      // console.log(button.dataset.menuitems);
                      //  console.log(button.dataset.toppings);
                        return false;
                        };
                    });


     $('#addToCart').on('show.bs.modal', function (event) {
      var button = $(event.relatedTarget); // Button that triggered the modal
      var recipient = button.data('itemname'); // Extract info from data-* attributes
      // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
      // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
      var modal = $(this);
      modal.find('.modal-title').text(recipient);
      // Create - Checkbox topping List - based on ItemCategory.
      var toppingArea = document.querySelector('#ToppingArea');
      var toppingAreaChild = document.querySelector('#ToppingAreaChild');
      if (toppingAreaChild)
       {
          toppingAreaChild.remove() ;
       }
       toppingAreaChild = document.createElement("div");
       toppingAreaChild.setAttribute("id","ToppingAreaChild");
       var toppingCount =  button.data('nooftop');
       var toppings =  button.data('toppings');
       console.log(`toppingCount : ${toppingCount}`);
       console.log(`toppings : JSON.parse(${toppings})`);


    });

});



