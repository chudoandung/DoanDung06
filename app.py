import streamlit as st

st.set_page_config(page_title="MovieWeb", page_icon="🎬", layout="wide")

st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <style>
    /* 1. Đổi toàn bộ nền app sang màu đen Netflix và sửa font chữ */
    .stApp {
        background-color: #141414 !important;
        color: #ffffff !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
    }
    
    /* 2. Xóa bỏ khoảng trắng thừa (Padding) mặc định ở đầu trang của Streamlit */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }
    
    /* 3. Ẩn các thành phần thừa như Menu, Footer và nút GitHub của Streamlit */
    header, footer, .stDeployButton {
        visibility: hidden !important;
        height: 0 !important;
    }
    
    /* 4. Tối ưu lại ô Tìm Kiếm để nhìn sang trọng hơn */
    .stTextInput input {
        background-color: #2b2b2b !important;
        color: #ffffff !important;
        border: 1px solid #444444 !important;
        border-radius: 30px !important;
        padding: 12px 25px !important;
        font-size: 1rem !important;
    }
    .stTextInput input:focus {
        border-color: #e50914 !important;
        box-shadow: 0 0 0 0.2rem rgba(229, 9, 20, 0.25) !important;
    }
    /* Ẩn dòng chữ label nhỏ phía trên ô tìm kiếm của Streamlit */
    .stTextInput label {
        display: none !important;
    }
    
    /* 5. Custom lại các nút bấm Streamlit cho đồng bộ với màu đỏ Bootstrap/Netflix */
    .stButton>button {
        background-color: #e50914 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 6px !important;
        font-weight: bold !important;
        padding: 8px 16px !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        background-color: #b20710 !important;
        transform: scale(1.02);
        color: #ffffff !important;
    }
    
    /* Nút Quay lại (màu trong suốt viền trắng) */
    .stButton>button[data-testid="stBaseButton-secondary"] {
        background-color: transparent !important;
        border: 1px solid #ffffff !important;
        width: auto !important;
    }
    .stButton>button[data-testid="stBaseButton-secondary"]:hover {
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    /* 6. Ép văn bản mô tả trên Banner chỉ hiển thị tối đa 3 dòng kèm dấu ba chấm */
    .limit-text {
        display: -webkit-box !important;
        -webkit-box-orient: vertical !important;
        -webkit-line-clamp: 3 !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        color: #cccccc !important;
    }
    
    /* 7. Hiệu ứng phóng to nhẹ khi di chuột vào các thẻ Card phim */
    .movie-card {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .movie-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(229, 9, 20, 0.2) !important;
    }
    </style>
""", unsafe_allow_html=True)


movies = [
    {
        "id": 1, "title": "Dune: Hành Tinh Cát - Phần 2", "genre": "Khoa học viễn tưởng, Phiêu lưu",
        "desc": "Paul Atreides hợp lực với Chani và người Fremen để trả thù những kẻ âm mưu hủy hoại gia đình mình. Đối mặt với sự lựa chọn giữa tình yêu của đời mình và số phận của vũ trụ.",
        "image": "https://m.media-amazon.com/images/M/MV5BNTc0YmQxMjEtODI5MC00NjFiLTlkMWUtOGQ5NjFmYWUyZGJhXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg" 
    },
    {
        "id": 2, "title": "Người Kiến & Chiến Binh Ong", "genre": "Hành động, Khoa học viễn tưởng",
        "desc": "Scott Lang với bộ đồ công nghệ siêu việt có khả năng thu nhỏ nhưng có sức mạnh lớn. Anh đồng hành cùng Hope van Dyne trong nhiệm vụ mới vào Lượng Tử Giới.",
        "image": "https://images2.thanhnien.vn/thumb_w/686/528068263637045248/2023/2/8/ant-man-3-4x5-1675846349809495443319-0-227-858-871-crop-16758467161031369488729.jpeg" 
    },
    {
        "id": 3, "title": "Moana 2", "genre": "Hoạt hình, Phiêu lưu",
        "desc": "Tiếp tục hành trình của Moana sau khi nhận được cuộc gọi bất ngờ từ tổ tiên, cô cùng thủy thủ đoàn hướng tới vùng biển xa xôi để kết nối lại các hòn đảo.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjlaCsHyHSV1Gf-tm2DEvx3Ohz6Ma6nSI9tuf3l8BM7MzBmSkWKliMKYxd&s=10"
    },
    {
        "id": 4, "title": "Avatar: Dòng Chảy Của Nước", "genre": "Giả tưởng, Hành động",
        "desc": "Jake Sully sống cuộc sống mới trên Pandora. Khi một mối đe dọa quen thuộc quay trở lại, anh phải cùng người Na'vi chiến đấu bảo vệ gia đình.",
        "image": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/t6HI7m10wYpSTvPhwg6Yw0g0SjG.jpg"
    },
    {
        "id": 5, "title": "Người Nhện: Du Hành Vũ Trụ Nhện", "genre": "Hoạt hình, Hành động",
        "desc": "Miles Morales gặp lại Gwen Stacy và được phóng qua Đa vũ trụ, nơi anh chạm trán với một nhóm Người Nhện chịu trách nhiệm bảo vệ chính sự tồn tại của nó.",
        "image": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/8VtW97g9tujg4CH6vN68vRCHpZp.jpg"
    },
    {
        "id": 6, "title": "Oppenheimer", "genre": "Lịch sử, Chính kịch",
        "desc": "Câu chuyện về nhà vật lý lý thuyết J. Robert Oppenheimer, người dẫn đầu Dự án Manhattan nhằm chế tạo ra vũ khí hạt nhân đầu tiên trên thế giới.",
        "image": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/8G9v9nB19yZ0zR04K42j9v7wV1V.jpg"
    },
    {
        "id": 7, "title": "Interstellar: Hố Đen Tử Thần", "genre": "Khoa học viễn tưởng, Bí ẩn",
        "desc": "Một nhóm các nhà thám hiểm du hành qua một hố sâu trong không gian nhằm nỗ lực đảm bảo sự sống còn của nhân loại khi Trái Đất sắp bị hủy diệt.",
        "image": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/gEU2Wthw0uOJJm783Xv3Q3mwVwZ.jpg"
    },
    {
        "id": 8, "title": "Kung Fu Panda 4", "genre": "Hoạt hình, Hài hước",
        "desc": "Po được giao trọng trách trở thành Thủ lĩnh tâm linh của Thung lũng Bình Yên và phải tìm kiếm một hậu duệ Thần Long Đại Hiệp mới trong khi đối đầu với Tắc Kè Bông.",
        "image": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/kDp1vUBi32bWaaCmBF7YgghjLE5.jpg"
    }
]

# 3. KHỞI TẠO TRẠNG THÁI CHUYỂN TRANG
if "page" not in st.session_state:
    st.session_state.page = "home"
if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

# --- GIAO DIỆN TRANG CHI TIẾT PHIM ---
if st.session_state.page == "detail" and st.session_state.selected_movie:
    movie = st.session_state.selected_movie
    
    # Nút quay lại kiểu viền trắng sang trọng
    if st.button("← Quay lại Trang chủ", key="btn_back"):
        st.session_state.page = "home"
        st.session_state.selected_movie = None
        st.rerun()
        
    st.write("---")
    
    st.markdown(f"""
        <div class="container mt-2">
            <div class="row text-white">
                <div class="col-md-4">
                    <img src="{movie['image']}" class="img-fluid rounded-3 shadow-lg" style="width: 100%; max-height: 480px; object-fit: cover;">
                </div>
                <div class="col-md-8">
                    <h1 class="display-4 fw-bold text-white" style="color: white !important;">{movie['title']}</h1>
                    <p class="text-warning fs-5 fw-semibold">🎬 {movie['genre']}</p>
                    <hr class="border-secondary">
                    <p class="fs-5 text-light-50">{movie['desc']}</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write(" ")
    st.button(" XEM PHIM NGAY CHẤT LƯỢNG CAO", type="primary", key="btn_watch")

else:
    featured = movies[0]
    
    st.markdown(f"""
        <div class="p-5 mb-4 rounded-4 position-relative overflow-hidden text-white shadow-lg d-flex align-items-center" 
             style="background: linear-gradient(to right, rgba(0,0,0,0.95) 45%, rgba(0,0,0,0.3)), url('{featured['image']}') center/cover; min-height: 380px;">
            <div class="col-md-6 position-relative" style="z-index: 10;">
                <span class="badge bg-danger mb-2 px-3 py-2 text-uppercase fw-bold" style="font-size: 0.8rem;">Phim Nổi Bật Nhất</span>
                <h1 class="display-4 fw-bold text-white mb-2" style="color: white !important;">{featured['title']}</h1>
                <p class="text-warning mb-3 fw-semibold">★ {featured['genre']}</p>
                <p class="fs-5 text-light mb-4 limit-text">{featured['desc']}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("▶ XEM CHI TIẾT PHIM NỔI BẬT", key="btn_featured"):
        st.session_state.selected_movie = featured
        st.session_state.page = "detail"
        st.rerun()

    st.write(" ")
    
    search_query = st.text_input("", placeholder="🔍 Tìm tên bộ phim bạn yêu thích...").strip()
    
    if search_query:
        filtered_movies = [m for m in movies if search_query.lower() in m["title"].lower()]
        st.markdown(f"<h3 class='mb-4 text-muted'>Kết quả tìm kiếm cho: <span class='text-white'>\"{search_query}\"</span></h3>", unsafe_allow_html=True)
    else:
        filtered_movies = movies
        st.markdown("<h2 class='mb-4 text-light fw-bold ps-3' style='border-left: 5px solid #e50914; color: white !important;'>Tất Cả Phim</h2>", unsafe_allow_html=True)

    if filtered_movies:
        cols = st.columns(4)  
        
        for idx, movie in enumerate(filtered_movies):
            with cols[idx % 4]:
                st.markdown(f"""
                    <div class="card h-100 text-white border-0 shadow-sm position-relative overflow-hidden rounded-3 movie-card" style="background-color: rgba(255, 255, 255, 0.05); margin-bottom: 10px;">
                        <img src="{movie['image']}" class="card-img-top" style="height: 300px; object-fit: cover;">
                        <div class="card-body p-3">
                            <h6 class="card-title fw-bold text-truncate mb-1" style="color: white !important;">{movie['title']}</h6>
                            <p class="card-text text-warning" style="font-size: 0.8rem; margin-bottom: 0;">{movie['genre']}</p>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                if st.button("Xem Chi Tiết", key=f"btn_{movie['id']}"):
                    st.session_state.selected_movie = movie
                    st.session_state.page = "detail"
                    st.rerun()
    else:
        st.markdown("<div class='text-center py-5'><p class='text-muted fs-4'>Không tìm thấy bộ phim nào phù hợp.</p></div>", unsafe_allow_html=True)