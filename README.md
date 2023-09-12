Pembuatan Tugas 2

Link Url Website : https://website-v1.adaptable.app/main/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    a. Membuat sebuah projek django
        Dengan menggunakan syntax django-admin startproject pbptugas2 ., kita meminta framework django untuk membuatkan
        kita sebuah projek yang sudah lengkap dengan beberapa file yang penting.
    b. Membuat aplikasi dengan nama main pada proyek tersebut
        Untuk membuat app dengan nama main kita memakai syntax python manage.py startapp main.
        Setelah dijalankan maka akan muncul direktori main khusus.
    c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
        Agar bisa menjalanlan routing, kita membuka berkas settings.py di direktori pbptugas2 dan mencari
        variable INSTALLED APPS dan menambahkan 'main' agar terdaftarkan dalam projek kita,
    d.  Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
        Dengan menuliskan pada models.py:
        from django.db import models

        class Item(models.Model):
            name = models.CharField(max_length=255,default="")
            amount = models.IntegerField(default=0)
            description = models.TextField(default = "")

        artinya kita membuat sebuah models pada django kita yang berisi Item yang memiiki beberapa atribut
        seperti name, amount, dan description

    e.  Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta   nama dan kelas kamu.
        Dengan menuliskan pada views.py:

        from django.shortcuts import render
            def show_main(request):
                context = {
                'application': 'Miracle',
                'name': 'Kevin Ignatius Wijaya',
                'class': 'PBP F'
             }

        return render(request, "main.html", context)

        artinya kita meminta parameter request yang berfungsi mengatur permintaan HTTP dengan template seperti 
        folder templates.
        lalu mengirimkan context yang berisi data untuk diberikan kepada templates dan mereturn render 
        untuk merender tampilan pada HTML.
    
    f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

        Dengan menuliskan urls.py dalam direkotri main :

            from django.urls import path
            from main.views import show_main

            app_name = 'main'

            urlpatterns = [
            path('', show_main, name='show_main'),
            ]
        
        Berkas ini mengatur rute url yang terkait pada aplikasi main 
        dengan menggunakan import path kita mendefinisikan pola urls nya lalu menggunakan fungsi show_main
        dari modulnya untuk menampilkan views.py ketika url diakses.

    g.  Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
        Membuat akun adaptable lalu memasukan repo github projek yang diinginkan. Lalu memilih python app template , postgres sql dan memberikan python version serta menuliskan command python manage.py migrate && gunicorn pbptugas2.wsgi. Lalu memberikan nama aplikasi dan http port. Setelah itu mendeploynya ke adaptable.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.


3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Ada 3 alasan:
    a. Untuk mengisolasi pustaka dan modul
     karena setiap proyek memperlukan pustaka dan modul yang berbeda

    b. Untuk menghindari konflik pustaka
    jika ingin membuat sebuah proyek dengan versi pustaka yang sama kita memerlukan virtual envinronment agar tidak konflik saat 1 proyek memiliki beberapa versi

    c. Untuk mempermudah pengembangan
    kita bisa ganti ganti dari 1 proyek ke proyek lain dengan mudah saat menggunakan virtual environment .

    kita tetap bisa membuat aplikasi dgn framework django tanpa virtual environment namun bisa menyebabka konflik versi pustaka dan proyek yang tidak stabil

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya

MVC, MVT, dan MVVM adalah tiga desain arsitektur yang umum digunakan dalam pengembangan perangkat lunak. Ketiganya membagi aplikasi menjadi tiga komponen utama: model, view, dan controller.

MVC (Model-View-Controller) adalah desain arsitektur yang paling umum digunakan. MVC membagi aplikasi menjadi tiga komponen utama:

Model: Model adalah komponen yang bertanggung jawab untuk menyimpan data dan logika bisnis.
View: View adalah komponen yang bertanggung jawab untuk menampilkan data ke pengguna.
Controller: Controller adalah komponen yang bertanggung jawab untuk menerima input dari pengguna dan memperbarui model dan view.
MVT (Model-View-Template) adalah desain arsitektur yang mirip dengan MVC, tetapi dengan perbedaan utama bahwa view dan template digabungkan menjadi satu komponen.

Model: Sama seperti MVC.
View: Sama seperti MVC, tetapi juga bertanggung jawab untuk menghasilkan kode HTML untuk menampilkan data ke pengguna.
Template: Template adalah kode HTML statis yang digunakan oleh view untuk menghasilkan kode HTML yang dinamis.
MVVM (Model-View-ViewModel) adalah desain arsitektur yang mirip dengan MVC, tetapi dengan perbedaan utama bahwa view dan controller digabungkan menjadi satu komponen.

Model: Sama seperti MVC.
View: Sama seperti MVC, tetapi juga bertanggung jawab untuk menerima input dari pengguna dan memperbarui model.
ViewModel: ViewModel adalah komponen yang bertindak sebagai mediator antara model dan view. ViewModel bertanggung jawab untuk menyediakan data yang diperlukan ke view dan memperbarui model berdasarkan input dari view.
Perbedaan utama dari ketiga desain arsitektur ini adalah peran dari controller dan view. Pada MVC, controller bertanggung jawab untuk menerima input dari pengguna dan memperbarui model dan view. Pada MVT, view dan template digabungkan menjadi satu komponen yang bertanggung jawab untuk menampilkan data ke pengguna dan menerima input dari pengguna. Pada MVVM, view dan controller digabungkan menjadi satu komponen yang bertanggung jawab untuk menampilkan data ke pengguna dan memperbarui model.







