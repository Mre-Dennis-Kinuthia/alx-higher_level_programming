$(document).ready(function () {
  $('#btn_translate').click(function () {
    const lang = $('#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  });

  $('#language_code').keydown(function (event) {
    if (event.keyCode == 13) {
      const lang = $(this).val();
      const url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
      $.get(url, function (data) {
        $('#hello').text(data.hello);
      });
    }
  });
});
