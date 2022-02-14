function translateHello () {
  const service = 'https://fourtonfish.com/hellosalut/?lang=';
  const lang = $('INPUT#language_code').val();
  const url = service + lang;
  $.getJSON(url, function (data) {
    $('DIV#hello').text(data.hello);
  });
}

$(document).ready(function () {
  $('INPUT#btn_translate').click(translateHello);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        translateHello();
      }
    });
  });
});
