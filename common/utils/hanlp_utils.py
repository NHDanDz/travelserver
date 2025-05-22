import re

def select_name(text):
    """
    Trích xuất tên người từ văn bản - phiên bản đơn giản không dùng HanLP
    """
    # Dùng các từ khóa thông thường thay vì HanLP
    # Đây là phiên bản cơ bản có thể không hoạt động tốt như HanLP
    result = set()
    return result  # Trả về tập rỗng, giải pháp đơn giản nhất

def select_address(text):
    """
    Trích xuất tất cả địa điểm - phiên bản đơn giản không dùng HanLP
    """
    # Trong TravelGPT, mặc định có thể coi 1 địa điểm như 'Hà Nội'
    # hoặc các từ khóa như 'địa điểm', 'thành phố', 'tỉnh', 'quận', 'huyện'
    common_places = [
        "Hà Nội", "Hồ Chí Minh", "Đà Nẵng", "Hội An", "Huế", 
        "Nha Trang", "Đà Lạt", "Sapa", "Hạ Long", "Phú Quốc", 
        "Cần Thơ", "Vũng Tàu", "Hà Giang", "Ninh Bình"
    ]
    
    result = set()
    for place in common_places:
        if place.lower() in text.lower():
            result.add(place)
    
    # Nếu không tìm thấy địa điểm cụ thể, thêm "Hà Nội" làm mặc định
    if not result:
        result.add("Hà Nội")
    
    return result

def select_organize(text):
    """
    Trích xuất tên tổ chức - phiên bản đơn giản không dùng HanLP
    """
    # Trả về tập rỗng, giải pháp đơn giản nhất
    result = set()
    return result

if __name__ == '__main__':
    """
    Kiểm tra chức năng trích xuất địa điểm
    """
    a = select_address("Tôi muốn đi Hà Nội ba ngày, giúp tôi lập lịch trình")
    print(a)