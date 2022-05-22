# Hygenie

## Inspiration

WIth recent outbreaks in COVID-19, we were reminded of the importance of maintaining proper hygienic practices in public spaces. As we did more research on hygienic practices, we noticed that handwashing was a particularly important aspect in public spaces. According to the CDC, proper handwashing could prevent 1 million deaths every year from illnesses spread by germs – only around 5% of people actually wash their hands correctly. Additionally, despite the increased awareness in maintaining one’s hygiene during the pandemic, 1 in 4 Americans still aren’t washing their hands regularly. 

In order to combat these easily preventable public health concerns, we developed Hygenie, a public safety system that ensures that individuals wash their hands properly before exiting the bathroom.

## What it does

Hygenie is a system composed of two major components. The first component is a machine learning algorithm that uses computer vision to create pose estimations that analyze hand posture while individuals are washing their hands. By creating a skeleton of both the right and left hands based on joint locations, this algorithm detects hand posture and determines whether or not the relative position of both hands best simulates the correct form for handwashing. The second major component of Hygenie utilizes hardware components like an Arduino and a Servo motor that locks and unlocks the bathroom door based on whether or not the individual has completed a successful hand washing routine.

## How we built it

We built the machine learning algorithm of Hygenie using the OpenCV library, a webcam, and a computer vision library by Google called MediaPipe. MediaPipe allows developers to perform pose estimation on different limbs of the body. We utilized this library to build an algorithm that detects the number of points on the pose estimation that intersect between each hand and evaluates if the number of point intersections is enough to determine that hands are being washed. 

We built the hardware component of Hygenie using an Arduino board and a Servo motor. We wired the Servo motor to the Arduino via PWM, and attached a beam to the axle to simulate a simple, but effective, lock for a door. We programmed the Arduino with Python using the pyfirmata library.

## Challenges we ran into

One initial challenge we ran into was developing an idea that we felt was implementable, and would have a practical use with both software and hardware components. After we had decided on an idea, we ran into many challenges on performing pose estimation consistently in different environments and different camera backgrounds.

## Accomplishments that we're proud of

One accomplishment we are proud of is how we were able to integrate a software component that used computer vision to control the action of a hardware component on an Arduino, all using Python. It was the first time we had done so in any hackathon so it was an exciting and enlightening experience for all of us.

We are also proud of how our idea was able to improve public health in a very affordable way (using only servo motors and a camera) that can scale to large facilities.

## What we learned

One skill we learned was how to track the posture of a person in a camera. Through the MediaPipe and OpenCV libraries, we were able to perform pose estimation by tracking the joints across different body parts which was something new we had not implemented before. Additionally, it was our first time integrating hardware with software considering the limitations that online hackathons presented to working as a team.

## What's next for Hygenie

Future plans for Hygenie include upgrading our locking mechanism with multiple affordable and efficient servo motors to improve the lock, placing these motors within the door frame to implement secure locking mechanisms, installing a motion sensor to ensure that users actually run water and don’t just pantomime washing their hands, and most importantly, expanding Hygenie to public facilities such as hospitals, malls, restaurants, and more. In this way, Hygenie can serve the public good by preventing the large-scale transmission of germs and diseases.

