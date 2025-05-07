from utils.settings_loader import app_settings
import traceback
import datetime
import os


class Logger:
    LOG_PATH = app_settings.log_path

    @staticmethod
    def error(ex: Exception):
        """Запись ошибки в лог и вывод в консоль

        Args:
            ex (Exception): исключение, сгенерированное ошибкой
        """
        if not os.path.isdir(Logger.LOG_PATH):
            os.mkdir(Logger.LOG_PATH)
        error = traceback.TracebackException(
            exc_type=type(ex), exc_traceback=ex.__traceback__, exc_value=ex
        ).stack[-1]
        time_now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        date_now = datetime.datetime.now().strftime("%d-%m-%Y")
        log_name = os.path.join(Logger.LOG_PATH, f"{date_now}.log")
        if os.path.exists(log_name):
            file = open(log_name, "at", encoding="utf-8")
        else:
            file = open(log_name, "xt", encoding="utf-8")
        log_string = (
            f"! [{time_now}] {error.filename} ({error.lineno}) :"
            + f" [{ex.__class__.__name__}] {ex} (string: {error.line})\n"
        )
        file.write(log_string)
        file.close()
        print(log_string)

    @staticmethod
    def info(info: str):
        """Запись информации в лог

        Args:
            info (str): Информация для записи
        """
        if not os.path.isdir(Logger.LOG_PATH):
            os.mkdir(Logger.LOG_PATH)
        time_now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        date_now = datetime.datetime.now().strftime("%d-%m-%Y")
        log_name = os.path.join(Logger.LOG_PATH, f"{date_now}.log")
        if os.path.exists(log_name):
            file = open(log_name, "at", encoding="utf-8")
        else:
            file = open(log_name, "xt", encoding="utf-8")
        log_string = f"* [{time_now}] {info}\n"
        file.write(log_string)
        file.close()
        print(log_string)
