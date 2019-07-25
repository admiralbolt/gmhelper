socket.onmessage = function(event) {
  console.log(event);
  data = JSON.parse(event.data);
  switch(data.type) {
    case "letter":
      display_letter(data.text);
      break;
    default:
      console.log("UNKNOWN MESSAGE TYPE");
  }
}

function display_letter(text) {
  $("#content").html(text);
}
