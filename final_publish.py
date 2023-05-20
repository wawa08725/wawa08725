import rospy
from std_msgs.msg import String

rospy.init_node('publisher_node', anonymous=True)
pub = rospy.Publisher('std_id', int, queue_size=10)

message = "6352500048"
rate = rospy.Rate(10) 
while not rospy.is_shutdown():
    pub.publish(message)
    rate.sleep()
