# pythonProject
1. Idea:
Our shared passion for basketball inspired us to combine our interests with the available hardware, leading to the creation of a simple and enjoyable game. Our goal was to develop a motion-controlled basketball game where players can throw the ball using hand gestures.
2. Implementation:
To bring our idea to life, we divided the tasks among our team members. One team focused on setting up the environment for the DPS368 air pressure sensor, while the other team worked on designing and coding the basketball game using Python.
2.1.1 Setting up the Sensor Environment:
We followed a comprehensive guide that you can find at this post to set up the environment for the DPS368 air pressure sensor. However, we encountered limitations with using macOS and Applesilicon, as the sensor was not recognized effectively. As a result, we found that the Arduino IDE installation on a Windows device provided the most efficient solution.
2.1.2 Implementing code in Arduino IDE
We utilized the Arduino IDE to implement the necessary code for the sensor, enabling us to capture motion data accurately. We used the default code given in the provided guide but we made small changes such as ignoring the temperature factors because they were redundant for our project.
2.2 Implementing a simple basketball game in Python
Using Python, we developed a basic basketball game that incorporated the motion data from the sensor. Players could interact with the game by making throwing motions with their hand, resulting in a simulated ball throw. The project was mainly fulfilled by using the turtle library.  
3. Project Outcome
Within approximately 20 hours, we successfully achieved our objective of combining our interests and creating a unique prototype that showcased the capabilities of the DPS368 air pressure sensor. Throughout the project, we gained valuable experience, particularly since most of us had limited programming knowledge and no previous experience with Raspberry Pis or sensors. This opportunity allowed us to deepen our understanding of Infineon's sensors and improve our programming skills.
4. Outlook for Future Improvements
Due to time constraints, there were several improvements that we were unable to implement. For instance, enhancing the game's graphical user interface (GUI) and optimizing the code to reduce the time required to process the sensor's movement data for ball throwing. A more efficient approach would involve throwing the ball as soon as the sensor detects any movement.
5. Conclusion
Completing this project was a rewarding experience for all of us. Working with Infineon's sensors has sparked our interest in programming with sensors and we are grateful for the opportunity to learn and grow. The project not only allowed us to combine our passion for basketball with technology but also expanded our skills and knowledge in programming and sensor integration.
