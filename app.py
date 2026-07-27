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

with tabs[0]:
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
        },
        {
            "id": 4,
            "title": "🏠 ขายคอนโด Plum Condo รังสิต เฟส 1 ชั้น 5 ตึก A",
            "category": "🏠 อสังหาริมทรัพย์",
            "price": 1250000,
            "price_text": "1,250,000 บาท (เหมาะสำหรับลงทุนปล่อยเช่า)",
            "details": "ห้องสวย สภาพใหม่ แถมเครื่องใช้ไฟฟ้าครบชุด ตู้เย็น แอร์ TV ติด ม.กรุงเทพ รังสิต",
            "location": "ปทุมธานี",
            "seller": "คุณนภา",
            "verified": False,
            "img": "https://via.placeholder.com/400x250.png?text=Plum+Condo+Rangsit"
        },
        {
            "id": 5,
            "title": "📦 iPhone 13 Pro 128GB สี Sierra Blue สภาพสวย 95%",
            "category": "📦 สินค้าทั่วไป",
            "price": 18500,
            "price_text": "18,500 บาท",
            "details": "เครื่องไทยการ์ดแท้ สุขภาพแบตเตอรี่ 88% แถมเคสแท้และสายชาร์จ นัดรับได้ที่โลตัสปทุมธานี",
            "location": "ปทุมธานี",
            "seller": "คุณกิตติ",
            "verified": True,
            "img": "https://via.placeholder.com/400x250.png?text=iPhone+13+Pro"
        }
    ]

    with st.expander("🎯 ตัวกรองการค้นหาขั้นสูง", expanded=True):
        col_f1, col_f2, col_f3, col_f4 = st.columns(4)
        with col_f1:
            search_kw = st.text_input("คีย์เวิร์ดค้นหา").strip().lower()
        with col_f2:
            search_cat = st.selectbox("หมวดหมู่สินค้า", ["ทั้งหมด", "🚗 รถยนต์มือสอง", "🏠 อสังหาริมทรัพย์", "📦 สินค้าทั่วไป"])
        with col_f3:
            search_price = st.selectbox("ช่วงราคา", ["ทั้งหมด", "ต่ำกว่า 100,000 บาท", "100,000 - 500,000 บาท", "500,000 - 2,000,000 บาท", "2,000,000 บาทขึ้นไป"])
        with col_f4:
            search_province = st.selectbox("จังหวัด/พื้นที่", ["ทั้งหมด", "ปทุมธานี", "กรุงเทพฯ และปริมณฑล", "ต่างจังหวัด"])

    filtered_listings = []
    for item in mock_listings:
        match = True
        if search_kw and (search_kw not in item["title"].lower() and search_kw not in item["details"].lower()):
            match = False
        if search_cat != "ทั้งหมด" and item["category"] != search_cat:
            match = False
        if search_province != "ทั้งหมด" and item["location"] != search_province:
            match = False
        if search_price == "ต่ำกว่า 100,000 บาท" and item["price"] >= 100000:
            match = False
        elif search_price == "100,000 - 500,000 บาท" and not (100000 <= item["price"] <= 500000):
            match = False
        elif search_price == "500,000 - 2,000,000 บาท" and not (500000 <= item["price"] <= 2000000):
            match = False
        elif search_price == "2,000,000 บาทขึ้นไป" and item["price"] < 2000000:
            match = False

        if match:
            filtered_listings.append(item)

    st.divider()
    st.subheader(f"📌 ผลการค้นหาพบทั้งหมด {len(filtered_listings)} รายการ")
    
    for idx, item in enumerate(filtered_listings):
        with st.container():
            col_img, col_detail = st.columns([1, 2])
            with col_img:
                st.image(item["img"], caption=item["title"], use_column_width=True)
            with col_detail:
                v_badge = " ✨ (Verified)" if item["verified"] else ""
                st.markdown(f"### {item['title']}{v_badge}")
                st.markdown(f"**ราคา:** {item['price_text']}")
                st.write(item["details"])
                st.caption(f"📍 พิกัด: {item['location']} | ผู้ขาย: {item['seller']}")
                
                col_act1, col_act2, col_act3 = st.columns(3)
                col_act1.button("📞 โทรด่วน", key=f"call_{idx}")
                col_act2.button("💬 ทัก LINE", key=f"line_{idx}")
                col_act3.button("🛡️ ซื้อคนกลาง", key=f"escrow_{idx}")
        st.divider()

with tabs[1]:
    st.subheader("🛡️ ระบบชำระเงินปลอดภัยผ่านคนกลาง (Escrow)")
    col_esc1, col_esc2 = st.columns([1, 1])
    with col_esc1:
        with st.form("escrow_buy_form"):
            st.text_input("ชื่อสินค้า")
            st.text_input("ชื่อผู้ขาย")
            st.number_input("ราคาสินค้า (บาท)", min_value=100, step=100)
            st.text_input("ชื่อผู้ซื้อ")
            st.form_submit_button("💳 สร้างรายการชำระเงิน")
    with col_esc2:
        if os.path.exists("qr_code.jpg"):
            st.image("qr_code.jpg", width=260)
        elif os.path.exists("qr_code.png"):
            st.image("qr_code.png", width=260)
        st.info("สถานะ: รอผู้ซื้อโอนเงิน -> รอผู้ขายจัดส่ง")
        st.button("✅ กดยืนยันได้รับสินค้าแล้ว")

with tabs[2]:
    st.subheader("➕ ลงประกาศใหม่")
    with st.form("listing_form"):
        st.text_input("หัวข้อประกาศ")
        st.number_input("ราคาขาย", min_value=0)
        st.text_area("รายละเอียด")
        st.form_submit_button("ส่งข้อมูลลงประกาศ")

with tabs[3]:
    st.subheader("🚗 จัดไฟแนนซ์รถยนต์")

with tabs[4]:
    st.subheader("🚘 คำนวณค่างวดผ่อนรถ")

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
