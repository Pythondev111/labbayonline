
$(document).ready(function(){


	/* ---- Countdown timer ---- */

	// $('#counter').countdown({
	// 	timestamp : (new Date()).getTime() + 11*24*60*60*1000
	// });


	/* ---- Animations ---- */

	$('#links a').hover(
		function(){ $(this).animate({ left: 3 }, 'fast'); },
		function(){ $(this).animate({ left: 0 }, 'fast'); }
	);

	$('footer a').hover(
		function(){ $(this).animate({ top: 3 }, 'fast'); },
		function(){ $(this).animate({ top: 0 }, 'fast'); }
	);
	const signIn = `<div id="id01" class="modal">
//    <form action="{% url 'signin' %}" class="modal-content animate" method='get'>
//        <div class="imgcontainer">
//            <span onclick="document.getElementById('id01').style.display = 'none'" class="close" title="Close Modal">&times;</span>
//            <img src="./images/logo1.jpg" alt="Avatar" class="avatar">
//        </div>
//        <div class="conta">
//            <label> <b>Login</b></label>
//            <input type="text" placeholder="Loginni kiriting" name="uname" required>
//            <label><b>Parol</b></label>
//            <input type="password" placeholder="Parolni kiriting" name="parol" required>
//            <button type="submit">Login</button>
//            <input type="checkbox" checked="checked">
//            remember me
//        </div>
//    </form>
</div>`;
document.querySelector('.signIn').addEventListener('click',function(){
	  document.querySelector('#signIn').innerHTML = signIn;
	  document.getElementById('id01').style.display ='block';
	  document.getElementById('id01').style.width ='auto';
})

var modal = document.getElementById('id01');

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};
	const logIn = `<div id="id02" class="modal">
    <form action="{% url 'signin' %}" class="modal-content animate" method='get'>
        <div class="imgcontainer">
            <span onclick="document.getElementById('id02').style.display = 'none'" class="close" title="Close Modal">&times;</span>
            <img src="./images/logo1.jpg" alt="Avatar" class="avatar">
        </div>
        <div class="conta">
            <label> <b>Ismingiz</b></label>
            <input type="text" placeholder="Ismingiz" name="ism" required>
            <label for="number"><b>Telefon raqamingiz</b></label>
            <input type="text"placeholder="+998 91 123 45 67" id="phone" name='tel' >
           <br> 
           <label>Jinsni tanlang</label><br>
           <label class="radio-inline">
            <input type="radio" name="erkak" checked>Erkak
          </label>
          <label class="radio-inline">
            <input type="radio" name="ayol">Ayol
          </label><br>
          <label for sel1>Yosh oralig'ini tanlang</label>
          <select class="form-control" id="sel1" name='yosh'>
          <option>8-15</option>
          <option>15-25</option>
          <option>25-40</option>
          <option>40-55</option>
          <option>55+</option>
        </select>
        <label> <b>Username</b></label>
            <input type="text" placeholder="Username..." name="username" required>
        <label for="password"><b>Parol</b></label>
            <input type="password" name='parol' placeholder="Parolni kiriting" id="password">
            <label><b>Parolni takrorlang</b></label>
            <input type="password" placeholder="Parolni takrorlang" name="parol2" required>
            <button type="submit">Login</button>
        </div>
    </form>
</div>`;
document.querySelector('.logIn').addEventListener('click',function(){
	  document.querySelector('#logIn').innerHTML = logIn;
	  document.getElementById('id02').style.display ='block';
	  document.getElementById('id02').style.width ='auto';
})

var modal = document.getElementById('id02');

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

window.addEventListener('DOMContentLoaded', function(){
    let loader = document.querySelector('.loader')
    setTimeout(()=>{
        loader.style.opacity = '0'
        setTimeout(()=>{
            loader.style.display = 'none'
        },500)
    },2000)
})
});
