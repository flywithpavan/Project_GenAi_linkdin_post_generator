import html

import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post


length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]


def apply_custom_css():
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

            html, body, [class*="css"] {
                font-family: 'Inter', sans-serif;
            }

            .stApp {
                background:
                    radial-gradient(circle at top left, rgba(255, 120, 84, 0.22), transparent 32rem),
                    radial-gradient(circle at top right, rgba(38, 166, 154, 0.18), transparent 30rem),
                    linear-gradient(135deg, #fff8f0 0%, #f7fbff 48%, #f8fff7 100%);
                color: #18212f;
            }

            .block-container {
                max-width: 1120px;
                padding-top: 2.2rem;
                padding-bottom: 3rem;
            }

            .hero {
                padding: 2rem 2.2rem;
                border-radius: 18px;
                background:
                    linear-gradient(135deg, rgba(16, 24, 40, 0.94), rgba(48, 82, 126, 0.92)),
                    linear-gradient(90deg, #ff7043, #26a69a);
                border: 1px solid rgba(255, 255, 255, 0.28);
                box-shadow: 0 20px 60px rgba(22, 34, 51, 0.18);
                margin-bottom: 1.5rem;
            }

            .hero-kicker {
                color: #8ff3d5;
                font-size: 0.8rem;
                font-weight: 800;
                letter-spacing: 0.12em;
                text-transform: uppercase;
                margin-bottom: 0.45rem;
            }

            .hero-title {
                color: #ffffff;
                font-size: clamp(2rem, 5vw, 3.5rem);
                font-weight: 800;
                line-height: 1.04;
                margin: 0;
            }

            .hero-copy {
                color: rgba(255, 255, 255, 0.82);
                max-width: 720px;
                font-size: 1.02rem;
                line-height: 1.6;
                margin-top: 0.8rem;
            }

            .panel {
                padding: 1.25rem;
                border-radius: 14px;
                background: rgba(255, 255, 255, 0.84);
                border: 1px solid rgba(34, 46, 64, 0.10);
                box-shadow: 0 16px 42px rgba(36, 48, 71, 0.10);
                margin-bottom: 1rem;
            }

            .panel-title {
                font-size: 1.05rem;
                font-weight: 800;
                color: #1f2a3d;
                margin-bottom: 0.85rem;
            }

            div[data-testid="stSelectbox"] label {
                color: #31415c;
                font-weight: 700;
            }

            div[data-baseweb="select"] > div {
                border-radius: 10px;
                border-color: rgba(49, 65, 92, 0.24);
                background: #ffffff;
            }

            div[data-baseweb="select"] span,
            div[data-baseweb="select"] div {
                color: #18212f;
            }

            div[data-baseweb="select"] svg {
                color: #18212f;
                fill: #18212f;
            }

            .stButton > button {
                width: 100%;
                min-height: 3rem;
                border: 0;
                border-radius: 10px;
                color: #ffffff;
                font-weight: 800;
                background: linear-gradient(90deg, #f45b2f 0%, #0e9f8f 100%);
                box-shadow: 0 12px 28px rgba(14, 159, 143, 0.22);
                transition: transform 0.15s ease, box-shadow 0.15s ease;
            }

            .stButton > button:hover {
                color: #ffffff;
                transform: translateY(-1px);
                box-shadow: 0 16px 34px rgba(244, 91, 47, 0.25);
            }

            .post-card {
                padding: 1.35rem 1.45rem;
                border-radius: 14px;
                background: #ffffff;
                border: 1px solid rgba(34, 46, 64, 0.10);
                box-shadow: 0 16px 42px rgba(36, 48, 71, 0.10);
            }

            .post-title {
                color: #18212f;
                font-size: 1.15rem;
                font-weight: 800;
                margin-bottom: 0.75rem;
            }

            div[data-testid="stDownloadButton"] > button {
                width: 100%;
                min-height: 3rem;
                border-radius: 10px;
                border: 1px solid rgba(24, 33, 47, 0.18);
                background: #ffffff;
                color: #18212f;
                font-weight: 800;
                box-shadow: 0 12px 28px rgba(36, 48, 71, 0.10);
            }

            div[data-testid="stDownloadButton"] > button:hover {
                border-color: rgba(24, 33, 47, 0.32);
                background: #ffffff;
                color: #000000;
            }

            div[data-testid="stDownloadButton"] > button:disabled,
            div[data-testid="stDownloadButton"] > button:disabled:hover {
                border-color: rgba(24, 33, 47, 0.14);
                background: #ffffff;
                color: #18212f;
                opacity: 0.55;
            }

            .post-body {
                white-space: pre-wrap;
                color: #263247;
                font-size: 1.02rem;
                line-height: 1.7;
            }

            .empty-state {
                padding: 1.4rem;
                border-radius: 14px;
                background: rgba(255, 255, 255, 0.72);
                border: 1px dashed rgba(49, 65, 92, 0.24);
                color: #526174;
                text-align: center;
            }

            @media (max-width: 760px) {
                .hero {
                    padding: 1.5rem;
                    border-radius: 14px;
                }

            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main():
    st.set_page_config(
        page_title="LinkedIn Post Generator",
        page_icon="in",
        layout="wide",
    )
    apply_custom_css()

    st.markdown(
        """
        <section class="hero">
            <div class="hero-kicker">AI LinkedIn Studio</div>
            <h1 class="hero-title">LinkedIn Post Generator</h1>
            <div class="hero-copy">
                Choose the topic, post length, and language style. The generator uses your past
                examples to draft a fresh LinkedIn post with a familiar voice.
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    fs = FewShotPosts()
    tags = sorted(fs.get_tags())

    st.markdown('<div class="panel"><div class="panel-title">Post Settings</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        selected_length = st.selectbox("Length", options=length_options, index=1)

    with col3:
        selected_language = st.selectbox("Language", options=language_options)

    generate_clicked = st.button("Generate Post", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    if generate_clicked:
        with st.spinner("Writing your LinkedIn post..."):
            try:
                post = generate_post(selected_length, selected_language, selected_tag)
                st.session_state["generated_post"] = post
            except Exception as exc:
                st.error(f"Could not generate the post: {exc}")

    post = st.session_state.get("generated_post", "")
    header_col, download_col = st.columns([2, 1])
    with header_col:
        st.markdown('<div class="post-title">Generated Post</div>', unsafe_allow_html=True)
    with download_col:
        st.download_button(
            "Download Post",
            data=post,
            file_name="linkedin_post.txt",
            mime="text/plain",
            use_container_width=True,
            disabled=not post,
        )

    if "generated_post" in st.session_state:
        safe_post = html.escape(post)
        st.markdown(
            f"""
            <div class="post-card">
                <div class="post-body">{safe_post}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="empty-state">
                Your generated post will appear here after you choose the settings and press Generate Post.
            </div>
            """,
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    main()
