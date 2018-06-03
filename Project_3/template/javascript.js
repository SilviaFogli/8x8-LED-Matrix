

$(document).ready(function() {

  $('.pad-0').mousedown(function() {
      Z.call('set_led', [0]);
  });

  $('.pad-1').mousedown(function() {
      Z.call('set_led', [1]);
  });

  $('.pad-2').mousedown(function() {
      Z.call('set_led', [2]);
  });

  $('.pad-3').mousedown(function() {
      Z.call('set_led', [3]);
  });

  $('.pad-4').mousedown(function() {
      Z.call('set_led', [4]);
  });

  $('.pad-5').mousedown(function() {
      Z.call('set_led', [5]);
  });

  $('.pad-6').mousedown(function() {
      Z.call('set_led', [6]);
  });
  
  $('.pad-7').mousedown(function() {
      Z.call('set_led', [7]);
  });

  $('.pad-8').mousedown(function() {
      Z.call('set_led', [8]);
  });

  $('.pad-9').mousedown(function() {
      Z.call('set_led', [9]);
  });
  
  Z.init({
                on_connected:  function(){$("#status").html("CONNECTED")},
                on_error:  function(){$("#status").html("ERROR")},
                on_disconnected:  function(){$("#status").html("DISCONNECTED"); return true},
                on_online:  function(evt){$("#status").html("ONLINE");},
                on_offline:  function(evt){$("#status").html("OFFLINE");},
                on_event:  function(evt){
                    console.log(evt.payload.data)
                }
  })

});