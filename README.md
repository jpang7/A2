# CURent-- list and view properties near Cornell

Used Cornell's PoBE A2 Flask boilerplate.  
Deployed through Docker + Google Cloud  
Databasing with PostgreSQL + SQLAlchemy  
Many thanks to the AppDev team, especially Backend instructors.

##Endpoints  
http://35.231.160.51/rent/ returns "Hello World"  
http://35.231.160.51/rent/allhouses returns a list of dictionaries representing each property. View all the listings here.  
http://35.231.160.51/rent/createhouse/name/price/location/address/ownerName/latitude/longitude
  fill in the parameters and list your property. Will throw if you enter a duplicate propertyName. Returns success indicator otherwise.   
http://35.231.160.51/rent/delete/<name> fill in the property name-- will throw if specified property does not exist. Returns success indicator otherwise.  
http://35.231.160.51/rent/deleteall deletes all listings. Returns success indicator when used correctly.
