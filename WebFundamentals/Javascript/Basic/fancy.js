function fancyArray(symbol, reversed){
  var arr = [ "James", "Jill", "Jane", "Jack" ];
  if (reversed == false){
    for (var i = 0; i < arr.length;i++){
      console.log(i + " " + symbol + " " + arr[i])
    }
  }
  else if (reversed == true){
    for (var i = arr.length-1; i >= 0; i--)(
      console.log(i + " " + symbol + " " + arr[i])
    )
  }
}
fancyArray("->", false);
