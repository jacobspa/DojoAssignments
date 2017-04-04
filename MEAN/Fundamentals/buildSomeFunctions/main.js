function runningLogger(){
  console.log('I am running');
}

function multiplyByTen(x){
  var ans = x * 10;
  return ans;
}

var ten = multiplyByTen(7);
console.log(ten);

function stringReturnOne(){
  return "This is the best string return function";
}

function stringReturnTwo(){
  return "NO! This is the best string return function";
}

function caller(x){
  if (typeof(x) === 'function'){
    x();
    console.log('ITS WORKING!!!')
  }
}

function myDoubleConsoleLog(x,y){
  if(typeof(x) === 'function'){
    var ans = x();
    console.log(ans);
  }
  if(typeof(y)=== 'function'){
    var ansY = y();
    console.log(ansY);
  }
}

function caller2(x){
  console.log('Starting');
  setTimeout(function(){
    if (typeof x === 'function'){
      x(stringReturnOne,stringReturnTwo);
    }
  }, 2000);
  console.log("ending?");
  return 'Interesting';
}

caller2(myDoubleConsoleLog);
