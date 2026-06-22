from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)


class BaseDevice(ABC):
    factory_name = "Rikkei Smart Factory"
    base_maintenance_cost = 1000000

    def __init__(self, device_code, device_name, operating_hours=0):
        self.device_code = device_code
        self.device_name = device_name
        self.__operating_hours = operating_hours

    @property
    def operating_hours(self):
        return self.__operating_hours

    @operating_hours.setter
    def operating_hours(self, value):
        if value >= 0:
            self.__operating_hours = value

    @property
    def device_name(self):
        return self.__device_name

    @device_name.setter
    def device_name(self, value):
        self.__device_name = " ".join(value.strip().upper().split())

    @staticmethod
    def validate_device_code(device_code):
        return (
            len(device_code) == 10
            and device_code[0].isalpha()
        )

    @classmethod
    def update_maintenance_cost(cls, new_cost):
        cls.base_maintenance_cost = new_cost

    def __add__(self, other):
        if not isinstance(other, BaseDevice):
            raise TypeError(
                "[Lỗi] (ERR-IOT-04): Lỗi kiểu dữ liệu! Không thể thực hiện toán tử với đối tượng ngoài hệ thống."
            )

        return self.operating_hours + other.operating_hours

    def __lt__(self, other):
        if not isinstance(other, BaseDevice):
            raise TypeError(
                "[Lỗi] (ERR-IOT-04): Lỗi kiểu dữ liệu! Không thể thực hiện toán tử với đối tượng ngoài hệ thống."
            )

        return self.operating_hours < other.operating_hours

    @abstractmethod
    def track_performance(self):
        pass

    @abstractmethod
    def run_diagnostic(self):
        pass


class ProductionRobot(BaseDevice):
    def __init__(
        self,
        device_code,
        device_name,
        operating_hours=0,
        completed_products=0
    ):
        super().__init__(
            device_code,
            device_name,
            operating_hours
        )
        self.completed_products = completed_products

    def track_performance(self):
        if self.operating_hours == 0:
            return 0

        return round(
            self.completed_products /
            self.operating_hours,
            2
        )

    def run_diagnostic(self):
        if self.completed_products > 10000:
            return (
                "Cảnh báo bảo dưỡng: "
                "Sản lượng vượt 10,000 sản phẩm."
            )

        return "Robot hoạt động bình thường."


class ThermalSensor(BaseDevice):
    def __init__(
        self,
        device_code,
        device_name,
        operating_hours=0,
        current_temperature=25.0,
        safety_threshold=80.0
    ):
        super().__init__(
            device_code,
            device_name,
            operating_hours
        )

        self.current_temperature = current_temperature
        self.safety_threshold = safety_threshold

    def track_performance(self):
        return abs(
            self.safety_threshold
            - self.current_temperature
        )

    def run_diagnostic(self):
        if self.current_temperature > self.safety_threshold:
            return (
                f"Nguy hiểm: Vượt ngưỡng nhiệt! "
                f"(Nhiệt độ hiện tại: "
                f"{self.current_temperature} độ C / "
                f"Ngưỡng an toàn: "
                f"{self.safety_threshold} độ C)"
            )

        return "Nhiệt độ an toàn."


class HybridSmartActuator(
    ProductionRobot,
    ThermalSensor
):
    def __init__(
        self,
        device_code,
        device_name,
        operating_hours=0,
        completed_products=0,
        current_temperature=25.0,
        safety_threshold=80.0
    ):
        BaseDevice.__init__(
            self,
            device_code,
            device_name,
            operating_hours
        )

        self.completed_products = completed_products
        self.current_temperature = current_temperature
        self.safety_threshold = safety_threshold

    def track_performance(self):
        if self.operating_hours == 0:
            return 0

        return round(
            self.completed_products /
            self.operating_hours,
            2
        )

    def run_diagnostic(self):
        if self.current_temperature > self.safety_threshold:
            return (
                f"Nguy hiểm: Vượt ngưỡng nhiệt! "
                f"(Nhiệt độ hiện tại: "
                f"{self.current_temperature} độ C / "
                f"Ngưỡng an toàn: "
                f"{self.safety_threshold} độ C)"
            )

        if self.completed_products > 10000:
            return (
                "Cảnh báo bảo dưỡng: "
                "Sản lượng vượt 10,000 sản phẩm."
            )

        return "Hybrid hoạt động bình thường."


