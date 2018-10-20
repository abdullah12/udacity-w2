class Udacian:
   

   def __init__(self, name, city,enrollment,nanodegree,status):
      self.name = name
      self.city = city
      self.enrollment = enrollment
      self.nanodegree = nanodegree
      self.status = status
   

   def print_udacian(self):
      print ( self.name , ' is enrolled in ', self.city, 'studying',  self.nanodegree, ' with Ms. ', self.enrollment, 'he/she is', self.status  )


u = Udacian('ahmed','dammam','Elham','fullstack','ontrack')

u.print_udacian()
