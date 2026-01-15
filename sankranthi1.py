# import streamlit as st
# import os

# # MUST be the first Streamlit command
# st.set_page_config(
#     page_title="Madam garu, meekosamay 💖",
#     page_icon="💖",
#     layout="centered"
# )

# # Custom CSS
# st.markdown("""
# <style>

# /* Center content */
# .main {
#     text-align: center;
# }

# /* Main title */
# h1 {
#     color: #d35400;
#     font-size: 30px;
#     text-align: center;
# }

# /* Buttons */
# .stButton button {
#     width: 100%;
#     border-radius: 25px;
#     font-size: 20px;
#     background-color: #27ae60;
#     color: white;
# }

# /* Animation */
# @keyframes fadeInUp {
#     from {
#         opacity: 0;
#         transform: translateY(12px);
#     }
#     to {
#         opacity: 1;
#         transform: translateY(0);
#     }
# }

# .animated-text {
#     animation: fadeInUp 1s ease-in-out;
#     font-weight: 600;
#     margin-bottom: 10px;
# }

# /* Step-wise sizes */
# .step-1 { font-size: 32px; color: #34495e; }
# .step-2 { font-size: 34px; color: #2c3e50; }
# .step-3 { font-size: 36px; color: #1e8449; }
# .step-4 { font-size: 38px; color: #d35400; }

# /* Mobile */
# @media (max-width: 768px) {
#     h1 { font-size: 28px; }
#     .stButton button { font-size: 16px; }

#     .step-1 { font-size: 20px; }
#     .step-2 { font-size: 22px; }
#     .step-3 { font-size: 24px; }
#     .step-4 { font-size: 26px; }
# }

# </style>
# """, unsafe_allow_html=True)

# # Session state
# if "step" not in st.session_state:
#     st.session_state.step = 1

# # Visible page title
# st.title("A Small Surprise 💖")

# # Image path
# img_path = os.path.join(os.path.dirname(__file__), "baby1.jpg")

# # STEP 1
# if st.session_state.step == 1:
#     st.markdown(
#         '<div class="animated-text step-1">Picture kindha click cheyyari madammm 👇</div>',
#         unsafe_allow_html=True
#     )
#     st.image(img_path, use_container_width=True)

#     if st.button("ento? ⏩"):
#         st.session_state.step = 2
#         st.rerun()

# # STEP 2
# elif st.session_state.step == 2:
#     st.markdown(
#         '<div class="animated-text step-2">Chusthara? 👀</div>',
#         unsafe_allow_html=True
#     )
#     st.image(img_path, use_container_width=True)

#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button("chusthaaa"):
#             st.session_state.step = 3
#             st.rerun()
#     with col2:
#         if st.button("chudanu"):
#             st.warning("Please chudachu kada Madaammmm! 🥺")

# # STEP 3
# elif st.session_state.step == 3:
#     st.markdown(
#         '<div class="animated-text step-3">Gift box click cheyandi 🎁</div>',
#         unsafe_allow_html=True
#     )
#     st.image(img_path, use_container_width=True)

#     if st.button("🎁 Open Gift"):
#         st.session_state.step = 4
#         st.rerun()

# # STEP 4
# elif st.session_state.step == 4:
#     st.balloons()
#     st.markdown(
#         '<div class="animated-text step-4">Sankranthi Subhakankshalu! 💗 🌾✨</div>',
#         unsafe_allow_html=True
#     )
#     st.image(img_path, use_container_width=True)

#     if st.button("🔄 Start Over"):
#         st.session_state.step = 1
#         st.rerun()
import streamlit as st
import os

# MUST be the first Streamlit command
st.set_page_config(
    page_title="Madam garu, meekosamay 💖",
    page_icon="💖",
    layout="centered"
)

# ---------------- URL STEP HANDLING ----------------
query_params = st.experimental_get_query_params()

if "step" not in st.session_state:
    st.session_state.step = int(query_params.get("step", [1])[0])

def go_to_step(step):
    st.session_state.step = step
    st.experimental_set_query_params(step=step)
    st.rerun()

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main { text-align: center; }

h1 {
    color: #d35400;
    font-size: 30px;
    text-align: center;
}

.stButton button {
    width: 100%;
    border-radius: 25px;
    font-size: 20px;
    background-color: #27ae60;
    color: white;
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(12px); }
    to { opacity: 1; transform: translateY(0); }
}

.animated-text {
    animation: fadeInUp 1s ease-in-out;
    font-weight: 600;
    margin-bottom: 10px;
}

.step-1 { font-size: 32px; color: #34495e; }
.step-2 { font-size: 34px; color: #2c3e50; }
.step-3 { font-size: 36px; color: #1e8449; }
.step-4 { font-size: 38px; color: #d35400; }

@media (max-width: 768px) {
    h1 { font-size: 26px; }
    .stButton button { font-size: 16px; }
    .step-1 { font-size: 20px; }
    .step-2 { font-size: 22px; }
    .step-3 { font-size: 24px; }
    .step-4 { font-size: 26px; }
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("A Small Surprise 💖")

# ---------------- IMAGE PATH ----------------
img_path = os.path.join(os.path.dirname(__file__), "baby1.jpg")

# ---------------- STEP 1 ----------------
if st.session_state.step == 1:
    st.markdown(
        '<div class="animated-text step-1">Picture kindha click cheyyari madammm 👇</div>',
        unsafe_allow_html=True
    )
    st.image(img_path, use_container_width=True)

    if st.button("ento? ⏩"):
        go_to_step(2)

# ---------------- STEP 2 ----------------
elif st.session_state.step == 2:
    st.markdown(
        '<div class="animated-text step-2">Chusthara? 👀</div>',
        unsafe_allow_html=True
    )
    st.image(img_path, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("chusthaaa"):
            go_to_step(3)
    with col2:
        if st.button("chudanu"):
            st.warning("Please chudachu kada Madaammmm! 🥺")

# ---------------- STEP 3 ----------------
elif st.session_state.step == 3:
    st.markdown(
        '<div class="animated-text step-3">Gift box click cheyandi 🎁</div>',
        unsafe_allow_html=True
    )
    st.image(img_path, use_container_width=True)

    if st.button("🎁 Open Gift"):
        go_to_step(4)

# ---------------- STEP 4 ----------------
elif st.session_state.step == 4:
    st.balloons()
    st.markdown(
        '<div class="animated-text step-4">Sankranthi Subhakankshalu! 💗 🌾✨</div>',
        unsafe_allow_html=True
    )
    st.image(img_path, use_container_width=True)

    if st.button("🔄 Start Over"):
        go_to_step(1)

