"use strict";

$(document).ready(function(){

  	function update_user_profile(evt){
  		evt.preventDefault();

		var formData = {
			"top_listing": top_listing,
			"accessory_listing": accessory_listing,
			"bottom_listing": bottom_listing,
			"dress_listing": dress_listing,
			"bag_listing": bag_listing,
			"shoe_listing": shoe_listing
		};

  		$.ajax({
  			type: 'post',
  			url: '/ensembles',
  			data: formData,
  			success:function(results){
  				$('#saved_ensemble').html(results)
  				console.log("success!!!!!" + results)
  			}

  		});
  			
  	}

  	$('#save_ensemble').on('click', update_user_profile)

});

