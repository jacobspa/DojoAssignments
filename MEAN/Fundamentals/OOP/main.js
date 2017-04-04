
// our test object
var customObject = {
  name:'California, Eureka',
  onClick:function(){
    console.log("I've been clicked");
    console.log(this.name);
  }
}

$('button').click(customObject.onClick.bind(customObject));

var newObject = {
  name:"West Virginia,  Montani semper liberi"
}
// modify the button method to this:
$('button').click(customObject.onClick.bind(newObject));
