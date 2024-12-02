import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TrajectorySubscriber(Node):

    def __init__(self):
        super().__init__('trajectory_subscriber')
        self.pose_subscriber = self.create_subscription(Twist, "trajectory", self.listener_callback, 10)
        # TODO: Create a subscriber of type Twist, that calls listener_callback
        # Your code here

        self.get_logger().info('Subscriber node has been started.')
        self.position = {'x': 0.0, 'z': 0.0, 'ry': 0.0}

    def listener_callback(self, msg : Twist):
        if msg.linear.z and msg.angular.y or msg.linear.z and msg.linear.x :
            print("Forbidden move")
        else :
            if msg.linear.x > 0 and not msg.angular.y :
                print("Go Forward")
            if msg.linear.x < 0 and not msg.angular.y :
                print("Go Backward")
            
            if msg.linear.x*msg.angular.y > 0  :
                print("Go Right")
            if msg.linear.x*msg.angular.y < 0 :
                print("Go Left")

            if msg.angular.y > 0 and not msg.linear.x :
                print("Rotating on itself to the Left")
            if msg.angular.y < 0 and not msg.linear.x :
                print("Rotating on itself to the Right")
            
            if msg.linear.z > 0 :
                print("Slide Right")
            if msg.linear.z < 0 :
                print("Slide Left")
        
        self.position['ry'] += msg.angular.y
        self.position['z'] += msg.linear.z
        self.position['x'] += msg.linear.x
       
        # TODO: Interpret the received commands and log the result using self.get_logger().info()
        # Your code here

        self.get_logger().info(f'New Position: {self.position}')

def main(args=None):
    rclpy.init(args=args)
    node = TrajectorySubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()