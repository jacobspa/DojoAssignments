function sum(arr, i, s){
  if (i < arr.length){
    console.log(s)
    return sum(arr, i+1, s+arr[i]);
  }
  else{
    console.log('its elseing')
    return s;
  }
}
var x = sum([1,2,3,4,5,6,7,8], 0, 0);
console.log(x);

var arr = [3, 6];
arr[234] = "hi";
//
console.log( arr.length ); // 235
console.log( arr[34] ); // undefined
arr.length = 3;
console.log( arr[34] );
console.log( arr[234] );
console.log( arr.length );
arr.length = 500;
console.log( arr[234] );
console.log( arr.length );
