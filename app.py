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
    .card-box {
        background-color: #ffffff;
        border: 1px solid #e4e6eb;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="main-header">
        <h1>🌐 my-marketplace - ศูนย์กลางโซเชียล & ตลาดอสังหาฯ ทั่วไทย</h1>
        <p>ฟีดไทม์ไลน์โพสต์จริง ระบบค้นหาบ้านเช่าทั่วไทย คำนวณสินเชื่อ และระบบ Escrow ปลอดภัย 100%</p>
    </div>
""", unsafe_allow_html=True)

if "timeline_posts" not in st.session_state:
    st.session_state.timeline_posts = [
        {"user": "คุณอรัญ (Fresh Food Manager - ปทุมธานี)", "time": "15 นาทีที่แล้ว", "text": "สวัสดีครับทุกท่าน! ใครกำลังจะย้ายจากต่างจังหวัดเข้ามาทำงานหรือหาบ้านเช่าโซนปทุมธานี ทักมาพูดคุยสอบถามได้เลยนะครับ 😊🏡"}
    ]

if "listings" not in st.session_state:
    st.session_state.listings = [
        {"title": "🏠 ทาวน์โฮมให้เช่า ทำเลใกล้แหล่งงาน", "province": "ปทุมธานี", "price": 6500, "type": "บ้านเช่า / หอพัก", "desc": "พร้อมเข้าอยู่ เดินทางสะดวก ปลอดภัย", "seller": "คุณอรัญ"}
    ]

if "finance_requests" not in st.session_state:
    st.session_state.finance_requests = []

if "contacts" not in st.session_state:
    st.session_state.contacts = []

provinces_thailand = [
    "--- ทุกจังหวัดทั่วไทย ---",
    "กรุงเทพมหานคร", "ปทุมธานี", "นนทบุรี", "สมุทรปราการ", "สมุทรสาคร", "นครปฐม",
    "เชียงใหม่", "เชียงราย", "ขอนแก่น", "นครราชสีมา", "อุบลราชธานี", "อุดรธานี",
    "ชลบุรี", "ระยอง", "ภูเก็ต", "สงขลา", "สุราษฎร์ธานี", "พระนครศรีอยุธยา"
]

menu_option = st.selectbox("📌 เลือกเมนูการใช้งานหลัก:", [
    "📰 1. ฟีดไทม์ไลน์",
    "🏠 2. ค้นหาบ้านเช่า",
    "🌐 3. โซเชียล & ร้านค้า",
    "🔴 4. รีวิว YouTube",
    "📱 5. คลิปสั้น TikTok",
    "🛒 6. ตลาดออนไลน์",
    "🛡️ 7. ระบบ Escrow",
    "➕ 8. ลงประกาศใหม่", 
    "🚗 9. บริการจัดไฟแนนซ์",
    "🚘 10. คำนวณค่างวดผ่อนรถ",
    "🏦 11. คำนวณกู้ซื้อบ้าน",
    "💳 12. ชำระเงินค่าบริการ", 
    "📞 13. ติดต่อ / ร้องเรียน",
    "⚙️ 14. ระบบแอดมิน"
])

st.divider()

if menu_option.startswith("📰"):
    st.subheader("📰 ฟีดไทม์ไลน์ชุมชนออนไลน์")
    with st.form("f_post", clear_on_submit=True):
        u_name = st.text_input("ชื่อของคุณ / จังหวัด")
        u_text = st.text_area("คุณกำลังคิดอะไรอยู่ หรือต้องการหาบ้านเช่าที่ไหน?")
        if st.form_submit_button("🚀 โพสต์ลงไทม์ไลน์"):
            if u_name and u_text:
                st.session_state.timeline_posts.insert(0, {"user": u_name, "time": "เมื่อสักครู่นี้", "text": u_text})
                st.success("🎉 โพสต์สำเร็จ!")
            else:
                st.warning("⚠️ กรุณากรอกข้อมูลให้ครบ")

    for p in st.session_state.timeline_posts:
        st.markdown(f'<div class="card-box"><strong>👤 {p["user"]}</strong> <span style="color:gray; font-size:12px;">{p["time"]}</span><p style="margin-top:10px;">{p["text"]}</p></div>', unsafe_allow_html=True)

elif menu_option.startswith("🏠"):
    st.subheader("📍 ระบบค้นหาบ้านเช่าและอสังหาริมทรัพย์ทั่วไทย")
    s_prov = st.selectbox("📍 เลือกจังหวัด", provinces_thailand)
    s_type = st.selectbox("🏠 ประเภท", ["ทั้งหมด", "บ้านเช่า / หอพัก", "บ้านเดี่ยว / ทาวน์โฮม", "คอนโดมิเนียม", "ที่ดิน"])
    
    for item in st.session_state.listings:
        if (s_prov == "--- ทุกจังหวัดทั่วไทย ---" or item["province"] == s_prov) and (s_type == "ทั้งหมด" or item["type"] == s_type):
            st.markdown(f'<div class="card-box"><h3>{item["title"]}</h3><p><strong>ราคา:</strong> {item["price"]:,} บาท/เดือน | <strong>ประเภท:</strong> {item["type"]}</p><p>{item["desc"]}</p><p style="color:gray; font-size:13px;">📍 จังหวัด: {item["province"]} | ผู้ติดต่อ: {item["seller"]}</p></div>', unsafe_allow_html=True)

elif menu_option.startswith("🌐"):
    st.subheader("🌐 ศูนย์รวมลิงก์เชื่อมโยงโซเชียลมีเดีย")
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown('<div class="card-box"><h3>📘 Facebook</h3><a href="https://www.facebook.com" target="_blank">🔗 ไปที่ Facebook</a></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="card-box"><h3>🔴 YouTube</h3><a href="https://www.youtube.com" target="_blank">🔗 ไปที่ YouTube</a></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="card-box"><h3>📱 TikTok</h3><a href="https://www.tiktok.com" target="_blank">🔗 ไปที่ TikTok</a></div>', unsafe_allow_html=True)
    with c4: st.markdown('<div class="card-box"><h3>🛍️ Shopee</h3><a href="https://shopee.co.th" target="_blank">🔗 ไปที่ Shopee</a></div>', unsafe_allow_html=True)

elif menu_option.startswith("🔴"):
    st.subheader("🔴 วิดีโอรีวิวบ้านเช่า & โครงการ (YouTube Style)")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

elif menu_option.startswith("📱"):
    st.subheader("📱 คลิปสั้นรีวิวบ้านด่วน (TikTok Style)")
    st.info("🔥 **Reel #1:** คอนโดแต่งครบ 4,500 บ./เดือน (พร้อมเข้าอยู่)")

elif menu_option.startswith("🛒"):
    st.subheader("🛒 ตลาดสินค้าตกแต่งบ้าน")
    st.markdown('<div class="card-box"><h4>🛏️ ชุดเครื่องนอนพรีเมียม</h4><p>590 บาท</p><a href="https://shopee.co.th" target="_blank">🛒 สั่งซื้อผ่าน Shopee</a></div>', unsafe_allow_html=True)

elif menu_option.startswith("🛡️"):
    st.subheader("🛡️ ระบบชำระเงินปลอดภัยผ่านคนกลาง (Escrow)")
    st.write("ระบบพักเงินปลอดภัย 100% ป้องกันการโดนโกงสำหรับผู้ย้ายมาอยู่ต่างจังหวัด")

elif menu_option.startswith("➕"):
    st.subheader("➕ ลงประกาศใหม่ (เพิ่มเข้าสู่ระบบค้นหาทันที)")
    with st.form("f_add", clear_on_submit=True):
        l_title = st.text_input("หัวข้อประกาศ")
        l_prov = st.selectbox("จังหวัด", provinces_thailand[1:])
        l_type = st.selectbox("ประเภท", ["บ้านเช่า / หอพัก", "บ้านเดี่ยว / ทาวน์โฮม", "คอนโดมิเนียม", "ที่ดิน"])
        l_price = st.number_input("ราคาต่อเดือน (บาท)", min_value=0, step=500)
        l_desc = st.text_area("รายละเอียด")
        l_seller = st.text_input("ชื่อผู้ติดต่อ / เบอร์โทร")
        if st.form_submit_button("💾 บันทึกประกาศ"):
            if l_title and l_price > 0 and l_seller:
                st.session_state.listings.insert(0, {"title": l_title, "province": l_prov, "price": l_price, "type": l_type, "desc": l_desc, "seller": l_seller})
                st.success("🎉 บันทึกประกาศสำเร็จ!")
            else:
                st.warning("⚠️ กรุณากรอกข้อมูลให้ครบ")

elif menu_option.startswith("🚗"):
    st.subheader("🚗 บริการจัดไฟแนนซ์รถยนต์ & รีไฟแนนซ์")
    with st.form("f_fin", clear_on_submit=True):
        f_name = st.text_input("ชื่อ-นามสกุล")
        f_tel = st.text_input("เบอร์โทรศัพท์")
        f_car = st.text_input("รุ่นรถยนต์ / ปี")
        f_amt = st.number_input("วงเงินกู้ (บาท)", min_value=10000, step=10000)
        if st.form_submit_button("📩 ส่งเรื่องขอสินเชื่อ"):
            if f_name and f_tel:
                st.session_state.finance_requests.append({"name": f_name, "tel": f_tel, "car": f_car, "amount": f_amt})
                st.success("🎉 ส่งข้อมูลขอสินเชื่อสำเร็จ เจ้าหน้าที่กำลังติดต่อกลับ!")
            else:
                st.warning("⚠️ กรุณากรอกชื่อและเบอร์โทร")

elif menu_option.startswith("🚘"):
    st.subheader("🚘 เครื่องมือคำนวณค่างวดผ่อนชำระรถยนต์")
    c_price = st.number_input("ราคารถ (บาท)", min_value=50000, value=350000, step=10000)
    c_down = st.number_input("เงินดาวน์ (บาท)", min_value=0, value=30000, step=5000)
    c_rate = st.slider("ดอกเบี้ยต่อปี (%)", min_value=2.0, max_value=15.0, value=4.5, step=0.25)
    c_term = st.selectbox("งวด (เดือน)", [24, 36, 48, 60, 72, 84])
    
    net_loan = max(0, c_price - c_down)
    m_pay = (net_loan + (net_loan * (c_rate / 100) * (c_term / 12))) / c_term
    st.metric(label="ยอดจัดไฟแนนซ์สุทธิ", value=f"{net_loan:,.0f} บาท")
    st.metric(label="ค่างวดผ่อนประมาณ / เดือน (รวม VAT 7%)", value=f"{m_pay * 1.07:,.0f} บาท")

elif menu_option.startswith("🏦"):
    st.subheader("🏦 เครื่องมือคำนวณวงเงินกู้ซื้อบ้าน")
    sal = st.number_input("รายได้สุทธิต่อเดือน (บาท)", min_value=10000, value=30000, step=1000)
    deb = st.number_input("ภาระหนี้เดิมต่อเดือน (บาท)", min_value=0, value=0, step=500)
    net_inc = max(0, sal - deb)
    st.metric(label="ค่างวดผ่อนบ้านสูงสุด / เดือน", value=f"{net_inc * 0.40:,.0f} บาท")
    st.metric(label="ประมาณการวงเงินกู้ซื้อบ้านสูงสุด", value=f"{((net_inc * 0.40) / 7000) * 1000000:,.0f} บาท")

elif menu_option.startswith("💳"):
    st.subheader("💳 ชำระเงินค่าบริการแอดมิน / อัปเกรดพรีเมียม")
    st.write("สแกน QR Code พร้อมเพย์ด้านล่างนี้เพื่อโอนเงินเข้าบัญชี")
    
    col_q1, col_q2 = st.columns([1, 2])
    with col_q1:
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; border: 1px solid #dee2e6;">
            <h4>📌 รายละเอียดบัญชี</h4>
            <p><strong>ธนาคาร:</strong> กสิกรไทย (K+)<br>
            <strong>ชื่อบัญชี:</strong> นาย อรัญ ไชยทิพย์<br>
            <strong>พร้อมเพย์ / เลขที่:</strong> xxx-x-x1601-x</p>
        </div>
        """, unsafe_allow_html=True)
    with col_q2:
        if os.path.exists("qr_code.jpg"):
            st.image("qr_code.jpg", caption="สแกน QR Code เพื่อชำระเงิน", width=300)
        elif os.path.exists("qr_code.png"):
            st.image("qr_code.png", caption="สแกน QR Code เพื่อชำระเงิน", width=300)
        else:
            st.info("💡 สามารถบันทึกสลิปแล้วส่งแจ้งแอดมินได้ที่เมนูติดต่อ / แจ้งเรื่องร้องเรียน")

elif menu_option.startswith("📞"):
    st.subheader("📞 ช่องทางติดต่อ & แจ้งเรื่องร้องเรียน / ส่งสลิปโอนเงิน")
    with st.form("f_con", clear_on_submit=True):
        c_name = st.text_input("ชื่อ-นามสกุล")
        c_tel = st.text_input("เบอร์โทรศัพท์")
        c_msg = st.text_area("ข้อความ / แจ้งปัญหา / แนบแจ้งหลักฐานการโอนเงิน (สลิป)")
        if st.form_submit_button("📩 ส่งข้อมูล"):
            if c_name and c_t
