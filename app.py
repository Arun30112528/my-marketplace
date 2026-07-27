import streamlit as st
import os

# ตั้งค่าหน้าตาของเว็บ
st.set_page_config(page_title="ศูนย์กลางลงประกาศบ้าน อสังหาฯ & รถยนต์มือสอง", page_icon="🏠", layout="wide")

# ---------------------------------------------------------
# 🎨 ส่วนที่ 0: Header & โลโก้เว็บไซต์
# ---------------------------------------------------------
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

# ---------------------------------------------------------
# 📢 ส่วนที่ 1: แบนเนอร์สปอนเซอร์ & สัญลักษณ์ความปลอดภัย
# ---------------------------------------------------------
st.markdown("---")
col_banner1, col_banner2 = st.columns([3, 1])

with col_banner1:
    if os.path.exists("banner.jpg") or os.path.exists("banner.png"):
        banner_file = "banner.jpg" if os.path.exists("banner.jpg") else "banner.png"
        st.image(banner_file, use_column_width=True)
    else:
        st.info("📢 **พื้นที่สำหรับติดแบนเนอร์โฆษณา** (สนใจลงโฆษณาเต็นท์รถ/นายหน้า ติดต่อแอดมิน โทร/LINE: 08X-XXX-XXXX)")

with col_banner2:
    st.success("🛡️ **ปลอดภัย 100%**\n\nผู้ขายผ่านการยืนยันตัวตน (Verified Seller) + ระบบชำระเงินผ่านคนกลาง Escrow")

st.markdown("---")

# ---------------------------------------------------------
# 📌 ส่วนที่ 2: เมนูหลักของเว็บไซต์
# ---------------------------------------------------------
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

# =========================================================
# TAB 1: ค้นหาประกาศทั้งหมด (Mock Data Engine)
# =========================================================
with tabs[0]:
    st.subheader("🔍 ค้นหาบ้าน คอนโด รถยนต์ และสินค้ามือสอง")
    
    # ฐานข้อมูลจำลอง (Mock Data Database)
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

    # --- แถบตัวกรองการค้นหา (Search Filter) ---
    with st.expander("🎯 ตัวกรองการค้นหาขั้นสูง (คลิกเพื่อเปิด/ปิด)", expanded=True):
        col_f1, col_f2, col_f3, col_f4 = st.columns(4)
        with col_f1:
            search_kw = st.text_input("คีย์เวิร์ดค้นหา (เช่น Toyota, บ้าน, คอนโด)").strip().lower()
        with col_f2:
            search_cat = st.selectbox("หมวดหมู่สินค้า", ["ทั้งหมด", "🚗 รถยนต์มือสอง", "🏠 อสังหาริมทรัพย์", "📦 สินค้าทั่วไป"])
        with col_f3:
            search_price = st.selectbox("ช่วงราคา", ["ทั้งหมด", "ต่ำกว่า 100,000 บาท", "100,000 - 500,000 บาท", "500,000 - 2,000,000 บาท", "2,000,000 บาทขึ้นไป"])
        with col_f4:
            search_province = st.selectbox("จังหวัด/พื้นที่", ["ทั้งหมด", "ปทุมธานี", "กรุงเทพฯ และปริมณฑล", "ต่างจังหวัด"])

    # ประมวลผลการกรองข้อมูล
    filtered_listings = []
    for item in mock_listings:
        match = True
        
        # กรองคีย์เวิร์ด
        if search_kw and (search_kw not in item["title"].lower() and search_kw not in item["details"].lower()):
            match = False
            
        # กรองหมวดหมู่
        if search_cat != "ทั้งหมด" and item["category"] != search_cat:
            match = False
            
        # กรองจังหวัด
        if search_province != "ทั้งหมด" and item["location"] != search_province:
            match = False
            
        # กรองราคา
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
    
    if len(filtered_listings) == 0:
        st.warning("⚠️ ไม่พบรายการประกาศที่ตรงกับเงื่อนไขการค้นหา กรุณาลองปรับเปลี่ยนตัวกรองครับ")
    else:
        for idx, item in enumerate(filtered_listings):
            with st.container():
                col_img, col_detail = st.columns([1, 2])
                with col_img:
                    st.image(item["img"], caption=item["title"], use_column_width=True)
                with col_detail:
                    v_badge = " ✨ *(Verified Seller)*" if item["verified"] else ""
                    st.markdown(f"### {item['title']}{v_badge}")
                    st.markdown(f"**ราคา:** {item['price_text']}")
                    st.write(item["details"])
                    st.caption(f"📍 พิกัด: {item['location']} | ผู้ขาย: {item['seller']}")
                    
                    col_act1, col_act2, col_act3 = st.columns(3)
                    col_act1.button("📞 โทรหาผู้ขายด่วน", key=f"call_{idx}")
                    col_act2.button("💬 ทัก LINE ผู้ขาย", key=f"line_{idx}")
                    col_act3.button("🛡️ ซื้อผ่านระบบคนกลาง", key=f"escrow_{idx}")
            st.divider()

# =========================================================
# TAB 2: ระบบชำระเงินผ่านคนกลาง (Escrow)
# =========================================================
with tabs[1]:
    st.subheader("🛡️ ระบบชำระเงินปลอดภัยผ่านคนกลาง (Escrow Payment System)")
    st.write("ซื้อขายมั่นใจ 100% ระบบจะกักเงินไว้จนกว่าผู้ซื้อจะได้รับสินค้าถูกต้อง จึงจะโอนเงินให้ผู้ขาย")
    
    col_esc1, col_esc2 = st.columns([1, 1])
    with col_esc1:
        st.markdown("#### 1️⃣ กรอกรายการสั่งซื้อ & โอนเงินเข้าคนกลาง")
        with st.form("escrow_buy_form"):
            order_item = st.text_input("ชื่อสินค้า / รหัสทรัพย์ที่ต้องการซื้อ")
            seller_name = st.text_input("ชื่อผู้ขาย / ชื่อร้านค้า")
            item_price = st.number_input("ราคาสินค้า (บาท)", min_value=100, step=100)
            buyer_name = st.text_input("ชื่อ-นามสกุล ผู้ซื้อ")
            buyer_tel = st.text_input("เบอร์โทรศัพท์ผู้ซื้อ")
            
            submit_buy = st.form_submit_button("💳 สร้างรายการชำระเงินคนกลาง")
            if submit_buy:
                st.success(f"🎉 สร้างคำสั่งซื้อเรียบร้อย! กรุณาสแกนจ่ายเงินจำนวน {item_price:,.2f} บาท เข้าบัญชีคนกลางด้านขวา")

    with col_esc2:
        st.markdown("#### 2️⃣ สแกนโอนเงินเข้าบัญชีกลางระบบ")
        if os.path.exists("qr_code.jpg"):
            st.image("qr_code.jpg", caption="สแกนโอนเงินชำระเข้าบัญชีคนกลาง (ระบบพักเงินไว้ปลอดภัย)", width=260)
        elif os.path.exists("qr_code.png"):
            st.image("qr_code.png", caption="สแกนโอนเงินชำระเข้าบัญชีคนกลาง (ระบบพักเงินไว้ปลอดภัย)", width=260)
            
        st.divider()
        st.markdown("#### 3️⃣ สถานะคำสั่งซื้อ & กดยืนยันรับของ")
        st.info("📌 **สถานะปัจจุบัน:** รอผู้ซื้อโอนเงิน ➔ รอผู้ขายจัดส่ง ➔ **[กดปุ่มด้านล่างเมื่อได้รับของแล
