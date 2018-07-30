document.addEventListener('DOMContentLoaded', () => {
    //set_Your_channel_links();
                    document.querySelectorAll('.table-row').forEach(button => {
                    button.onclick = () => {
                        console.log(button.dataset.itemid);
                        console.log(button.dataset.itemcat);
                        console.log(button.dataset.nooftop);
                        return false;
                        };
                    });
});