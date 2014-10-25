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
        var bookId = lendRequestButton.data('book-id');
        var shouldCancel = lendRequestButton.data('should-cancel');

        console.log(shouldCancel);

        if(shouldCancel == 'yes') {
            $.get('/lends/cancel-request', {
                'book': bookId
            }, function(response) {
                lendRequestButton.data('should-cancel', 'no');
                lendRequestButton.text('Заявка за заемане');
            });
        } else {
            $.get('/lends/request', {
                'book': bookId
            }, function(response) {
                lendRequestButton.data('should-cancel', 'yes');
                lendRequestButton.text('Отмени заявката');
            }).fail(function() {
                $('#lend-request-error').text('Възникна грешка при обработката на заявката ви. Вероятно сте превишили максималния борй заявки за деня. Опитайте пак утре!');
            });
        }
    });
});
