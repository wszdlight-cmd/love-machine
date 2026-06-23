import streamlit as st
from datetime import datetime
import random

st.set_page_config(page_title="我们的小宇宙", page_icon="💕", layout="centered")

st.title("💑 我们的恋爱时光机")
st.caption("把每一天都过成纪念日")

# ===== 侧边栏：输入层（属于你们的数据）=====
with st.sidebar:
    st.header("✨ 我们的信息")
    start_date = st.date_input("在一起的第一天", datetime(2023, 1, 1))
    her_name = st.text_input("她的名字", "宝贝")
    my_name = st.text_input("我的名字", "笨蛋")
    st.markdown("---")
    st.info("填好后，主页面会自动更新~")

# ===== 计算层：时间运算 =====
today = datetime.now()
start = datetime.combine(start_date, datetime.min.time())
days = (today - start).days
hours = days * 24
minutes = hours * 60

# 下个纪念日
next_anniv = datetime(today.year, start_date.month, start_date.day)
if next_anniv < today:
    next_anniv = datetime(today.year + 1, start_date.month, start_date.day)
days_left = (next_anniv - today).days

# 今年进度
year_start = datetime(today.year, 1, 1)
year_end = datetime(today.year + 1, 1, 1)
year_progress = (today - year_start).days / (year_end - year_start).days

# ===== 展示层：四列指标 =====
st.markdown("### 📊 时间轨迹")
c1, c2, c3, c4 = st.columns(4)
c1.metric("💕 天数", f"{days}")
c2.metric("⏰ 小时", f"{hours:,}")
c3.metric("⌛ 分钟", f"{minutes:,}")
c4.metric("🎂 纪念日", f"{days_left}天后")

st.progress(year_progress)
st.caption(f"今年已走过 {year_progress*100:.1f}%，剩下的时光也要一起呀")

# ===== 互动层：情话抽取 =====
st.markdown("---")
st.subheader("💌 专属情话")

quotes = [
    f"{her_name}，你是我所有美好里的刚刚好。",
    f"自从遇见{her_name}，我再也没羡慕过别人。",
    f"{my_name}和{her_name}的故事，比任何电影都浪漫。",
    f"今天比昨天更喜欢{her_name}，虽然昨天已经很喜欢了。",
    f"世界很大，但{my_name}只想和{her_name}窝在沙发里。",
]

if st.button("🎁 点击抽取今日情话", use_container_width=True):
    st.balloons()  # 屏幕放气球！
    st.success(random.choice(quotes))

# ===== 互动层：甜蜜挑战 =====
st.markdown("---")
st.subheader("🎯 本周甜蜜挑战")

challenges = [
    "手写一封情书，拍照发给对方",
    "一起煮一顿晚餐，不许点外卖",
    "给对方讲一个没听过的童年故事",
    "拍一张搞怪合照设为聊天背景",
    "为对方按摩10分钟，不许偷懒",
]

if st.button("🎲 抽取本周挑战", use_container_width=True):
    st.info(random.choice(challenges))

# ===== 回忆层：照片上传 =====
st.markdown("---")
st.subheader("📸 我们的回忆相册")
uploaded = st.file_uploader("上传一张合照", type=["jpg", "png"])
if uploaded:
    st.image(uploaded, caption=f"{my_name} ❤️ {her_name} 的甜蜜瞬间", use_column_width=True)