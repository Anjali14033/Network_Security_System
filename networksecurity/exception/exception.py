import sys
from networksecurity.logging import logfile

class NetworkSecurityException(Exception):
    """Custom exception class for network security errors."""

    def __init__(self, error, error_details: sys):
        _, _, exc_tb = error_details.exc_info()
        self.line_no = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.error_message = str(error)

        # Log automatically whenever exception is created
        logfile.error(self.__str__())

    def __str__(self):
        return "Error occurred in python script [{0}] line [{1}] → {2}".format(
            self.file_name, self.line_no, self.error_message
        )


if __name__ == "__main__":
    try:
        logfile.info("Entered try block")
        a = 1 / 0   # ❌ This will raise ZeroDivisionError
    except Exception as e:
        custom_exception = NetworkSecurityException(e, sys)

        # ✅ Instead of raising again, just print clean message
        print(custom_exception)
