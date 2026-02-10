import sys
from src.logger import logging
def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Build a detailed error message with filename, line number, and the exception message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "<unknown>"
    line_no = exc_tb.tb_lineno if exc_tb else -1
    return (
        "Error occurred in python script [{0}] at line [{1}]: {2}"
        .format(file_name, line_no, str(error))
    )



class CustomException(Exception):

    def __init__(self, error_message: str, error_detail: sys):
        super().__init__(error_message)
        
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_no = exc_tb.tb_lineno
        self.error_message = (
            f"Error occurred in python script [{file_name}] "
            f"at line [{line_no}]: {error_message}"
        )

    def __str__(self):
        return self.error_message
    
    '''

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero error")
        raise CustomException(e, sys)

        '''
        
