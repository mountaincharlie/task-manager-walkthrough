
document.addEventListener('DOMContentLoaded', function() {
    // initialisation snippet for Materialize's sidenav (with custom var names)
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // datepicker initialisation (see materialize datepicker doc)
    var datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
      format:"dd mmmm, yyyy",
      i18n: {done: "select"},
    });

    // select initialisation (see materialize datepicker doc)
    var selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);
  });