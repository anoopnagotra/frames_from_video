// File:           customjs.js
// Developer       Anoop Kumar
// Purpose         Custome functions and code
// Created Date    03-04-2020
$(document).ready(function() {
    $('#loginForm').validate();
    $('#forgotPasswordForm').validate();
    $('#contactForm').validate();

    $('#userEditProfile').validate();

    $("#restPassword").validate({
        rules: {
            "signupPassword": {
                required: true,
                minlength: 5
            },
            "signupCPassword": {
                required: true,
                minlength: 5,
                equalTo: "#signupPassword"
            }
        },
        messages: {
            "resetCPassword": " Confirm password should be same as password"
        }
    });

    $("#userChangePassword").validate({
        rules: {
            "userCurPassword": {
                required: true,
                minlength: 5
            },
            "userNPassword": {
                required: true,
                minlength: 5
            },
            "userCPassword": {
                required: true,
                minlength: 5,
                equalTo: "#userNPassword"
            }
        },
        messages: {
            "signupCPassword": " Confirm password should be same as password"
        }
    });

    $.validator.addMethod("valueNotEquals", function(value, element, arg){
      return arg !== value;
     }, "Value must not equal arg.");

    $("#signupForm").validate({
        rules: {
            "name": {
                required: true,
                minlength: 3
            },
            "username": {
                required: true,
                minlength: 3
            },
            "email": {
                required: true,
                email: true
            },
            "password": {
                required: true,
                minlength: 5
            },
            "state": {
                required: true,
                // valueNotEquals: "default" 
            },
            // "signupCPassword": {
            //     required: true,
            //     minlength: 5,
            //     equalTo: "#signupPassword"
            // }
            'register-terms': {
                required: true
            }
        },
        messages: {
        }
    });

    //Forgot Password
    $("#forgotPasswordForm").validate({
        ignore: ":hidden",
        rules: {
            email: {
                required: true,
                email: true
            }
        },
        submitHandler: function(form) {
            var email = $('#frgtEmail').val();
            $.ajax({
                type: "POST",
                url: "/forgot_password/",
                data: {
                    email: email
                },
                beforeSend: function() {
                    $('.sm-loader').show();
                },
                success: function(data) {
                    $('.sm-loader').hide();
                    $('.forgot-flash').show();
                    $("#forgotPasswordModal").modal("hide");
                }
            });
            return false;
        }

    });


    jQuery.validator.addMethod("dollarsscents", function(value, element) {
        return this.optional(element) || /^\d{0,4}(\.\d{0,2})?$/i.test(value);
    }, "You must include two decimal places");
    
    // $("#form-fie-add").form-file-update
    $("#form-file-add").validate({
        rules: {
            "doc_company": {
                required: true,
                minlength: 3
            },
            "doc_amount": {
                required: true,
                number: true,
                dollarsscents: true
            },
            "doc_number": {
                required: true,
                number: true
            },
            "doc_coustomer_number": {
                required: true,
                minlength: 3
            },
            "doc_search_key": {
                required: true,
                minlength: 3
            },
            "doc_notice": {
                required: true,
                minlength: 3,
            },
            "tax_number": {
                required: true,
                minlength: 3,
            },
        },
        messages: {
        }
    });


    $("#form-file-update").validate({
        rules: {
            "doc_company": {
                required: true,
                minlength: 3
            },
            "doc_amount": {
                required: true,
                number: true,
                dollarsscents: true
            },
            "doc_number": {
                required: true,
                number: true
            },
            "doc_coustomer_number": {
                required: true,
                minlength: 3
            },
            "doc_search_key": {
                required: true,
                minlength: 3
            },
            "doc_notice": {
                required: true,
                minlength: 3,
            },
            "tax_number": {
                required: true,
                minlength: 3,
            },
        },
        messages: {
        }
    });

});