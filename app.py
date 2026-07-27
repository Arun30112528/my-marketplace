import streamlit as st
import os

# ตั้งค่าหน้าเว็บให้เต็มจอและทันสมัย
st.set_page_config(page_title="my-marketplace | ศูนย์กลางโซเชียล & อีคอมเมิร์ซทั่วไทย", page_icon="🌐", layout="wide")

# ---------------------------------------------------------
# 🎨 Custom CSS แต่งหน้าเว็บให้ดูพรีเมียม สไตล์ Social & E-Commerce
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
    .social-card {
        background-color: #ffffff;
        border: 1px solid #e4e6eb;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .shopping-card {
        background-color: #fff8f6;
        border: 1px solid #ff5722;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    .highlight-box {
        background-color: #e7f3ff;
        border-left: 5px solid #1877f2;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ส่วนหัวหลักของเว็บ
st.markdown("""
    <div class="main-header">
        <h1>🌐 my-marketplace - ศูนย์กลางเชื่อมโยงโซเชียล & อีคอมเมิร์ซทั่วไทย</h1>
        <p>เชื่อมต่อบ้านเช่า ซื้อ-ขายอสังหาฯ กับ Facebook, YouTube, TikTok และร้านค้าออนไลน์ชั้นนำ ปลอดภัยด้วยระบบ Escrow</p>
    </div>
""", unsafe_allow_html=True)

# เมนูหลักของเว็บไซต์
tabs = st.tabs([
    "🏠 ค้นหาบ้านเช่า / บ้านมือสอง (ทั่วไทย)",
    "🌐 เชื่อมโยงโซเชียล & ร้านค้าออนไลน์",
    "📰 ฟีดชุมชน (Facebook Style)",
    "🔴 วิดีโอรีวิว (YouTube Style)",
    "📱 คลิปสั้นรีวิวบ้าน (TikTok Style)",
    "🛒 ตลาดสินค้าออนไลน์ (Shopee/Lazada Style)",
    "🛡️ ชำระเงินผ่านระบบกลาง (Escrow)",
    "➕ ลงประกาศใหม่ (ระบุพิกัดทั่วไทย)", 
    "🚗 ธุรกรรม & จัดไฟแนนซ์",
    "🚘 คำนวณค่างวดผ่อนรถ",
    "🏦 เช็กวงเงินกู้บ้าน",
    "💳 ชำระเงินค่าบริการแอดมิน", 
    "📞 ติดต่อ / ร้องเรียน",
    "⚙️ แอดมิน"
])

provinces_thailand = [
    "--- ทุกจังหวัดทั่วไทย ---",
    "กรุงเทพมหานคร", "ปทุมธานี", "นนทบุรี", "สมุทรปราการ", "สมุทรสาคร", "นครปฐม",
    "เชียงใหม่", "เชียงราย", "ขอนแก่น", "นครราชสีมา", "อุบลราชธานี", "อุดรธานี",
    "ชลบุรี", "ระยอง", "ภูเก็ต", "สงขลา", "สุราษฎร์ธานี", "พระนครศรีอยุธยา"
]

# =========================================================
# TAB 0: ค้นหาบ้านเช่า / บ้านมือสอง (ทั่วไทย)
# =========================================================
with tabs[0]:
    st.subheader("📍 ระบบค้นหาอสังหาฯ และบ้านเช่าแม่นยำทั่วประเทศไทย")
    
    with st.container():
        st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
        col_loc1, col_loc2, col_loc3 = st.columns(3)
        with col_loc1:
            selected_province = st.selectbox("📍 เลือกจังหวัดที่ต้องการหาที่พัก", provinces_thailand)
        with col_loc2:
            property_type = st.selectbox("🏠 ประเภทอสังหาริมทรัพย์", ["ทั้งหมด", "บ้านเช่า / หอพัก", "บ้านเดี่ยว / ทาวน์โฮม", "คอนโดมิเนียม", "ที่ดิน"])
        with col_loc3:
            price_range = st.selectbox("💰 ช่วงราคา / ค่าเช่า", ["ทั้งหมด", "ต่ำกว่า 5,000 บาท/เดือน", "5,000 - 10,000 บาท/เดือน", "10,000 - 20,000 บาท/เดือน", "20,000 บาทขึ้นไป"])
        st.markdown('</div>', unsafe_allow_html=True)

    st.subheader(f"📌 ผลการค้นหาในพื้นที่: {selected_province}")

    all_listings = [
        {"title": "🏠 ทาวน์โฮมให้เช่า ทำเลใกล้แหล่งงาน", "province": "ปทุมธานี", "price": "6,500 บาท/เดือน", "type": "บ้านเช่า / หอพัก", "desc": "พร้อมเข้าอยู่ เดินทางสะดวก ปลอดภัย", "seller": "คุณอรัญ"},
        {"title": "🏢 คอนโดมิเนียมวิวสวย ใจกลางเมือง", "province": "กรุงเทพมหานคร", "price": "12,000 บาท/เดือน", "type": "คอนโดมิเนียม", "desc": "แต่งครบพร้อมกระเป๋าใบเดียว", "seller": "คุณสมชาย"},
        {"title": "🏡 บ้านเดี่ยวสองชั้น บรรยากาศธรรมชาติ", "province": "เชียงใหม่", "price": "15,000 บาท/เดือน", "type": "บ้านเดี่ยว / ทาวน์โฮม", "desc": "วิวภูเขา อากาศดี เหมาะแก่การพักผ่อน", "seller": "คุณA"}
    ]

    filtered = [item for item in all_listings if (selected_province == "--- ทุกจังหวัดทั่วไทย ---" or item["province"] == selected_province) and (property_type == "ทั้งหมด" or item["type"] == property_type)]

    for item in filtered:
        with st.container():
            st.markdown(f"### {item['title']}")
            st.markdown(f"**ค่าเช่า/ราคา:** {item['price']} | **ประเภท:** {item['type']}")
            st.write(item['desc'])
            st.caption(f"📍 จังหวัด: {item['province']} | ผู้ลงประกาศ: {item['seller']}")
            st.button("📞 ติดต่อผู้ลงประกาศ", key=f"btn_{item['title']}")
            st.divider()

# =========================================================
# TAB 1: เชื่อมโยงโซเชียล & ร้านค้าออนไลน์
# =========================================================
with tabs[1]:
    st.subheader("🌐 ศูนย์รวมลิงก์เชื่อมโยง (Social & E-Commerce Integration)")
    st.write("เข้าถึงช่องทางทางการของเราบนแพลตฟอร์มภายนอกได้อย่างรวดเร็ว")

    col_s1, col_s2, col_s3, col_s4 = st.columns(4)
    with col_s1:
        st.markdown('<div class="social-card">', unsafe_allow_html=True)
        st.markdown("### 📘 Facebook")
        st.write("ติดตามเพจหลัก แชร์ประกาศ และพูดคุยในกลุ่มชุมชน")
        st.markdown("[🔗 ไปที่ Facebook Page](https://www.facebook.com)", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col_s2:
        st.markdown('<div class="social-card">', unsafe_allow_html=True)
        st.markdown("### 🔴 YouTube")
        st.write("รับชมวิดีโอรีวิวบ้านเช่า ทัวร์โครงการ และไลฟ์สตรีม")
        st.markdown("[🔗 ไปที่ YouTube Channel](https://www.youtube.com)", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col_s3:
        st.markdown('<div class="social-card">', unsafe_allow_html=True)
        st.markdown("### 📱 TikTok")
        st.write("รับชมคลิปสั้นรีวิวห้องพัก บรรยากาศจริงแบบรวดเร็วทันใจ")
        st.markdown("[🔗 ไปที่ TikTok Profile](https://www.tiktok.com)", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col_s4:
        st.markdown('<div class="social-card">', unsafe_allow_html=True)
        st.markdown("### 🛍️ Shopee / Lazada")
        st.write("เลือกซื้อสินค้าตกแต่งบ้าน อุปกรณ์ไอที และของใช้จำเป็น")
        st.markdown("[🔗 ไปที่ Shopee Store](https://shopee.co.th)", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# TAB 2: ฟีดชุมชน (Facebook Style)
# =========================================================
with tabs[2]:
    st.subheader("📰 ฟีดข่าวสาร & ชุมชนออนไลน์ (Facebook Style)")
    with st.container():
        st.markdown('<div class="social-card">', unsafe_allow_html=True)
        with st.form("fb_post_form", clear_on_submit=True):
            st.text_input("ชื่อของคุณ / จังหวัด")
            st.text_area("แชร์เรื่องราวหรือประกาศหาบ้าน...")
            if st.form_submit_button("📤 โพสต์ลงฟีด"):
                st.success("🎉 โพสต์เรียบร้อยแล้ว!")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="social-card"><strong>👤 คุณอรัญ (ปทุมธานี):</strong><p>ยินดีต้อนรับทุกท่านสู่แพลตฟอร์มเชื่อมโยงทั่วไทยครับ 😊</p></div>', unsafe_allow_html=True)

# =========================================================
# TAB 3: วิดีโอรีวิว (YouTube Style)
# =========================================================
with tabs[3]:
    st.subheader("🔴 วิดีโอรีวิวบ้านเช่า & โครงการ (YouTube Style)")
    col_v1, col_v2 = st.columns(2)
    with col_v1:
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    with col_v2:
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# =========================================================
# TAB 4: คลิปสั้นรีวิวบ้าน (TikTok Style)
# =========================================================
with tabs[4]:
    st.subheader("📱 คลิปสั้นรีวิวบ้านด่วน (TikTok Style Reels)")
    col_t1, col_t2, col_t3 = st.columns(3)
    with col_t1:
        st.info("🔥 **Reel #1:** คอนโดแต่งครบ 4,500 บ.")
    with col_t2:
        st.info("✨ **Reel #2:** ทาวน์โฮมรีโนเวทใหม่")
    with col_t3:
        st.info("🏡 **Reel #3:** บ้านเดี่ยวเชียงใหม่")

# =========================================================
# TAB 5: ตลาดสินค้าออนไลน์ (Shopee/Lazada Style)
# =========================================================
with tabs[5]:
    st.subheader("🛒 ตลาดสินค้าตกแต่งบ้าน & ของใช้ (Shopee / Lazada Style)")
    st.write("เลือกซื้ออุปกรณ์เสริมสำหรับบ้านใหม่ เฟอร์นิเจอร์ และเครื่องใช้ไฟฟ้าส่งตรงถึงบ้าน")
    
    col_p1, col_p2, col_p3 = st.columns(3)
    with col_p1:
        st.markdown('<div class="shopping-card">', unsafe_allow_html=True)
        st.markdown("#### 🛏️ ชุดเครื่องนอนครบชุดเกรดพรีเมียม")
        st.markdown("**ราคา:** 590 บาท ⭐ 4.8 (1.2K ขายแล้ว)")
        st.markdown("[🛒 สั่งซื้อผ่าน Shopee/Lazada](https://shopee.co.th)", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col_p2:
        st.markdown('<div class="shopping-card">', unsafe_allow_html=True)
        st.markdown("#### 🪑 โต๊ะทำงานพับได้มินิมอล")
        st.markdown("**ราคา:** 450 บาท ⭐ 4.9 (3.5K ขายแล้ว)")
        st.markdown("[🛒 สั่งซื้อผ่าน Shopee/Lazada](https://shopee.co.th)", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col_p3:
        st.markdown('<div class="shopping-card">', unsafe_allow_html=True)
        st.markdown("#### 💡 หลอดไฟอัจฉริยะควบคุมผ่านมือถือ")
        st.markdown("**ราคา:** 199 บาท ⭐ 4.7 (890 ขายแล้ว)")
        st.markdown("[🛒 สั่งซื้อผ่าน Shopee/Lazada](https://shopee.co.th)", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# TAB อื่นๆ คงระบบเดิมครบถ้วน
# =========================================================
with tabs[6]:
    st.subheader("🛡️ ระบบชำระเงินปลอดภัยผ่านคนกลาง (Escrow)")
with tabs[7]:
    st.subheade
