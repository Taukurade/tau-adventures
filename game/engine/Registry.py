from peewee import *

Regisrty = SqliteDatabase(":memory:")


class RegMdl(Model):
    class Meta:
        database = Regisrty
