import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Proposal 💖", layout="centered")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
  background: linear-gradient(135deg, #000000, #1a1a2e);
  color: white;
  font-family: 'Segoe UI', sans-serif;
  text-align: center;
  overflow: hidden;
}

.container {
  margin-top: 80px;
}

.question {
  font-size: 32px;
  margin-bottom: 40px;
}

.name {
  font-size: 36px;
  color: #ff4d6d;
  margin-bottom: 20px;
}

button {
  padding: 12px 30px;
  font-size: 18px;
  border: none;
  border-radius: 30px;
  cursor: pointer;
}

#yesBtn {
  background: #2ecc71;
  color: white;
  margin-right: 20px;
}

#noBtn {
  background: #e74c3c;
  color: white;
  position: absolute;
}

#message {
  font-size: 28px;
  margin-top: 40px;
}
</style>
</head>

<body>
  <div class="container">
    <div class="name">Vani ❤️</div>

    <div class="question">
      Will you be my Valentine? 🌹
    </div>

    <button id="yesBtn" onclick="yesClicked()">YES 💕</button>
    <button id="noBtn">NO 😅</button>

    <div id="message"></div>
  </div>

<script>
const noBtn = document.getElementById("noBtn");

function moveNoButton() {
  const maxX = window.innerWidth - noBtn.offsetWidth;
  const maxY = window.innerHeight - noBtn.offsetHeight;

  const x = Math.random() * maxX;
  const y = Math.random() * maxY;

  noBtn.style.left = x + "px";
  noBtn.style.top = y + "px";
}

noBtn.addEventListener("mouseenter", moveNoButton);

function yesClicked() {
  document.body.innerHTML = `
    <div style="margin-top:120px; font-size:34px; color:white;">
      Vani ❤️ 😍<br><br>
      Naku telusu nuv YES antav ani 😌<br><br>
      From today… you are my Valentine 🌹💍
    </div>
  `;
}
</script>
</body>
</html>
"""

components.html(html_code, height=520)
