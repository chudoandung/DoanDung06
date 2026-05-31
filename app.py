from flask import Flask, render_template, request

app = Flask(__name__)

# Danh sách phim phong phú (Thay thế CSDL)
movies = [
    {
        "id": 1,
        "title": "Dune: Hành Tinh Cát - Phần 2",
        "genre": "Khoa học viễn tưởng, Phiêu lưu",
        "desc": "Paul Atreides hợp lực với Chani và người Fremen để trả thù những kẻ âm mưu hủy hoại gia đình mình. Đối mặt với sự lựa chọn giữa tình yêu của đời mình và số phận của vũ trụ.",
        "image": "https://image.tmdb.org/t/p/w500/czbKjt5YHe8gYy2gcZp7gSgYAIW.jpg" 
    },
    {
        "id": 2,
        "title": "Người Kiến & Chiến Binh Ong",
        "genre": "Hành động, Khoa học viễn tưởng",
        "desc": "Scott Lang với bộ đồ công nghệ siêu việt có khả năng thu nhỏ nhưng có sức mạnh lớn. Anh đồng hành cùng Hope van Dyne trong nhiệm vụ mới vào Lượng Tử Giới.",
        "image": "https://image.tmdb.org/t/p/w500/qnGoAsv1G16m4g6ZisIq4TfWj6f.jpg" 
    },
    {
        "id": 3,
        "title": "Moana 2",
        "genre": "Hoạt hình, Phiêu lưu",
        "desc": "Tiếp tục hành trình của Moana sau khi nhận được cuộc gọi bất ngờ từ tổ tiên, cô cùng thủy thủ đoàn hướng tới vùng biển xa xôi để kết nối lại các hòn đảo.",
        "image": "https://image.tmdb.org/t/p/w500/9gYslF3TyR7w76CZaInR06ZgfwO.jpg"
    },
    {
        "id": 4,
        "title": "Avatar: Dòng Chảy Của Nước",
        "genre": "Giả tưởng, Hành động",
        "desc": "Jake Sully sống cuộc sống mới trên Pandora. Khi một mối đe dọa quen thuộc quay trở lại, anh phải cùng người Na'vi chiến đấu bảo vệ gia đình.",
        "image": "https://image.tmdb.org/t/p/w500/t6HI7m10wYpSTvPhwg6Yw0g0SjG.jpg"
    },
    {
        "id": 5,
        "title": "Người Nhện: Du Hành Vũ Trụ Nhện",
        "genre": "Hoạt hình, Hành động",
        "desc": "Miles Morales gặp lại Gwen Stacy và được phóng qua Đa vũ trụ, nơi anh chạm trán với một nhóm Người Nhện chịu trách nhiệm bảo vệ chính sự tồn tại của nó.",
        "image": "https://image.tmdb.org/t/p/w500/8VtW97g9tujg4CH6vN68vRCHpZp.jpg"
    },
    {
        "id": 6,
        "title": "Oppenheimer",
        "genre": "Lịch sử, Chính kịch",
        "desc": "Câu chuyện về nhà vật lý lý thuyết J. Robert Oppenheimer, người dẫn đầu Dự án Manhattan nhằm chế tạo ra vũ khí hạt nhân đầu tiên trên thế giới.",
        "image": "https://image.tmdb.org/t/p/w500/8G9v9nB19yZ0zR04K42j9v7wV1V.jpg"
    },
    {
        "id": 7,
        "title": "Interstellar: Hố Đen Tử Thần",
        "genre": "Khoa học viễn tưởng, Bí ẩn",
        "desc": "Một nhóm các nhà thám hiểm du hành qua một hố sâu trong không gian nhằm nỗ lực đảm bảo sự sống còn của nhân loại khi Trái Đất sắp bị hủy diệt.",
        "image": "https://image.tmdb.org/t/p/w500/gEU2Wthw0uOJJm783Xv3Q3mwVwZ.jpg"
    },
    {
        "id": 8,
        "title": "Kung Fu Panda 4",
        "genre": "Hoạt hình, Hài hước",
        "desc": "Po được giao trọng trách trở thành Thủ lĩnh tâm linh của Thung lũng Bình Yên và phải tìm kiếm một hậu duệ Thần Long Đại Hiệp mới trong khi đối đầu với Tắc Kè Bông.",
        "image": "https://image.tmdb.org/t/p/w500/kDp1vUBi32bWaaCmBF7YgghjLE5.jpg"
    }
]

# Trang chủ & Tìm kiếm
@app.route('/')
def index():
    query = request.args.get('q', '').strip()
    
    # Chúng ta lấy bộ phim đầu tiên (Dune) làm phim nổi bật ở banner đầu trang chủ
    featured_movie = movies[0] if movies else None
    
    if query:
        # Lọc phim theo tên (không phân biệt chữ hoa, chữ thường)
        filtered_movies = [m for m in movies if query.lower() in m['title'].lower()]
        return render_template('index.html', movies=filtered_movies, search_query=query, featured_movie=None) # Ẩn banner khi đang tìm kiếm
        
    return render_template('index.html', movies=movies, featured_movie=featured_movie)

# Trang chi tiết phim
@app.route('/movie/<int:movie_id>')
def detail(movie_id):
    movie = next((m for m in movies if m['id'] == movie_id), None)
    if movie:
        return render_template('detail.html', movie=movie)
    return "Phim không tồn tại", 404

if __name__ == '__main__':
    app.run(debug=True)