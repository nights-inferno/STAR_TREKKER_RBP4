# colcom build marche pas

import rclpy
import re
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TrajectoryPublisher(Node):

    def __init__(self):
        super().__init__('trajectory_publisher')
        # TODO: Create a publisher of type Twist
        # Your code here
        self.cmd_vel_pub_ = self.create_publisher(Twist,"trajectory", 10)
        self.timer = self.create_timer(0.5, self.cmd_acquisition)
        self.get_logger().info('Publisher node has been started.')

        # TODO: Create a loop here to ask users a prompt and send messages accordingly

     # Function that prompts user for a direction input, and sends the command
    def cmd_acquisition(self):
        msg = Twist()
        command = input("Enter command (w/a/s/d/q/e - max 2 characters): ")
        
        re.sub('[^wasdqe]','',command)
        if len(command) > 2 :
            command[:1]
        
        if 'w' in command :
            msg.linear.x += 1
        if 's' in command :
            msg.linear.x += -1
        if 'a' in command :
            msg.linear.z += -1 
        if 'd' in command :
            msg.linear.z += 1 
        if 'q' in command :
            msg.angular.y += 1
        if 'e' in command :
            msg.angular.y += -1    
        
        self.cmd_vel_pub_.publish(msg)
        #pass

def main(args=None):
    rclpy.init(args=args)   # Init ROS python
    node = TrajectoryPublisher()  # Create a Node instance
    rclpy.spin(node)  # Run the node in a Thread
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()