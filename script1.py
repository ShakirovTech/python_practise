class TelegramAlert:
    def __init__(self, chat_id):
        self.chat_id = chat_id

    def send(self, message):
        print(f'[Telegram] Message in chat {self.chat_id}: {message}')


class EmailAlert:
    def __init__(self, email):
        self.email = email

    def send(self, message):
        print(f'[Email] Letter to email {self.email}: {message}')


class LogAlert:
    def __init__(self, file_path):
        self.file_path = file_path

    def send(self, message):
        print(f'[Log] Commit the file {self.file_path}: {message}')


def broadcast_alert(channels, message):
    for channel in channels:
        channel.send(message)


tg = TelegramAlert(54321098)
mail = EmailAlert("admin@company.com")
logger = LogAlert("/var/log/server_errors.log")

alert_channels = [tg, mail, logger]

broadcast_alert(alert_channels, "КРИТИЧЕСКАЯ ОШИБКА: Сервер eu-central недоступен")
