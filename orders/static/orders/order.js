document.addEventListener('DOMContentLoaded', () => {
    //set_Your_channel_links();
       /*
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
           */


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
       toppingArea.appendChild(toppingAreaChild);

       var toppingCount =  button.data('nooftop');
       var p_toppings =  button.data('p_toppings');
       var s_toppings =  button.data('s_toppings');

       var toppings = false;
      // p_toppings = JSON.parse(JSON.stringify(p_toppings))
       if(button.data('itemcat') == 'Pizza' && toppingCount > 0)
       {
            toppings =p_toppings;
       }
       else if (button.data('itemcat') == 'Subs')
       {
            toppings = s_toppings;
       }
       if(toppings){
           toppingAreaChild.innerHTML='<strong>Choice of Toppings:</strong>';
           console.log(`toppingCount : ${toppingCount}`);
           for(var idx =0; idx < toppings.length; idx++)
            {
                console.log(toppings[idx][1]);
                var seperator = document.createElement('div');

                var checkbox = document.createElement('input');
                var label = document.createElement('label');
                checkbox.type = "checkbox";
                checkbox.name = "topping";
                checkbox.className = "c_topping";
                checkbox.value = toppings[idx][1]+'($'+toppings[idx][2] +')';
                checkbox.id = toppings[idx][0];
                checkbox.onclick= ()=> {
                        //console.log('Inside validateToppingCount');
                        //console.log(toppingCount);
                        var checkboxes = document.getElementsByName("topping");
                        var numberOfCheckedItems = 0;
                        for(var i = 0; i < checkboxes.length; i++)
                        {
                            if(checkboxes[i].checked)
                                numberOfCheckedItems++;
                        }
                        if(numberOfCheckedItems >= toppingCount)
                        {
                            //console.log('we have reached the limit - of Toppings');
                            // loop thru and disable all the unchecked
                            for (var i=0; i< checkboxes.length; i++)
                             {
                                 if (! checkboxes[i].checked)
                                    checkboxes[i].disabled = true;
                             }
                        //return false;
                        }
                        else
                        {
                            //loop thru and enable all
                            for (var i=0; i< checkboxes.length; i++)
                             {
                               checkboxes[i].disabled = false;
                             }
                        }
                };

                label.htmlFor = toppings[idx][0];
                label.innerText = toppings[idx][1]+'($'+toppings[idx][2] +')';
                toppingAreaChild.appendChild(seperator);
                seperator.appendChild(checkbox);
                seperator.appendChild(label);
            }
       }
      // return false;
        // adding inside the model handler - so we can extract the values needed.
        var addToCartbtn = document.querySelector('#addToCartbtn');
             addToCartbtn.onclick = () => {
                        console.log('inside add to cart button');
                        console.log(button.data('itemname'));
                        console.log(button.data('itemid'));
                        // Post the data to the back-end Order Table
                        // Update the Cart

                        };

    });

});

