from datetime import date
from dateutil.relativedelta import relativedelta


class YearMonth:

    @staticmethod
    def get_year_month(month_increment):
        today = date.today()
        year_month_day = today + relativedelta(months=+month_increment)
        year_month_day_tostring = str(year_month_day)
        year_month = year_month_day_tostring[:7]
        return year_month

    @staticmethod
    def get_current_date():
        today = date.today()
        return today

    """
    "%d/%m/%Y" ==> dd/mm/YY
    "%m/%d/%y" ==> mm/dd/y
    "%b-%d-%Y" ==> Month abbreviation, day and year
    """
    @staticmethod
    def get_current_formatted_date(date_format):
        today = date.today()
        formatted_date = today.strftime(date_format)
        return formatted_date
