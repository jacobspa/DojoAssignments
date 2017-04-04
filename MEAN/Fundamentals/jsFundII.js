var seventy = (x, y) => {
  var total = 0;
  for(var i = x; i < y; i++){
    total += i;
  }
  console.log(total);
  return total;
};

var anono = (arr) => {
  min = arr[0];
  for(var i = 0; i < arr.length; i++){
    if(arr[i] < min){
      min = arr[i];
    }
  }
  console.log(min);
  return min;
};

var that = (arr) => {
  total = 0;
  for(var i = 0; i < arr.length; i++){
    total += arr[i];
  }
  var avg = total/arr.length;
  console.log(avg);
  return avg;
};

seventy(6, 10);
anono([1,2,3,4,5]);
that([1,2,3,4,5]);

var person = {
  name: "Phillip Jacobs",
  distance_traveled: 0
}

function say_name(p) {
  console.log(p.name);
  return p.name
}

function say_something(something){
  console.log(person.name + " says "+ something);
}

function walk(){
  console.log(person.name + " is walking...");
  person.distance_traveled += 3;
  return person.distance_traveled
}

function run(){
  console.log(person.name + " is running...");
  person.distance_traveled += 10;
  return person.distance_traveled
}

function crawl(){
  console.log(person.name + " is crawling");
  person.distance_traveled += 1;
  return person.distance_traveled
}

say_name(person);
say_something("I am cool");
var w = walk();
console.log(w);
var r = run();
console.log(r);
var c = crawl();
console.log(c);
