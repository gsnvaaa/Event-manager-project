import re

class Helpers:
    @staticmethod
    def validate_date(date_str):
       
        date_pattern = r'^\d{4}-\d{2}-\d{2}$'
        
        
        if re.match(date_pattern, date_str):
            return True
        else:
            return False
