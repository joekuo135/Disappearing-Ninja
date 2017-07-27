# Disappearing-Ninja-Python
![](static/images/tmnt.png) <br>
Build a FLASK application with the below functionality:

  • URL routing
  • Using views
  • Rendering static content

These are the routes that need to set up:
1. On the default page ('localhost:5000'), it should display a view that says "No ninjas here"
2. When user visits 
    /ninja, it should display all four Ninja Turtles (Leonardo, Michelangelo, Raphael, and Donatello)
    /ninja/[ninja_color], should display the corresponding Ninja Turtle (grab the color parameter out of the requested URL)
3. If user visits /ninja/blue, it should only display the Ninja Turtle Leonardo.
    /ninja/orange - Ninja Turtle Michelangelo.
    /ninja/red - Ninja Turtle Raphael
    /ninja/purple - Ninja Turtle Donatello
4. If a user tries to hack into your web app by specifying a color or string combination other than the colors 
    (Blue, Orange, Red, and Purple), example: /ninja/black or /ninja/123, then display the image notapril.jpg
