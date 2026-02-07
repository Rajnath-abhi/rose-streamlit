import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
body {
    background-color: #0e0e0e;
}

.rose {
    font-size: 120px;
    text-align: center;
    margin-top: 100px;
}

.petal {
    position: absolute;
    font-size: 24px;
    animation: fall 6s linear infinite;
}

@keyframes fall {
    0% {
        top: -10%;
        opacity: 1;
    }
    100% {
        top: 110%;
        opacity: 0;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="rose">🌹</div>

<div class="petal" style="left:20%;">🌸</div>
<div class="petal" style="left:40%; animation-delay:1s;">🌸</div>
<div class="petal" style="left:60%; animation-delay:2s;">🌸</div>
<div class="petal" style="left:80%; animation-delay:3s;">🌸</div>
""", unsafe_allow_html=True)
