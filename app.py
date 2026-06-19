import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os

st.set_page_config(page_title="MovieWeb", page_icon="🎬", layout="wide")

st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <style>
    .stApp {
        background-color: #141414 !important;
        color: #ffffff !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
    }
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }
    
    header, footer, .stDeployButton {
        visibility: hidden !important;
        height: 0 !important;
    }
    
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
    
    .stButton>button[data-testid="stBaseButton-secondary"] {
        background-color: transparent !important;
        border: 1px solid #ffffff !important;
        width: auto !important;
    }
    .stButton>button[data-testid="stBaseButton-secondary"]:hover {
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    .limit-text {
        display: -webkit-box !important;
        -webkit-box-orient: vertical !important;
        -webkit-line-clamp: 3 !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        color: #cccccc !important;
    }
        
    .movie-card {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .movie-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(229, 9, 20, 0.2) !important;
    }
    </style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_cnn_model():
    model_path = r"D:\destop 15092021\CSI08\SPCK\actor_cnn_model.keras"
    label_path = r"D:\destop 15092021\CSI08\SPCK\actor_labels.txt"
        
    if os.path.exists(model_path) and os.path.exists(label_path):
        model = tf.keras.models.load_model(model_path)
        with open(label_path, "r", encoding="utf-8") as f: # Thêm encoding="utf-8" để tránh lỗi đọc chữ tiếng Việt/ký tự đặc biệt
            classes = [line.strip() for line in f.readlines()]
        return model, classes
    return None, None

cnn_model, actor_classes = load_cnn_model()

def predict_actor(image_data):
    if cnn_model is None: return "Chưa có Model"
    img = Image.open(image_data).convert('RGB').resize((150, 150))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    
    predictions = cnn_model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    return actor_classes[np.argmax(score)].replace("_", " ")


movies = [
    {
        "id": 1, "title": "Dune: Hành Tinh Cát - Phần 2", "genre": "Khoa học viễn tưởng", 
        "cast": ["Timothee Chalamet", "Zendaya"],
        "desc": "Paul Atreides hợp lực với Chani và người Fremen để trả thù những kẻ âm mưu hủy hoại gia đình mình.",
        "image": "https://i.pinimg.com/1200x/4e/76/d0/4e76d01767ce3f08fa5f522163bb7a0b.jpg" 
    },
    {
        "id": 2, "title": "Avatar: Dòng Chảy Của Nước", "genre": "Giả tưởng, Hành động", 
        "cast": ["Sam Worthington", "Zoe Saldana"],
        "desc": "Jake Sully sống cuộc sống mới trên Pandora. Khi mối đe dọa quay trở lại, anh phải cùng tộc Na'vi chiến đấu.",
        "image": "https://i.pinimg.com/736x/66/ec/b5/66ecb58a7db3308030eac58dbb3d39c3.jpg"
    },
    {
        "id": 3, "title": "Kung Fu Panda 4", "genre": "Hoạt hình, Võ thuật", 
        "cast": ["Jack Black", "Awkwafina"],
        "desc": "Po trở thành Thủ lĩnh tâm linh của Thung lũng Bình Yên và phải tìm kiếm một hậu duệ Thần Long Đại Hiệp mới.",
        "image": "https://i.pinimg.com/1200x/af/16/b4/af16b444d0868297483994d359c70da4.jpg"
    },
    {
        "id": 4, "title": "Người Kiến & Chiến Binh Ong: Thế Giới Lượng Tử", "genre": "Hành động, Viễn tưởng", 
        "cast": ["Paul Rudd", "Evangeline Lilly"],
        "desc": "Gia đình Scott Lang vô tình bị hút vào Lượng Tử Giới và phải đối đầu với Kang kẻ chinh phạt.",
        "image": "https://i.pinimg.com/736x/83/88/71/838871da115aa61b57c4ed0f18cb9ef8.jpg" 
    },
    {
        "id": 5, "title": "Oppenheimer", "genre": "Lịch sử, Chính kịch", 
        "cast": ["Cillian Murphy", "Robert Downey Jr", "Emily Blunt"],
        "desc": "Câu chuyện về nhà vật lý lý thuyết J. Robert Oppenheimer trong việc chế tạo ra những quả bom nguyên tử đầu tiên.",
        "image": "https://i.pinimg.com/736x/06/c8/70/06c87059cd71c7b46d8d5e25d8aab08b.jpg"
    },
    {
        "id": 6, "title": "Người Nhện: Du Hành Vũ Trụ Nhện", "genre": "Hoạt hình, Hành động", 
        "cast": ["Shameik Moore", "Hailee Steinfeld"],
        "desc": "Miles Morales gặp lại Gwen Stacy và bị phóng qua Đa vũ trụ, đối mặt với Liên minh Người Nhện.",
        "image": "https://iguov8nhvyobj.vcdn.cloud/media/catalog/product/cache/3/image/1800x/71252117777b696995f01934522c402d/r/s/rsz_nguoi-nhen-2023.jpg"
    },
    {
        "id": 7, "title": "Interstellar: Hố Đen Tử Thần", "genre": "Khoa học viễn tưởng", 
        "cast": ["Matthew McConaughey", "Anne Hathaway"],
        "desc": "Một nhóm phi hành gia du hành qua hố đen vũ trụ để tìm kiếm một hành tinh duy trì sự sống mới cho nhân loại.",
        "image": "https://i.pinimg.com/736x/3d/1f/12/3d1f12068833142d5cc0e6f951b4f48a.jpg"
    },
    {
        "id": 8, "title": "Inside Out 2: Những Mảnh Ghép Cảm Xúc", "genre": "Hoạt hình, Hài hước", 
        "cast": ["Amy Poehler", "Maya Hawke"],
        "desc": "Riley bước vào tuổi dậy thì, và tổng hành dinh cảm xúc bất ngờ đón nhận những thành viên mới điều khiển.",
        "image": "https://i.pinimg.com/736x/a4/ef/18/a4ef186bd89e61ef7e5aebcd4d564482.jpg"
    }
]

if "page" not in st.session_state: st.session_state.page = "home"
if "selected_movie" not in st.session_state: st.session_state.selected_movie = None

if st.session_state.page == "detail" and st.session_state.selected_movie:
    movie = st.session_state.selected_movie
    if st.button("← Quay lại Trang chủ"):
        st.session_state.page = "home"
        st.session_state.selected_movie = None
        st.rerun()
        
    st.markdown(f"""
        <div class="container mt-4 text-white">
            <div class="row">
                <div class="col-md-4"><img src="{movie['image']}" class="img-fluid rounded-3 shadow-lg"></div>
                <div class="col-md-8">
                    <h1 class="fw-bold">{movie['title']}</h1>
                    <p class="text-warning fs-5">🎬 {movie['genre']}</p>
                    <p class="text-info">👥 Diễn viên chính: {', '.join(movie['cast'])}</p>
                    <hr class="border-secondary">
                    <p class="fs-5 text-light-50">{movie['desc']}</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("<h1 class='text-center text-danger fw-bold mb-4'> HỆ THỐNG PHIM NETFLIX</h1>", unsafe_allow_html=True)
    
    # st.markdown("<div class='p-3 rounded mb-4' style='background-color: #222;'><h4 class='text-white' style='margin-bottom:0;'>📷 TÌM KIẾM NÂNG CAO BẰNG HÌNH ẢNH DIỄN VIÊN</h4></div>", unsafe_allow_html=True)
    
    if cnn_model is None:
        st.warning("⚠️ Chưa tìm thấy file 'actor_cnn_model.keras'. Vui l  òng chạy file train_cnn.py trước!")
        
    uploaded_file = st.file_uploader("Tải lên ảnh một diễn viên để tìm phim của họ:", type=["jpg", "jpeg", "png"])
    
    detected_actor = ""
    if uploaded_file is not None:
        col1, col2 = st.columns([1, 4])
        with col1: st.image(uploaded_file, width=130, caption="Ảnh quét")
        with col2:
            with st.spinner("AI đang nhận diện khuôn mặt..."):
                detected_actor = predict_actor(uploaded_file)
                st.success(f"🎯 Kết quả nhận diện khuôn mặt: **{detected_actor}**")

    search_query = st.text_input("", placeholder="🔍 Hoặc nhập tên phim cần tìm...").strip()

    if detected_actor:
        filtered_movies = [m for m in movies if any(detected_actor.lower() in actor.lower() for actor in m["cast"])]
        st.markdown(f"<h4 class='text-light mb-4'>Các phim có sự tham gia của: <span class='text-danger'>{detected_actor}</span></h4>", unsafe_allow_html=True)
    elif search_query:
        filtered_movies = [m for m in movies if search_query.lower() in m["title"].lower()]
    else:
        filtered_movies = movies

    if filtered_movies:
        cols = st.columns(4)
        for idx, movie in enumerate(filtered_movies):
            with cols[idx % 4]:
                st.markdown(f"""
                    <div class="card h-100 text-white border-0 movie-card" style="background-color: #1f1f1f; margin-bottom: 15px; border-radius: 8px; overflow:hidden;">
                        <img src="{movie['image']}" style="height: 280px; object-fit: cover;">
                        <div class="card-body p-2">
                            <h6 class="fw-bold text-truncate" style='color: white !important; margin-bottom: 5px;'>{movie['title']}</h6>
                            <p class="text-warning small" style="margin-bottom:5px;">{movie['genre']}</p>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                if st.button("Xem Chi Tiết phim", key=f"btn_{movie['id']}"):
                    st.session_state.selected_movie = movie
                    st.session_state.page = "detail"
                    st.rerun()
    else:
        st.error("❌ Không tìm thấy phim nào phù hợp với từ khóa hoặc diễn viên này.")