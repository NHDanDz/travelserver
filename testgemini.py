try:
    import google.generativeai as genai
    print("Thư viện Google Generative AI đã được cài đặt thành công!")
except ImportError:
    print("Lỗi: Chưa cài đặt thư viện Google Generative AI.")
    print("Vui lòng cài đặt bằng lệnh: pip install google-generativeai")
    exit(1)

def test_gemini_api():
    # Thay API key thật của bạn vào đây
    api_key = ""   
    
    print(f"Sử dụng API key: {api_key}")
    
    try:
        # Cấu hình Gemini API
        genai.configure(api_key=api_key)
        
        # Tạo system prompt và user prompt
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
        
        # Thử với GenerativeModel API (cách đang hoạt động)
        print("Gọi API với GenerativeModel API (gemini-2.0-flash)...")
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(combined_prompt)
        
        print("\n=== PHẢN HỒI ĐẦY ĐỦ TỪ GEMINI API ===")
        print(response.text)
        
        return True
            
    except Exception as e:
        print(f"Lỗi: {e}")
        return False

# Demo sử dụng API tương tự như trong dự án CoLy
def test_summarize_content():
    print("\n===== DEMO HÀM TƯƠNG TỰ NHƯ TỪ DỰ ÁN COLY =====")
    
    # Thay API key thật của bạn vào đây
    api_key = "AIzaSyDjfHLGQLFOFEuxFVk-GYDCU5WU52MU3X0"
    
    try:
        genai.configure(api_key=api_key)
        
        keyword = "Sapa"
        content = """
        Sa Pa là một thị trấn miền núi thuộc tỉnh Lào Cai ở Tây Bắc Việt Nam. Thị trấn này nằm ở độ cao 1600m so với mực nước biển, được bao quanh bởi những dãy núi hùng vĩ, thung lũng và ruộng bậc thang.
        Sa Pa nổi tiếng với cảnh quan thiên nhiên tuyệt đẹp, khí hậu mát mẻ, và là nơi sinh sống của nhiều dân tộc thiểu số như H'Mông, Dao đỏ, Tày, Giáy. 
        Du khách đến Sa Pa có thể tham gia các hoạt động như leo núi Fansipan - "nóc nhà Đông Dương", đi bộ qua các bản làng, thưởng thức ẩm thực địa phương, và tham quan chợ Sa Pa nhộn nhịp.
        """
        
        prompt = (
            f"Hãy đọc nội dung sau và so sánh với nội dung mà từ khóa '{keyword}' yêu cầu."
            f"Nếu nội dung không liên quan hoặc không phù hợp, hãy trả về đúng một dòng: 'None'."
            f"Nếu nội dung phù hợp, hãy đọc dữ liệu đầu vào và tạo lịch trình du lịch 7 ngày ở Sapa."
            f"Hãy trả về dữ liệu dưới dạng JSON với cấu trúc:"
            f"""
            {{
              "trip": {{
                "location": "Sapa",
                "duration_days": 7,
                "itinerary": [
                  {{
                    "day": 1,
                    "activities": [
                      {{
                        "time": "07:00",
                        "place": "Tên địa điểm",
                        "coordinates": {{
                          "latitude": 22.3363,
                          "longitude": 103.8387
                        }},
                        "rating": 4.5,
                        "note": "Mô tả ngắn gọn"
                      }}
                    ]
                  }}
                ]
              }}
            }}
            """
            f"\n\n{content}"
        )

        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(prompt)
        
        print("\n=== PHẢN HỒI ĐẦY ĐỦ TỪ HÀM TƯƠNG TỰ SUMMARIZE_CONTENT ===")
        print(response.text)
        
        return True
        
    except Exception as e:
        print(f"Lỗi khi gọi hàm: {e}")
        return False

if __name__ == "__main__":
    print("===== KIỂM TRA GEMINI API =====")
    test_gemini_api()
 