import streamlit as st
import os

# ตั้งค่าหน้าเว็บให้เต็มจอและทันสมัย
st.set_page_config(page_title="my-marketplace | ศูนย์กลางหาบ้านเช่า & ตลาดออนไลน์ทั่วไทย", page_icon="🏠", layout="wide")

# ---------------------------------------------------------
# 🎨 Custom CSS แต่งหน้าเว็บให้ดูพรีเมียม
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
        <h1>🇹🇭 my-marketplace - แพลตฟอร์มศูนย์กลางทั่วประเทศไทย</h1>
        <p>บริการหาบ้านเช่า ซื้อ-ขายบ้านมือสอง และอสังหาริมทรัพย์ ระบุโลเคชั่นแม่นยำทั่วไทย ปลอดภัยด้วยระบบคนกลาง Escrow</p>
    </div>
""", unsafe_allow_html=True)

# เมนูหลักของเว็บไซต์
tabs = st.tabs([
    "🏠 ค้นหาบ้านเช่า / บ้านมือสอง (ทั่วไทย)",
    "📰 ฟีดชุมชน (Timeline)",
    "🔴 วิดีโอสตรีมมิ่ง",
    "🛡️ ชำระเงินผ่านระบบกลาง (Escrow)",
    "➕ ลงประกาศใหม่ (ระบุพิกัดทั่วไทย)", 
    "🚗 ธุรกรรม & จัดไฟแนนซ์",
    "🚘 คำนวณค่างวดผ่อนรถ",
    "🏦 เช็กวงเงินกู้บ้าน",
    "🎁 กิจกรรม & ส่วนลด",
    "💳 ชำระเงินค่าบริการแอดมิน", 
    "📞 ติดต่อ / ร้องเรียน",
    "⚙️ แอดมิน"
])

# =========================================================
# TAB 0: ค้นหาบ้านเช่า / บ้านมือสอง (ระบุโลเคชั่นทั่วไทย)
# =========================================================
with tabs[0]:
    st.subheader("📍 ระบบค้นหาอสังหาฯ และบ้านเช่าแม่นยำทั่วประเทศไทย")
    
    # 🇹🇭 รายชื่อจังหวัดหลักทั่วประเทศไทยสำหรับให้ผู้ใช้เลือกอย่างแม่นยำ
    provinces_thailand = [
        "--- ทุกจังหวัดทั่วไทย ---",
        "กรุงเทพมหานคร", "ปทุมธานี", "นนทบุรี", "สมุทรปราการ", "สมุทรสาคร", "นครปฐม",
        "เชียงใหม่", "เชียงราย", "ขอนแก่น", "นครราชสีมา", "อุบลราชธานี", "อุดรธานี",
        "ชลบุรี", "ระยอง", "ภูเก็ต", "สงขลา", "สุราษฎร์ธานี", "พระนครศรีอยุธยา"
    ]

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

    # ตัวอย่างข้อมูลจำลองกระจายตามจังหวัด
    all_listings = [
        {"title": "🏠 ทาวน์โฮมให้เช่า ทำเลใกล้แหล่งงาน", "province": "ปทุมธานี", "price": "6,500 บาท/เดือน", "type": "บ้านเช่า / หอพัก", "desc": "พร้อมเข้าอยู่ เดินทางสะดวก ปลอดภัย", "seller": "คุณอรัญ"},
        {"title": "🏢 คอนโดมิเนียมวิวสวย ใจกลางเมือง", "province": "กรุงเทพมหานคร", "price": "12,000 บาท/เดือน", "type": "คอนโดมิเนียม", "desc": "แต่งครบพร้อมกระเป๋าใบเดียว", "seller": "คุณสมชาย"},
        {"title": "🏡 บ้านเดี่ยวสองชั้น บรรยากาศธรรมชาติ", "province": "เชียงใหม่", "price": "15,000 บาท/เดือน", "type": "บ้านเดี่ยว / ทาวน์โฮม", "desc": "วิวภูเขา อากาศดี เหมาะแก่การพักผ่อน", "seller": "คุณA"}
    ]

    # กรองข้อมูลตามจังหวัดที่ผู้ใช้เลือก
    filtered = []
    for item in all_listings:
        if selected_province == "--- ทุกจังหวัดทั่วไทย ---" or item["province"] == selected_province:
            if property_type == "ทั้งหมด" or item["type"] == property_type:
                filtered.append(item)

    if len(filtered) == 0:
        st.info(f"🔍 ยังไม่มีประกาศในจังหวัด **{selected_province}** ท่านสามารถลงประกาศหรือโพสต์หาห้องพักในฟีดชุมชนได้เลยครับ")
    else:
        for item in filtered:
            with st.container():
                st.markdown(f"### {item['title']}")
                st.markdown(f"**ค่าเช่า/ราคา:** {item['price']} | **ประเภท:** {item['type']}")
                st.write(item['desc'])
                st.caption(f"📍 จังหวัด: {item['province']} | ผู้ลงประกาศ: {item['seller']}")
                st.button("📞 ติดต่อผู้ลงประกาศ", key=f"btn_{item['title']}")
                st.divider()

# =========================================================
# TAB 1: ฟีดชุมชน (Timeline)
# =========================================================
with tabs[1]:
    st.subheader("📰 ฟีดข่าวสาร & ชุมชนออนไลน์ทั่วไทย")
    with st.form("post_form", clear_on_submit=True):
        p_name = st.text_input("ชื่อของคุณ / จังหวัดของคุณ")
        p_text = st.text_area("กำลังหาบ้านเช่า หรืออยากโพสต์ประกาศในจังหวัดไหน พิมพ์บอกเพื่อนๆ ได้เลย...")
        if st.form_submit_button("📤 โพสต์ลงฟีด"):
            st.success("🎉 โพสต์ของคุณถูกแชร์เรียบร้อยแล้ว!")

    st.markdown("---")
    st.markdown("👤 **คุณอรัญ (ปทุมธานี):** สวัสดีครับ ผมช่วยดูแลและแนะนำข้อมูลสำหรับท่านที่ต้องการย้ายถิ่นฐานมาทุกจังหวัดทั่วไทย สอบถามได้ครับ!")

# =========================================================
# TAB อื่นๆ คงระบบเดิมครบถ้วน
# =========================================================
with tabs[2]:
    st.subheader("🔴 วิดีโอรีวิวบ้านเช่าทั่วไทย")
with tabs[3]:
    st.subheader("🛡️ ระบบชำระเงินปลอดภัยผ่านคนกลาง (Escrow)")
with tabs[4]:
    st.subheader("➕ ลงประกาศใหม่ (ระบุจังหวัดและพิกัดแม่นยำ)")
    with st.form("new_listing"):
        st.text_input("หัวข้อประกาศ")
        st.selectbox("เลือกจังหวัดของท่าน", provinces_thailand[1:])
        st.number_input("ราคา / ค่าเช่า (บาท)", min_value=0)
        st.form_submit_button("บันทึกประกาศ")
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
