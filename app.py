import streamlit as st
import os

st.set_page_config(page_title="my-marketplace | ศูนย์กลางอสังหาฯ & นายหน้ามืออาชีพ", page_icon="🏡", layout="wide")

# ตกแต่ง CSS หน้าจอให้ทันสมัยสไตล์ Facebook / YouTube และระบบนายหน้า
st.markdown("""
    <style>
    .fb-header {
        background: linear-gradient(135deg, #1877f2 0%, #0c4a9e 100%);
        padding: 25px;
        border-radius: 12px;
        color: white;
        margin-bottom: 20px;
    }
    .card-post {
        background-color: #ffffff;
        border: 1px solid #ced4da;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    .wallet-box {
        background: linear-gradient(135deg, #28a745 0%, #1e7e34 100%);
        padding: 20px;
        border-radius: 12px;
        color: white;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="fb-header">
        <h1>🏡 my-marketplace - ศูนย์รวมอสังหาฯ & ระบบนายหน้าอัจฉริยะ</h1>
        <p>ฟีดไทม์ไลน์สไตล์โซเชียล, ระบบฝากขาย/หาบ้าน, คำนวณคอมมิชชั่นแบบ Lalamove/Shopee และระบบจัดการแอดมิน</p>
    </div>
""", unsafe_allow_html=True)

# ฐานข้อมูลจำลอง (Session State)
if "timeline_feed" not in st.session_state:
    st.session_state.timeline_feed = [
        {"user": "คุณอรัญ (Fresh Food Manager & นายหน้าอสังหาฯ)", "time": "10 นาทีที่แล้ว", "text": "🏡 เปิดรับฝากขายบ้านมือสองและหาบ้านเช่าโซนปทุมธานีแล้วครับ ค่าคอมมิชชั่นเป็นธรรม ระบบหักอัตโนมัติปลอดภัย 100% สนใจทักมาได้เลย!", "type": "text", "media": ""}
    ]

if "property_listings" not in st.session_state:
    st.session_state.property_listings = [
        {"name": "คุณสมชาย ใจดี", "tel": "081-234-5678", "type": "ฝากขายบ้านมือสอง", "title": "บ้านเดี่ยว 2 ชั้น ทำเลดี ปทุมธานี", "price": 2500000, "commission_rate": 3.0}
    ]

if "wallet_transactions" not in st.session_state:
    st.session_state.wallet_transactions = [
        {"id": "TXN-001", "desc": "ค่าคอมมิชชั่นขายบ้าน (คุณสมชาย)", "total": 2500000, "rate": 3.0, "commission": 75000, "net": 2425000, "status": "หักสำเร็จ & โอนเข้ากระเป๋าแล้ว"}
    ]

if "support_tickets" not in st.session_state:
    st.session_state.support_tickets = []

provinces_thailand = [
    "กรุงเทพมหานคร", "ปทุมธานี", "นนทบุรี", "สมุทรปราการ", "สมุทรสาคร", "นครปฐม",
    "เชียงใหม่", "เชียงราย", "ขอนแก่น", "นครราชสีมา", "อุบลราชธานี", "อุดรธานี",
    "ชลบุรี", "ระยอง", "ภูเก็ต", "สงขลา", "สุราษฎร์ธานี", "พระนครศรีอยุธยา"
]

# เมนูหลัก 6 ฟีเจอร์ตรงตามความต้องการ
menu_option = st.selectbox("📌 เลือกเมนูการใช้งานหลัก:", [
    "📰 5. หน้าจอ Timeline ทันสมัย (Facebook & YouTube Style)",
    "🏡 1. โปรแกรมรับฝากขายบ้านมือสองและหาบ้านเช่า",
    "💰 6. บัญชีหักค่านายหน้า & กระเป๋าเงินอัจฉริยะ (Lalamove/Shopee Style)",
    "🏦 3. โปรแกรมคำนวณวงเงินกู้ซื้อบ้าน",
    "📞 4. โปรแกรมแอดมินแจ้งปัญหา & ศูนย์ช่วยเหลือ",
    "⚙️ ระบบจัดการหลังบ้าน (Admin)"
])

st.divider()

