<p align="center"><img src="Screenshoot/Automation_Testing.jpg" style="width:50%"/></p>
<h1 align="center"> 
<b>Automation Testing</b>
</h1>
<p align ="justify">
Sebuah projek akhir bootcamp dari <b>PyAutoID</b> untuk melakukan test aplikasi berbasis <i>Web-Browser</i> secara otomatis. Testing menggunakan <b>Selenium</b> dengan bahasa yang digunakan adalah <b>Python</b>. Dengan <b>Pytest</b> sebagai framework testing tersebut. Dan hasil report dalam bentuk <b>html</b>.
</p>
<hr>
<br>

<h2><b>Project's Description</b>
</h2>
<hr>
<p align ="justify">
<b>Automation Testing</b> adalah melakukan uji perangkat lunak dengan secara otomatis dengan rangkaian uji yang sudah dibuat. Ini merupakan sebuah projek. Tools yang digunakan disini adalah <b>Selenium</b> yang merupakan tools auto testing yang digunakan untuk tes aplikasi berbasis <i>Web-Browser</i>.
</p>
<p align ="justify">
Bahasa pemrograman yang digunakan adalah <b>Python</b> untuk menulis script <b>Automation Testing</b>. Sedangkan untuk teks editor yang digunakan disini adalah menggunakan <b>Visual Studio Code</b>. <b>Automation Testing</b> ini merupakan sebuah projek akhir dari <b>Bootcamp Selenium PyAutoID</b> dengan alur tes melakukan login pada sebuah alamat Web. Framework testing yang digunakan adalah <b>Pytest</b> yang hasil dari testing tersebut akan ditampilkan dalam bentuk <b>HTML</b>. Alamat web yang digunakan untuk testing login disini adalah <a href="url">https://dribbble.com/session/new</a> 
<h3><b>Note</b></h3>
Pada alamat web tersebut terdapat limit akses ketika login seperti gambar berikut.
<img src="Screenshoot/LimitAkses.JPG">
</p>
<hr>
<br>

<h1><b>Scenario Testing</b></h1>
<p align = "justify"> Berikut skenario test yang dilakukan untuk automation testing. Skenario tersebut berupa test case yang akan dilakukan pada saat testing alamat web. Sesi yang diambil disini ketika user mencoba melakukan login menggunakan alamat email yang terdaftar maupun mencoba melakukan melakukan login dengan alamat email yang tidak terdaftar. Dengan expected resultnya ketika berhasil login akan dilanjutkan ke halaman HOME dari web dan ketika tidak berhasil melakukan login akan muncul notifikasi/alert bahwa email tidak terdaftar. </p>
<table>
<tr>
    <th>Test_ID</th>
    <th>Session</th>
    <th>Summary</th>
    <th>Action Step</th>
    <th>Expected Result</th>
</tr>
<tr>
    <td>Test_01</td>
    <td>User</td>
    <td>As a User, You can login with a Registered Email and Pasword</td>
    <td>
        <ol>
            <li>Go to Web Address https://dribbble.com/session/new</li>
            <li>Enter Registered Email Address</li> 
            <li>Enter the Registered Password</li>
            <li>Click the Sign-in button</li>
        </ol>
    </td>
    <td>Go to the Home Page</td>
</tr>
<tr>
    <td>Test_02</td>
    <td>User</td>
    <td>As a User, can't login with Unregistered Email</td>
    <td>
        <ol>
            <li>Go to Web Address https://dribbble.com/session/new</li>
            <li>Enter Unregistered Email Address</li> 
            <li>Enter Registered Password</li>
            <li>Click the Sign-in button</li>
        </ol>
    </td>
    <td>There is a notification or alert the account is not registered</td>
</tr>
<tr>
    <td>Test_03</td>
    <td>User</td>
    <td>As a User, can't login with Unregistered Password</td>
    <td>
        <ol>
            <li>Go to Web Address https://dribbble.com/session/new</li>
            <li>Enter Registered Email Address</li> 
            <li>Enter Unregistered Password</li>
            <li>Click the Sign-in button</li>
        </ol>
    </td>
    <td>There is a notification or alert the account is not registered</td>
