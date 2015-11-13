$(document).ready(function() {
    $('.sortable.table').tablesort();
    $('body').on('click', '.button, input[type="submit"]', function() {
        $(this).transition('pulse');
    })
});
