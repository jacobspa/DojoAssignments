function removeDup(arr){
  counter = 0;
  for(var i = 0; i < arr.length; i++){
    counter++;
    if(arr[i+1] == arr[i]){
      for(var j = i; j < arr.length-1; j++){
        arr[j+1]= arr[j+2];
      }
      arr.length = arr.length-1;
    }
    else if(i > 0 && arr[i-1] == arr[i]){
      for(var j = i; j < arr.length-1; j++){
        arr[j] = arr[j+1];
      }
      arr.length = arr.length-1
    }
  }
  return [counter, arr];
}
var ans = removeDup([1,1,1,2,2,2,3,3,3,3,3,3])
console.log(ans)
