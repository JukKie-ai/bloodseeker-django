from email import message
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.views.generic.base import View
from .models import *
from .forms import *

# Create your views here.



class editAccountView(View):
    template_name = "user/editAccount.html"

    def get(self, request, user):
        
        if User.objects.filter(pk=user).count() != 0:
            account = User.objects.get(pk=user)
        
        return render(request, self.template_name, {'user': user, 'account': account})
        
    def post(self, request, user):

        if User.objects.filter(pk=user).count() != 0:
            account = User.objects.get(pk=user)

        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        username = request.POST.get('username')
        email = request.POST.get('email')
        contactNumber = request.POST.get('contactNumber')
        age = request.POST.get('age')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if password == confirmPassword:
            updateAccount = User(username=username, password=password, firstName=firstName, lastName=lastName, email=email,
        contactNumber=contactNumber, gender=account.gender, age=age)
            updateAccount.save()
            messages.error(request, 'Account Update Successful!')
        else:
            messages.error(request, 'Password does not match!')
        
        if User.objects.filter(pk=user).count() != 0:
            account = User.objects.get(pk=user)
        
        return render(request, self.template_name, {'user': user, 'account': account})


class loginView(View):

    template_name = "user/login.html"

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name)

    def post(self, request):
        form = LoginForm(request.POST)
        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        if User.objects.filter(pk=uname).count() != 0:
            account = User.objects.get(pk=uname)

            if account.password == pwd:
                return redirect(reverse('user:dashboard', kwargs={'user': uname}))
            else:
                messages.error(request, 'Incorrect Password')
        else:
            messages.error(request, 'Username Does Not Exist')

        return render(request, self.template_name)


class registerView(View):
    template_name = "user/register.html"

    def get(self, request):
        formUser = UserForm()
        return render(request, self.template_name)

    def post(self, request):
        formUser = UserForm(request.POST)
        uname = request.POST.get('username')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if len(uname) < 4 and len(password) < 8:
            messages.error(request, "Username and Password are too short.")
        elif User.objects.filter(pk=uname).count() != 0 and len(password) < 8:
            messages.error(
                request, "Username already exist and Password is too short.")
        elif len(uname) < 4:
            messages.error(request, "Username is too short.")
        elif User.objects.filter(pk=uname).count() != 0:
            messages.error(request, "Username already exist!")
        elif len(password) < 8:
            messages.error(request, "Password is too short.")
        elif confirmPassword != password:
            messages.error(request, "Password doesn't match.")
        else:
            customer = formUser.save(commit=False)
            customer.save()
            return redirect(reverse('user:login'))

        return render(request, self.template_name)


class userListView(View):
    template_name = "user/userList.html"

    def get(self, request):
        user = User.objects.all()
        return render(request, self.template_name, {'user': user})


class dashboardView(View):
    template_name = "user/dashboard.html"

    def get(self, request, user):
        formRequestDonor = RequestDonorForm()
        return render(request, self.template_name, {'user': user})

    def post(self, request, user):
        donor = RequestDonorForm(request.POST)

        address = request.POST.get('address')
        donorBloodType = request.POST.get('donorBloodType')
        isApproved = False
        username = User.objects.get(pk=user)

        donorReq = Donor(address=address, donorBloodType=donorBloodType,
                                isApproved=isApproved, username=username)

        donorReq.save()

        return render(request, self.template_name, {'user': user})


class aboutView(View):
    template_name = "user/about.html"

    def get(self, request, user):
        return render(request, self.template_name, {'user': user})


class donorView(View):
    template_name = "user/donorList.html"

    def get(self, request, user):
        donor = Donor.objects.all()

        if User.objects.filter(pk=user).count() != 0:
            account = User.objects.get(pk=user)
        else:
            account = 0

        if Donor.objects.filter(username_id=user).count() != 0:
            donor1 = Donor.objects.get(username_id=user)
        else:
            donor1 = 0

        return render(request, self.template_name, {'donor': donor, 'user': user, 'account': account, 'donor1': donor1})


