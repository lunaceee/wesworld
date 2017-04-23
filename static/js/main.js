"use strict";

var movieBtnClick = function(e){
    console.log(e);
    console.log($(e.target).attr('data-movie-name'));

    var selectedMovie = {
      "movie_name": $(e.target).attr('data-movie-name')
    };

    // set all loading icons to visible
    $("#ensemble-loader").css('display', 'block');
    console.log("loading??")

    $.ajax({
      type: 'get',
      url: '/search_json',
      data: selectedMovie,
      success:function(results){

        // set all loading icons to invisible
        $("#ensemble-loader").css('display', 'none');

        $("#a_img").attr('src', results['a_img_url']);
        $("#a_listing").attr('href', results['accessory_listing']);
        $("#accessory_color").css('background-color', "#" + results['colors'][2]);
        $("#accessory_link").attr('href', results['accessory_listing']);

        $("#b_img").attr('src', results['b_img_url']);
        $("#b_listing").attr('href', results['bag_listing']);
        $("#bag_color").css('background-color', "#" + results['colors'][4]);
        $("#bag_link").attr('href', results['bag_listing']);

        $("#bo_img").attr('src', results['bo_img_url']);
        $("#bo_listing").attr('href', results['bottom_listing']);
        $("#bottom_color").css('background-color', "#" + results['colors'][1]);
        $("#bottom_link").attr('href', results['bottom_listing']);

        $("#d_img").attr('src', results['d_img_url']);
        $("#d_listing").attr('href', results['dress_listing']);
        $("#dress_color").css('background-color', "#" + results['colors'][0]);
        $("#dress_link").attr('href', results['dress_listing']);
        console.log(results['colors'][0]);

        $("#s_img").attr('src', results['s_img_url']);
        $("#s_listing").attr('href', results['shoe_listing']);
        $("#shoe_color").css('background-color', "#" + results['colors'][3]);
        $("#shoe_link").attr('href', results['shoe_listing']);

        $("#t_img").attr('src', results['t_img_url']);
        $("#t_listing").attr('href', results['top_listing']);
        $("#top_color").css('background-color', "#" + results['colors'][4]);
        $("#top_link").attr('href', results['top_listing']);

        console.log("changed movie", results);
      }
    });
  }

$(document).ready(function(){
  // Initialize Carousel.
  $('.carousel').carousel({
          dist: 0
  });

  // Modal windows for listing images.
  $('.modal').modal();

  $('.modal_trigger').click(function(e){
    $('#login').modal('open');
    $('#register').modal('open');
  });

  // Lightbox effect for images.
  $('.materialboxed').materialbox();

  // Movile Nav bar.
  $(".button-collapse").sideNav();

  // Hide movie title and colors by default
  $(".wes-initial-item").click(function(e){
    $("#btn-holder").empty();
  });

  // Background animation when clicking on carousel items

  // Show movie title and colors on click
  $(".wes-carousel-item").click(function(e){
        console.log(e);

    var desiredID = $(e.currentTarget).attr('data-movie-id');


    console.log(desiredID);

    var y = $("#btn-hider #movie-" + desiredID);
    var newBtn = y.clone();

    newBtn.click(movieBtnClick);
    $("#btn-holder").empty();
    $("#btn-holder").append(
      newBtn
      );


    $("#btn-holder button").css({
      "font-size":"20px",
      "margin":"auto",
      "display":"block",
      "height":"4em",
      "margin-top":"-2em",
      "margin-bottom":"2em",
      "font-family": "'Dancing Script', cursive"
      // "font-family": "'Pacifico', cursive"
      // "font-family": "'Lobster', cursive"
      // "font-family": "'Satisfy', cursive"
    });
  });

  // Save ensemble function.
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
      }
    }); 

   $('#save_ensemble').on('click', update_user_profile);
  
  }

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
      console.log("shuffle bag item");
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
      console.log("shuffle dress item");
      var postData = {
        "category_name": 'dress',
        "movie_name": $("#selected_movie").val(),
      };

      // set all loading icons to invisible
      $("#dress-loader").css('display', 'block');
      console.log("loading icon");

      $.ajax({
        type: 'get',
        url: '/shuffle_item',
        data: postData,
        success:function(results){
          $("#dress-loader").css('display', 'none');
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
    console.log("shuffle shoe item");
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
// $(".share").on('click', function(e) {
//   var el = $(e.target);
//   el.find(".fab").removeClass("no");
//   el.find('.share, .fab').toggleClass("active");
// });




});