class MQTTEngineGateway:
    def process_stream(self, device):
        print(
            "[Hệ thống MQTT Engine]: "
            "Đang khởi tạo băng thông kết nối dữ liệu IoT..."
        )

        print(
            f"Dữ liệu của thiết bị "
            f"{device.device_code} "
            f"đã được đóng gói và xuất chuỗi "
            f"luồng thành công."
        )


class ERPReportGateway:
    def process_stream(self, device):
        print(
            "[ERP Gateway]: "
            "Đồng bộ dữ liệu quản trị..."
        )

        print(
            f"Dữ liệu thiết bị "
            f"{device.device_code} "
            f"đã được ghi nhận vào ERP."
        )


def export_telemetry_data(
    data_gateway,
    device_object
):
    try:
        data_gateway.process_stream(
            device_object
        )

        print(
            "Xác thực cổng ngoại vi "
            "bằng Duck Typing thành công!"
        )

    except AttributeError:
        print(
            "[Lỗi] (ERR-IOT-05): "
            "Xung đột kiến trúc! "
            "Không thể xuất dữ liệu do "
            "cấu hình cổng ngoại vi "
            "không tương thích."
        )


def device_required(device):
    if device is None:
        print(
            "[Lỗi] (ERR-IOT-02): "
            "Thao tác bị từ chối! "
            "Hệ thống chưa có thông tin "
            "thiết bị hoạt động."
        )
        return False

    return True


