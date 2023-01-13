from datetime import date
from dateutil.relativedelta import relativedelta

from utils.rapper_function import func_loger


class YearMonth:

    @staticmethod
    @func_loger
    def get_year_month(month_increment: int):
        """
        Configures year and month
        :param month_increment: Month increment
        :return: Returns year month
        """
        today = date.today()
        year_month_day = today + relativedelta(months=+month_increment)
        year_month_day_tostring = str(year_month_day)
        year_month = year_month_day_tostring[:7]
        return year_month

    @staticmethod
    @func_loger
    def get_current_date():
        """
        Configures current date
        :return: Returns today's date
        """
        today = date.today()
        return today

    """
    "%d/%m/%Y" ==> dd/mm/YY
    "%m/%d/%y" ==> mm/dd/y
    "%b-%d-%Y" ==> Month abbreviation, day and year
    """
    @staticmethod
    @func_loger
    def get_current_formatted_date(date_format: str):
        """
        Configures current date formatted as above
        :param date_format: Date format
        :return: Returns formatted date
        """
        today = date.today()
        formatted_date = today.strftime(date_format)
        return formatted_date
