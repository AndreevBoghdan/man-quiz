jQuery(document).ready(function ($) {
    var interactive = location.search.split('interactive=')[1] ? location.search.split('interactive=')[1] : '0';
    alert(interactive);
    if(interactive == 1){
        //alert("setMenuActive('menuItem2')");
        window.external.callMethodInChannelFramesByName("navi", "setMenuActive('menuItem2')");
    } else {
        //alert("resetAll()");        
        window.external.callMethodInChannelFramesByName("navi", "resetAll()");
    }
});




    $('.next-button__not-last').bind('touchstart', function(e){
        e.preventDefault();

        $(this).parent().hide();
        $(this).parent().next().show();
        hideStat();
        });

    $('.next-button__not-last').mousedown(function(e){
        e.preventDefault();
        $(this).parent().hide();
        $(this).parent().next().show();
        hideStat();
        });


    $('.back-button__not-first').bind('touchstart', function(e){
        e.preventDefault();
        $(this).parent().hide();
        $(this).parent().prev().show();

        hideStat()

        });

    $('.back-button__not-first').mousedown(function(e){
        e.preventDefault();
        $(this).parent().hide();
        $(this).parent().prev().show();

        hideStat()

        });


    $('.back-button__first').bind('touchstart',function(e){
        e.preventDefault();
        window.external.callMethodInChannelFramesByName("navi", "resetAll()");
        window.external.PlayPreviousLcInChannelByName ('main');
        });

    $('.back-button__first').mousedown(function(e){
        e.preventDefault();
        window.external.callMethodInChannelFramesByName("navi", "resetAll()");
        window.external.PlayPreviousLcInChannelByName ('main');
        });


    $('.next-button__last').bind('touchstart', function(e){
        e.preventDefault();
        window.external.callMethodInChannelFramesByName("navi", "setMenuActive('menuItem2')");
        window.external.playNextContentStartsNameInChannel('umfrage', 'main');
        });

    $('.next-button__last').mousedown(function(e){
        e.preventDefault();
        window.external.callMethodInChannelFramesByName("navi", "setMenuActive('menuItem2')");
        window.external.playNextContentStartsNameInChannel('umfrage', 'main');
        });
    
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }



    $('.answer').bind('touchstart', function(e){
        e.preventDefault();

        $(this).parent().parent().addClass('question-answered');
        var chosen = $(this);
        var question = $(this).parent().parent().attr('id');
        var questionNumber = $('#'+ question).attr('number');
        $('#'+ question).attr('number', parseInt(questionNumber) + 1);
        $('.question-answered').find('.answer').each(function( index ) {
            var answer = $(this).attr('value');
            $('#' + question +'-answer').attr("value",answer);
            var answerNumber = $(this).attr('number');

            if ($(this).attr('value')==chosen.attr('value')){
                var ajaxUrl = "http://h1475695.stratoserver.net" + $('#' + question + '_answer-' + answer + '-url').val();
                var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
                $.ajax({
                    type: "POST",
                    url: ajaxUrl,
                    success: statChangedSecceed,
                    error:  function(resp){
                        console.log(resp.responseText);
                    }, 
                    beforeSend: function(xhr, settings) {
                            xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                    });
                $(this).attr('number', parseInt(answerNumber)+1);
                rate = (parseInt(answerNumber)+1) * 100 / (parseInt(questionNumber)+1);
                $('#' + question + '_answer-' + answer + '-span').css("color", "rgb(230,0,70)");
            } else {
                rate = (parseInt(answerNumber)) * 100 / (parseInt(questionNumber)+1);
            }
            rate = rate.toFixed(2)
            $('#' + question + '_answer-' + answer + '-progress-span').text(rate + " %");
            $('#' + question + '_answer-' + answer + '-progress').width(rate + "%");
        });
        showStat();

        });

    $('.answer').mousedown(function(e){
        e.preventDefault();

        $(this).parent().parent().addClass('question-answered');
        var chosen = $(this);
        var question = $(this).parent().parent().attr('id');
        var questionNumber = $('#'+ question).attr('number');
        $('#'+ question).attr('number', parseInt(questionNumber) + 1);
        $('.question-answered').find('.answer').each(function( index ) {
            var answer = $(this).attr('value');
            $('#' + question +'-answer').attr("value",answer);
            var answerNumber = $(this).attr('number');

            if ($(this).attr('value')==chosen.attr('value')){
                var ajaxUrl = "http://h1475695.stratoserver.net" + $('#' + question + '_answer-' + answer + '-url').val();
                var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
                $.ajax({
                    type: "POST",
                    url: ajaxUrl,
                    success: statChangedSecceed,
                    error:  function(resp){
                        console.log(resp.responseText);
                    },
                    beforeSend: function(xhr, settings) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                    });
                $(this).attr('number', parseInt(answerNumber)+1);
                rate = (parseInt(answerNumber)+1) * 100 / (parseInt(questionNumber)+1);
                $('#' + question + '_answer-' + answer + '-span').css("color", "rgb(230,0,70)");
            } else {
                rate = (parseInt(answerNumber)) * 100 / (parseInt(questionNumber)+1);
            }
            rate = rate.toFixed(2)
            $('#' + question + '_answer-' + answer + '-progress-span').text(rate + " %");
            $('#' + question + '_answer-' + answer + '-progress').width(rate + "%");
        });
        showStat();

        });

showStat = function (){
    $('.question-answered').last().find('.answer').hide();
    $('.question-answered').last().find('.statistic').show();
    $('.question-answered').last().find('.statistic').css("display", "inline-block");

};

hideStat = function (){
    $('.question-answered').last().find('.answer').show();
    $('.question-answered').last().find('.statistic').hide();
    $('.question-answered').removeClass('question-answered');

    $('.answer-span').each(function( index ) {
        var id = $(this).attr("id");
        $('#'+id).css("color", "rgb(44,59,74)");
    });

};

statChangedSecceed = function (){

};

timeout = window.setTimeout(function(){
    window.external.callMethodInChannelFramesByName("navi", "resetAll()");
    window.external.HTMLTemplateComplete(window.name);
}, 30000);


$('body').bind('touchstart', function(){
    window.clearTimeout(timeout);
    timeout = window.setTimeout(function(){
        window.external.callMethodInChannelFramesByName("navi", "resetAll()");
        window.external.HTMLTemplateComplete(window.name);
    }, 120000);

});

$('body').mousedown(function(){
    window.clearTimeout(timeout);
    timeout = window.setTimeout(function(){
        window.external.callMethodInChannelFramesByName("navi", "resetAll()");
        window.external.HTMLTemplateComplete(window.name);
    }, 120000);

});