def main():
    devices_list = []
    current_device = None

    while True:

        print("""
===========================
RIKKEI SMART FACTORY IOT
===========================
1. Đăng ký thiết bị
2. Xem thông tin thiết bị
3. Check-in vận hành
4. Chẩn đoán kỹ thuật
5. Operator Overloading
6. Xuất dữ liệu ngoại vi
7. Thoát
===========================
""")

        choice = input(
            "Chọn chức năng (1-7): "
        )

        try:

            if choice == "1":

                print(
                    "\n--- ĐĂNG KÝ THIẾT BỊ IOT MỚI ---"
                )

                print(
                    "1. Production Robot"
                )
                print(
                    "2. Thermal Sensor"
                )
                print(
                    "3. Hybrid Smart Actuator"
                )

                device_type = input(
                    "Chọn phân loại thiết bị (1-3): "
                )

                code = input(
                    "Nhập mã thiết bị 10 ký tự: "
                )

                if not BaseDevice.validate_device_code(
                    code
                ):
                    print(
                        "[Lỗi] (ERR-IOT-01): "
                        "Mã thiết bị không hợp lệ!"
                    )
                    continue

                name = input(
                    "Nhập tên thiết bị: "
                )

                if device_type == "1":

                    current_device = (
                        ProductionRobot(
                            code,
                            name
                        )
                    )

                    print(
                        "[Thành công]: "
                        "Đăng ký Robot sản xuất "
                        "thành công!"
                    )

                elif device_type == "2":

                    current_device = (
                        ThermalSensor(
                            code,
                            name
                        )
                    )

                    print(
                        "[Thành công]: "
                        "Đăng ký Cảm biến "
                        "thành công!"
                    )

                elif device_type == "3":

                    current_device = (
                        HybridSmartActuator(
                            code,
                            name
                        )
                    )

                    print(
                        "[Thành công]: "
                        "Đăng ký Hybrid "
                        "thành công!"
                    )

                else:
                    print(
                        "[Lỗi] (ERR-IOT-06): "
                        "Lựa chọn không hợp lệ!"
                    )
                    continue

                devices_list.append(
                    current_device
                )

                print(
                    "Tên thiết bị:",
                    current_device.device_name
                )

            elif choice == "2":

                if not device_required(
                    current_device
                ):
                    continue

                print(
                    "\n--- THÔNG TIN THIẾT BỊ HIỆN TẠI ---"
                )

                print(
                    "Loại thiết bị:",
                    type(
                        current_device
                    ).__name__
                )

                print(
                    "Nhà máy:",
                    current_device.factory_name
                )

                print(
                    "Mã thiết bị:",
                    current_device.device_code
                )

                print(
                    "Tên thiết bị:",
                    current_device.device_name
                )

                print(
                    "Số giờ vận hành:",
                    current_device.operating_hours
                )

                print(
                    "[Hệ thống MRO]:",
                    " -> ".join(
                        cls.__name__
                        for cls in
                        current_device.__class__.mro()
                    )
                )

            elif choice == "3":

                if not device_required(
                    current_device
                ):
                    continue

                print(
                    "\n--- GHI NHẬN "
                    "SỐ LIỆU VẬN HÀNH ---"
                )

                hours = float(
                    input(
                        "Nhập số giờ chạy mới phát sinh: "
                    )
                )

                if hours <= 0:
                    raise ValueError

                current_device.operating_hours += (
                    hours
                )

                if isinstance(
                    current_device,
                    (
                        ProductionRobot,
                        HybridSmartActuator
                    )
                ):
                    products = int(
                        input(
                            "Nhập số lượng sản phẩm hoàn thành mới bổ sung: "
                        )
                    )

                    if products < 0:
                        raise ValueError

                    current_device.completed_products += (
                        products
                    )

                logging.info(
                    "Cập nhật dữ liệu vận hành"
                )

                print(
                    "Chỉ số hiệu suất:",
                    current_device.track_performance()
                )

            elif choice == "4":

                if not device_required(
                    current_device
                ):
                    continue

                print(
                    "\n--- QUY TRÌNH "
                    "TỰ CHẨN ĐOÁN ---"
                )

                print(
                    current_device.run_diagnostic()
                )

                print(
                    "Định mức chi phí "
                    "bảo trì:",
                    f"{BaseDevice.base_maintenance_cost:,}",
                    "VND"
                )

            elif choice == "5":

                if not device_required(
                    current_device
                ):
                    continue

                if len(devices_list) < 2:
                    print(
                        "Cần ít nhất "
                        "2 thiết bị."
                    )
                    continue

                code = input(
                    "Nhập mã thiết bị đối ứng: "
                )

                other = None

                for d in devices_list:
                    if d.device_code == code:
                        other = d
                        break

                if other:

                    print(
                        "\n[Kết quả So sánh (__lt__)]:"
                    )

                    if current_device < other:
                        print(
                            "Thiết bị hiện tại "
                            "ít hao mòn hơn."
                        )
                    else:
                        print(
                            "Thiết bị hiện tại "
                            "hao mòn nhiều hơn "
                            "hoặc bằng."
                        )

                    print(
                        "\n[Kết quả Tổng hợp (__add__)]:"
                    )

                    print(
                        current_device + other,
                        "giờ"
                    )

            elif choice == "6":

                if not device_required(
                    current_device
                ):
                    continue

                print(
                    "1. MQTT Gateway"
                )

                print(
                    "2. ERP Gateway"
                )

                gateway_choice = input(
                    "Chọn cổng: "
                )

                if gateway_choice == "1":
                    gateway = (
                        MQTTEngineGateway()
                    )
                else:
                    gateway = (
                        ERPReportGateway()
                    )

                export_telemetry_data(
                    gateway,
                    current_device
                )

            elif choice == "7":

                print(
                    "\nCảm ơn bạn đã "
                    "sử dụng hệ thống "
                    "Quản lý Thiết bị "
                    "Rikkei Smart Factory IoT Pro!"
                )

                break

            else:

                print(
                    "[Lỗi] (ERR-IOT-06): "
                    "Lựa chọn không hợp lệ!"
                )

        except ValueError:

            print(
                "[Lỗi] (ERR-IOT-03): "
                "Định dạng dữ liệu sai! "
                "Giá trị nhập vào phải "
                "là số lớn hơn 0."
            )

        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()

