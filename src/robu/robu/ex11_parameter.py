
import rclpy 
from rclpy.node import Node

class MinimalParameter(Node):
      def __init__(self):
            super().__init__('MinimalParameter')           ##super greift auf elternklasse zu (Node)

            self.declare_parameter('my_parameter')

            ##self.get_parameter('my_parameter')        ## parameter bekommen

            my_param=self.get_parameter('my_parameter')
            print("my_parameter: ", my_param)

def main():
      rclpy.init()
      node=MinimalParameter()
      rclpy.spin(node)

