# Import necessary libraries
import pandas as pd

# Load the data
businesses = pd.read_csv("data/businesses.csv")
new_businesses = pd.read_csv("data/new_businesses.csv")
countries = pd.read_csv("data/countries.csv")
categories = pd.read_csv("data/categories.csv")


# Use as many cells as you like
businesses.head(5)

#1
#merging the businesses and countries datasets into one
businesses_countries = businesses.merge(countries, on="country_code")
businesses_countries.head(10)

# DataFrame that lists only the continent and oldest year_founded
continent_df = businesses_countries.groupby("continent").agg({"year_founded": "min"})
continent_df.head(10)

#Merge this continent DataFrame with businesses_countries
merged_continent = continent_df.merge(businesses_countries, on = ["continent", "year_founded"])
merged_continent.head(10)

#oldest_business_continent with four columns: continent, country, business, and year_founded
oldest_by_continent_category = merged_continent[["continent","country","business","year_founded"]]
oldest_by_continent_category.head(10)


#2
#Add the data in new_businesses
all_businesses  = pd.concat([new_businesses,businesses])

#merge between the businesses and the countries data. Use additional parameters this time to perform an outer merge and create an indicator column to better see the missing values. An outer merge combines two DataFrames based on a key column and includes all rows from both DataFrames

new_all_countries = all_businesses.merge(countries, on = "country_code", how = "outer", indicator = True)
new_all_countries.head(10)

#find countries with missing business data]
new_missing_countries = new_all_countries[new_all_countries["_merge"] != "both"]
print(new_missing_countries)

#Group by continent and create a "count_missing" column

count_missing = new_missing_countries.groupby("continent").agg({"country":"count"})

count_missing.columns = ["count_missing"]
print(count_missing)

#3
##] Start by merging the businesses and categories data into one DataFrame

businesses_categories = businesses.merge(categories, on = "category_code")
print(businesses_categories)

## Merge all businesses, countries, and categories together
businesses_categories_countries  = businesses_categories.merge(countries, on="country_code")

#Create the oldest by continent and category DataFrame
oldest_by_continent_category = businesses_categories_countries.groupby(["continent", "category"]).agg({"year_founded":"min"})
print(oldest_by_continent_category)