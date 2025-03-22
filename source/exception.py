import sys

def errorMessageFun(error , errorDetail:sys):

    _,_,exce_tab = errorDetail.exc_info()
    fileName = exce_tab.tb_frame.f_code.co_filename

    errorMessage = f"error ocurred in python script name {fileName} line number {exce_tab.tb_lineno} error messsge {str(error)}"

    return errorMessage

class customException(Exception):
    def __init__(self,errorMessage,errorDetail:sys):
            super().__init__(errorMessage)
            self.errorMessagge = errorMessageFun(errorMessage , errorDetail=errorDetail)
    
    def __str__(self):
         return self.errorMessagge

