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


    var lendRequestButton = $('#land');

    lendRequestButton.on('click', function(event) {
        if(lendRequestButton.data('cancel') == 'true') {
            $.get('/lends/cancel-request', {
                'book': lendRequestButton.data('book-id')
            }, function(response) {
                lendRequestButton.data('cancel', 'false');
                lendRequestButton.text('Заявка за заемане');
            });
        } else {
            $.get('/lends/request', {
                'book': lendRequestButton.data('book-id')
            }, function(response) {
                lendRequestButton.data('cancel', 'true');
                lendRequestButton.text('Отмени запазването');
            });
        }
    });

    var cancelLendRequestButton = $('#cancel-land');

    cancelLendRequestButton.on('click', function(event) {
        $.get('/lends/cancel-request', {
            'book': cancelLendRequestButton.data('book-id')
        }, function(response) {
            cancelLendRequestButton.attr('id','land');
            cancelLendRequestButton.toggleClass('btn-primary btn-success');
            cancelLendRequestButton.text('Заявка за заемане');
        });
    });
});
