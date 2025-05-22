# Thay thế dòng import
import google.generativeai as genai

# Thay thế cách cấu hình API key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Thay thế phần gọi API
try:
    # Tạo model từ Gemini
    model = genai.GenerativeModel('gemini-pro')
    
    # Tạo prompt từ system message và user message
    system_prompt = "Bạn là trợ lý du lịch."
    user_prompt = """Tôi muốn đi du lịch sa pa 7 ngày, hãy lập lịch trình giúp tôi chi tiết từ sáng đến tối. Viết dưới dạng file json và có tọa độ địa điểm và các đánh giá với cấu trúc sau {
  "trip": {
    "location": "Tên địa điểm du lịch",
    "duration_days": Số_ngày,
    "itinerary": [
      {
        "day": Số_thứ_tự_ngày,
        "activities": [
          {
            "time": "HH:MM",
            "place": "Tên địa điểm",
            "coordinates": {
              "latitude": Vĩ_độ,
              "longitude": Kinh_độ
            },
            "rating": Điểm_đánh_giá,  // Ví dụ: 4.5
            "note": "Mô tả ngắn gọn về địa điểm, lịch sử, không gian, trải nghiệm..."
          }
          // ... các hoạt động khác trong ngày
        ]
      }
      // ... các ngày tiếp theo
    ]
  }
}
"""
    
    # Kết hợp system prompt và user prompt
    combined_prompt = f"{system_prompt}\n\n{user_prompt}"
    
    # Gửi request đến Gemini
    response = model.generate_content(combined_prompt, generation_config={
        "temperature": 0.7,
        "max_output_tokens": 2048
    })
    
    print("API key hoạt động tốt!")
    print(f"Phản hồi: {response.text}")
except Exception as e:
    print(f"Lỗi: {e}")