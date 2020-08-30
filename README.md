# Recipe-Picker

### A program that can scrape recipes from certain websites and randomly choose one for the user


Download the files, navigate to the location it was saved to.
To scrape a recipe run this code in command line while in the directory with the project:
```python recipe_adder```
It will prompt for the recipe URL and the website host (i.e. Food, Foodnetwork,...)
If this is the first recipe you are adding, a txt file name recipes will be created in the current directory with the recipe added.
If not then it will append the recipe onto the existing txt file. 

To generate a random recipe run this code in command line while in the directory with the project:
```python main```
A window will pop up and click the Generate button. It will choose a random recipe from 'recipes.txt' and copy the URL to your clipboard


#### Currently supports:
 - [food.com](https://www.food.com/)
 - [foodnetwork.com](https://www.foodnetwork.com/)
 - [delish.com](https://www.delish.com/)
 
 
