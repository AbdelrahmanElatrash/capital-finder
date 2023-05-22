# capital-finder

this project is buld using serverless function and deploy in vercel ,
using python 


## deployed URL
[link](https://capital-finder-ecru-eta.vercel.app/api/capital_finder)

## END POINT 
go to url https://capital-finder-ecru-eta.vercel.app/api/capital_finder

- to find capital of country add country name as query params 
> https://capital-finder-ecru-eta.vercel.app/api/capital_finder?country=country_name

response : "The capital of country is capital"  
         or "Unable to find the capital of country"

- to find country for a capital add capital name as query params
> https://capital-finder-ecru-eta.vercel.app/api/capital_finder?capital=capital_name

response : "capital_name is the capital of country"
         or "Unable to find the countrycapital of capital"
