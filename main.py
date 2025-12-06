from factories.BenzFactory import BenzFactory
from factories.BmwFactory import BmwFactory


# ---------- Client Code ----------
def manage_customer_cars(brand: str):
    # انتخاب کارخانه براساس برند
    if brand.lower() == "benz":
        factory = BenzFactory()
    elif brand.lower() == "bmw":
        factory = BmwFactory()
    else:
        raise ValueError("برند پشتیبانی نمی‌شود")

    # ساخت ماشین‌ها بدون وابستگی به کلاس‌های واقعی
    suv = factory.create_suv()
    coupe = factory.create_coupe()

    print("SUV مشتری:", suv.specs())
    print("Coupe مشتری:", coupe.specs())

# استفاده از کد
if __name__ == "__main__":
    manage_customer_cars("benz")
    print("-" * 40)
    manage_customer_cars("bmw")
