<h1>Idea 1:  Calculate “fitness plan” for the day based on transportation schedules, daily walking and fitness goals</h1>
<h2>Problem Definition: </h2>
<p>I have a specific schedule for my work/school. I also want to walk a specific number of miles every day to stay fit, but I don’t know what is the most effective time to walk in between my classes and daily activities. </p>
<h2>User Story: </h2>
<p>With this web app, users will input their tentative schedules (either using Google Calendar or our template calendar) and be able to start their day by setting a distance goal to meet. The application will use traffic, MBTA and distance information to compute the most optimal way for the user to reach this goal, and produce a “route” for them to follow that day, incorporating the bus, T, walking and a car (if applicable), to take to and from each of their destinations.</p>
<h2>User Requirements: </h2>
<ul>
<li>The application takes in the user’s schedule for the week as well the location of each event.</li>
<li>The system will pull data about public transportation and traffic based on the user’s route/schedule.</li>
<li>The software can develop a user friendly graphic object of a calendar with all the information displayed.</li>
<li>The algorithm will compute route options for the user using the MBTA and traffic info, giving path intervals for users to use to walk/meet their fitness goals for the day.</li>
</ul>
<h2>Data Sources - APIs: </h2>
<ul>
  <li>Google Calendar API</li>
  <li>Nutrionix API</li>
  <li>Google Maps, Directions API</li>
  <li>Google Authentication</li>
  <li>BU Shuttle Database (?)</li>
</ul>


<br>
<h1>Idea 2: Calculate a rating of location </h1>
<h2>Problem Definition: </h2>
<p>
  If I am moving to a different city, I don’t know which area to live 
in. Factors such as public transportation, the cost of living, location of nearby police 
departments, hospitals, public schools, crime rate all influence my decision of location. 
</p>
<h2>User Story: </h2>
<p>
  The webapp makes the process of moving one step easier by providing users with the ability to search different places and receive a rating or livability score based on different factors about the location. The algorithm will take information regarding things such as nightlife, employment, rent, transportation, and safety and compute a rating based on this information.
</p>
<h2>User Requirements: </h2>
<ul>
  <li>The software shall provide users the ability to search any location in the US.</li>
  <li>The webapp will generate livability scores based on the queries after pulling data about that location.</li>
  <li>User picks a radius of a specific location to track places to live in.</li>
  <li>User has an option to pick what requirements mean more to them.</li>
  <li>A picture of the map with the desired radius is displayed. The map will be separated into different sections of three colours: Red, Yellow, Green.</li>
  <li>When the user picks an area, they can view the available real estates in that area.</li>
</ul>
<h2>Data Sources - APIs: </h2>
<ul>
<li>Indeed API - employment</li>
<li>Zillow API - rent</li>
<li>Google Maps API - Transportation</li>
<li>FBI Crime Data API - crime rates</li>
<li>Bureau of Labor Statistics' Public Data API - unemployment rate, pensions</li>
<li>Civil Rights Data Collection API - schools, civil rights, etc. </li>
  <li>Real Estate Cloud MLS API - real estate searcher </li>
<li>Google Authentication</li>
</ul>
