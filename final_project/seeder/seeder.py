import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.models import *
from app import STORE_NAME

Texts(**{"title": "Greetings", "info": f"Вас приветствует магазин {STORE_NAME}"}).save()
Texts(**{"title": "About", "info": f"Вас приветствует телеграм магазин {STORE_NAME}.\nТут вы сможете дешево купить комплектующие для вашего ПК"}).save()
Texts(**{"title": "Last news", "info": f"В нашем магазине акция ! купите любой AMD процессор и получите игру в подарок !"}).save()

nvidia_video = Category(**{"title": "RTX"}).save()
amd_video = Category(**{"title": "RX"}).save()

intel_processor = Category(**{"title": "i5"}).save()
amd_processor = Category(**{"title": "ryzen 5"}).save()

motherboard_AM4 = Category(**{"title": "Для AMD процессора"}).save()
motherboard_Z370 = Category(**{"title": "Для intel процессора"}).save()

ozu = Category(**{"title": "DDR4"}).save()

processors = Category(**{"title": "Процессор"}).save()
processors.add_subcategory(intel_processor)
processors.add_subcategory(amd_processor)
processors.save()

videos = Category(**{"title": "Видеокарты"}).save()
videos.add_subcategory(nvidia_video)
videos.add_subcategory(amd_video)
videos.save()

motherboards = Category(**{"title": "Материнская плата"}).save()
motherboards.add_subcategory(motherboard_AM4)
motherboards.add_subcategory(motherboard_Z370)
motherboards.save()

ozus = Category(**{"title": "Оперативная память"}).save()
ozus.add_subcategory(ozu)
ozus.save()

product = Product(**{
    "title": "i5-9400kf",
    "description": "Производительный процессор intel, выпущен в 2019",
    "price": 6000,
    "new_price": 0,
    "is_discount": False,
    "category": intel_processor,
    }
).save()
_photo = open('photo/one.jpg', 'rb')
product.photo.put(_photo, content_type= 'image/jpeg')
product.save()


product = Product(**{
    "title": "AMD RYZEN 5 3600",
    "description": "Производительный процессор AMD, выпущен в 2019",
    "price": 6000,
    "new_price": 5500,
    "is_discount": True,
    "category": amd_processor,
    }
).save()
_photo = open('photo/one.jpg', 'rb')
product.photo.put(_photo, content_type= 'image/jpeg')
product.save()

product = Product(**{
    "title": "RTX 2070 Super",
    "description": "Высокопроизводительная видеокарта от NVIDIA",
    "price": 16000,
    "new_price": 0,
    "is_discount": False,
    "category": nvidia_video,
    }
).save()
_photo = open('photo/one.jpg', 'rb')
product.photo.put(_photo, content_type= 'image/jpeg')
product.save()

product = Product(**{
    "title": "RX 5700 XT",
    "description": "Высокопроизводительная видеокарта от AMD",
    "price": 11000,
    "new_price": 0,
    "is_discount": False,
    "category": amd_video,
    }
).save()
_photo = open('photo/one.jpg', 'rb')
product.photo.put(_photo, content_type= 'image/jpeg')
product.save()

product = Product(**{
    "title": "MSI Z370",
    "description": "Отличная плата для 6-ядерных процессоров",
    "price": 4000,
    "new_price": 3500,
    "is_discount": True,
    "category": motherboard_Z370,
    }
).save()
_photo = open('photo/one.jpg', 'rb')
product.photo.put(_photo, content_type= 'image/jpeg')
product.save()

product = Product(**{
    "title": "MSI B450",
    "description": "Отличная плата для 6-ядерных процессоров",
    "price": 2500,
    "new_price": 0,
    "is_discount": False,
    "category": motherboard_AM4,
    }
).save()
_photo = open('photo/one.jpg', 'rb')
product.photo.put(_photo, content_type= 'image/jpeg')
product.save()

product = Product(**{
    "title": "8 GB 3200",
    "description": "Быстрая оперативная память",
    "price": 1000,
    "new_price": 0,
    "is_discount": False,
    "category": ozu,
    }
).save()
_photo = open('photo/one.jpg', 'rb')
product.photo.put(_photo, content_type= 'image/jpeg')
product.save()
