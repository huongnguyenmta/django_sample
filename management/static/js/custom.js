$(function () {
  //   $('#published-date').datetimepicker();
  fade_alerts();
});

function fade_alerts() {
  var alerts = document.getElementsByClassName('msg');
  var i = alerts.length;
  for (let elem of alerts) {
    i--;
    time = 3250 + 1000 * i;
    setTimeout(function () {
      $(elem).fadeOut('slow');
    }, time);
  }
}
