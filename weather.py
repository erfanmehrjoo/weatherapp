import tkinter as tk
import requests
from translate import Translator
import datetime
from tkinter.messagebox import showerror
### all the requirment imported

### make the interface
root = tk.Tk()
root.title("آب و هوا")
root.minsize(200 , 500)

### make thr text variable
city_name = tk.StringVar()
city_label = tk.StringVar()
wheather_type = tk.StringVar()
temp = tk.StringVar()
wind = tk.StringVar()
sunset = tk.StringVar()
### make the functions
def second_to_clock(seconds):
        m , s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return h, m, s

def time_calculate(seconds):
    sunsetdate = datetime.datetime.fromtimestamp(seconds)
    now = datetime.datetime.now()
    if now >  sunsetdate:
        result = now - sunsetdate
        second = result.seconds
        h,m,s = second_to_clock(second)
        sunset.set(str(h)+"ساعت و"+str(m)+ "دقیقه و"+str(s)+" ثانیه پیش")
        
    else:
        result = sunsetdate - now
        second = result.seconds
        h,m,s = second_to_clock(second)
        sunset.set(str(h)+"ساعت و"+str(m)+ "دقیقه و"+str(s)+" ثانیه دیگر")


def search():
    city = city_name.get()
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    app_id = "109d424b54ae460e540bad9953047757"
    try:
        result = requests.get(url.format(city, app_id)).json()
        translator= Translator(to_lang="Persian")
        status = translator.translate(result['weather'][0]['main'])
        city = translator.translate(result['name'])
        wheather_type.set(status)
        city_label.set(city)
        temp.set(str(round(result['main']['temp']-273.15,2) )+'درجه سانتی گراد')
        wind.set(str(result['wind']['speed'])+"متر بر ثانیه")
        time_calculate(result['sys']['sunset'])
    except:
        showerror("خطا!"," نام شهر صحیح نمی باشد یا خطای اجرایی است که نگران نباشید")
        city_name.set("")
### make the weidgets funtions
def widgets():
    label = tk.Label(root , text="وضعیت آب و هوا" , width=25 , height=2)
    label.config(font=('Titr' , 22 , 'bold') , fg='#000' , bg='lightblue')
    label.grid(row=0 , columnspan=2)

    label_name = tk.Label(root , text="نام شهر" )
    label_name.config(font=('Lalezar' , 18 , 'bold') , fg='red')
    label_name.grid(row=1 , column=0 , pady=20)

    input_name = tk.Entry(root , textvariable=city_name)
    input_name.grid(row=1 , column=1 , pady=10)

    search_btn = tk.Button(root , text="جستجو" , width=10 , height=2 , background='green' , fg='white' , font=('None' , 15) , command=search)
    search_btn.grid(row=2 , columnspan=2 , pady=10)  

    label_city_name = tk.Label(root , text="نام شهر" , font=("Aviny",16,"bold"), fg="blue")
    label_city_name.grid(row=3 , column=0 , pady=10)

    label_city = tk.Label(root , text='' , font=("Aviny",16,"bold"), fg="black" , textvariable=city_label)
    label_city.grid(row=3 , column=1 , pady=10)

    label_weather_type = tk.Label(root , text='وضعیت' , font=("Aviny",16,"bold"), fg="blue" )
    label_weather_type.grid(row=4 , column=0 , pady=10)

    label_wheather = tk.Label(root , text='' , font=("Aviny",16,"bold"), fg="black" , textvariable=wheather_type )
    label_wheather.grid(row=4 , column=1 , pady=10)

    label_temp = tk.Label(root , text='دما' , font=("Aviny",16,"bold"), fg="blue" )
    label_temp.grid(row=5, column=0 , pady=10)

    label_temp_show = tk.Label(root , text='' , font=("Aviny",16,"bold"), fg="black"  , textvariable=temp)
    label_temp_show.grid(row=5 , column=1 , pady=10)

    label_wind = tk.Label(root , text='باد' , font=("Aviny",16,"bold"), fg="blue" )
    label_wind.grid(row=6 , column=0 , pady=10)

    label_wind_show = tk.Label(root , text='' , font=("Aviny",16,"bold"), fg="black" , textvariable=wind)
    label_wind_show.grid(row=6 , column=1 , pady=10)

    label_sunset = tk.Label(root , text='غروب خورشید' , font=("Aviny",16,"bold"), fg="blue" )
    label_sunset.grid(row=7 , column=0 , pady=10)

    label_sunset_show = tk.Label(root , text='' , font=("Aviny",16,"bold"), fg="black" , textvariable=sunset)
    label_sunset_show.grid(row=7 , column=1 , pady=10)


widgets()



### make the app loop
root.mainloop()