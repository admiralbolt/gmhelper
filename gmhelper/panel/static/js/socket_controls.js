var socket = new WebSocket("ws://" + window.location.host + "/ws/session_control/");
// Used for timing delay for auto complete.
var debounce;

function send_message(e) {
  socket.send(JSON.stringify(e));
}

/**
 * Makes an API call to fetch the auto-complete data.
 * Look at the auto_complete view in views.py for more info.
 */
function auto_complete(keyword) {
  $.ajax({
    method: "GET",
    url: "/panel/auto_complete?keyword=" + keyword,
    dataType: "json"
  }).done(function(result) {
    var data = jQuery.parseJSON(result);
    var html_string = "";
    for (var i = 0; i < data.length; i++) {
      var model_name = data[i].model.split(".")[1];
      model_name = model_name.charAt(0).toUpperCase() + model_name.slice(1);
      html_string += "<li class='entry' data-id='" + data[i].pk + "' data-model='" + data[i].model + "'>" + data[i].fields.name + "<span class='item-type'>" + model_name + "</span></li>";
    }
    $("#auto-complete-results").html(html_string);
    $("#auto-complete-results").show();
    current_selection = -1;
  });
}

$(function() {
  $("audio").on("play", function() {
    $("audio").not(this).each(function(index, audio) {
      audio.pause();
    });
  });

  /**
   * Aww yiss, roll your own debounce.
   */
  $("#input-keyword").on("input", function() {
    clearTimeout(debounce);
    var keyword = $("#input-keyword").val();
    if (keyword.length > 0) {
      debounce = setTimeout(function() {
        auto_complete(keyword);
      }, 250);
    } else {
      $("#auto-complete-results").hide();
      $("#auto-complete-results").empty();
    }
  });
});
