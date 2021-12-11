$(function () {
  //   $('#published-date').datetimepicker();
  fade_alerts();

  // Set default date range of week from Monday to Sunday
  const date_range = get_date_range_in_week(new Date());
  set_date_range(date_range[0], date_range[1]);
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

function get_date_range_in_week(rnd_date, step = 0) {
  const curr = format_date(rnd_date);

  var monday_date = format_date();

  const monday = 1 - curr.getDay(); // monday: 1 (day of week)
  monday_date.setDate(monday_date.getDate() + monday + step);

  var sunday_date = format_date();

  const sunday = 7 - curr.getDay(); // sunday: 0 (day of week)
  sunday_date.setDate(sunday_date.getDate() + sunday + step);

  return [monday_date.toISOString().split('T')[0], sunday_date.toISOString().split('T')[0]];
}

// Set default date range of week from Monday to Sunday
function set_date_range(date_from, date_end) {
  $('#date-from').val(date_from);
  $('#date-to').val(date_end);
  // const url = window.location.href;

  // if (url.includes(window.location.origin+'/books/'))
}

function format_date(value = new Date()) {
  return new Date(value.toISOString().split('T')[0]);
}
