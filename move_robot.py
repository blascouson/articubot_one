import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class MoveRobotNode(Node):
    def __init__(self):
        super().__init__('move_robot')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.start_time = time.time()
        
    def timer_callback(self):
        elapsed_time = time.time() - self.start_time
        
        # Create a Twist message and fill in the velocity values
        msg = Twist()
        
        if elapsed_time < 3.0:  # Move forward for 3 seconds
            msg.linear.x = 0.5  # Forward velocity
            msg.angular.z = 0.0 # No angular velocity
        else:
            msg.linear.x = 0.0  # Stop moving
            msg.angular.z = 0.0
        
        # Publish the message
        self.publisher.publish(msg)
        
        # Shutdown the node after the movement
        if elapsed_time >= 3.0:
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    move_robot_node = MoveRobotNode()
    rclpy.spin(move_robot_node)

if __name__ == '__main__':
    main()
