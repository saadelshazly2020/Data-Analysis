$(function(){
	$('button').click(function(){
		
		$.ajax({
			url: '/predict',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				$('#result').text(response)
				console.log(response);
			},
			error: function(error){
				
				console.log(error);
			}
		});
	});
});