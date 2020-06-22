/*
 *  Document   : login.js
 *  Author     : pixelcave
 *  Description: Custom javascript code used in Log In page
 */

var Reset = function() {

    return {
        init: function() {
            /* Jquery Validation, Check out more examples and documentation at https://github.com/jzaefferer/jquery-validation */
            /* Log In form - Initialize Validation */
            $('#restPassword').validate({
                errorClass: 'help-block animation-slideDown', // You can change the animation class for a different entrance animation - check animations page
                errorElement: 'div',
                errorPlacement: function(error, e) {
                    e.parents('.form-group > div').append(error);
                },
                highlight: function(e) {
                    $(e).closest('.form-group').removeClass('has-success has-error').addClass('has-error');
                    $(e).closest('.help-block').remove();
                },
                success: function(e) {
                    e.closest('.form-group').removeClass('has-success has-error');
                    e.closest('.help-block').remove();
                },
                rules: {
                    'signupPassword': {
                        required: true,
                        minlength: 5
                    },
                    'signupCPassword': {
                        required: true,
                        minlength: 5
                    }
                },
                messages: {
                    'signupPassword': {
                        required:'Please provide your password',
                        minlength: 'Your password must be at least 5 characters long'
                    },
                    'signupCPassword': {
                        required: 'Please confirm your password',
                        minlength: 'Your password must be at least 5 characters long'
                    }
                }
            });
        }
    };
}();