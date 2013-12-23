var subNavOpen = false;
window.onload = function() {
    $.getJSON("/api/joke/", function(data) {
        document.getElementById('joke').innerHTML = data.joke[0];
    });
    $.getJSON("/api/categories/", function(data) {
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
        url = '/api/joke/';
    } else {
        url = '/api/joke/category/' + category;
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
function openSubNav() {
    if ($('#sub_nav').css('display') == 'none') {
        $('#sub_nav').css('display', 'inline');
    }
}
$('body').click(function(evt){
    if(evt.target.id == "api_docs_content"
     || evt.target.id == "api_docs_button") {
        return;
    }
    $.modal.close();
    if ($('#sub_nav').css('display') != 'none'
        && !subNavOpen) {
        subNavOpen = true;
    } else if ($('#sub_nav').css('display') != 'none'
        && subNavOpen
        && evt.target.id != "sub_nav") {
        $('#sub_nav').css('display', 'none');
        subNavOpen = false;
    }
});