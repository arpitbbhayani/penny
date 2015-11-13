$(document).ready(function() {
    $('body').on('click', '.button, input[type="submit"]', function() {
        $(this).transition('pulse');
    })
});
