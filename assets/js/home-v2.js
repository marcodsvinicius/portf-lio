/* Open career disclosures before the shared anchor handler calculates scrolling. */
(function () {
  'use strict';
  document.addEventListener('click', function (event) {
    var link = event.target.closest && event.target.closest('a[href^="#exp-"]');
    if (!link) return;
    var target = document.getElementById(link.getAttribute('href').slice(1));
    if (!target) return;
    var disclosure = target.closest('details');
    while (disclosure) {
      disclosure.open = true;
      disclosure = disclosure.parentElement.closest('details');
    }
  }, true);
})();
