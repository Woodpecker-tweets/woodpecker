$(function (){
    $('.btn-lg').click(function () {
      freq = $('#frequency option:selected').text();
      keyword = $('input').val();
      message = 'currently tweeting' + keyword;
      if (!(keyword).match(/^[0-9a-zA-Z]+$/)) {
          alert('Input is not alphanumeric');
      }
      keyword_list = keyword.split(' ');
      key = keyword_list[0];
      data_dict = {'hastag': key, 'tweet_time': freq};
      $.ajax({
        type: 'POST',
        url: '',
        contentType: 'application/json',
        data: JSON.stringify(data_dict),
        success: function(data) {
          // Hid Tweet This
          // Show Activate Deactivate
          // Manipulate Data

        }
      });
      $('.has_server').css('display', '');
      $('.no_service').css('display', 'none');
      $('#status').text('Currently retweeting #' + keyword + ' ' + freq.toUpperCase())
    });

    $('.btn-md').click(function () {
      $('.has_server').css('display', 'none');
      $('.no_service').css('display', '');

    })
})
