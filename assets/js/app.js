/* Young Docents of the Southern Branch — shared interactions
   1) 🔊 Speak buttons: read English text aloud via the Web Speech API.
   2) Quiz: tap an option, see right/wrong + an explanation. English options only. */

(function () {
  "use strict";

  /* ---------- 🔊 Pronunciation (Web Speech API) ---------- */
  var synth = window.speechSynthesis || null;
  var current = null;

  function pickVoice() {
    if (!synth) return null;
    var voices = synth.getVoices() || [];
    // Prefer a natural en-US/en-GB voice.
    var pref = voices.filter(function (v) { return /^en(-|_)?(US|GB)?/i.test(v.lang); });
    return pref[0] || voices[0] || null;
  }

  function speak(btn) {
    if (!synth) return;
    var text = btn.getAttribute("data-speak");
    if (!text) return;
    // Toggle off if this button is mid-speech.
    if (current === btn && synth.speaking) {
      synth.cancel();
      clearPlaying();
      return;
    }
    synth.cancel();
    clearPlaying();
    var u = new SpeechSynthesisUtterance(text);
    u.lang = "en-US";
    u.rate = 0.92;
    u.pitch = 1.0;
    var v = pickVoice();
    if (v) u.voice = v;
    u.onend = clearPlaying;
    u.onerror = clearPlaying;
    current = btn;
    btn.classList.add("is-playing");
    synth.speak(u);
  }

  function clearPlaying() {
    document.querySelectorAll(".speak.is-playing").forEach(function (b) {
      b.classList.remove("is-playing");
    });
    current = null;
  }

  document.addEventListener("click", function (e) {
    var btn = e.target.closest(".speak");
    if (btn) { e.preventDefault(); speak(btn); }
  });

  // Some browsers load voices asynchronously.
  if (synth && typeof synth.onvoiceschanged !== "undefined") {
    synth.onvoiceschanged = pickVoice;
  }
  // If speech is unsupported, hide the buttons rather than show dead controls.
  if (!synth) {
    document.querySelectorAll(".speak").forEach(function (b) { b.style.display = "none"; });
  }

  /* ---------- Quiz ---------- */
  document.querySelectorAll(".q-item").forEach(function (item) {
    var opts = item.querySelectorAll(".q-opt");
    var explain = item.querySelector(".q-explain");
    var answered = false;
    opts.forEach(function (opt) {
      opt.addEventListener("click", function () {
        if (answered) return;
        answered = true;
        var isCorrect = opt.getAttribute("data-correct") === "true";
        opt.classList.add(isCorrect ? "correct" : "wrong");
        var mark = document.createElement("span");
        mark.className = "mark";
        mark.textContent = isCorrect ? "✓ " : "✗ ";
        opt.prepend(mark);
        if (!isCorrect) {
          // Also reveal the correct option.
          opts.forEach(function (o) {
            if (o.getAttribute("data-correct") === "true") {
              o.classList.add("correct");
              var m = document.createElement("span");
              m.className = "mark";
              m.textContent = "✓ ";
              o.prepend(m);
            }
          });
        }
        opts.forEach(function (o) { o.classList.add("locked"); });
        if (explain) explain.classList.add("show");
      });
    });
  });
})();
