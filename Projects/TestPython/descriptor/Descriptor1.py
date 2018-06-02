class EmpNameDescripor:
    def __get__(self, instance, owner):
        return self.__empname

    def __set__(self, instance, value):
        if not isinstance(value,str):
            raise TypeError("'empname' must be  a String")
        self.__empname = value

