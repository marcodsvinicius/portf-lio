/* ==========================================================================
   Marco Vinicius — Portfólio
   Comportamentos das páginas de case: carrosséis com swipe, imagem sincronizada
   da solução (dados no bloco JSON #solucao-data), lightbox e trava de senha.
   ========================================================================== */
(function () {
  'use strict';

  /* --- Swipe (touch) --------------------------------------------------- */
  function attachSwipe(el, onPrev, onNext) {
    if (!el) return;
    var startX = 0, startY = 0, tracking = false;
    el.addEventListener('touchstart', function (e) {
      if (!e.touches || !e.touches.length) return;
      startX = e.touches[0].clientX; startY = e.touches[0].clientY; tracking = true;
    }, { passive: true });
    el.addEventListener('touchend', function (e) {
      if (!tracking) return;
      tracking = false;
      var t = e.changedTouches && e.changedTouches[0];
      if (!t) return;
      var dx = t.clientX - startX, dy = t.clientY - startY;
      if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) { if (dx < 0) onNext(); else onPrev(); }
    }, { passive: true });
  }

  /* --- Carrosséis ------------------------------------------------------- */
  var CAROUSELS = {
    solucao: { active: 'w-2 h-2 rounded-full bg-black transition-colors', idle: 'w-2 h-2 rounded-full bg-black/20 transition-colors' },
    antigo: { active: 'w-2 h-2 rounded-full bg-white transition-colors', idle: 'w-2 h-2 rounded-full bg-white/30 transition-colors' }
  };
  var dataEl = document.getElementById('solucao-data');
  var solucaoData = null;
  if (dataEl) { try { solucaoData = JSON.parse(dataEl.textContent); } catch (e) { solucaoData = null; } }

  Object.keys(CAROUSELS).forEach(function (key) {
    var track = document.getElementById(key + '-carousel-track');
    var prev = document.getElementById(key + '-prev');
    var next = document.getElementById(key + '-next');
    var dotsBox = document.getElementById(key + '-dots');
    if (!track || !prev || !next || !dotsBox) return;
    var image = key === 'solucao' ? document.getElementById('solucao-image') : null;
    var total = track.children.length;
    var dots = dotsBox.children;
    var index = 0;
    var cls = CAROUSELS[key];

    function update() {
      track.style.transform = 'translateX(-' + (index * 100) + '%)';
      if (image && solucaoData && solucaoData.images && solucaoData.images[index]) {
        image.src = solucaoData.images[index];
        image.alt = (solucaoData.alts && solucaoData.alts[index]) || image.alt;
      }
      prev.disabled = index === 0;
      next.disabled = index === total - 1;
      Array.prototype.forEach.call(dots, function (dot, i) { dot.className = i === index ? cls.active : cls.idle; });
    }
    prev.addEventListener('click', function () { if (index > 0) { index--; update(); } });
    next.addEventListener('click', function () { if (index < total - 1) { index++; update(); } });
    attachSwipe(document.getElementById(key + '-carousel-container'),
      function () { if (!prev.disabled) prev.click(); },
      function () { if (!next.disabled) next.click(); });
    update();
  });

  /* --- Comparador antes / depois ----------------------------------------- */
  document.querySelectorAll('.ba-compare').forEach(function (box) {
    var range = box.querySelector('.ba-compare__range');
    var before = box.querySelector('.ba-compare__before');
    var thumbs = box.querySelectorAll('.ba-compare__thumb');
    if (!range) return;
    function sync() { box.style.setProperty('--pos', range.value + '%'); }
    range.addEventListener('input', sync);
    range.addEventListener('pointerdown', function () { box.classList.add('is-dragging'); });
    ['pointerup', 'pointercancel', 'blur'].forEach(function (ev) { range.addEventListener(ev, function () { box.classList.remove('is-dragging'); }); });
    thumbs.forEach(function (t) {
      t.addEventListener('click', function () {
        if (!before) return;
        before.src = t.dataset.src; before.alt = t.dataset.alt || before.alt;
        thumbs.forEach(function (o) { o.classList.toggle('is-active', o === t); });
      });
    });
    sync();
  });

  /* --- Lightbox ---------------------------------------------------------- */
  var modal = document.getElementById('image-modal');
  var modalImg = document.getElementById('modal-image');
  var closeBtn = document.getElementById('close-modal');
  function openModal(src, alt) {
    if (!modal || !modalImg) return;
    modalImg.src = src; if (alt) modalImg.alt = alt;
    modal.classList.remove('hidden'); modal.classList.add('flex');
    void modal.offsetWidth;
    modal.classList.remove('opacity-0');
    modalImg.classList.remove('scale-95'); modalImg.classList.add('scale-100');
    document.body.style.overflow = 'hidden';
  }
  function closeModal() {
    if (!modal || !modalImg) return;
    modal.classList.add('opacity-0');
    modalImg.classList.remove('scale-100'); modalImg.classList.add('scale-95');
    setTimeout(function () { modal.classList.add('hidden'); modal.classList.remove('flex'); document.body.style.overflow = ''; }, 300);
  }
  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  if (modal) modal.addEventListener('click', function (e) { if (e.target === modal) closeModal(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && modal && !modal.classList.contains('hidden')) closeModal(); });
  document.querySelectorAll('.zoomable-image').forEach(function (img) {
    img.addEventListener('click', function () { openModal(img.src, img.alt); });
  });

  /* --- Galeria dos cases v2: diálogo nativo, zoom e navegação ---------- */
  (function gallery() {
    var viewer = document.getElementById('case-image-viewer');
    if (!viewer || typeof viewer.showModal !== 'function') return;
    var figures = Array.prototype.slice.call(document.querySelectorAll('.case-figure'));
    if (!figures.length) return;
    var image = viewer.querySelector('#case-viewer-image');
    var stage = viewer.querySelector('.case-viewer-stage');
    var caption = viewer.querySelector('#case-viewer-caption');
    var count = viewer.querySelector('#case-viewer-count');
    var previous = viewer.querySelector('[data-viewer-prev]');
    var next = viewer.querySelector('[data-viewer-next]');
    var zoom = viewer.querySelector('[data-viewer-zoom]');
    var hint = viewer.querySelector('.case-viewer-zoom-hint');
    var active = 0, zoomed = false, invoker = null, savedOverflow = '';

    function fit() {
      zoomed = false;
      viewer.classList.remove('is-zoomed');
      image.style.width = '';
      zoom.textContent = viewer.dataset.zoomLabel;
      zoom.setAttribute('aria-pressed', 'false');
      hint.hidden = true;
      stage.scrollLeft = stage.scrollTop = 0;
    }
    function show(index) {
      fit();
      active = index;
      var focused = document.activeElement;
      var source = figures[index].querySelector('img');
      image.alt = source.alt;
      image.src = source.currentSrc || source.src;
      caption.textContent = figures[index].querySelector('[data-image-caption]').textContent;
      count.textContent = (index + 1) + ' / ' + figures.length;
      previous.disabled = index === 0;
      next.disabled = index === figures.length - 1;
      if ((focused === previous && previous.disabled) || (focused === next && next.disabled)) {
        viewer.querySelector('[data-viewer-close]').focus();
      }
    }
    function move(step) {
      var target = active + step;
      if (target >= 0 && target < figures.length) show(target);
    }
    document.querySelectorAll('[data-case-image]').forEach(function (trigger) {
      trigger.addEventListener('click', function (event) {
        if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
        event.preventDefault();
        invoker = trigger;
        show(Number(trigger.dataset.caseImage));
        savedOverflow = document.body.style.overflow;
        document.body.style.overflow = 'hidden';
        viewer.showModal();
      });
    });
    viewer.querySelector('[data-viewer-close]').addEventListener('click', function () { viewer.close(); });
    viewer.addEventListener('close', function () {
      document.body.style.overflow = savedOverflow;
      fit();
      if (invoker && invoker.isConnected) invoker.focus({ preventScroll: true });
    });
    viewer.addEventListener('click', function (event) {
      if (event.target !== viewer) return;
      var bounds = viewer.getBoundingClientRect();
      if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) viewer.close();
    });
    viewer.addEventListener('keydown', function (event) {
      if (event.key === 'Tab') {
        var stops = viewer.querySelectorAll('button:not(:disabled), [tabindex="0"]');
        var first = stops[0], last = stops[stops.length - 1];
        if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
        else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
        return;
      }
      if (zoomed) return; // Arrow keys scroll the enlarged image naturally.
      if (event.key === 'ArrowLeft') { event.preventDefault(); move(-1); }
      if (event.key === 'ArrowRight') { event.preventDefault(); move(1); }
    });
    previous.addEventListener('click', function () { move(-1); });
    next.addEventListener('click', function () { move(1); });
    zoom.addEventListener('click', function () {
      if (zoomed) { fit(); return; }
      if (!image.complete || !image.naturalWidth) return;
      var width = image.getBoundingClientRect().width;
      zoomed = true;
      viewer.classList.add('is-zoomed');
      image.style.width = (width * 2) + 'px';
      zoom.textContent = viewer.dataset.fitLabel;
      zoom.setAttribute('aria-pressed', 'true');
      hint.hidden = false;
      stage.scrollLeft = (stage.scrollWidth - stage.clientWidth) / 2;
      stage.scrollTop = (stage.scrollHeight - stage.clientHeight) / 2;
      stage.focus();
    });
    stage.tabIndex = 0;
    attachSwipe(stage, function () { if (!zoomed) move(-1); }, function () { if (!zoomed) move(1); });
  })();

  /* --- Trava de senha (só nos cases com #password-gate) ------------------ */
  (function gate() {
    var GATE_KEY = 'mv_unlock_hubobras';
    var GATE_HASH = '79065d4daf7a460f402dcdd81cebcb972024fe63d202750707067432f5b5542f';
    var pageContent = document.getElementById('page-content');
    var gateEl = document.getElementById('password-gate');
    if (!gateEl) return;
    var labelBusy = gateEl.dataset.labelBusy || 'Verificando...';
    var labelOk = gateEl.dataset.labelOk || 'Acesso liberado';

    function sha256Hex(text) {
      return crypto.subtle.digest('SHA-256', new TextEncoder().encode(text)).then(function (buf) {
        return Array.prototype.map.call(new Uint8Array(buf), function (b) { return b.toString(16).padStart(2, '0'); }).join('');
      });
    }
    function unlock() {
      if (pageContent) { pageContent.classList.remove('is-locked'); pageContent.removeAttribute('aria-hidden'); }
      gateEl.classList.add('is-hidden');
      document.body.style.overflow = '';
      setTimeout(function () { gateEl.style.display = 'none'; }, 400);
    }
    if (localStorage.getItem(GATE_KEY) === '1') { unlock(); return; }

    document.body.style.overflow = 'hidden';
    var input = document.getElementById('gate-password');
    var form = document.getElementById('gate-form');
    var errorMsg = document.getElementById('gate-error');
    var toggleBtn = document.getElementById('gate-toggle-visibility');
    var submitBtn = document.getElementById('gate-submit');
    var submitLabel = document.getElementById('gate-submit-label');
    var card = gateEl.querySelector('.gate-card');
    var labelIdle = submitLabel ? submitLabel.textContent : '';
    setTimeout(function () { if (input) input.focus(); }, 300);

    if (toggleBtn && input) {
      toggleBtn.addEventListener('click', function () {
        var showing = input.type === 'text';
        input.type = showing ? 'password' : 'text';
        toggleBtn.innerHTML = '<i data-lucide="' + (showing ? 'eye' : 'eye-off') + '" width="18" height="18"></i>';
        if (window.lucide) window.lucide.createIcons();
        input.focus();
      });
    }
    if (input) input.addEventListener('input', function () { if (errorMsg) errorMsg.classList.add('hidden'); });
    if (form) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var value = (input.value || '').trim();
        if (!value) { input.focus(); return; }
        submitBtn.disabled = true; submitLabel.textContent = labelBusy;
        sha256Hex(value).then(function (hash) {
          if (hash === GATE_HASH) {
            localStorage.setItem(GATE_KEY, '1');
            submitLabel.textContent = labelOk;
            if (errorMsg) errorMsg.classList.add('hidden');
            setTimeout(unlock, 350);
          } else {
            submitBtn.disabled = false; submitLabel.textContent = labelIdle;
            if (errorMsg) errorMsg.classList.remove('hidden');
            input.value = ''; input.focus();
            if (card) { card.classList.remove('gate-shake'); void card.offsetWidth; card.classList.add('gate-shake'); }
          }
        });
      });
    }
  })();
})();
