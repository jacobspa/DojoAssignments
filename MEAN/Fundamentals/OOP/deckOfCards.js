function Deck(){
  //prototype {
  Deck.prototype.create = function(){
    this.deck = [];
    this.suit = ['H', 'D', 'S', 'C'];
    for (var i = 0; i < this.suit.length; i++){
      for(var j = 0; j < 14; j++){
        if( j == 11){
          this.deck.push('Jack'+ this.suit[i]);
        }
        else if(j == 12){
          this.deck.push('Queen' + this.suit[i]);
        }
        else if(j == 13){
          this.deck.push('King'+ this.suit[i]);
        }
        else if(j == 14){
          this.deck.push('Ace'+ this.suit[i]);
        }
        else {
          this.deck.push(j+ this.suit[i]);
        }
      }
    }
    return this;
  }
  Deck.prototype.shuffle =function(array) {
  var m = array.length, t, i;

  // While there remain elements to shuffle…
  while (m) {

    // Pick a remaining element…
    i = Math.floor(Math.random() * m--);

    // And swap it with the current element.
    t = array[m];
    array[m] = array[i];
    array[i] = t;
  }

  return array;
}
Deck.prototype.deal = function(deck){
  for (var i = 0; i < this.deck.length; i++){
    var c = Math.floor(Math.random()* this.deck.length-1);
    var card = this.deck[c];
    delete this.deck[c]
    return card;
  }
}
Deck.prototype.reset = function(){
  this.create();
}
}
function Player(n){
  this.name = n;
  this.hand = [];

  Player.prototype.take(deck){
    this.hand.push(deck.deal());
    return this;
  }
  Player.prototype.discard(){
    this.hand.pop();
    return this;
  }
}
