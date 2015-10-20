var uiModules   = new uiModulesClass();

$(document).ready(function() {

    var $wish = $('#wish');
    var $md = $('#md-content');
    var $html = $('#html-content');

    var todoNotificationArea = $('#todos .notification-area');
    var todoNotificationIcon = $('#todos .notification-area > i');
    var todoNotificationText = $('#todos .notification-area > span');

    $('#zone .menu .item').tab({history:false});

    $('#wish-form').submit(function(e){
        e.preventDefault();
        var wish = $wish.val();

        $.get('/wish', {wish: wish}, function(resp) {
            var targetType = resp.type;

            if(targetType === 'remind') {
                var value = resp.response;

                $('#reminders table tbody').append(
                        $('<tr>').attr('id', value.id)
                            .append($('<td>').html(value.m))
                            .append($('<td>').html(value.t))
                            .append($('<td>').html(value.d))
                            .append($('<td>').append($('<i>').addClass('ui delete icon').click(function(){
                                    var $parentTr = $(this).parents("tr");
                                    $.post('/reminders/' + $parentTr.attr('id') + '/delete', function(resp) {
                                        $parentTr.remove();
                                    })
                            })))
                );
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

                $button.text('Edit Markdown');
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

    /* Load Todos */
    $.get('/todo/getid', function(resp){
        Cookies.set('todoid', resp.id);

        $.get('/todo/get', {id: Cookies.get('todoid')}, function(resp) {
            $md.val(resp.content);
            var md = window.markdownit();
            var result = md.render($md.val());
            $html.html(result);
        });
    });

    $('#reminders table tbody i').click(function(e){
        var $parentTr = $(this).parents("tr");
        $.post('/reminders/' + $parentTr.attr('id') + '/delete', function(resp) {
            $parentTr.remove();
        })
    });

});
