"use strict";

$(document).ready(function(){
  $('.modal').modal();

  $('.modal_trigger').click(function(e){
      $('#modal1_img').attr('src', $(this).attr('data-img-url'));
      console.log($('#modal1'));
      $('#modal1').modal('open');

    console.log(this)
    console.log($(this).attr('data-img-url'));
  });

  $(".button-collapse").sideNav();


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
    debugger;
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

        console.log("changed movie", results);
      }
    });
  });


    $("#top_category").click(function(){
      // console.log("to change movie")
        debugger;
        var selectedCategory = {
          "category_name": $("#top_category").val()
        };

      $.ajax({
        type: 'get',
        url: '/shuffle_item',
        data: selectedCategory,
        success:function(results){
          $("#t_img").attr('src', results['t_img_url']);
          $("#top_listing").attr('href', results['top_listing']);
          $("#top_color").css('background-color', '#'+results['top_color']);
          $("#top_color").text(results['top_color']);
          
          console.log(results['top_color']);
          console.log("change top listing");

        }
      });
    });

    $("#bottom_category").click(function(){
    // console.log("to change movie")
      debugger;
      console.log('shuffle bottom item');
      var postData = {
        "category_name": 'bottom',
        "movie_name": $("#selected_movie").val(),
      };

      $.ajax({
        type: 'get',
        url: '/shuffle_item',
        data: postData,
        success:function(results){
          console.log('results', results);
          $("#bo_img").attr('src', results['bo_img_url']);
          $("#bottom_listing").attr('href', results['bottom_listing']);
          $("#bottom_color").css('background-color', '#'+results['bottom_color']);
          $("#bottom_color").text(results['bottom_color']);

          console.log(results['bottom_color']);
          console.log("change bottom listing");
        }
      });
    });

    $("#accessory_category").click(function(){
    // console.log("to change movie")
      debugger;
      console.log("shuffle accessory item");
      var postData = {
        "category_name": 'accessory',
        "movie_name": $("#selected_movie").val(),
      };

      $.ajax({
        type: 'get',
        url: '/shuffle_item',
        data: postData,
        success:function(results){
          console.log('results', results);
          $("#a_img").attr('src', results['a_img_url']);
          $("#accessory_listing").attr('href', results['accessory_listing']);
          $("#accessory_color").css('background-color', '#'+results['accessory_color']);
          $("#accessory_color").text(results['accessory_color']);

          console.log(results['accessory_color']);
          console.log("change accessory listing");
        }
      });
    });

    $("#bag_category").click(function(){
    // console.log("to change movie")
      debugger;
      console.log("shuffle top item");
      var postData = {
        "category_name": 'bag',
        "movie_name": $("#selected_movie").val(),
      };

      $.ajax({
        type: 'get',
        url: '/shuffle_item',
        data: postData,
        success:function(results){
          $("#b_img").attr('src', results['b_img_url']);
          $("#bag_listing").attr('href', results['bag_listing']);
          $("#bag_color").css('background-color', '#'+results['bag_color']);
          $("#bag_color").text(results['bag_color']);

          console.log(results['bag_color']);
          console.log("change bag listing");
        }
      });
    });

    $("#dress_category").click(function(){
    // console.log("to change movie")
      debugger;
      console.log("shuffle top item");
      var postData = {
        "category_name": 'dress',
        "movie_name": $("#selected_movie").val(),
      };

      $.ajax({
        type: 'get',
        url: '/shuffle_item',
        data: postData,
        success:function(results){
          $("#d_img").attr('src', results['d_img_url']);
          $("#dress_listing").attr('href', results['dress_listing']);
          $("#dress_color").css('background-color', '#'+results['dress_color']);
          $("#dress_color").text(results['dress_color']);

          console.log(results['dress_color']);
          console.log("change dress listing");
        }
      });
    });

    $("#shoe_category").click(function(){
    // console.log("to change movie")
    debugger;
    console.log("shuffle top item");
    var postData = {
        "category_name": 'shoe',
        "movie_name": $("#selected_movie").val(),
    };

      $.ajax({
        type: 'get',
        url: '/shuffle_item',
        data: postData,
        success:function(results){
          $("#s_img").attr('src', results['s_img_url']);
          $("#shoe_listing").attr('href', results['shoe_listing']);
          $("#shoe_color").css('background-color', '#'+results['shoe_color']);
          $("#shoe_color").text(results['shoe_color']);

          console.log(results['shoe_color']);
          console.log("change shoe listing");
        }
      });
    });


//share button

$(".share").on('click', function(e) {
  $(".fab").removeClass("no");
  if(e.target != this) return;
  $('.share, .fab').toggleClass("active");
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