# -------------------------------------------------------------
# 1. หน้าจอ Timeline (Facebook & YouTube Style)
# -------------------------------------------------------------
if menu_option.startswith("📰"):
    st.subheader("📰 ฟีดไทม์ไลน์ชุมชนอสังหาฯ (Social Feed)")
    
    with st.form("form_post_feed", clear_on_submit=True):
        st.markdown("### ✍️ สร้างโพสต์ใหม่ของคุณ (แชร์บ้าน, วิดีโอ YouTube, หรือประกาศด่วน)")
        p_user = st.text_input("ชื่อของคุณ / ตำแหน่ง (เช่น คุณอรัญ นายหน้าอสังหาฯ)")
        p_text = st.text_area("คุณกำลังคิดอะไรอยู่ หรือมีบ้านมือสอง/บ้านเช่าตัวไหนมานำเสนอ?")
        p_media_type = st.selectbox("ประเภทสื่อที่แนบ", ["ข้อความปกติ", "แนบลิงก์วิดีโอ YouTube", "แนบรูปภาพอสังหาฯ"])
        p_link = st.text_input("วางลิงก์ YouTube (ถ้ามี เช่น https://www.youtube.com/watch?v=...) หรือลิงก์รูปภาพ")
        
        if st.form_submit_button("🚀 โพสต์ลงฟีดทันที"):
            if p_user and p_text:
                st.session_state.timeline_feed.insert(0, {
                    "user": p_user, "time": "เมื่อสักครู่นี้", "text": p_text, "type": p_media_type, "media": p_link
                })
                st.success("🎉 โพสต์ลงไทม์ไลน์สำเร็จ!")
            else:
                st.warning("⚠️ กรุณากรอกชื่อและข้อความโพสต์")
                
    st.markdown("### 🌐 ฟีดโพสต์ล่าสุดจากสมาชิก")
    for post in st.session_state.timeline_feed:
        st.markdown(f"""
        <div class="card-post">
            <strong>👤 {post['user']}</strong> <span style="color:gray; font-size:12px;">{post['time']}</span>
            <p style="margin-top:10px; font-size:15px;">{post['text']}</p>
        </div>
        """, unsafe_allow_html=True)
        if post['type'] == "แนบลิงก์วิดีโอ YouTube" and post['media']:
            try:
                st.video(post['media'])
            except:
                st.info(f"🔗 ลิงก์วิดีโอ: {post['media']}")
        elif post['type'] == "แนบรูปภาพอสังหาฯ" and post['media']:
            st.image(post['media'], width=400)

# -------------------------------------------------------------
# 2. โปรแกรมรับฝากขายบ้านมือสองและหาบ้านเช่า + คำนวณคอมมิชชั่น
# -------------------------------------------------------------
elif menu_option.startswith("🏡"):
    st.subheader("🏡 โปรแกรมรับฝากขายบ้านมือสองและหาบ้านเช่า")
    
    tab1, tab2 = st.tabs(["📝 ลงทะเบียนฝากทรัพย์ / หาบ้าน", "📋 รายการทรัพย์สินในระบบ"])
    
    with tab1:
        with st.form("form_property", clear_on_submit=True):
            c_name = st.text_input("ชื่อ-นามสกุลผู้ติดต่อ")
            c_tel = st.text_input("เบอร์โทรศัพท์มือถือ")
            c_action = st.selectbox("ประเภทบริการ", ["ฝากขายบ้านมือสอง", "ฝากปล่อยเช่าบ้าน", "ต้องการหาบ้านเช่า", "ต้องการซื้อบ้านมือสอง"])
            c_title = st.text_input("หัวข้อประกาศ (เช่น ขายบ้านเดี่ยว 2 ชั้น ทำเลปทุมธานี)")
            c_price = st.number_input("ราคาประเมินขาย / ค่าเช่าต่อเดือน (บาท)", min_value=1000, value=2500000, step=10000)
            c_comm_rate = st.slider("กำหนดค่าคอมมิชชั่นนายหน้า (%)", min_value=1.0, max_value=5.0, value=3.0, step=0.5)
            c_detail = st.text_area("รายละเอียดเพิ่มเติม / ทำเล / สิ่งอำนวยความสะดวก")
            
            if st.form_submit_button("💾 บันทึกข้อมูลเข้าระบบ"):
                if c_name and c_tel and c_title:
                    # คำนวณคอมมิชชั่นอัตโนมัติ
                    calc_comm = (c_price * c_comm_rate) / 100
                    calc_net = c_price - calc_comm
                    
                    st.session_state.property_listings.insert(0, {
                        "name": c_name, "tel": c_tel, "type": c_action, "title": c_title, "price": c_price, "commission_rate": c_comm_rate
                    })
                    
                    # บันทึกลงระบบกระเป๋าเงินอัตโนมัติ
                    txn_id = f"TXN-{len(st.session_state.wallet_transactions)+1:03d}"
                    st.session_state.wallet_transactions.insert(0, {
                        "id": txn_id, "desc": f"{c_action} ({c_title})", "total": c_price, "rate": c_comm_rate, "commission": calc_comm, "net": calc_net, "status": "บันทึกคำขอสำเร็จ"
                    })
                    
                    st.success(f"🎉 บันทึกสำเร็จ! ระบบคำนวณค่าคอมมิชชั่น {c_comm_rate}% เป็นเงิน {calc_comm:,.2f} บาท เรียบร้อยแล้ว")
                else:
                    st.warning("⚠️ กรุณากรอกข้อมูลสำคัญให้ครบถ้วน")
                    
    with tab2:
        st.markdown("### 📋 รายการอสังหาริมทรัพย์ทั้งหมดในระบบ")
        for prop in st.session_state.property_listings:
            st.markdown(f"""
            <div class="card-post">
                <h4>🏷️ {prop['title']}</h4>
                <p><strong>ผู้ติดต่อ:</strong> {prop['name']} ({prop['tel']}) | <strong>ประเภท:</strong> {prop['type']}</p>
                <p><strong>ราคา:</strong> {prop['price']:,.2f} บาท | <strong>ค่าคอมมิชชั่นนายหน้า:</strong> {prop['commission_rate']}%</p>
            </div>
            """, unsafe_allow_html=True)

