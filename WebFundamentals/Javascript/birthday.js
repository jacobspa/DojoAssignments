var daysUntilMyBirthday = 60;
while(daysUntilMyBirthday >= 0){
  if (daysUntilMyBirthday > 30){
    console.log(daysUntilMyBirthday + " days until my birthday. Such a long time... : (");
  }
  else if (daysUntilMyBirthday <=30 && daysUntilMyBirthday >= 5) {
    console.log(daysUntilMyBirthday + " days until my birthday! It's coming up!");
  }
  else if (daysUntilMyBirthday <=4 && daysUntilMyBirthday > 0) {
    console.log(daysUntilMyBirthday + " DAYS UNTIL MY BIRTHDAY!!!!");
  }
  else if (daysUntilMyBirthday == 0){
    console.log("TIME TO PARTY!!!!!! WOOOP WOOOOP!!!!!");
  }
    daysUntilMyBirthday = daysUntilMyBirthday - 1;
}
