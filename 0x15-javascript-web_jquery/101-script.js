$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>item</li>');
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list li').last().remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list li').remove();
  });
});
