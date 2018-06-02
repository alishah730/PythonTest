class EmpIdDescriptor:



    def __get__(self, obj, owner):

        return self.__empid



    def __set__(self, obj, value):

        if hasattr(obj, 'empid'):

            raise ValueError("'empid' is read only attribute")

        if not isinstance(value, int):

            raise TypeError("'empid' must be an integer.")

        self.__empid = value    