/* ------------------------------------------------------------------
   Bourgain-pedia — shared front-end.
   No build step, no dependencies; the data files are plain JS globals
   so the site also works when opened straight off the filesystem.
------------------------------------------------------------------ */
(function (global) {
  "use strict";

  var BP = {};

  /* ------------------------------------------------------------ util */

  function esc(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }
  BP.esc = esc;

  function el(html) {
    var t = document.createElement("template");
    t.innerHTML = html.trim();
    return t.content.firstElementChild;
  }
  BP.el = el;

  function num(n) {
    return n == null ? "—" : String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  }
  BP.num = num;

  /* ------------------------------------------------------ TeX → text

     zbMATH titles carry raw TeX ("\(L^ p\)", "\mathcal L^\infty").
     There is no MathJax here on purpose — the site must work offline —
     so titles are transliterated into Unicode, which reads well for the
     short formulas that appear in titles.                              */

  var SYMBOLS = {
    alpha: "α", beta: "β", gamma: "γ", delta: "δ", epsilon: "ε",
    varepsilon: "ε", zeta: "ζ", eta: "η", theta: "θ", vartheta: "ϑ",
    iota: "ι", kappa: "κ", lambda: "λ", mu: "μ", nu: "ν", xi: "ξ",
    pi: "π", rho: "ρ", sigma: "σ", tau: "τ", upsilon: "υ", phi: "φ",
    varphi: "φ", chi: "χ", psi: "ψ", omega: "ω",
    Gamma: "Γ", Delta: "Δ", Theta: "Θ", Lambda: "Λ", Xi: "Ξ", Pi: "Π",
    Sigma: "Σ", Upsilon: "Υ", Phi: "Φ", Psi: "Ψ", Omega: "Ω",
    ell: "ℓ", infty: "∞", partial: "∂", nabla: "∇", times: "×",
    cdot: "·", cdots: "⋯", ldots: "…", dots: "…", leq: "≤", le: "≤",
    geq: "≥", ge: "≥", neq: "≠", ne: "≠", approx: "≈", sim: "∼",
    simeq: "≃", cong: "≅", equiv: "≡", propto: "∝", subset: "⊂",
    subseteq: "⊆", supset: "⊃", supseteq: "⊇", in: "∈", notin: "∉",
    cap: "∩", cup: "∪", setminus: "∖", emptyset: "∅", varnothing: "∅",
    forall: "∀", exists: "∃", to: "→", rightarrow: "→", mapsto: "↦",
    Rightarrow: "⇒", leftrightarrow: "↔", oplus: "⊕", otimes: "⊗",
    uparrow: "↑", downarrow: "↓", nearrow: "↗", searrow: "↘", gets: "←",
    leftarrow: "←", hookrightarrow: "↪", twoheadrightarrow: "↠", ll: "≪",
    gg: "≫", lesssim: "≲", gtrsim: "≳", asymp: "≍", bmod: "mod",
    binom: "choose", overline: "", underline: "", mathord: "",
    sum: "∑", prod: "∏", int: "∫", iint: "∬", sqrt: "√", pm: "±",
    mp: "∓", circ: "∘", star: "⋆", ast: "∗", perp: "⊥", angle: "∠",
    aleph: "ℵ", hbar: "ℏ", Re: "ℜ", Im: "ℑ", wp: "℘", deg: "deg",
    lvert: "|", rvert: "|", vert: "|", Vert: "‖", langle: "⟨",
    rangle: "⟩", quad: " ", qquad: "  ", colon: ":", prime: "′"
  };

  var BB = { A: "𝔸", B: "𝔹", C: "ℂ", D: "𝔻", E: "𝔼", F: "𝔽", G: "𝔾",
             H: "ℍ", I: "𝕀", J: "𝕁", K: "𝕂", L: "𝕃", M: "𝕄", N: "ℕ",
             O: "𝕆", P: "ℙ", Q: "ℚ", R: "ℝ", S: "𝕊", T: "𝕋", U: "𝕌",
             V: "𝕍", W: "𝕎", X: "𝕏", Y: "𝕐", Z: "ℤ" };

  var CAL = { A: "𝒜", B: "ℬ", C: "𝒞", D: "𝒟", E: "ℰ", F: "ℱ", G: "𝒢",
              H: "ℋ", I: "ℐ", J: "𝒥", K: "𝒦", L: "ℒ", M: "ℳ", N: "𝒩",
              O: "𝒪", P: "𝒫", Q: "𝒬", R: "ℛ", S: "𝒮", T: "𝒯", U: "𝒰",
              V: "𝒱", W: "𝒲", X: "𝒳", Y: "𝒴", Z: "𝒵" };

  var SUP = { "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵",
              "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹", "+": "⁺", "-": "⁻",
              "=": "⁼", "(": "⁽", ")": "⁾", n: "ⁿ", i: "ⁱ", p: "ᵖ",
              q: "𐞥", s: "ˢ", d: "ᵈ", k: "ᵏ", m: "ᵐ", x: "ˣ", a: "ᵃ",
              b: "ᵇ", c: "ᶜ", e: "ᵉ", f: "ᶠ", g: "ᵍ", h: "ʰ", j: "ʲ",
              l: "ˡ", o: "ᵒ", r: "ʳ", t: "ᵗ", u: "ᵘ", v: "ᵛ", w: "ʷ",
              y: "ʸ", z: "ᶻ", "*": "*", "/": "ᐟ" };
  // no superscript comma exists, so "W^{s,p}" falls back to "W^(s,p)"

  var SUB = { "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅",
              "6": "₆", "7": "₇", "8": "₈", "9": "₉", "+": "₊", "-": "₋",
              "=": "₌", "(": "₍", ")": "₎", a: "ₐ", e: "ₑ", h: "ₕ",
              i: "ᵢ", j: "ⱼ", k: "ₖ", l: "ₗ", m: "ₘ", n: "ₙ", o: "ₒ",
              p: "ₚ", r: "ᵣ", s: "ₛ", t: "ₜ", u: "ᵤ", v: "ᵥ", x: "ₓ" };

  /* Sentinels so a fallback like "^(s,p)" is not re-processed by the next
     superscript pass, which would turn its parentheses into ⁽ ⁾. */
  var SUP_MARK = "\u0001", SUB_MARK = "\u0002";

  function script(body, table, marker) {
    var out = "", ok = true;
    for (var i = 0; i < body.length; i++) {
      var c = body[i];
      if (c === " ") continue;
      if (table[c]) { out += table[c]; } else { ok = false; break; }
    }
    if (ok && out) return out;
    body = body.trim();
    return marker + (body.length > 1 ? "(" + body + ")" : body);
  }

  BP.tex = function (raw) {
    if (!raw) return "";
    var s = String(raw);

    s = s.replace(/\\(?:mathbb|Bbb)\s*\{?\s*([A-Z])\s*\}?/g,
                  function (_, c) { return BB[c] || c; });
    s = s.replace(/\\(?:mathcal|cal|mathscr)\s*\{?\s*([A-Z])\s*\}?/g,
                  function (_, c) { return CAL[c] || c; });
    s = s.replace(/\\(?:mathrm|mathbf|mathit|mathsf|text|textrm|textit|hbox|operatorname)\s*\{([^{}]*)\}/g, "$1");
    s = s.replace(/\\(?:hat|bar|tilde|widehat|widetilde|overline|vec|dot)\s*\{([^{}]*)\}/g, "$1");
    s = s.replace(/\\frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}/g, "$1/$2");
    s = s.replace(/\\(?:left|right|big|Big|bigg|Bigg|displaystyle|nolimits|limits)\b/g, "");

    s = s.replace(/\\([a-zA-Z]+)/g, function (m, name) {
      return Object.prototype.hasOwnProperty.call(SYMBOLS, name) ? SYMBOLS[name] : m;
    });

    s = s.replace(/\^\s*\{([^{}]*)\}/g, function (_, b) { return script(b, SUP, SUP_MARK); });
    s = s.replace(/\^\s*([A-Za-z0-9+\-*]|.)/g, function (_, b) { return script(b, SUP, SUP_MARK); });
    s = s.replace(/_\s*\{([^{}]*)\}/g, function (_, b) { return script(b, SUB, SUB_MARK); });
    s = s.replace(/_\s*([A-Za-z0-9+\-*]|.)/g, function (_, b) { return script(b, SUB, SUB_MARK); });

    s = s.replace(/\\[(){}[\]]/g, "").replace(/\$+/g, "");
    s = s.replace(/\\[,;:!> ]/g, " ");
    s = s.replace(/[{}]/g, "");
    s = s.replace(/``|''/g, '"');
    s = s.split(SUP_MARK).join("^").split(SUB_MARK).join("_");
    s = s.replace(/\s{2,}/g, " ").trim();
    return s;
  };

  /* ---------------------------------------------------------- layout */

  var NAV = [
    { href: "index.html",         label: "Bourgain-pedia", key: "home" },
    { href: "articles.html",      label: "All articles",   key: "articles" },
    { href: "toolkit.html",       label: "Bourgain's toolkit", key: "toolkit" },
    { href: "collaborators.html", label: "Collaborators",  key: "collaborators" },
    { href: "about.html",         label: "Method",         key: "about" }
  ];

  BP.layout = function (page) {
    var head = document.createElement("header");
    head.className = "masthead";
    head.innerHTML =
      '<div class="masthead-inner">' +
        '<a class="wordmark" href="index.html">Bourgain-pedia</a>' +
        '<span class="tagline">An encyclopedia of the work of Jean Bourgain (1954–2018)</span>' +
      "</div>" +
      '<nav class="primary">' +
        NAV.map(function (n) {
          return '<a href="' + n.href + '"' +
                 (n.key === page ? ' aria-current="page"' : "") + ">" + esc(n.label) + "</a>";
        }).join("") +
      "</nav>";
    document.body.insertBefore(head, document.body.firstChild);

    var papers = global.BOURGAIN_PAPERS || {};
    var foot = document.createElement("footer");
    foot.className = "colophon";
    foot.innerHTML =
      '<div class="colophon-inner">' +
        "<span>Bibliography merged from zbMATH Open, OpenAlex and arXiv. " +
        "Summaries, digestions and toolkit entries are written by this project.</span>" +
        "<span>Bibliography built " + esc(papers.generated || "—") +
        " · citation counts " + esc(papers.citations_updated || "—") + "</span>" +
      "</div>";
    document.body.appendChild(foot);
  };

  /* ------------------------------------------------------ paper cards */

  function authorLine(p) {
    if (!p.authors || !p.authors.length) return "Bourgain, Jean";
    return p.authors.map(function (a) {
      var self = /bourgain/i.test(a);
      return '<span class="' + (self ? "self" : "") + '">' + esc(a) + "</span>";
    }).join("; ");
  }

  function metaBits(p) {
    var bits = [];
    if (p.type) bits.push(esc(p.type));
    if (p.languages && p.languages.length && p.languages.join() !== "English") {
      bits.push(esc(p.languages.join(", ")));
    }
    if (p.zbl) bits.push("Zbl <code>" + esc(p.zbl) + "</code>");
    if (p.doi) bits.push("DOI <code>" + esc(p.doi) + "</code>");
    if (p.arxiv) bits.push("arXiv <code>" + esc(p.arxiv) + "</code>");
    if (p.msc && p.msc.length) bits.push("MSC " + esc(p.msc.slice(0, 5).join(", ")));
    return bits;
  }

  BP.paperCard = function (p) {
    var cited = p.cited_by == null
      ? '<span class="cites none" title="not indexed by OpenAlex">cited by —</span>'
      : '<span class="cites" title="OpenAlex citation count">cited by <b>' +
        num(p.cited_by) + "</b></span>";

    var links = (p.links || []).map(function (l) {
      return '<a class="chip' + (l.url === p.primary_link ? " primary" : "") +
             '" href="' + esc(l.url) + '" target="_blank" rel="noopener">' +
             esc(l.label) + "</a>";
    }).join("");
    if (!links) links = '<span class="chip tag">no online copy located</span>';

    var summary = p.summary
      ? '<p class="slot-body">' + esc(p.summary) + "</p>"
      : '<p class="slot-body empty">Not yet written — this is the project’s own ' +
        "précis of the paper, not its abstract.</p>";

    var digestion = p.digestion
      ? '<p class="slot-body"><a href="' + esc(p.digestion) + '">' +
        esc(p.digestion) + "</a></p>"
      : '<p class="slot-body empty">Not yet produced — run <code>/bourgainize</code> ' +
        "to expand this paper.</p>";

    var bits = metaBits(p);

    return '<li class="paper" id="' + esc(p.id) + '">' +
      '<div class="paper-head">' +
        '<h3 class="paper-title">' + esc(BP.tex(p.title)) + "</h3>" + cited +
      "</div>" +
      '<p class="paper-authors">' + authorLine(p) + "</p>" +
      (p.reference ? '<p class="paper-ref">' + esc(BP.tex(p.reference)) + "</p>" : "") +
      (bits.length ? '<p class="paper-meta">' +
        bits.map(function (b) { return "<span>" + b + "</span>"; }).join("") + "</p>" : "") +
      '<div class="slot' + (p.summary ? " filled" : "") + '">' +
        '<p class="slot-label">Summary</p>' + summary +
      "</div>" +
      '<div class="slot' + (p.digestion ? " filled" : "") + '">' +
        '<p class="slot-label">Digestion</p>' + digestion +
      "</div>" +
      '<p class="paper-links">' + links + "</p>" +
    "</li>";
  };

  /* --------------------------------------------------------- helpers */

  BP.fold = function (s) {
    return String(s || "").normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
  };

  BP.debounce = function (fn, ms) {
    var t;
    return function () {
      var args = arguments, self = this;
      clearTimeout(t);
      t = setTimeout(function () { fn.apply(self, args); }, ms || 140);
    };
  };

  global.BP = BP;
})(window);
