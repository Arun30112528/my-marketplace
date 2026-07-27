import streamlit as st
import os

# ตั้งค่าหน้าเว็บให้เต็มจอและทันสมัย
st.set_page_config(page_title="my-marketplace | ศูนย์กลางโซเชียล & ตลาดออนไลน์", page_icon="🚀", layout="wide")

# ---------------------------------------------------------
# 🎨 Custom CSS แต่งหน้าเว็บให้ดูพรีเมียม สไตล์ Facebook / YouTube
# ---------------------------------------------------------
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #1877f2 0%, #0c4a9e 100%);
        padding: 25px;
        border-radius: 12px;
        color: white;
        margin-bottom: 20px;
    }
    .feed-card {
        background-color: #ffffff;
        border: 1px solid #e4e6eb;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    .video-card {
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# ส่วนหัวหลักของเว็บ
st.markdown("""
    <div class="main-header">
        <h1>🚀 my-marketplace & Community Hub</h1>
        <p>แพลตฟอร์มซื้อ-ขายอสังหาฯ รถยนต์ และฟีดชุมชนออนไลน์สุดล้ำ ปลอดภัยด้วยระบบคนกลาง Escrow</p>
    </div>
""", unsafe_allow_html=True)

# เมนูหลักของเว็บไซต์
tabs = st.tabs([
    "📰 ฟีดชุมชน (Timeline)",
    "🔴 วิดีโอสตรีมมิ่ง (YouTube Style)",
    "🔍 ค้นหาประกาศทั้งหมด", 
    "🛡️ ชำระเงินผ่านระบบกลาง (Escrow)",
    "➕ ลงประกาศใหม่ (ฟรี)", 
    "🚗 ธุรกรรม & จัดไฟแนนซ์",
    "🚘 คำนวณค่างวดผ่อนรถ",
    "🏦 เช็กวงเงินกู้บ้าน",
    "🎁 กิจกรรม & ส่วนลด",
    "💳 ชำระเงินค่าบริการแอดมิน", 
    "📞 ติดต่อ / ร้องเรียน",
    "⚙️ แอดมิน"
])

# =========================================================
# TAB 0: ฟีดไทม์ไลน์ (News Feed สไตล์ Facebook)
# =========================================================
with tabs[0]:
    col_f_left, col_f_right = st.columns([2, 1])
    
    with col_f_left:
        st.subheader("📰 ฟีดข่าวสาร & ชุมชนออนไลน์")
        
        # กล่องสร้างโพสต์สไตล์ Facebook
        with st.container():
            st.markdown('<div class="feed-card">', unsafe_allow_html=True)
            st.markdown("##### ✍️ สร้างโพสต์ใหม่ถึงเพื่อนๆ ในชุมชน")
            with st.form("fb_post_form", clear_on_submit=True):
                p_name = st.text_input("ชื่อผู้โพสต์ / ร้านค้าของคุณ")
                p_text = st.text_area("คุณกำลังคิดอะไรอยู่ หรือมีสินค้าอะไรอยากแชร์ไหม?")
                p_submit = st.form_submit_button("📤 โพสต์ทันที")
                if p_submit:
                    if p_name and p_text:
                        st.success("🎉 โพสต์ของคุณถูกแชร์ลงฟีดเรียบร้อยแล้ว!")
                    else:
                        st.warning("⚠️ กรุณากรอกข้อมูลให้ครบถ้วนก่อนโพสต์")
            st.markdown('</div>', unsafe_allow_html=True)

        # รายการโพสต์ในฟีด
        posts = [
            {"user": "คุณอรัญ (Fresh Food Manager)", "time": "25 นาทีที่แล้ว", "text": "สวัสดีครับทุกคน วันนี้ระบบฟีดใหม่ดีไซน์สวยและใช้งานง่ายมากๆ ใครสนใจซื้อขายบ้านหรือรถยนต์มือสองโพสต์พูดคุยกันได้เลยครับ! 🚗🏡"},
            {"user": "คุณสมชาย รถบ้านมือสอง", "time": "2 ชั่วโมงที่แล้ว", "text": "อัปเดตสต็อกรถยนต์เข้าใหม่วันนี้ Yaris และ Civic ฟรีดาวน์ทุกคัน สนใจทักแชทสอบถามรายละเอียดได้เลยครับ"},
            {"user": "คุณนภา ชุมชนปทุมธานี", "time": "5 ชั่วโมงที่แล้ว", "text": "ระบบคนกลาง Escrow ของเว็บนี้ปลอดภัยดีมากค่ะ เพิ่งลองใช้ซื้อขายสินค้าไปเมื่อวาน สะดวกและมั่นใจสุดๆ 👍"}
        ]

        for post in posts:
            st.markdown(f'''
                <div class="feed-card">
                    <strong>👤 {post['user']}</strong> &nbsp;&nbsp; <span style="color:gray; font-size:12px;">{post['time']}</span>
                    <p style="margin-top: 10px; font-size: 15px;">{post['text']}</p>
                </div>
            ''', unsafe_allow_html=True)

    with col_f_right:
        st.markdown("### 🔥 ข่าวสารยอดฮิต")
        st.info("📌 **ประกาศจากแอดมิน:** ระบบชำระเงินผ่านคนกลาง (Escrow) เปิดให้บริการเต็มรูปแบบแล้ว ปลอดภัย 100%")
        st.success("🌟 **สมาชิกแนะนำ:** คุณอรัญ (Verified Seller ระดับพรีเมียม)")

# =========================================================
# TAB 1: วิดีโอสตรีมมิ่ง (สไตล์ YouTube)
# =========================================================
with tabs[1]:
    st.subheader("🔴 วิดีโอรีวิวสินค้า & ไลฟ์สตรีมมิ่ง (YouTube Style)")
    st.write("รับชมวิดีโอแนะนำรถยนต์ บ้านจัดสรร และรีวิวสินค้ามือสองจากผู้ขายโดยตรง")
    
    col_v1, col_v2 = st.columns(2)
    
    with col_v1:
        st.markdown('<div class="video-card">', unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        st.markdown("##### 🚗 รีวิวรถยนต์ Nissan Almera มือสอง สภาพป้ายแดง")
        st.caption("ช่อง: Car Review Thailand | ผู้เข้าชม 1.2K ครั้ง")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_v2:
        st.markdown('<div class="video-card">', unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        st.markdown("##### 🏠 พาชมบ้านเดี่ยวโซนปทุมธานี ใกล้โลตัส พร้อมเข้าอยู่")
        st.caption("ช่อง: Real Estate Live | ผู้เข้าชม 3.4K ครั้ง")
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# TAB 2: ค้นหาประกาศทั้งหมด
# =========================================================
with tabs[2]:
    st.subheader("🔍 ค้นหาบ้าน คอนโด รถยนต์ และสินค้ามือสอง")
    search_query = st.text_input("🔍 พิมพ์ค้นหาสินค้าที่ต้องการ...")
    
    st.divider()
    col_item1, col_item2 = st.columns(2)
    with col_item1:
        st.markdown("### 🚗 **Toyota Yaris Ativ 1.2 E ปี 2020**")
        st.markdown("**ราคา:** 359,000 บาท (ฟรีดาวน์)")
        st.write("รถบ้านสภาพสวย เลขไมล์ 45,000 กม. ตรวจเช็กเล่มเรียบร้อย")
        st.caption("📍 พิกัด: ปทุมธานี | ผู้ขาย: คุณสมชาย (Verified)")
        st.button("📞 ติดต่อผู้ขาย", key="c1")
    with col_item2:
        st.markdown("### 🏠 **บ้านเดี่ยว 2 ชั้น หมู่บ้านภัทรินทร์**")
        st.markdown("**ราคา:** 3,490,000 บาท (กู้ได้ 100%)")
        st.write("เนื้อที่ 52 ตร.วา บรรยากาศร่มรื่น ใกล้โลตัสปทุมธานี")
        st.caption("📍 พิกัด: ปทุมธานี | ผู้ขาย: คุณอรัญ (Verified)")
        st.button("📞 ติดต่อผู้ขาย", key="c2")

# =========================================================
# TAB อื่นๆ คงระบบเดิมครบถ้วน
# =========================================================
with tabs[3]:
    st.subheader("🛡️ ระบบชำระเงินปลอดภัยผ่านคนกลาง (Escrow)")
    st.info("สถานะ: รอผู้ซื้อโอนเงินเข้าบัญชีกลาง ➔ รอผู้ขายจัดส่ง ➔ กดยืนยันรับสินค้า")
with tabs[4]:
    st.subheader("➕ ลงประกาศฟรี")
    st.text_input("หัวข้อประกาศของคุณ")
with tabs[5]:
    st.subheader("🚗 ธุรกรรม & จัดไฟแนนซ์รถยนต์")
with tabs[6]:
    st.subheader("🚘 คำนวณค่างวดผ่อนรถ")
with tabs[7]:
    st.subheader("🏦 เช็กวงเงินกู้บ้าน")
with tabs[8]:
    st.subheader("🎁 กิจกรรม & ส่วนลด")
with tabs[9]:
    st.subheader("💳 ชำระเงินค่าบริการแอดมิน")
with tabs[10]:
    st.subheader("📞 ติดต่อ / เรื่องร้องเรียน")
with tabs[11]:
    st.subheader("⚙️ สำหรับแอดมิน")
    if st.text_input("รหัสผ่านแอดมิน", type="password") == "1234":
        st.success("เข้าสู่ระบบแอดมินสำเร็จ")
