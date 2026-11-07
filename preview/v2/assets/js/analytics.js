/* Microsoft Clarity — collect visits to the public portfolio only. */
(function () {
  'use strict';

  var host = window.location.hostname;
  if (host !== 'marcodsvinicius.com' && host !== 'www.marcodsvinicius.com') return;
  if (window.location.pathname.indexOf('/preview/') === 0) return;
  if (window.clarity) return;

  (function (c, l, a, r, i, t, y) {
    c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments); };
    t = l.createElement(r);
    t.async = true;
    t.src = 'https://www.clarity.ms/tag/' + i;
    y = l.getElementsByTagName(r)[0];
    y.parentNode.insertBefore(t, y);
  })(window, document, 'clarity', 'script', 'za2y0un6sp');
})();
