import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import serial

ser = serial.Serial('/dev/ttyACM0')

class TrajectorySubscriber(Node):

    def __init__(self):
        super().__init__('trajectory_subscriber')
        self.pose_subscriber = self.create_subscription(Twist, "trajectory", self.listener_callback, 10)
        # TODO: Create a subscriber of type Twist, that calls listener_callback
        # Your code here

        self.get_logger().info('Subscriber node has been started.')
        # self.position = {'x': 0.0, 'z': 0.0, 'ry': 0.0}

    def listener_callback(self, msg : Twist):
        
        self.get_logger().info(f'received {msg.linear.x=}')
        speed = (int(msg.linear.x)).to_bytes(1, 'little')
        angle = (int(msg.angular.y)).to_bytes(1, 'little')
        self.get_logger().info(f'Speed : {speed} | Angle : {angle}')
        
        ser.write(speed)
        ser.write(angle)

        print(ser.readline())
        print(ser.readline())


def main(args=None):
    rclpy.init(args=args)
    node = TrajectorySubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
