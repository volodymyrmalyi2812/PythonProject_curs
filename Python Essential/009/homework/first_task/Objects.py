class LinkService:
    def __init__(self, database_name):
        self.__database_name = database_name

    @property
    def database_name(self):
        return self.__database_name

    @database_name.setter
    def database_name(self, database_name):
        self.__database_name = database_name

link_service = LinkService('link_service')