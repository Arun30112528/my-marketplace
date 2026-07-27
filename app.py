import streamlit as st
import os

st.set_page_config(page_title="ศูนย์กลางลงประกาศบ้าน อสังหาฯ & รถยนต์มือสอง", page_icon="🏠", layout="wide")

col_logo, col_header = st.columns([1, 5])

with col_logo:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=120)
    elif os.path.exists("logo.jpg"):
        st.image("logo.jpg", width=120)
    else:
        st.title("🏠")

with col_header:
    st.title("ศูนย์กลางลงประกาศบ้าน อสังหาฯ & รถยนต์มือสอง")
    st.write("ซื้อ-ขายบ้าน คอนโด รถยนต์มือสอง ปลอดภัยด้วยระบบชำระเงินคนกลาง (Escrow) และ Verified Seller")

st.markdown("---")
col_banner1, col_banner2 = st.columns([3, 1])

with col_banner1:
    if os.path.exists("banner.jpg") or os.path.exists("banner.png"):
        banner_file = "banner.jpg" if os.path.exists("banner.jpg") else "banner.png"
        st.image(banner_file, use_column_width=True)
    else:
        st.info("📢 พื้นที่สำหรับติดแบนเนอร์โฆษณา")

with col_banner2:
    st.success("🛡️ ปลอดภัย 100%\n\nผู้ขายผ่านการยืนยันตัวตน + ระบบ Escrow")

st.markdown("---")

tabs = st.tabs([
    "📰 ฟีดไทม์ไลน์ (Feed)",
    "🔍 ค้นหาประกาศทั้งหมด", 
    "🛡️ ชำระเงินผ่านระบบกลาง (Escrow)",
    "➕ ลงประกาศใหม่ (ฟรี)", 
    "🚗 ธุรกรรม & จัดไฟแนนซ์รถยนต์",
    "🚘 คำนวณค่างวดผ่อนรถ",
    "🏦 เช็กวงเงินกู้บ้าน",
    "🎁 กิจกรรม & ส่วนลด",
    "🔴 ไลฟ์สดขายสินค้า (Live)",
    "💳 ชำระเงินค่าบริการแอดมิน", 
    "📞 ติดต่อ / เรื่องร้องเรียน",
    "⚙️ สำหรับแอดมิน"
])

# =========================================================
# TAB 0: ฟีดไทม์ไลน์ (News Feed สไตล์ Facebook)
# =========================================================
with tabs[0]:
    st.subheader("📰 ฟีดไทม์ไลน์ (News Feed & Community)")
    st.write("พื้นที่แชร์เรื่องราว อัปเดตสถานะ พูดคุย หรือสอบถามข้อมูลซื้อขายได้ที่นี่ครับ")

    # ส่วนสร้างโพสต์ใหม่ (Create Post Box)
    with st.form("timeline_post_form", clear_on_submit=True):
        st.markdown("##### ✍️ คุณกำลังคิดอะไรอยู่ ?")
        poster_name = st.text_input("ชื่อของคุณ / ชื่อร้านค้า")
        post_content = st.text_area("เขียนข้อความ หรือแชร์เรื่องราวที่นี่...")
        submit_post = st.form_submit_button("🚀 โพสต์ลงไทม์ไลน์")
        
        if submit_post:
            if poster_name and post_content:
                st.success("🎉 โพสต์ของคุณถูกเผยแพร่ลงบนไทม์ไลน์เรียบร้อยแล้ว!")
            else:
                st.warning("⚠️ กรุณากรอกชื่อและข้อความก่อนโพสต์ครับ")

    st.divider()
    st.subheader("📌 โพสต์ล่าสุดในชุมชน")

    # ตัวอย่างโพสต์จำลองในฟีด (Mock Timeline Posts)
    sample_posts = [
        {
            "name": "คุณอรัญ (ผู้ช่วยผู้จัดการโลตัสปทุมธานี)",
            "time": "10 นาทีที่แล้ว",
            "text": "สวัสดีครับชาวชุมชนปทุมธานี ใครกำลังมองหารถยนต์มือสองสภาพดี หรือบ้านเดี่ยวทำเลใกล้โลตัส ทักสอบถามพูดคุยกันได้นะครับ ยินดีให้บริการครับผม 😊🚗🏡"
        },
        {
            "name": "คุณสมชาย เต็นท์รถมือสอง",
            "time": "1 ชั่วโมงที่แล้ว",
            "text": "วันนี้มีรถเข้าใหม่หลายคันครับ Yaris Ativ และ Civic สภาพป้ายแดง ฟรีดาวน์ทุกคัน สนใจแวะมาดูที่หน้าเว็บหมวดรถยนต์ได้เลยครับ!"
        },
        {
            "name": "คุณวิภาวดี",
            "time": "3 ชั่วโมงที่แล้ว",
            "text": "ระบบคนกลาง Escrow ของเว็บนี้ใช้งานสะดวกมากเลยค่ะ โอนเงินปลอดภัยดี สบายใจทั้งผู้ซื้อและผู้ขายเลย 👍✨"
        }
    ]

    for post in sample_posts:
        with st.container():
            st.markdown(f"**👤 {post['name']}** &nbsp;&nbsp;&nbsp; <span style='color:gray; font-size:12px;'>{post['time']}</span>", unsafe_allow_html=True)
            st.write(post["text"])
            
            col_like, col_comment, col_share = st.columns([1, 1, 4])
            col_like.button("👍 ถูกใจ", key=f"like_{post['name']}")
            col_comment.button("💬 แสดงความคิดเห็น", key=f"cmt_{post['name']}")
        st.divider()

