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
	})
});