# GISLang

Geographic Information System Language proposal

## Introduction

Geographic information system (GIS) software is used for visualizing, managing, creating, and analyzing geographic data. This kind of software builds a platform to understand the geographic context of data, allowing the identification of patterns in new ways. 
GIS software lets you produce maps and other graphic displays of geographic information for analysis and presentation. With these capabilities a GIS is a valuable tool to visualize spatial data or to build decision support systems for use in your organization.
A GIS stores data on geographical features and their characteristics. The features are typically classified as points, lines, or areas. On a map city data could be stored as points, road data could be stored as lines, and boundaries could be stored as areas.

Geographic Information System (GIS) software evolved out of the fields of geography, cartography, and database management. As a result, off-the-shelf GIS software requires the user to have or to acquire considerable knowledge of these fields. Navigation through the interfaces of most off-the-shelf GIS software is difficult because they support a system architecture view, rather than a view of the user's work. These problems are compounded for users with little computing experience. In many workplaces, a single technical user becomes the local GIS expert, and acts as a surrogate for other users who have neither the expertise to use the software nor the resources to acquire that expertise.

The idea behind the design of a Language for implementation of GIS Software is approaching the problem from a friendly using perspective. This language will be designed to be used intuitively and in this sense enables non expert user the use of a powerful tool for GIS implementation. 


## Language Features

Types:  
	Edification (x, y):  
	House  
	School  
	Hospital  
	Comercial (big and small)  
Region ( x[ ] ):  
	Block  ( Edification[ ] )  
	Neighborhood ( Block[ ]  )  
	Town ( Neighborhood[ ] )  
	State ( Town[ ] )  
WaterBody:  
	River ( x[ ], y[ ])  
	Lake ( x[ ] )  
Street ( x[ ], y[ ] )  

Map ( Edification[ ], Region[ ], WaterBody[ ], Street[ ] )

Control flow statement  
	For loop:  
For a certain element type it goes over a set identifying the elements with the desired element type   ( For( House  h1 in  B) ).

Operation and Rules  
	Arithmetic operations:  
		+: Every operation in the same type return an array of the same type  
			Operations with different type in same set return set type.  
			(e.g. River+Streams -> WaterBody)  
			Operation in different set return Map type.  
			(e.g. River+Neighborhood -> Map)  
		-: As differentiation sets.  

Functions:

list(Type)  
	Show a list of element and their attributes.  
perimeter(Type)  
	Calculate the perimeter of the given region.  
area(Type)  
	Calculate the area of the given region.  
distance(Type, Type)  
Type(Type)  
	Return Type.  
sizeof(Type)
	Return number of element.  
Location(Type)  
	Return mass center coordinate of type.  
print(Type)  
	returns the Type information in a certain format.  

## Credits

Kevin Aponte.  
Andres Chamorro.  
Daniel Rodriguez.  
Mario Zepeda.  
