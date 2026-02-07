import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Valentine 💖", layout="centered")

st.markdown(
    """
    <h1 style="text-align:center;">Will you be my Valentine, puppy? 🐶❤️</h1>
    <br>
    """,
    unsafe_allow_html=True
)

html_code = """
<div style="text-align:center; position:relative; height:200px;">

  <button onclick="yesClicked()" 
          style="padding:12px 25px; font-size:18px; background:#ff4d6d; color:white; border:none; border-radius:8px; cursor:pointer;">
    YES 💕
  </button>

  <button id="noBtn"
          style="padding:12px 25px; font-size:18px; margin-left:20px; position:absolute; background:#ccc; border:none; border-radius:8px; cursor:pointer;">
    NO 🙈
  </button>

</div>

<script>
  const noBtn = document.getElementById("noBtn");

  noBtn.addEventListener("mouseover", () => {
    const x = Math.random() * 200 - 100;
    const y = Math.random() * 100 - 50;
    noBtn.style.transform = `translate(${x}px, ${y}px)`;
  });

  function yesClicked() {
    document.body.innerHTML = `
      <h1 style="text-align:center; margin-top:80px;">
        Yayyy! 🥰❤️<br><br>
        I knew it 🐶🌹
      </h1>
    `;
  }
</script>
"""

components.html(html_code, height=300)
