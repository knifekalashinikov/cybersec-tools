javascript-tools/input_sanitizer.js
// input_sanitizer.js
// Simple input sanitizer for HTML display (educational).
// Use this function before inserting user-provided text into innerHTML.

function sanitizeForHTML(input) {
  if (input === null || input === undefined) return "";
  return String(input)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

// Example usage:
// const safe = sanitizeForHTML(userInput);
// document.getElementById('output').innerHTML = safe;

if (typeof module !== "undefined") {
  module.exports = { sanitizeForHTML };
}

javascript-tools/demo_sanitizer.html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Input Sanitizer Demo</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body>
  <h1>Input Sanitizer Demo (Educational)</h1>

  <label for="user-input">Type something (try HTML tags):</label><br/>
  <input id="user-input" type="text" style="width:80%" />
  <button id="show-btn">Show (sanitized)</button>

  <h2>Output (sanitized):</h2>
  <div id="output" style="white-space:pre-wrap; border:1px solid #ccc; padding:10px;"></div>

  <script src="input_sanitizer.js"></script>
  <script>
    // assumes input_sanitizer.js is in same folder
    const btn = document.getElementById('show-btn');
    const inp = document.getElementById('user-input');
    const out = document.getElementById('output');

    function sanitizeForHTML(input) {
      if (input === null || input === undefined) return "";
      return String(input)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
    }

    btn.addEventListener('click', () => {
      const text = inp.value;
      out.innerHTML = sanitizeForHTML(text);
    });
  </script>
</body>
</html>

