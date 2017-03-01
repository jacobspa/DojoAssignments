$(document).ready(function() {
  $('img').click(function() {
    var temp = $(this).attr('src');
    var change = $(this).attr('data-alt-src')
    $(this).attr("src", change);
    $(this).attr("data-alt-src", temp);
  });
});
