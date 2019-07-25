var socket = new WebSocket("ws://" + window.location.host + "/ws/session_control/");

function send_message(e) {
  socket.send(JSON.stringify({"message": e}));
}

socket.onmessage = function(e) {
  alert("got a message");
}
