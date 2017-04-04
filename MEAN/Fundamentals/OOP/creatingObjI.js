function VehicleConstructor(name, wheels, passengers, s){
  console.log('Creating new vehicle ' + name);
  // private
  var distance_traveled = 0;

  var updateDistance = function(s){
    console.log('Traveling ' + s + ' distance!');
    distance_traveled += s;
  }

  // public
  this.name = name;
  this.numberOfWheels = wheels;
  this.numberOfPassengers = passengers;
  this.speed = s;
  this.vin = Math.floor(Math.random()* 1000000000000);

  this.makeNoise = function(){
    console.log('Vrrrmmmmmm Vrrrmmmmmmmmmm!');
  }
  VehicleConstructor.prototype.move = function (){
    updateDistance(this.speed);
    this.makeNoise();
    return this;
  }
  this.checkMiles = function(){
    console.log(distance_traveled);
  }
}

var bike =  new VehicleConstructor('bike', 2, 1, 5);

bike.makeNoise = function(){
  console.log('ring ring!');
}
bike.makeNoise();
bike.move();
bike.checkMiles();

var sedan =  new VehicleConstructor('sedan', 4, 2, 17);
sedan.makeNoise = function(){
  console.log('Honk Honk!')
}
sedan.makeNoise();
sedan.move();

var bus = new VehicleConstructor('bus', 4, 1, 6);
bus.pickUp = function(n){
  console.log('Picking up ' + n + ' passengers');
  bus.numberOfPassengers += n;
}
bus.pickUp(3);
bus.move();
console.log(bus.numberOfPassengers);
console.log(bus.vin);
