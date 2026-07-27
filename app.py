import streamlit as st
import os

st.set_page_config(page_title="my-marketplace | ศูนย์กลางโซเชียล & อีคอมเมิร์ซทั่วไทย", page_icon="🌐", layout="wide")

st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #1877f2 0%, #0c4a9e 100%);
        padding: 25px;
        border-radius: 12px;
        color: white;
        margin-bottom: 20px;
    }
    .timeline-card, .listing-card {
        background-color: #ffffff;
        border: 1px solid #e4e6eb;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .social-card {
        background-color: #ffffff;
        border: 1px solid #e4e6eb;
        padding: 20px;
        border-radius: 12px;
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

st.markdown("""
    <div class="main-header">
        <h1>🌐 my-marketplace - ศูนย์กลางโซเชียล & ตลาดอสังหาฯ ทั่วไทย</h1>
        <p>ฟีดไทม์ไลน์โพสต์จริง ระบบค้นหาบ้านเช่าทั่วไทย คำนวณสินเชื่อ และระบบ Escrow ปลอดภัย 100%</p>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Session State สำหรับเก็บข้อมูล
# ---------------------------------------------------------
if "timeline_posts" not in st.session_state:
    st.session_state.timeline_posts = [
        {"user": "คุณอรัญ (Fresh Food Manager - ปทุมธานี)", "time": "15 นาทีที่แล้ว", "text": "สวัสดีครับทุกท่าน! ใครกำลังจะย้ายจากต่างจังหวัดเข้ามาทำงานหรือหาบ้านเช่าโซนปทุมธานี ทักมาพูดคุยหรือโพสต์สอบถามได้เลยนะครับ 😊🏡"},
        {"user": "คุณสมชาย (ตัวแทนอสังหาฯ - กรุงเทพฯ)", "time": "1 ชั่วโมงที่แล้ว", "text": "อัปเดตบ้านเช่าและคอนโดพร้อมอยู่ทั่วกรุงเทพฯ และปริมณฑล ราคาประหยัด สนใจดูรายละเอียดกดที่แท็บค้นหาได้เลยครับ 🏢✨"}
    ]

if "listings" not in st.session_state:
    st.session_state.listings = [
        {"title": "🏠 ทาวน์โฮมให้เช่า ทำเลใกล้แหล่งงาน", "province": "ปทุมธานี", "price": 6500, "type": "บ้านเช่า / หอพัก", "desc": "พร้อมเข้าอยู่ เดินทางสะดวก ปลอดภัย", "seller": "คุณอรัญ"},
        {"title": "🏢 คอนโดมิเนียมวิวสวย ใจกลางเมือง", "province": "กรุงเทพมหานคร", "price": 12000, "type": "คอนโดมิเนียม", "desc": "แต่งครบพร้อมกระเป๋าใบเดียว", "seller": "คุณสมชาย"},
        {"title": "🏡 บ้านเดี่ยวสองชั้น บรรยากาศธรรมชาติ", "province": "เชียงใหม่", "price": 15000, "type": "บ้านเดี่ยว / ทาวน์โฮม", "desc": "วิวภูเขา อากาศดี เหมาะแก่การพักผ่อน", "seller": "คุณA"}
    ]

if "finance_requests" not in st.session_state:
    st.session_state.finance_requests = []

if "contacts" not in st.session_state:
    st.session_state.contacts = []

# สร้าง Tabs หลัก
tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13 = st.tabs([
    "📰 ฟีดไทม์ไลน์",
    "🏠 ค้นหาบ้านเช่า",
    "🌐 โซเชียล",
    "🔴 รีวิว",
    "📱 คลิปสั้น",
    "🛒 ตลาดออนไลน์",
    "🛡️ Escrow",
    "➕ ลงประกาศ", 
    "🚗 ไฟแนนซ์",
    "🚘 ค่างวด",
    "🏦 กู้บ้าน",
    "💳 ชำระเงิน", 
    "📞 ติดต่อ",
    "⚙️ แอดมิน"
])

provinces_thailand = [
    "--- ทุกจังหวัดทั่วไทย ---",
    "กรุงเทพมหานคร", "ปทุมธานี", "นนทบุรี", "สมุทรปราการ", "สมุทรสาคร", "นครปฐม",
    "เชียงใหม่", "เชียงราย", "ขอนแก่น", "นครราชสีมา", "อุบลราชธานี", "อุดรธานี",
    "ชลบุรี", "ระยอง", "ภูเก็ต", "สงขลา", "สุราษฎร์ธานี", "พระนครศรีอยุธยา"
]

with tab0:
    st.subheader("📰 ฟีดไทม์ไลน์ชุมชนออนไลน์ (Community Timeline)")
    with st.form("form_t0", clear_on_submit=True):
        p_user = st.text_input("ชื่อของคุณ / จังหวัด")
        p_text = st.text_area("คุณกำลังคิดอะไรอยู่ หรือต้องการหาบ้านเช่าที่ไหน?")
        if st.form_submit_button("🚀 โพสต์ลงไทม์ไลน์ทันที"):
            if p_user and p_text:
                st.session_state.timeline_posts.insert(0, {"user": p_user, "time": "เมื่อสักครู่นี้", "text": p_text})
                st.success("🎉 โพสต์สำเร็จ!")
            else:
                st.warning("⚠️ กรุณากรอกข้อมูลให้ครบ")

    st.markdown("### 🔥 ฟีดโพสต์ล่าสุด")
    for post in st.session_state.timeline_posts:
        st.markdown(f'<div class="timeline-card"><strong>👤 {post["user"]}</strong> <span style="color:gray; font-size:12px;">{post["time"]}</span><p style="margin-top:10px;">{post["text"]}</p></div>', unsafe_allow_html=True)

with tab1:
    st.subheader("📍 ระบบค้นหาอสังหาฯ และบ้านเช่าทั่วไทย")
    sel_prov = st.selectbox("📍 เลือกจังหวัด", provinces_thailand, key="s_prov")
    sel_type = st.selectbox("🏠 ประเภท", ["ทั้งหมด", "บ้านเช่า / หอพัก", "บ้านเดี่ยว / ทาวน์โฮม", "คอนโดมิเนียม", "ที่ดิน"], key="s_type")
    
    for item in st.session_state.listings:
        if (sel_prov == "--- ทุกจังหวัดทั่วไทย ---" or item["province"] == sel_prov) and (sel_type == "ทั้งหมด" or item["type"] == sel_type):
            st.markdown(f'<div class="listing-card"><h3>{item["title"]}</h3><p><strong>ราคา:</strong> {item["price"]:,} บาท/เดือน | <strong>ประเภท:</strong> {item["type"]}</p><p>{item["desc"]}</p><p style="color:gray; font-size:13px;">📍 จังหวัด: {item["province"]} | ผู้ติดต่อ: {item["seller"]}</p></div>', unsafe_allow_html=True)

with tab2:
    st.subheader("🌐 ศูนย์รวมลิงก์เชื่อมโยงโซเชียลมีเดีย")
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown('<div class="social-card"><h3>📘 Facebook</h3><a href="https://www.facebook.com" target="_blank">🔗 ไปที่ Facebook</a></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="social-card"><h3>🔴 YouTube</h3><a href="https://www.youtube.com" target="_blank">🔗 ไปที่ YouTube</a></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="social-card"><h3>📱 TikTok</h3><a href="https://www.tiktok.com" target="_blank">🔗 ไปที่ TikTok</a></div>', unsafe_allow_html=True)
    with c4: st.markdown('<div class="social-card"><h3>🛍️ Shopee / Lazada</h3><a href="https://shopee.co.th" target="_blank">🔗 ไปที่ Shopee</a></div>', unsafe_allow_html=True)

with tab3:
    st.subheader("🔴 วิดีโอรีวิวบ้านเช่า & โครงการ (YouTube Style)")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

with tab4:
    st.subheader("📱 คลิปสั้นรีวิวบ้านด่วน (TikTok Style Reels)")
    st.info("🔥 **Reel #1:** คอนโดแต่งครบ 4,500 บ./เดือน")

with tab5:
    st.subheader("🛒 ตลาดสินค้าตกแต่งบ้าน (Shopee / Lazada Style)")
    st.markdown('<div class="social-card"><h4>🛏️ ชุดเครื่องนอน</h4><p>590 บาท</p><a href="https://shopee.co.th" target="_blank">🛒 สั่งซื้อ</a></div>', unsafe_allow_html=True)

with tab6:
    st.subheader("🛡️ ระบบชำระเงินปลอดภัยผ่านคนกลาง (Escrow)")
    st.write("ระบบพักเงินปลอดภัย 100% สำหรับผู้ซื้อและผู้เช่าที่อยู่ต่างจังหวัด")

with tab7:
    st.subheader("➕ ลงประกาศใหม่")
    with st.form("form_t7", clear_on_submit=True):
        l_title = st.text_input("หัวข้อประกาศ")
        l_prov = st.selectbox("จังหวัด", provinces_thailand[1:], key="l_p")
        l_type = st.selectbox("ประเภท", ["บ้านเช่า / หอพัก", "บ้านเดี่ยว / ทาวน์โฮม", "คอนโดมิเนียม", "ที่ดิน"], key="l_t")
        l_price = st.number_input("ราคาต่อเดือน (บาท)", min_value=0, step=500)
        l_desc = st.text_area("รายละเอียด")
        l_seller = st.text_input("ชื่อผู้ติดต่อ / เบอร์โทร")
        if st.form_submit_button("💾 บันทึกประกาศ"):
            if l_title and l_price > 0 and l_seller:
                st.session_state.listings.insert(0, {"title": l_title, "province": l_prov, "price": l_price, "type": l_type, "desc": l_desc, "seller": l_seller})
                st.success("🎉 บันทึกประกาศสำเร็จ!")
            else:
                st.warning("⚠️ กรุณากรอกข้อมูลให้ครบ")

with tab8:
    st.subheader("🚗 บริการจัดไฟแนนซ์รถยนต์ & รีไฟแนนซ์")
    with st.form("form_t8", clear_on_submit=True):
        f_name = st.text_input("ชื่อ-นามสกุล")
        f_tel = st.text_input("เบอร์โทรศัพท์")
        f_car = st.text_input("รุ่นรถยนต์ / ปี")
        f_amt = st.number_input("วงเงินกู้ (บาท)", min_value=10000, step=10000)
        if st.form_submit_button("📩 ส่งเรื่องขอสินเชื่อ"):
            if f_name and f_tel:
                st.session_state.finance_requests.append({"name": f_name, "tel": f_tel, "car": f_car, "amount": f_amt})
                st.success("🎉 ส่งข้อมูลขอสินเชื่อสำเร็จ!")
            else:
                st.warning("⚠️ กรุณากรอกชื่อและเบอร์โทร")

with tab9:
    st.subheader("🚘 เครื่องมือคำนวณค่างวดผ่อนชำระรถยนต์")
    c_price = st.number_input("ราคารถ (บาท)", min_value=50000, value=350000, step=10000)
    c_down = st.number_input("เงินดาวน์ (บาท)", min_value=0, value=30000, step=5000)
    c_rate = st.slider("ดอกเบี้ยต่อปี (%)", min_value=2.0, max_value=15.0, value=4.5, step=0.25)
    c_term = st.selectbox("งวด (เดือน)", [24, 36, 48, 60, 72, 84])
    
    net_loan = max(0, c_price - c_down)
    m_pay = (net_loan + (net_loan * (c_rate / 100) * (c_term / 12))) / c_term
    st.metric(label="ยอดจัดไฟแนนซ์สุทธิ", value=f"{net_loan:,.0f} บาท")
    st.metric(label="ค่างวดผ่อนประมาณ / เดือน (รวม VAT 7%)", value=f"{m_pay * 1.07:,.0f} บาท")

with tab10:
    st.subheader("🏦 เครื่องมือคำนวณวงเงินกู้ซื้อบ้าน")
    sal = st.number_input("รายได้สุทธิต่อเดือน (บาท)", min_value=10000, value=30000, step=1000)
    deb = st.number_input("ภาระหนี้เดิมต่อเดือน (บาท)", min_value=0, value=0, step=500)
    net_inc = max(0, sal - deb)
    st.metric(label="ค่างวดผ่อนบ้านสูงสุด / เดือน", value=f"{net_inc * 0.40:,.0f} บาท")
    st.metric(label="ประมาณการวงเงินกู้ซื้อบ้านสูงสุด", value=f"{((net_inc * 0.40) / 7000) * 1000000:,.0f} บาท")

with tab11:
    st.subheader("💳 ชำระเงินค่าบริการแอดมิน / อัปเกรดพรีเมียม")
    st.info("🎯 **พร้อมเพย์:** 0XX-XXX-XXXX (ชื่อบัญชี: ศูนย์กลางมาร์เก็ตเพลส)")

with tab12:
    st.subheader("📞 ช่องทางติดต่อ & แจ้งเรื่องร้องเรียน")
    with st.form("form_t12", clear_on_submit=True):
        c_name = st.text_input("ชื่อ-นามสกุล")
        c_tel = st.text_input("เบอร์โทรศัพท์")
        c_msg = st.text_area("ข้อความ / แจ้งปัญหา / แนบสลิป")
        if st.form_submit_button("📩 ส่งข้อความ"):
            if c_name and c_tel and c_msg:
                st.sessio
