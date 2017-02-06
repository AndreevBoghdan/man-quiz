jQuery(document).ready(function ($) {
    $('.next-button__not-last').click(function(e){
        e.preventDefault();
        $(this).parent().hide();
        $(this).parent().next().show();
        });

    $('.back-button__not-first').click(function(e){
        e.preventDefault();
        $(this).parent().hide();
        $(this).parent().prev().show();
        });

    $('.back-button__first').click(function(e){
        e.preventDefault();
        alert('not implemented');
        });

    $('.next-button__last').click(function(e){
        e.preventDefault();
        alert('not implemented');
        });

})

