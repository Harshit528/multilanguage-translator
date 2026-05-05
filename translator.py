import streamlit as st
from deep_translator import GoogleTranslator

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="Multilanguage Translator",
    page_icon="🌐",
    layout="centered"
)

# ── Supported languages ───────────────────────────────────────
LANGUAGES = {
    "English":    "en",
    "Hindi":      "hi",
    "Japanese":   "ja",
    "Chinese":    "zh-CN",
    "Spanish":    "es",
    "French":     "fr",
    "Arabic":     "ar",
    "German":     "de",
    "Korean":     "ko",
    "Portuguese": "pt",
    "Russian":    "ru",
    "Italian":    "it",
}

# ── UI ────────────────────────────────────────────────────────
st.title("🌐 Multilanguage Translator")
st.markdown("Type any text and translate it instantly into any language.")
st.divider()

# Input text
input_text = st.text_area(
    "✏️ Enter text to translate",
    placeholder="Type something here...",
    height=150
)

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "🔤 Source language",
        options=["Auto Detect"] + list(LANGUAGES.keys()),
        index=0
    )

with col2:
    target_lang = st.selectbox(
        "🎯 Translate to",
        options=list(LANGUAGES.keys()),
        index=1   # Hindi by default
    )

st.divider()

# Translate button
if st.button("🚀 Translate", use_container_width=True, type="primary"):
    if not input_text.strip():
        st.warning("⚠️ Please enter some text first.")
    else:
        try:
            src = "auto" if source_lang == "Auto Detect" else LANGUAGES[source_lang]
            tgt = LANGUAGES[target_lang]

            translated = GoogleTranslator(source=src, target=tgt).translate(input_text)

            st.success("✅ Translation complete!")
            st.subheader(f"📝 Result — {target_lang}")
            st.text_area(
                label="",
                value=translated,
                height=150,
                key="output"
            )

            # Copy hint
            st.caption("💡 Click inside the box above and press Ctrl+A → Ctrl+C to copy.")

        except Exception as e:
            st.error(f"❌ Translation failed: {e}")
            st.info("Make sure you have an internet connection.")

# ── Bulk translate section ────────────────────────────────────
st.divider()
with st.expander("🌍 Translate to ALL languages at once"):
    if st.button("Translate to all languages", use_container_width=True):
        if not input_text.strip():
            st.warning("⚠️ Please enter some text first.")
        else:
            st.subheader("Translations")
            for lang_name, lang_code in LANGUAGES.items():
                try:
                    result = GoogleTranslator(source="auto", target=lang_code).translate(input_text)
                    st.markdown(f"**{lang_name}:** {result}")
                except:
                    st.markdown(f"**{lang_name}:** _(failed)_")

# ── Footer ────────────────────────────────────────────────────
st.divider()
st.caption("Built with Streamlit + Google Translate API · Internship Project 🎓")
