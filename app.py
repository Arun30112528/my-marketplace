import streamlit as st
import time

# ตั้งค่าหน้าตาของเว็บ
st.set_page_config(page_title="ศูนย์กลางลงประกาศบ้าน & สินค้ามือสอง", page_icon="🏠", layout="wide")

st.title("🏠 ศูนย์กลางลงประกาศซื้อ-ขาย/เช่า บ้านและสินค้ามือสอง")
st.write("ลงประกาศง่ายๆ พร้อมระบบชำระเงินอัปเกรดประกาศพรีเมียม")

# แบ่งแท็บการทำงาน
tab1, tab2, tab3 = st.tabs(["📌 รายการประกาศทั้งหมด", "➕ ลงประกาศใหม่", "💎 ชำระเงิน / อัปเกรดพรีเมียม"])

with tab1:
    st.subheader("รายการประกาศล่าสุด")
    st.info("ยังไม่มีรายการประกาศในระบบ สามารถทดลองลงประกาศได้ที่แท็บ 'ลงประกาศใหม่'")

with tab2:
    st.subheader("กรอกข้อมูลลงประกาศ")
    with st.form("listing_form"):
        title = st.text_input("หัวข้อประกาศ (เช่น ขายบ้านเดี่ยว 2 ชั้น / ขายรถยนต์มือสอง)")
        category = st.selectbox("หมวดหมู่", ["อสังหาริมทรัพย์ (บ้าน/คอนโด/ที่ดิน)", "ยานพาหนะ", "สินค้าทั่วไปมือสอง"])
        price_item = st.number_input("ราคา (บาท)", min_value=0, step=500)
        details = st.text_area("รายละเอียดเพิ่มเติม")
        contact_name = st.text_input("ชื่อผู้ติดต่อ")
        phone = st.text_input("เบอร์โทรศัพท์ / LINE ID")
        
        submitted = st.form_submit_button("ส่งข้อมูลลงประกาศ")
        if submitted:
            st.success("🎉 บันทึกข้อมูลประกาศเรียบร้อยแล้ว!")

with tab3:
    st.subheader("💳 ชำระเงินอัปเกรดประกาศพรีเมียม (รับเงินอัตโนมัติ)")
    st.write("เพิ่มโอกาสการมองเห็นประกาศของคุณให้อยู่ในตำแหน่งหน้าแรก!")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        package = st.radio(
            "เลือกแพ็กเกจที่ต้องการ:",
            ["ติดป้ายพรีเมียม 7 วัน (50 บาท)", "ติดป้ายพรีเมียม 30 วัน (150 บาท)", "แพ็กเกจเหมาจ่ายรายเดือน (299 บาท)"]
        )
        
        # คำนวณราคา
        if "50" in package:
            amount = 50
        elif "150" in package:
            amount = 150
        else:
            amount = 299
            
        btn_pay = st.button("สร้าง QR Code ชำระเงิน", type="primary")

    with col2:
        if btn_pay:
            st.markdown(f"### **ยอดชำระทั้งสิ้น: {amount} บาท**")
            # สร้าง QR Code ตัวอย่างสำหรับการสแกนจ่าย
            qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=220x220&data=PromptPay-Payment-Amount-{amount}"
            st.image(qr_url, caption="สแกน QR Code ด้วยแอปธนาคารเพื่อชำระเงิน")
            
            st.warning("⏳ ระบบกำลังรอสัญญาณชำระเงินอัตโนมัติ...")
            
            # จำลองระบบตรวจเช็กการโอนเงิน (Real-time check)
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.03)
                progress_bar.progress(i + 1)
                
            st.success("✅ ระบบได้รับยอดชำระเงินเรียบร้อยแล้ว! ประกาศของคุณได้รับการปรับเป็นพรีเมียมทันที")
            st.balloons()

    st.divider()
    st.caption("สอบถามเพิ่มเติมหรือติดต่อนายหน้า: LINE Official / โทรศัพท์ 08X-XXX-XXXX")
