$(document).ready(function() {

    var $wish = $('#wish');

    $('#wish-form').submit(function(e){
        e.preventDefault();
        var wish = $wish.val();

        $.get('/wish', {wish: wish}, function(resp) {
            console.log(resp.response);
            $('#reply').addClass('animated slideInDown').html(resp.response.message);
            setTimeout(function() {
                $('#reply').removeClass('animated slideInDown');
            }, 1000);
        });

        $wish.val(null);
    });
});
