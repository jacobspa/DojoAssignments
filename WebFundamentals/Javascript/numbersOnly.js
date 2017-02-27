function numbersOnly(arr){
  var newArray = [];
  for (var i = 0; i < arr.length; i++){
    if (typeof arr[i] === "number"){
      newArray.push(arr[i]);
    }
  }
  console.log(newArray);
}
numbersOnly([1, "apple", -3, "orange", 0.5]);
