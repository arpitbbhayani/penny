$('#flashes').transition('pulse');
$('#flashes, #msg').click(function(){
    $(this).transition('fade out');
});

var uiModules = {
    /*
     *  uiModulesClass: Class that defines the UI Modules
     *  Contains all the methods that would enable showing errors,
     *  show waiting ticker, context menu .. etc.
     */

    notify : function(response) {
        $('#msg').removeClass('negative positive').addClass('info').html(response).transition('bounce');
        $('#msggrid').show();
    },

    showError : function(response) {
    var error = response.error;
        if (!error) {
            error = response;
        }
        $('#msg').removeClass('info positive').addClass('negative').html(error).transition('bounce');
        $('#msggrid').show();
    },

    showWaiting : function(targetElement) {
        targetElement.html('<i class="fa fa-spinner fa-spin"></i>');
    },

    removeWaiting : function(targetElement) {
        targetElement.html(null);
    }
};
