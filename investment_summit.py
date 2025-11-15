import streamlit as st

# -----------------------------
# تنظیمات صفحه (باید اول باشد)
# -----------------------------
st.set_page_config(
    page_title="Investment Summit - Health Science and Technology Park",
    layout="centered"
)

# -----------------------------
# اضافه کردن پس‌زمینه و شفافیت Accordion
# -----------------------------
page_bg_img = """
<style>
.stApp {
    background-image: url("parkenter.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* شفافیت Accordion ها */
div.stExpander {
    background: rgba(255, 255, 255, 0.8); /* سفید شفاف */
    border-radius: 10px;
    padding: 10px;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# -----------------------------
# نمایش تصویر بالای صفحه
# -----------------------------
st.image("Picture1.png", use_column_width=True)

# -----------------------------
# تعریف داده‌ها
# -----------------------------
stages = [
    # … داده‌های شما
]

# -----------------------------
# رابط کاربری Accordion
# -----------------------------
st.markdown("### Pipeline")

for stage in stages:
    with st.expander(f"🔹 {stage['title_en']} "):
        st.markdown(f"<div dir='rtl'><b>📅 تاریخ:</b> {stage['date']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div dir='rtl'><b>🎯 هدف:</b> {stage['goal']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div dir='rtl'><b>📄 خروجی:</b> {stage['output']}</div>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)

# نمایش لوگو در انتهای صفحه
st.image("logo-removebg-preview.png", use_column_width=True)