</tr>
<tr>
    <td>Test_04</td>
    <td>User</td>
    <td>As a User, can't login with Unregistered Email and Password</td>
        <td>
        <ol>
            <li>Go to Web Address https://dribbble.com/session/new</li>
            <li>Enter Unregistered Email Address</li> 
            <li>Enter Unregistered Password</li>
            <li>Click the Sign-in button</li>
        </ol>
    </td>
    <td>Go to the Home Page</td>
</tr>
</table>

<h2><b>Dependencies</b>
</h2>
<hr>
<p>
<li>Operating System : Windows 10.</li>
<li>Teks Editor : Visual Studio Code.</li>
<li>Automation Tools : Selenium.</li>
<li>WebDriver : Chrome Driver.</li>
<li>Progamming Language : Python.</li>
<li>Framework Testing : Pytest.</li>
<li>Report Model : HTML.</li>
<li>Test Scenario</li>
</p>
<hr>
<br>

<h2><b>Installing</b>
</h2>
<hr>
<p>
<ul>
    <li>Install <b>Visual Studio Code</b> and <b>Python</b></li>
    <ol>
    <li>Download and Install <b>Visual Studio Code</b> :
    <a href="url">https://code.visualstudio.com/download</a></li>
    <li>Download and Install <b>Python</b> :
    <a href="url">https://www.python.org/downloads/</a></li>
    </ol>
    <li>Install <b>WebDriver</b></li>
    Driver disini tergantung web browser yang digunakan, dalam hal ini digunakan Chrome Driver. Dan jika menggunakan Chrome Driver diharapkan menggunakan versi terbaru sesuai versi yang ada pada Chrome. Berikut link download.
    <a href="url">https://chromedriver.chromium.org/</a>
    <li>Install <b>Selenium</b></li>
    Buka Command Prompt lalu masukkan perintah dibawah. Maka selenium akan terinstall.
    <div style="background-color:black;color:white;padding:10px">pip install selenium</div>
    <li>Install <b>Pytest</b></li>
    Buka Command Prompt lalu masukkan perintah dibawah. Maka pytest akan otomatis terinstall.
    <div style="background-color:black;color:white;padding:10px">pip install pytest</div>
    <li>Install <b>Pytest Html</b></li>
    Buka Command Prompt lalu masukkan perintah dibawah. Maka pytest html akan otomatis terinstall.
    <div style="background-color:black;color:white;padding:10px">pip install pytest-html</div>
</ul>
</p>
<hr>
<br>

<h2><b>Executing Program</b>
</h2>
<hr>
<ul>
    <li>Memulai program dengan memasukkan library webdriver dari selenium dan juga pytest dengan memasukkan perintah</li> 
    <div style="background-color:black;color:white;padding:10px" >
    from selenium import webdriver
    <br>import pytest</br>
    </div>
    <li>Memasukkan script untuk melakukan testing secara otomatis. Berikut listing program automation tersebut</li>
    <img src="Screenshoot/Script 1.JPG"/>
    <img src="Screenshoot/Script 2.JPG"/>
    <li>Menjalankan perintah tersebut dengan memasukkan perintah pada terminal yang terdapat pada teks editor sebagai berikut.</li>
    <div style="background-color:black;color:white;padding:10px" >
    python -m pytest -v test_namafile.py
    </div>
    Maka akan memunculkan output seperti gambar dibawah.
    <img src="Screenshoot/OutputTerminal.JPG"/>
    <li>Membuat output report kedalam bentuk html dengan memasukkan perintah berikut kedalam terminal.</li>
    <div style="background-color:black;color:white;padding:10px" >
    python -m pytest -v test_namafile.py --html=namafilereport.html
    </div>
    Maka hasil dari perintah tersebut akan memberikan file dalam bentuk html sebagai berikut.
    <img src="Screenshoot/ReportHtml.JPG"/>
    Sehingga lebih mudah dibaca daripada hasil output yang ditampilkan pada terminal.
</ul>
</p>
<br>

<h1><b>Author</b></h1>
<p>Mohammad Febrian Nur Ghifari Ramadhan
<br>Email : febrian0530@gmail.com
<br>Instagram : @mfebrianngr
</p>
<br>

<h1><b>Acknowledgments</b></h1>
<ul>
<li>PyAutoID yang telah memberi kesempatan untuk mengikuti Bootcamp </li>
<li>InterviewBit untuk gambar diawal judul</li>
</ul>





