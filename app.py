import streamlit as st
import os

st.set_page_config(page_title="ศูนย์กลางลงประกาศบ้าน & สินค้ามือสอง", page_icon="🏠", layout="wide")

st.title("🏠 ศูนย์กลางลงประกาศซื้อ-ขาย/เช่า บ้านและสินค้ามือสอง")
st.write("ลงประกาศง่ายๆ พร้อมระบบชำระเงินอัปเกรดประกาศพรีเมียม")

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
    st.subheader("💳 ชำระเงินอัปเกรดประกาศพรีเมียม (โอนตรงเข้าบัญชี)")
    st.write("เพิ่มโอกาสการมองเห็นประกาศของคุณให้อยู่ในตำแหน่งหน้าแรก!")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        package = st.radio(
            "เลือกแพ็กเกจที่ต้องการ:",
            ["ติดป้ายพรีเมียม 7 วัน (50 บาท)", "ติดป้ายพรีเมียม 30 วัน (150 บาท)", "แพ็กเกจเหมาจ่ายรายเดือน (299 บาท)"]
        )
        
        if "50" in package:
            amount = 50
        elif "150" in package:
            amount = 150
        else:
            amount = 299
            
        st.info(f"💰 ยอดชำระทั้งสิ้น: **{amount} บาท**")

    with col2:
        st.markdown("### **สแกนชำระเงินผ่าน PromptPay**")
        
        # เช็กชื่อไฟล์รูปภาพ QR Code ทั้ง .jpg และ .png
        if os.path.exists("qr_code.jpg"):
            st.image("qr_code.jpg", caption="สแกน QR Code เพื่อโอนเงินเข้าบัญชี นาย อรัญ ไชยทิพย์ โดยตรง", width=280)
        elif os.path.exists("qr_code.png"):
            st.image("qr_code.png", caption="สแกน QR Code เพื่อโอนเงินเข้าบัญชี นาย อรัญ ไชยทิพย์ โดยตรง", width=280)
        elif os.path.exists("qr_code.jpeg"):
            st.image("qr_code.jpeg", caption="สแกน QR Code เพื่อโอนเงินเข้าบัญชี นาย อรัญ ไชยทิพย์ โดยตรง", width=280)
        else:
            st.warning("⚠️ กรุณาอัปโหลดไฟล์รูป 'qr_code' ขึ้น GitHub เพื่อแสดง QR Code พร้อมเพย์ของคุณ")

    st.divider()
    st.subheader("📲 แจ้งการชำระเงิน / ส่งสลิป")
    st.write("เมื่อโอนเงินเรียบร้อยแล้ว กรุณาส่งสลิปยืนยันมาที่ LINE หรือโทรแจ้งได้เลยครับ")
