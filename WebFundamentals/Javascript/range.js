function printRange(start, end, skip){
  for (start; start < end; start= start + skip){
    console.log(start);
  }
}
printRange(2,10,2);
