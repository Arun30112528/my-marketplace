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
# TAB 1: ค้นหาประกาศทั้งหมด
# =========================================================
with tabs[0]:
    st.subheader("🔍 ค้นหาบ้าน คอนโด รถยนต์ และสินค้ามือสอง")
    
    with st.expander("🎯 ตัวกรองการค้นหาขั้นสูง (คลิกเพื่อเปิด/ปิด)", expanded=True):
        col_f1, col_f2, col_f3, col_f4 = st.columns(4)
        with col_f1:
            search_kw = st.text_input("คีย์เวิร์ดค้นหา (เช่น Nissan, คอนโด, ปทุมธานี)")
        with col_f2:
            search_cat = st.selectbox("หมวดหมู่สินค้า", ["ทั้งหมด", "🚗 รถยนต์มือสอง", "🏠 อสังหาริมทรัพย์", "📦 สินค้าทั่วไป"])
        with col_f3:
            search_price = st.selectbox("ช่วงราคา", ["ทั้งหมด", "ต่ำกว่า 100,000 บาท", "100,000 - 500,000 บาท", "500,000 - 2,000,000 บาท", "2,000,000 บาทขึ้นไป"])
        with col_f4:
            search_province = st.selectbox("จังหวัด/พื้นที่", ["ทั้งหมด", "ปทุมธานี", "กรุงเทพฯ และปริมณฑล", "ต่างจังหวัด"])

    st.divider()
    st.subheader("📌 ประกาศแนะนำ / ประกาศล่าสุด")
    
    # ตัวอย่างประกาศที่ 1 (รถยนต์)
    with st.container():
        col_img1, col_detail1 = st.columns([1, 2])
        with col_img1:
            st.image("https://via.placeholder.com/400x250.png?text=Nissan+Almera+2014", caption="Nissan Almera 1.2 E ปี 2014", use_column_width=True)
        with col_detail1:
            st.markdown("### 🚗 **Nissan Almera 1.2 E ปี 2014 (เกียร์ออโต้)**")
            st.markdown("**ราคา: 189,000 บาท** (ฟรีดาวน์ / ผ่อนประมาณ 3,xxx บาท/เดือน)")
            st.write("สภาพดีพร้อมใช้งาน เครื่องยนต์ดีเยี่ยม รถบ้านมือเดียว เลขไมล์น้อย ตรวจเช็กเล่มทะเบียนเรียบร้อยแล้ว")
            st.caption("📍 พิกัด: อ.เมือง จ.ปทุมธานี | ผู้ขาย: คุณอรัญ (นายหน้า Verified)")
            
            col_act1, col_act2, col_act3 = st.columns(3)
            col_act1.button("📞 โทรหาผู้ขายด่วน", key="call1")
            col_act2.button("💬 ทัก LINE ผู้ขาย", key="line1")
            col_act3.button("🛡️ ซื้อผ่านระบบคนกลาง", key="escrow1")

    st.divider()

    # ตัวอย่างประกาศที่ 2 (บ้าน)
    with st.container():
        col_img2, col_detail2 = st.columns([1, 2])
        with col_img2:
            st.image("https://via.placeholder.com/400x250.png?text=Townhome+Pathumthani", caption="ทาวน์โฮม 2 ชั้น ปทุมธานี", use_column_width=True)
        with col_detail2:
            st.markdown("### 🏠 **ขายทาวน์โฮม 2 ชั้น 3 ห้องนอน 2 ห้องน้ำ ใกล้โลตัสปทุมธานี**")
            st.markdown("**ราคา: 1,950,000 บาท** (กู้ได้เต็ม 100%)")
            st.write("เนื้อที่ 20 ตร.วา ต่อเติมครัวไทยและโรงจอดรถเรียบร้อย ทำเลดีเดินทางสะดวก ใกล้ตลาดและสถานศึกษา")
            st.caption("📍 พิกัด: อ.เมือง จ.ปทุมธานี | ผู้ขาย: คุณอรัญ")
            
            col_act4, col_act5, col_act6 = st.columns(3)
            col_act4.button("📞 โทรหาผู้ขายด่วน", key="call2")
            col_act5.button("💬 ทัก LINE ผู้ขาย", key="line2")
            col_act6.button("🏦 เช็กวงเงินกู้บ้านนี้", key="loan2")

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
        st.info("📌 **สถานะปัจจุบัน:** รอผู้ซื้อโอนเงิน ➔ รอผู้ขายจัดส่ง ➔ **[กดปุ่มด้านล่างเมื่อได้รับของแล้ว]**")
        
        if st.button("✅ กดยืนยัน 'ได้รับสินค้าถูกต้อง' (เพื่อปล่อยเงินให้ผู้ขาย)"):
            st.balloons()
            st.success("🎉 ยืนยันสำเร็จ! ระบบได้ทำการโอนเงินตรงเข้าบัญชีผู้ขายเรียบร้อยแล้ว ขอบคุณที่ใช้บริการครับ")

