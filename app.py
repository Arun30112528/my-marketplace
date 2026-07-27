import streamlit as st
import os

# ตั้งค่าหน้าตาของเว็บ
st.set_page_config(page_title="ศูนย์กลางลงประกาศบ้าน อสังหาฯ & รถยนต์มือสอง", page_icon="🏠", layout="wide")

# ---------------------------------------------------------
# 🎨 ส่วนที่ 0: Header & โลโก้เว็บไซต์
# ---------------------------------------------------------
col_logo, col_header = st.columns([1, 5])

with col_logo:
    # ตรวจสอบและแสดงรูปโลโก้ไอคอนเว็บไซต์
    if os.path.exists("logo.png"):
        st.image("logo.png", width=120)
    elif os.path.exists("logo.jpg"):
        st.image("logo.jpg", width=120)
    else:
        st.title("🏠")

with col_header:
    st.title("ศูนย์กลางลงประกาศบ้าน อสังหาฯ & รถยนต์มือสอง")
    st.write("แพลตฟอร์มซื้อ-ขายครบวงจร พร้อมระบบจัดไฟแนนซ์ เช็กวงเงินกู้ ไลฟ์สด และกิจกรรมส่วนลด")

# ---------------------------------------------------------
# 📢 ส่วนที่ 1: พื้นที่แสดงแบนเนอร์โฆษณา
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
    st.success("🚗 **รับจัดไฟแนนซ์ / ฝากขายรถมือสอง & บ้าน!**\n\nอนุมัติไว ดอกเบี้ยพิเศษ บริการถึงที่")

st.markdown("---")

# ---------------------------------------------------------
# 📌 ส่วนที่ 2: เมนูหลักของเว็บไซต์
# ---------------------------------------------------------
tabs = st.tabs([
    "📌 รายการประกาศทั้งหมด", 
    "➕ ลงประกาศใหม่", 
    "🚗 ธุรกรรม & จัดไฟแนนซ์รถยนต์",
    "🚘 คำนวณค่างวดผ่อนรถ",
    "🏦 เช็กวงเงินกู้บ้าน",
    "🎁 กิจกรรม & ส่วนลด",
    "🔴 ไลฟ์สดขายสินค้า (Live)",
    "💳 ชำระเงิน / พรีเมียม", 
    "👑 สมัครนายหน้า/เต็นท์รถ VIP",
    "📞 ติดต่อ / เรื่องร้องเรียน",
    "⚙️ สำหรับแอดมิน"
])

# --- TAB 1: รายการประกาศ ---
with tabs[0]:
    st.subheader("รายการประกาศล่าสุด")
    st.info("ยังไม่มีรายการประกาศในระบบ สามารถทดลองลงประกาศได้ที่แท็บ 'ลงประกาศใหม่'")

# --- TAB 2: ลงประกาศใหม่ ---
with tabs[1]:
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

# --- TAB 3: ธุรกรรม & จัดไฟแนนซ์รถยนต์ ---
with tabs[2]:
    st.subheader("🚗 บริการธุรกรรมทางการเงินสำหรับรถยนต์มือสองครบวงจร")
    st.write("จัดไฟแนนซ์ซื้อรถมือสอง / รีไฟแนนซ์ย้ายไฟแนนซ์ / จำนำเล่มทะเบียนรับเงินสด")
    
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
        st.markdown("#### 📝 ยื่นเรื่องขอปรึกษา / ยื่นกู้จัดไฟแนนซ์รถ")
        with st.form("car_finance_form"):
            fin_type = st.selectbox("เลือกบริการที่ต้องการ", ["จัดไฟแนนซ์ซื้อรถมือสอง", "รีไฟแนนซ์ / ย้ายไฟแนนซ์", "จำนำเล่มทะเบียน (ยืมเงินสด)", "ประเมินราคากลางรถยนต์"])
            car_info = st.text_input("ยี่ห้อ / รุ่น / ปีรถ (เช่น Nissan Almera ปี 2014)")
            request_amount = st.number_input("วงเงินที่ต้องการกู้ (บาท)", min_value=10000, step=10000)
            user_name = st.text_input("ชื่อ-นามสกุล ผู้ขอปรึกษา")
            user_tel = st.text_input("เบอร์โทรศัพท์ติดต่อกลับ")
            
            submit_fin = st.form_submit_button("📩 ยื่นเรื่องขอประเมินวงเงินฟรี")
            if submit_fin:
                st.success("🎉 ยื่นข้อมูลเรียบร้อยแล้ว! เจ้าหน้าที่ฝ่ายสินเชื่อรถยนต์จะติดต่อกลับโดยด่วนครับ")

