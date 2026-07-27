import streamlit as st
import os

# ตั้งค่าหน้าตาของเว็บ
st.set_page_config(page_title="ศูนย์กลางลงประกาศบ้าน อสังหาฯ & รถยนต์มือสอง", page_icon="🏠", layout="wide")

# Header & โลโก้เว็บไซต์
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
    st.write("แพลตฟอร์มซื้อ-ขายครบวงจร พร้อมระบบชำระเงินคนกลาง (Escrow) เพิ่มความปลอดภัย 100%")

# ---------------------------------------------------------
# 📢 พื้นที่แสดงแบนเนอร์โฆษณา
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
    st.success("🛡️ **ชำระเงินผ่านระบบกลาง (Escrow)**\n\nการันตีได้รับของชัวร์ ไม่โดนโกง เงินไม่ถึงมือผู้ขายจนกว่าจะได้รับของ")

st.markdown("---")

# ---------------------------------------------------------
# 📌 เมนูหลักของเว็บไซต์ (เพิ่มระบบ Escrow)
# ---------------------------------------------------------
tabs = st.tabs([
    "📌 รายการประกาศทั้งหมด", 
    "🛒 ชำระเงินผ่านระบบกลาง (Escrow)",
    "➕ ลงประกาศใหม่", 
    "🚗 ธุรกรรม & จัดไฟแนนซ์รถยนต์",
    "🚘 คำนวณค่างวดผ่อนรถ",
    "🏦 เช็กวงเงินกู้บ้าน",
    "🎁 กิจกรรม & ส่วนลด",
    "🔴 ไลฟ์สดขายสินค้า (Live)",
    "💳 ชำระเงินค่าแอดมิน / VIP", 
    "📞 ติดต่อ / เรื่องร้องเรียน",
    "⚙️ สำหรับแอดมิน"
])

# --- TAB 1: รายการประกาศ ---
with tabs[0]:
    st.subheader("รายการประกาศล่าสุด")
    st.info("ยังไม่มีรายการประกาศในระบบ สามารถทดลองลงประกาศได้ที่แท็บ 'ลงประกาศใหม่'")

# --- TAB 2: ระบบชำระเงินผ่านคนกลาง สไตล์ Lalamove/Shopee (ฟีเจอร์ใหม่) ---
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

# --- TAB 3: ลงประกาศใหม่ ---
with tabs[2]:
    st.subheader("กรอกข้อมูลลงประกาศ")
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

