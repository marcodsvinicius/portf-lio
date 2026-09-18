/* ==========================================================================
   Marco Vinicius — Portfólio
   Comportamentos compartilhados: menu, cabeçalho, scrollspy, reveal,
   transições entre páginas, voltar ao topo. Carregado com `defer`.
   ========================================================================== */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  var prefersReducedMotion = function () { return reduceMotion.matches; };
  window.MV = window.MV || {};
  window.MV.prefersReducedMotion = prefersReducedMotion;

  /* --- Ícones ------------------------------------------------------------- */
  function icons() { if (window.lucide) window.lucide.createIcons(); }
  icons();

  /* --- Revela a página (evita flash sem estilo do Tailwind CDN) ----------- */
  function ready() { document.body.classList.add('is-ready'); }
  if (window.tailwind || document.readyState === 'complete') ready();
  else { window.addEventListener('load', ready); setTimeout(ready, 400); }

  /* --- Menu lateral (gaveta) --------------------------------------------- */
  var menuBtn = document.getElementById('mobile-menu-btn');
  var drawer = document.getElementById('mobile-menu-drawer');
  var backdrop = document.getElementById('mobile-menu-backdrop');

  function setMenu(open) {
    if (!menuBtn || !drawer || !backdrop) return;
    drawer.classList.toggle('opacity-100', open);
    drawer.classList.toggle('opacity-0', !open);
    drawer.classList.toggle('pointer-events-auto', open);
    drawer.classList.toggle('pointer-events-none', !open);
    drawer.classList.toggle('scale-100', open);
    drawer.classList.toggle('scale-95', !open);
    backdrop.classList.toggle('opacity-100', open);
    backdrop.classList.toggle('opacity-0', !open);
    backdrop.classList.toggle('pointer-events-none', !open);
    menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    menuBtn.innerHTML = '<i data-lucide="' + (open ? 'x' : 'menu') + '" class="w-6 h-6 text-white transition-transform duration-300"></i>';
    icons();
    document.body.style.overflow = (open && window.innerWidth < 768) ? 'hidden' : '';
  }
  window.MV.closeMenu = function () { setMenu(false); };

  if (menuBtn) {
    menuBtn.addEventListener('click', function () {
      setMenu(!drawer.classList.contains('opacity-100'));
    });
  }
  if (backdrop) backdrop.addEventListener('click', function () { setMenu(false); });
  document.querySelectorAll('.mobile-nav-link').forEach(function (link) {
    link.addEventListener('click', function () { setMenu(false); });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && drawer && drawer.classList.contains('opacity-100')) setMenu(false);
  });

  /* --- Cabeçalho ganha vidro ao rolar ------------------------------------ */
  var logoBox = document.getElementById('logo-box');
  var heroEl = document.getElementById('hero') || document.querySelector('header');
  function headerState() {
    var scrolled = window.scrollY > ((heroEl ? heroEl.offsetHeight : 100) - 80);
    [logoBox, menuBtn].forEach(function (el) {
      if (!el) return;
      el.classList.toggle('backdrop-blur-xl', scrolled);
      el.classList.toggle('bg-black/60', scrolled);
      el.classList.toggle('bg-transparent', !scrolled);
      el.classList.toggle('border-white/10', scrolled);
      el.classList.toggle('border-transparent', !scrolled);
      el.classList.toggle('shadow-lg', scrolled);
      el.classList.toggle('shadow-none', !scrolled);
    });
  }

  /* --- Scrollspy da gaveta ------------------------------------------------ */
  var sections = document.querySelectorAll('section[id]');
  var navItems = document.querySelectorAll('[data-mobile-section]');
  if (sections.length && navItems.length && 'IntersectionObserver' in window) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var id = '#' + entry.target.id;
        navItems.forEach(function (item) {
          var active = item.getAttribute('href') === id;
          item.classList.toggle('text-lime', active);
          item.classList.toggle('bg-white/10', active);
          item.classList.toggle('text-gray-400', !active);
          item.classList.toggle('hover:bg-white/5', !active);
        });
      });
    }, { root: null, rootMargin: '-30% 0px -60% 0px', threshold: 0 });
    sections.forEach(function (s) { spy.observe(s); });
  }

  /* --- Scroll suave em âncoras internas ---------------------------------- */
  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var id = link.getAttribute('href');
      if (!id || id === '#') return;
      var target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: prefersReducedMotion() ? 'auto' : 'smooth', block: 'start' });
    });
  });

  /* --- Reveal no scroll --------------------------------------------------- */
  var revealEls = document.querySelectorAll('.reveal');
  if (revealEls.length) {
    if ('IntersectionObserver' in window && !prefersReducedMotion()) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        });
      }, { rootMargin: '0px 0px -10% 0px', threshold: 0.08 });
      revealEls.forEach(function (el) { io.observe(el); });
    } else {
      revealEls.forEach(function (el) { el.classList.add('is-visible'); });
    }
  }

  /* --- Voltar ao topo ----------------------------------------------------- */
  var backTop = document.getElementById('back-to-top');
  function alignBackTop() {
    if (!backTop) return;
    if (menuBtn) {
      var rect = menuBtn.getBoundingClientRect();
      backTop.style.right = (window.innerWidth - rect.right) + 'px';
    }
  }
  function backTopState() {
    if (!backTop) return;
    backTop.classList.toggle('is-visible', window.scrollY > window.innerHeight * 0.9);
  }
  if (backTop) {
    backTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: prefersReducedMotion() ? 'auto' : 'smooth' });
    });
    alignBackTop();
    window.addEventListener('resize', alignBackTop);
  }

  /* --- Um único listener de scroll, sincronizado com o frame -------------- */
  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      headerState();
      backTopState();
      if (window.MV.onScroll) window.MV.onScroll();
      ticking = false;
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  headerState();
  backTopState();

  /* --- Transição de saída para navegadores sem View Transitions ---------- */
  var hasCrossDocVT = 'startViewTransition' in document && CSS.supports && CSS.supports('view-transition-name: x');
  if (!hasCrossDocVT && !prefersReducedMotion()) {
    document.addEventListener('click', function (e) {
      var a = e.target.closest && e.target.closest('a[href]');
      if (!a || a.target === '_blank' || a.hasAttribute('download') || e.defaultPrevented) return;
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;
      var url;
      try { url = new URL(a.href, location.href); } catch (err) { return; }
      if (url.origin !== location.origin) return;
      if (url.pathname === location.pathname && url.hash) return;
      if (!/^https?:$/.test(url.protocol)) return;
      e.preventDefault();
      document.body.classList.add('is-leaving');
      setTimeout(function () { location.href = url.href; }, 200);
    });
    window.addEventListener('pageshow', function (e) {
      if (e.persisted) document.body.classList.remove('is-leaving');
    });
  }
})();
