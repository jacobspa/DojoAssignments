$(document).ready(function(){
  $("button").click(function(){
    var city = $("input").val();
    console.log(city);
    $.get("http://api.openweathermap.org/data/2.5/weather?q="+ city +",uk&&appid=edbaf41c6024b1b4e55be732d18eb066", function(res){
      console.log(res);
      var temp = Math.floor((1.8 *((res.main.temp)-273))+32);
      console.log(temp)
      $("h1, h2").hide();
      $('div').append("<h1>"+ city + "</h1><h2>Temperature:"+ temp + "</h2>");
    });
  });
});
