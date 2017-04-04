function personCreator(n){
  var human = {
    name: n,
    distance_traveled: 0,
    say_something: function(s){
      console.log(human.name + " says" + s)
    }
    walk: function() {
      console.log(human.name + " is walking");
      human.distance_traveled += 3;
    },
    run: function(){
      console.log(human.name + " is running");
      human.distance_traveled += 10;
    },
    crawl: function(){
      console.log(human.name + " is crawling");
      human.distance_traveled += 1;
    }
    }
  }

function ninjaCreator(o){
  var ninja = {
    name: o,
    cohort: 'Best',
    belt_level: 'Yellow'
    levelUp: function(){
      if (ninja.belt_level == 'Yellow'){
        ninja.belt_level = 'Red';
      }
      else if(ninja.belt_level == 'Red'){
        ninja.belt_level = 'Black';
      }
      else if(ninja.belt_leve == 'Black'){
        console.log('You have reached maximum Ninja level!!!');
      }
    }
  }
}
