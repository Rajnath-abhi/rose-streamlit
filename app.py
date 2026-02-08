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
