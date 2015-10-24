var uiModules   = new uiModulesClass();
var markdown = window.markdownit();

$(document).ready(function() {

    var $wish = $('#wish');

    var todoNotificationArea = $('#todos .notification-area');
    var todoNotificationIcon = $('#todos .notification-area > i');
    var todoNotificationText = $('#todos .notification-area > span');

    $('#zone .menu .item').tab({history:false});
    $('.demo.menu .item').tab({history:false});

    $('#todos').ready(function() {
        $.each($('#todos .segment'), function(index, $element){
            var $html, $md;

            $element = $($element);

            $md = $element.find('.md-content-name');
            $html = $element.find('.html-content-name');

            $html.html(markdown.render($md.val()));

            $md = $element.find('.md-content');
            $html = $element.find('.html-content');

            $html.html(markdown.render($md.val()));
        });
    });

    $('#todos').on('click', '.edit.button', function() {
        var $button = $(this);
        var $html = $button.parent().siblings('.html-content');
        var $md = $button.parent().siblings('.md-content');
        var $htmlname = $button.parent().siblings('.html-content-name');
        var $mdname = $button.parent().siblings('.md-content-name');

        if($html.css('display') == 'none') {
            var result = markdown.render($md.val());
            $html.html(result);

            result = markdown.render($mdname.val());
            $htmlname.html(result);

            $button.text('Edit');
        }
        else {
            $button.text('Preview');
        }
        $md.toggle();
        $html.toggle();
        $mdname.toggle();
        $htmlname.toggle();
    });

    $('#todos').on('click', '.save.button', function() {
        var $button = $(this);
        var $mdname = $button.parent().parent().find('input');
        var $md = $button.parent().parent().find('textarea');
        var id = $button.parent().parent().attr('data-tab');

        $.post('/todos/save', {id:id, name: $mdname.val(), content: $md.val()}, function(resp){
            console.log('Saved');
        });
    });

    $('#todos').on('click', '.delete.button', function() {
        var $button = $(this);
        var id = $button.parent().parent().attr('data-tab');

        $.post('/todos/delete', {id:id}, function(resp){
            $('*[data-tab="'+id+'"]').remove();
        });
    });

    $('#new-todo').click(function(e) {
        $button = $(this);
        $.post('/todos/create', function(resp) {
            var $menuItem = $('<a>').addClass('item').attr('data-tab', resp.id)
                                    .html(resp.name);
            var $todoContent = $('<div>').addClass('ui tab basic segment basic')
                                .attr('data-tab', resp.id)
                                .append(
                                    $('<div>').addClass('ui text menu right floated')
                                        .append($('<div>').addClass('ui edit basic button item').text('Edit'))
                                        .append($('<div>').addClass('ui save basic button item').text('Save'))
                                        .append($('<div>').addClass('ui download basic button item').text('Download'))
                                        .append($('<div>').addClass('ui delete basic button item').text('Delete'))
                                )
                                .append(
                                    $('<div>').addClass('ui section divider')
                                )
                                .append(
                                    $('<input>').addClass('ui fluid md-content-name')
                                        .attr('style', 'display:none;').val(resp.name)
                                )
                                .append(
                                    $('<div>').addClass('html-content-name').html(markdown.render(resp.name))
                                )
                                .append(
                                    $('<div>').addClass('ui horizontal divider')
                                )
                                .append(
                                    $('<textarea>').addClass('md-content')
                                        .attr('style', 'display:none;').html(resp.content)
                                )
                                .append(
                                    $('<div>').addClass('html-content')
                                );
            $button.parent().append($menuItem);
            $button.parent().parent().next().prepend($todoContent);
            $button.parent().children().last().tab({history:false});
        })
        .fail(function() {
            uiModules.showError('Something went wrong while creating a Todo');
        });
    })

    $('#reminders').on('click', 'i.delete', function(e){
        var $parentTr = $(this).parents("tr");
        $.post('/reminders/' + $parentTr.attr('id') + '/delete', function(resp) {
            $parentTr.remove();
        })
    });

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
                            .append($('<td>').append($('<i>').addClass('ui delete red icon')))
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

    $('#webcomics .button').click(function(e) {
        var $comic = $(this).parent()

        var comic_id = $comic.attr('id');
        var $button = $comic.find('.button');

        $button.addClass('loading');

        $.post('/webcomics/' + comic_id + '/sync', function(response) {
            $comic.find('p').text(response.resp.links_count);
            $comic.find('label').text(response.resp.last_sync);
        }).
        always(function() {
            $button.removeClass('loading');
        });
    })

});
