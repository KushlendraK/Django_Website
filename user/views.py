from django.shortcuts import HttpResponse,render,redirect
import random
import mysql.connector as mysql
from datetime  import datetime
def home(req):
    con = mysql.connect(host="localhost", user="root",
                            password="kush", database="django3", charset="utf8")
    cr = con.cursor()   
    sql = "select * from admin_item"    
    cr.execute(sql)         
    all_data = cr.fetchall()
    con.commit()
    con.close()
    return render(req, 'index.html',{'all_data':all_data})



def login(request):
    num=random.randrange(112121,989329)
    global str_num
    str_num=str(num)
    return render(request,"login.html",{"img":str_num})



def login_user(req):
    choose1 = req.GET.get('choose')
    cap = req.GET.get('cap')
    if choose1 == "user":
        if cap == str_num:             
            email = req.GET.get('email')
            password = req.GET.get('pass')
            con = mysql.connect(host="localhost", user="root",
                                password="kush", database="django3")
            cr = con.cursor()
            sql = "select * from student where email='{0}' and cpass='{1}'".format(
                email, password)
            cr.execute(sql)     
            rec = cr.fetchall()
            global rec1
            rec1 = rec
            con.close()
            if rec == []:
                return redirect("/user/login")
            else:         
                return redirect("/user/user_dash")
        else:
            return redirect("/user/login")

    elif choose1 == 'admin':               
        if cap == str_num:             
            email = req.GET.get('email')
            password = req.GET.get('pass')
            con = mysql.connect(host="localhost", user="root",
                                password="kush", database="django3")
            cr = con.cursor()
            sql = "select * from admin1 where email='{0}' and pass='{1}'".format(
                email, password)
            cr.execute(sql)     
            rec_admin = cr.fetchall()
            global rec3
            rec3 = rec_admin
            con.close()
            if rec_admin == []:
                return redirect("/user/login")
            else:
                return redirect("/user/admin_dash")
        else:
            return redirect("/user/login")

    elif choose1 == "employe":
        cap = req.GET.get('cap')
        if cap == str_num:             
            email = req.GET.get('email')
            password = req.GET.get('pass')
            con = mysql.connect(host="localhost", user="root",
                                password="kush", database="django3")
            cr = con.cursor()
            sql = "select * from emp where email='{0}' and cpass='{1}'".format(
                email, password)
            cr.execute(sql)     
            rec = cr.fetchall()
            global rec2           
            rec2 = rec
            con.close()
            if rec == []:
                return redirect("/user/login")
            else:         
                return redirect("/user/emp_dash")
        else:
            return redirect("/user/login")

def emp_dash(req):
    if rec2 == []:
        return redirect("/user/login")
    else:
        detail = rec2[0][0]
        return render(req,'emp_dash.html',{'name':detail})
        


def admin_dash(req):
    if rec3 == []:
        return redirect("/user/login")
    else:
        con = mysql.connect(host="localhost", user="root",
                                password="kush", database="django3")
        cr = con.cursor()
        sql = "select count(Id) from admin_item"
        cr.execute(sql)   
        tot_item = cr.fetchone()
        tot_item1 = tot_item[0]
        con.commit()
        sql1 = "select count(user_id) from student"
        cr.execute(sql1)   
        tot_user = cr.fetchone()
        tot_user1 = tot_user[0]
        con.commit()
                 
        return render(req, 'admin_dash.html',{'tot_item':tot_item1,'tot_user':tot_user1})


    #  user side data

def user_dash(req):
    if rec1 == []:
        return redirect("/user/login")
    else:
        global g_email, g_name,g_id
        g_email = rec1[0][4]
        g_name = rec1[0][1]
        g_id = rec1[0][0]
        detail = rec1[0][1]
        con = mysql.connect(host="localhost", user="root",
                            password="kush", database="django3", charset="utf8")
        cr = con.cursor()   
        sql = "select * from admin_item"    
        cr.execute(sql)         
        all_data = cr.fetchall()
               
        return render(req, 'user_dash.html',{'name':detail,'data1':all_data})




def signup(req):
    return render(req, 'signup.html')

