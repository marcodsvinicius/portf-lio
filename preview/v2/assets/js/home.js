/* ==========================================================================
   Marco Vinicius — Portfólio
   Interações exclusivas da home: malha do hero (sinais e pulso ao toque),
   faixa de empresas, AI First, tilt dos cards, skills, timeline, descrições
   expansíveis, ficha da foto, recomendações, resumo em 30 segundos,
   contato (status, copiar e-mail, radar) e modal de senha do Hub de Obras.
   ========================================================================== */
(function () {
  'use strict';

  var reduced = window.MV && window.MV.prefersReducedMotion ? window.MV.prefersReducedMotion : function () { return false; };
  var canHover = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var lang = (document.documentElement.lang || 'pt').slice(0, 2);

  /* ======================================================================
     HERO — malha de nós com sinais percorrendo as conexões.
     Um toque ou clique no fundo dispara um pulso que acende a rede em ondas.
     ====================================================================== */
  (function heroBackground() {
    var hero = document.getElementById('hero');
    var canvas = document.getElementById('hero-canvas');
    var spot = hero && hero.querySelector('.hero-spot');
    if (!hero || !canvas) return;

    var ctx = canvas.getContext('2d');
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var LIME = '204,255,0';
    var RANGE = 170;   // alcance do cursor
    var PUSH = 7;      // quanto os nós se afastam do cursor
    var W = 0, H = 0, vignette = null;
    var nodes = [], edges = [], signals = [], waves = [];
    var HOP = 55;      // ms entre um anel de conexões e o próximo no pulso
    var GLOW = 900;    // ms que cada nó fica aceso depois que o pulso passa
    var mouse = { x: -9999, y: -9999, tx: -9999, ty: -9999, on: false };
    var raf = null, visible = false, last = 0;
    var still = reduced();

    /* Ruído determinístico: a malha fica igual a cada carregamento. */
    function noise(a, b) {
      var v = Math.sin(a * 12.9898 + b * 78.233) * 43758.5453;
      return v - Math.floor(v);
    }

    function build() {
      var step = W < 640 ? 46 : 62;
      var cols = Math.ceil(W / step) + 1;
      var rows = Math.ceil(H / step) + 1;
      var at = function (i, j) { return i * rows + j; };
      nodes = [];
      edges = [];
      for (var i = 0; i < cols; i++) {
        for (var j = 0; j < rows; j++) {
          nodes.push({
            x: i * step + (noise(i, j) - 0.5) * step * 0.5,
            y: j * step + (noise(j, i) - 0.5) * step * 0.5,
            dx: 0, dy: 0, g: 0, h: 0, pt: -1e9, pp: 1, pv: 0, fl: 0, e: []
          });
        }
      }
      function connect(a, b) {
        var k = edges.length;
        edges.push({ a: a, b: b, g: 0 });
        nodes[a].e.push(k);
        nodes[b].e.push(k);
      }
      for (i = 0; i < cols; i++) {
        for (j = 0; j < rows; j++) {
          if (i + 1 < cols) connect(at(i, j), at(i + 1, j));
          if (j + 1 < rows) connect(at(i, j), at(i, j + 1));
          if (i + 1 < cols && j + 1 < rows && noise(i * 3.7, j * 9.1) > 0.87) connect(at(i, j), at(i + 1, j + 1));
        }
      }
      signals = [];
      waves = [];
      if (still) return;
      var total = W < 640 ? 2 : 4;
      for (var n = 0; n < total; n++) signals.push(respawn(n * 500));
    }

    function respawn(wait) {
      for (var tries = 0; tries < 12; tries++) {
        var i = Math.floor(Math.random() * nodes.length);
        if (nodes[i] && nodes[i].e.length) {
          return {
            edge: nodes[i].e[Math.floor(Math.random() * nodes[i].e.length)],
            from: i,
            t: 0,
            hops: 5 + Math.floor(Math.random() * 10),
            wait: wait == null ? 300 + Math.random() * 1400 : wait
          };
        }
      }
      return { edge: -1, from: 0, t: 0, hops: 0, wait: 1000 };
    }

    function resize() {
      var rect = hero.getBoundingClientRect();
      W = rect.width; H = rect.height;
      canvas.width = Math.round(W * dpr);
      canvas.height = Math.round(H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      vignette = ctx.createRadialGradient(W / 2, H / 2, 0, W / 2, H / 2, Math.max(W, H) * 0.46);
      vignette.addColorStop(0, 'rgba(5,5,5,0.74)');
      vignette.addColorStop(0.55, 'rgba(5,5,5,0.34)');
      vignette.addColorStop(1, 'rgba(5,5,5,0)');
      build();
      draw();
    }

    function step(dt) {
      var i, n, e;
      for (i = 0; i < edges.length; i++) { e = edges[i]; if (e.g > 0) e.g = Math.max(0, e.g - dt * 0.0009); }
      for (i = 0; i < nodes.length; i++) { n = nodes[i]; if (n.g > 0) n.g = Math.max(0, n.g - dt * 0.0013); }
      for (i = 0; i < signals.length; i++) {
        var s = signals[i];
        if (s.wait > 0) { s.wait -= dt; continue; }
        e = edges[s.edge];
        if (!e) { signals[i] = respawn(); continue; }
        var a = nodes[e.a], b = nodes[e.b];
        var len = Math.sqrt((b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y - a.y)) || 1;
        e.g = 1;
        s.t += (dt * 0.17) / len;
        if (s.t < 1) continue;
        var end = s.from === e.a ? e.b : e.a;
        nodes[end].g = 1;
        s.hops--;
        var ways = nodes[end].e.filter(function (k) { return k !== s.edge; });
        if (s.hops <= 0 || !ways.length) { signals[i] = respawn(); continue; }
        s.edge = ways[Math.floor(Math.random() * ways.length)];
        s.from = end;
        s.t = 0;
      }
    }

    function draw() {
      if (!W) return;
      ctx.clearRect(0, 0, W, H);
      var i, n, e, a, b;
      var mx = mouse.x, my = mouse.y, has = mx > -999;
      var now = performance.now();

      /* posição exibida de cada nó, já com o empurrão do cursor */
      for (i = 0; i < nodes.length; i++) {
        n = nodes[i];
        n.dx = n.x; n.dy = n.y; n.h = 0;
        var age = now - n.pt;
        n.pv = still ? n.fl : (age < 0 || age > GLOW ? 0 : (1 - age / GLOW) * n.pp);
        if (!has) continue;
        var ox = n.x - mx, oy = n.y - my;
        var d = Math.sqrt(ox * ox + oy * oy);
        if (d >= RANGE) continue;
        var f = 1 - d / RANGE; f *= f;
        n.h = f;
        n.dx += (ox / (d || 1)) * f * PUSH;
        n.dy += (oy / (d || 1)) * f * PUSH;
      }

      /* conexões em repouso: um traço só, para não pesar */
      ctx.beginPath();
      for (i = 0; i < edges.length; i++) {
        e = edges[i]; a = nodes[e.a]; b = nodes[e.b];
        if (e.g > 0.02 || a.h > 0.02 || b.h > 0.02 || Math.min(a.pv, b.pv) > 0.02) continue;
        ctx.moveTo(a.dx, a.dy); ctx.lineTo(b.dx, b.dy);
      }
      ctx.strokeStyle = 'rgba(' + LIME + ',0.055)';
      ctx.lineWidth = 1;
      ctx.stroke();

      /* conexões acesas pelo sinal ou pelo cursor */
      for (i = 0; i < edges.length; i++) {
        e = edges[i]; a = nodes[e.a]; b = nodes[e.b];
        var lit = Math.max(e.g, (a.h + b.h) * 0.5, Math.min(a.pv, b.pv));
        if (lit <= 0.02) continue;
        ctx.beginPath();
        ctx.moveTo(a.dx, a.dy); ctx.lineTo(b.dx, b.dy);
        ctx.strokeStyle = 'rgba(' + LIME + ',' + (0.055 + lit * 0.5).toFixed(3) + ')';
        ctx.lineWidth = 1 + lit * 0.7;
        ctx.stroke();
      }

      /* nós em repouso */
      ctx.beginPath();
      for (i = 0; i < nodes.length; i++) {
        n = nodes[i];
        if (n.g > 0.02 || n.h > 0.02 || n.pv > 0.02) continue;
        ctx.moveTo(n.dx + 1.15, n.dy);
        ctx.arc(n.dx, n.dy, 1.15, 0, Math.PI * 2);
      }
      ctx.fillStyle = 'rgba(' + LIME + ',0.17)';
      ctx.fill();

      /* nós acesos, com anel de pulso quando o sinal chega */
      for (i = 0; i < nodes.length; i++) {
        n = nodes[i];
        var v = Math.max(n.g, n.h, n.pv);
        if (v <= 0.02) continue;
        ctx.beginPath();
        ctx.arc(n.dx, n.dy, 1.15 + v * 2.3, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(' + LIME + ',' + (0.17 + v * 0.78).toFixed(3) + ')';
        ctx.fill();
        if (n.g > 0.25) {
          ctx.beginPath();
          ctx.arc(n.dx, n.dy, (1 - n.g) * 26 + 3, 0, Math.PI * 2);
          ctx.strokeStyle = 'rgba(' + LIME + ',' + (n.g * 0.3).toFixed(3) + ')';
          ctx.lineWidth = 1;
          ctx.stroke();
        }
      }

      /* anel de luz que acompanha a onda do pulso */
      for (i = waves.length - 1; i >= 0; i--) {
        var w = waves[i], wa = now - w.t0;
        if (wa > w.life) { waves.splice(i, 1); continue; }
        ctx.beginPath();
        ctx.arc(w.x, w.y, wa * w.speed, 0, Math.PI * 2);
        ctx.strokeStyle = 'rgba(' + LIME + ',' + (w.a * (1 - wa / w.life)).toFixed(3) + ')';
        ctx.lineWidth = 1.5;
        ctx.stroke();
      }

      /* cabeça luminosa de cada sinal */
      for (i = 0; i < signals.length; i++) {
        var s = signals[i];
        if (s.wait > 0) continue;
        e = edges[s.edge];
        if (!e) continue;
        a = nodes[s.from === e.a ? e.a : e.b];
        b = nodes[s.from === e.a ? e.b : e.a];
        var x = a.dx + (b.dx - a.dx) * s.t;
        var y = a.dy + (b.dy - a.dy) * s.t;
        var halo = ctx.createRadialGradient(x, y, 0, x, y, 18);
        halo.addColorStop(0, 'rgba(' + LIME + ',0.5)');
        halo.addColorStop(1, 'rgba(' + LIME + ',0)');
        ctx.fillStyle = halo;
        ctx.beginPath(); ctx.arc(x, y, 18, 0, Math.PI * 2); ctx.fill();
        ctx.beginPath(); ctx.arc(x, y, 2.4, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(232,255,150,0.95)'; ctx.fill();
      }

      /* escurece o centro para o título continuar legível */
      if (vignette) { ctx.fillStyle = vignette; ctx.fillRect(0, 0, W, H); }
    }

    function frame(now) {
      raf = null;
      if (!visible) return;
      var dt = Math.min(now - last, 60) || 16;
      last = now;
      if (mouse.on) {
        mouse.x += (mouse.tx - mouse.x) * 0.16;
        mouse.y += (mouse.ty - mouse.y) * 0.16;
      }
      if (spot) {
        spot.style.setProperty('--mx', (mouse.on ? mouse.x : W / 2) + 'px');
        spot.style.setProperty('--my', (mouse.on ? mouse.y : H * 0.45) + 'px');
      }
      step(dt);
      draw();
      raf = requestAnimationFrame(frame);
    }
    function kick() { if (!raf && visible && !still) { last = performance.now(); raf = requestAnimationFrame(frame); } }

    /* Pulso: parte do nó mais próximo do toque e acende a rede anel por anel.
       Com movimento reduzido, os nós em volta só acendem e apagam no lugar. */
    function pulse(x, y, power, reach) {
      if (!nodes.length) return;
      power = power || 1;
      reach = reach || 16;
      var i, best = 0, bd = Infinity;
      for (i = 0; i < nodes.length; i++) {
        var ox = nodes[i].x - x, oy = nodes[i].y - y, d = ox * ox + oy * oy;
        if (d < bd) { bd = d; best = i; }
      }
      if (still) {
        var hit = [];
        for (i = 0; i < nodes.length; i++) {
          var sx = nodes[i].x - x, sy = nodes[i].y - y;
          if (sx * sx + sy * sy < 130 * 130) { nodes[i].fl = 1; hit.push(nodes[i]); }
        }
        draw();
        setTimeout(function () { hit.forEach(function (nd) { nd.fl = 0; }); draw(); }, GLOW);
        return;
      }
      var now = performance.now();
      var depth = [];
      for (i = 0; i < nodes.length; i++) depth.push(-1);
      depth[best] = 0;
      var queue = [best];
      for (var q = 0; q < queue.length; q++) {
        var cur = queue[q];
        if (depth[cur] >= reach) continue;
        var list = nodes[cur].e;
        for (var k = 0; k < list.length; k++) {
          var ed = edges[list[k]], nb = ed.a === cur ? ed.b : ed.a;
          if (depth[nb] < 0) { depth[nb] = depth[cur] + 1; queue.push(nb); }
        }
      }
      for (i = 0; i < nodes.length; i++) if (depth[i] >= 0) { nodes[i].pt = now + depth[i] * HOP; nodes[i].pp = power; }
      var stepPx = W < 640 ? 46 : 62;
      waves.push({ x: nodes[best].x, y: nodes[best].y, t0: now, speed: (stepPx / HOP) * 0.85, life: 1000, a: 0.4 * power });
      kick();
    }

    hero.addEventListener('click', function (ev) {
      if (ev.target.closest('a, button, input, select, textarea, label, [role="navigation"]')) return;
      var rect = hero.getBoundingClientRect();
      pulse(ev.clientX - rect.left, ev.clientY - rect.top);
    });

    if (canHover) {
      hero.addEventListener('pointermove', function (ev) {
        var rect = hero.getBoundingClientRect();
        mouse.tx = ev.clientX - rect.left;
        mouse.ty = ev.clientY - rect.top;
        if (!mouse.on) { mouse.x = mouse.tx; mouse.y = mouse.ty; }
        mouse.on = true;
        kick();
      });
      hero.addEventListener('pointerleave', function () {
        mouse.on = false;
        mouse.x = mouse.y = mouse.tx = mouse.ty = -9999;
      });
    }

    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        visible = entries[0].isIntersecting;
        if (visible) kick(); else if (raf) { cancelAnimationFrame(raf); raf = null; }
      }, { threshold: 0 }).observe(hero);
    } else { visible = true; }

    document.addEventListener('visibilitychange', function () {
      if (document.hidden) { visible = false; if (raf) { cancelAnimationFrame(raf); raf = null; } }
      else { visible = true; kick(); }
    });

    var tmr;
    window.addEventListener('resize', function () { clearTimeout(tmr); tmr = setTimeout(resize, 150); });
    resize();
    if (still) {
      for (var k = 0; k < nodes.length; k += 9) nodes[k].g = 0.5;
      draw();
    } else {
      visible = true;
      kick();
      setTimeout(function () { if (window.scrollY < H * 0.5) pulse(W / 2, H * 0.48, 0.45, 9); }, 1100);
    }
  })();

  /* ======================================================================
     JÁ ATUEI EM — cada empresa leva ao cargo na timeline e acende o item
     (a rolagem suave vem do site.js)
     ====================================================================== */
  (function companies() {
    document.querySelectorAll('.company[href^="#"]').forEach(function (link) {
      link.addEventListener('click', function () {
        var item = document.querySelector(link.getAttribute('href'));
        if (!item) return;
        clearTimeout(item._flash);
        item.classList.remove('is-flash');
        item._flash = setTimeout(function () {
          item.classList.add('is-flash');
          item._flash = setTimeout(function () { item.classList.remove('is-flash'); }, 2400);
        }, reduced() ? 0 : 700);
      });
    });
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
     AI FIRST — o terminal digita o prompt da capacidade em foco
     ====================================================================== */
  (function aiFirst() {
    var term = document.querySelector('.ai-term');
    var cards = Array.prototype.slice.call(document.querySelectorAll('.ai-card'));
    if (!term || !cards.length) return;
    var promptEl = term.querySelector('.ai-term__prompt');
    var outBox = term.querySelector('.ai-term__out');
    var outEl = term.querySelector('.ai-term__outtext');
    var still = reduced();
    var index = -1, typeTimer = null, nextTimer = null, hold = false, visible = false;

    function stop() { clearTimeout(typeTimer); clearTimeout(nextTimer); typeTimer = null; nextTimer = null; }
    function queue(delay) { if (!hold && visible && !still) nextTimer = setTimeout(advance, delay); }
    function advance() { show((index + 1) % cards.length, false); }

    function show(i, quick) {
      stop();
      index = i;
      cards.forEach(function (c, n) { c.classList.toggle('is-active', n === i); });
      var card = cards[i];
      var text = card.getAttribute('data-prompt') || '';
      var out = card.getAttribute('data-out') || '';
      if (still || quick) {
        promptEl.textContent = text;
        outEl.textContent = out;
        outBox.classList.add('is-on');
        queue(3600);
        return;
      }
      outBox.classList.remove('is-on');
      promptEl.textContent = '';
      var n = 0;
      (function type() {
        promptEl.textContent = text.slice(0, ++n);
        if (n < text.length) { typeTimer = setTimeout(type, 24); return; }
        outEl.textContent = out;
        typeTimer = setTimeout(function () { outBox.classList.add('is-on'); queue(3400); }, 320);
      })();
    }

    if (canHover) {
      cards.forEach(function (card, i) {
        card.addEventListener('pointerenter', function () { hold = true; show(i, true); });
        card.addEventListener('pointerleave', function () { hold = false; queue(2000); });
      });
    }

    var section = document.getElementById('ai-first') || term;
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        visible = entries[0].isIntersecting;
        if (!visible) { stop(); return; }
        if (index === -1) show(0, false); else queue(1600);
      }, { threshold: 0.2 }).observe(section);
    } else { visible = true; show(0, true); }
  })();

  /* ======================================================================
     AI FIRST — cartões de artigos vindos do bloco JSON #ai-articles
     ====================================================================== */
  (function aiArticles() {
    var box = document.getElementById('ai-articles-list');
    var data = document.getElementById('ai-articles');
    if (!box || !data) return;
    var items = [];
    try { items = JSON.parse(data.textContent) || []; } catch (e) { items = []; }
    var d = box.dataset;
    function esc(v) { return String(v == null ? '' : v).replace(/[&<>"]/g, function (c) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]; }); }
    function link(url, cls, inner) {
      return '<a class="' + cls + '" href="' + esc(url) + '" target="_blank" rel="noopener noreferrer">' + inner + '</a>';
    }
    var arrow = '<i data-lucide="arrow-up-right" class="w-4 h-4"></i>';
    if (!items.length) {
      box.innerHTML = link(d.profile, 'ai-article ai-article--empty',
        '<span class="ai-article__title">' + esc(d.emptyTitle) + '</span>' +
        '<span class="ai-article__cta">' + esc(d.emptyCta) + ' ' + arrow + '</span>');
    } else {
      box.innerHTML = items.map(function (a) {
        return link(a.url, 'ai-article',
          '<span class="ai-article__meta"><i data-lucide="newspaper" class="w-3.5 h-3.5"></i>' + esc(a.source || 'Medium') + (a.date ? ' · ' + esc(a.date) : '') + '</span>' +
          '<span class="ai-article__title">' + esc(a.title) + '</span>' +
          (a.summary ? '<span class="ai-article__sum">' + esc(a.summary) + '</span>' : '') +
          (a.result ? '<span class="ai-article__result">' + esc(a.result) + '</span>' : '') +
          '<span class="ai-article__cta">' + esc(d.cta) + ' ' + arrow + '</span>');
      }).join('');
    }
    if (window.lucide) window.lucide.createIcons();
  })();

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
     SKILLS — brilho que acompanha o cursor pelas bordas dos cards
     ====================================================================== */
  (function skillsSpotlight() {
    var grid = document.getElementById('skills-grid');
    if (!grid || !canHover || reduced()) return;
    var cards = Array.prototype.slice.call(grid.querySelectorAll('.skill-card'));
    var raf = null, lx = 0, ly = 0;
    function paint() {
      raf = null;
      cards.forEach(function (card) {
        var r = card.getBoundingClientRect();
        card.style.setProperty('--mx', (lx - r.left) + 'px');
        card.style.setProperty('--my', (ly - r.top) + 'px');
      });
    }
    grid.addEventListener('pointermove', function (e) {
      lx = e.clientX; ly = e.clientY;
      grid.classList.add('is-lit');
      if (!raf) raf = requestAnimationFrame(paint);
    });
    grid.addEventListener('pointerleave', function () { grid.classList.remove('is-lit'); });
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
    // fuso do Brasil calculado na hora (UTC-3; muda sozinho se voltar a ter horário de verão)
    var utc = document.getElementById('local-utc');
    if (utc) {
      try {
        var part = new Intl.DateTimeFormat('en-US', { timeZone: tz, timeZoneName: 'shortOffset' })
          .formatToParts(new Date()).filter(function (x) { return x.type === 'timeZoneName'; })[0];
        if (part && /GMT/.test(part.value)) utc.textContent = '(' + part.value.replace('GMT', 'UTC') + ')';
      } catch (e) { /* mantém o (UTC-3) do HTML */ }
    }
    function tick() { clock.textContent = fmt.format(new Date()); }
    tick();
    setInterval(tick, 20000);
  })();

  /* ======================================================================
     CONTATO — copiar e-mail com feedback
     ====================================================================== */
  (function copyEmail() {
    var btns = document.querySelectorAll('.copy-email, [data-copy-email]');
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
            if (label) label.textContent = btn.dataset.label || email;
            if (icon) icon.innerHTML = iconHTML;
          }, 2000);
        });
      });
    });
  })();

  /* ======================================================================
     SOBRE — ficha que escaneia a foto: uma linha lima varre a imagem e as
     etiquetas surgem quando ela passa pela altura de cada uma. Roda quando
     a foto aparece, ao passar o mouse e ao tocar.
     ====================================================================== */
  (function aboutHud() {
    var hud = document.querySelector('.about-hud');
    var photo = document.getElementById('about-photo');
    if (!hud || !photo) return;
    if (reduced()) { hud.classList.add('is-done'); return; }
    hud.classList.add('is-armed');
    var busy = false;
    function scan() {
      if (busy) return;
      busy = true;
      hud.classList.remove('is-scanning');
      void hud.offsetWidth;
      hud.classList.add('is-scanning');
      setTimeout(function () {
        hud.classList.add('is-done');
        hud.classList.remove('is-scanning');
        busy = false;
      }, 1600);
    }
    if (canHover) photo.addEventListener('pointerenter', scan);
    photo.addEventListener('click', scan);
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        if (!entries[0].isIntersecting) return;
        io.disconnect();
        setTimeout(scan, 300);
      }, { threshold: 0.5 });
      io.observe(photo);
    } else {
      hud.classList.add('is-done');
    }
  })();

  /* ======================================================================
     RECOMENDAÇÕES — uma por vez, trocando sozinha enquanto a seção está na
     tela. O anel no avatar marca o tempo até a próxima (mais longo para
     textos maiores); mouse em cima ou foco pausam, e qualquer escolha
     manual (avatar, setas ou deslizar no celular) encerra a troca automática.
     ====================================================================== */
  (function recommendations() {
    var box = document.querySelector('[data-recs]');
    if (!box) return;
    var slides = Array.prototype.slice.call(box.querySelectorAll('.rec'));
    var people = Array.prototype.slice.call(box.querySelectorAll('.recs__person'));
    var stage = box.querySelector('.recs__stage');
    var count = box.querySelector('.recs__count b');
    var row = box.querySelector('.recs__people');
    if (slides.length < 2 || people.length !== slides.length) return;
    var index = 0, inView = false, hovering = false, focused = false;

    box.classList.add('is-ready');
    if (reduced()) box.classList.add('is-manual');

    function pad(n) { return (n < 10 ? '0' : '') + n; }
    function show(i, manual) {
      index = (i + slides.length) % slides.length;
      var text = slides[index].querySelector('.rec__text');
      var chars = text ? text.textContent.length : 200;
      box.style.setProperty('--dur', Math.min(24, Math.max(6, 2.5 + chars * 0.045)).toFixed(1) + 's');
      if (manual) box.classList.add('is-manual');
      slides.forEach(function (sl, k) { sl.classList.toggle('is-active', k === index); });
      people.forEach(function (b, k) {
        if (k === index) b.setAttribute('aria-current', 'true'); else b.removeAttribute('aria-current');
      });
      if (count) count.textContent = pad(index + 1);
      var chip = people[index];
      if (row && row.scrollWidth > row.clientWidth + 2) {
        row.scrollTo({ left: chip.offsetLeft - row.clientWidth / 2 + chip.offsetWidth / 2, behavior: reduced() ? 'auto' : 'smooth' });
      }
    }
    function sync() { box.classList.toggle('is-paused', !inView || hovering || focused || document.hidden); }

    people.forEach(function (b, k) { b.addEventListener('click', function () { show(k, true); }); });
    var prev = box.querySelector('[data-rec-prev]'), next = box.querySelector('[data-rec-next]');
    if (prev) prev.addEventListener('click', function () { show(index - 1, true); });
    if (next) next.addEventListener('click', function () { show(index + 1, true); });

    /* fim do anel = próxima recomendação */
    box.addEventListener('animationend', function (e) {
      if (e.animationName !== 'rec-ring' || box.classList.contains('is-manual')) return;
      show(index + 1, false);
    });

    box.addEventListener('pointerenter', function (e) { if (e.pointerType === 'mouse') { hovering = true; sync(); } });
    box.addEventListener('pointerleave', function (e) { if (e.pointerType === 'mouse') { hovering = false; sync(); } });
    box.addEventListener('focusin', function () { focused = true; sync(); });
    box.addEventListener('focusout', function () { setTimeout(function () { focused = box.contains(document.activeElement); sync(); }, 0); });
    document.addEventListener('visibilitychange', sync);

    /* deslizar para os lados troca no toque */
    var sx = 0, sy = 0, tracking = false;
    stage.addEventListener('pointerdown', function (e) {
      if (e.pointerType === 'mouse') return;
      tracking = true; sx = e.clientX; sy = e.clientY;
    });
    stage.addEventListener('pointerup', function (e) {
      if (!tracking) return;
      tracking = false;
      var dx = e.clientX - sx, dy = e.clientY - sy;
      if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.3) show(index + (dx < 0 ? 1 : -1), true);
    });
    stage.addEventListener('pointercancel', function () { tracking = false; });

    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) { inView = entries[0].isIntersecting; sync(); }, { threshold: 0.35 }).observe(box);
    } else { inView = true; }
    show(0, false);
    sync();
  })();

  /* ======================================================================
     RESUMO EM 30 SEGUNDOS — abre pelo botão do cabeçalho ou pela tecla R.
     Cartão central no computador; no celular, folha que sobe de baixo e
     fecha arrastando a alça. Foco preso no diálogo e Esc para fechar.
     ====================================================================== */
  (function summary() {
    var dialog = document.getElementById('summary-dialog');
    var backdrop = document.getElementById('summary-backdrop');
    var trigger = document.getElementById('summary-btn');
    if (!dialog || !backdrop) return;
    var title = document.getElementById('summary-name');
    var grip = dialog.querySelector('.summary__grip');
    var gate = document.getElementById('hub-gate-modal');
    var lastFocus = null, hideTimer = null;

    function isOpen() { return dialog.classList.contains('is-open'); }
    function focusables() {
      return Array.prototype.filter.call(
        dialog.querySelectorAll('a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])'),
        function (el) { return el.offsetParent !== null; });
    }
    function open() {
      if (isOpen()) return;
      if (window.MV && window.MV.closeMenu) window.MV.closeMenu();
      clearTimeout(hideTimer);
      lastFocus = document.activeElement;
      dialog.hidden = false;
      backdrop.hidden = false;
      dialog.style.transition = '';
      dialog.style.transform = '';
      document.documentElement.classList.add('summary-lock');
      void dialog.offsetWidth;
      dialog.classList.add('is-open');
      backdrop.classList.add('is-open');
      setTimeout(function () { if (title) title.focus({ preventScroll: true }); }, 40);
    }
    function close(restoreFocus) {
      if (!isOpen()) return;
      dialog.classList.remove('is-open');
      backdrop.classList.remove('is-open');
      dialog.style.transition = '';
      dialog.style.transform = '';
      document.documentElement.classList.remove('summary-lock');
      hideTimer = setTimeout(function () { dialog.hidden = true; backdrop.hidden = true; }, reduced() ? 0 : 400);
      if (restoreFocus !== false && lastFocus && lastFocus.focus) lastFocus.focus({ preventScroll: true });
    }

    if (trigger) trigger.addEventListener('click', open);
    backdrop.addEventListener('click', function () { close(); });
    dialog.querySelectorAll('[data-summary-close]').forEach(function (b) { b.addEventListener('click', function () { close(); }); });

    /* "Ver cases": fecha e leva até os projetos */
    dialog.querySelectorAll('[data-summary-cases]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        e.preventDefault();
        close(false);
        var target = document.querySelector(a.getAttribute('href'));
        if (target) setTimeout(function () { target.scrollIntoView({ behavior: reduced() ? 'auto' : 'smooth', block: 'start' }); }, 30);
      });
    });
    /* Resultados levam ao case: fecha antes para a volta não reabrir travada */
    dialog.querySelectorAll('.summary__res a').forEach(function (a) {
      a.addEventListener('click', function () { close(false); });
    });
    window.addEventListener('pageshow', function (e) { if (e.persisted && isOpen()) close(false); });

    document.addEventListener('keydown', function (e) {
      if (isOpen()) {
        if (e.key === 'Escape') { e.preventDefault(); close(); return; }
        if (e.key === 'Tab') {
          var f = focusables();
          if (!f.length) return;
          var first = f[0], last = f[f.length - 1];
          var inside = dialog.contains(document.activeElement);
          if (e.shiftKey && (document.activeElement === first || !inside)) { e.preventDefault(); last.focus(); }
          else if (!e.shiftKey && (document.activeElement === last || !inside)) { e.preventDefault(); first.focus(); }
        }
        return;
      }
      if (e.key !== 'r' && e.key !== 'R') return;
      if (e.metaKey || e.ctrlKey || e.altKey || e.repeat) return;
      var el = e.target;
      if (el && (/^(INPUT|TEXTAREA|SELECT)$/.test(el.tagName) || el.isContentEditable)) return;
      if (gate && !gate.classList.contains('hidden')) return;
      e.preventDefault();
      open();
    });

    /* Arrastar a alça para baixo fecha a folha no celular */
    if (grip) {
      var y0 = 0, dy = 0, dragging = false;
      grip.addEventListener('pointerdown', function (e) {
        dragging = true; y0 = e.clientY; dy = 0;
        grip.setPointerCapture(e.pointerId);
        dialog.style.transition = 'none';
      });
      grip.addEventListener('pointermove', function (e) {
        if (!dragging) return;
        dy = Math.max(0, e.clientY - y0);
        dialog.style.transform = 'translateY(' + dy + 'px)';
      });
      var end = function () {
        if (!dragging) return;
        dragging = false;
        dialog.style.transition = '';
        if (dy > 90) close(); else dialog.style.transform = '';
      };
      grip.addEventListener('pointerup', end);
      grip.addEventListener('pointercancel', end);
    }
  })();

  /* ======================================================================
     CONTATO — radar de sinal: varredura contínua, pontos que acendem
     quando o feixe passa e um ponto extra onde o cursor está
     ====================================================================== */
  (function radar() {
    var section = document.getElementById('contact');
    var wrap = document.getElementById('contact-orb-shape');
    var canvas = document.getElementById('contact-canvas');
    if (!section || !wrap || !canvas) return;
    var ctx = canvas.getContext('2d');
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var S = 0, C = 0, R = 0;
    var angle = -Math.PI / 2, raf = null, visible = false;
    var staticMode = reduced();
    var pointer = null;
    var blips = [];
    var LIME = '204,255,0';

    function resize() {
      var r = wrap.getBoundingClientRect();
      S = r.width; C = S / 2; R = C - 6;
      canvas.width = Math.round(S * dpr); canvas.height = Math.round(S * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      if (!blips.length) seed();
      draw();
    }
    function seed() {
      blips = [];
      for (var i = 0; i < 7; i++) blips.push(newBlip());
    }
    function newBlip() {
      var a = Math.random() * Math.PI * 2, d = R * (0.25 + Math.random() * 0.68);
      return { x: C + Math.cos(a) * d, y: C + Math.sin(a) * d, a: a, lit: 0, life: 6 + Math.random() * 8 };
    }
    function angleDiff(a, b) { var d = (a - b) % (Math.PI * 2); if (d < 0) d += Math.PI * 2; return d; }

    function draw() {
      ctx.clearRect(0, 0, S, S);
      // fundo translúcido
      ctx.beginPath(); ctx.arc(C, C, R, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(0,0,0,0.35)'; ctx.fill();
      // anéis
      for (var i = 1; i <= 4; i++) {
        ctx.beginPath(); ctx.arc(C, C, (R / 4) * i, 0, Math.PI * 2);
        ctx.strokeStyle = 'rgba(' + LIME + ',' + (i === 4 ? 0.55 : 0.14) + ')';
        ctx.lineWidth = i === 4 ? 1.5 : 1; ctx.stroke();
      }
      // cruz
      ctx.strokeStyle = 'rgba(' + LIME + ',0.12)'; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(C - R, C); ctx.lineTo(C + R, C); ctx.moveTo(C, C - R); ctx.lineTo(C, C + R); ctx.stroke();
      // feixe de varredura
      var g = ctx.createConicGradient ? ctx.createConicGradient(angle, C, C) : null;
      ctx.save(); ctx.beginPath(); ctx.arc(C, C, R, 0, Math.PI * 2); ctx.clip();
      if (g) {
        g.addColorStop(0, 'rgba(' + LIME + ',0)');
        g.addColorStop(0.78, 'rgba(' + LIME + ',0)');
        g.addColorStop(0.97, 'rgba(' + LIME + ',0.22)');
        g.addColorStop(1, 'rgba(' + LIME + ',0.4)');
        ctx.fillStyle = g; ctx.fillRect(0, 0, S, S);
      }
      // linha do feixe
      ctx.beginPath(); ctx.moveTo(C, C); ctx.lineTo(C + Math.cos(angle) * R, C + Math.sin(angle) * R);
      ctx.strokeStyle = 'rgba(' + LIME + ',0.9)'; ctx.lineWidth = 1.5; ctx.stroke();
      // pontos
      blips.concat(pointer ? [pointer] : []).forEach(function (b) {
        var glow = b.lit;
        if (glow <= 0.02) return;
        ctx.beginPath(); ctx.arc(b.x, b.y, 3 + glow * 3, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(' + LIME + ',' + (0.25 + glow * 0.75) + ')'; ctx.fill();
        ctx.beginPath(); ctx.arc(b.x, b.y, 6 + (1 - glow) * 14, 0, Math.PI * 2);
        ctx.strokeStyle = 'rgba(' + LIME + ',' + (glow * 0.5) + ')'; ctx.lineWidth = 1; ctx.stroke();
      });
      ctx.restore();
    }

    function frame() {
      raf = null;
      if (!visible || staticMode) return;
      angle += 0.022;
      blips.forEach(function (b, i) {
        var d = angleDiff(angle, b.a);
        if (d < 0.08) b.lit = 1;
        b.lit = Math.max(0, b.lit - 0.012);
        b.life -= 1 / 60;
        if (b.life <= 0) blips[i] = newBlip();
      });
      if (pointer) {
        var d2 = angleDiff(angle, pointer.a);
        if (d2 < 0.08) pointer.lit = 1;
        pointer.lit = Math.max(0.35, pointer.lit - 0.012);
      }
      draw();
      raf = requestAnimationFrame(frame);
    }
    function kick() { if (!raf) raf = requestAnimationFrame(frame); }

    if (canHover) {
      var cur = { rx: 0, ry: 0 }, goal = { rx: 0, ry: 0 }, tiltRaf = null;
      function tiltStep() {
        tiltRaf = null; var moving = false;
        ['rx', 'ry'].forEach(function (k) { var d = goal[k] - cur[k]; if (Math.abs(d) > 0.02) moving = true; cur[k] += d * 0.08; });
        wrap.style.transform = 'rotateX(' + cur.rx.toFixed(2) + 'deg) rotateY(' + cur.ry.toFixed(2) + 'deg)';
        if (moving) tiltRaf = requestAnimationFrame(tiltStep);
      }
      section.addEventListener('pointermove', function (e) {
        var r = wrap.getBoundingClientRect();
        var cx = r.left + r.width / 2, cy = r.top + r.height / 2;
        var nx = Math.max(-1, Math.min(1, (e.clientX - cx) / (window.innerWidth / 2)));
        var ny = Math.max(-1, Math.min(1, (e.clientY - cy) / (window.innerHeight / 2)));
        goal.ry = nx * 12; goal.rx = -ny * 12;
        if (!tiltRaf && !staticMode) tiltRaf = requestAnimationFrame(tiltStep);
        // ponto do cursor, preso dentro do radar
        var dx = e.clientX - cx, dy = e.clientY - cy, dist = Math.sqrt(dx * dx + dy * dy);
        var max = R * 0.92, k = dist > max ? max / dist : 1;
        pointer = { x: C + dx * k, y: C + dy * k, a: Math.atan2(dy, dx), lit: pointer ? pointer.lit : 0.35 };
        if (staticMode) draw();
      });
      section.addEventListener('pointerleave', function () {
        goal.rx = goal.ry = 0; pointer = null;
        if (!tiltRaf && !staticMode) tiltRaf = requestAnimationFrame(tiltStep);
        if (staticMode) draw();
      });
    }

    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        visible = entries[0].isIntersecting;
        if (visible) kick();
      }, { threshold: 0.1 }).observe(wrap);
    } else { visible = true; kick(); }
    document.addEventListener('visibilitychange', function () { if (!document.hidden && visible) kick(); });
    var rT; window.addEventListener('resize', function () { clearTimeout(rT); rT = setTimeout(resize, 120); });
    resize();
    if (staticMode) { blips.forEach(function (b, i) { b.lit = i % 2 ? 0.8 : 0.4; }); draw(); }
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
