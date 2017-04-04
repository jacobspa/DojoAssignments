var game = {
  players: [],
  addPlayer: function(n){}
};
function playerConstructor(){
  player = {};
  player.name = name;
    player.hand = [];
  player.addCard = function(card){
    player.hand.push(card);
  };
  return player;
};

playerConstructor('Phil');
playerConstructor('Chris');
