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

function convert_newlines(text) {
  return text.replace(/\r\n/g, "<br />");
}

function display_letter(text) {
  $("#content").html(convert_newlines(text));
}
