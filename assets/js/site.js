/* Vault Movement — site.js (v1). No dependencies. */
(function () {
  'use strict';

  /* ---- Settings to fill in (see docs/OPEN-CONFIRM-ITEMS.md) ---- */
  var GA4_ID = '';          // e.g. 'G-XXXXXXXXXX'  [confirm]
  var META_PIXEL_ID = '';   // e.g. '123456789012345' [confirm]
  var ZOHO_FORM = 'https://forms.zohopublic.in/cpkformszoho1/form/WebsiteLeads/formperma/JdH2H50F6gaokRRyTUzDz5V_0EQ9sQ6OEVGA_8cIyiU';
  // Our key -> the Zoho field alias that receives it (create these hidden fields in Zoho).
  var ZOHO_FIELDS = { page: 'page', programme: 'programme', studio: 'studio', utm_source: 'utm_source', utm_medium: 'utm_medium', utm_campaign: 'utm_campaign', gclid: 'gclid', fbclid: 'fbclid' };
  var CONSENT_KEY = 'vm_consent';

  var d = document, w = window, de = d.documentElement;
  de.classList.add('js');

  function store(k, v) { try { if (v === undefined) return w.localStorage.getItem(k); w.localStorage.setItem(k, v); } catch (e) { return null; } }
  function sstore(k, v) { try { if (v === undefined) return w.sessionStorage.getItem(k); w.sessionStorage.setItem(k, v); } catch (e) { return null; } }

  /* ---- Analytics events (sent only if analytics loaded after consent) ---- */
  w.dataLayer = w.dataLayer || [];
  function track(name, params) {
    params = params || {};
    w.dataLayer.push(Object.assign({ event: name }, params));
    if (typeof w.gtag === 'function') w.gtag('event', name, params);
    if (typeof w.fbq === 'function') w.fbq('trackCustom', name, params);
  }
  d.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('a,button') : null;
    if (!a) return;
    var href = a.getAttribute('href') || '';
    var pl = a.closest('[data-placement]');
    var placement = a.getAttribute('data-cta') || (pl ? pl.getAttribute('data-placement') : 'unspecified');
    if (href.indexOf('https://wa.me') === 0) track('whatsapp_click', { placement: placement, page: location.pathname });
    else if (href.indexOf('tel:') === 0) track('call_click', { placement: placement, page: location.pathname });
    else if (a.hasAttribute('data-cta')) track('cta_click', { placement: placement, page: location.pathname });
  });

  /* ---- Consent + analytics loading ---- */
  function loadAnalytics() {
    if (GA4_ID && !w.gtag) {
      var s = d.createElement('script'); s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA4_ID; d.head.appendChild(s);
      w.gtag = function () { w.dataLayer.push(arguments); };
      w.gtag('js', new Date()); w.gtag('config', GA4_ID);
    }
    if (META_PIXEL_ID && !w.fbq) {
      var n = w.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); };
      n.push = n; n.loaded = true; n.version = '2.0'; n.queue = [];
      var t = d.createElement('script'); t.async = true; t.src = 'https://connect.facebook.net/en_US/fbevents.js'; d.head.appendChild(t);
      w.fbq('init', META_PIXEL_ID); w.fbq('track', 'PageView');
    }
  }
  var banner = d.querySelector('.consent');
  function setConsent(v) { store(CONSENT_KEY, v); if (banner) banner.classList.remove('is-open'); if (v === 'all') loadAnalytics(); }
  if (banner) {
    var c = store(CONSENT_KEY);
    if (!c) banner.classList.add('is-open'); else if (c === 'all') loadAnalytics();
    banner.addEventListener('click', function (e) {
      var b = e.target.closest('[data-consent]'); if (b) setConsent(b.getAttribute('data-consent'));
    });
  }
  d.querySelectorAll('[data-open-consent]').forEach(function (b) {
    b.addEventListener('click', function () { if (banner) banner.classList.add('is-open'); });
  });

  /* ---- Thank-you page conversion ---- */
  if (d.body.getAttribute('data-page') === 'thank-you') {
    var fire = function () { track('form_submit', { form: 'experience_session' }); };
    if (store(CONSENT_KEY) === 'all') setTimeout(fire, 800); else fire();
  }

  /* ---- Sticky header shrink ---- */
  var hdr = d.querySelector('.hdr'), strip = d.querySelector('.topstrip');
  function onScroll() {
    if (!hdr) return;
    var limit = (strip ? strip.offsetHeight : 0) + 4;
    hdr.classList.toggle('is-scrolled', w.scrollY > limit);
  }
  w.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* ---- Mobile menu (details/summary) ---- */
  var mnav = d.querySelector('.mnav');
  if (mnav) {
    var sum = mnav.querySelector('summary');
    mnav.addEventListener('toggle', function () { sum.setAttribute('aria-expanded', mnav.open ? 'true' : 'false'); });
    mnav.addEventListener('click', function (e) { if (e.target.closest('a')) mnav.open = false; });
    w.addEventListener('resize', function () { if (w.innerWidth >= 1200) mnav.open = false; });
  }
  d.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (mnav && mnav.open) { mnav.open = false; mnav.querySelector('summary').focus(); }
    var dd = d.activeElement && d.activeElement.closest ? d.activeElement.closest('.dd') : null;
    if (dd) { var btn = dd.querySelector('button'); if (btn) { btn.focus(); btn.blur(); } }
  });
  d.querySelectorAll('.dd').forEach(function (dd) {
    var btn = dd.querySelector('button');
    dd.addEventListener('focusin', function () { btn.setAttribute('aria-expanded', 'true'); });
    dd.addEventListener('focusout', function () { setTimeout(function () { if (!dd.contains(d.activeElement)) btn.setAttribute('aria-expanded', 'false'); }, 0); });
    dd.addEventListener('mouseenter', function () { btn.setAttribute('aria-expanded', 'true'); });
    dd.addEventListener('mouseleave', function () { if (!dd.contains(d.activeElement)) btn.setAttribute('aria-expanded', 'false'); });
  });

  /* ---- First-touch attribution for the enquiry form ---- */
  var qs = new URLSearchParams(location.search);
  ['utm_source', 'utm_medium', 'utm_campaign', 'gclid', 'fbclid'].forEach(function (k) {
    var v = qs.get(k); if (v && !sstore('vm_' + k)) sstore('vm_' + k, v.slice(0, 200));
  });

  /* ---- Zoho form: lazy iframe with hidden-field prefill ---- */
  function zohoSrc(box) {
    var vals = {
      page: location.pathname,
      programme: box.getAttribute('data-programme') || '',
      studio: box.getAttribute('data-studio') || '',
      utm_source: sstore('vm_utm_source') || '', utm_medium: sstore('vm_utm_medium') || '',
      utm_campaign: sstore('vm_utm_campaign') || '', gclid: sstore('vm_gclid') || '', fbclid: sstore('vm_fbclid') || ''
    };
    var p = ['zf_rszfm=1'];
    Object.keys(ZOHO_FIELDS).forEach(function (k) { if (vals[k]) p.push(encodeURIComponent(ZOHO_FIELDS[k]) + '=' + encodeURIComponent(vals[k])); });
    return (box.getAttribute('data-form') || ZOHO_FORM) + '?' + p.join('&');
  }
  function mountZoho(box) {
    if (box.classList.contains('is-loaded')) return;
    var f = d.createElement('iframe');
    f.src = zohoSrc(box); f.title = box.getAttribute('data-title') || 'Book an Experience Session form';
    f.loading = 'lazy'; f.setAttribute('aria-label', f.title);
    box.appendChild(f); box.classList.add('is-loaded');
  }
  var zboxes = d.querySelectorAll('.zoho[data-zoho]');
  if ('IntersectionObserver' in w) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (en) { if (en.isIntersecting) { mountZoho(en.target); io.unobserve(en.target); } }); }, { rootMargin: '600px 0px' });
    zboxes.forEach(function (b) { io.observe(b); });
  } else { zboxes.forEach(mountZoho); }
  // Zoho posts "formperma|height" messages to resize its iframe.
  w.addEventListener('message', function (e) {
    if (typeof e.data !== 'string' || e.origin.indexOf('zoho') === -1) return;
    var parts = e.data.split('|'); if (parts.length < 2) return;
    var h = parseInt(parts[1], 10); if (!h) return;
    d.querySelectorAll('.zoho iframe').forEach(function (f) { if (f.src.indexOf(parts[0]) > -1) f.style.height = (h + 15) + 'px'; });
  });

  /* ---- Instagram reels: click to load ---- */
  d.addEventListener('click', function (e) {
    var b = e.target.closest('[data-ig]'); if (!b) return;
    e.preventDefault();
    var id = b.getAttribute('data-ig');
    var host = b.closest('.ig-card, .reel-wrap') || b;
    var f = d.createElement('iframe');
    f.className = 'ig-frame'; f.src = 'https://www.instagram.com/reel/' + id + '/embed/';
    f.title = 'Instagram reel'; f.loading = 'lazy'; f.allow = 'encrypted-media; picture-in-picture'; f.setAttribute('allowfullscreen', '');
    host.innerHTML = ''; host.appendChild(f);
  });

  /* ---- Google Maps: click to load ---- */
  d.addEventListener('click', function (e) {
    var b = e.target.closest('[data-map]'); if (!b) return;
    e.preventDefault();
    var box = b.closest('.map');
    var f = d.createElement('iframe');
    f.src = 'https://maps.google.com/maps?q=' + encodeURIComponent(b.getAttribute('data-map')) + '&z=15&output=embed';
    f.title = b.getAttribute('data-title') || 'Map'; f.loading = 'lazy'; f.referrerPolicy = 'no-referrer-when-downgrade';
    box.appendChild(f);
  });

  /* ---- Ported photos: hide broken images so the labelled placeholder shows ---- */
  d.querySelectorAll('img.photo').forEach(function (img) {
    function fail() { img.remove(); }
    if (img.complete && img.naturalWidth === 0) fail(); else img.addEventListener('error', fail);
  });
})();
