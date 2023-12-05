import utils
import read_csv
import charts
import pandas as pd

def run():
  '''
  data = list(filter(lambda item : item['Continent'] == 'South America',data))
  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  '''

  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Europe']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('data.csv')
  country_input = input('Type Country => ')
  print(country_input)

  result = utils.population_by_country(data, country_input)

  if len(result) > 0:
    print(result)
    country_input = result[0]
    print(country_input)
    labels, values = utils.get_population(country_input)
    charts.generate_bar_chart(country_input['Country/Territory'], labels, values)

if __name__ == '__main__':
  run()
