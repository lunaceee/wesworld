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

   $('#save_ensemble').on('click', update_user_profile);
  
  }

  $(document).on("change", "#selected_movie", function(){
    // console.log("to change movie")
    
    var selectedMovie = {
      "movie_name": $("#selected_movie").val()
    };

    $.ajax({
      type: 'get',
      url: '/search_json',
      data: selectedMovie,
      success:function(results){
        $("#a_img").attr('src', results['a_img_url']);
        $("#a_listing").attr('href', results['accessory_listing']);

        $("#b_img").attr('src', results['b_img_url']);
        $("#b_listing").attr('href', results['bag_listing']);

        $("#bo_img").attr('src', results['bo_img_url']);
        $("#bo_listing").attr('href', results['bottom_listing']);

        $("#d_img").attr('src', results['d_img_url']);
        $("#d_listing").attr('href', results['dress_listing']);

        $("#s_img").attr('src', results['s_img_url']);
        $("#s_listing").attr('href', results['shoe_listing']);

        $("#t_img").attr('src', results['t_img_url']);
        $("#t_listing").attr('href', results['top_listing']);

        // console.log("changed movie", results);
      }
    });

  });


// function openCity(evt, ensemble) {
//     var i, x, tablinks;
//     x = document.getElementsByClassName("city");
//     for (i = 0; i < x.length; i++) {
//         x[i].style.display = "none";
//     }
//     tablinks = document.getElementsByClassName("tablink");
//     for (i = 0; i < x.length; i++) {
//         tablinks[i].className = tablinks[i].className.replace(" w3-red", "");
//     }
//     document.getElementById(cityName).style.display = "block";
//     evt.currentTarget.className += " w3-red";
// }




});

