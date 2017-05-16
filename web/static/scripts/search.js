$(function (){
    $('.btn').click(function () {
      let freq = $('#frequency option:selected').text();
      let keyword = $('input').val();
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
      alert(key);
    });
})
