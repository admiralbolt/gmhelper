var socket = new WebSocket("ws://" + window.location.host + "/ws/session_control/");

function send_message(e) {
  socket.send(JSON.stringify(e));
}

$(function() {
  $("audio").on("play", function() {
    $("audio").not(this).each(function(index, audio) {
      audio.pause();
    });
  });
});
