from datetime import date

def format_dates(start_date:date|None = None, end_date:date|None = None):
    today = date.today()

    if start_date is None and end_date is None:
        if today.month >= 8:
            start_date = date(year=today.year, month=8, day=1)
        else:
            start_date = date(year=today.year-1, month=8, day=1)
        end_date = date(year=today.year, month=today.month, day=today.day)
        
    elif start_date is None:
        start_date = date(year=2023, month=8, day=1)
        
    elif end_date is None:
        end_date = date(year=today.year, month=today.month, day=today.day)
        
    return start_date, end_date