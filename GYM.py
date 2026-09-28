from Member import Member
from Trainer import Trainer
from Membership import Membership
from Payment import Payment
from Attendance import Attendance
from datetime import date
class action_status(Exception):
    pass
class not_found(Exception):
    pass
class Gym:
    def __init__(self):
        self.members = []
        self.trainers = []
        self.memberships  = []
        self.__payments = []
        self.attendances = []

    def add_member(self , member:Member):
        self.members.append(member)

    def add_trainer(self , trainer:Trainer):
        self.trainers.append(trainer)

    def add_membership(self, membership: Membership):
        self.validate_membership(membership)

    @property
    def payments(self):
        return self.__payments
    
    def add_payment(self , payment:Payment):
        self.__payments.append(payment)

    def add_attendance(self , attendance:Attendance):
        self.attendances.append(attendance)

    def validate_membership(self , membership: Membership):
        for i in self.memberships:
            if i.member.id == membership.member.id:
                is_valid = i.membership_status()
                if is_valid == "active membership":
                    raise action_status("You already active")
                    
        self.memberships.append(membership)
            

    def member_attendace(self, attendance: Attendance, membership: Membership):
        found = False
        for i in self.members:
            if i.id == attendance.member.id:
                found = True
                break
        if not found:
            raise not_found("member not found")
        if membership.member.id != attendance.member.id:
            raise not_found("member not found")
        is_valid = membership.membership_status()
        if is_valid != "active membership":
            raise action_status("Your are not active")
        self.add_attendance(attendance)

    def update_member(self , member_id):
        found = False
        for i in self.members:
            if i.id == member_id:
                found = True
                user = i
                while True:
                    user_input = input("What do you want to update: (phone , name , email)?")
                    if user_input == "phone":
                        user.phone = input("Update the phone number: ")
                        break
                    elif user_input == "name":
                        user.name = input("Update the name: ")
                        break
                    elif user_input == "email":
                        user.email = input("Update the email: ")
                        break
                    else:
                        print("invalid input! , choose from (phone , name , email)")
                break
        if not found:
            raise not_found("User not found")

    def delete_member(self , member_id):
        found = False
        for i in self.members:
            if i.id == member_id:
                found = True
                self.members.remove(i)
                break
        if not found:
            raise not_found("User not found")
        print("member deleted successfully")

    def search_member(self , member_id):
        found = False
        for i in self.members:
            if i.id == member_id:
                found = True
                user = i
                break
        if not found:
            raise not_found("User not found")
        return user

    
    def filter_memberships(self , filter_search):
        self.active_filter_list = []
        self.expired_filter_list = []
        for i in self.memberships:
            if i.membership_status() == "active membership":
                self.active_filter_list.append(i)
            else:
                self.expired_filter_list.append(i)
        if filter_search == "all":
            return self.memberships
        elif filter_search == "active":
            return self.active_filter_list
        elif filter_search == "expired":
            return self.expired_filter_list
        else:
            raise not_found("this filter search not found in our system")

    def search_trainer(self , trainer_id):
        found = False
        for i in self.trainers:
            if i.id == trainer_id:
                found = True
                user = i
                break
        if not found:
            raise not_found("trainer not found")
        return user

    def update_trainer(self , trianer_id):
        found = False
        for i in self.trainers:
            if i.id == trianer_id:
                found = True
                user = i
                while True:
                    user_input = input("What do you want to update: (phone , name , specialty)?")
                    if user_input == "phone":
                        user.phone = input("Update the phone number: ")
                        break
                    elif user_input == "name":
                        user.name = input("Update the name: ")
                        break
                    elif user_input == "specialty":
                        fits = ["fitness", "cardio", "bodybuilding"]
                        user_fit = input("choose from this option: ( fitness, cardio, bodybuilding )")
                        if user_fit.lower() in fits:
                            user.specialty = user_fit.lower()
                            break
                        else:
                            raise not_found("your specialty not found in our programe , our programe includes ( fitness , cardio , bodybuilding ) only! ")
                    else:
                        print("invalid input! , choose from (phone , name , specialty)")
                break
        if not found:
            raise not_found("trainer not found")

    def delete_trainer(self,trainer_id):
        found = False
        for i in self.trainers:
            if i.id == trainer_id:
                found = True
                self.trainers.remove(i)
                break
        if not found:
            raise not_found("trainer not found")
        print("trainer deleted successfully")

    def search_membership(self , membership_id):
        found = False
        for i in self.memberships:
            if i.id == membership_id:
                found = True
                user = i
                break
        if not found:
            raise not_found("membership  not found")
        return user

    def delete_membership(self ,membership_id):
        found = False
        for i in self.memberships:
            if i.id == membership_id:
                found = True
                self.memberships.remove(i)
                break
        if not found:
            raise not_found("membership  not found")
        print("membership deleted successfully")

    def update_membership(self, membership_id):
        found = False
        for i in self.memberships:
            if i.id == membership_id:
                found = True
                user = i
                while True:
                    user_input = input("What do you want to update: (start_date ,end_date , type)?")
                    if user_input == "start_date":
                        user_date = input("Update the start_date , 0?/0?/2026: ")
                        user_date = user_date.split("/")
                        new_start_date = date(int(user_date[2]), int(user_date[1]), int(user_date[0]))
                        if new_start_date <= user.end_date:
                             user.start_date = new_start_date 
                             break
                        else:
                            raise action_status("date invalide")
                    elif user_input == "end_date":
                        user_date = input("Update the end_date , 0?/0?/2026: ")
                        user_date = user_date.split("/")
                        new_end_date = date(int(user_date[2]), int(user_date[1]), int(user_date[0]))
                        if user.start_date <= new_end_date:
                             user.end_date = new_end_date 
                             break
                        else: 
                            raise action_status("date invalide")
                    elif user_input == "type":
                        types = ["monthly", "quarterly" , "yearly"]
                        user_type = input("Update the type: ")
                        if user_type.lower() in types: 
                            user.type = user_type.lower()
                            break
                        else:
                            raise not_found("your type not found in our programe , our types includes ( monthly , quarterly , yearly ) only! ") 
                        
                    else:
                        print("invalid input! , choose from (start_date ,end_date , type)")
                break
        if not found:
            raise not_found("membership not found")
        print("user updated successfully")


    def search_payment(self , payment_id):
        found = False
        for i in self.__payments:
            if i.id == payment_id:
                found = True
                user_payment = i
                break
        if not found:
            raise not_found("payment not found")
        return user_payment

    def update_payment(self , payment_id):
        found = False
        for i in self.__payments:
            if i.id == payment_id:
                found = True
                user_payment = i
                while True:
                    user_input = input("What do you want to update: (amount or payment_date)?")
                    if user_input == "amount":
                        user_amount =  int(input("Update the payment amount: "))
                        if user_amount > 0:
                            user_payment.amount = user_amount
                        else:
                            raise action_status("you can't add an amount less than or equal 0")
                        break
                    elif user_input == "payment_date":
                        user_date = input("Update the end_date , 0?/0?/2026: ")
                        user_date = user_date.split("/")
                        new_payment_date = date(int(user_date[2]), int(user_date[1]), int(user_date[0]))
                        user_payment.date = new_payment_date
                        break
                    else:
                        print("invalid input! , choose from (phone , name , specialty)")
        if not found:
            raise not_found("payment not found")
        print("payment updated successfully")

    def delete_payment(self , payment_id):
        found = False
        for i in self.__payments:
            if i.id == payment_id:
                found = True
                self.__payments.remove(i)
                break
        if not found:
            raise not_found("payment not found")
        print("payment deleted successfully")

    def search_attendance(self , attendance_id):
        found = False
        for i in self.attendances:
            if i.id == attendance_id:
                found = True
                attendance = i
                break
        if not found:
            raise not_found("attendance not found")
        return attendance

    def delete_attendance(self , attendance_id ):
        found = False
        for i in self.attendances:
            if i.id == attendance_id:
                found = True
                self.attendances.remove(i)
                break
        if not found:
            raise not_found("attendance not found")
        print("attendance deleted successfully")

    def update_attendance(self, attendance_id):
        found = False
        for i in self.attendances:
            if i.id == attendance_id:
                found = True
                attendance = i
                user_date = input("Update the attendance date, 0?/0?/2026: ")
                user_date = user_date.split("/")
                new_attendance_date = date(
                    int(user_date[2]),
                    int(user_date[1]),
                    int(user_date[0])
                )
                attendance.date = new_attendance_date
                break
        if not found:
            raise not_found("attendance not found")
        print("attendance updated successfully")

    def to_dict(self):
        return {
            "members": [member.to_dict() for member in self.members],
            "trainers": [trainer.to_dict() for trainer in self.trainers],
            "memberships": [membership.to_dict() for membership in self.memberships],
            "payments": [payment.to_dict() for payment in self.__payments],
            "attendances": [attendance.to_dict() for attendance in self.attendances]
        }


    def load_data(self, file_manager):
        data = file_manager.load()
        for member_data in data["members"]:
            member = Member.from_dict(member_data)
            self.members.append(member)
        for trainer_data in data["trainers"]:
            trainer = Trainer.from_dict(trainer_data)
            self.trainers.append(trainer)
        for membership_data in data["memberships"]:
            membership = Membership.from_dict(membership_data)
            self.memberships.append(membership)
        for payment_data in data["payments"]:
            payment = Payment.from_dict(payment_data)
            self.__payments.append(payment)
        for attendance_data in data["attendances"]:
            attendance = Attendance.from_dict(attendance_data)
            self.attendances.append(attendance)



    def total_members(self):
        return len(self.members)

    def total_trainers(self):
        return len(self.trainers)

    def total_active_memberships(self):
        count = 0
        for membership in self.memberships:
            if membership.membership_status() == "active membership":
                count += 1
        return count

    def total_expired_memberships(self):
        count = 0
        for membership in self.memberships:
            if membership.membership_status() == "date expired":
                count += 1
        return count


    def total_payments(self):
        return len(self.__payments)

    def total_attendance(self):
        return len(self.attendances)

    def dashboard(self):
        return {
            "total_members": self.total_members(),
            "total_trainers": self.total_trainers(),
            "active_memberships": self.total_active_memberships(),
            "expired_memberships": self.total_expired_memberships(),
            "total_payments": self.total_payments(),
            "total_attendance": self.total_attendance()
        }
                