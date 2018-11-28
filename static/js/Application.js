$(document).ready(function() {
   $('.modal').modal()
   $("#button").click(function(e) {
       e.preventDefault();
       $.ajax({
           type: "POST",
           url: "/removechannel",
           data: {
           id: $("#channelInput").val(),

            },
           success: function(data) {
              alert('ok');
            },
            error: function(data) {
                alert('error');
              }
            });
  });

       });