# --- TAB 4: คำนวณค่างวดผ่อนรถยนต์มือสอง ---
with tabs[3]:
    st.subheader("🚘 เครื่องมือคำนวณค่างวดผ่อนชำระ รถยนต์มือสอง")
    st.write("คำนวณค่างวดผ่อนต่อเดือนแบบประมาณการตามราคารถและเงินดาวน์")
    
    col_cc1, col_cc2 = st.columns([1, 1])
    
    with col_cc1:
        car_price = st.number_input("ราคารถยนต์ (บาท)", min_value=50000, value=250000, step=10000)
        down_payment = st.number_input("เงินดาวน์ (บาท) [ใส่ 0 หากต้องการฟรีดาวน์]", min_value=0, value=20000, step=5000)
        interest_car = st.slider("อัตราดอกเบี้ยคงที่ต่อปี (%)", min_value=2.0, max_value=12.0, value=4.5, step=0.25)
        terms_month = st.selectbox("จำนวนงวดที่ต้องการผ่อน (เดือน)", [24, 36, 48, 60, 72, 84])

    with col_cc2:
        finance_amount = max(0, car_price - down_payment)
        years = terms_month / 12
        total_interest = finance_amount * (interest_car / 100) * years
        total_loan = finance_amount + total_interest
        monthly_installment = total_loan / terms_month
        vat_monthly = monthly_installment * 1.07
        
        st.markdown("#### 📊 ผลการคำนวณประมาณการค่างวด")
        st.metric(label="ยอดจัดไฟแนนซ์", value=f"{finance_amount:,.0f} บาท")
        st.metric(label="ค่างวดผ่อนประมาณ/เดือน (รวม VAT 7%)", value=f"{vat_monthly:,.0f} บาท")

# --- TAB 5: เช็กวงเงินกู้บ้าน ---
with tabs[4]:
    st.subheader("🏦 เครื่องมือคำนวณวงเงินกู้ & ประเมินสินเชื่อบ้าน/อสังหาฯ")
    col_loan1, col_loan2 = st.columns([1, 1])
    
    with col_loan1:
        salary = st.number_input("เงินเดือน / รายได้สุทธิต่อเดือน (บาท)", min_value=10000, value=30000, step=1000)
        debt = st.number_input("ภาระหนี้เดิมต่อเดือน (เช่น ผ่อนรถ, บัตรเครดิต)", min_value=0, value=0, step=500)
        loan_years = st.selectbox("ระยะเวลาที่ต้องการกู้ (ปี)", [10, 15, 20, 25, 30])
        
    with col_loan2:
        net_income = max(0, salary - debt)
        max_monthly_pay = net_income * 0.40
        estimated_loan = (max_monthly_pay / 7000) * 1000000
        
        st.markdown("#### 💡 ผลการประเมินวงเงินกู้เบื้องต้น")
        st.metric(label="ค่างวดที่สามารถผ่อนได้สูงสุด / เดือน", value=f"{max_monthly_pay:,.0f} บาท")
        st.metric(label="ประมาณการวงเงินกู้สูงสุด", value=f"{estimated_loan:,.0f} บาท")

