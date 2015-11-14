var markdown = window.markdownit();

$(document).ready(function() {


    var $wish = $('#wish');

    var todoNotificationArea = $('#todos .notification-area');
    var todoNotificationIcon = $('#todos .notification-area > i');
    var todoNotificationText = $('#todos .notification-area > span');

    $('#news-stream .menu .item').tab({history:false});
    $('.todo.menu .item').tab({history:false});
    $('.top.menu .item').tab({history:false});

    $('body').on('click', '.button', function() {
        $(this).transition('pulse');
    })

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
                var error = resp.error

                if (error) {
                    uiModules.showError(error);
                    return;
                }

                $('#reminders table tbody').append(
                        $('<tr>').attr('id', value.id)
                            .append($('<td>').html(value.m))
                            .append($('<td>').html(value.t))
                            .append($('<td>').html(value.d))
                            .append($('<td>').append($('<i>').addClass('ui delete red icon')))
                );
            }
            else if(targetType === 'comic') {
                var link = resp.response;
                var error = resp.error

                if (error) {
                    uiModules.showError(error);
                    return;
                }

                var $webcomicmodal = $('#webcomic-modal');

                $webcomicmodal.find('.header').html(link.title);
                $webcomicmodal.find('a').attr('href', link.url);

                var showModal = true;
                if (link.content_type == 'image') {
                    $webcomicmodal.find('img').attr('src', link.content_url);
                }
                else if (link.content_type == 'page') {
                    alert('Page found');
                }
                else {
                    showModal = false;
                    uiModules.showError('Unsuported content_type ' + link.content_type);
                }

                if( showModal ) {
                    $webcomicmodal.modal({
                        context: 'html',
                        observeChanges: true,
                        onVisible: function () {
                            $webcomicmodal.modal("refresh");
                        }
                    }).modal('show');
                }

            }
            else if(targetType === 'astro') {
                var url = resp.response;
                var error = resp.error

                if (error) {
                    uiModules.showError(error);
                    return;
                }

                $('#astro-modal iframe').attr('src', url);
                $('#astro-modal').modal({
                    onVisible: function () {
                        $("#astro-modal").modal("refresh");
                    }
                }).modal('show');

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

        $button.addClass('disabled');

        $.post('/webcomics/' + comic_id + '/sync', function(response) {
            $comic.find('p').text(response.resp.links_count);
            $comic.find('label').text(response.resp.last_sync);
        }).
        always(function() {
            $button.removeClass('disabled');
        });
    });

    $('#astros .button').click(function(e) {
        var $astro = $(this).parent()

        var astro_id = $astro.attr('id');
        var $button = $astro.find('.button');

        $button.addClass('disabled');

        $.post('/astros/' + astro_id + '/sync', function(response) {
            $astro.find('p').text(response.resp.links_count);
            $astro.find('label').text(response.resp.last_sync);
        }).
        always(function() {
            $button.removeClass('disabled');
        });
    });


    $('#create-playlist-button').click(function(e) {
        var $playlist_name = $('#playlist-name');
        var name = $playlist_name.val();

        if(!name) {
            uiModules.showError('Playlist name cannot be empty');
            return;
        }

        name = name.trim();

        $.post('/music/playlist/create', {name:name}, function(resp) {
            if(resp.error) {
                uiModules.showError(resp.error);
                return;
            }
            $('#music .playlists').append(resp.html);
            $playlist_name.val(null);
        });
    });

    $('#music').on('click', 'i.delete-playlist', function(e) {
        var $playlist_element = $(this).parents('div');
        var playlist_id = $playlist_element.attr('id');

        $.post('/music/playlist/delete', {id:playlist_id}, function(resp) {
            if(resp.error) {
                uiModules.showError(resp.error);
                return;
            }
            if(resp.resp) {
                $('#' + playlist_id).remove();
                uiModules.notify('Playlist deleted successfully');
            }
            else {
                uiModules.showError('Playlist not deleted');
            }
        })
    });

    $('#music').on('click', '.youtube-link button', function(e) {
        var $button = $(this);
        var $link_input = $(this).siblings('input');
        var link = $link_input.val();
        if(!link) {
            $link_input.parent().addClass('error');
            uiModules.showError('No link found');
            return;
        }
        var playlist_id = $button.parents('div.playlist').attr('id');
        var $playlist_element = $('#' + playlist_id);

        $button.addClass('loading');

        $.post('/music/playlist/'+ playlist_id +'/add', {link: link, site: 'youtube'}, function(resp) {
            if(resp.error) {
                uiModules.showError(resp.error);
                return;
            }
            $playlist_element.find('.update-field').text(resp.resp.updated_at);
            $playlist_element.find('.links-count').text(resp.resp.links_count)
        }).always(function(){
            $link_input.val(null);
            $button.removeClass('loading');
        });
    });

    $('#music').on('click', '.random-music', function(e) {
        var $button = $(this);
        var playlist_id = $button.parents('div.playlist').attr('id');
        var $playlist_element = $('#' + playlist_id);

        $.get('/music/playlist/'+ playlist_id +'/random', function(resp) {
            var video_id = resp.resp.video_id;
            var $musicmodal = $('#music-modal');

            $musicmodal.find('.header').html(resp.resp.title);

            $musicmodal.modal({
                context: 'html',
                observeChanges: true,
                onVisible: function () {
                    $musicmodal.modal("refresh");
                    music_player.loadVideoById(video_id, 0, "large")
                },
                onHidden: function() {
                    music_player.stopVideo();
                }
            }).modal('show');

        }).fail(function(response) {
            uiModules.showError(response.responseText);
        })

    });


    $('#music').on('click', '.full-playlist', function(e) {
        var $button = $(this);
        var playlist_id = $button.parents('div.playlist').attr('id');
        var $playlist_element = $('#' + playlist_id);

        var playlist_name = $playlist_element.find('a.header').text();

        $.get('/music/playlist/'+ playlist_id +'/all', function(resp) {

            var $musicmodal = $('#music-modal');

            $musicmodal.find('.header').html(resp.resp.title);

            $musicmodal.modal({
                context: 'html',
                observeChanges: true,
                onVisible: function () {
                    $musicmodal.modal("refresh");
                    var ids = [];
                    for( var i = 0; i < 100 && i < resp.resp.length ; i++ ) {
                        var video = resp.resp[i];
                        ids.push(video.video_id);
                    }
                    music_player.loadPlaylist(ids);
                },
                onHidden: function() {
                    music_player.stopVideo();
                }
            }).modal('show');

        }).fail(function(response) {
            uiModules.showError(response.responseText);
        })

    });

});
