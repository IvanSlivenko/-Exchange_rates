from peewee import (SqliteDatabase, Model, IntegerField, DoubleField,
                    DateTimeField, datetime as peewee_datetime)

db = SqliteDatabase("golden-eye.db")# підключаємо базу данних

class XRate(Model):
    class Meta:
        database = db # назва бази данних
        db_table = "xrates" # назва таблиці
        indexes = (
            (("from_currency", "to_currency"), True),
        )# індекси та ознака унікальності = True
    from_currency = IntegerField()
    to_currency = IntegerField()
    rate = DoubleField()
    updated = DateTimeField(default=peewee_datetime.datetime.now)