# =========================================================
# TAB 1: ค้นหาประกาศทั้งหมด
# =========================================================
with tabs[1]:
    st.subheader("🔍 ค้นหาบ้าน คอนโด รถยนต์ และสินค้ามือสอง")
    
    mock_listings = [
        {
            "id": 1,
            "title": "🚗 Toyota Yaris Ativ 1.2 E ปี 2020 (เกียร์ออโต้)",
            "category": "🚗 รถยนต์มือสอง",
            "price": 359000,
            "price_text": "359,000 บาท (ฟรีดาวน์ / ผ่อนประมาณ 6,xxx บาท/เดือน)",
            "details": "รถบ้านสภาพสวยเดิมๆ ไม่เคยชนหนัก เลขไมล์ 45,000 กม. เช็กศูนย์ตลอด เจ้าของขายเอง",
            "location": "ปทุมธานี",
            "seller": "คุณสมชาย",
            "verified": True,
            "img": "https://via.placeholder.com/400x250.png?text=Toyota+Yaris+Ativ+2020"
        },
        {
            "id": 2,
            "title": "🚗 Honda Civic FC 1.8 EL ปี 2018 (เกียร์ออโต้)",
            "category": "🚗 รถยนต์มือสอง",
            "price": 529000,
            "price_text": "529,000 บาท (ผ่อนประมาณ 9,xxx บาท/เดือน)",
            "details": "ตัวท็อปออปชั่นเต็ม เบาะหนัง ปรับไฟฟ้า ปุ่ม Push Start เอกสารเล่มพร้อมโอนทันที",
            "location": "กรุงเทพฯ และปริมณฑล",
            "seller": "คุณวิชัย (เต็นท์รถ VIP)",
            "verified": True,
            "img": "https://via.placeholder.com/400x250.png?text=Honda+Civic+FC+2018"
        },
        {
            "id": 3,
            "title": "🏠 ขายบ้านเดี่ยว 2 ชั้น 4 ห้องนอน 3 ห้องน้ำ หมู่บ้านภัทรินทร์ ปทุมธานี",
            "category": "🏠 อสังหาริมทรัพย์",
            "price": 3490000,
            "price_text": "3,490,000 บาท (กู้ได้เต็ม 100%)",
            "details": "เนื้อที่ 52 ตร.วา พร้อมเฟอร์นิเจอร์บางส่วน บรรยากาศร่มรื่น ใกล้ศูนย์ราชการและโลตัสปทุมธานี",
            "location": "ปทุมธานี",
            "seller": "คุณอรัญ (นายหน้า VIP)",
            "verified": True,
            "img": "https://via.placeholder.com/400x250.png?text=Single+House+Pathumthani"
        }
    ]

    for idx, item in enumerate(mock_listings):
        with st.container():
            col_img, col_detail = st.columns([1, 2])
            with col_img:
                st.image(item["img"], caption=item["title"], use_column_width=True)
            with col_detail:
                st.markdown(f"### {item['title']}")
                st.markdown(f"**ราคา:** {item['price_text']}")
                st.write(item["details"])
                st.caption(f"📍 พิกัด: {item['location']} | ผู้ขาย: {item['seller']}")
        st.divider()

# =========================================================
# TAB อื่นๆ ครบถ้วนตามเดิม
# =========================================================
with tabs[2]:
    st.subheader("🛡️ ระบบชำระเงินปลอดภัยผ่านคนกลาง (Escrow)")
    st.info("สถานะ: รอผู้ซื้อโอนเงิน -> รอผู้ขายจัดส่ง")

with tabs[3]:
    st.subheader("➕ ลงประกาศใหม่")
    st.text_input("หัวข้อประกาศ")

with tabs[4]:
    st.subheader("🚗 จัดไฟแนนซ์รถยนต์")
with tabs[5]:
    st.subheader("🏦 เช็กวงเงินกู้บ้าน")
with tabs[6]:
    st.subheader("🎁 กิจกรรม & ส่วนลด")
with tabs[7]:
    st.subheader("🔴 ไลฟ์สดขายสินค้า")
with tabs[8]:
    st.subheader("💳 ชำระเงินค่าบริการแอดมิน")
with tabs[9]:
    st.subheader("📞 ติดต่อ / เรื่องร้องเรียน")
with tabs[10]:
    st.subheader("⚙️ สำหรับแอดมิน")
    if st.text_input("รหัสผ่านแอดมิน", type="password") == "1234":
        st.success("เข้าสู่ระบบแอดมินสำเร็จ")
