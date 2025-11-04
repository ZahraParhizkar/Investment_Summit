# فایل: summit_schedule_app.py

import streamlit as st

# -----------------------------
# عنوان اپلیکیشن
# -----------------------------
st.set_page_config(page_title="Investment Summit - Life Sciences", layout="centered")
st.title("🧭 Investment Summit – Life Sciences Roadmap")

# -----------------------------
# تعریف داده‌ها (هر مرحله به همراه نام انگلیسی)
# -----------------------------
stages = [
    {
        "id": "PFS_Workshop",
        "title_fa": "کارگاه Pre-Feasibility Study",
        "title_en": "PFS Workshop",
        "date": "۱۰–۱۴ آذر",
        "goal": "آموزش تیم‌ها برای نوشتن Pre-Feasibility Study استاندارد",
        "output": "سند اولیه Pre-Feasibility Study"
    },
    {
        "id": "Registration",
        "title_fa": "ثبت‌نام و بارگذاری فایل PSF",
        "title_en": "Idea Registration & Upload",
        "date": "۱۵–۲۰ آذر",
        "goal": "دریافت ایده‌ها و Pre-Feasibility Study تیم‌ها",
        "output": "بانک داده ایده یا محصول اولیه به همراه PSF"
    },
    {
        "id": "Kickoff",
        "title_fa": "Kick-Off Meeting",
        "title_en": "Kick-Off Meeting",
        "date": "۲۲ آذر",
        "goal": "معرفی اهداف Summit و جدول زمان‌بندی؛ شبکه‌سازی اولیه",
        "output": "درک مشترک فرآیند و ایجاد شبکه ارتباطی"
    },
    {
        "id": "Evaluation",
        "title_fa": "داوری اولیه (Evaluation Committee)",
        "title_en": "Initial Evaluation",
        "date": "۲۳–۲۷ آذر",
        "goal": "غربالگری ایده‌ها و انتخاب تیم‌های برگزیده برای Bootcamp",
        "output": "فهرست تیم‌های پذیرفته‌شده برای Bootcamp"
    },
    {
        "id": "Bootcamp",
        "title_fa": "Bootcamp ۴ روزه",
        "title_en": "4-Day Bootcamp",
        "date": "۲۹ آذر الی ۲ دی",
        "goal": "آموزش و آماده‌سازی تیم‌ها برای Pitch و نوشتن BP",
        "output": """روز ۱: Technical Brief / TRL  
روز ۲: Market Summary + Sales Estimate  
روز ۳: Financial Model اولیه  
روز ۴: نسخه اولیه Business Plan + Pitch Summary"""
    },
    {
        "id": "Checkpoint",
        "title_fa": "جلسات Checkpoint / منتورینگ نهایی",
        "title_en": "Checkpoint & Final Mentorship",
        "date": "۳–۵ دی",
        "goal": "بازبینی، اصلاح Business Plan و آماده‌سازی Pitch",
        "output": "نسخه نهایی Business Plan و Pitch Deck"
    },
    {
        "id": "PitchNight",
        "title_fa": "Pitch Night",
        "title_en": "Pitch Night",
        "date": "۱۰ دی",
        "goal": "ارائه تیم‌ها به هیئت داوران و سرمایه‌گذاران",
        "output": "انتخاب تیم‌های نهایی برای مرحله مذاکره سرمایه‌گذاری"
    },
    {
        "id": "FinalNight",
        "title_fa": "Final Night",
        "title_en": "Final Night",
        "date": "۲۵ دی",
        "goal": "معرفی برگزیدگان و شبکه‌سازی میان تیم‌ها و سرمایه‌گذاران",
        "output": "تیم‌های منتخب و فرصتی برای مذاکرات اولیه"
    },
    {
        "id": "MOU",
        "title_fa": "انعقاد MOU",
        "title_en": "MOU Signing",
        "date": "هفته اول بهمن",
        "goal": "رسمیت‌بخشیدن همکاری بین تیم‌ها و سرمایه‌گذاران",
        "output": "MOU امضا شده بین طرفین"
    }
]

# -----------------------------
# رابط کاربری تعاملی (Accordion style)
# -----------------------------
st.markdown("### 📅 مراحل و جزئیات")

for stage in stages:
    with st.expander(f"🔹 {stage['title_en']} "):
        st.markdown(f"<div dir='rtl'><b>📅 تاریخ:</b> {stage['date']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div dir='rtl'><b>🎯 هدف:</b> {stage['goal']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div dir='rtl'><b>📄 خروجی:</b> {stage['output']}</div>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("✅ طراحی شده توسط Streamlit – نسخه نمایشی برنامه زمان‌بندی سامیت")

