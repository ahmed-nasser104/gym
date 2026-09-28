import tkinter as tk
from tkinter import messagebox
from datetime import date
from Member import Member
from Trainer import Trainer
from Membership import Membership
from Payment import Payment
from Attendance import Attendance
class GymGUI:

    def __init__(self, gym, file_manager):

        self.gym = gym
        self.file_manager = file_manager

        self.window = tk.Tk()
        self.window.title("Gym Management System")
        self.window.geometry("900x650")

        self.window.protocol("WM_DELETE_WINDOW", self.close_app)

        self.create_dashboard()

        self.window.mainloop()

    # =========================
    # DASHBOARD
    # =========================

    def create_dashboard(self):

        title = tk.Label(
            self.window,
            text="Gym Management System",
            font=("Arial", 24)
        )
        title.pack(pady=20)

        self.dashboard_frame = tk.Frame(self.window)
        self.dashboard_frame.pack()

        self.update_dashboard()

        buttons_frame = tk.Frame(self.window)
        buttons_frame.pack(pady=30)

        tk.Button(
            buttons_frame,
            text="Members",
            width=15,
            command=self.show_members
        ).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(
            buttons_frame,
            text="Trainers",
            width=15,
            command=self.show_trainers
        ).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(
            buttons_frame,
            text="Memberships",
            width=15,
            command=self.show_memberships
        ).grid(row=0, column=2, padx=5, pady=5)

        tk.Button(
            buttons_frame,
            text="Payments",
            width=15,
            command=self.show_payments
        ).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(
            buttons_frame,
            text="Attendance",
            width=15,
            command=self.show_attendance
        ).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(
            buttons_frame,
            text="Save Data",
            width=15,
            command=self.save_data
        ).grid(row=1, column=2, padx=5, pady=5)

    def update_dashboard(self):

        for widget in self.dashboard_frame.winfo_children():
            widget.destroy()

        dashboard = self.gym.dashboard()

        data = [
            f"Total Members: {dashboard['total_members']}",
            f"Total Trainers: {dashboard['total_trainers']}",
            f"Active Memberships: {dashboard['active_memberships']}",
            f"Expired Memberships: {dashboard['expired_memberships']}",
            f"Total Payments: {dashboard['total_payments']}",
            f"Total Attendance: {dashboard['total_attendance']}"
        ]

        for item in data:

            label = tk.Label(
                self.dashboard_frame,
                text=item,
                font=("Arial", 14)
            )

            label.pack(pady=5)

    # =========================
    # SAVE / CLOSE
    # =========================

    def save_data(self):

        try:

            self.file_manager.save(
                self.gym.to_dict()
            )

            messagebox.showinfo(
                "Success",
                "Data saved successfully"
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    def close_app(self):

        try:

            self.file_manager.save(
                self.gym.to_dict()
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

        self.window.destroy()

    # =========================
    # MEMBERS
    # =========================

    def show_members(self):

        window = tk.Toplevel(self.window)
        window.title("Members")
        window.geometry("850x600")

        tk.Label(
            window,
            text="Members",
            font=("Arial", 20)
        ).pack(pady=15)

        list_frame = tk.Frame(window)
        list_frame.pack()

        def refresh():

            for widget in list_frame.winfo_children():
                widget.destroy()

            for member in self.gym.members:

                row = tk.Frame(list_frame)
                row.pack(pady=5)

                tk.Label(
                    row,
                    text=(
                        f"{member.id} | "
                        f"{member.name} | "
                        f"{member.email} | "
                        f"{member.phone}"
                    ),
                    width=55,
                    anchor="w"
                ).pack(side="left")

                tk.Button(
                    row,
                    text="Update",
                    command=lambda m=member: update_member(m)
                ).pack(side="left", padx=5)

                tk.Button(
                    row,
                    text="Delete",
                    command=lambda m=member: delete_member(m)
                ).pack(side="left")

        def add_member():

            form = tk.Toplevel(window)
            form.title("Add Member")
            form.geometry("400x350")

            entries = {}

            fields = [
                "ID",
                "Name",
                "Email",
                "Phone"
            ]

            for field in fields:

                tk.Label(
                    form,
                    text=field
                ).pack()

                entry = tk.Entry(form)
                entry.pack(pady=5)

                entries[field] = entry

            def save():

                try:

                    member = Member(
                        entries["ID"].get(),
                        entries["Phone"].get(),
                        entries["Name"].get(),
                        entries["Email"].get()
                    )

                    self.gym.add_member(member)

                    self.file_manager.save(
                        self.gym.to_dict()
                    )

                    messagebox.showinfo(
                        "Success",
                        "Member added successfully"
                    )

                    form.destroy()

                    refresh()

                    self.update_dashboard()

                except Exception as error:

                    messagebox.showerror(
                        "Error",
                        str(error)
                    )

            tk.Button(
                form,
                text="Add Member",
                command=save
            ).pack(pady=20)

        def update_member(member):

            form = tk.Toplevel(window)
            form.title("Update Member")
            form.geometry("400x300")

            tk.Label(
                form,
                text="Name"
            ).pack()

            name_entry = tk.Entry(form)
            name_entry.insert(0, member.name)
            name_entry.pack(pady=5)

            tk.Label(
                form,
                text="Email"
            ).pack()

            email_entry = tk.Entry(form)
            email_entry.insert(0, member.email)
            email_entry.pack(pady=5)

            tk.Label(
                form,
                text="Phone"
            ).pack()

            phone_entry = tk.Entry(form)
            phone_entry.insert(0, member.phone)
            phone_entry.pack(pady=5)

            def update():

                try:

                    member.name = name_entry.get()
                    member.email = email_entry.get()
                    member.phone = phone_entry.get()

                    self.file_manager.save(
                        self.gym.to_dict()
                    )

                    messagebox.showinfo(
                        "Success",
                        "Member updated successfully"
                    )

                    form.destroy()

                    refresh()

                except Exception as error:

                    messagebox.showerror(
                        "Error",
                        str(error)
                    )

            tk.Button(
                form,
                text="Update",
                command=update
            ).pack(pady=20)

        def delete_member(member):

            try:

                self.gym.delete_member(
                    member.id
                )

                self.file_manager.save(
                    self.gym.to_dict()
                )

                messagebox.showinfo(
                    "Success",
                    "Member deleted successfully"
                )

                refresh()

                self.update_dashboard()

            except Exception as error:

                messagebox.showerror(
                    "Error",
                    str(error)
                )

        tk.Button(
            window,
            text="Add Member",
            command=add_member
        ).pack(pady=10)

        refresh()

    # =========================
    # TRAINERS
    # =========================

    def show_trainers(self):

        window = tk.Toplevel(self.window)
        window.title("Trainers")
        window.geometry("850x600")

        tk.Label(
            window,
            text="Trainers",
            font=("Arial", 20)
        ).pack(pady=15)

        list_frame = tk.Frame(window)
        list_frame.pack()

        def refresh():

            for widget in list_frame.winfo_children():
                widget.destroy()

            for trainer in self.gym.trainers:

                row = tk.Frame(list_frame)
                row.pack(pady=5)

                tk.Label(
                    row,
                    text=(
                        f"{trainer.id} | "
                        f"{trainer.name} | "
                        f"{trainer.phone} | "
                        f"{trainer.specialty}"
                    ),
                    width=55,
                    anchor="w"
                ).pack(side="left")

                tk.Button(
                    row,
                    text="Update",
                    command=lambda t=trainer: update_trainer(t)
                ).pack(side="left", padx=5)

                tk.Button(
                    row,
                    text="Delete",
                    command=lambda t=trainer: delete_trainer(t)
                ).pack(side="left")

        def add_trainer():

            form = tk.Toplevel(window)
            form.title("Add Trainer")
            form.geometry("400x400")

            tk.Label(
                form,
                text="ID"
            ).pack()

            id_entry = tk.Entry(form)
            id_entry.pack(pady=5)

            tk.Label(
                form,
                text="Name"
            ).pack()

            name_entry = tk.Entry(form)
            name_entry.pack(pady=5)

            tk.Label(
                form,
                text="Phone"
            ).pack()

            phone_entry = tk.Entry(form)
            phone_entry.pack(pady=5)

            tk.Label(
                form,
                text="Specialty"
            ).pack()

            specialty_entry = tk.Entry(form)
            specialty_entry.pack(pady=5)

            def save():

                try:

                    trainer = Trainer(
                        id_entry.get(),
                        phone_entry.get(),
                        name_entry.get(),
                        specialty_entry.get()
                    )

                    self.gym.add_trainer(
                        trainer
                    )

                    self.file_manager.save(
                        self.gym.to_dict()
                    )

                    messagebox.showinfo(
                        "Success",
                        "Trainer added successfully"
                    )

                    form.destroy()

                    refresh()

                    self.update_dashboard()

                except Exception as error:

                    messagebox.showerror(
                        "Error",
                        str(error)
                    )

            tk.Button(
                form,
                text="Add Trainer",
                command=save
            ).pack(pady=20)

        def update_trainer(trainer):

            form = tk.Toplevel(window)
            form.title("Update Trainer")
            form.geometry("400x400")

            tk.Label(
                form,
                text="Name"
            ).pack()

            name_entry = tk.Entry(form)
            name_entry.insert(0, trainer.name)
            name_entry.pack(pady=5)

            tk.Label(
                form,
                text="Phone"
            ).pack()

            phone_entry = tk.Entry(form)
            phone_entry.insert(0, trainer.phone)
            phone_entry.pack(pady=5)

            tk.Label(
                form,
                text="Specialty"
            ).pack()

            specialty_entry = tk.Entry(form)
            specialty_entry.insert(0, trainer.specialty)
            specialty_entry.pack(pady=5)

            def update():

                try:

                    specialty = specialty_entry.get().lower()

                    if specialty not in [
                        "fitness",
                        "cardio",
                        "bodybuilding"
                    ]:
                        raise ValueError(
                            "Specialty must be fitness, cardio or bodybuilding"
                        )

                    trainer.name = name_entry.get()
                    trainer.phone = phone_entry.get()
                    trainer.specialty = specialty

                    self.file_manager.save(
                        self.gym.to_dict()
                    )

                    messagebox.showinfo(
                        "Success",
                        "Trainer updated successfully"
                    )

                    form.destroy()

                    refresh()

                except Exception as error:

                    messagebox.showerror(
                        "Error",
                        str(error)
                    )

            tk.Button(
                form,
                text="Update",
                command=update
            ).pack(pady=20)

        def delete_trainer(trainer):

            try:

                self.gym.delete_trainer(
                    trainer.id
                )

                self.file_manager.save(
                    self.gym.to_dict()
                )

                messagebox.showinfo(
                    "Success",
                    "Trainer deleted successfully"
                )

                refresh()

                self.update_dashboard()

            except Exception as error:

                messagebox.showerror(
                    "Error",
                    str(error)
                )

        tk.Button(
            window,
            text="Add Trainer",
            command=add_trainer
        ).pack(pady=10)

        refresh()

    # =========================
    # MEMBERSHIPS
    # =========================

    def show_memberships(self):

        window = tk.Toplevel(self.window)
        window.title("Memberships")
        window.geometry("1000x650")

        tk.Label(
            window,
            text="Memberships",
            font=("Arial", 20)
        ).pack(pady=15)

        list_frame = tk.Frame(window)
        list_frame.pack()

        def refresh(filter_type="all"):

            for widget in list_frame.winfo_children():
                widget.destroy()

            memberships = self.gym.filter_memberships(
                filter_type
            )

            for membership in memberships:

                status = membership.membership_status()

                row = tk.Frame(list_frame)
                row.pack(pady=5)

                tk.Label(
                    row,
                    text=(
                        f"{membership.id} | "
                        f"{membership.member.name} | "
                        f"{membership.type} | "
                        f"{membership.start_date} | "
                        f"{membership.end_date} | "
                        f"{status}"
                    ),
                    width=85,
                    anchor="w"
                ).pack(side="left")

                tk.Button(
                    row,
                    text="Update",
                    command=lambda m=membership: update_membership(m)
                ).pack(side="left", padx=5)

                tk.Button(
                    row,
                    text="Delete",
                    command=lambda m=membership: delete_membership(m)
                ).pack(side="left")

        filter_frame = tk.Frame(window)
        filter_frame.pack(pady=10)

        tk.Button(
            filter_frame,
            text="All",
            command=lambda: refresh("all")
        ).pack(side="left", padx=5)

        tk.Button(
            filter_frame,
            text="Active",
            command=lambda: refresh("active")
        ).pack(side="left", padx=5)

        tk.Button(
            filter_frame,
            text="Expired",
            command=lambda: refresh("expired")
        ).pack(side="left", padx=5)

        def add_membership():

            form = tk.Toplevel(window)
            form.title("Add Membership")
            form.geometry("450x500")

            tk.Label(
                form,
                text="Membership ID"
            ).pack()

            id_entry = tk.Entry(form)
            id_entry.pack(pady=5)

            tk.Label(
                form,
                text="Member ID"
            ).pack()

            member_entry = tk.Entry(form)
            member_entry.pack(pady=5)

            tk.Label(
                form,
                text="Start Date (DD/MM/YYYY)"
            ).pack()

            start_entry = tk.Entry(form)
            start_entry.pack(pady=5)

            tk.Label(
                form,
                text="End Date (DD/MM/YYYY)"
            ).pack()

            end_entry = tk.Entry(form)
            end_entry.pack(pady=5)

            tk.Label(
                form,
                text="Type"
            ).pack()

            type_entry = tk.Entry(form)
            type_entry.pack(pady=5)

            def save():

                try:

                    member = self.gym.search_member(
                        member_entry.get()
                    )

                    start = start_entry.get().split("/")
                    end = end_entry.get().split("/")

                    membership = Membership(
                        id_entry.get(),
                        (
                            int(start[2]),
                            int(start[1]),
                            int(start[0])
                        ),
                        (
                            int(end[2]),
                            int(end[1]),
                            int(end[0])
                        ),
                        type_entry.get(),
                        member
                    )

                    self.gym.add_membership(
                        membership
                    )

                    self.file_manager.save(
                        self.gym.to_dict()
                    )

                    messagebox.showinfo(
                        "Success",
                        "Membership added successfully"
                    )

                    form.destroy()

                    refresh()

                    self.update_dashboard()

                except Exception as error:

                    messagebox.showerror(
                        "Error",
                        str(error)
                    )

            tk.Button(
                form,
                text="Add Membership",
                command=save
            ).pack(pady=20)

        def update_membership(membership):

            form = tk.Toplevel(window)
            form.title("Update Membership")
            form.geometry("450x450")

            tk.Label(
                form,
                text="Start Date (DD/MM/YYYY)"
            ).pack()

            start_entry = tk.Entry(form)
            start_entry.insert(
                0,
                membership.start_date.strftime("%d/%m/%Y")
            )
            start_entry.pack(pady=5)

            tk.Label(
                form,
                text="End Date (DD/MM/YYYY)"
            ).pack()

            end_entry = tk.Entry(form)
            end_entry.insert(
                0,
                membership.end_date.strftime("%d/%m/%Y")
            )
            end_entry.pack(pady=5)

            tk.Label(
                form,
                text="Type"
            ).pack()

            type_entry = tk.Entry(form)
            type_entry.insert(
                0,
                membership.type
            )
            type_entry.pack(pady=5)

            def update():

                try:

                    start = start_entry.get().split("/")
                    end = end_entry.get().split("/")

                    new_start = date(
                        int(start[2]),
                        int(start[1]),
                        int(start[0])
                    )

                    new_end = date(
                        int(end[2]),
                        int(end[1]),
                        int(end[0])
                    )

                    if new_start > new_end:
                        raise ValueError(
                            "Start date can't be after end date"
                        )

                    membership_type = type_entry.get().lower()

                    if membership_type not in [
                        "monthly",
                        "quarterly",
                        "yearly"
                    ]:
                        raise ValueError(
                            "Type must be monthly, quarterly or yearly"
                        )

                    membership.start_date = new_start
                    membership.end_date = new_end
                    membership.type = membership_type

                    self.file_manager.save(
                        self.gym.to_dict()
                    )

                    messagebox.showinfo(
                        "Success",
                        "Membership updated successfully"
                    )

                    form.destroy()

                    refresh()

                    self.update_dashboard()

                except Exception as error:

                    messagebox.showerror(
                        "Error",
                        str(error)
                    )

            tk.Button(
                form,
                text="Update",
                command=update
            ).pack(pady=20)

        def delete_membership(membership):

            try:

                self.gym.delete_membership(
                    membership.id
                )

                self.file_manager.save(
                    self.gym.to_dict()
                )

                messagebox.showinfo(
                    "Success",
                    "Membership deleted successfully"
                )

                refresh()

                self.update_dashboard()

            except Exception as error:

                messagebox.showerror(
                    "Error",
                    str(error)
                )

        tk.Button(
            window,
            text="Add Membership",
            command=add_membership
        ).pack(pady=10)

        refresh()

    # =========================
    # PAYMENTS
    # =========================

    def show_payments(self):

        window = tk.Toplevel(self.window)
        window.title("Payments")
        window.geometry("900x600")

        tk.Label(
            window,
            text="Payments",
            font=("Arial", 20)
        ).pack(pady=15)

        list_frame = tk.Frame(window)
        list_frame.pack()

        def refresh():

            for widget in list_frame.winfo_children():
                widget.destroy()

            # IMPORTANT:
            # Gym has a property called payments
            for payment in self.gym.payments:

                row = tk.Frame(list_frame)
                row.pack(pady=5)

                tk.Label(
                    row,
                    text=(
                        f"{payment.id} | "
                        f"{payment.member.name} | "
                        f"{payment.amount} | "
                        f"{payment.date}"
                    ),
                    width=60,
                    anchor="w"
                ).pack(side="left")

                tk.Button(
                    row,
                    text="Update",
                    command=lambda p=payment: update_payment(p)
                ).pack(side="left", padx=5)

                tk.Button(
                    row,
                    text="Delete",
                    command=lambda p=payment: delete_payment(p)
                ).pack(side="left")

        def add_payment():

            form = tk.Toplevel(window)
            form.title("Add Payment")
            form.geometry("450x450")

            tk.Label(
                form,
                text="Payment ID"
            ).pack()

            id_entry = tk.Entry(form)
            id_entry.pack(pady=5)

            tk.Label(
                form,
                text="Member ID"
            ).pack()

            member_entry = tk.Entry(form)
            member_entry.pack(pady=5)

            tk.Label(
                form,
                text="Amount"
            ).pack()

            amount_entry = tk.Entry(form)
            amount_entry.pack(pady=5)

            tk.Label(
                form,
                text="Date (DD/MM/YYYY)"
            ).pack()

            date_entry = tk.Entry(form)
            date_entry.pack(pady=5)

            def save():

                try:

                    member = self.gym.search_member(
                        member_entry.get()
                    )

                    payment_date = date_entry.get().split("/")

                    payment = Payment(
                        id_entry.get(),
                        member,
                        int(amount_entry.get()),
                        (
                            int(payment_date[2]),
                            int(payment_date[1]),
                            int(payment_date[0])
                        )
                    )

                    self.gym.add_payment(
                        payment
                    )

                    self.file_manager.save(
                        self.gym.to_dict()
                    )

                    messagebox.showinfo(
                        "Success",
                        "Payment added successfully"
                    )

                    form.destroy()

                    refresh()

                    self.update_dashboard()

                except Exception as error:

                    messagebox.showerror(
                        "Error",
                        str(error)
                    )

            tk.Button(
                form,
                text="Add Payment",
                command=save
            ).pack(pady=20)

        def update_payment(payment):

            form = tk.Toplevel(window)
            form.title("Update Payment")
            form.geometry("400x350")

            tk.Label(
                form,
                text="Amount"
            ).pack()

            amount_entry = tk.Entry(form)
            amount_entry.insert(
                0,
                payment.amount
            )
            amount_entry.pack(pady=5)

            tk.Label(
                form,
                text="Date (DD/MM/YYYY)"
            ).pack()

            date_entry = tk.Entry(form)
            date_entry.insert(
                0,
                payment.date.strftime("%d/%m/%Y")
            )
            date_entry.pack(pady=5)

            def update():

                try:

                    amount = int(
                        amount_entry.get()
                    )

                    if amount <= 0:
                        raise ValueError(
                            "Amount must be greater than 0"
                        )

                    payment_date = date_entry.get().split("/")

                    new_date = date(
                        int(payment_date[2]),
                        int(payment_date[1]),
                        int(payment_date[0])
                    )

                    payment.amount = amount
                    payment.date = new_date

                    self.file_manager.save(
                        self.gym.to_dict()
                    )

                    messagebox.showinfo(
                        "Success",
                        "Payment updated successfully"
                    )

                    form.destroy()

                    refresh()

                except Exception as error:

                    messagebox.showerror(
                        "Error",
                        str(error)
                    )

            tk.Button(
                form,
                text="Update",
                command=update
            ).pack(pady=20)

        def delete_payment(payment):

            try:

                self.gym.delete_payment(
                    payment.id
                )

                self.file_manager.save(
                    self.gym.to_dict()
                )

                messagebox.showinfo(
                    "Success",
                    "Payment deleted successfully"
                )

                refresh()

                self.update_dashboard()

            except Exception as error:

                messagebox.showerror(
                    "Error",
                    str(error)
                )

        tk.Button(
            window,
            text="Add Payment",
            command=add_payment
        ).pack(pady=10)

        refresh()

    # =========================
    # ATTENDANCE
    # =========================

    def show_attendance(self):

        window = tk.Toplevel(self.window)
        window.title("Attendance")
        window.geometry("850x600")

        tk.Label(
            window,
            text="Attendance",
            font=("Arial", 20)
        ).pack(pady=15)

        list_frame = tk.Frame(window)
        list_frame.pack()

        def refresh():

            for widget in list_frame.winfo_children():
                widget.destroy()

            for attendance in self.gym.attendances:

                row = tk.Frame(list_frame)
                row.pack(pady=5)

                tk.Label(
                    row,
                    text=(
                        f"{attendance.id} | "
                        f"{attendance.member.name} | "
                        f"{attendance.date}"
                    ),
                    width=55,
                    anchor="w"
                ).pack(side="left")

                tk.Button(
                    row,
                    text="Update",
                    command=lambda a=attendance: update_attendance(a)
                ).pack(side="left", padx=5)

                tk.Button(
                    row,
                    text="Delete",
                    command=lambda a=attendance: delete_attendance(a)
                ).pack(side="left")

        def add_attendance():

            form = tk.Toplevel(window)
            form.title("Add Attendance")
            form.geometry("450x400")

            tk.Label(
                form,
                text="Attendance ID"
            ).pack()

            id_entry = tk.Entry(form)
            id_entry.pack(pady=5)

            tk.Label(
                form,
                text="Member ID"
            ).pack()

            member_entry = tk.Entry(form)
            member_entry.pack(pady=5)

            tk.Label(
                form,
                text="Membership ID"
            ).pack()

            membership_entry = tk.Entry(form)
            membership_entry.pack(pady=5)

            tk.Label(
                form,
                text="Date (DD/MM/YYYY)"
            ).pack()

            date_entry = tk.Entry(form)
            date_entry.pack(pady=5)

            def save():

                try:

                    member = self.gym.search_member(
                        member_entry.get()
                    )

                    membership = self.gym.search_membership(
                        membership_entry.get()
                    )

                    attendance_date = date_entry.get().split("/")

                    attendance = Attendance(
                        id_entry.get(),
                        member,
                        (
                            int(attendance_date[2]),
                            int(attendance_date[1]),
                            int(attendance_date[0])
                        )
                    )

                    # Use the exact method name
                    # from your Gym class
                    self.gym.member_attendace(
                        attendance,
                        membership
                    )

                    self.file_manager.save(
                        self.gym.to_dict()
                    )

                    messagebox.showinfo(
                        "Success",
                        "Attendance added successfully"
                    )

                    form.destroy()

                    refresh()

                    self.update_dashboard()

                except Exception as error:

                    messagebox.showerror(
                        "Error",
                        str(error)
                    )

            tk.Button(
                form,
                text="Add Attendance",
                command=save
            ).pack(pady=20)

        def update_attendance(attendance):

            form = tk.Toplevel(window)
            form.title("Update Attendance")
            form.geometry("400x300")

            tk.Label(
                form,
                text="Date (DD/MM/YYYY)"
            ).pack()

            date_entry = tk.Entry(form)

            date_entry.insert(
                0,
                attendance.date.strftime("%d/%m/%Y")
            )

            date_entry.pack(pady=10)

            def update():

                try:

                    attendance_date = date_entry.get().split("/")

                    new_date = date(
                        int(attendance_date[2]),
                        int(attendance_date[1]),
                        int(attendance_date[0])
                    )

                    attendance.date = new_date

                    self.file_manager.save(
                        self.gym.to_dict()
                    )

                    messagebox.showinfo(
                        "Success",
                        "Attendance updated successfully"
                    )

                    form.destroy()

                    refresh()

                except Exception as error:

                    messagebox.showerror(
                        "Error",
                        str(error)
                    )

            tk.Button(
                form,
                text="Update",
                command=update
            ).pack(pady=20)

        def delete_attendance(attendance):

            try:

                self.gym.delete_attendance(
                    attendance.id
                )

                self.file_manager.save(
                    self.gym.to_dict()
                )

                messagebox.showinfo(
                    "Success",
                    "Attendance deleted successfully"
                )

                refresh()

                self.update_dashboard()

            except Exception as error:

                messagebox.showerror(
                    "Error",
                    str(error)
                )

        tk.Button(
            window,
            text="Add Attendance",
            command=add_attendance
        ).pack(pady=10)

        refresh()