# --- TAB 4: ธุรกรรม & จัดไฟแนนซ์รถยนต์ ---
with tabs[3]:
    st.subheader("🚗 บริการธุรกรรมทางการเงินสำหรับรถยนต์มือสองครบวงจร")
    col_fin1, col_fin2 = st.columns([1, 1])
    with col_fin1:
        st.markdown("""
        #### 📋 บริการของเรา:
        * 🔑 **จัดไฟแนนซ์รถมือสอง:** ผ่อนสบายสูงสุด 84 เดือน ไม่ต้องมีผู้ค้ำประกัน
        * 🔄 **รีไฟแนนซ์ / ปิดบัญชี:** ย้ายไฟแนนซ์เดิม ลดดอกเบี้ย ดึงเงินสดออกมาใช้
        * 📑 **จำนำเล่มทะเบียน:** มีรถใช้ มีเงินใช้อนุมัติไวภายใน 1 วัน
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

# --- TAB 5: คำนวณค่างวดผ่อนรถยนต์มือสอง ---
with tabs[4]:
    st.subheader("🚘 เครื่องมือคำนวณค่างวดผ่อนชำระ รถยนต์มือสอง")
    col_cc1, col_cc2 = st.columns([1, 1])
    with col_cc1:
        car_price = st.number_input("ราคารถยนต์ (บาท)", min_value=50000, value=250000, step=10000)
        down_payment = st.number_input("เงินดาวน์ (บาท)", min_value=0, value=20000, step=5000)
        interest_car = st.slider("อัตราดอกเบี้ยคงที่ต่อปี (%)", min_value=2.0, max_value=12.0, value=4.5, step=0.25)
        terms_month = st.selectbox("จำนวนงวดที่ต้องการผ่อน (เดือน)", [24, 36, 48, 60, 72, 84])
    with col_cc2:
        finance_amount = max(0, car_price - down_payment)
        years = terms_month / 12
        total_interest = finance_amount * (interest_car / 100) * years
        total_loan = finance_amount + total_interest
        monthly_installment = total_loan / terms_month
        vat_monthly = monthly_installment * 1.07
        st.metric(label="ยอดจัดไฟแนนซ์", value=f"{finance_amount:,.0f} บาท")
        st.metric(label="ค่างวดผ่อนประมาณ/เดือน (รวม VAT 7%)", value=f"{vat_monthly:,.0f} บาท")

# --- TAB 6: เช็กวงเงินกู้บ้าน ---
with tabs[5]:
    st.subheader("🏦 เครื่องมือคำนวณวงเงินกู้ & ประเมินสินเชื่อบ้าน/อสังหาฯ")
    col_loan1, col_loan2 = st.columns([1, 1])
    with col_loan1:
        salary = st.number_input("เงินเดือน / รายได้สุทธิต่อเดือน (บาท)", min_value=10000, value=30000, step=1000)
        debt = st.number_input("ภาระหนี้เดิมต่อเดือน (บาท)", min_value=0, value=0, step=500)
        loan_years = st.selectbox("ระยะเวลาที่ต้องการกู้ (ปี)", [10, 15, 20, 25, 30])
    with col_loan2:
        net_income = max(0, salary - debt)
        max_monthly_pay = net_income * 0.40
        estimated_loan = (max_monthly_pay / 7000) * 1000000
        st.metric(label="ค่างวดที่ผ่อนได้สูงสุด / เดือน", value=f"{max_monthly_pay:,.0f} บาท")
        st.metric(label="ประมาณการวงเงินกู้สูงสุด", value=f"{estimated_loan:,.0f} บาท")

# --- TAB 7: กิจกรรม & ส่วนลด ---
with tabs[6]:
    st.subheader("🎁 กิจกรรมโปรโมชั่น & โค้ดส่วนลดพิเศษ")
    with st.form("discount_form"):
        promo_code = st.text_input("กรอกรหัสส่วนลด / โค้ดกิจกรรม")
        submit_code = st.form_submit_button("ยืนยันรับส่วนลด")
        if submit_code:
            if promo_code.upper() == "NEWYEAR50":
                st.success("🎉 ยินดีด้วย! คุณได้รับส่วนลด 50% สำหรับการชำระเงินอัปเกรดพรีเมียม")

# --- TAB 8: ไลฟ์สดขายสินค้า ---
with tabs[7]:
    st.subheader("🔴 ห้องไลฟ์สด ซื้อ-ขายสินค้าออนไลน์")
    col_live1, col_live2 = st.columns([2, 1])
    with col_live1:
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    with col_live2:
        with st.form("live_order_form"):
            item_code = st.text_input("รหัสสินค้าในไลฟ์ (เช่น C01)")
            customer_name = st.text_input("ชื่อของคุณ")
            customer_contact = st.text_input("เบอร์โทร / LINE ID")
            st.form_submit_button("🛒 กด F/CF จองสินค้าในไลฟ์")

# --- TAB 9: ชำระเงินค่าบริการแอดมิน ---
with tabs[8]:
    st.subheader("💳 ชำระเงินค่าบริการแอดมิน / อัปเกรดพรีเมียม")
    col1, col2 = st.columns([1, 1])
    with col1:
        package = st.radio("เลือกแพ็กเกจที่ต้องการ:", ["ติดป้ายพรีเมียม 7 วัน (50 บาท)", "ติดป้ายพรีเมียม 30 วัน (150 บาท)", "ดันโพสต์ให้อยู่หน้าแรก 1 วัน (20 บาท)"])
        amount = 50 if "50" in package else (150 if "150" in package else 20)
  