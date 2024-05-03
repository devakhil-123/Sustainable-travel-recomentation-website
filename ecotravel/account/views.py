from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,ListView,TemplateView,DetailView,DeleteView
from .forms import LogForm,RegForm,BicycleForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from account.models import Accomodation,Selections,Review,Orders
from .models import BicycleModel
from django.contrib.auth import login,logout
from django.utils.decorators import method_decorator
from django.core.mail import send_mail


class LogView(View):
    def get(self,request):
        form=LogForm()
        return render(request,"log.html",{"form":form})
    def post(self,request):
        form=LogForm(data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get('username')
            pswd=form.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                return redirect('home')
            else:
                return redirect('log')

        return render(request,"log.html",{"form":form})
    


class RegView(View):
    def get(self,request):
        form=RegForm()
        return render(request,"reg.html",{"form":form})

    def post(self,request):
        form_data=RegForm(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Registration success!!")
            return redirect('log')
        messages.error(request,"Validation Failed!")
        return render(request,"reg.html",{"form":form_data})

class LogoutView(View):
     def get(self,request):
         logout(request)
         return redirect('log')



class HomeView(ListView):
    template_name="Home1.html"
    queryset=Accomodation.objects.all()
    context_object_name="data"



class HbookView(TemplateView):
    template_name="Hbook.html"



    

class bicycleView(DetailView):
    def get(self,request):
        form=BicycleForm()
        return render(request,"Bicycle1.html",{"form":form})
    
    def post(self,request):
       form_data=BicycleForm(data=request.POST)
       if form_data.is_valid():
           form_data.save()
           messages.success(request,"Registration success!!")
           return redirect('home')
       messages.error(request,"Validation Failed!")
       return render(request,"index1.html",{"form":form_data})
    


class BicycleDetails(ListView):
    template_name="bicycle.html"
    queryset=BicycleModel.objects.all()
    context_object_name="bicyclemodel"



class BookedBicycleDeleteView(DeleteView):
        model=BicycleModel
        success_url=reverse_lazy('bicycle1')
        template_name="BookedItemDelete.html"
        pk_url_kwarg="bid"





class DestinationView(TemplateView):
    def get(self,request):
        return render(request,"index8.html")

    # def get_queryset(self):
    #     queryset= super().get_queryset()
    #     # fid=self.kwargs.get('fid')
    #     # bicycleModel=BicycleModel.objects.get(id=fid)
    #     queryset=queryset.f
    #     return queryset









    
class AccomodationView(ListView):
    template_name="accomodation.html"
    queryset=Accomodation.objects.all()
    context_object_name="accomodation"


class DetailsView(ListView):
    template_name="details.html"
    queryset=Accomodation.objects.all()
    context_object_name="accomodation"

    def get_context_data(self, **kwargs):
        res=Accomodation.objects.filter(type=self.kwargs.get('cat'))
        return super().get_context_data(**kwargs)



    

class TypeView(View):
    def get(self,request,*args,**kwargs):
       id=kwargs.get('hid')
       acc=Accomodation.objects.get(id=id)
       return render(request,"viewdetails.html",{"data":acc})

       
    


    


class Order1View(DetailView):
    template_name="accbooking.html"
    queryset=Accomodation.objects.all()
    pk_url_kwarg='pid'
    context_object_name="accomodation"
    def get_context_data(self, **kwargs:any):
               context=super().get_context_data(**kwargs)
               pid=self.kwargs.get('pid')
               accomodation=Accomodation.objects.get(id=pid)
               rev=Review.objects.filter(accomodation=accomodation)
               context["reviews"]=rev
               return context
   

def addtoselection(request,*args,**kwargs):
    pid=kwargs.get('pid')
    acco=Accomodation.objects.get(id=pid)
    userdata=request.user
    print(userdata)
    Selections.objects.create(accomodation=acco,user=userdata)
    messages.success(request,"Booking Done")
    return redirect('home')



class BookedListView(ListView):
    template_name="Booked.html"
    queryset=Selections.objects.all()
    context_object_name="accomodation"

    def get_queryset(self):
        res=super().get_queryset()
        res=res.filter(user=self.request.user)
        print(res)
        return res





class BookedItemDeleteView(DeleteView):
        model=Selections
        success_url=reverse_lazy('blist')
        template_name="BookedItemDelete.html"
        pk_url_kwarg="sid"

# @signin_required
def addreview(request,**kwargs):
        review=request.POST.get('rev')
        accomodation_id=kwargs.get('pid')
        accomodation=Accomodation.objects.get(id=accomodation_id)
        user=request.user
        print(review,accomodation_id)
        Review.objects.create(review=review,user=user,accomodation=accomodation)
        messages.success(request,"Review added")
        return redirect('home')

# @method_decorator(signin_required,name="dispatch")
class bookView(TemplateView):
    template_name="Hbook.html"
    def post(self,request,*args,**kwargs):
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        sid=kwargs.get('sid')
        selections=Selections.objects.get(id=sid)
        accomodation=selections.accomodation
        user=request.user
        Orders.objects.create(accomodation=accomodation,user=user,address=address,phone=phone)
        selections.status="Booking Finished"
        selections.save()
        messages.success(request,"Booking finished Successfully")
        to_mail=request.user.email
        msg=f"Booking for the {accomodation.name} is finished successfully!!check your travel account for more details"
        from_mail="akhildevm436@gmail.com"
        subject="Booking confirmation"
        send_mail(subject,msg,from_mail,{to_mail})
        return redirect('home')
    
# @method_decorator(signin_required,name="dispatch")
class BookedflistView(ListView):
    template_name="finishedbook.html"
    queryset=Orders.objects.all()
    context_object_name="orders"
    

    def get_queryset(self):
        queryset= super().get_queryset()
        queryset=queryset.filter(user=self.request.user)
        return queryset


# @signin_required
def cancelView(request,**kwargs):
        oid=kwargs.get('oid')
        order=orders.objects.get(id=oid)
        order.order_status="Cancelled"
        order.save()
        #mail service
        to_mail=request.user.email
        msg=f"Order for the product {order.accomodation.name} is cancelled successfully!!check your travel account for more details"
        from_mail="akhildevm436@gmail.com"
        subject="Order cancellation confirmation"
        send_mail(subject,msg,from_mail,{to_mail})
        return redirect('mview')