# --- TAB 6: กิจกรรม & ส่วนลด ---
with tabs[5]:
    st.subheader("🎁 กิจกรรมโปรโมชั่น & โค้ดส่วนลดพิเศษ")
    col_promo1, col_promo2 = st.columns([1, 1])
    
    with col_promo1:
        st.markdown("""
        #### 🔥 โปรโมชั่นประจำเดือน
        * 🏷️ **แจกโค้ดส่วนลด:** กรอกโค้ด **`NEWYEAR50`** ลดทันที 50% สำหรับการดันโพสต์ครั้งแรก
        * 🎟️ **กิจกรรมแจกป้ายพรีเมียมฟรี:** ร่วมเล่นกิจกรรมกู้ซื้อบ้านหรือลงประกาศครบ 3 รายการ รับสิทธิ์ดันโพสต์ฟรี 7 วัน
        """)

    with col_promo2:
        st.markdown("#### 🎟️ นำโค้ดส่วนลดมาใช้ที่นี่")
        with st.form("discount_form"):
            promo_code = st.text_input("กรอกรหัสส่วนลด / โค้ดกิจกรรม")
            submit_code = st.form_submit_button("ยืนยันรับส่วนลด")
            if submit_code:
                if promo_code.upper() == "NEWYEAR50":
                    st.success("🎉 ยินดีด้วย! คุณได้รับส่วนลด 50% สำหรับการชำระเงินอัปเกรดพรีเมียม")
                elif promo_code != "":
                    st.error("❌ โค้ดส่วนลดไม่ถูกต้อง หรือหมดอายุแล้ว")

# --- TAB 7: ไลฟ์สดขายสินค้า ---
with tabs[6]:
    st.subheader("🔴 ห้องไลฟ์สด ซื้อ-ขายสินค้าออนไลน์")
    col_live1, col_live2 = st.columns([2, 1])
    
    with col_live1:
        st.markdown("##### 📹 สตรีมมิ่งไลฟ์สดขณะนี้")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    with col_live2:
        st.markdown("##### 💬 สั่งซื้อสินค้า / ปักหมุดในไลฟ์")
        with st.form("live_order_form"):
            item_code = st.text_input("รหัสสินค้า / รหัสรถในไลฟ์ (เช่น C01)")
            customer_name = st.text_input("ชื่อของคุณ")
            customer_contact = st.text_input("เบอร์โทร / LINE ID")
            st.form_submit_button("🛒 กด F/CF จองสินค้าในไลฟ์")

# --- TAB 8: ชำระเงิน ---
with tabs[7]:
    st.subheader("💳 ชำระเงินอัปเกรดประกาศพรีเมียม")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        package = st.radio(
            "เลือกแพ็กเกจที่ต้องการ:",
            ["ติดป้ายพรีเมียม 7 วัน (50 บาท)", "ติดป้ายพรีเมียม 30 วัน (150 บาท)", "ดันโพสต์ให้อยู่หน้าแรก 1 วัน (20 บาท)"]
        )
        amount = 50 if "50" in package else (150 if "150" in package else 20)
        st.info(f"💰 ยอดชำระทั้งสิ้น: **{amount} บาท**")

    with col2:
        st.markdown("### **สแกนชำระเงินผ่าน PromptPay**")
        if os.path.exists("qr_code.jpg"):
            st.image("qr_code.jpg", caption="สแกน QR Code ด้วยแอปธนาคารเพื่อชำระเงิน", width=280)
        elif os.path.exists("qr_code.png"):
            st.image("qr_code.png", caption="สแกน QR Code ด้วยแอปธนาคารเพื่อชำระเงิน", width=280)
        else:
            st.warning("⚠️ กรุณาอัปโหลดไฟล์รูป 'qr_code' ขึ้น GitHub เพื่อแสดง QR Code ชำระเงิน")

# --- TAB 9: สมัครนายห