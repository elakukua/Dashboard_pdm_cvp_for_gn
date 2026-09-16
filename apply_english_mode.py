import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update CSS for icon buttons and language toggle
css_search = """/* Dark mode toggle button */
.theme-btn {
  background: none;
  border: 1px solid var(--b-line);
  border-radius: 6px;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--d-2);
  transition: all .2s;
  flex-shrink: 0;
  padding: 0;
}
.theme-btn:hover {
  background: var(--bg-card);
  color: var(--t);
  border-color: var(--d-3);
}"""

css_replace = """/* Mode switchers (Theme & Language) - pure icon buttons */
.aside-actions {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-shrink: 0;
}
.mob-actions {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-shrink: 0;
}
.theme-btn, .lang-btn {
  background: none;
  border: 1px solid var(--b-line);
  border-radius: 6px;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--d-2);
  transition: all .2s ease;
  flex-shrink: 0;
  padding: 0;
  position: relative;
}
.theme-btn:hover, .lang-btn:hover {
  background: var(--bg-card);
  color: var(--t);
  border-color: var(--d-3);
}
.lang-btn.active-en {
  color: var(--o);
  border-color: var(--o);
  background: var(--o-3);
}
.mob-btn.active-en {
  color: var(--o);
  border-color: var(--o);
}"""

assert css_search in html, "Could not find css_search"
html = html.replace(css_search, css_replace)

# 2. Update Mobile Bar and Sidebar Markup (adding language icon button next to theme toggle, purely icon-based)
mob_search = """<div class="mobile-bar">
  <button type="button" class="mob-btn" id="mob-menu-toggle" aria-label="Menu Navigasi">
    <svg viewBox="0 0 24 24"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
  </button>
  <span class="mob-title">Dashboard PDM CVP for GN</span>
  <button type="button" class="mob-btn" id="mob-theme-toggle" aria-label="Ganti Mode Gelap / Terang" title="Ganti Mode Gelap / Terang">
    <svg class="icon-moon" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
    <svg class="icon-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
  </button>
</div>"""

mob_replace = """<div class="mobile-bar">
  <button type="button" class="mob-btn" id="mob-menu-toggle" aria-label="Menu Navigasi">
    <svg viewBox="0 0 24 24"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
  </button>
  <span class="mob-title">Dashboard PDM CVP for GN</span>
  <div class="mob-actions">
    <button type="button" class="mob-btn lang-btn" id="mob-lang-toggle" aria-label="Toggle English / Bahasa Indonesia" title="Switch to English / Beralih ke Bahasa Indonesia">
      <svg viewBox="0 0 24 24" style="width:18px;height:18px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
    </button>
    <button type="button" class="mob-btn" id="mob-theme-toggle" aria-label="Ganti Mode Gelap / Terang" title="Ganti Mode Gelap / Terang">
      <svg class="icon-moon" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
      <svg class="icon-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
    </button>
  </div>
</div>"""

assert mob_search in html, "Could not find mob_search"
html = html.replace(mob_search, mob_replace)

aside_search = """  <div class="aside-head">
    <button type="button" class="toggle-btn" id="menu-toggle" aria-label="Toggle Sidebar" title="Buka / Sembunyikan Sidebar">
      <svg viewBox="0 0 24 24"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
    </button>
    <span class="aside-title">Menu Navigasi</span>
    <button type="button" class="theme-btn" id="theme-toggle" aria-label="Ganti Mode Gelap / Terang" title="Ganti Mode Gelap / Terang">
      <svg class="icon-moon" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
      <svg class="icon-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
    </button>
  </div>"""

aside_replace = """  <div class="aside-head">
    <button type="button" class="toggle-btn" id="menu-toggle" aria-label="Toggle Sidebar" title="Buka / Sembunyikan Sidebar">
      <svg viewBox="0 0 24 24"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
    </button>
    <span class="aside-title">Menu Navigasi</span>
    <div class="aside-actions">
      <button type="button" class="lang-btn" id="lang-toggle" aria-label="Toggle English / Bahasa Indonesia" title="Switch to English / Beralih ke Bahasa Indonesia">
        <svg viewBox="0 0 24 24" style="width:16px;height:16px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
      </button>
      <button type="button" class="theme-btn" id="theme-toggle" aria-label="Ganti Mode Gelap / Terang" title="Ganti Mode Gelap / Terang">
        <svg class="icon-moon" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
        <svg class="icon-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
      </button>
    </div>
  </div>"""

assert aside_search in html, "Could not find aside_search"
html = html.replace(aside_search, aside_replace)

# 3. Update export and print button texts in HTML
fhead_search = """      <div class="fhead-actions">
        <button type="button" class="f-act-btn" id="btn-export-csv" title="Unduh data terfilter dalam format CSV">
          <svg viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          <span>Ekspor CSV</span>
        </button>
        <button type="button" class="f-act-btn" id="btn-print-pdf" title="Cetak atau Simpan sebagai PDF">
          <svg viewBox="0 0 24 24"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
          <span>Cetak PDF</span>
        </button>
        <button type="button" class="freset" id="f-reset" hidden>Bersihkan filter</button>
      </div>"""

fhead_replace = """      <div class="fhead-actions">
        <button type="button" class="f-act-btn" id="btn-export-csv" title="Unduh data terfilter dalam format CSV">
          <svg viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          <span id="btn-export-csv-txt">Ekspor CSV</span>
        </button>
        <button type="button" class="f-act-btn" id="btn-print-pdf" title="Cetak atau Simpan sebagai PDF">
          <svg viewBox="0 0 24 24"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
          <span id="btn-print-pdf-txt">Cetak PDF</span>
        </button>
        <button type="button" class="freset" id="f-reset" hidden>Bersihkan filter</button>
      </div>"""

assert fhead_search in html, "Could not find fhead_search"
html = html.replace(fhead_search, fhead_replace)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML template elements updated successfully!")
