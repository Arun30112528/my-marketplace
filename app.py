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
    .timeline-card {
        background-color: #ffffff;
        border: 1px solid #e4e6eb;
        padding: 22px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
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

st.markdown("""
    <div class="main-header">
        <h1>🌐 my-marketplace - ฟีดไทม์ไลน์ & ศูนย์กลางทั่วไทย</h1>
        <p>แหล่งรวมบ้านเช่า ซื้อ-ขายอสังหาฯ ฟีดชุมชนสุดฮิต และเชื่อมโยงโซเชียลมีเดีย ปลอดภัยด้วยระบบ Escrow</p>
    </div>
""", unsafe_allow_html=True)

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
    st.write("พื้นที่แชร์เรื่องราว อัปเดตสถานะ ประกาศหาบ้านเช่า หรือพูดคุยแลกเปลี่ยนข้อมูลกันได้ที่นี่ครับ!")

    with st.container():
        st.markdown('<div class="timeline-card">', unsafe_allow_html=True)
        st.markdown("##### ✍️ คุณกำลังคิดอะไรอยู่? หรือต้องการหาบ้านเช่าจังหวัดไหน โพสต์บอกเพื่อนๆ ได้เลย")
        with st.form("timeline_post_active", clear_on_submit=True):
            t_name = st.text_input("ชื่อของคุณ / จังหวัดของคุณ")
            t_msg = st.text_area("เขียนข้อความ แชร์เรื่องราว หรือรายละเอียดบ้านที่กำลังมองหา...")
            if st.form_submit_button("🚀 เผยแพร่โพสต์ลงไทม์ไลน์"):
                if t_name and t_msg:
                    st.success("🎉 โพสต์ของคุณถูกแชร์ขึ้นหน้าฟีดไทม์ไลน์เรียบร้อยแล้ว!")
                else:
                    st.warning("⚠️ กรุณากรอกชื่อและข้อความก่อนโพสต์ครับ")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 🔥 โพสต์ยอดฮิตในชุมชนตอนนี้")

    timeline_posts = [
        {"user": "คุณอรัญ (Fresh Food Manager - ปทุมธานี)", "time": "15 นาทีที่แล้ว", "text": "สวัสดีครับทุกท่าน! ใครกำลังจะย้ายจากต่างจังหวัดเข้ามาทำงานหรือหาบ้านเช่าโซนปทุมธานี ทักมาพูดคุยหรือโพสต์สอบถามในฟีดนี้ได้เลยนะครับ ยินดีต้อนรับครับผม 😊🏡"},
        {"user": "คุณสมชาย (ตัวแทนอสังหาฯ - กรุงเทพฯ)", "time": "1 ชั่วโมงที่แล้ว", "text": "อัปเดตบ้านเช่าและคอนโดพร้อมอยู่ทั่วกรุงเทพฯ และปริมณฑล ราคาประหยัด สนใจดูรายละเอียดกดที่แท็บค้นหาได้เลยครับ 🏢✨"},
        {"user": "คุณนภา (เชียงใหม่)", "time": "3 ชั่วโมงที่แล้ว", "text": "เพิ่งใช้บริการหาบ้านเช่าผ่านเว็บนี้ สะดวกมากค่ะ ได้บ้านบรรยากาศดีที่เชียงใหม่แล้ว แนะนำเลยค่ะ 👍"}
    ]

    for post in timeline_posts:
        st.markdown(f'''
            <div class="timeline-card">
                <strong>👤 {post['user']}</strong> &nbsp;&nbsp; <span style="color:gray; font-size:12px;">{post['time']}</span>
                <p style="margin-top: 12px; font-size: 16px; line-height: 1.5;">{post['text']}</p>
                <hr style="margin: 10px 0; border: none; border-top: 1px solid #eaeaea;">
                <span style="color: #1877f2; cursor: pointer; font-weight: bold;">👍 ถูกใจ</span> &nbsp;&nbsp;&nbsp;&nbsp; 
                <span style="color: #65676b; cursor: pointer; font-weight: bold;">💬 แสดงความคิดเห็น</span> &nbsp;&nbsp;&nbsp;&nbsp; 
                <span style="color: #65676b; cursor: pointer; font-weight: bold;">↗️ แชร์</span>
            </div>
        ''', unsafe_allow_html=True)

with tabs[1]:
    st.subheader("📍 ระบบค้นหาอสังหาฯ และบ้านเช่าแม่นยำทั่วประเทศไทย")
    with st.container():
        st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
        col_loc1, col_loc2, col_loc3 = st.columns(3)
        with col_loc1:
            selected_province = st.selectbox("📍 เลือกจังหวัด", provinces_thailand)
        with col_loc2:
            property_type = st.selectbox("🏠 ประเภท", ["ทั้งหมด", "บ้านเช่า / หอพัก", "บ้านเดี่ยว / ทาวน์โฮม", "คอนโดมิเนียม", "ที่ดิน"])
        with col_loc3:
            price_range = st.selectbox("💰 ช่วงราคา", ["ทั้งหมด", "ต่ำกว่า 5,000 บาท/เดือน", "5,000 - 10,000 บาท/เดือน", "10,000 - 20,000 บาท/เดือน", "20,000 บาทขึ้นไป"])
        st.markdown('</div>', unsafe_allow_html=True)

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

with tabs[2]:
    st.subheader("🌐 ศูนย์รวมลิงก์เชื่อมโยงโซเชียล")
    col_s1, col_s2, col_s3, col_s4 = st.columns(4)
    with col_s1:
        st.markdown('<div class="social-card"><h3>📘 Facebook</h3><p>ติดตามเพจหลักชุมชน</p><a href="https://www.facebook.com" target="_blank">🔗 ไปที่ Facebook</a></div>', unsafe_allow_html=True)
    with col_s2:
        st.markdown('<div class="social-card"><h3>🔴 YouTube</h3><p>รับชมวิดีโอรีวิวบ้าน</p><a href="https://www.youtube.com" target="_blank">🔗 ไปที่ YouTube</a></div>', unsafe_allow_html=True)
    with col_s3:
        st.markdown('<div class="social-card"><h3>📱 TikTok</h3><p>รับชมคลิปสั้นรีวิวห้องพัก</p><a href="https://www.tiktok.com" target="_blank">🔗 ไปที่ TikTok</a></div>', unsafe_allow_html=True)
    with col_s4:
        st.markdown('<div class="social-card"><h3>🛍️ Shopee / Lazada</h3><p>เลือกซื้อของแต่งบ้าน</p><a href="https://shopee.co.th" target="_blank">🔗 ไปที่ Shopee</a></div>', unsafe_allow_html=True)

with tabs[3]:
    st.subheader("🔴 วิดีโอรีวิวบ้านเช่า & โครงการ (YouTube Style)")
    col_v1, col_v2 = st.columns(2)
    with col_v1:
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    with col_v2:
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

with tabs[4]:
    st.subheader("📱 คลิปสั้นรีวิวบ้านด่วน (TikTok Style Reels)")
    col_t1, col_t2, col_t3 = st.columns(3)
    with col_t1:
        st.info("🔥 **Reel #1:** คอนโดแต่งครบ 4,500 บ.")
    with col_t2:
        st.info("✨ **Reel #2:** ทาวน์โฮมรีโนเวทใหม่")
    with col_t3:
        st.info("🏡 **Reel #3:** บ้านเดี่ยวเชียงใหม่")

with tabs[5]:
    st.subheader("🛒 ตลาดสินค้าตกแต่งบ้าน (Shopee / Lazada Style)")
    col_p1, col_p2, col_p3 = st.columns(3)
    with col_p1:
        st.markdown('<div class="shopping-card"><h4>🛏️ ชุดเครื่องนอน</h4><p>590 บาท</p><a href="https://shopee.co.th" target="_blank">🛒 สั่งซื้อ</a></div>', unsafe_allow_html=True)
    with col_p2:
        st.markdown('<div class="shopping-card"><h4>🪑 โต๊ะทำงาน</h4><p>450 บาท</p><a href="https://shopee.co.th" target="_blank">🛒 สั่งซื้อ</a></div>', unsafe_allow_html=True)
    with col_p3:
        st.markdown('<div class="shopping-card"><h4>💡 หลอดไฟอัจฉริยะ</h4><p>199 บาท</p><a href="https://shopee.co.th" target="_blank">🛒 สั่งซื้อ</a></div>', unsafe_allow_html=True)

with tabs[6]:
    st.subheader("🛡️ ระบบชำระเงินปลอดภัยผ่านคนกลาง (Escrow)")
with tabs[7]:
    st.subheader("➕ ลงประกาศใหม่ (ระบุพิกัดทั่วไทย)")
    with st.form("new_listing"):
        st.text_input("หัวข้อประกาศ")
        st.selectbox("เลือกจังหวัด", provinces_thailand[1:])
        st.number_input("ราคา", min_value=0)
        st.form_submit_button("บันทึก")
with tabs[8]:
    st.subheader("🚗 ธุรกรรม & จัดไฟแนนซ์รถยนต์")
with tabs[9]:
    st.subheader("🚘 คำนวณค่างวดผ่อนรถ")
with tabs[10]:
    st.subheader("🏦 เช็กวงเงินกู้บ้าน")
with tabs[11]:
    st.subheader("💳 ชำระเงินค่าบริการแอดมิน")
with tabs[12]:
    st.subheader("📞 ติดต่อ / เรื่องร้องเรียน")
with tabs[13]:
    st.subheader("⚙️ สำหรับแอดมิน")
    if st.text_input("รหัสผ่านแอดมิน", type="password") == "1234":
        st.success("เข้าสู่ระบบแอดมินสำเร็จ")
