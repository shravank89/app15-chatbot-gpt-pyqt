import sys
from PyQt6.QtWidgets import QApplication, QLineEdit, QPushButton, QMainWindow, QTextEdit

from PyQt6.QtGui import QIcon
from backend import ChatBot
import threading


class MainWindow(QMainWindow):
    def __init__(self):
        self.chatter_bot = ChatBot()
        super().__init__()
        self.setWindowTitle("Chatterbot")
        self.setMinimumSize(580, 400)
        self.setWindowIcon(QIcon("icons/chatbot.png"))

        self.chat_box = QTextEdit(self)
        self.chat_box.setGeometry(10, 10, 480, 320)
        self.chat_box.setReadOnly(True)

        self.text_box = QLineEdit(self)
        self.text_box.setGeometry(10, 340, 480, 40)
        self.text_box.setPlaceholderText("Hey, How can I help you today?")
        self.text_box.returnPressed.connect(self.send_chat)

        self.send_button = QPushButton(self)
        self.send_button.setIcon(QIcon("icons/send_button.png"))
        self.send_button.setGeometry(500, 340, 60, 40)

        self.send_button.clicked.connect(self.send_chat)


    def send_chat(self):
        query = self.text_box.text()
        self.chat_box.append(f"<p style='color:#333333'>Me: {query}</p>")
        self.text_box.clear()
        thread = threading.Thread(target=self.get_chatter_bot_response, args=(query,))
        thread.start()

    def get_chatter_bot_response(self,query):
        response = self.chatter_bot.get_response(query)
        self.chat_box.append(f"<p style='color:#333333; background-color:#E9E9E9'>Bot: {response}</p>")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    chatbot = MainWindow()
    chatbot.show()
    sys.exit(app.exec())