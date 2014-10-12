$(document).ready( function(){ 
    $('.progress-bar').each(function(){
        var maximum = $(this).attr('data-max');
        var current = $(this).attr('data-current');
        var procentage = current / maximum * 100;

        $(this).width(procentage + '%');

        if (procentage >= 90) {
            $(this).addClass('progress-bar-danger')
        } else if (procentage >= 60) {
            $(this).addClass('progress-bar-warning')
        } else {
            $(this).addClass('progress-bar-info')
        }
    });

    var dateNow = new Date();
    if(dateNow.getMonth() >= 11 || dateNow.getMonth() == 0) {
        $.fn.snow({minSize: 10, maxSize: 25, newOn: 700});
        $('.container').add('<img id="christmas-panda" src="/static/images/panda_cut.png" alt="panda">');
    }


    var lendRequestButton = $('.lend-request');

    lendRequestButton.bind('click', function(event) {
        console.log(event);
        $.get('/lends/request', {
            'book': 1
        }, function(response) {
            lendRequestButton.toggleClass('btn-primary btn-success');
            lendRequestButton.text('Запазена');
        });
    });
});