def new_user(req):
    select1 = req.GET.get('select')
    name = req.GET.get('name')
    fname = req.GET.get('fname')  
    mobile = req.GET.get('mobile')  
    email = req.GET.get('email')
    address = req.GET.get('add')
    cpass = req.GET.get('cpass')

    if select1 == "user":        
        con = mysql.connect(host="localhost", user="root",
                            password="kush", database="django3", charset="utf8")
        cr = con.cursor()   
        sql = "insert into student(name,fname,mobile,email,address,cpass) value('{0}','{1}','{2}','{3}','{4}',{5})".format(name, fname,mobile, email, address ,cpass)
        cr.execute(sql)
        con.commit()
        con.close()
        return redirect('/user/login')

    elif select1 == "employe":      
        con = mysql.connect(host="localhost", user="root",
                            password="kush", database="django3", charset="utf8")
        cr = con.cursor()   
        sql = "insert into emp(name,fname,mobile,email,address,cpass) value('{0}','{1}','{2}','{3}','{4}',{5})".format(name, fname,mobile, email, address ,cpass)
        cr.execute(sql)
        con.commit()
        con.close()
        return render(req, 'emp_user.html',{'name':name})

def user_logout(req):
    rec1.clear()
    return redirect('/user/home')

def emp_logout(req):
    rec2.clear()
    return redirect('/user/home')

def admin_logout(req):
    rec3.clear() 
    return redirect('/user/home')






# add items by admin side

def add_item(req):
    return render(req, 'add_item.html')

def admin_items(req):
    pro_type = req.GET.get('type')
    name = req.GET.get('name')
    price = req.GET.get('price')
    quan = req.GET.get('quantity')    
    con = mysql.connect(host="localhost", user="root",
                            password="kush", database="django3", charset="utf8")
    cr = con.cursor()   
    sql = "insert into admin_item(pro_type,pro_name,price,quantity) value('{0}','{1}','{2}',{3})".format(pro_type,name, price,quan)
    cr.execute(sql)
    con.commit()
    con.close()
    return redirect('/user/admin_dash')

def show_all_items(req):
    con = mysql.connect(host="localhost", user="root",
                                password="kush", database="django3")
    cr = con.cursor()
    sql = "select * from  admin_item"
    cr.execute(sql)     
    rec = cr.fetchall()
    return render(req, 'show_all_items.html',{'all':rec})

def admin_search(req):
    return render(req,'admin_search.html')


def search_by_category(req):
    choose1 = req.GET.get('choose')
    con = mysql.connect(host="localhost", user="root",
                            password="kush", database="django3")
    cr = con.cursor()
    if choose1 == 'Clothes':        
        sql = "select * from admin_item where pro_type='{0}'".format(choose1)
        cr.execute(sql)     
        rec = cr.fetchall()
        return render(req,'clothes.html',{'cloth':rec})

    elif choose1 == 'Shoes':
        sql = "select * from admin_item where pro_type='{0}'".format(choose1)
        cr.execute(sql)     
        rec = cr.fetchall()
        return render(req,'shoes.html',{'shoes':rec})

    elif choose1 == 'Mobile':
        sql = "select * from admin_item where pro_type='{0}'".format(choose1)
        cr.execute(sql)     
        rec = cr.fetchall()
        return render(req,'mobile.html',{'mobile':rec})
    
    else:
        return HttpResponse("No product Found")


def cart(req): 
    # item = req.GET.get('cart')
     
    pro_id = req.GET.get('id')
    con = mysql.connect(host="localhost", user="root",
                            password="kush", database="django3", charset="utf8")
    cr = con.cursor()   
    sql = "select * from admin_item where Id='{0}'".format(pro_id)
    cr.execute(sql)
    data = cr.fetchall()
    con.commit()
    con.close()
    return render(req,'cart.html',{'pro_code':pro_id,'data':data} )

def buy(req):
    x = datetime.now()
    year  = str(x.year)
    month = str(x.month)
    day = str(x.day)
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    time1 = str(time)
    date = str(day+"/"+month+"/"+year)
     
    id1 = req.GET.get('id')
    name = req.GET.get('name')
    price = req.GET.get('price')
    quantity1 = int(req.GET.get('quantity1'))
    con = mysql.connect(host="localhost", user="root",
                            password="kush", database="django3", charset="utf8")
    cr = con.cursor()   
    sql = "select * from admin_item where Id='{0}'".format(id1)
    cr.execute(sql) 
    a = cr.fetchall()
    a1 = a[0][4]
    if a1 > 0:    
        left_product = a1-quantity1
        sql1 = "update admin_item set quantity={0} where Id='{1}'".format(left_product,id1)         
        cr.execute(sql1)
        con.commit()
        sql2 = "insert into  user_buy_record(user_id,name,email,pro_id,pro_name,quantity,price,Date1,time1) value('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(g_id,g_name,g_email,id1,name,quantity1,price,date,time1)
        cr.execute(sql2)
        con.commit()
        con.close()
        return render(req,'buy_success.html')
    else:
        return render(req,'pro_not_available.html')

def invoice(req):
    return render(req,'invoice.html')

