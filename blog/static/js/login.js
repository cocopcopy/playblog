
$(document).ready(function() {
	// 单件注册选项
	$('a#signup-link').on('click', function(event) {
		event.preventDefault();

		$('a#signin-link').removeClass('active')
		$(this).addClass('active');

		$('div#signin-block').hide();
		$('div#signup-block').show();
		$('span.slider-bar').animate({
			position: 'relative',
			left: 0
		},{
			duration: 'fast'
		});
	});
	// 单击登录选项
	$('a#signin-link').on('click', function(event) {
		event.preventDefault();

		$('a#signup-link').removeClass('active');
		$(this).addClass('active');

		$('div#signup-block').hide();
		$('div#signin-block').show();
		$('span.slider-bar').animate({
			position: 'relative',
			left: '4em'
		}, {
			duration: 'fast'
		});
	});
})