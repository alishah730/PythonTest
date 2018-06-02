class Employee:



    empid = EmpIdDescriptor()

    empname = EmpNameDescriptor()



    def __init__(self, emp_id, emp_name):

        self.empid = emp_id

        self.empname = emp_name