# WaterMeter

#### Solution repository for Hack3 hackathon's 3rd track (Water)

## Inspiration
Our inspiration was ESDS(The Earth Science Data Systems),that provides full and open access to NASA's collection of Earth science data for understanding and protecting our home planet.Our main idea was to create something similar,so we started working on it.

## What it does
WaterMeter is a system that provides the client an ability to define a drinking water source/lack location with detailed description. All these locations are added to the database and are visualized on interactive maps with detailed information.

## How we built it
First of all, it started with finding a tool that could visualize data on map. After google searching for a while, we ran into a tool for python called "Folium" that could handle interactive map visualization with markers, area definitions etc.

Secondly, we chose a framework to handle all the templates and backend stuff. We ended up choosing Flask, because of its strait forward architecture and also, due to the reason that Folium had an example of integration with Flask.

Finally, it was a matter of 10+ hours of development, learning, surfing through various tools documentations, watching YouTube tutorials ant etc.

## Challenges we ran into
During development and brainstorming, we ran into many complex challenges that needed a solution and answer.

- Data gathering from clients (input forms etc.)
- Data visualization on map
- General idea of the app (How to define water lack and source locations, etc.)

## Accomplishments that we're proud of

## What we learned
- Got more proficient in Git and Github
- Learned how to visualize data on map with python (Folium library)
- Got more proficient in Flask and Python


## What's next for WaterMeter
- Creation of machine learning algorithm that will predict water lack locations based on previous locations and on factors like humidity, temperature, water quality and etc.
- More detailed maps with heatmaps of water quality, Ph, pollution level around the globe.

## Languages & tools we used
- Python
- Flask
- Sqlite
- SQLAlchemy
- Folium
- OpenStreetMap
- Html, CSS, Bootstrap
- Github
- Figma (For logo and banner design)