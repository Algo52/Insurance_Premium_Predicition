from fileinput import filename
import os,sys


class InsuranceException(Exception):

    def __init__(self,error_message:Exception,error_detail:sys) :
        super().__init__(error_message)
        #Exception(error_message) both are same
        
        self.error_message=error_message
        self.error_message=InsuranceException.get_detailed_error_message(error_message=error_message,
                                                                       error_detail=error_detail
                                                                        )

    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_detail:sys)-> str: #getting eroor in form of string
        """
        error_message: Exception object
        error_detail: object of sys module
        """
        _,_,exec_tb= error_detail.exc_info()
        
        line_number=exec_tb.tb_frame.f_lineno
        filename=exec_tb.tb_frame.f_code.co_filename
        error_message=f"Error occured in script:[{filename}] at line number:[{line_number}] error message is :[{error_message}]"

        return error_message

    def __str__(self):
        return self.error_message
    
    def __repr__(self) -> str:
        return InsuranceException.__name__.str()