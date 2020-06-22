/*
 *  Document   : signup.js
 *  Author     : pixelcave
 *  Description: Custom javascript code used in Sign Up page
 */

var Signup = function() {

    return {
        init: function() {
            /* Jquery Validation, Check out more examples and documentation at https://github.com/jzaefferer/jquery-validation */
            /* Sign Up form - Initialize Validation */
            $('#form-sign-up').validate({
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
                    'name': {
                        required: true,
                        minlength: 2
                    },
                    'username': {
                        required: true,
                        minlength: 2
                    },
                    'email': {
                        required: true,
                        email: true
                    },
                    'password': {
                        required: true,
                        minlength: 5
                    },
                    // 'cpassword': {
                    //     required: true,
                    //     equalTo: '#password'
                    // },
                    'register-terms': {
                        required: true
                    }
                },
                messages: {
                    'name': {
                        required: 'Please enter your name',
                        minlength: 'Please enter your name'
                    },
                    'username': {
                        required: 'Please enter your username',
                        minlength: 'Please enter your username'
                    },
                    'email': 'Please enter a valid email address',
                    'password': {
                        required: 'Please provide a password',
                        minlength: 'Your password must be at least 5 characters long'
                    },
                    'cpassword': {
                        required: 'Please provide a password',
                        minlength: 'Your password must be at least 5 characters long',
                        equalTo: 'Please enter the same password as above'
                    },
                    'register-terms': {
                        required: 'Please accept the terms!'
                    }
                }
            });
        }
    };
}();