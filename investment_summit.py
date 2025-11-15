# فایل: summit_schedule_app.py
import streamlit as st

# -----------------------------
# تنظیمات صفحه
# -----------------------------
st.set_page_config(
    page_title="Investment Summit - Health Science and Technology Park",
    layout="centered"
)

# -----------------------------

st.markdown(page_bg_img, unsafe_allow_html=True)

# -----------------------------
# نمایش تصویر بالای صفحه
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
    {
        "id": "Registration",
        "title_fa": "ثبت‌نام و بارگذاری فایل PSF",
        "title_en": "Registration",
        "date": "15-20 آذر",
        "goal": "دریافت ایده‌ها و Pre-Feasibility Study تیم‌ها",
        "output": "بانک داده ایده یا محصول اولیه به همراه PSF"
    },
    {
        "id": "Evaluation",
        "title_fa": "داوری اولیه (Evaluation Committee)",
        "title_en": "Initial Evaluation",
        "date": "22-26 آذر",
        "goal": "غربالگری ایده‌ها و انتخاب تیم‌های برگزیده برای Bootcamp",
        "output": "فهرست تیم‌های پذیرفته‌شده برای Bootcamp"
    },
    {
        "id": "Kickoff",
        "title_fa": "Kick-Off Meeting",
        "title_en": "Kick-Off Meeting",
        "date": "27 آذر",
        "goal": "معرفی اهداف Summit و جدول زمان‌بندی؛ شبکه‌سازی اولیه",
        "output": "درک مشترک فرآیند و ایجاد شبکه ارتباطی"
    },
    {
        "id": "Bootcamp",
        "title_fa": "Bootcamp 4 روزه",
        "title_en": "4-Day Bootcamp",
        "date": "29 آذر الی 2 دی",
        "goal": """ 
روز اول: امکان سنجی از نظر فنی (برآورد هزینه)
روز دوم: امکان سنجی از نظر بازار (برآورد فروش)
روز سوم: امکان سنجی از نظر مالی (ارزیابی اقتصادی طبق داده های بدست آمده از هزینه-فروش)
روز چهارم: نگارش Business Plan  """ ,
        "output":"Business Plan"
    },
    {
        "id": "Checkpoint",
        "title_fa": "جلسات Checkpoint / منتورینگ نهایی",
        "title_en": "Checkpoint & Final Mentorship",
        "date": "3-5 دی",
        "goal": "بازبینی، اصلاح Business Plan و آماده‌سازی Pitch",
        "output": "نسخه نهایی Business Plan و Pitch Deck"
    },
    {
        "id": "PitchNight",
        "title_fa": "Pitch Night",
        "title_en": "Pitch Night",
        "date": "10 دی",
        "goal": "ارائه تیم‌ها به هیئت داوران و سرمایه‌گذاران",
        "output": "انتخاب تیم‌های نهایی برای مرحله مذاکره سرمایه‌گذاری"
    },
    {
        "id": "FinalNight",
        "title_fa": "Final Night",
        "title_en": "Final Night",
        "date": "25 دی",
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
# رابط کاربری Accordion
# -----------------------------
st.markdown("### Pipeline")

for stage in stages:
    with st.expander(f"🔹 {stage['title_en']} "):
        st.markdown(f"<div dir='rtl'><b>📅 تاریخ:</b> {stage['date']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div dir='rtl'><b>🎯 هدف:</b> {stage['goal']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div dir='rtl'><b>📄 خروجی:</b> {stage['output']}</div>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------
# نمایش لوگو در انتهای صفحه
# -----------------------------
st.image("logo-removebg-preview.png", use_column_width=True)

