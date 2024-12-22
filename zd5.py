import sys
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget

class ClassOperationsApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Работа с классами и JSON")
        self.setGeometry(100, 100, 600, 400)

        self.label = QLabel("Выберите операцию", self)
        self.label.setStyleSheet("font-size: 16px;")

        self.add_button = QPushButton("Добавить объект", self)
        self.add_button.clicked.connect(self.add_object)

        self.delete_button = QPushButton("Удалить объект", self)
        self.delete_button.clicked.connect(self.delete_object)

        self.compare_button = QPushButton("Сравнить объекты", self)
        self.compare_button.clicked.connect(self.compare_objects)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.add_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.compare_button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.data = {}

    def add_object(self):
        try:
            key = f"Object_{len(self.data) + 1}"
            self.data[key] = {"attribute": len(self.data) + 1}
            self.save_to_json()
            self.label.setText(f"Добавлен: {key}")
        except Exception as e:
            self.label.setText(f"Ошибка: {str(e)}")

    def delete_object(self):
        try:
            if self.data:
                key = list(self.data.keys())[-1]
                del self.data[key]
                self.save_to_json()
                self.label.setText(f"Удалён: {key}")
            else:
                self.label.setText("Нет объектов для удаления")
        except Exception as e:
            self.label.setText(f"Ошибка: {str(e)}")

    def compare_objects(self):
        try:
            if len(self.data) >= 2:
                keys = list(self.data.keys())
                obj1, obj2 = self.data[keys[-1]], self.data[keys[-2]]
                comparison = obj1["attribute"] > obj2["attribute"]
                result = f"{keys[-1]} {'больше' if comparison else 'меньше или равно'} {keys[-2]}"
                self.label.setText(result)
            else:
                self.label.setText("Недостаточно объектов для сравнения")
        except Exception as e:
            self.label.setText(f"Ошибка: {str(e)}")

    def save_to_json(self):
        with open("data_log.json", "w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClassOperationsApp()
    window.show()
    sys.exit(app.exec())
