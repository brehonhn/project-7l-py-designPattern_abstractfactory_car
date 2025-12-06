# 🚘 Car Management System – Abstract Factory Design Pattern (Python)

این پروژه یک سیستم مدیریت خودرو را پیاده‌سازی می‌کند که با استفاده از **الگوی طراحی Abstract Factory**، امکان ساخت خودروهای مختلف از برندهای متفاوت مانند **Benz** و **BMW** را به صورت ساخت‌یافته و قابل‌گسترش فراهم می‌کند.

---

## 🎯 هدف پروژه

- ایجاد خودروها بر اساس برند (Benz / BMW) بدون تغییر در کد اصلی
- ساخت "خانواده‌ای" از اشیای مرتبط:
  - SUV
  - Coupe
- پیاده‌سازی اصل **Open/Closed Principle**
- اضافه‌کردن برندهای جدید بدون نیاز به تغییر کدهای موجود
- جداسازی کامل منطق ساخت خودرو از منطق استفاده

---

## 🧩 معماری سیستم (Abstract Factory)

در این پروژه هر برند خودرو یک "کارخانه" است که انواع مدل‌های مرتبط را تولید می‌کند.

### ✔ Abstract Factory:
```python
class CarFactory(ABC):
    def create_suv(self): ...
    def create_coupe(self): ...

project/
│
├── factories/
│   ├── CarFactory.py
│   ├── BenzFactory.py
│   ├── BmwFactory.py
│
├── products/
│   ├── SUV.py
│   ├── Coupe.py
│   ├── BenzSUV.py
│   ├── BenzCoupe.py
│   ├── BmwSUV.py
│   ├── BmwCoupe.py
│
├── main.py
└── README.md

