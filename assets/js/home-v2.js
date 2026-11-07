/* Keep selected roles and the complete career in one chronological list. */
(function () {
  'use strict';
  var career = document.getElementById('career-experience');
  var toggle = career && career.querySelector('[data-career-toggle]');
  var heading = career && career.querySelector('#career-heading');
  var additional = career ? career.querySelectorAll('[data-career-extra]') : [];

  function setExpanded(open) {
    if (!toggle || !heading) return;
    additional.forEach(function (item) { item.hidden = !open; });
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    toggle.textContent = open ? toggle.dataset.collapseLabel : toggle.dataset.expandLabel;
    heading.textContent = open ? heading.dataset.expandedHeading : heading.dataset.selectedHeading;
  }

  if (toggle) {
    setExpanded(false);
    toggle.hidden = false;
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') !== 'true';
      setExpanded(open);
      if (!open) {
        var reduced = window.MV && window.MV.prefersReducedMotion && window.MV.prefersReducedMotion();
        career.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'start' });
      }
    });
  }

  function revealRole(target) {
    if (!target) return;
    if (target.hasAttribute('data-career-extra')) setExpanded(true);
    var disclosure = target.closest('details');
    while (disclosure) {
      disclosure.open = true;
      disclosure = disclosure.parentElement.closest('details');
    }
  }

  // Capture runs before the shared smooth-scroll handler measures its target.
  document.addEventListener('click', function (event) {
    var link = event.target.closest && event.target.closest('a[href^="#exp-"]');
    if (!link) return;
    revealRole(document.getElementById(link.getAttribute('href').slice(1)));
  }, true);

  function revealHash() {
    if (location.hash.indexOf('#exp-') === 0) revealRole(document.getElementById(location.hash.slice(1)));
  }
  revealHash();
  window.addEventListener('hashchange', revealHash);
})();
