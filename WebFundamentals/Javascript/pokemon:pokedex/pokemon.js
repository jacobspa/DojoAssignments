$(document).ready(function(){

  $("button").click(function(){
    for(var i = 1; i <= 151; i++){
      var poke = "<img src='http://pokeapi.co/media/img/"+i+".png'>"
      $("body").append(poke);
    };
  });
});
