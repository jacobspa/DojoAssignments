function randomChance() {
  var coins = Math.floor(Math.random()*50)+50;
  while (coins > 0){
    console.log("You have " + coins + " coins remaining")
    coins = coins - 1;
    var win = Math.floor(Math.random() * 100)+1
    if (win == 1){
      var winnings = Math.floor(Math.random()*50)+50;
      coins = coins + winnings;
      console.log("You won" + winnings + "coins! You now have" + coins + " coins!")
    }
    else{
      console.log("You lost.. :( you now have " + coins + " coins remaining...")
    }

  }
}
randomChance();