# =========================================================
# TAB 3: ลงประกาศใหม่
# =========================================================
with tabs[2]:
    st.subheader("กรอกข้อมูลลงประกาศ (ฟรี 100%)")
    category = st.selectbox("เลือกหมวดหมู่ที่ต้องการลงประกาศ", ["🚗 รถยนต์มือสอง / ยานพาหนะ", "🏠 อสังหาริมทรัพย์ (บ้าน/คอนโด/ที่ดิน)", "📦 สินค้าทั่วไปมือสอง"])
    
    with st.form("listing_form"):
        title = st.text_input("หัวข้อประกาศ (เช่น ขาย Nissan Almera ปี 2014 / ขายบ้านเดี่ยว 2 ชั้น)")
        if "รถยนต์" in category:
            col_car1, col_car2, col_car3 = st.columns(3)
            with col_car1:
                car_brand = st.text_input("ยี่ห้อ / รุ่น (เช่น Nissan Almera, Toyota Vios)")
            with col_car2:
                car_year = st.number_input("ปี ค.ศ. (เช่น 2014)", min_value=1990, max_value=2026, value=2014)
            with col_car3:
                car_mileage = st.number_input("ระยะทางวิ่ง / เลขไมล์ (กม.)", min_value=0, step=5000)
            car_gear = st.radio("ระบบเกียร์", ["เกียร์ออโต้ (AT)", "เกียร์ธรรมดา (MT)"], horizontal=True)

        price_item = st.number_input("ราคาขาย (บาท)", min_value=0, step=1000)
        details = st.text_area("รายละเอียดเพิ่มเติม / สภาพสินค้า")
        contact_name = st.text_input("ชื่อผู้ติดต่อ")
        phone = st.text_input("เบอร์โทรศัพท์ / LINE ID")
        
        submitted = st.form_submit_button("ส่งข้อมูลลงประกาศ")
        if submitted:
            st.success("🎉 บันทึกข้อมูลประกาศเรียบร้อยแล้ว!")

# =========================================================
# TAB 4: ธุรกรรม & จัดไฟแนนซ์รถยนต์
# =========================================================
with tabs[3]:
    st.subheader("🚗 บริการธุรกรรมทางการเงินสำหรับรถยนต์มือสองครบวงจร")
    col_fin1, col_fin2 = st.columns([1, 1])
    with col_fin1:
        st.markdown("""
        #### 📋 บริการของเรา:
        * 🔑 **จัดไฟแนนซ์รถมือสอง:** ผ่อนสบายสูงสุด 84 เดือน ไม่ต้องมีผู้ค้ำประกัน
        * 🔄 **รีไฟแนนซ์ / ปิดบัญชี:** ย้ายไฟแนนซ์เดิม ลดดอกเบี้ย ดึงเงินสดออกมาใช้
        * 📑 **จำนำเล่มทะเบียน:** มีรถใช้ มีเงินใชอนุมัติไวภายใน 1 วัน
        """)
        st.success("✅ ประเมินยอดจัดฟรี! บริการเซ็นสัญญาถึงบ้านทั่วประเทศ")

    with col_fin2:
        with st.form("car_finance_form"):
            fin_type = st.selectbox("เลือกบริการที่ต้องการ", ["จัดไฟแนนซ์ซื้อรถมือสอง", "รีไฟแนนซ์ / ย้ายไฟแนนซ์", "จำนำเล่มทะเบียน (ยืมเงินสด)", "ประเมินราคากลางรถยนต์"])
            car_info = st.text_input("ยี่ห้อ / รุ่น / ปีรถ (เช่น Nissan Almera ปี 2014)")
            request_amount = st.number_input("วงเงินที่ต้องการกู้ (บาท)", min_value=10000, step=10000)
            user_name = st.text_input("ชื่อ-นามสกุล ผู้ขอปรึกษา")
            user_tel = st.text_input("เบอร์โทรศัพท์ติดต่อกลับ")
            submit_fin = st.form_submit_button("📩 ยื่นเรื่องขอประเมินวงเงินฟรี")
            if submit_fin:
                st.success("🎉 ยื่นข้อมูลเรียบร้อยแล้ว! เจ้าหน้าที่ฝ่ายสินเชื่อจะติดต่อกลับโดยด่วนครับ")

# =========================================================
# TAB 5: คำนวณค่างวดผ่อนรถ
# ====================================
