class Vehicle:
      def _init_(self,make,model,color):
           self.make = make
           self.model = model
           self.color = color
      def move(self):
          print("starts moving")     
      def hoot(self):
         print("Honk honk")

class Bus(Vehicle):
      def _init_(make,model,color, capacity):   
          super()._init_( self,make,model,color)  
      def start_boarding(self):
          print("The bus is now boarding")    

class lorry(Vehicle):
      def _init_(self,make,model,color,max_load):
          super(). _init_ (make,model,color)
          self.max_load = max_load
      def load(self) :  
        print("start loading") 



