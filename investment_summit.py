# فایل: summit_schedule_app.py
import streamlit as st

# -----------------------------
# تنظیمات صفحه (باید اول باشد)
# -----------------------------
st.set_page_config(
    page_title="Investment Summit - Health Science and Technology Park",
    layout="centered"
)

# -----------------------------
# اضافه کردن پس‌زمینه
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
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# -----------------------------
# نمایش تصویر اصلی در بالای صفحه
# -----------------------------
st.image("Picture1.png", use_column_width=True)

# -----------------------------
# تعریف داده‌ها
# -----------------------------
stages = [
    {
        "id": "Pre-Feasibility Study Workshop",
        "title_fa": "کارگاه Pre-Feasibility Study",
        "title_en": "Pre-Feasibility Study Workshop",
        "date": "8-13آذر",
        "goal": "آموزش تیم‌ها برای نوشتن Pre-Feasibility Study استاندارد",
        "output": "سند اولیه Pre-Feasibility Study"
    },
    # … بقیه داده‌ها مانند قبل
]

# -----------------------------
# رابط کاربری تعاملی (Accordion style)
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
