window.onload = function() {
    $.getJSON("http://127.0.0.1:5000/api/categories/", function(data) {
        var categories = []
        $.each(data.categories, function(key, val) {
            var dropDown = document.getElementById('drop_down');
            option = document.createElement('option');
            option.value = val;
            option.innerHTML = val;
            dropDown.appendChild(option);
        })
    });
}
function getJoke() {
    var category = document.getElementById('cat_button').innerHTML;
    if (category == 'CATEGORIES' || category == 'ALL CATEGORIES') {
        url = 'http://127.0.0.1:5000/api/joke/';
    } else {
        url = 'http://127.0.0.1:5000/api/joke/category/' + category;
    }
    $.getJSON(url, function(data) {
        document.getElementById('joke').innerHTML = data.joke[0];
    });
}
function getCategories() {
    if ($('#drop_down').css('bottom') != '-120px') {
        $('#drop_down').attr('size',1);
        $('#drop_down').css('bottom','-120px');
        $('#drop_down').css('height','0%');
        $('#drop_down').css('border','none');
        var dropDown = document.getElementById("drop_down");
        var category = dropDown.options[dropDown.selectedIndex].value;
        document.getElementById('cat_button').innerHTML = category;
    } else {
        $('#drop_down').attr('size',6);
        $('#drop_down').css('bottom','100%');
        $('#drop_down').css('height','240px');
        $('#drop_down').css('border','solid');
        $('#drop_down').css('position','absolute');
    }
}
function openDocs() {
    $('#api_docs_content').modal();
    return false;
}
$('body').click(function(evt){
       if(evt.target.id == "api_docs_content"
        || evt.target.id == "api_docs_button")
          return;
      $.modal.close();

});