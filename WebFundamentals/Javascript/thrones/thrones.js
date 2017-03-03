$(document).ready(function(){
  $("img").click(function(){
    var house = $(this).attr("id");
    $.get("http://anapioficeandfire.com/api/houses/"+house, function(res){
      console.log(res);
      var name = res.name;
      var words = res.coatOfArms;
      var Name = res.name;
      var titles;
      for(var i = 0;i < res.titles.length;i++){
        titles = titles +", "+ res.titles[i];
      }
      $("div").html("<h1>House Details</h1><p>Name: "+ name +"</p><br><p>Words: "+ words + "</p><br><p>Name: "+ name + "</p><br><p>Titles: " + titles);
    });
  });
});