class accreditedHospitalView(View):
    template_name = "user/hospital.html"

    def get(self, request, user):
        hospital = Organizer.objects.all()

        if User.objects.filter(pk=user).count() != 0:
            account = User.objects.get(pk=user)
        else:
            account = 0

        if Organizer.objects.filter(username_id=user).count() != 0:
            hospital1 = Organizer.objects.get(username_id=user)
        else:
            hospital1 = 0

        return render(request, self.template_name, {'hospital': hospital, 'user': user, 'account':account, 'hospital1':hospital1})


class accountView(View):
    template_name = "user/account.html"

    def get(self, request, user):
        if User.objects.filter(pk=user).count() != 0:
            account = User.objects.get(pk=user)
        else:
            account = 0

        if Donor.objects.filter(username_id=user).count() != 0:
            donor = Donor.objects.get(username_id=user)
        else:
            donor = 0
            
        return render(request, self.template_name, {'user': user, 'account': account, 'donor': donor})

    def post(self, request, user, account):
        
            
            return render(request, self.template_name, {'user': user, 'account': account})


class requestDonorView(View):
    template_name = "user/requestDonor.html"

    def get(self, request, user):
        formRequestDonor = RequestDonorForm()
        return render(request, self.template_name, {'user': user})

    def post(self, request, user):
        donor = RequestDonorForm(request.POST)

        address = request.POST.get('address')
        donorBloodType = request.POST.get('donorBloodType')
        attachmentsDonor = request.POST.get('attachmentsDonor')
        isApproved = False
        username = User.objects.get(pk=user)

        donorReq = Donor(address=address, donorBloodType=donorBloodType, attachmentsDonor=attachmentsDonor,
                                isApproved=isApproved, username=username)

        donorReq.save()

        return render(request, self.template_name, {'user': user})


class requestOrganizerView(View):
    template_name = "user/requestOrganizer.html"

    def get(self, request, user):
        formRequestOrganizer = OrganizerForm()
        return render(request, self.template_name, {'user': user})

    def post(self, request, user):
        organizer = OrganizerForm(request.POST)

        hospitalName = request.POST.get('hospitalName')
        hospitalAddress = request.POST.get('hospitalAddress')
        businessEmail = request.POST.get('businessEmail')
        contactInfo = request.POST.get('contactInfo')
        attachmentsID = request.POST.get('attachmentsID')
        isApproved = False
        username = User.objects.get(pk=user)

        organizerReq = Organizer(hospitalName=hospitalName, hospitalAddress=hospitalAddress, businessEmail=businessEmail,
                                        contactInfo=contactInfo, attachmentsID=attachmentsID, 
                                        isApproved=isApproved, username=username)

        organizerReq.save()

        return render(request, self.template_name, {'user': user})

class requestAppointmentView(View):
    template_name = "user/requestAppointment.html"

    def get(self, request, user):
        formRequestDonor = AppointmentForm()
        return render(request, self.template_name, {'user': user})

    def post(self, request, user):
        appointment = AppointmentForm(request.POST)

        appointmentType = request.POST.get('appointmentType')
        setDate = request.POST.get('setDate')
        setTime = request.POST.get('setTime')
        isApproved = False
        #requestDonorID = Donor.objects.get(pk=user)

        appointmentReq = Appointment(appointmentType=appointmentType, setDate=setDate, setTime=setTime,
                                isApproved=isApproved, )

        appointmentReq.save()

        return render(request, self.template_name, {'user': user})

class AppointmentView(View):
    template_name = "user/appointmentList.html"

    def get(self, request, user):
        formDonor = AppointmentForm()
        requestAppointmentID = Appointment.objects.all()

        return render(request, self.template_name, {'user': user, 'requestAppointmentID':requestAppointmentID})

    def post(self, request, user):
        appointmentList = AppointmentForm(request.POST)

        requestAppointmentID = Appointment.objects.get(pk=user)
        
        appointmentList = Donor(requestAppointmentID=requestAppointmentID)

        appointmentList.save()

        return render(request, self.template_name, {'user': user, 'requestAppointmentID':requestAppointmentID})

class editOrganizerView(View):
    template_name = "user/editOrganizer.html"

    def get(self, request, user):
        return render(request, self.template_name, {'user': user})

class editDetailsView(View):
    template_name = "user/editDetails.html"

    def get(self, request, user):
        return render(request, self.template_name, {'user':user})

class viewDetailsView(View):
    template_name = "user/viewDetails.html"

    def get(self, request, user):
        return render(request, self.template_name, {'user':user})


