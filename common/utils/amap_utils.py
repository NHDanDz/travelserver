import os

from common.utils import load_yaml
from common.utils.req_utils import get
from dotenv import load_dotenv
from apps.base.log import logger  # Thêm dòng này

load_dotenv()

# Read application configuration
cfg = load_yaml("config/application.yaml")

# Key obtained from the AMap Open Platform
api_key = os.environ.get("GAO_DE_API_KEY") or cfg.get("gao_de").get("api_key")
api_url = os.environ.get("GAO_DE_API_URL") or cfg.get("gao_de").get("api_url")
nva_url = os.environ.get("GAO_DE_NVA_URL") or cfg.get("gao_de").get("nva_url")


async def gaode(pre_name, addr_name):
    para = {
        'key': api_key,
        'address': (pre_name or "") + addr_name
    }

    try:
        res = get(api_url + "/geocode/geo", para)
        if not res or 'geocodes' not in res or not res['geocodes']:
            # Trả về dữ liệu mặc định nếu không tìm thấy kết quả
            addr_local = {
                "des_name": addr_name,
                "formatted_address": addr_name,
                "country": "Việt Nam",
                "province": "Hà Nội",
                "city_code": "01",
                "city": "Hà Nội",
                "ad_code": "01",
                "street": "",
                "number": "",
                "location": "105.8342,21.0278"  # Tọa độ mặc định của Hà Nội
            }
            annotate_url = f"{nva_url}/?dest=105.8342,21.0278&destName={pre_name + addr_name}&key={api_key}"
            return addr_local, annotate_url
            
        data = res['geocodes'][0]
        addr_local = {
            "des_name": addr_name,
            "formatted_address": data.get("formatted_address"),
            "country": data.get("country"),
            "province": data.get("province"),
            "city_code": data.get("citycode"),
            "city": data.get("city"),
            "ad_code": data.get("adcode"),
            "street": data.get("street"),
            "number": data.get("number"),
            "location": data.get("location")
        }

        dest = addr_local.get("location")
        annotate_url = f"{nva_url}/?dest={dest}&destName={pre_name + addr_name}&key={api_key}"
        return addr_local, annotate_url
        
    except Exception as e:
        logger.error(f"Error in gaode: {e}")
        # Trả về dữ liệu mặc định nếu có lỗi
        addr_local = {
            "des_name": addr_name,
            "formatted_address": addr_name,
            "country": "Việt Nam",
            "province": "Hà Nội",
            "city_code": "01",
            "city": "Hà Nội",
            "ad_code": "01",
            "street": "",
            "number": "",
            "location": "105.8342,21.0278"  # Tọa độ mặc định của Hà Nội
        }
        annotate_url = f"{nva_url}/?dest=105.8342,21.0278&destName={pre_name + addr_name}&key={api_key}"
        return addr_local, annotate_url


async def circum_address(key_word: str):
    """
    Surrounding information query
    """
    para = {
        'key': api_key,
        'keywords': key_word,
        # 'city': "beijing",
        'offset': 20,
        'page': 1,
        'extensions': 'all'
    }
    res = get(api_url + "/place/text", para)
    return res


if __name__ == '__main__':
    # a, u = gaode("", "West Lake")
    # print(a, u)
    print(circum_address("West Lake"))
