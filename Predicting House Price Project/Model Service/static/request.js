

$(function(){
	$('button').click(function(){
		//console.log($("#aminities").val())
		console.log('ok')
		$('#hidden-aminities-id').val($("#aminities").val())
		console.log('current val : ',$('#hidden-aminities-id').val())
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

$( document ).ready(function() {
	console.log( "ready5!" );
	   $.ajax({
			url: '/cities',
			type: 'GET',
			success: function(response){
				var $select_elem = $('.select-city');
				$select_elem.empty();
				$select_elem.append('<option value="Select City"></option>');
				$.each(response, function (idx,city) {
					$select_elem.append('<option value="' + city + '">' + city + '</option>');
				});
				$select_elem.chosen({ width: "95%",no_results_text:"Not found" });

				console.log("cities");
				console.log(response);
			},
			error: function(error){
				
				console.log(error);
			}
		});

		// Compound 
		$.ajax({
			url: '/compound',
			type: 'GET',
			success: function(response){
				var $select_elem = $('.select-comp');
				$select_elem.empty();
				$select_elem.append('<option value="Not in Compound"></option>');
				$.each(response, function (idx,comp) {
					$select_elem.append('<option value="' + comp + '">' + comp + '</option>');
				});
				$select_elem.chosen({ width: "95%",no_results_text:"Not found" });
				console.log(response);
			},
			error: function(error){
				
				console.log(error);
			}
		});

			// aminities 
			$.ajax({
				url: '/aminities',
				type: 'GET',
				success: function(response){
					var $select_elem = $('.chosen-select');
					$select_elem.empty();
					$select_elem.append('<option value="No"></option>');
					$.each(response, function (idx,amnt) {
						$select_elem.append('<option value="' + amnt + '">' + amnt + '</option>');
					});
					$select_elem.chosen({ width: "95%",no_results_text:"Not found" });
					console.log(response);
				},
				error: function(error){
					
					console.log(error);
				}
			});
		// on change
		// $("#aminities").chosen().change(function(){
			
		// });

});

