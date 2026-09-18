/* ==========================================================================
   Marco Vinicius — Portfólio
   Interações exclusivas da home: fundo reativo e decodificação do hero,
   tilt dos cards, filtro de skills, timeline, descrições expansíveis,
   contato (status, copiar e-mail, espiral) e modal de senha do Hub de Obras.
   ========================================================================== */
(function () {
  'use strict';

  var reduced = window.MV && window.MV.prefersReducedMotion ? window.MV.prefersReducedMotion : function () { return false; };
  var canHover = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var lang = (document.documentElement.lang || 'pt').slice(0, 2);

  /* ======================================================================
     HERO — fundo reativo (grade de pontos + foco de luz)
     ====================================================================== */
  (function heroBackground() {
    var hero = document.getElementById('hero');
    var canvas = document.getElementById('hero-canvas');
    var spot = hero && hero.querySelector('.hero-spot');
    if (!hero || !canvas) return;

    var ctx = canvas.getContext('2d');
    var dpr = Math.min(window.devicePixelRatio || 1, 1.5);
    var W = 0, H = 0, cols = 0, rows = 0;
    var GAP = 30, R = 180;
    var mouse = { x: -9999, y: -9999, tx: -9999, ty: -9999, active: false };
    var drift = { t: Math.random() * 100 };
    var raf = null, visible = true, lastMove = 0;
    var staticMode = reduced();

    function resize() {
      var rect = hero.getBoundingClientRect();
      W = rect.width; H = rect.height;
      canvas.width = Math.round(W * dpr);
      canvas.height = Math.round(H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      cols = Math.ceil(W / GAP) + 1;
      rows = Math.ceil(H / GAP) + 1;
      draw();
    }

    function draw() {
      ctx.clearRect(0, 0, W, H);
      var mx = mouse.x, my = mouse.y;
      var hasPointer = mx > -999;
      for (var i = 0; i < cols; i++) {
        for (var j = 0; j < rows; j++) {
          var x = i * GAP + (GAP / 2), y = j * GAP + (GAP / 2);
          var a = 0.10, r = 1;
          var ox = 0, oy = 0;
          if (hasPointer) {
            var dx = x - mx, dy = y - my;
            var d = Math.sqrt(dx * dx + dy * dy);
            if (d < R) {
              var f = 1 - d / R;
              f = f * f;
              a = 0.10 + f * 0.85;
              r = 1 + f * 1.6;
              var push = f * 9;
              ox = (dx / (d || 1)) * push;
              oy = (dy / (d || 1)) * push;
            }
          }
          // esmaece a grade nas bordas para não competir com o texto
          var edge = Math.min(y / (H * 0.25), 1) * Math.min((H - y) / (H * 0.25), 1);
          ctx.fillStyle = 'rgba(204,255,0,' + (a * Math.max(edge, 0.25)).toFixed(3) + ')';
          ctx.beginPath();
          ctx.arc(x + ox, y + oy, r, 0, Math.PI * 2);
          ctx.fill();
        }
      }
    }

    function frame(now) {
      raf = null;
      if (!visible) return;
      if (mouse.active) {
        mouse.x += (mouse.tx - mouse.x) * 0.16;
        mouse.y += (mouse.ty - mouse.y) * 0.16;
      } else {
        // sem ponteiro (touch) a luz vagueia sozinha, bem devagar
        drift.t += 0.0035;
        mouse.x = W * (0.5 + 0.38 * Math.sin(drift.t * 1.1));
        mouse.y = H * (0.45 + 0.28 * Math.cos(drift.t * 0.8));
      }
      if (spot) {
        spot.style.setProperty('--mx', mouse.x + 'px');
        spot.style.setProperty('--my', mouse.y + 'px');
      }
      draw();
      var idle = mouse.active && (now - lastMove > 2500);
      if (!idle) raf = requestAnimationFrame(frame);
    }
    function kick() { if (!raf && visible && !staticMode) raf = requestAnimationFrame(frame); }

    if (canHover) {
      hero.addEventListener('pointermove', function (e) {
        var rect = hero.getBoundingClientRect();
        mouse.tx = e.clientX - rect.left;
        mouse.ty = e.clientY - rect.top;
        if (!mouse.active) { mouse.x = mouse.tx; mouse.y = mouse.ty; }
        mouse.active = true;
        lastMove = performance.now();
        kick();
      });
      hero.addEventListener('pointerleave', function () {
        mouse.active = false;
        kick();
      });
    }

    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        visible = entries[0].isIntersecting;
        if (visible) kick();
      }, { threshold: 0 }).observe(hero);
    }
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) visible = false; else { visible = true; kick(); }
    });

    var rT;
    window.addEventListener('resize', function () { clearTimeout(rT); rT = setTimeout(resize, 120); });
    resize();
    if (staticMode) { mouse.x = W * 0.5; mouse.y = H * 0.45; draw(); }
    else kick();
  })();

  /* ======================================================================
     HERO — efeito de decodificação do título
     ====================================================================== */
  (function decodeTitle() {
    var el = document.querySelector('[data-decode]');
    if (!el || reduced()) return;
    var original = el.textContent.replace(/\s+/g, ' ').trim();
    var CHARS = '01<>/\\|[]{}=+*#_-';
    var STEP = 18, START = 350, FLIP = 40;

    var h = el.getBoundingClientRect().height;
    el.style.minHeight = h + 'px';
    el.setAttribute('aria-label', original);

    var spans = [];
    el.textContent = '';
    for (var i = 0; i < original.length; i++) {
      var ch = original[i];
      if (ch === ' ') { el.appendChild(document.createTextNode(' ')); spans.push(null); continue; }
      var s = document.createElement('span');
      s.className = 'dc dc-pending';
      s.setAttribute('aria-hidden', 'true');
      s.textContent = CHARS[Math.floor(Math.random() * CHARS.length)];
      el.appendChild(s);
      spans.push(s);
    }

    var t0 = performance.now(), lastFlip = 0;
    function tick(now) {
      var elapsed = now - t0;
      var front = Math.floor((elapsed - START) / STEP);
      var doFlip = now - lastFlip > FLIP;
      if (doFlip) lastFlip = now;
      var done = true;
      for (var k = 0; k < spans.length; k++) {
        var s = spans[k];
        if (!s || s.dataset.done) continue;
        if (k <= front) {
          s.textContent = original[k];
          s.classList.remove('dc-pending');
          s.dataset.done = '1';
        } else {
          done = false;
          if (doFlip && k < front + 14) s.textContent = CHARS[Math.floor(Math.random() * CHARS.length)];
        }
      }
      if (!done) requestAnimationFrame(tick);
      else {
        el.textContent = original;
        el.removeAttribute('aria-label');
        el.style.minHeight = '';
      }
    }
    requestAnimationFrame(tick);
  })();

  /* ======================================================================
     HERO — indicador de scroll some após rolar
     ====================================================================== */
  var cue = document.querySelector('.scroll-cue');
  var prevScroll = window.MV && window.MV.onScroll;
  var scrollHandlers = [];
  if (window.MV) window.MV.onScroll = function () { scrollHandlers.forEach(function (fn) { fn(); }); if (prevScroll) prevScroll(); };
  if (cue) scrollHandlers.push(function () { cue.classList.toggle('is-hidden', window.scrollY > 80); });

  /* ======================================================================
     PROJETOS — tilt 3D com brilho que segue o cursor
     ====================================================================== */
  (function tilt() {
    var cards = document.querySelectorAll('.tilt-card');
    if (!cards.length || !canHover || reduced()) return;
    var MAX = 6;
    cards.forEach(function (card) {
      var raf = null, px = 0, py = 0;
      function apply() {
        raf = null;
        var rx = (0.5 - py) * MAX * 2;
        var ry = (px - 0.5) * MAX * 2;
        card.style.transform = 'perspective(1100px) rotateX(' + rx.toFixed(2) + 'deg) rotateY(' + ry.toFixed(2) + 'deg) translateY(-8px)';
      }
      card.addEventListener('pointerenter', function () {
        card.classList.remove('is-resetting');
        card.classList.add('is-tilting');
      });
      card.addEventListener('pointermove', function (e) {
        var r = card.getBoundingClientRect();
        px = (e.clientX - r.left) / r.width;
        py = (e.clientY - r.top) / r.height;
        card.style.setProperty('--mx', (px * 100).toFixed(1) + '%');
        card.style.setProperty('--my', (py * 100).toFixed(1) + '%');
        if (!raf) raf = requestAnimationFrame(apply);
      });
      card.addEventListener('pointerleave', function () {
        card.classList.remove('is-tilting');
        card.classList.add('is-resetting');
        card.style.transform = '';
        setTimeout(function () { card.classList.remove('is-resetting'); }, 650);
      });
    });
  })();

  /* ======================================================================
     SKILLS — filtro por categoria com animação de reposicionamento (FLIP)
     ====================================================================== */
  (function skillsFilter() {
    var bar = document.getElementById('skills-filter');
    var grid = document.getElementById('skills-grid');
    if (!bar || !grid) return;
    var chips = bar.querySelectorAll('.skill-chip');
    var items = Array.prototype.slice.call(grid.children);
    var busy = false;

    function setFilter(cat) {
      if (busy) return;
      busy = true;
      chips.forEach(function (c) {
        var on = c.dataset.filter === cat;
        c.classList.toggle('is-active', on);
        c.setAttribute('aria-pressed', on ? 'true' : 'false');
      });

      var first = {};
      items.forEach(function (el) { first[el.dataset.key] = el.getBoundingClientRect(); });

      var toHide = [], toShow = [];
      items.forEach(function (el) {
        var match = cat === 'all' || el.dataset.cat === cat;
        var hidden = el.classList.contains('is-filtered-out');
        if (!match && !hidden) toHide.push(el);
        if (match && hidden) toShow.push(el);
      });

      var instant = reduced();
      var D = instant ? 0 : 220;
      toHide.forEach(function (el) {
        el.style.transition = 'opacity ' + D + 'ms ease, transform ' + D + 'ms ease';
        el.style.opacity = '0';
        el.style.transform = 'scale(0.9)';
      });

      setTimeout(function () {
        toHide.forEach(function (el) { el.classList.add('is-filtered-out'); el.style.transition = ''; el.style.opacity = ''; el.style.transform = ''; });
        toShow.forEach(function (el) { el.classList.remove('is-filtered-out'); el.style.opacity = '0'; el.style.transform = 'scale(0.9)'; });

        var last = {};
        items.forEach(function (el) { last[el.dataset.key] = el.getBoundingClientRect(); });

        items.forEach(function (el, i) {
          if (el.classList.contains('is-filtered-out')) return;
          var f = first[el.dataset.key], l = last[el.dataset.key];
          var isNew = toShow.indexOf(el) !== -1;
          if (isNew) {
            el.style.transition = 'none';
            void el.offsetWidth;
            el.style.transition = 'opacity 320ms ease ' + (i * 18) + 'ms, transform 320ms cubic-bezier(.22,1,.36,1) ' + (i * 18) + 'ms';
            el.style.opacity = '1';
            el.style.transform = '';
            return;
          }
          var dx = f.left - l.left, dy = f.top - l.top;
          if (!dx && !dy) return;
          el.style.transition = 'none';
          el.style.transform = 'translate(' + dx + 'px,' + dy + 'px)';
          void el.offsetWidth;
          el.style.transition = 'transform 380ms cubic-bezier(.22,1,.36,1)';
          el.style.transform = '';
        });
        setTimeout(function () {
          items.forEach(function (el) { el.style.transition = ''; el.style.opacity = ''; el.style.transform = ''; });
          busy = false;
        }, instant ? 0 : 420);
      }, D);
    }

    items.forEach(function (el, i) { el.dataset.key = String(i); });
    chips.forEach(function (chip) {
      chip.addEventListener('click', function () { setFilter(chip.dataset.filter); });
    });
  })();

  /* ======================================================================
     EXPERIÊNCIA — linha da timeline que se desenha + pontos que acendem
     ====================================================================== */
  (function timelines() {
    var lists = document.querySelectorAll('.timeline');
    if (!lists.length) return;
    var instant = reduced();
    function update() {
      var trigger = window.innerHeight * 0.72;
      lists.forEach(function (list) {
        var rect = list.getBoundingClientRect();
        var p = instant ? 1 : Math.min(Math.max((trigger - rect.top) / rect.height, 0), 1);
        list.style.setProperty('--p', p.toFixed(4));
        var lineY = rect.top + rect.height * p;
        list.querySelectorAll('.tl-dot').forEach(function (dot) {
          var d = dot.getBoundingClientRect();
          dot.classList.toggle('is-lit', instant || d.top + d.height / 2 <= lineY + 2);
        });
      });
    }
    scrollHandlers.push(update);
    window.addEventListener('resize', update);
    update();
  })();

  /* ======================================================================
     EXPERIÊNCIA — descrições expansíveis (só quando o texto estoura)
     ====================================================================== */
  (function expandable() {
    var blocks = document.querySelectorAll('[data-expandable]');
    if (!blocks.length) return;
    var CHEVRON = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>';
    function init() {
      blocks.forEach(function (block) {
        if (block.dataset.ready) return;
        var text = block.querySelector('.exp-text');
        if (!text) return;
        block.classList.add('is-clamped');
        var clampH = text.clientHeight;
        var fullH = text.scrollHeight;
        if (fullH <= clampH + 12) { block.classList.remove('is-clamped'); block.dataset.ready = '1'; return; }
        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'exp-toggle';
        btn.setAttribute('aria-expanded', 'false');
        btn.innerHTML = '<span>' + block.dataset.more + '</span>' + CHEVRON;
        block.appendChild(btn);
        btn.addEventListener('click', function () {
          var open = btn.getAttribute('aria-expanded') === 'true';
          if (open) {
            text.style.maxHeight = text.scrollHeight + 'px';
            void text.offsetWidth;
            block.classList.add('is-clamped');
            text.style.maxHeight = '';
            btn.setAttribute('aria-expanded', 'false');
            btn.firstChild.textContent = block.dataset.more;
          } else {
            text.style.maxHeight = text.scrollHeight + 'px';
            block.classList.remove('is-clamped');
            btn.setAttribute('aria-expanded', 'true');
            btn.firstChild.textContent = block.dataset.less;
            setTimeout(function () { text.style.maxHeight = ''; }, 480);
          }
        });
        block.dataset.ready = '1';
      });
    }
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(init); else init();
    init();
  })();

  /* ======================================================================
     CONTATO — status ao vivo com horário local
     ====================================================================== */
  (function liveStatus() {
    var clock = document.getElementById('local-time');
    if (!clock) return;
    var tz = clock.dataset.tz || 'America/Sao_Paulo';
    var fmt;
    try {
      fmt = new Intl.DateTimeFormat(lang === 'en' ? 'en-US' : 'pt-BR', { hour: '2-digit', minute: '2-digit', hour12: false, timeZone: tz });
    } catch (e) { return; }
    function tick() { clock.textContent = fmt.format(new Date()); }
    tick();
    setInterval(tick, 20000);
  })();

  /* ======================================================================
     CONTATO — copiar e-mail com feedback
     ====================================================================== */
  (function copyEmail() {
    var btns = document.querySelectorAll('.copy-email');
    if (!btns.length) return;
    var CHECK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>';
    function fallbackCopy(text) {
      var ta = document.createElement('textarea');
      ta.value = text; ta.setAttribute('readonly', ''); ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); } catch (e) {}
      document.body.removeChild(ta);
    }
    btns.forEach(function (btn) {
      var label = btn.querySelector('.copy-email__text');
      var icon = btn.querySelector('.copy-email__icon');
      var email = btn.dataset.email;
      var iconHTML = icon ? icon.innerHTML : '';
      var timer;
      btn.addEventListener('click', function () {
        var p = (navigator.clipboard && navigator.clipboard.writeText) ? navigator.clipboard.writeText(email) : Promise.reject();
        p.catch(function () { fallbackCopy(email); }).then(function () {
          btn.classList.add('is-copied');
          if (label) label.textContent = btn.dataset.copied;
          if (icon) icon.innerHTML = CHECK;
          clearTimeout(timer);
          timer = setTimeout(function () {
            btn.classList.remove('is-copied');
            if (label) label.textContent = email;
            if (icon) icon.innerHTML = iconHTML;
          }, 2000);
        });
      });
    });
  })();

  /* ======================================================================
     CONTATO — espiral que inclina em direção ao cursor
     ====================================================================== */
  (function orb() {
    var section = document.getElementById('contact');
    var shape = document.getElementById('contact-orb-shape');
    if (!section || !shape || !canHover || reduced()) return;
    var cur = { rx: 0, ry: 0, tx: 0, ty: 0 };
    var goal = { rx: 0, ry: 0, tx: 0, ty: 0 };
    var raf = null;
    function step() {
      var k = 0.08, moving = false;
      ['rx', 'ry', 'tx', 'ty'].forEach(function (p) {
        var diff = goal[p] - cur[p];
        if (Math.abs(diff) > 0.02) moving = true;
        cur[p] += diff * k;
      });
      shape.style.transform = 'rotateX(' + cur.rx.toFixed(2) + 'deg) rotateY(' + cur.ry.toFixed(2) + 'deg) translate3d(' + cur.tx.toFixed(1) + 'px,' + cur.ty.toFixed(1) + 'px,0)';
      raf = moving ? requestAnimationFrame(step) : null;
    }
    function kick() { if (!raf) raf = requestAnimationFrame(step); }
    section.addEventListener('pointermove', function (e) {
      var r = shape.getBoundingClientRect();
      var cx = r.left + r.width / 2, cy = r.top + r.height / 2;
      var nx = Math.max(-1, Math.min(1, (e.clientX - cx) / (window.innerWidth / 2)));
      var ny = Math.max(-1, Math.min(1, (e.clientY - cy) / (window.innerHeight / 2)));
      goal.ry = nx * 16; goal.rx = -ny * 16;
      goal.tx = nx * 18; goal.ty = ny * 18;
      kick();
    });
    section.addEventListener('pointerleave', function () {
      goal.rx = goal.ry = goal.tx = goal.ty = 0;
      kick();
    });
  })();

  /* ======================================================================
     HUB DE OBRAS — modal de senha (acesso restrito)
     ====================================================================== */
  (function gate() {
    var GATE_KEY = 'mv_unlock_hubobras';
    var GATE_HASH = '79065d4daf7a460f402dcdd81cebcb972024fe63d202750707067432f5b5542f';
    var trigger = document.getElementById('project-hub-obras');
    var modal = document.getElementById('hub-gate-modal');
    if (!trigger || !modal) return;

    var card = modal.querySelector('.hub-gate-card');
    var form = document.getElementById('hub-gate-form');
    var input = document.getElementById('hub-gate-password');
    var errorMsg = document.getElementById('hub-gate-error');
    var toggleBtn = document.getElementById('hub-gate-toggle-visibility');
    var submitBtn = document.getElementById('hub-gate-submit');
    var submitLabel = document.getElementById('hub-gate-submit-label');
    var cancelBtn = document.getElementById('hub-gate-cancel');
    var closeBtn = document.getElementById('hub-gate-close');
    var destination = trigger.getAttribute('href');
    var labelIdle = submitLabel ? submitLabel.textContent : '';
    var labelBusy = modal.dataset.labelBusy || 'Verificando...';
    var labelOk = modal.dataset.labelOk || 'Acesso liberado';
    var lastFocus = null;

    function sha256Hex(text) {
      return crypto.subtle.digest('SHA-256', new TextEncoder().encode(text)).then(function (buf) {
        return Array.prototype.map.call(new Uint8Array(buf), function (b) { return b.toString(16).padStart(2, '0'); }).join('');
      });
    }
    function focusables() {
      return Array.prototype.filter.call(modal.querySelectorAll('button, [href], input, [tabindex]:not([tabindex="-1"])'), function (el) {
        return !el.disabled && el.offsetParent !== null;
      });
    }
    function openModal() {
      lastFocus = document.activeElement;
      modal.classList.remove('hidden');
      modal.classList.add('flex');
      void modal.offsetWidth;
      modal.classList.remove('opacity-0');
      if (card) card.classList.remove('scale-95');
      document.body.style.overflow = 'hidden';
      setTimeout(function () { if (input) input.focus(); }, 200);
    }
    function closeModal() {
      modal.classList.add('opacity-0');
      if (card) card.classList.add('scale-95');
      document.body.style.overflow = '';
      setTimeout(function () {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
        if (input) input.value = '';
        if (errorMsg) errorMsg.classList.add('hidden');
        if (submitBtn) submitBtn.disabled = false;
        if (submitLabel) submitLabel.textContent = labelIdle;
        if (lastFocus && lastFocus.focus) lastFocus.focus();
      }, 300);
    }
    function isOpen() { return !modal.classList.contains('hidden'); }

    trigger.addEventListener('click', function (e) {
      if (localStorage.getItem(GATE_KEY) === '1') return;
      e.preventDefault();
      e.stopImmediatePropagation();
      openModal();
    }, true);

    if (closeBtn) closeBtn.addEventListener('click', closeModal);
    if (cancelBtn) cancelBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', function (e) { if (e.target === modal) closeModal(); });
    document.addEventListener('keydown', function (e) {
      if (!isOpen()) return;
      if (e.key === 'Escape') { closeModal(); return; }
      if (e.key === 'Tab') {
        var f = focusables();
        if (!f.length) return;
        var first = f[0], last = f[f.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });

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
        submitBtn.disabled = true;
        submitLabel.textContent = labelBusy;
        sha256Hex(value).then(function (hash) {
          if (hash === GATE_HASH) {
            localStorage.setItem(GATE_KEY, '1');
            submitLabel.textContent = labelOk;
            setTimeout(function () { window.location.href = destination; }, 400);
          } else {
            submitBtn.disabled = false;
            submitLabel.textContent = labelIdle;
            if (errorMsg) errorMsg.classList.remove('hidden');
            input.value = '';
            input.focus();
            if (card) { card.classList.remove('gate-shake'); void card.offsetWidth; card.classList.add('gate-shake'); }
          }
        });
      });
    }
  })();
})();
