$('#flashes').transition('bounce', {
    onComplete: function() {
        setTimeout(function() {
            $('#flashes').transition('fade out');
        }, 5000);
    }
});

var uiModules = {
    /*
     *  uiModulesClass: Class that defines the UI Modules
     *  Contains all the methods that would enable showing errors,
     *  show waiting ticker, context menu .. etc.
     */

    notify : function(response) {
        $('#msg')
                .removeClass('negative positive')
                .addClass('info')
                .html(response)
                .transition('bounce', {
                    onComplete: function() {
                        setTimeout(function() {
                            $('#msg').transition('fade out');
                        }, 5000);
                    }
                });
    },

    showError : function(response) {
    var error = response.error;
        if (!error) {
            error = response;
        }
        $('#msg')
                .removeClass('info positive')
                .addClass('negative')
                .html(response)
                .transition('bounce', {
                    onComplete: function() {
                        setTimeout(function() {
                            $('#msg').transition('fade out');
                        }, 5000);
                    }
                });
    }
};
