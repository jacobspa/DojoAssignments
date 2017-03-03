$(document).ready(function(){

    for(var i = 1; i <= 151; i++){
      var poke = "<img id='"+ i + "' src='http://pokeapi.co/media/img/"+i+".png'>"
      $("#pokepics").append(poke);
    };
    $("img").click(function(){
      $("p,h2,ul,h1").hide();
      $("#pokedex img").hide();
      var id = $(this).attr("id");
      $.get("http://pokeapi.co/api/v1/pokemon/"+ id +"", function(res){
      console.log(res);
      if(res.types.length == 2){
      $("#pokedex").append("<h1>"+ res.name + "</h1><img src='http://pokeapi.co/media/img/"+id+".png'><h2> Types</h2><ul><li>"+ res.types[0].name + "</li><li>"+ res.types[1].name +"</li></ul><h2>Height</h2><p>"+ res.height +"<p><h2>Weight</h2><p>"+ res.weight + "</p>");
    }
    if(res.types.length == 1){
      $("#pokedex").append("<h1>"+ res.name + "</h1><img src='http://pokeapi.co/media/img/"+id+".png'><h2> Types</h2><ul><li>"+ res.types[0].name + "</li></ul><h2>Height</h2><p>"+ res.height +"<p><h2>Weight</h2><p>"+ res.weight + "</p>");
    }
    });
    });

  });
