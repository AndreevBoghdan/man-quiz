

    $('.next-button__not-last').click(function(e){
        e.preventDefault();
        $(this).parent().hide();
        $(this).parent().next().show();
        if ( ($(this).parent().attr('id') ==  $('.question').first().attr('id')) && ($('.question-answered').length==1)){
            $('.back-button__not-first').first().off('click');
            $('.back-button__not-first').first().attr("class","navigation-button back-button back-button__first");

                $('.back-button__first').click(function(e){
                    e.preventDefault();
                    alert('not implemented');
                    });

        }
        $('.question-answered').remove();
        });


    $('.back-button__not-first').click(function(e){
        e.preventDefault();
        $(this).parent().hide();
        $(this).parent().prev().show();
        if ( ($(this).parent().attr('id') ==  $('.question').last().attr('id')) && ($('.question-answered').length==1) ){
            $('.next-button__not-last').last().off('click');
            $('.next-button__not-last').last().attr("class","navigation-button next-button next-button__last");

                $('.next-button__last').click(function(e){
                    e.preventDefault();
                    alert('not implemented');
                    });

        }
        $('.question-answered').remove();
        });


    $('.back-button__first').click(function(e){
        e.preventDefault();
        alert('not implemented');
        });


    $('.next-button__last').click(function(e){
        e.preventDefault();
        alert('not implemented');
        });


    $('.answer').click(function(e){
        e.preventDefault();
        $(this).parent().parent().addClass('question-answered');
        var question = $(this).parent().parent().attr('id');
        var answer = $(this).attr('value');
        $('#' + question +'-answer').attr("value",answer);
        var answerNumber = $(this).attr('number');
        var questionNumber = $('#'+ question).attr('number');
        $(this).attr('number', parseInt(answerNumber)+1);
        var isRight = $('#'+ question+'_answer-'+answer+'-span').attr('is-right');
            if (isRight=="True"){
                $('#'+ question+'_answer-'+answer+'-span').css("color", "green");

            } else {
                $('#'+ question+'_answer-'+answer+'-span').css("color", "red");
            }
        rate = parseInt(answerNumber+1) * 100 / (parseInt(questionNumber)+1);
        $('#'+ question+'_answer-'+answer+'-progress-span').text(rate + " %");
        $('#'+ question+'_answer-'+answer+'-progress').width(rate + "%");
        showStat();
        });

showStat = function (){
    $('.question-answered').last().find('.answer').hide();
    $('.question-answered').last().find('.statistic').show();
    $('.question-answered').last().find('.statistic').css("display", "inline-block");

};

