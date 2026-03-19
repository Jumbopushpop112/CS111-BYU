# 2024 Orbital Launches Web Scraping

## Data Scraping

We will scrape the 2024 orbital launch data from the provided URL and create a
visualization based on the scraped data.

**2024 orbital launch data**: https://space.skyrocket.de/doc_chr/lau2024.htm

You should download this page and find the `<table>` tag. There is only one
table on this page and it contains all the launch data we need.

## Graphs

You will need to create two bar graphs:

1. Number of launches per launch site, saved to a file called
   `launch_sites.output.png`
2. Number of launches per country, saved to a file called `countries.output.png`

These files should be saved in the same directory as your `orbital_launches.py`
file.

The launch site is listed in the table column labeled "Site". The launch sites
can be paired with their respective countries as follows:
![launch_site_locations](./assets/launch_site_locations.png)

This information is also included in a dictionary in your `orbital_launches.py`
file, which you can use to easily map launch sites to their respective
countries.

Keep in mind that you only need to worry about the first word in the "Site"
column, as this is what is used in the key. For example, if the "Site" column
says "Va SLC-4E", you should count it as "Va". Also, there are launch sites
listed in the table that do not exist in the key; these should be ignored in
your final count.

**Note**: You can ignore any `<th>` elements in the table beyond the first row
as they simply divide the table into months.

As a reminder, using MatPlotLib you can create a bar graph with the following
code:

```python
plt.bar(categories, y_points)
```

The `categories` in our case are the launch sites or the countries, and the
`y_points` are the number of launches per launch site/country.

{% important "Important" %}

In order to match the autograder, the `categories` should be **sorted in alphabetical order**.
As a reminder, you can use `sorted()` to sort a list in Python. If you want to sort a dictionary, 
you can convert it to a list of tuples using `my_dict.items()` and then sort it.

{% endimportant %}

## Data Comparison

You are now given these numbers for the number of orbital launches per country
in 2024:

- USA: 146
- China: 68
- Russia/Kazakhstan: 17
- New Zealand: 13
- Japan: 7
- India: 5
- Iran: 4
- Europe (France): 3
- North Korea: 1

Do you notice a discrepancy between the numbers you scraped and these numbers?
It appears that one or more launch sites are missing from the key provided. Your
task now is to identify which launch site(s) is/are missing from the key and
print those sites and their number of launches to the console:

```
<site>: <launches>
```

Each new site should go on a new line.

If we could match the missing launch sites to their respective countries, we
would get the numbers above.

## Rubric

| Grade Level   | Required standards                                                                                                                                                                                                                                                                                                                                       |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Core**      | - The launch sites bar graph is produced correctly and saved to `launch_sites.output.png`<br/> - There are no hardcoded values except for the information given in the specs                                                                                                                                                                             |
| **Advanced**  | - The countries bar graph is produced correctly and saved to `countries.output.png`<br/> - Variable and function names are clear and informative and follow a consistent style<br/> - The `launch_site_countries` dictionary is used appropriately, or another method is used that easily maps the countries to each site<br/> - There is no unused code |
| **Excellent** | - The missing launch site(s) and counts are found and printed to the console<br/> - Code is broken down into functions that follow the Single Responsibility Principle, with no large sections of duplicate code<br/> - Code is easy to read                                                                                                             |