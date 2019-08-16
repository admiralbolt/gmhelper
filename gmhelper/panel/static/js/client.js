var socket = new WebSocket("ws://" + window.location.host + "/ws/session_control/");

socket.onmessage = function(event) {
  console.log(event);
  data = JSON.parse(event.data);
  switch(data.type) {
    case "letter":
      display_letter(data.text);
      break;
    case "image":
      display_image(data.path);
      break;
    default:
      console.log("UNKNOWN MESSAGE TYPE");
  }
}

function convert_newlines(text) {
  return text.replace(/\r\n/g, "<br />");
}

function display_letter(text) {
  $("#content").html(convert_newlines(text));
}

function display_image(path) {
  $("#content").html("<img height='100%' width='100%' src='" + path + "' />");
}
