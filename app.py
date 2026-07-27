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

tabs = st.tabs([
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

with tabs[0]:
    st.subheader("📰 ฟีดไทม์ไลน์ชุมชนออนไลน์ (Community Timeline)")
    st.write("พื้นที่แชร์เรื่องราว อัปเดตสถานะ ประกาศหาบ้านเช่า หรือพูดคุยแลกเปลี่ยนข้อมูลกันได้ทันที!")

    with st.container():
        st.markdown('<div class="timeline-card">', unsafe_allow_html=True)
        st.markdown("##### ✍️ สร้างโพสต์ใหม่ของคุณ")
        with st.form("timeline_form_real", clear_on_submit=True):
            p_user = st.text_input("ชื่อของคุณ / จังหวัด")
            p_text = st.text_area("คุณกำลังคิดอะไรอยู่ หรือต้องการหาบ้านเช่าที่ไหน?")
            if st.form_submit_button("🚀 โพสต์ลงไทม์ไลน์ทันที"):
                if p_user and p_text:
                    new_post = {"user": p_user, "time": "เมื่อสักครู่นี้", "text": p_text}
                    st.session_state.timeline_posts.insert(0, new_post)
                    st.success("🎉 โพสต์ของคุณถูกเผยแพร่ลงหน้าฟีดเรียบร้อยแล้ว!")
                else:
                    st.warning("⚠️ กรุณากรอกชื่อและข้อความก่อนกดโพสต์ครับ")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 🔥 ฟีดโพสต์ล่าสุดจากสมาชิก")
    for post in st.session_state.timeline_posts:
        st.markdown(f'''
            <div class="timeline-card">
                <strong>👤 {post['user']}</strong> &nbsp;&nbsp; <span style="color:gray; font-size:12px;">{post['time']}</span>
                <p style="margin-top: 10px; font-size: 15px; line-height: 1.5;">{post['text']}</p>
            </div>
        ''', unsafe_allow_html=True)

with tabs[1]:
    st.subheader("📍 ระบบค้นหาอสังหาฯ และบ้านเช่าแม่นยำทั่วประเทศไทย")
    with st.container():
        st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
        col_l1, col_l2, col_l3 = st.columns(3)
        with col_l1:
            sel_prov = st.selectbox("📍 เลือกจังหวัด", provinces_thailand)
        with col_l2:
            sel_type = st.selectbox("🏠 ประเภท", ["ทั้งหมด", "บ้านเช่า / หอพัก", "บ้านเดี่ยว / ทาวน์โฮม", "คอนโดมิเนียม", "ที่ดิน"])
        with col_l3:
            sel_price = st.selectbox("💰 ช่วงราคา / ค่าเช่า", ["ทั้งหมด", "ต่ำกว่า 10,000 บาท", "10,000 - 20,000 บาท", "20,000 บาทขึ้นไป"])
        st.markdown('</div>', unsafe_allow_html=True)

    filtered_list = []
    for item in st.session_state.listings:
        match = True
        if sel_prov != "--- ทุกจังหวัดทั่วไทย ---" and item["province"] != sel_prov:
            match = False
        if sel_type != "ทั้งหมด" and item["type"] != sel_type:
            match = False
        if sel_price == "ต่ำกว่า 10,000 บาท" and item["price"] >= 10000:
            match = False
        elif sel_price == "10,000 - 20,000 บาท" and not (10000 <= item["price"] <= 20000):
            match = False
        elif sel_price == "20,000 บาทขึ้นไป" and item["price"] <= 20000:
            match = False
        if match:
            filtered_list.append(item)

    st.subheader(f"📌 ผลการค้นหาพบทั้งหมด {len(filtered_list)} รายการ")
    for item in filtered_list:
        st.markdown(f'''
            <div class="listing-card">
                <h3>{item['title']}</h3>
                <p><strong>ค่าเช่า/ราคา:</strong> {item['price']:,} บาท/เดือน | <strong>ประเภท:</strong> {item['type']}</p>
                <p>{item['desc']}</p>
                <p style="color: gray; font-size: 13px;">📍 จังหวัด: {item['province']} | ผู้ลงประกาศ: {item['seller']}</p>
            </div>
        ''', unsafe_allow_html=True)

with tabs[2]:
    st.subheader("🌐 ศูนย์รวมลิงก์เชื่อมโยงโซเชียลมีเดีย")
    col_s1, col_s2, col_s3, col_s4 = st.columns(4)
    with col_s1:
        st.markdown('<div class="social-card"><h3>📘 Facebook</h3><a href="https://www.facebook.com" target="_blank">🔗 ไปที่ Facebook</a></div>', unsafe_allow_html=True)
    with col_s2:
        st.markdown('<div class="social-card"><h3>🔴 YouTube</h3><a href="https://www.youtube.com" target="_blank">🔗 ไปที่ YouTube</a></div>', unsafe_allow_html=True)
    with col_s3:
        st.markdown('<div class="social-card"><h3>📱 TikTok</h3><a href="https://www.tiktok.com" target="_blank">🔗 ไปที่ TikTok</a></div>', unsafe_allow_html=True)
    with col_s4:
        st.markdown('<div class="social-card"><h3>🛍️ Shopee / Lazada</h3><a href="https://shopee.co.th" target="_blank">🔗 ไปที่ Shopee</a></div>', unsafe_allow_html=True)

with tabs[3]:
    st.subheader("🔴 วิดีโอรีวิวบ้านเช่า & โครงการ (YouTube Style)")
    c1, c2 = st.columns(2)
    with c1:
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    with c2:
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

with tabs[4]:
    st.subheader("📱 คลิปสั้นรีวิวบ้านด่วน (TikTok Style Reels)")
    t1, t2, t3 = st.columns(3)
    with t1:
        st.info("🔥 **Reel #1:** คอนโดแต่งครบ 4,500 บ.")
    with t2:
        st.info("✨ **Reel #2:** ทาวน์โฮมรีโนเวทใหม่")
    with t3:
        st.info("🏡 **Reel #3:** บ้านเดี่ยวเชียงใหม่")

with tabs[5]:
    st.subheader("🛒 ตลาดสินค้าตกแต่งบ้าน (Shopee / Lazada Style)")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown('<div class="social-card"><h4>🛏️ ชุดเครื่องนอน</h4><p>590 บาท</p><a href="https://shopee.co.th" target="_blank">🛒 สั่งซื้อ</a></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="social-card"><h4>🪑 โต๊ะทำงาน</h4><p>450 บาท</p><a href="https://shopee.co.th" target="_blank">🛒 สั่งซื้อ</a></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="social-card"><h4>💡 หลอดไฟอัจฉริยะ</h4><p>199 บาท</p><a href="https://shopee.co.th" target="_blank">🛒 สั่งซื้อ</a></div>', unsafe_allow_html=True)

with tabs[6]:
    st.subheader("🛡️ ระบบชำระเงินปลอดภัยผ่านคนกลาง (Escrow)")
    st.write("ระบบพักเงินปลอดภัย 100% สำหรับผู้ซื้อและผู้เช่า")

with tabs[7]:
    st.subheader("➕ ลงประกาศใหม่ (เพิ่มข้อมูลเข้าสู่ระบบค้นหาทันที)")
    with st.form("real_listing_form", clear_on_submit=True):
        l_title = st.text_input("หัวข้อประกาศ")
        l_prov = st.selectbox("เลือกจังหวัด", provinces_thailand[1:])
        l_type = st.selectbox("ประเภทอสังหาริมทรัพย์", ["บ้านเช่า / หอพัก", "บ้านเดี่ยว / ทาวน์โฮม", "คอนโดมิเนียม", "ที่ดิน"])
        l_price = st.number_input("ราคา / ค่าเช่าต่อเดือน (บาท)", min_value=0, step=500)
        l_desc = st.text_area("รายละเอียดเพิ่มเติม")
        l_seller = st.text_input("ชื่อผู้ติดต่อ / เบอร์โทร")
        
        if st.form_submit_button("💾 บันทึกและเผยแพร่ประกาศ"):
            if l_title and l_price > 0 and l_seller:
                new_item = {
                    "title": l_title,
                    "province": l_prov,
                    "price": l_price,
                    "type": l_type,
                    "desc": l_desc,
                    "seller": l_seller
                }
                st.session_state.listings.insert(0, new_item)
                st.success("🎉 บันทึกประกาศสำเร็จ! ข้อมูลถูกเพิ่มเข้าไปในระบบค้นหาเรียบร้อยแล้วครับ")
            else:
                st.warning("⚠️ กรุณากรอกข้อมูลให้ครบถ้วน")

with tabs[8]:
    st.subheader("🚗 บริการจัดไฟแนนซ์รถยนต์ & รีไฟแนนซ์")
 
