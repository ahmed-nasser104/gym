from Member import Member
from Trainer import Trainer
from Membership import Membership
from Payment import Payment
from Attendance import Attendance
from GYM import Gym
from FileManager import FileManager
from gui import GymGUI
gym = Gym()
file_manager = FileManager("gym_data.json")
gym.load_data(file_manager)
app = GymGUI( gym, file_manager )