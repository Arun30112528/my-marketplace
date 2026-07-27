import streamlit as st

st.set_page_config(page_title="ศูนย์กลางบ้านเช่าและขายมือสอง", layout="wide")

st.title("🏡 ศูนย์กลางบ้านเช่าและขายมือสอง")
st.subheader("รวมประกาศเช่า-ซื้อ-ขาย อสังหาริมทรัพย์คุณภาพ")

# สร้างระบบเก็บข้อมูลจำลองในหน่วยความจำ
if "properties" not in st.session_state:
    st.session_state.properties = [
        {
            "id": 1,
            "title": "ทาวน์โฮม 2 ชั้น สภาพใหม่พร้อมอยู่",
            "type": "ให้เช่า",
            "price": "12,000 บาท/เดือน",
            "zone": "ปทุมธานี",
            "detail": "3 ห้องนอน 2 ห้องน้ำ แอร์ครบ เฟอร์นิเจอร์พร้อมเข้าอยู่",
            "contact": "081-XXX-XXXX"
        },
        {
            "id": 2,
            "title": "บ้านเดี่ยวหลังใหญ่ แปลงมุม มีพื้นที่สวน",
            "type": "ขายมือสอง",
            "price": "3,500,000 บาท",
            "zone": "รังสิต",
            "detail": "4 ห้องนอน 3 ห้องน้ำ จอดรถได้ 2 คัน ใกล้ทางด่วน",
            "contact": "089-XXX-XXXX"
        }
    ]

# แถบด้านข้าง (Sidebar) สำหรับค้นหา และ ฟอร์มฝากลงประกาศ
st.sidebar.header("🔍 ค้นหาและกรองข้อมูล")
selected_type = st.sidebar.selectbox("เลือกประเภท", ["ทั้งหมด", "ให้เช่า", "ขายมือสอง"])

st.sidebar.write("---")
st.sidebar.header("➕ ฝากลงประกาศ (ฟรี)")

with st.sidebar.form("add_property_form", clear_on_submit=True):
    new_title = st.text_input("หัวข้อประกาศ")
    new_type = st.selectbox("ประเภท", ["ให้เช่า", "ขายมือสอง"])
    new_price = st.text_input("ราคา (เช่น 15,000 บาท/เดือน)")
    new_zone = st.text_input("ทำเล/โซน (เช่น ปทุมธานี)")
    new_detail = st.text_area("รายละเอียดบ้าน")
    new_contact = st.text_input("เบอร์โทรศัพท์/Line ID")
    
    submitted = st.form_submit_button("บันทึกประกาศ")
    if submitted:
        if new_title and new_price and new_contact:
            new_item = {
                "id": len(st.session_state.properties) + 1,
                "title": new_title,
                "type": new_type,
                "price": new_price,
                "zone": new_zone,
                "detail": new_detail,
                "contact": new_contact
            }
            st.session_state.properties.append(new_item)
            st.sidebar.success("ลงประกาศสำเร็จเรียบร้อย!")
        else:
            st.sidebar.error("กรุณากรอกข้อมูลสำคัญให้ครบถ้วน")

# แสดงรายการประกาศ
st.write("---")
for item in st.session_state.properties:
    if selected_type == "ทั้งหมด" or item["type"] == selected_type:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"### {item['title']}")
            st.write(f"📍 **โซน:** {item['zone']} | 🏷️ **ประเภท:** {item['type']}")
            st.write(f"📝 {item['detail']}")
            st.write(f"📞 **ติดต่อ:** {item['contact']}")
        with col2:
            st.subheader(f"💰 {item['price']}")
            st.button("สนใจติดต่อ", key=f"btn_{item['id']}")
        st.write("---")