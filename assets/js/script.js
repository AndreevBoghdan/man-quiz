    $('.next-button__not-last').click(function(e){
        e.preventDefault();
        $(this).parent().hide();
        $(this).parent().next().show();
        
        hideStat();
        $('.answer-span').css("color", "rgb(44,59,74)");
        });

    $('.next-button__not-last').bind('touchstart', function(e){
        e.preventDefault();
        $(this).parent().hide();
        $(this).parent().next().show();
        
        hideStat();
        $('.answer-span').css("color", "rgb(44,59,74)");
        });

    $('.next-button__not-last').mousedown(function(e){
        e.preventDefault();
        $(this).parent().hide();
        $(this).parent().next().show();
        
        hideStat();
        $('.answer-span').css("color", "rgb(44,59,74)");
        });


    $('.back-button__not-first').click(function(e){
        e.preventDefault();
        $(this).parent().hide();
        $(this).parent().prev().show();

        hideStat()
        $('.answer-span').css("color", "rgb(44,59,74)");
        });

    $('.back-button__not-first').bind('touchstart', function(e){
        e.preventDefault();
        $(this).parent().hide();
        $(this).parent().prev().show();

        hideStat()
        $('.answer-span').css("color", "rgb(44,59,74)");
        });

    $('.back-button__not-first').mousedown(function(e){
        e.preventDefault();
        $(this).parent().hide();
        $(this).parent().prev().show();

        hideStat()
        $('.answer-span').css("color", "rgb(44,59,74)");
        });


    $('.back-button__first').click(function(e){
        e.preventDefault();
        window.external.PlayPreviousLcInChannelByName ('main');
        });

    $('.back-button__first').bind('touchstart',function(e){
        e.preventDefault();
        window.external.PlayPreviousLcInChannelByName ('main');
        });

    $('.back-button__first').mousedown(function(e){
        e.preventDefault();
        window.external.PlayPreviousLcInChannelByName ('main');
        });


    $('.next-button__last').click(function(e){
        e.preventDefault();
        window.external.playNextContentStartsNameInChannel('umfrage', 'main');
        });

    $('.next-button__last').bind('touchstart', function(e){
        e.preventDefault();
        window.external.playNextContentStartsNameInChannel('umfrage', 'main');
        });

    $('.next-button__last').mousedown(function(e){
        e.preventDefault();
        window.external.playNextContentStartsNameInChannel('umfrage', 'main');
        });
    
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }


    $('.answer').click(function(e){
        e.preventDefault();
        $(this).parent().parent().addClass('question-answered');
        var chosen = $(this);
        $('.question-answered').find('.answer').each(function( index ) {

            var question = $(this).parent().parent().attr('id');
            var answer = $(this).attr('value');
            $('#' + question +'-answer').attr("value",answer);
            var answerNumber = $(this).attr('number');
            var questionNumber = $('#'+ question).attr('number');
            $(this).attr('number', parseInt(answerNumber)+1);

            var ajaxUrl = $('#' + question + '_answer-' + answer + '-url').val();
            var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
            $.ajax({
                type: "POST",
                url: ajaxUrl,
                success: statChangedSecceed,
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
                });

            if ($(this).attr('number')==chosen.attr('number')){
                rate = (parseInt(answerNumber)+1) * 100 / (parseInt(questionNumber) + 1);
                $('#' + question + '_answer-' + answer + '-span').css("color", "red");
            } else {
                rate = (parseInt(answerNumber)) * 100 / (parseInt(questionNumber) + 1);
            }
            rate = rate.toFixed(2)
            $('#' + question + '_answer-' + answer + '-progress-span').text(rate + " %");
            $('#' + question + '_answer-' + answer + '-progress').width(rate + "%");
            $('#'+ question).attr('number', parseInt(questionNumber)+1);
        });
        showStat();

        });

    $('.answer').bind('touchstart', function(e){
        e.preventDefault();
        $(this).parent().parent().addClass('question-answered');
        var chosen = $(this);
        $('.question-answered').find('.answer').each(function( index ) {

            var question = $(this).parent().parent().attr('id');
            var answer = $(this).attr('value');
            $('#' + question +'-answer').attr("value",answer);
            var answerNumber = $(this).attr('number');
            var questionNumber = $('#'+ question).attr('number');
            $(this).attr('number', parseInt(answerNumber)+1);

            var ajaxUrl = $('#' + question + '_answer-' + answer + '-url').val();
            var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
            $.ajax({
                type: "POST",
                url: ajaxUrl,
                success: statChangedSecceed,
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
                });

            if ($(this).attr('number')==chosen.attr('number')){
                rate = (parseInt(answerNumber)+1) * 100 / (parseInt(questionNumber) + 1);
                $('#' + question + '_answer-' + answer + '-span').css("color", "red");
            } else {
                rate = (parseInt(answerNumber)) * 100 / (parseInt(questionNumber) + 1);
            }
            rate = rate.toFixed(2)
            $('#' + question + '_answer-' + answer + '-progress-span').text(rate + " %");
            $('#' + question + '_answer-' + answer + '-progress').width(rate + "%");
            $('#'+ question).attr('number', parseInt(questionNumber)+1);
        });
        showStat();

        });

    $('.answer').mousedown(function(e){
        e.preventDefault();
        $(this).parent().parent().addClass('question-answered');
        var chosen = $(this);
        $('.question-answered').find('.answer').each(function( index ) {

            var question = $(this).parent().parent().attr('id');
            var answer = $(this).attr('value');
            $('#' + question +'-answer').attr("value",answer);
            var answerNumber = $(this).attr('number');
            var questionNumber = $('#'+ question).attr('number');
            $(this).attr('number', parseInt(answerNumber)+1);

            var ajaxUrl = $('#' + question + '_answer-' + answer + '-url').val();
            var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
            $.ajax({
                type: "POST",
                url: ajaxUrl,
                success: statChangedSecceed,
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
                });

            if ($(this).attr('number')==chosen.attr('number')){
                rate = (parseInt(answerNumber)+1) * 100 / (parseInt(questionNumber) + 1);
                $('#' + question + '_answer-' + answer + '-span').css("color", "red");
            } else {
                rate = (parseInt(answerNumber)) * 100 / (parseInt(questionNumber) + 1);
            }
            rate = rate.toFixed(2)
            $('#' + question + '_answer-' + answer + '-progress-span').text(rate + " %");
            $('#' + question + '_answer-' + answer + '-progress').width(rate + "%");
            $('#'+ question).attr('number', parseInt(questionNumber)+1);
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

};

statChangedSecceed = function (){

};

interval = window.setInterval(function(){
    alert('every 300 sec mix-l exec');
}, 30000);


$('body').click(function(){
    window.clearInterval(interval);
    interval = window.setInterval(function(){
        alert('every 300 sec mix-l exec');
    }, 30000);

});

$('body').bind('touchstart', function(){
    window.clearInterval(interval);
    interval = window.setInterval(function(){
        alert('every 300 sec mix-l exec');
    }, 30000);

});

$('body').mousedown(function(){
    window.clearInterval(interval);
    interval = window.setInterval(function(){
        alert('every 300 sec mix-l exec');
    }, 30000);

});