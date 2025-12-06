from abc import ABC, abstractmethod


# ---------- Abstract Products ----------

class SUV(ABC):
    @abstractmethod
    def specs(self):
        pass


class Coupe(ABC):
    @abstractmethod
    def specs(self):
        pass

# ---------- Benz ----------

class BenzSUV(SUV):
    def specs(self):
        return "Benz SUV - موتور 3.0L، سیستم 4MATIC، لوکس خانوادگی"


class BenzCoupe(Coupe):
    def specs(self):
        return "Benz Coupe - دو در اسپرت، موتور 2.0 توربو"


# ---------- BMW ----------

class BmwSUV(SUV):
    def specs(self):
        return "BMW SUV - سری X، هندلینگ قوی، موتور 3.0 TwinPower"


class BmwCoupe(Coupe):
    def specs(self):
        return "BMW Coupe - سری 4، اسپرت، دیفرانسیل عقب"


# ---------- Abstract Factory ----------

class CarFactory(ABC):
    @abstractmethod
    def create_suv(self) -> SUV:
        pass

    @abstractmethod
    def create_coupe(self) -> Coupe:
        pass

# ---------- Concrete Factories ----------
class BenzFactory(CarFactory):
    def create_suv(self) -> SUV:
        return BenzSUV()

    def create_coupe(self) -> Coupe:
        return BenzCoupe()

class BmwFactory(CarFactory):
    def create_suv(self) -> SUV:
        return BmwSUV()

    def create_coupe(self) -> Coupe:
        return BmwCoupe()

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