# -------------------------------------------------------------
# 3. บัญชีหักค่านายหน้า & กระเป๋าเงินอัจฉริยะ (Lalamove/Shopee Style)
# -------------------------------------------------------------
elif menu_option.startswith("💰"):
    st.subheader("💰 บัญชีหักค่านายหน้า & กระเป๋าเงินอัจฉริยะ (Wallet System)")
    st.markdown("""
    <div class="wallet-box">
        <h3>💳 ระบบกระเป๋าเงินนายหน้า (Agent Wallet)</h3>
        <p>ระบบหักค่านายหน้าและจัดการรายรับอัตโนมัติ คล้ายกับระบบขนส่ง Lalamove หรือแพลตฟอร์มสั่งอาหาร Shopee</p>
    </div>
    """, unsafe_allow_html=True)
    
    total_revenue = sum([item['total'] for item in st.session_state.wallet_transactions])
    total_commission = sum([item['commission'] for item in st.session_state.wallet_transactions])
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="📊 มูลค่าซื้อ-ขายรวมในระบบ", value=f"{total_revenue:,.2f} บาท")
    with col2:
        st.metric(label="💵 รายได้ค่าคอมมิชชั่นสะสม (สุทธิ)", value=f"{total_commission:,.2f} บาท")
        
    st.markdown("### 📜 ประวัติการหักค่านายหน้าและธุรกรรมล่าสุด")
    for txn in st.session_state.wallet_transactions:
        st.markdown(f"""
        <div class="card-post">
            <strong>รหัสรายการ: {txn['id']}</strong> | <span style="color:green;">{txn['status']}</span>
            <p><strong>รายการ:</strong> {txn['desc']}</p>
            <p><strong>มูลค่าทรัพย์:</strong> {txn['total']:,.2f} บาท (หักค่าคอมมิชชั่น {txn['rate']}%)</p>
            <p><strong>ค่าคอมมิชชั่นที่หักเข้ากระเป๋า:</strong> <span style="color:#28a745; font-weight:bold;">+{txn['commission']:,.2f} บาท</span></p>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------------------
# 4. โปรแกรมคำนวณวงเงินกู้ซื้อบ้าน
# -------------------------------------------------------------
elif menu_option.startswith("🏦"):
    st.subheader("🏦 โปรแกรมคำนวณวงเงินกู้ซื้อบ้าน & ค่างวดผ่อน")
    
    sal = st.number_input("รายได้สุทธิต่อเดือน (บาท)", min_value=10000, value=35000, step=1000)
    deb = st.number_input("ภาระหนี้สินเดิมต่อเดือน (บาท)", min_value=0, value=0, step=500)
    interest_rate 
