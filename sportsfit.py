import cherrypy
from login import LoginPage 
from products import Products
from productdetails import ProductPage
from contact import ContactPage
from cart import CartPage
from wishlist import WishlistPage
from checkout import CheckoutPage

class SportsFitECommerce:
    def __init__(self):
      self.wishlist = WishlistPage()
      self.cart = CartPage()
      self.product = ProductPage()
     
    @cherrypy.expose
    def index(self, name=None):
        if name:
            return f"<h1>Welcome, {name}!</h1>"
        return """
        <html>
        <head>
            <title>SportsFit - Home</title>
            <style>
                * { margin: 0; padding: 0; box-sizing: border-box; }
                body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: white; }
                /* Header */
                header {
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    background-color: rgb(4 3 3 / 80%);
                    color: #f1f1f1;
                    padding: 1px 20px;
                    position: sticky;
                    top: 0;
                    z-index: 1000;
                    transition: background-color 0.3s ease;
                    font-family: Arial, sans-serif;
                }

                /* Logo */
                .logo {
                    font-size: 37px;
                    font-family: math;
                    color: #fff;
                    margin: 20px;
                }

                /* Hamburger Menu */
                .hamburger-menu {
                    display: flex;
                    align-items: center;
                    cursor: pointer;
                    width: 60px;
                }
                .hamburger-menu:hover{
                    border: 2px solid white;
                }

                .hamburger-menu svg {
                    fill: #fff;
                }

                /* Menu Box */
                .menu-box {
                    position: fixed;
                    top: 0;
                    left: -100%;
                    height: 100vh;
                    width: 300px;
                    background-color: #333;
                    color: #f1f1f1;
                    display: flex;
                    flex-direction: column;
                    padding: 20px;
                    transition: 0.3s ease;
                }

                .menu-box.open {
                    left: 0;
                }

                .close-btn {
                    background: none;
                    color: #f1f1f1;
                    font-size: 24px;
                    border: none;
                    cursor: pointer;
                    align-self: flex-end;
                }

                .menu-section {
                    margin-bottom: 20px;
                }

                .menu-section h3 {
                    margin-bottom: 10px;
                    font-size: 18px;
                }

                .menu-section a {
                    color: #f1f1f1;
                    text-decoration: none;
                    font-size: 19px;
                    margin-bottom: 10px;
                    display: block;
                    transition: 0.2s ease;
                }

                .menu-section a:hover {
                    color: #ff9800;
                }

                .user_logo a{
                    font-size: 2rem;
                    margin: 20px;
                    user-select: none;
                }
                .user_logo a:hover{
                    color: #ff9800;
                    user-select: none;
                }
                /* Dropdown Menu */
                .dropdown-menu a {
                    margin-left: 10px;
                }
                /* Search bar  */
                .search-bar {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    margin: 20px auto;
                    width: 60%; /* Adjust width as needed */
                    max-width: 800px;
                    background-color: white;
                    border: 1px solid #ddd;
                    border-radius: 50px;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                    overflow: hidden;
                }

                .search-bar input {
                    flex-grow: 1;
                    font-size: 20px;
                    border: none;
                    outline: none;
                    padding: 12px 15px;
                    border-radius: 50px 0 0 50px;
                    color: #333;
                    font-family: Arial, sans-serif;
                }

                .search-bar input::placeholder {
                    color: #aaa;
                    font-style: italic;
                }

                .search-bar button {
                    background-color: #febd69; /* Amazon's signature color */
                    border: none;
                    padding: 11px 20px;
                    cursor: pointer;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    border-radius: 0 50px 50px 0;
                    transition: background-color 0.3s ease;
                }

                .search-bar button:hover {
                    background-color: #f90;
                }

                .search-bar button svg {
                    width: 20px;
                    height: 20px;
                    fill: #333;
                    transition: fill 0.3s ease;
                }

                .search-bar button:hover svg {
                    fill: black;
                }


                /* Icons */
                .icon {
                    display: flex;
                    gap: 40px;
                }

                .icon a {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: #fff;
                }

                .icon svg {
                    fill: #fff;
                    width: 24px;
                    height: 24px;
                    cursor: pointer;
                }
                .icon svg:hover {
                    border: 2px solid white;
                    padding: 2px;
                    border-radius: 20px;
                }
                .prodetails {
                   display: inline-block;
                   text-align: center;
                   text-decoration: none;
                   color: light-blue; 
                   padding: 8px 15px;
                   font-size: 14px;
                   border-radius: 5px;
                   border: 1px solid #0056b3;
                   background-color: #75CDD2; 
                   cursor: pointer;
                   transition: background-color 0.2s ease, color 0.2s ease;
                }
                .prodetails:hover {
                    background-color: #585EBA;
                    transform: scale(1.05);
                    color: white; 
                }
                /*Background image slider */
                /* Slider Container */
                .background-slider-container {
                    position: relative;
                    width: 100%;
                    height: 600px; /* Adjust height based on preference */
                    overflow: hidden;
                }

                /* Slider and Slides */
                .background-slider {
                    display: flex;
                    transition: transform 1s ease-in-out;
                    height: 100%;
                }

                .background-slide {
                    min-width: 100%;
                    height: 100%;
                    background-size: cover;
                    background-position: center;
                }

                /* Dots Navigation */
                .slider-dots {
                    position: absolute;
                    bottom: 20px;
                    left: 50%;
                    transform: translateX(-50%);
                    display: flex;
                    gap: 15px;
                    z-index: 10;
                }

                .dot {
                    width: 15px;
                    height: 15px;
                    background-color: rgba(255, 255, 255, 0.5);
                    border-radius: 50%;
                    cursor: pointer;
                    transition: background-color 0.3s ease;
                }

                .dot.active {
                    background-color: #007bff;
                }
                .title{text-align: center; margin: 70px;}
                .slider { display: grid; width: 80vw; margin: 20px auto; overflow: hidden; position: relative;}
                .slides { display: flex; transition: transform 0.5s ease-in-out; }
                .slide { min-width: 100%; box-sizing: border-box; text-align: center; }
                .homeproduct { background: white; padding: 20px; border: 1px solid #ccc; border-radius: 10px; text-align: center; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); margin: 0px; display: inline-block; }
                .homeproduct img { width: 100%; max-width: 300px; height: auto; border-bottom: 1px solid #ccc; margin-bottom: 10px; }
                .homeproduct h3 { font-size: 18px; margin: 10px 0; }
                .homeproduct p { font-size: 16px; color: #333; }
                .homeproduct button { background-color: #ff9900; color: white; border: none; margin: 20px; padding: 10px; border-radius: 5px; cursor: pointer; }
                .homeproduct button:hover { background-color: #e68a00; transform: scale(1.05);}
                .slider-buttons { position: absolute; top: 50%; transform: translateY(-50%); width: 100%; display: flex; justify-content: space-between; }
                .slider-buttons button { background-color: rgba(0, 0, 0, 0.5); color: white; border: none; padding: 45px; cursor: pointer; border-radius: 50%; }
                /* Home products button */
                .homeprobtn{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }
                
                /* workout at home */
                .product-section {
                    text-align: center;
                    padding: 20px;
                    background-color: #fff;
                }

                .product-section h1 {
                    font-size: 24px;
                    margin-bottom: 10px;
                    color: #000;
                }

                .product-section h2 {
                    font-size: 20px;
                    margin-bottom: 20px;
                    color: #333;
                }

                .product-container {
                    display: flex;
                    justify-content: center;
                    gap: 60px;
                    flex-wrap: wrap;
                }

                .product-card {
                    background-color: #e6f8f9;
                    width: 200px;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    padding: 15px;
                    transition: transform 0.3s;
                }

                .product-card:hover {
                    transform: translateY(-10px);
                }

                .product-image {
                    height: 320px;
                    margin-bottom: 15px;
                }

                .product-title {
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 10px;
                    color: #333;
                }

                .shop-now {
                    display: inline-block;
                    background-color: #00aaff;
                    color: #fff;
                    padding: 8px 15px;
                    border-radius: 5px;
                    text-decoration: none;
                    margin-top: 10px;
                    font-size: 14px;
                    font-weight: bold;
                }

                .shop-now:hover {
                    background-color: #0088cc;
                }
                /* build muscles */
                .section {
                    text-align: center;
                    padding: 70px;
                    background-color: #fff;
                }
    
                .section h1, .section h2 {
                    margin: 10px 0;
                }

                .product-cont{
                    display: flex;
                    justify-content: center;
                    flex-wrap: wrap;
                    gap: 90px;
                    margin-top: 20px;
                }

                .product-cards {
                    width: 120px;
                    text-align: center;
                    transition: transform 0.3s;
                }

                .product-cards:hover{
                    transform: translateY(-10px);
                }
                
                .circle-image {
                    width: 200px;
                    height: 200px;
                    border-radius: 50%;
                    overflow: hidden;
                    border: 5px solid #6be3e0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }

                .circle-image img {
                    width: 290px;
                    height: 290px;
                    object-fit: cover;
                }

                .product-title {
                    margin-top: 10px;
                    font-size: 18px;
                    font-weight: bold;
                }

                .divider{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    width: 90vw;
                }
                /* Yoga section products */
                .yoga-section {
                    text-align: center;
                    padding: 20px;
                    background-color: #fff;
                }

                .yoga-section h1 {
                    margin: 10px 0;
                    font-size: 20px;
                    color: #333;
                }

                .yoga-product-container {
                    display: flex;
                    justify-content: center;
                    flex-wrap: wrap;
                    gap: 70px;
                    margin-top: 20px;
                }

                .yoga-product-card {
                    width: 305px;
                    text-align: center;
                    border-radius: 10px;
                    overflow: hidden;
                    background-color: #fff;
                    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                    transition: transform 0.3s ease, box-shadow 0.3s ease;
                }

                .yoga-product-card:hover {
                    transform: scale(1.05);
                    box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.15);
                }

                .yoga-product-image {
                    width: 100%;
                    height: 341px;
                    object-fit: cover;
                }
                /* Cards Section Styling */
                .cards-section {
                    padding: 20px;
                    background-color: white;
                    margin: 20px 0;
                }
                
                .cards-container {
                    display: grid;
                    grid-template-columns: 1fr 1fr 1fr;
                    gap: 70px;
                    padding: 0 11%;
                }
                .card {
                    background: #fff;
                    border-radius: 12px;
                    box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
                    overflow: hidden;
                    transition: transform 0.3s ease, box-shadow 0.3s ease;
                }
                .card:hover {
                    transform: translateY(-5px);
                    box-shadow: 0px 15px 25px rgba(0, 0, 0, 0.2);
                }
                .card img {
                    width: 350px;
                    height: 300px;
                    object-fit: cover;
                    border-bottom: 3px solid #ddd;
                }
                .card-content {
                    padding: 15px;
                    text-align: center;
                }
                
                .card-content h3 {
                    font-size: 20px;
                    font-weight: bold;
                    margin: 10px 0;
                    color: #333;
                }
                
                .card-content p {
                    font-size: 14px;
                    color: #555;
                    margin: 10px 0;
                }
                .card-content a {
                    display: inline-block;
                    margin-top: 10px;
                    padding: 10px 20px;
                    background-color: #007bff;
                    color: white;
                    text-decoration: none;
                    font-size: 14px;
                    border-radius: 20px;
                    transition: background-color 0.3s ease, transform 0.3s ease;
                }
                .card-content a:hover {
                    background-color: #0056b3;
                    transform: scale(1.05);
                }
                .study_logos{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    flex-wrap: wrap;
                    width: 61vw;
                    margin: 20px auto;
                }
                .fitness-destination {
                    padding: 40px 10%;
                    background-color: #f7f7f7;
                    margin-top: 40px;
                    margin-bottom: 60px;
                    border-radius: 15px;
                    box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
                }
                
                .fitness-content {
                    text-align: left;
                    font-family: Arial, sans-serif;
                    color: #333;
                    line-height: 1.6;
                }
                
                .fitness-title {
                    font-size: 28px;
                    font-weight: bold;
                    margin-bottom: 20px;
                    text-align: center;
                    color: #007bff;
                }
                
                .fitness-category {
                    margin: 20px 0;
                }
                
                .fitness-category h3 {
                    font-size: 22px;
                    font-weight: bold;
                    margin-bottom: 10px;
                    color: #ff9900;
                }
                
                .fitness-category p {
                    margin: 0;
                    font-size: 16px;
                }

                .customreview-section{
                    padding: 30px;
                    margin: 20px auto;
                    width: 85vw;
                }
                
                .customer_rev{
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                }
                .cta {
                    margin-top: 30px;
                    font-size: 18px;
                    font-weight: bold;
                    text-align: center;
                    color: #0056b3;
                }
                .back-to-top {
                  text-align: center;
                }
                .back-to-top button {
                  background-color: #333;
                  color: white;
                  border: none;
                  padding: 12px 20px;
                  font-size: 16px;
                  border-radius: 25px;
                  cursor: pointer;
                  transition: all 0.3s ease-in-out;
                  box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
                } 
                .back-to-top button:hover {
                   background-color: #555;
                   transform: scale(1.05);
                }
                footer {
                    background-color: #232f3e;
                    color: white;
                    padding: 30px;
                    font-family: Arial, sans-serif;
                }
                footer { background-color: #333; color: white; text-align: center; padding: 80px; margin-top: 50px;}
                .footer-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                    gap: 20px;
                    margin-bottom: 20px;
                }

                .footer-grid h3 {
                    font-size: 25px;
                    margin-bottom: 5px;
                    border-bottom: 1px solid #3a45533;
                    padding-bottom: 5px;
                }

                .footer-grid ul {
                    list-style: none;
                    padding: 0;
                }

                .footer-grid ul li {
                    margin: 5px 0;
                }

                .footer-grid ul li a {
                    color: #ddd;
                    text-decoration: none;
                    font-size: 19px;
                    line-height: 40px;
                }

                .footer-grid ul li a:hover {
                    color: white;
                    text-decoration: underline;
                }

                .footer-bottom {
                    text-align: center;
                    border-top: 1px solid #3a4553;
                    padding-top: 5px;
                    font-size: 20px;
                    line-height: 80px;
                    width: 88vw;
                }
                .footer-bottom svg{
                    margin: -5px;
                    width: 50px;
                }
                .breakline{
                    margin: 8px -4px 24px;
                    width: 100%;
                }
                .userface{
                    fill: rgba(236, 232, 232, 1);
                    height: 120px;
                    width: 207px;
                }
        </style>
        </head>
        <body>
        <header>
            <nav>
                <div class="hamburger-menu" onclick="toggleMenu()">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="50" height="50" color="#ffffff" fill="none">
                    <path d="M2 10H7" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                    <path d="M2 17H7" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                    <path d="M2 3H19" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                    <path d="M19.6 18.6L22 21M20.8 14.4C20.8 11.4176 18.3824 9 15.4 9C12.4176 9 10 11.4176 10 14.4C10 17.3824 12.4176 19.8 15.4 19.8C18.3824 19.8 20.8 17.3824 20.8 14.4Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                </svg>
                </div>
                <div class="menu-box" id="menuBox">
                <button class="close-btn" onclick="toggleMenu()">✖</button>
                <div class="menu-section">
                <svg class = "userface" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(236, 232, 232, 1);transform: ;msFilter:;"><path d="M12 2A10.13 10.13 0 0 0 2 12a10 10 0 0 0 4 7.92V20h.1a9.7 9.7 0 0 0 11.8 0h.1v-.08A10 10 0 0 0 22 12 10.13 10.13 0 0 0 12 2zM8.07 18.93A3 3 0 0 1 11 16.57h2a3 3 0 0 1 2.93 2.36 7.75 7.75 0 0 1-7.86 0zm9.54-1.29A5 5 0 0 0 13 14.57h-2a5 5 0 0 0-4.61 3.07A8 8 0 0 1 4 12a8.1 8.1 0 0 1 8-8 8.1 8.1 0 0 1 8 8 8 8 0 0 1-2.39 5.64z"></path><path d="M12 6a3.91 3.91 0 0 0-4 4 3.91 3.91 0 0 0 4 4 3.91 3.91 0 0 0 4-4 3.91 3.91 0 0 0-4-4zm0 6a1.91 1.91 0 0 1-2-2 1.91 1.91 0 0 1 2-2 1.91 1.91 0 0 1 2 2 1.91 1.91 0 0 1-2 2z"></path></svg>
                <div class="user_logo"><a href = "/login">Hello User!!</a></div>    
                    <h1><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffffff" fill="none">
                        <path d="M3.16405 11.3497L4 11.5587L4.45686 16.1005C4.715 18.6668 4.84407 19.9499 5.701 20.7249C6.55793 21.5 7.84753 21.5 10.4267 21.5H13.5733C16.1525 21.5 17.4421 21.5 18.299 20.7249C19.1559 19.9499 19.285 18.6668 19.5431 16.1005L20 11.5587L20.836 11.3497C21.5201 11.1787 22 10.564 22 9.85882C22 9.35735 21.7553 8.88742 21.3445 8.59985L13.1469 2.86154C12.4583 2.37949 11.5417 2.37949 10.8531 2.86154L2.65549 8.59985C2.24467 8.88742 2 9.35735 2 9.85882C2 10.564 2.47993 11.1787 3.16405 11.3497Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                        <path d="M15 16C14.2005 16.6224 13.1502 17 12 17C10.8498 17 9.79952 16.6224 9 16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                    </svg></h1>
                    <br>
                    <a href="/">Home</a>
                </div>
                <hr class="breakline">
                <div class="menu-section">
                    <h3><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffffff" fill="none">
                        <path d="M16 23V4L4 7.5L3 20.5L16 23Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                        <path d="M17.5 5.14833L16 4V23L21 21.5C21 18.8371 20.7998 16.178 20.4012 13.5451L19.1298 5.14833H17.5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                        <path d="M13.0016 4.87502C13.0092 2.85785 12.239 1.26304 11.0023 1.02911C9.44084 0.73373 7.72699 2.71982 7.17435 5.46517C7.09535 5.85761 7.04435 6.24433 7.01953 6.61979" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                        <path d="M14.8665 4.33083C14.5732 3.14854 13.9527 2.31296 13.1092 2.14837C11.7258 1.8784 10.2195 3.50662 9.55469 5.8801" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                        <path d="M12.7896 9.42437C11.7896 9.0035 9.19076 8.24627 8.50372 10.266C8.1332 11.3553 8.79795 12.5183 10.2171 13.6331C12.2041 15.1939 11.867 16.524 11.5033 17.0001C10.2176 18.6837 7.64621 17.7016 6.78906 17.0001" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                    </svg></h3>
                    <a href="/products">Fitness & Sports Products</a>
                       <div class="dropdown-menu">
                       <a href="/products?category=fitness-accessories">Fitness Accessories</a>
                       <a href="/products?category=gym-equipment">Gym Equipments</a>
                       <a href="/products?category=sports-collection">Sports Collection</a>
                       <a href="/products?category=sports-wear">Sports Wear</a>
                       <a href="/products?category=sports-accessories">Sports Accessories</a>
                    </div>
                </div>
                <hr class="breakline">
                <div class="menu-section">
                    <h3><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffffff" fill="none">
                        <path d="M4 10C4 6.22876 4 4.34315 5.17157 3.17157C6.34315 2 8.22876 2 12 2H13.5C17.2712 2 19.1569 2 20.3284 3.17157C21.5 4.34315 21.5 6.22876 21.5 10V14C21.5 17.7712 21.5 19.6569 20.3284 20.8284C19.1569 22 17.2712 22 13.5 22H12C8.22876 22 6.34315 22 5.17157 20.8284C4 19.6569 4 17.7712 4 14V10Z" stroke="currentColor" stroke-width="1.5" />
                        <path d="M9.79993 11.9741C9.37332 11.2302 9.16733 10.6228 9.04313 10.007C8.85943 9.09641 9.27981 8.20686 9.97622 7.63926C10.2706 7.39937 10.608 7.48133 10.782 7.79358L11.1749 8.49851C11.4864 9.05725 11.6421 9.33663 11.6112 9.63282C11.5803 9.929 11.3703 10.1702 10.9503 10.6527L9.79993 11.9741ZM9.79993 11.9741C10.6634 13.4797 12.0185 14.8356 13.5259 15.7001M13.5259 15.7001C14.2698 16.1267 14.8772 16.3327 15.493 16.4569C16.4036 16.6406 17.2931 16.2202 17.8607 15.5238C18.1006 15.2294 18.0187 14.892 17.7064 14.718L17.0015 14.3251C16.4427 14.0136 16.1634 13.8579 15.8672 13.8888C15.571 13.9197 15.3298 14.1297 14.8473 14.5497L13.5259 15.7001Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" />
                        <path d="M5 6L2.5 6M5 12L2.5 12M5 18H2.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                    </svg></h3>
                    <a href="/contact">Contact</a>
                <hr class="breakline">
                </div>
                </div>
                </nav>
                <h1 class = "logo"><a href= "/" style="text-decoration: none; color: #ff9800;">SportsFit</a></h1>
            <div class="search-bar">
                <form method="get" action="/search" style="display: flex; align-items: center; width: 100%;">
                    <input type="text" name="query" id="searchInput" placeholder="Search for products..." required>
                    <button type="submit" class="search-btn">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                            <path d="M10 18a7.952 7.952 0 0 0 4.897-1.688l4.396 4.396 1.414-1.414-4.396-4.396A7.952 7.952 0 0 0 18 10c0-4.411-3.589-8-8-8s-8 3.589-8 8 3.589 8 8 8zm0-14c3.309 0 6 2.691 6 6s-2.691 6-6 6-6-2.691-6-6 2.691-6 6-6z"></path>
                        </svg>
                    </button>
                </form>
            </div>
            <div class="icon">
                <a href="/wishlist"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(241, 234, 234, 1);">
                    <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
                </svg></a>
                <a href="/cart"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(241, 234, 234, 1);">
                    <circle cx="10.5" cy="19.5" r="1.5"></circle>
                    <circle cx="17.5" cy="19.5" r="1.5"></circle>
                    <path d="M21 7H7.334L6.18 4.23A1.995 1.995 0 0 0 4.333 3H2v2h2.334l4.743 11.385c.155.372.52.615.923.615h8c.417 0 .79-.259.937-.648l3-8A1.003 1.003 0 0 0 21 7zm-4 6h-2v2h-2v-2h-2v-2h2V9h2v2h2v2z"></path>
                </svg></a>
                <a href="/login"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(241, 234, 234, 1);">
                    <path d="M12 2a5 5 0 1 0 5 5 5 5 0 0 0-5-5zm0 8a3 3 0 1 1 3-3 3 3 0 0 1-3 3zm9 11v-1a7 7 0 0 0-7-7h-4a7 7 0 0 0-7 7v1h2v-1a5 5 0 0 1 5-5h4a5 5 0 0 1 5 5v1z"></path>
                </svg></a>
            </div>
            </header> 
            <div class="background-slider-container">
                <div class="background-slider">  
                    <div class="background-slide" style="background-image: url('https://images-eu.ssl-images-amazon.com/images/G/31/Sports/EnFRevmap/COMBO-OFFERS.jpg');"></div>
                    <div class="background-slide" style="background-image: url('https://images-eu.ssl-images-amazon.com/images/G/31/Sports/EnFRevmap/Curatedstores/Cycling-store.jpg');"></div>
                    <div class="background-slide" style="background-image: url('https://images-eu.ssl-images-amazon.com/images/G/31/Sports/EnFRevmap/Curatedstores/fintness.jpg');"></div>
                    <div class="background-slide" style="background-image: url('https://images-eu.ssl-images-amazon.com/images/G/31/Sports/EnFRevmap/Curatedstores/Home-gym.jpg');"></div>
                </div>
                <div class="slider-dots">
                    <span class="dot active" data-slide="0"></span>
                    <span class="dot" data-slide="1"></span>
                    <span class="dot" data-slide="2"></span>
                    <span class="dot" data-slide="3"></span>
                </div>
            </div>
            <div class = "title">
                <h1>Welcome to SportsFit</h1>
                <p>Your one-stop shop for sports and fitness needs!</p>
            </div> 
            <div class="slider">
                <div class="slides">
                    <div class="slide">
                        <div class="homeproduct">
                            <img src="https://m.media-amazon.com/images/I/71f3BmjCwtL._AC_UY1000_.jpg" alt="Running Shoes">
                            <h3>Running Shoes</h3>
                            <p>Price: Rs. 999</p>
                            <br>
                            <a class = "prodetails" href="/product?id=running-shoes"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffff" fill="none">
                                <path d="M8.9835 1.99998C6.17689 2.06393 4.53758 2.33109 3.41752 3.44727C2.43723 4.42416 2.10954 5.79742 2 7.99998M15.0165 1.99998C17.8231 2.06393 19.4624 2.33109 20.5825 3.44727C21.5628 4.42416 21.8905 5.79742 22 7.99998M15.0165 22C17.8231 21.9361 19.4624 21.6689 20.5825 20.5527C21.5628 19.5758 21.8905 18.2026 22 16M8.9835 22C6.17689 21.9361 4.53758 21.6689 3.41752 20.5527C2.43723 19.5758 2.10954 18.2026 2 16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                <path d="M15 15L17 17M16 11.5C16 9.01468 13.9853 6.99998 11.5 6.99998C9.01469 6.99998 7 9.01468 7 11.5C7 13.9853 9.01469 16 11.5 16C13.9853 16 16 13.9853 16 11.5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                            </svg></a> 
                            <br>
                            <div class= "homeprobtn">
                              <button onclick="addTohomeCart('Running Shoes', 999, 'High-performance running shoes for athletes.', 'https://m.media-amazon.com/images/I/71f3BmjCwtL._AC_UY1000_.jpg')">
                              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffffff" fill="none">
                                <path d="M8 16H15.2632C19.7508 16 20.4333 13.1808 21.261 9.06908C21.4998 7.88311 21.6192 7.29013 21.3321 6.89507C21.045 6.5 20.4947 6.5 19.3941 6.5H19M6 6.5H7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                                <path d="M10.5 7C10.5 7 11.5 7 12.5 9C12.5 9 15.6765 4 18.5 3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                <path d="M8 16L5.37873 3.51493C5.15615 2.62459 4.35618 2 3.43845 2H2.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                                <path d="M8.88 16H8.46857C7.10522 16 6 17.1513 6 18.5714C6 18.8081 6.1842 19 6.41143 19H17.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                <circle cx="10.5" cy="20.5" r="1.5" stroke="currentColor" stroke-width="1.5" />
                                <circle cx="17.5" cy="20.5" r="1.5" stroke="currentColor" stroke-width="1.5" />
                              </svg></button>  
                              <form method="post" action="/wishlist/add">
                                <input type="hidden" name="item" value="Running Shoes">
                                <input type="hidden" name="price" value="999">
                                <input type="hidden" name="imageUrl" value="https://m.media-amazon.com/images/I/71f3BmjCwtL._AC_UY1000_.jpg">
                               <button><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffffff" fill="none">
                                    <path d="M12 21C10.6588 21 9.88572 20.4278 8.33953 19.2834C0.221721 13.2749 1.01807 6.15294 4.53744 3.99415C7.21909 2.34923 9.55962 3.01211 10.9656 4.06801C11.5422 4.50096 11.8304 4.71743 12 4.71743C12.1696 4.71743 12.4578 4.50096 13.0344 4.06801C14.4404 3.01211 16.7809 2.34923 19.4626 3.99415C21.1812 5.04838 22.2505 7.28623 21.9494 10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                                    <path d="M14 18C14 18 15 18 16 20C16 20 19.1765 15 22 14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                               </svg></button>
                              </form>
                            </div> 
                        </div>
                    </div>
                    <div class="slide">
                        <div class="homeproduct">
                            <img src="https://www.ukgymequipment.com/images/2-5-50kg-premium-urethane-dumbbell-set-p5790-75425_image.jpg" alt="Adjustable Dumbbells">
                            <h3>Adjustable Dumbbells</h3>
                            <p>Price: Rs. 1,500</p>
                            <br>
                            <a class = "prodetails" href="/product?id=adjustable-dumbbells"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffff" fill="none">
                                <path d="M8.9835 1.99998C6.17689 2.06393 4.53758 2.33109 3.41752 3.44727C2.43723 4.42416 2.10954 5.79742 2 7.99998M15.0165 1.99998C17.8231 2.06393 19.4624 2.33109 20.5825 3.44727C21.5628 4.42416 21.8905 5.79742 22 7.99998M15.0165 22C17.8231 21.9361 19.4624 21.6689 20.5825 20.5527C21.5628 19.5758 21.8905 18.2026 22 16M8.9835 22C6.17689 21.9361 4.53758 21.6689 3.41752 20.5527C2.43723 19.5758 2.10954 18.2026 2 16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                <path d="M15 15L17 17M16 11.5C16 9.01468 13.9853 6.99998 11.5 6.99998C9.01469 6.99998 7 9.01468 7 11.5C7 13.9853 9.01469 16 11.5 16C13.9853 16 16 13.9853 16 11.5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                            </svg></a>
                            <br>
                            <div class= "homeprobtn">
                                <button onclick="addTohomeCart('Adjustable Dumbbells',  1500, 'Adjustable dumbbells for versatile workouts.', 'https://www.ukgymequipment.com/images/2-5-50kg-premium-urethane-dumbbell-set-p5790-75425_image.jpg')">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffffff" fill="none">
                                    <path d="M8 16H15.2632C19.7508 16 20.4333 13.1808 21.261 9.06908C21.4998 7.88311 21.6192 7.29013 21.3321 6.89507C21.045 6.5 20.4947 6.5 19.3941 6.5H19M6 6.5H7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                                    <path d="M10.5 7C10.5 7 11.5 7 12.5 9C12.5 9 15.6765 4 18.5 3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                    <path d="M8 16L5.37873 3.51493C5.15615 2.62459 4.35618 2 3.43845 2H2.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                                    <path d="M8.88 16H8.46857C7.10522 16 6 17.1513 6 18.5714C6 18.8081 6.1842 19 6.41143 19H17.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                    <circle cx="10.5" cy="20.5" r="1.5" stroke="currentColor" stroke-width="1.5" />
                                    <circle cx="17.5" cy="20.5" r="1.5" stroke="currentColor" stroke-width="1.5" />
                                </svg></button>
                                <form method="post" action="/wishlist/add">
                                    <input type="hidden" name="item" value="Adjustable Dumbbells">
                                    <input type="hidden" name="price" value="1500">
                                    <input type="hidden" name="imageUrl" value="https://www.ukgymequipment.com/images/2-5-50kg-premium-urethane-dumbbell-set-p5790-75425_image.jpg">
                                <button><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffffff" fill="none">
                                    <path d="M12 21C10.6588 21 9.88572 20.4278 8.33953 19.2834C0.221721 13.2749 1.01807 6.15294 4.53744 3.99415C7.21909 2.34923 9.55962 3.01211 10.9656 4.06801C11.5422 4.50096 11.8304 4.71743 12 4.71743C12.1696 4.71743 12.4578 4.50096 13.0344 4.06801C14.4404 3.01211 16.7809 2.34923 19.4626 3.99415C21.1812 5.04838 22.2505 7.28623 21.9494 10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                                    <path d="M14 18C14 18 15 18 16 20C16 20 19.1765 15 22 14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                               </svg></button>
                                </form>
                            </div>    
                        </div>
                    </div>
                    <div class="slide">
                        <div class="homeproduct">
                            <img src="https://bicyclewarehouse.com/cdn/shop/products/giant-fathom-1-27-5-mountain-bike-2022-28685815382118.jpg" alt="Mountain Bike">
                            <h3>Mountain Bike</h3>
                            <p>Price: Rs. 2,500</p>
                            <br>
                            <a class = "prodetails" href="/product?id=mountain-bike"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffff" fill="none">
                                <path d="M8.9835 1.99998C6.17689 2.06393 4.53758 2.33109 3.41752 3.44727C2.43723 4.42416 2.10954 5.79742 2 7.99998M15.0165 1.99998C17.8231 2.06393 19.4624 2.33109 20.5825 3.44727C21.5628 4.42416 21.8905 5.79742 22 7.99998M15.0165 22C17.8231 21.9361 19.4624 21.6689 20.5825 20.5527C21.5628 19.5758 21.8905 18.2026 22 16M8.9835 22C6.17689 21.9361 4.53758 21.6689 3.41752 20.5527C2.43723 19.5758 2.10954 18.2026 2 16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                <path d="M15 15L17 17M16 11.5C16 9.01468 13.9853 6.99998 11.5 6.99998C9.01469 6.99998 7 9.01468 7 11.5C7 13.9853 9.01469 16 11.5 16C13.9853 16 16 13.9853 16 11.5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                            </svg></a>
                            <br>
                            <div class= "homeprobtn">
                                <button onclick="addTohomeCart('Mountain Bike', 2500, '"High-performance, Compact design bike for athletes.', 'https://bicyclewarehouse.com/cdn/shop/products/giant-fathom-1-27-5-mountain-bike-2022-28685815382118.jpg')">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffffff" fill="none">
                                    <path d="M8 16H15.2632C19.7508 16 20.4333 13.1808 21.261 9.06908C21.4998 7.88311 21.6192 7.29013 21.3321 6.89507C21.045 6.5 20.4947 6.5 19.3941 6.5H19M6 6.5H7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                                    <path d="M10.5 7C10.5 7 11.5 7 12.5 9C12.5 9 15.6765 4 18.5 3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                    <path d="M8 16L5.37873 3.51493C5.15615 2.62459 4.35618 2 3.43845 2H2.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                                    <path d="M8.88 16H8.46857C7.10522 16 6 17.1513 6 18.5714C6 18.8081 6.1842 19 6.41143 19H17.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                    <circle cx="10.5" cy="20.5" r="1.5" stroke="currentColor" stroke-width="1.5" />
                                    <circle cx="17.5" cy="20.5" r="1.5" stroke="currentColor" stroke-width="1.5" />
                                </svg></button>
                                <form method="post" action="/wishlist/add">
                                    <input type="hidden" name="item" value="Mountain Bike">
                                    <input type="hidden" name="price" value="2500">
                                    <input type="hidden" name="imageUrl" value="https://bicyclewarehouse.com/cdn/shop/products/giant-fathom-1-27-5-mountain-bike-2022-28685815382118.jpg">
                                <button><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffffff" fill="none">
                                    <path d="M12 21C10.6588 21 9.88572 20.4278 8.33953 19.2834C0.221721 13.2749 1.01807 6.15294 4.53744 3.99415C7.21909 2.34923 9.55962 3.01211 10.9656 4.06801C11.5422 4.50096 11.8304 4.71743 12 4.71743C12.1696 4.71743 12.4578 4.50096 13.0344 4.06801C14.4404 3.01211 16.7809 2.34923 19.4626 3.99415C21.1812 5.04838 22.2505 7.28623 21.9494 10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                                    <path d="M14 18C14 18 15 18 16 20C16 20 19.1765 15 22 14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                               </svg></button>
                                </form>
                            </div>    
                        </div>
                    </div>
                    <div class="slide">
                        <div class="homeproduct">
                            <img src="https://www.powermaxfitness.net/uploads/thumb/800_600_1657091228_product_06072022123708.jpg" alt="Treadmill">
                            <h3>Treadmill</h3>
                            <p>Price: Rs. 20000</p>
                            <br>
                            <a class = "prodetails" href="/product?id=treadmill"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffff" fill="none">
                                <path d="M8.9835 1.99998C6.17689 2.06393 4.53758 2.33109 3.41752 3.44727C2.43723 4.42416 2.10954 5.79742 2 7.99998M15.0165 1.99998C17.8231 2.06393 19.4624 2.33109 20.5825 3.44727C21.5628 4.42416 21.8905 5.79742 22 7.99998M15.0165 22C17.8231 21.9361 19.4624 21.6689 20.5825 20.5527C21.5628 19.5758 21.8905 18.2026 22 16M8.9835 22C6.17689 21.9361 4.53758 21.6689 3.41752 20.5527C2.43723 19.5758 2.10954 18.2026 2 16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                <path d="M15 15L17 17M16 11.5C16 9.01468 13.9853 6.99998 11.5 6.99998C9.01469 6.99998 7 9.01468 7 11.5C7 13.9853 9.01469 16 11.5 16C13.9853 16 16 13.9853 16 11.5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                            </svg></a>
                            <br>
                            <div class= "homeprobtn">
                                <button onclick="addTohomeCart('Treadmill', 20000, 'Treadmill for versatile workouts.', 'https://www.powermaxfitness.net/uploads/thumb/800_600_1657091228_product_06072022123708.jpg')">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffffff" fill="none">
                                    <path d="M8 16H15.2632C19.7508 16 20.4333 13.1808 21.261 9.06908C21.4998 7.88311 21.6192 7.29013 21.3321 6.89507C21.045 6.5 20.4947 6.5 19.3941 6.5H19M6 6.5H7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                                    <path d="M10.5 7C10.5 7 11.5 7 12.5 9C12.5 9 15.6765 4 18.5 3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                    <path d="M8 16L5.37873 3.51493C5.15615 2.62459 4.35618 2 3.43845 2H2.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                                    <path d="M8.88 16H8.46857C7.10522 16 6 17.1513 6 18.5714C6 18.8081 6.1842 19 6.41143 19H17.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                    <circle cx="10.5" cy="20.5" r="1.5" stroke="currentColor" stroke-width="1.5" />
                                    <circle cx="17.5" cy="20.5" r="1.5" stroke="currentColor" stroke-width="1.5" />
                                </svg></button>
                                <form method="post" action="/wishlist/add">
                                    <input type="hidden" name="item" value="Treadmill">
                                    <input type="hidden" name="price" value="20000">
                                    <input type="hidden" name="imageUrl" value="https://www.powermaxfitness.net/uploads/thumb/800_600_1657091228_product_06072022123708.jpg">
                                <button><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffffff" fill="none">
                                    <path d="M12 21C10.6588 21 9.88572 20.4278 8.33953 19.2834C0.221721 13.2749 1.01807 6.15294 4.53744 3.99415C7.21909 2.34923 9.55962 3.01211 10.9656 4.06801C11.5422 4.50096 11.8304 4.71743 12 4.71743C12.1696 4.71743 12.4578 4.50096 13.0344 4.06801C14.4404 3.01211 16.7809 2.34923 19.4626 3.99415C21.1812 5.04838 22.2505 7.28623 21.9494 10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                                    <path d="M14 18C14 18 15 18 16 20C16 20 19.1765 15 22 14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                </svg></button>
                                </form>
                            </div>    
                        </div>
                    </div>
                    <div class="slide">
                        <div class="homeproduct">
                            <img src="https://www.bigbasket.com/media/uploads/p/xl/40122051_8-ritebite-max-protein-daily-choco-almond-bar.jpg" alt="Protein Bar">
                            <h3>Protein Bar</h3>
                            <p>Price: Rs. 800</p>
                            <br>
                            <a class = "prodetails" href="/product?id=protein-bar"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffff" fill="none">
                                <path d="M8.9835 1.99998C6.17689 2.06393 4.53758 2.33109 3.41752 3.44727C2.43723 4.42416 2.10954 5.79742 2 7.99998M15.0165 1.99998C17.8231 2.06393 19.4624 2.33109 20.5825 3.44727C21.5628 4.42416 21.8905 5.79742 22 7.99998M15.0165 22C17.8231 21.9361 19.4624 21.6689 20.5825 20.5527C21.5628 19.5758 21.8905 18.2026 22 16M8.9835 22C6.17689 21.9361 4.53758 21.6689 3.41752 20.5527C2.43723 19.5758 2.10954 18.2026 2 16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                <path d="M15 15L17 17M16 11.5C16 9.01468 13.9853 6.99998 11.5 6.99998C9.01469 6.99998 7 9.01468 7 11.5C7 13.9853 9.01469 16 11.5 16C13.9853 16 16 13.9853 16 11.5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                            </svg></a>  
                            <br>
                            <div class= "homeprobtn">
                                <button onclick="addTohomeCart('Protein Bar', 800, 'Tasty Protein Bar.', 'https://www.bigbasket.com/media/uploads/p/xl/40122051_8-ritebite-max-protein-daily-choco-almond-bar.jpg')"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffffff" fill="none">
                                    <path d="M8 16H15.2632C19.7508 16 20.4333 13.1808 21.261 9.06908C21.4998 7.88311 21.6192 7.29013 21.3321 6.89507C21.045 6.5 20.4947 6.5 19.3941 6.5H19M6 6.5H7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                                    <path d="M10.5 7C10.5 7 11.5 7 12.5 9C12.5 9 15.6765 4 18.5 3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                    <path d="M8 16L5.37873 3.51493C5.15615 2.62459 4.35618 2 3.43845 2H2.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                                    <path d="M8.88 16H8.46857C7.10522 16 6 17.1513 6 18.5714C6 18.8081 6.1842 19 6.41143 19H17.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                    <circle cx="10.5" cy="20.5" r="1.5" stroke="currentColor" stroke-width="1.5" />
                                    <circle cx="17.5" cy="20.5" r="1.5" stroke="currentColor" stroke-width="1.5" />
                                </svg></button>
                                <form method="post" action="/wishlist/add">
                                    <input type="hidden" name="item" value="Protein Bar">
                                    <input type="hidden" name="price" value="800">
                                    <input type="hidden" name="imageUrl" value="https://www.bigbasket.com/media/uploads/p/xl/40122051_8-ritebite-max-protein-daily-choco-almond-bar.jpg">
                                <button><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffffff" fill="none">
                                    <path d="M12 21C10.6588 21 9.88572 20.4278 8.33953 19.2834C0.221721 13.2749 1.01807 6.15294 4.53744 3.99415C7.21909 2.34923 9.55962 3.01211 10.9656 4.06801C11.5422 4.50096 11.8304 4.71743 12 4.71743C12.1696 4.71743 12.4578 4.50096 13.0344 4.06801C14.4404 3.01211 16.7809 2.34923 19.4626 3.99415C21.1812 5.04838 22.2505 7.28623 21.9494 10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                                    <path d="M14 18C14 18 15 18 16 20C16 20 19.1765 15 22 14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                </svg></button>
                                </form>
                            </div>    
                        </div>
                    </div>
                    <div class="slide">
                        <div class="homeproduct">
                            <img src="https://m.media-amazon.com/images/I/61U5D3Cm0OL._AC_UF894,1000_QL80_.jpg" alt="Cricket">
                            <h3>Cricket Set</h3>
                            <p>Price: Rs. 1000</p>
                            <br>
                            <a class = "prodetails" href="/product?id=cricket-set"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffff" fill="none">
                                <path d="M8.9835 1.99998C6.17689 2.06393 4.53758 2.33109 3.41752 3.44727C2.43723 4.42416 2.10954 5.79742 2 7.99998M15.0165 1.99998C17.8231 2.06393 19.4624 2.33109 20.5825 3.44727C21.5628 4.42416 21.8905 5.79742 22 7.99998M15.0165 22C17.8231 21.9361 19.4624 21.6689 20.5825 20.5527C21.5628 19.5758 21.8905 18.2026 22 16M8.9835 22C6.17689 21.9361 4.53758 21.6689 3.41752 20.5527C2.43723 19.5758 2.10954 18.2026 2 16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                <path d="M15 15L17 17M16 11.5C16 9.01468 13.9853 6.99998 11.5 6.99998C9.01469 6.99998 7 9.01468 7 11.5C7 13.9853 9.01469 16 11.5 16C13.9853 16 16 13.9853 16 11.5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                            </svg></a> 
                            <br>
                            <div class= "homeprobtn">
                                <button onclick="addTohomeCart('Cricket Set', 1000, 'This is a Cricket Set  product.', 'https://m.media-amazon.com/images/I/61U5D3Cm0OL._AC_UF894,1000_QL80_.jpg')"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffffff" fill="none">
                                    <path d="M8 16H15.2632C19.7508 16 20.4333 13.1808 21.261 9.06908C21.4998 7.88311 21.6192 7.29013 21.3321 6.89507C21.045 6.5 20.4947 6.5 19.3941 6.5H19M6 6.5H7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                                    <path d="M10.5 7C10.5 7 11.5 7 12.5 9C12.5 9 15.6765 4 18.5 3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                    <path d="M8 16L5.37873 3.51493C5.15615 2.62459 4.35618 2 3.43845 2H2.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                                    <path d="M8.88 16H8.46857C7.10522 16 6 17.1513 6 18.5714C6 18.8081 6.1842 19 6.41143 19H17.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                    <circle cx="10.5" cy="20.5" r="1.5" stroke="currentColor" stroke-width="1.5" />
                                    <circle cx="17.5" cy="20.5" r="1.5" stroke="currentColor" stroke-width="1.5" />
                                </svg></button>
                                <form method="post" action="/wishlist/add">
                                    <input type="hidden" name="item" value="Cricket Set">
                                    <input type="hidden" name="price" value="1000">
                                    <input type="hidden" name="imageUrl"  value="https://m.media-amazon.com/images/I/61U5D3Cm0OL._AC_UF894,1000_QL80_.jpg">
                                <button><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffffff" fill="none">
                                    <path d="M12 21C10.6588 21 9.88572 20.4278 8.33953 19.2834C0.221721 13.2749 1.01807 6.15294 4.53744 3.99415C7.21909 2.34923 9.55962 3.01211 10.9656 4.06801C11.5422 4.50096 11.8304 4.71743 12 4.71743C12.1696 4.71743 12.4578 4.50096 13.0344 4.06801C14.4404 3.01211 16.7809 2.34923 19.4626 3.99415C21.1812 5.04838 22.2505 7.28623 21.9494 10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                                    <path d="M14 18C14 18 15 18 16 20C16 20 19.1765 15 22 14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                                </svg></button>
                                </form>
                            </div>    
                        </div>
                    </div>
                </div>
                <div class="slider-buttons">
                    <button onclick="prevSlide()">&#10094;</button>
                    <button onclick="nextSlide()">&#10095;</button>
                </div>
            </div>
            <!-- workout home -->
            <div class="product-section">
                <img src="https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Stripe_WAH.jpg" alt="header1">
                <img src="https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Getlean/PC/Header.jpg" alt="header2">

                <div class="product-container">
                    <!-- Product Card 1 -->
                    <div class="product-card">
                        <img src="https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Getlean/PC/1_Cardio_Kiosk.jpg" alt="Cross Trainers" class="product-image">
                        <div class="product-title">CROSS TRAINERS</div>
                        <a href="/products?category=gym-equipment" class="shop-now">Shop now</a>
                    </div>

                    <!-- Product Card 2 -->
                    <div class="product-card">
                        <img src="https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Getlean/PC/2_Cardio_Kiosk.jpg" alt="Treadmills" class="product-image">
                        <div class="product-title">TREADMILLS</div>
                        <a href="/products?category=gym-equipment" class="shop-now">Shop now</a>
                    </div>

                    <!-- Product Card 3 -->
                    <div class="product-card">
                        <img src="https://m.media-amazon.com/images/G/31/img22/Sports/September/BeatXP/Untitled-2.jpg" alt="Exercise Bikes" class="product-image">
                        <div class="product-title">EXERCISE BIKES</div>
                        <a href="/products?category=gym-equipment" class="shop-now">Shop now</a>
                    </div>

                    <!-- Product Card 4 -->
                    <div class="product-card">
                     <img src="https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Getlean/PC/4_Cardio_Kiosk.jpg" alt="Explore more" class="product-image">
                        <div class="product-title">EXPLORE MORE</div>
                        <a href="/products" class="shop-now">Explore</a>
                    </div>
                </div>
            </div>
            <!-- Build Muscles Section -->
            <div class="section">
                <img src = 'https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Build/PC/Build-Muscles-1500x100.jpg'>
                <div class="product-cont">
                    <!-- Product 1 -->
                    <div class="product-cards">
                        <div class="circle-image">
                        <a href="/products?category=gym-equipment">
                            <img src="https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Build/PC/dumbells.jpg" alt="Dumbbells">
                        </a>
                        </div>
                        <div class="product-title">Dumbbells</div>
                    </div>

                    <!-- Product 2 -->
                    <div class="product-cards">
                        <div class="circle-image">
                        <a href="/products?category=gym-equipment">
                            <img src="https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Build/PC/Gym-Sets.jpg" alt="Gym Sets">
                        </a>
                        </div>
                        <div class="product-title">Gym Sets</div>
                    </div>

                    <!-- Product 3 -->
                    <div class="product-cards">
                        <div class="circle-image">
                        <a href="/products?category=gym-equipment">
                            <img src="https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Build/PC/Hand-Grips.jpg" alt="Hand Grips">
                        </a>
                        </div>
                        <div class="product-title">Hand Grips</div>
                    </div>

                    <!-- Product 4 -->
                    <div class="product-cards">
                        <div class="circle-image">
                        <a href="/products?category=gym-equipment">
                            <img src="https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Build/PC/Explore-more.jpg" alt="Explore More">
                        </a>
                        </div>
                        <div class="product-title">Explore More</div>
                    </div>
                </div>
            </div>
            <!-- Divider -->
            <div class="divider"></div>

            <!-- Home Workout Section -->
            <div class="section">
            <img src = 'https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Equipment/PC/Equipment-for-Home-1500x100.jpg'>
                <div class="product-cont">
                    <!-- Product 1 -->
                    <div class="product-cards">
                        <div class="circle-image">
                        <a href="/products?category=gym-equipment">
                            <img src="https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Equipment/PC/Barbells.jpg" alt="Barbells">
                        </a>
                        </div>
                        <div class="product-title">Barbells</div>
                    </div>

                    <!-- Product 2 -->
                    <div class="product-cards">
                        <div class="circle-image">
                        <a href="/products?category=gym-equipment">
                            <img src="https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Equipment/PC/Tummy-twister.jpg" alt="Tummy Twister">
                        </a>
                        </div>
                        <div class="product-title">Tummy Twister</div>
                    </div>

                    <!-- Product 3 -->
                    <div class="product-cards">
                        <div class="circle-image">
                        <a href="/products?category=gym-equipment">
                            <img src="https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Equipment/PC/Resistance-bands.jpg" alt="Resistance Bands">
                        </a>
                        </div>
                        <div class="product-title">Resistance Bands</div>
                    </div>

                    <!-- Product 4 -->
                    <div class="product-cards">
                        <div class="circle-image">
                        <a href="/products?category=gym-equipment">
                            <img src="https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Equipment/PC/Pull-up-bar.jpg" alt="Pull Up Bar">
                        </a>
                        </div>
                        <div class="product-title">Pull Up Bar</div>
                    </div>

                    <!-- Product 5 -->
                    <div class="product-cards">
                        <div class="circle-image">
                        <a href="/products?category=gym-equipment">
                            <img src="https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Equipment/PC/Skipping-rope.jpg" alt="Skipping Rope">
                        </a>
                        </div>
                        <div class="product-title">Skipping Rope</div>
                    </div>

                    <!-- Product 6 -->
                    <div class="product-cards">
                        <div class="circle-image">
                        <a href="/products?category=gym-equipment">
                            <img src="https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Equipment/PC/Push-up-bar.jpg" alt="Push Up Bar">
                        </a>
                        </div>
                        <div class="product-title">Push Up Bar</div>
                    </div>
                </div>
            </div>
            <!-- yoga products -->
            <div class="yoga-section">
                <img src = 'https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Boosturmind/PC/1500x100.jpg'>
                <div class="yoga-product-container">
                    <!-- Product 1 -->
                    <div class="yoga-product-card">
                    <a href="/products?category=fitness-accessories">
                        <img class="yoga-product-image" src="https://m.media-amazon.com/images/G/31/img22/Sports/October/BAU/2.jpg" alt="Yoga Mat">
                    </a>
                    </div>

                    <!-- Product 2 -->
                    <div class="yoga-product-card">
                    <a href="/products?category=gym-equipment">
                        <img class="yoga-product-image" src="https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Boosturmind/PC/mats.jpg" alt="Medicine Balls">
                    </a>
                    </div>

                    <!-- Product 3 -->
                    <div class="yoga-product-card">
                    <a href="/products?category=gym-equipment">
                        <img class="yoga-product-image" src="https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Boosturmind/PC/Blocks.jpg" alt="Blocks">
                    </a>
                    </div>

                    <!-- Product 4 -->
                    <div class="yoga-product-card">
                    <a href="/products?category=gym-equipment">
                        <img class="yoga-product-image" src="https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Boosturmind/PC/Bands.jpg" alt="Bands">
                    </a>
                    </div>
                </div>
            </div>
            <div class="cards-section">
            <h2 style="text-align: center; margin: 40px 0; font-size: 28px; font-weight: bold; color: #333;">Shop by Category</h2>
            <div class="cards-container">
                <!-- Fitness Accessories -->
                <div class="card">
                    <img src="https://images.meesho.com/images/products/304515040/tprnb_512.webp" alt="Fitness Accessories">
                    <div class="card-content">
                        <h3>Fitness Accessories</h3>
                        <p>Enhance your workouts with top-quality accessories.</p>
                        <a href="products?category=fitness-accessories">Shop Now</a>
                    </div>
                </div>

                <!-- Gym Equipment -->
                <div class="card">
                    <img src="https://m.media-amazon.com/images/I/81B2Y+uQF5L._SX569_.jpg" alt="Gym Equipment">
                    <div class="card-content">
                        <h3>Gym Equipment</h3>
                        <p>Build your dream gym with premium equipment.</p>
                        <a href="/products?category=gym-equipment">Shop Now</a>
                    </div>
                </div>

                <!-- Sports Collection -->
                <div class="card">
                    <img src="https://static.vecteezy.com/system/resources/previews/053/232/116/non_2x/a-man-running-with-a-beard-and-mustache-free-vector.jpg" alt="Sports Collection">
                    <div class="card-content">
                        <h3>Sports Collection</h3>
                        <p>Gear up for your favorite sports with top-notch products.</p>
                        <a href="/products?category=sports-collection">Shop Now</a>
                    </div>
                </div>

                <!-- Sports Wear -->
                <div class="card">
                    <img src="https://m.media-amazon.com/images/I/91Ov-x9d3qL._SX679_.jpg" alt="Sports Wear">
                    <div class="card-content">
                        <h3>Sports Wear</h3>
                        <p>Stay stylish and comfortable during your workouts.</p>
                        <a href="/products?category=sports-wear">Shop Now</a>
                    </div>
                </div>

                <!-- Sports Accessories -->
                <div class="card">
                    <img src="https://m.media-amazon.com/images/I/71l2-gWOnpL._SX569_.jpg" alt="Sports Accessories">
                    <div class="card-content">
                        <h3>Sports Accessories</h3>
                        <p>Find essential accessories for every sport.</p>
                        <a href="/products?category=sports-accessories">Shop Now</a>
                     </div>
                  </div>
                <!-- All Products -->
                <div class="card">
                    <img src="https://www.shutterstock.com/image-photo/young-surprised-strong-fitness-trainer-260nw-2471093951.jpg" alt="Sports Accessories">
                    <div class="card-content">
                        <h3>Exciting Products</h3>
                        <p>Grab Now.</p>
                        <a href="/products">Shop Now</a>
                     </div>
                  </div>
                </div>
            </div>
            <div>
            <span class="study_logos">
            <a href="/products?category=sports-wear">
              <img src = 'https://m.media-amazon.com/images/G/31/img22/Sports/September/Gear-up.jpg'>
              <img src = 'https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Gearup/Revised/Gear-up-section_02.jpg'>
              <img src = 'https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Gearup/Revised/Gear-up-section_03.jpg'>
              <img src = 'https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Gearup/Revised/Gear-up-section_04.jpg'>
              <img src = 'https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Gearup/Revised/Gear-up-section_05.jpg'>
              <img src = 'https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Gearup/Revised/Gear-up-section_06.jpg'>
            </a>
            </span>  
            </div>
       <div class = "customreview-section">
          <h2 style="text-align: center; margin: 40px 0; font-size: 28px; font-weight: bold; color: #333;">Customer Review</h2>
           <div class = "customer_rev">
             <div class = "rev-box"><img style = "height: 250px;" src = 'https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Review/1_Review-MOB.jpg'></div>
             <div class = "rev-box"><img style = "height: 250px;" src = 'https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Review/2_Review-MOB-2.jpg'></div>
             <div class = "rev-box"><img style = "height: 250px;" src = 'https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Review/3_Review-MOB.jpg'></div>
             <div class = "rev-box"><img style = "height: 250px;" src = 'https://m.media-amazon.com/images/G/31/Sports/EnFRevmap/Review/4_Review-MOB.jpg'></div>
           </div>
       </div>
       <div class="fitness-destination">
             <div class="fitness-content">
             <h2 class="fitness-title">One-Stop Fitness Destination: Exercise & Fitness Store for Every Need</h2>
            <p>
              We understand that maintaining an active lifestyle is a journey, and we're here to support you every step of the way.
              Whether you're a fitness enthusiast, a beginner, or somewhere in between, our wide range of products caters to all.
              From <strong>treadmills</strong> to <strong>fitness bikes</strong>, <strong>yoga mats</strong> to <strong>gym equipment</strong>,
              we have everything you need for home workouts tailored to men and women alike.
            </p>
           <hr>
           <div class="fitness-category">
            <h3>Treadmills</h3>
            <p>Discover the convenience of indoor running with our <strong>top-notch treadmills</strong> designed for home use. 
                Whether you're a seasoned marathoner or just starting, our treadmills boost cardio and active lifestyles.
            </p>
         </div>
         <div class="fitness-category">
            <h3>Fitness Bikes</h3>
            <p>Pedal your way to better health with our range of <strong>fitness bikes</strong>, including upright and recumbent options. 
               Enjoy low-impact, joint-friendly workouts while improving endurance and stamina.
            </p>
         </div>
        <div class="fitness-category">
            <h3>Weights & Dumbbells</h3>
            <p>Strengthen and tone your muscles with our versatile <strong>weights and dumbbell sets</strong>. Ideal for bodybuilding, 
               strength training, and overall physical well-being.
            </p>
        </div>
        <div class="fitness-category">
            <h3>Fitness Accessories</h3>
            <p>Enhance your workouts with <strong>fitness accessories</strong>, including resistance bands, foam rollers, gym gloves, 
               exercise mats, and more. Add variety and effectiveness to your routine!
            </p>
        </div>
        <div class="fitness-category">
            <h3>Home Gym Sets</h3>
            <p>Transform any room into your personal gym with <strong>home gym sets</strong>. These packages include comprehensive 
               equipment for targeting various muscle groups.
            </p>
        </div>
        <div class="fitness-category">
            <h3>Multi Gym Trainers</h3>
            <p>Maximize your potential with <strong>multi gym trainers</strong>. These all-in-one machines are perfect for building strength, 
               endurance, and muscle definition.
            </p>
        </div>
        <div class="fitness-category">
            <h3>Yoga Essentials</h3>
            <p>Elevate your yoga practice with our <strong>yoga essentials</strong>, including mats, blocks, wheels, and straps. 
               Improve your balance, flexibility, and peace of mind.
            </p>
        </div>
          <p class="cta">Explore our store today on <strong>SportsFit</strong> and embrace the path to a healthier, more active you!</p>
        </div>
       </div>
            <div class="back-to-top">
              <button onclick="scrollToTop()">Back to Top</button>
            </div>
            <footer>
                <div class="footer-grid">
            <!-- Section: Get to Know Us -->
            <div>
                <h3>Get to Know Us</h3>
                <ul>
                    <li><a href="#">About SportsFit</a></li>
                    <li><a href="#">Careers</a></li>
                    <li><a href="#">Press Releases</a></li>
                    <li><a href="#">SportsFit Science</a></li>
                </ul>
            </div>

            <!-- Section: Connect with Us -->
            <div>
                <h3>Connect with Us</h3>
                <ul>
                    <li><a href="#">Facebook</a></li>
                    <li><a href="#">Twitter</a></li>
                    <li><a href="#">Instagram</a></li>
                </ul>
            </div>

            <!-- Section: Make Money with Us -->
            <div>
                <h3>Make Money with Us</h3>
                <ul>
                    <li><a href="#">Sell on SportsFit</a></li>
                    <li><a href="#">Sell under SportsFit Accelerator</a></li>
                    <li><a href="#">Protect and Build Your Brand</a></li>
                    <li><a href="#">SportsFit Global Selling</a></li>
                    <li><a href="#">Supply to sportsFit</a></li>
                    <li><a href="#">Become an Affiliate</a></li>
                    <li><a href="#">Fulfilment by SportsFit</a></li>
                    <li><a href="#">Advertise Your Products</a></li>
                    <li><a href="#">SportsFit Pay on Merchants</a></li>
                </ul>
            </div>

            <!-- Section: Let Us Help You -->
            <div>
                <h3>Let Us Help You</h3>
                <ul>
                    <li><a href="#">Your Account</a></li>
                    <li><a href="#">Returns Centre</a></li>
                    <li><a href="#">Recalls and Product Safety Alerts</a></li>
                    <li><a href="#">100% Purchase Protection</a></li>
                    <li><a href="#">Help</a></li>
                </ul>
            </div>
        </div>
            <div class="footer-bottom">
             <p><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(245, 236, 236, 1);transform: ;msFilter:;"><path d="M12 2C6.486 2 2 6.486 2 12s4.486 10 10 10 10-4.486 10-10S17.514 2 12 2zm7.931 9h-2.764a14.67 14.67 0 0 0-1.792-6.243A8.013 8.013 0 0 1 19.931 11zM12.53 4.027c1.035 1.364 2.427 3.78 2.627 6.973H9.03c.139-2.596.994-5.028 2.451-6.974.172-.01.344-.026.519-.026.179 0 .354.016.53.027zm-3.842.7C7.704 6.618 7.136 8.762 7.03 11H4.069a8.013 8.013 0 0 1 4.619-6.273zM4.069 13h2.974c.136 2.379.665 4.478 1.556 6.23A8.01 8.01 0 0 1 4.069 13zm7.381 6.973C10.049 18.275 9.222 15.896 9.041 13h6.113c-.208 2.773-1.117 5.196-2.603 6.972-.182.012-.364.028-.551.028-.186 0-.367-.016-.55-.027zm4.011-.772c.955-1.794 1.538-3.901 1.691-6.201h2.778a8.005 8.005 0 0 1-4.469 6.201z"></path></svg>English India</p>
            </div>
            <p style = "line-height: 44px; margin-top: -25px;">Your Support Our Efforts</p>
            <p>&copy; 2024 SportsFit. All rights reserved.</p>
            </footer>
            <script>
            //Background slider
            document.addEventListener("DOMContentLoaded", () => {
                const slides = document.querySelectorAll(".background-slide");
                const dots = document.querySelectorAll(".dot");
                const slider = document.querySelector(".background-slider");
                let currentSlide = 0;
                const slideCount = slides.length;
                const slideInterval = 5000; // Time in milliseconds for auto-slide

                // Function to show a specific slide
                const showSlide = (index) => {
                    currentSlide = index;
                    slider.style.transform = `translateX(-${index * 100}%)`;
                    dots.forEach((dot, idx) => {
                        dot.classList.toggle("active", idx === index);
                    });
                };

                // Function to move to the next slide
                const nextSlide = () => {
                    currentSlide = (currentSlide + 1) % slideCount;
                    showSlide(currentSlide);
                };

                // Set interval for automatic sliding
                let interval = setInterval(nextSlide, slideInterval);

                // Add manual navigation using dots
                dots.forEach((dot, index) => {
                    dot.addEventListener("click", () => {
                        clearInterval(interval); // Stop auto-slide on manual interaction
                        showSlide(index);
                        interval = setInterval(nextSlide, slideInterval); // Restart auto-slide
                    });
                });
            });
            // 
              let currentSlide = 0;

              // Function to move to the next slide
               function nextSlide() {
                const slides = document.querySelector(".slides");
                const totalSlides = slides.children.length;
                currentSlide = (currentSlide + 1) % totalSlides;
                slides.style.transform = `translateX(-${currentSlide * 100}%)`;
              }
 
              // Function to move to the previous slide (if needed)
                function prevSlide() {
                 const slides = document.querySelector(".slides");
                 const totalSlides = slides.children.length;
                 currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
                 slides.style.transform = `translateX(-${currentSlide * 100}%)`;
                }               

                // Automatically move to the next slide every 3 seconds
                setInterval(nextSlide, 3000);
               
                // Optional: Add stop and resume functionality for hover
                const slider = document.querySelector(".slider");
                let autoSlide = setInterval(nextSlide, 3000);

                slider.addEventListener("mouseover", () => clearInterval(autoSlide));
                slider.addEventListener("mouseout", () => {
                autoSlide = setInterval(nextSlide, 3000);
                });

                function addTohomeCart(productName, price, description, imageURL) {
                    alert(productName + " has been added to your cart!");
                    window.location.href = "/cart/add?item=" + encodeURIComponent(productName) +
                          "&price=" + encodeURIComponent(price) +
                          "&description=" + encodeURIComponent(description) +
                          "&imageURL=" + encodeURIComponent(imageURL);
                }

                const slides = document.querySelector('.image-slides');
                const slide = document.querySelectorAll('.image-slide');
                const prevBtn = document.querySelector('.prev-btn');
                const nextBtn = document.querySelector('.next-btn');
                let currentIndex = 0;
                let slideCount = slide.length;

                // Update the slider position
                function updateSlider() {
                    slides.style.transform = `translateX(-${currentIndex * 100}%)`;
                }
                // Move to the previous slide
                prevBtn.addEventListener('click', () => {
                    currentIndex = (currentIndex === 0) ? slideCount - 1 : currentIndex - 1;
                    updateSlider();
                    resetAutoSlide();
                });
                // Move to the next slide
                nextBtn.addEventListener('click', () => {
                    currentIndex = (currentIndex + 1) % slideCount;
                    updateSlider();
                    resetAutoSlide();
                });

                // Auto-slide functionality
                let autoSlideInterval = setInterval(() => {
                    currentIndex = (currentIndex + 1) % slideCount;
                    updateSlider();
                }, 3000); // Auto-slide every 3 seconds
                // Reset auto-slide on manual interaction
                function resetAutoSlide() {
                    clearInterval(autoSlideInterval);
                    autoSlideInterval = setInterval(() => {
                        currentIndex = (currentIndex + 1) % slideCount;
                        updateSlider();
                    }, 3000);
                }
                function scrollToTop() {
                  window.scrollTo({
                  top: 0,
                  behavior: 'smooth'
                });
            }
            const placeholders = ["Search for Products...", "Search for fitness-accessories...", 
            "Let's search for sports-wear...", "Search for sports-collection...", "Search for gym equipments..."];
            let index = 0;
            let charIndex = 0;
            let currentText = "";
            let isDeleting = false;

            const searchInput = document.getElementById("searchInput");

            function typeEffect() {
                if (!isDeleting && charIndex < placeholders[index].length) {
                    // Typing the characters
                    currentText += placeholders[index][charIndex];
                    charIndex++;
                    searchInput.setAttribute("placeholder", currentText);
                } else if (isDeleting && charIndex > 0) {
                    // Deleting the characters
                    currentText = currentText.slice(0, -1);
                    charIndex--;
                    searchInput.setAttribute("placeholder", currentText);
                }

                if (charIndex === placeholders[index].length && !isDeleting) {
                    setTimeout(() => (isDeleting = true), 1000);
                } else if (isDeleting && charIndex === 0) {
                    isDeleting = false;
                    index = (index + 1) % placeholders.length;
                }

                setTimeout(typeEffect, isDeleting ? 50 : 100); // Typing speed (faster when deleting)
            }
            typeEffect();
           
            function toggleMenu() {
                const menuBox = document.getElementById("menuBox");
                menuBox.classList.toggle("open");
            }
        </script>
        </body>
        </html>
        """
    
    @cherrypy.expose
    def search(self, query=None):
        # Simulated product database
        products = [
            {"name": "Yoga Mat", "category": "fitness-accessories", "genre": "Yoga", "price": 999, "image_url": "https://m.media-amazon.com/images/I/51VuwOmpbML._AC_UL320_.jpg"},
            {"name": "Yoga Belt", "category": "fitness-accessories", "genre": "Yoga", "price": 159, "image_url": "https://m.media-amazon.com/images/I/71cNPjtNRaL._SX569_.jpg"},
            {"name": "Yoga Wheel", "category": "fitness-accessories", "genre": "Yoga", "price": 905, "image_url": "https://m.media-amazon.com/images/I/81Fq3WnNtOL._SX679_.jpg"},
            {"name": "Mat Storage Rack", "category": "fitness-accessories", "genre": "Yoga", "price": 999, "image_url": "https://m.media-amazon.com/images/I/51hsMcavesL._SX569_.jpg"},
            {"name": "Yoga Knee Pad", "category": "fitness-accessories", "genre": "Yoga", "price": 599, "image_url": "https://m.media-amazon.com/images/I/41vhdylzM7L._SX300_SY300_QL70_FMwebp_.jpg"},
            {"name": "Protein Bar", "category": "fitness-accessories", "genre": "Strength Training Cardio Fitness Supplements", "price": 800, "image_url": "https://www.bigbasket.com/media/uploads/p/xl/40122051_8-ritebite-max-protein-daily-choco-almond-bar.jpg"},
            {"name": "Protein Bar All in One", "category": "fitness-accessories", "genre": "Strength Training Cardio Fitness Supplements", "price": 616, "image_url": "https://m.media-amazon.com/images/I/41-j+0FO0EL._SY300_SX300_.jpg"},
            {"name": "Whey Protein Powder", "category": "fitness-accessories", "genre": "Strength Training Cardio Fitness Supplements", "price": "2,295", "image_url": "https://m.media-amazon.com/images/I/61lWEi9oS9L._SX679_.jpg"},
            {"name": "Whey Protein Isolate", "category": "fitness-accessories", "genre": "Strength Training Cardio Fitness Supplements", "price": "1,899", "image_url": "https://m.media-amazon.com/images/I/61HkqmptLVL._SX679_.jpg"},
            {"name": "Creatine Monohydrate Powder", "category": "fitness-accessories", "genre": "Strength Training Cardio Fitness Supplements", "price": 549, "image_url": "https://m.media-amazon.com/images/I/51FWl4eLpXL._SX679_.jpg"},
            {"name": "OstoCalcium Chewable Tablets", "category": "fitness-accessories", "genre": "Strength Training Cardio Fitness Supplements", "price": 420, "image_url": "https://m.media-amazon.com/images/I/61Vq58l5tRL._SX679_PIbundle-60,TopRight,0,0_AA679SH20_.jpg"},
            {"name": "Relax Supplement Tablets", "category": "fitness-accessories", "genre": "Strength Training Cardio Fitness Supplements", "price": 899, "image_url": "https://m.media-amazon.com/images/I/51bIBBoiOzL._SX679_.jpg"},
            {"name": "Nutrition Fish Oil", "category": "fitness-accessories", "genre": "Strength Training Cardio Fitness Supplements", "price": 572, "image_url": "https://m.media-amazon.com/images/I/515PbVAs9BL._SY879_.jpg"},
            {"name": "Himalayan Shilajit/Shilajeet Resin", "category": "fitness-accessories", "genre": "Strength Training Cardio Fitness Supplements", "price": 998, "image_url": "https://m.media-amazon.com/images/I/61Axhy9QtOL._SX679_.jpg"},
            {"name": "Resistance Bands", "category": "fitness-accessories", "genre": "Yoga", "price": 500, "image_url": "https://m.media-amazon.com/images/I/612c73jZt1L._SX569_.jpg"},
            {"name": "Tshirt for Men", "category": "sports-wear", "genre": "Wear", "price": 598, "image_url": "https://m.media-amazon.com/images/I/61ThK8RnMjL._SX679_.jpg"},
            {"name": "Line Coat", "category": "sports-wear", "genre": "Wear", "price": 1249, "image_url": "https://m.media-amazon.com/images/I/51OYFbJbwDL._SX679_.jpg"},
            {"name": "Sports Running Set", "category": "sports-wear", "genre": "Wear", "price": 494, "image_url": "https://m.media-amazon.com/images/I/41g3uCT1OpL.jpg"},
            {"name": "Sports Shorts", "category": "sports-wear", "genre": "Wear", "price": 718, "image_url": "https://m.media-amazon.com/images/I/51+mkAk9KeL._SX679_.jpg"},
            {"name": "Bomber Jacket", "category": "sports-wear", "genre": "Wear", "price": 449, "image_url": "https://m.media-amazon.com/images/I/51XWUBbfe7L._SX679_.jpg"},
            {"name": "Treadmill", "category": "gym-equipment", "genre": "Strength Training Cardio Fitness", "price": 20000, "image_url": "https://www.powermaxfitness.net/uploads/thumb/800_600_1657091228_product_06072022123708.jpg"},
            {"name": "Dumbbells", "category": "gym-equipment", "genre": "Strength Training Cardio Fitness", "price": 1500, "image_url": "https://www.ukgymequipment.com/images/2-5-50kg-premium-urethane-dumbbell-set-p5790-75425_image.jpg"},
            {"name": "Kettlebell", "category": "gym-equipment", "genre": "Strength Training Cardio Fitness", "price": 800, "image_url": "https://m.media-amazon.com/images/I/615mcUuFzEL._SX569_.jpg"},
            {"name": "Rowing Machine", "category": "gym-equipment", "genre": "Strength Training Cardio Fitness", "price": 18000, "image_url": "https://m.media-amazon.com/images/I/61waH3MGrSL._AC_UY218_.jpg"},
            {"name": "Gym And Fitness Kit", "category": "gym-equipment", "genre": "Strength Training Cardio Fitness", "price": "1,299", "image_url": "https://m.media-amazon.com/images/I/81XNzjmXi+L._SX569_.jpg"},
            {"name": "Cricket Bat", "category": "sports-accessories", "genre": "Games Cricket Bat", "price": 299, "image_url": "https://m.media-amazon.com/images/I/61VM5dsvGHL._AC_UL320_.jpg"},
            {"name": "Wireless Controller", "category": "sports-accessories", "genre": "Games", "price": "1,746", "image_url": "https://m.media-amazon.com/images/I/31aJy+xNpZL._SY300_SX300_.jpg"},
            {"name": "Rechargeable Hover Football Indoor Game", "category": "sports-accessories", "genre": "Games", "price": 499, "image_url": "https://m.media-amazon.com/images/I/41E5hab325L._SX300_SY300_QL70_FMwebp_.jpg"},
            {"name": "Wrist Support", "category": "sports-accessories", "genre": "Games", "price": 179, "image_url": "https://m.media-amazon.com/images/I/51Ml+0Kx5YL._SX569_.jpg"},
            {"name": "Abs Roller", "category": "sports-accessories", "genre": "Games", "price": 180, "image_url": "https://m.media-amazon.com/images/I/71Vt2Pgy4hL._SX569_.jpg"},
            {"name": "Football", "category": "sports-collection", "genre": "Sports Soccer", "price": 400, "image_url": "https://m.media-amazon.com/images/I/51BREkhP4mL._SX300_SY300_QL70_FMwebp_.jpg"},
            {"name": "Sport Sunglasses", "category": "sports-collection", "genre": "Sports Soccer", "price": 799, "image_url": "https://m.media-amazon.com/images/I/51du4P5G3AL._SX679_.jpg"},
            {"name": "Sports Watch", "category": "sports-collection", "genre": "Sports Soccer", "price": 279, "image_url": "https://m.media-amazon.com/images/I/51BrFkZcMxL._SX679_.jpg"},
            {"name": "Dart Boards", "category": "sports-collection", "genre": "Sports Soccer", "price": 499, "image_url": "https://m.media-amazon.com/images/I/513y-y80AOL._SX300_SY300_QL70_FMwebp_.jpg"},
            {"name": "Stress Buster Cube", "category": "sports-collection", "genre": "Sports Soccer", "price": 349, "image_url": "https://m.media-amazon.com/images/I/71OXrIaR0nL._SY450_.jpg"},
        ]
    
        # Filter products based on search query
        results = [
          product for product in products 
            if query.lower() in product["name"].lower() or
            query.lower() in product["category"].lower() or
            query.lower() in product["genre"].lower()
        ]

        # Generate HTML for results
        if results:
            result_html = "".join(
                f"""
                <div class="product">
                    <img src="{product['image_url']}" alt="{product['name']}">
                    <h3>{product['name']}</h3>
                    <p>Category: {product['category']}</p>
                    <p>Price: ₹{product['price']}</p>
                    <button onclick="addToCart('{product['name']}', '{product['price']}', '{product['category']}', '{product['image_url']}')">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffffff" fill="none">
                        <path d="M8 16H15.2632C19.7508 16 20.4333 13.1808 21.261 9.06908C21.4998 7.88311 21.6192 7.29013 21.3321 6.89507C21.045 6.5 20.4947 6.5 19.3941 6.5H19M6 6.5H7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                        <path d="M10.5 7C10.5 7 11.5 7 12.5 9C12.5 9 15.6765 4 18.5 3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                        <path d="M8 16L5.37873 3.51493C5.15615 2.62459 4.35618 2 3.43845 2H2.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                        <path d="M8.88 16H8.46857C7.10522 16 6 17.1513 6 18.5714C6 18.8081 6.1842 19 6.41143 19H17.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                        <circle cx="10.5" cy="20.5" r="1.5" stroke="currentColor" stroke-width="1.5" />
                        <circle cx="17.5" cy="20.5" r="1.5" stroke="currentColor" stroke-width="1.5" />
                    </svg></button>
                    <button class="wishlist-btn" onclick="addToWishlist('{product['name']}', '{product['price']}', '{product['image_url']}')"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffffff" fill="none">
                        <path d="M12 21C10.6588 21 9.88572 20.4278 8.33953 19.2834C0.221721 13.2749 1.01807 6.15294 4.53744 3.99415C7.21909 2.34923 9.55962 3.01211 10.9656 4.06801C11.5422 4.50096 11.8304 4.71743 12 4.71743C12.1696 4.71743 12.4578 4.50096 13.0344 4.06801C14.4404 3.01211 16.7809 2.34923 19.4626 3.99415C21.1812 5.04838 22.2505 7.28623 21.9494 10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                        <path d="M14 18C14 18 15 18 16 20C16 20 19.1765 15 22 14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                    </svg></button>
                    <a href="/product_details?name={product['name']}"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#ffffff" fill="none">
                    <path d="M21.8551 15.5L18.9298 5.60666C18.6485 4.65457 17.7646 4 16.7601 4C15.475 4 14.4485 5.05662 14.502 6.32437L15 16M22 16.5C22 18.433 20.433 20 18.5 20C16.567 20 15 18.433 15 16.5C15 14.567 16.567 13 18.5 13C20.433 13 22 14.567 22 16.5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                    <path d="M10 8H14M9 16H15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                    <path d="M2.14494 15.5L5.07067 5.60666C5.35192 4.65457 6.23586 4 7.24034 4C8.52545 4 9.55194 5.05662 9.49844 6.32437L9.00044 16M9 16.5C9 18.433 7.433 20 5.5 20C3.567 20 2 18.433 2 16.5C2 14.567 3.567 13 5.5 13C7.433 13 9 14.567 9 16.5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                </svg></a>
                </div>
                """
                for product in results
            )
        else:
            result_html = "<p>No products found.</p>"

        return f"""
          <html>
           <head>
            <title>Search Results</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 0;
                }}
                h1 {{
                    text-align: center;
                    color: #333;
                    margin-top: 20px;
                }}
                .results {{
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                    gap: 20px;
                    margin: 20px;
                    padding: 20px;
                }}
                .product {{
                    background: white;
                    border: 1px solid #ccc;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    padding: 15px;
                    text-align: center;
                }}
                .product img {{
                    max-width: 100%;
                    height: auto;
                    border-radius: 10px;
                }}
                .product h3 {{
                    font-size: 18px;
                    margin: 10px 0;
                    color: #555;
                }}
                .product p {{
                    color: #666;
                    margin: 5px 0;
                }}
                a {{
                    display: block;
                    text-align: center;
                    margin-top: 20px;
                    color: white;
                    background-color: #007bff;
                    padding: 10px;
                    text-decoration: none;
                    border-radius: 5px;
                    width: fit-content;
                    margin-left: auto;
                    margin-right: auto;
                }}
                a:hover {{
                    background-color: #0056b3;
                    transform: scale(1.05);
                }}
                button {{
                        background-color: #ff9900;
                        color: white;
                        border: none;
                        padding: 10px 15px;
                        border-radius: 5px;
                        cursor: pointer;
                        margin-top: 10px;
                }}
                button:hover {{
                    background-color: #e68a00;
                    transform: scale(1.05);
                }}
                .wishlist-btn {{ background-color: #7ED321; }}
                .wishlist-btn:hover {{ background-color: #3F6416; transform: scale(1.05);}}
            </style>
        </head>
        <body>
            <h1>Search Results for "{query}"</h1>
            <div class="results">
                {result_html}
            </div>
             <script>
                function addToCart(name, price, category, imageURL) {{
                    alert(name + " has been added to your cart!");
                    // Redirect to cart endpoint (optional)
                    window.location.href = "/cart/add?item=" + encodeURIComponent(name)+
                          "&price=" + encodeURIComponent(price) +
                          "&category=" + encodeURIComponent(category) +
                          "&imageURL=" + encodeURIComponent(imageURL);
                }}
                function addToWishlist(name, price, imageUrl) {{
                const form = document.createElement('form');
                form.method = 'post';
                form.action = '/wishlist/add';

                const nameInput = document.createElement('input');
                nameInput.type = 'hidden';
                nameInput.name = 'item';
                nameInput.value = name;
                form.appendChild(nameInput);

                const priceInput = document.createElement('input');
                priceInput.type = 'hidden';
                priceInput.name = 'price';
                priceInput.value = price;
                form.appendChild(priceInput);

                const imageInput = document.createElement('input');
                imageInput.type = 'hidden';
                imageInput.name = 'imageUrl';
                imageInput.value = imageUrl;
                form.appendChild(imageInput);

                document.body.appendChild(form);
                form.submit();
            }}
        </script>
        </body>
        </html>
        """

    
    @cherrypy.expose
    def product_details(self, name=None):
    # Simulated product database
     products = [
         {"name": "Yoga Mat", "category": "fitness-accessories", "genre": "Yoga", "price": 999, "image_url": "https://m.media-amazon.com/images/I/51VuwOmpbML._AC_UL320_.jpg"},
         {"name": "Yoga Belt", "category": "fitness-accessories", "genre": "Yoga", "price": 159, "image_url": "https://m.media-amazon.com/images/I/71cNPjtNRaL._SX569_.jpg"},
         {"name": "Yoga Wheel", "category": "fitness-accessories", "genre": "Yoga", "price": 905, "image_url": "https://m.media-amazon.com/images/I/81Fq3WnNtOL._SX679_.jpg"},
         {"name": "Mat Storage Rack", "category": "fitness-accessories", "genre": "Yoga", "price": 999, "image_url": "https://m.media-amazon.com/images/I/51hsMcavesL._SX569_.jpg"},
         {"name": "Yoga Knee Pad", "category": "fitness-accessories", "genre": "Yoga", "price": 599, "image_url": "https://m.media-amazon.com/images/I/41vhdylzM7L._SX300_SY300_QL70_FMwebp_.jpg"},
         {"name": "Resistance Bands", "category": "fitness-accessories", "genre": "Yoga", "price": 500, "image_url": "https://m.media-amazon.com/images/I/612c73jZt1L._SX569_.jpg"},        
         {"name": "Protein Bar", "category": "fitness-accessories", "genre": "Strength Training Cardio Fitness", "price": 800, "image_url": "https://www.bigbasket.com/media/uploads/p/xl/40122051_8-ritebite-max-protein-daily-choco-almond-bar.jpg"},        
         {"name": "Protein Bar All in One", "category": "fitness-accessories", "genre": "Strength Training Cardio Fitness Supplements", "price": 616, "image_url": "https://m.media-amazon.com/images/I/41-j+0FO0EL._SY300_SX300_.jpg"},
         {"name": "Whey Protein Powder", "category": "fitness-accessories", "genre": "Strength Training Cardio Fitness Supplements", "price": "2,295", "image_url": "https://m.media-amazon.com/images/I/61lWEi9oS9L._SX679_.jpg"},
         {"name": "Whey Protein Isolate", "category": "fitness-accessories", "genre": "Strength Training Cardio Fitness Supplements", "price": "1,899", "image_url": "https://m.media-amazon.com/images/I/61HkqmptLVL._SX679_.jpg"},
         {"name": "Creatine Monohydrate Powder", "category": "fitness-accessories", "genre": "Strength Training Cardio Fitness Supplements", "price": 549, "image_url": "https://m.media-amazon.com/images/I/51FWl4eLpXL._SX679_.jpg"},
         {"name": "OstoCalcium Chewable Tablets", "category": "fitness-accessories", "genre": "Strength Training Cardio Fitness Supplements", "price": 420, "image_url": "https://m.media-amazon.com/images/I/61Vq58l5tRL._SX679_PIbundle-60,TopRight,0,0_AA679SH20_.jpg"},
         {"name": "Relax Supplement Tablets", "category": "fitness-accessories", "genre": "Strength Training Cardio Fitness Supplements", "price": 899, "image_url": "https://m.media-amazon.com/images/I/51bIBBoiOzL._SX679_.jpg"},
         {"name": "Nutrition Fish Oil", "category": "fitness-accessories", "genre": "Strength Training Cardio Fitness Supplements", "price": 572, "image_url": "https://m.media-amazon.com/images/I/515PbVAs9BL._SY879_.jpg"},
         {"name": "Himalayan Shilajit/Shilajeet Resin", "category": "fitness-accessories", "genre": "Strength Training Cardio Fitness Supplements", "price": 998, "image_url": "https://m.media-amazon.com/images/I/61Axhy9QtOL._SX679_.jpg"},
         {"name": "Tshirt for Men", "category": "sports-wear", "genre": "Wear", "price": 598, "image_url": "https://m.media-amazon.com/images/I/61ThK8RnMjL._SX679_.jpg"},
         {"name": "Line Coat", "category": "sports-wear", "genre": "Wear", "price": "1,249", "image_url": "https://m.media-amazon.com/images/I/51OYFbJbwDL._SX679_.jpg"},
         {"name": "Sports Running Set", "category": "sports-wear", "genre": "Wear", "price": 494, "image_url": "https://m.media-amazon.com/images/I/41g3uCT1OpL.jpg"},
         {"name": "Sports Shorts", "category": "sports-wear", "genre": "Wear", "price": 718, "image_url": "https://m.media-amazon.com/images/I/51+mkAk9KeL._SX679_.jpg"},
         {"name": "Bomber Jacket", "category": "sports-wear", "genre": "Wear", "price": 449, "image_url": "https://m.media-amazon.com/images/I/51XWUBbfe7L._SX679_.jpg"},
         {"name": "Skipping Rope", "category": "fitness-accessories", "genre": "Cardio", "price": 200},
         {"name": "Treadmill", "category": "gym-equipment", "genre": "Strength Training Cardio Fitness", "price": 20000, "image_url": "https://www.powermaxfitness.net/uploads/thumb/800_600_1657091228_product_06072022123708.jpg"},
         {"name": "Dumbbells", "category": "gym-equipment", "genre": "Strength Training Cardio Fitness", "price": 1500, "image_url": "https://www.ukgymequipment.com/images/2-5-50kg-premium-urethane-dumbbell-set-p5790-75425_image.jpg"},
         {"name": "Kettlebell", "category": "gym-equipment", "genre": "Strength Training Cardio Fitness", "price": 800, "image_url": "https://m.media-amazon.com/images/I/615mcUuFzEL._SX569_.jpg"},
         {"name": "Rowing Machine", "category": "gym-equipment", "genre": "Strength Training Cardio Fitness", "price": 18000, "image_url": "https://m.media-amazon.com/images/I/61waH3MGrSL._AC_UY218_.jpg"},
         {"name": "Gym And Fitness Kit", "category": "gym-equipment", "genre": "Strength Training Cardio Fitness", "price": "1,299", "image_url": "https://m.media-amazon.com/images/I/81XNzjmXi+L._SX569_.jpg"},
         {"name": "Dumbbells", "category": "gym-equipment", "genre": "Strength Training", "price": 1500},
         {"name": "Kettlebell", "category": "gym-equipment", "genre": "Strength Training", "price": 800},
         {"name": "Cricket Bat", "category": "sports-accessories", "genre": "Games Cricket Bat", "price": 299, "image_url": "https://m.media-amazon.com/images/I/61VM5dsvGHL._AC_UL320_.jpg"},
         {"name": "Wireless Controller", "category": "sports-accessories", "genre": "Games", "price": "1,746", "image_url": "https://m.media-amazon.com/images/I/31aJy+xNpZL._SY300_SX300_.jpg"},
         {"name": "Rechargeable Hover Football Indoor Game", "category": "sports-accessories", "genre": "Games", "price": 499, "image_url": "https://m.media-amazon.com/images/I/41E5hab325L._SX300_SY300_QL70_FMwebp_.jpg"},
         {"name": "Wrist Support", "category": "sports-accessories", "genre": "Games", "price": 179, "image_url": "https://m.media-amazon.com/images/I/51Ml+0Kx5YL._SX569_.jpg"},
         {"name": "Abs Roller", "category": "sports-accessories", "genre": "Games", "price": 180, "image_url": "https://m.media-amazon.com/images/I/71Vt2Pgy4hL._SX569_.jpg"},
         {"name": "Football", "category": "sports-collection", "genre": "Sports Soccer", "price": 400, "image_url": "https://m.media-amazon.com/images/I/51BREkhP4mL._SX300_SY300_QL70_FMwebp_.jpg"},
         {"name": "Sport Sunglasses", "category": "sports-collection", "genre": "Sports Soccer", "price": 799, "image_url": "https://m.media-amazon.com/images/I/51du4P5G3AL._SX679_.jpg"},
         {"name": "Sports Watch", "category": "sports-collection", "genre": "Sports Soccer", "price": 279, "image_url": "https://m.media-amazon.com/images/I/51BrFkZcMxL._SX679_.jpg"},
         {"name": "Dart Boards", "category": "sports-collection", "genre": "Sports Soccer", "price": 499, "image_url": "https://m.media-amazon.com/images/I/513y-y80AOL._SX300_SY300_QL70_FMwebp_.jpg"},
         {"name": "Stress Buster Cube", "category": "sports-collection", "genre": "Sports Soccer", "price": 349, "image_url": "https://m.media-amazon.com/images/I/71OXrIaR0nL._SY450_.jpg"},
    ]

    # Find the product by name
     product = next((p for p in products if p["name"] == name), None)

    # If product is not found
     if not product:
        return f"""
        <html>
        <head><title>Product Not Found</title></head>
        <body>
            <h1>Product Not Found</h1>
            <p>Sorry, we could not find the product you're looking for.</p>
        </body>
        </html>
        """
     
     return f"""
        <html>
        <head>
        <title>{product['name']} - Product Details</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
                text-align: center;
            }}
            .product {{
                background: white;
                margin: 50px auto;
                padding: 20px;
                max-width: 600px;
                border: 1px solid #ccc;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }}
            .product img {{
                max-width: 100%;
                border-radius: 10px;
            }}
            .product h1 {{
                font-size: 24px;
                color: #333;
            }}
            .product p {{
                font-size: 18px;
                color: #555;
            }}
            a {{
                color: white;
                background-color: #007bff;
                padding: 10px 15px;
                text-decoration: none;
                border-radius: 5px;
            }}
            a:hover {{
                background-color: #0056b3;
                transform: scale(1.05);
            }}
        </style>
    </head>
    <body>
        <div class="product">
            <img src="{product.get('image_url', '#')}" alt="{product['name']}">
            <h1>{product['name']}</h1>
            <p>Category: {product['category']}</p>
            <p>Genre: {product['genre']}</p>
            <p>Price: ₹{product['price']}</p>
        </div>
       <a href="/">Go Back to Home</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    root = SportsFitECommerce()
    root.login = LoginPage()  
    root.products = Products()
    root.contact = ContactPage()
    root.productdetails = ProductPage()
    root.checkout = CheckoutPage()
    root.cart = CartPage()
    root.wishlist = WishlistPage()
    cherrypy.config.update({
        "tools.sessions.on": True,  # Enable sessions
        "tools.sessions.storage_type": "ram",  # Use in-memory storage for sessions
        "tools.sessions.timeout": 60,  # Session timeout in minutes
        "server.socket_port": 8080,
        "server.socket_host": "127.0.0.1",
    })
    cherrypy.quickstart(root)
