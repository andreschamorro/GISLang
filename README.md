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

Operation and Rules  
	Arithmetic operations:  
		+: Every operation in the same type return an array of the same type  
			Operations with different type in same set return set type.  
			(e.g. River+Streams -> WaterBody)  
			Operation in different set return Map type.  
			(e.g. River+Neighborhood -> Map)  
		-: As differentiation sets.  

Functions:

print(Type)  
	returns the Type information in a certain format.

## Language Demostration

[![IMAGE ALT TEXT](http://img.youtube.com/vi/ZGW8-an3OGU/0.jpg)](http://www.youtube.com/watch?v=ZGW8-an3OGU "GISLang Demo")

## Language Reference Manual

Command | Parameter | Description
------- | --------- | -----------
Edification | Point (x, y) | Defines Edification type
House | Point (x, y) | Defines Edification type
School    | Point (x, y) | Defines School type
Hospital  | Point (x, y) | Defines Hospital type
Comercial | Point (x, y) | Defines Comercial type
Region | array of Point | Define a region on map
Block | array of Edification | Define a urban block on map
Neighborhood | array of Block | Define a Neighborhood with their Block
Town | array of Neighborhood | Define a Town
State | array of Town | Define a state with their Town
River | array of Point x[], y[] | Define a River on map
Lake  | array of Point x[] | Define a Lake on map
Street| array of Point x[], y[] | Define a Street on map
+ | Two types | Return set of elements

## Language development

The translator architecture was built with Python. It uses several functions written in Python that might exist inside the translator 
or outside it. Inside the translator,  the functions are merely used for token manipulation,  print,  select the right command. After 
being translated from GISLang execute the functions with the parameters taken from the tokens that got translated from GISLang. The 
tokens are preselected,  named with their functionality in the program they might get sent to other functions for further use if 
needed for token manipulation or to do a specific command as defined by the user that created the language.

To create the language,  we used a parser implemented in Python named PLY a package that includes Lex and YACC written in Python. It 
uses left to right parsing,  and provides most of the original functionalities of said programs,  which include support for empty 
productions,  precedence rules,  error recovery,  and support for ambiguous grammars. There we defined the characteristics of our 
language,  its reserved words,  grammatic,  and the general structure for the language.

## Credits

Kevin Aponte.  
Andres Chamorro.  
Daniel Rodriguez.  
Mario Zepeda.  
