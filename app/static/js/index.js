var uiModules   = new uiModulesClass();

$(document).ready(function() {

    var $wish = $('#wish');

    var todoNotificationArea = $('#todos .notification-area');
    var todoNotificationIcon = $('#todos .notification-area > i');
    var todoNotificationText = $('#todos .notification-area > span');

    $('#zone .menu .item').tab({history:false});
    $('.demo.menu .item').tab({history:false});

    $('.edit.button').click(function(e) {
        var $button = $(this);
        var $html = $button.siblings('.html-content');
        var $md = $button.siblings('.md-content');

        if($html.css('display') == 'none') {
            var md = window.markdownit();
            var result = md.render($md.val());
            $html.html(result);

            $button.text('Edit');
        }
        else {
            $button.text('Preview');
        }
        $md.toggle();
        $html.toggle();
    });

    $('#new-todo').click(function(e) {
        $button = $(this);
        $.post('/todos/create', function(resp) {
            var $menuItem = $('<a>').addClass('item').attr('data-tab', resp.id)
                                    .html(resp.name);
            var $todoContent = $('<div>').addClass('ui tab basic segment basic')
                                .attr('data-tab', resp.id)
                                .append(
                                    $('<textarea>').addClass('md-content')
                                        .attr('style', 'display:none;').html(resp.content)
                                )
                                .append(
                                    $('<div>').addClass('html-content').html('')
                                )
                                .append(
                                    $('<div>').addClass('ui orange edit button')
                                        .html('Edit Markdown')
                                );
            $button.parent().append($menuItem);
            $button.parent().parent().next().prepend($todoContent);
            $button.parent().children().last().tab({history:false});
        })
        .fail(function() {
            uiModules.showError('Something went wrong while creating a Todo');
        });
    })

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

    $.get('/commands', function(resp) {
        $('#commands').html(resp);
    });

    /* Load Todos */
    $.get('/todo/getid', function(resp){
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

    $('#webcomics .item').click(function(e) {
        var $item = $(this);
        var comic = $item.attr('id');

        $item.find('.button').addClass('loading');

        $.post('/webcomics/' + comic + '/sync', function(resp) {
            $item.find('p').html(resp.count);
        }).
        always(function() {
            $item.find('.button').removeClass('loading');
        });
    })

});