def sales_history(req):
    con = mysql.connect(host="localhost", user="root",
                            password="kush", database="django3", charset="utf8")
    cr = con.cursor()   
    sql = "select * from  user_buy_record"
    cr.execute(sql) 
    a = cr.fetchall()
    return render(req,'sales_history.html',{'a':a})

def user_shopping(req):
    con = mysql.connect(host="localhost", user="root",
                            password="kush", database="django3", charset="utf8")
    cr = con.cursor()   
    sql = "select * from user_buy_record where user_id='{0}'".format(g_id)
    cr.execute(sql) 
    a = cr.fetchall()
    return render(req,'user_shopping_details.html',{'data':a})

def show_cart_detail(req):
    con = mysql.connect(host="localhost", user="root",
                            password="kush", database="django3", charset="utf8")
    cr = con.cursor()   
    sql = "select * from user_cart where user_id='{0}'".format(g_id)
    cr.execute(sql)
    a = cr.fetchall()
    con.commit()
    return render(req,'show_cart_detail.html',{'data':a})

def add_to_cart(req):
    
    id2 = req.GET.get('id')    
    con = mysql.connect(host="localhost", user="root",
                            password="kush", database="django3", charset="utf8")
    cr = con.cursor()   
    sql1 = "select * from admin_item where Id='{0}'".format(id2)
    cr.execute(sql1)
    product = cr.fetchall()
    pro_type = product[0][1]
    pro_name = product[0][2]
    pro_id = product[0][0]
    price = product[0][3]

    sql = "insert into user_cart(user_id,pro_type,pro_id,pro_name,price) value('{0}','{1}','{2}','{3}','{4}')".format(g_id,pro_type,pro_id,pro_name,price)
    cr.execute(sql) 
    con.commit()
    sql2 = "select * from user_cart where user_id='{0}'".format(g_id)
    cr.execute(sql2)    
    cart = cr.fetchall()
    con.commit()
    con.close()
    return render(req, 'user_cart_page.html',{'data1':cart})

        
        # sql2 = "select * from user_cart where user_id='{0}'".format(g_id)
        # cr.execute(sql2)    
        # cart = cr.fetchall()
        # con.commit()
        # con.close()
        # return render(req, 'user_cart_page.html',{'data1':cart})

 

def user_cart_page(req):
    return render(req,'user_cart_page.html',{'data1': cart})

    

def delete_item(req):
    return render(req,'delete_item.html')

def admin_delete_item(req):
    pro_id=req.GET.get('id')
    con = mysql.connect(host="localhost", user="root",
                            password="kush", database="django3", charset="utf8")
    cr = con.cursor()   
    sql = "delete from admin_item where Id ='{0}'".format(pro_id)
    cr.execute(sql)
    con.commit()
    con.close()
     
    return redirect('/user/show_all_items')

def admin_edit_item(req):
    pro_id=req.GET.get('item')
    con = mysql.connect(host="localhost", user="root",
                            password="kush", database="django3", charset="utf8")
    cr = con.cursor()   
    sql = "select * from admin_item where Id='{0}'".format(pro_id)
    cr.execute(sql)
    a = cr.fetchall()
    con.commit()
    con.close()
    
    return render(req, 'admin_edit.html', {'data': a})

def admin_edit_item_set(req):
    id1 = req.GET.get('id')
    price = req.GET.get('price')
    con = mysql.connect(host="localhost", user="root",
                            password="kush", database="django3", charset="utf8")
    cr = con.cursor()   
    sql = "select * from admin_item where Id='{0}'".format(id1)
    cr.execute(sql)
    a = cr.fetchall()
    a1 = a[0][4]
    con.commit()
    

    quantity = int(req.GET.get('quantity1'))
    tot_quan =a1 + quantity
    con = mysql.connect(host="localhost", user="root",
                            password="kush", database="django3", charset="utf8")
    cr = con.cursor()   
    sql1 = "update admin_item set quantity={0},price='{1}' where Id='{2}'".format(tot_quan,price,id1)         
    
    cr.execute(sql1)
    con.commit()
    con.close()
    return redirect('/user/show_all_items')

def show_all_user(req):
    con = mysql.connect(host="localhost", user="root",
                            password="kush", database="django3", charset="utf8")
    cr = con.cursor()   
    sql = "select * from student"
    cr.execute(sql)
    a = cr.fetchall()    
    con.commit()
    con.close()
    return render(req, 'admin_all_user_data.html',{'a':a})

def admin_delete_user(req):
    id1 = req.GET.get('id')
    con = mysql.connect(host="localhost", user="root",
                            password="kush", database="django3", charset="utf8")
    cr = con.cursor()   
    sql = "delete from student where user_id='{0}'".format(id1)
    cr.execute(sql) 
    con.commit()
    con.close()
    return  redirect('/user/show_all_user')
