var x = [3,5,"Dojo", "rocks", "Michael", "Sensei"];
function logArr(x){
  for(var i=0; i < x.length; i++){
    console.log(x[i]);
  }
}
function pushOneHundred(x){
  x.push(100);
  console.log(x);
}
function addNew(){
  var arr = ["hello", "world", "JavaScript is Fun"];
  return arr;
}
function countTo500(){
  for(var i = 0; i < 501; i++)
  console.log(i);
}
function min(arr){
  min = arr[0];
  for(var i = 0; i < arr.length; i++){
    if(arr[i] < min){
      min = arr[i];
    }
  }
  return min;
}
function avg(arr){
  total = 0;
  for(var i = 0; i < arr.length; i++){
    total += arr[i];
  }
  avg = total/arr.length;
  return avg;
}
logArr(x);
pushOneHundred(x);

var y = addNew();
console.log(y);

countTo500();

var min = min( [1, 5, 90, 25, -3, 0]);
console.log(min);

var avg= avg( [1, 5, 90, 25, -3, 0]);
console.log(avg)

var newNinja = {
 name: 'Jessica',
 profession: 'coder',
 favorite_language: 'JavaScript', //like that's even a question!
 dojo: 'Dallas'
}
function newNinjaLoop(object){
  for(key in object){
    console.log(object[key]);
  }
}
newNinjaLoop(newNinja);
