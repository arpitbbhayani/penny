var uiModules   = new uiModulesClass();

$(document).ready(function() {

    var $wish = $('#wish');
    var $md = $('#md-content');
    var $html = $('#html-content');

    var todoNotificationArea = $('#todos .notification-area');
    var todoNotificationIcon = $('#todos .notification-area > i');
    var todoNotificationText = $('#todos .notification-area > span');

    $('#wish-form').submit(function(e){
        e.preventDefault();
        var wish = $wish.val();

        $.get('/wish', {wish: wish}, function(resp) {
            var targetType = resp.type;

            if(targetType === 'remind') {

            }
            else {
                uiModules.showError('Invalid type ' + resp.type);
            }
            // $('#reply').addClass('animated slideInDown').html(resp.response.message);
            // setTimeout(function() {
            //     $('#reply').removeClass('animated slideInDown');
            // }, 1000);
        });

        $wish.val(null);
    });

    $('#wish-form').visibility({
        type   : 'fixed',
        offset : 15
    });

    $('#toggle-md-div').click(function(e) {
        e.preventDefault();

        var $button = $(this);
        if($html.css('display') == 'none') {

            $.post('/todo/save', {id: Cookies.get('todoid'), mdcontent: $md.val()}, function(resp) {
                uiModules.notify('Data saved successfully');
            })
            .fail(function() {
                uiModules.showError('Something went wrong while saving the data');
            })
            .always(function() {
                var md = window.markdownit();
                var result = md.render($md.val());
                $html.html(result);

                $button.text('Edit');
            });
        }
        else {
            $button.text('Save & Preview');
        }
        $md.toggle();
        $html.toggle();
    });

    $.get('/commands', function(resp) {
        $('#commands').html(resp);
    });

    $.get('/todo/getid', function(resp){
        Cookies.set('todoid', resp.id);

        $.get('/todo/get', {id: Cookies.get('todoid')}, function(resp) {
            $md.val(resp.content);
        });
    });
});
