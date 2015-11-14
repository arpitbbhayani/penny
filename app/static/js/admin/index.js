$(document).ready(function() {
    $('.ui.checkbox').checkbox();
    $('.sortable.table').tablesort();
    $('body').on('click', '.button, input[type="submit"]', function() {
        $(this).transition('pulse');
    })
    $('input[readonly]').css('color', '#DDD');
});
