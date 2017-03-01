$(document).ready(function(){
  console.log($("input").val());

  $("button").click(function(){
    console.log($("input").val());
    var first = $("#first").val();
    var last = $("#last").val();
    var email = $("#email").val();
    var contact = $("#contact").val();
    console.log(contact);
    console.log(first);
    $("tbody").append("<tr><td>"+ first +  "</td><td>" + last + "</td><td>" + email + "</td><td>" + contact + "</td></tr>");
  });
});
